#!/usr/bin/env python3
"""
Ingest the MedData Nexus synthetic corpus into ChromaDB.

Clean baseline includes:
  - target-client/fake-data/source-documents/**/*.md
  - target-client/fake-data/sanitized-baseline/sanitized-incident-report.md

Scenario flags:
  --poisoned includes poisoned-documents/*.md with is_poisoned=true
  --unsafe includes secrets-and-pii-samples/*.md with is_unsafe=true

Usage:
  python3 evidence/ingest_meddata_to_chromadb.py --dry-run
  python3 evidence/ingest_meddata_to_chromadb.py --reset
  python3 evidence/ingest_meddata_to_chromadb.py --reset --poisoned
  python3 evidence/ingest_meddata_to_chromadb.py --reset --unsafe
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path

import chromadb
import requests
from chromadb.config import Settings

CAPSTONE2 = Path(__file__).resolve().parents[1]


def _find_repo_root(start: Path) -> Path:
    for candidate in [start, *start.parents]:
        if (candidate / "GP-MODEL-OPS").is_dir() and (candidate / "GP-SECLAB").is_dir():
            return candidate
    raise RuntimeError("Could not locate GP-copilot root containing GP-MODEL-OPS and GP-SECLAB")


REPO_ROOT = _find_repo_root(CAPSTONE2)
CHROMA_PATH = REPO_ROOT / "GP-MODEL-OPS" / "2-RagIngestion-Pipeline" / "05-ragged-data" / "chroma"
REPORT_DIR = CAPSTONE2 / "evidence"
FAKE_DATA = CAPSTONE2 / "target-client" / "fake-data"

SOURCE_DOCS_DIR = FAKE_DATA / "source-documents"
SANITIZED_DIR = FAKE_DATA / "sanitized-baseline"
POISONED_DOCS_DIR = FAKE_DATA / "poisoned-documents"
UNSAFE_DOCS_DIR = FAKE_DATA / "secrets-and-pii-samples"

COLLECTION_NAME = "eugene-meddata-nexus"
EMBED_MODEL = "nomic-embed-text:latest"
EMBED_DIM = 768
OLLAMA_URL = "http://localhost:11434"

_CATEGORY_CLASSIFICATION = {
    "policies": "Internal",
    "compliance": "Confidential",
    "security": "Confidential",
    "legal-contracts": "Confidential",
    "healthcare-privacy": "Restricted",
    "vendor-risk": "Confidential",
    "ai-governance": "Internal",
    "sanitized-baseline": "Confidential",
    "poisoned": "POISONED-TEST-ONLY",
    "unsafe": "UNSAFE-TEST-ONLY",
}

_CLASSIFICATION_RE = re.compile(
    r"\*\*Classification:\*\*\s*([^*\n]+)|Classification:\s*([^\n]+)",
    re.IGNORECASE,
)


class OllamaEmbeddingFunction:
    def __init__(self, url: str = OLLAMA_URL, model: str = EMBED_MODEL):
        self.url = url.rstrip("/")
        self.model = model

    def name(self) -> str:
        return f"ollama-{self.model}"

    def __call__(self, input: list[str]) -> list[list[float]]:
        return [_embed_or_raise(t, self.url, self.model) for t in input]


def _embed_or_raise(text: str, url: str, model: str) -> list[float]:
    r = requests.post(
        f"{url}/api/embeddings",
        json={"model": model, "prompt": text},
        timeout=30,
    )
    r.raise_for_status()
    v = r.json()["embedding"]
    if len(v) != EMBED_DIM:
        raise RuntimeError(f"expected {EMBED_DIM} dims, got {len(v)} from {model}")
    return v


def embed_with_retry(text: str, retries: int = 2, delay: float = 1.0) -> list[float] | None:
    for attempt in range(retries):
        try:
            return _embed_or_raise(text, OLLAMA_URL, EMBED_MODEL)
        except Exception as exc:
            if attempt == retries - 1:
                print(f"  EMBED FAIL: {exc}")
                return None
            time.sleep(delay)
    return None


def _infer_classification(text: str, category: str) -> str:
    match = _CLASSIFICATION_RE.search(text)
    if match:
        return (match.group(1) or match.group(2)).strip("*_ ")
    return _CATEGORY_CLASSIFICATION.get(category, "Internal")


def _split_markdown(text: str, max_chars: int = 3500) -> list[str]:
    """Split Markdown into heading-aware chunks with bounded size."""
    lines = text.splitlines()
    chunks: list[str] = []
    current: list[str] = []

    def flush() -> None:
        if current:
            chunk = "\n".join(current).strip()
            if len(chunk) >= 40:
                chunks.append(chunk)
            current.clear()

    for line in lines:
        starts_new_section = line.startswith("## ") or line.startswith("### ")
        would_overflow = sum(len(x) + 1 for x in current) + len(line) > max_chars
        if current and (starts_new_section or would_overflow):
            flush()
        current.append(line)
    flush()

    return chunks or [text]


def _make_chunks(path: Path, category: str, *, poisoned: bool = False, unsafe: bool = False) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(CAPSTONE2)
    classification = _infer_classification(text, category)
    sections = _split_markdown(text)
    chunks = []
    for index, section in enumerate(sections):
        chunks.append({
            "id": f"meddata::{category}::{path.stem}::chunk-{index:03d}",
            "text": section,
            "metadata": {
                "corpus": "meddata-nexus",
                "category": category,
                "classification": classification,
                "doc_name": path.stem,
                "source_file": path.name,
                "source_path": str(rel),
                "chunk_index": index,
                "chunk_count": len(sections),
                "is_poisoned": poisoned,
                "is_unsafe": unsafe,
                "ingested_at": datetime.now().isoformat(),
            },
        })
    return chunks


def collect_chunks(include_poisoned: bool, include_unsafe: bool) -> list[dict]:
    chunks: list[dict] = []

    for path in sorted(SOURCE_DOCS_DIR.rglob("*.md")):
        if not path.name.startswith("."):
            chunks.extend(_make_chunks(path, path.parent.name))

    for path in sorted(SANITIZED_DIR.glob("*.md")):
        if not path.name.startswith("."):
            chunks.extend(_make_chunks(path, "sanitized-baseline"))

    if include_poisoned:
        for path in sorted(POISONED_DOCS_DIR.glob("*.md")):
            if not path.name.startswith("."):
                chunks.extend(_make_chunks(path, "poisoned", poisoned=True))

    if include_unsafe:
        for path in sorted(UNSAFE_DOCS_DIR.glob("*.md")):
            if not path.name.startswith("."):
                chunks.extend(_make_chunks(path, "unsafe", unsafe=True))

    return chunks


def reject_stubs(chunks: list[dict]) -> None:
    for chunk in chunks:
        text = chunk["text"]
        if len(text.strip()) < 40:
            raise SystemExit(f"REFUSING TO INGEST short document: {chunk['id']}")
        for marker in ("TBD.", "TBD\n", "[PLACEHOLDER]", "[TODO]"):
            if marker in text:
                raise SystemExit(f"REFUSING TO INGEST stub marker {marker!r} in {chunk['id']}")


def write_report(collection, chunks: list[dict], inserted: int, failed: int, reset: bool, args) -> Path:
    timestamp = datetime.now().strftime("%Y%m%dT%H%M%S")
    label = "clean"
    if args.poisoned:
        label += "-poisoned"
    if args.unsafe:
        label += "-unsafe"
    out = REPORT_DIR / f"meddata-ingest-{label}-{timestamp}.md"

    by_category: dict[str, int] = {}
    for chunk in chunks:
        category = chunk["metadata"]["category"]
        by_category[category] = by_category.get(category, 0) + 1

    lines = [
        "# MedData Nexus Ingestion Evidence",
        "",
        f"**Timestamp:** {datetime.now().isoformat(timespec='seconds')}",
        f"**Collection:** `{COLLECTION_NAME}`",
        f"**Reset:** {reset}",
        f"**Poisoned included:** {args.poisoned}",
        f"**Unsafe included:** {args.unsafe}",
        f"**Inserted:** {inserted}",
        f"**Failed:** {failed}",
        f"**Final collection count:** {collection.count()}",
        "",
        "## Category Breakdown",
        "",
        "| Category | Documents |",
        "|---|---:|",
    ]
    for category, count in sorted(by_category.items()):
        lines.append(f"| {category} | {count} |")
    lines.extend([
        "",
        "## Notes",
        "",
        "- Clean baseline includes source documents plus sanitized incident report.",
        "- Poisoned and unsafe documents are scenario-only and explicitly flagged in metadata.",
        "- `expected-retrieval/golden-questions.md` is not ingested.",
    ])
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Ingest MedData Nexus synthetic corpus into ChromaDB.")
    parser.add_argument("--dry-run", action="store_true", help="parse and validate files without writing ChromaDB")
    parser.add_argument("--reset", action="store_true", help="delete and recreate eugene-meddata-nexus collection")
    parser.add_argument("--poisoned", action="store_true", help="include poisoned-documents scenario files")
    parser.add_argument("--unsafe", action="store_true", help="include secrets-and-pii-samples scenario files")
    parser.add_argument("--no-report", action="store_true", help="skip writing ingest evidence report")
    args = parser.parse_args()

    chunks = collect_chunks(args.poisoned, args.unsafe)
    reject_stubs(chunks)

    print(f"Corpus files: {len(chunks)}")
    for chunk in chunks:
        meta = chunk["metadata"]
        flags = []
        if meta["is_poisoned"]:
            flags.append("poisoned")
        if meta["is_unsafe"]:
            flags.append("unsafe")
        print(f"  {chunk['id']} [{meta['classification']}] {' '.join(flags)}")

    if args.dry_run:
        print("\n[dry-run] No ChromaDB writes performed.")
        return 0

    client = chromadb.PersistentClient(
        path=str(CHROMA_PATH),
        settings=Settings(anonymized_telemetry=False, allow_reset=True),
    )
    if args.reset and any(c.name == COLLECTION_NAME for c in client.list_collections()):
        print(f"\nDeleting existing collection: {COLLECTION_NAME}")
        client.delete_collection(COLLECTION_NAME)

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=OllamaEmbeddingFunction(),
        metadata={"corpus": "meddata-nexus", "embed_model": EMBED_MODEL, "embed_dim": EMBED_DIM},
    )

    existing = set(collection.get(include=[])["ids"])
    inserted = 0
    failed = 0
    for chunk in chunks:
        if chunk["id"] in existing:
            continue
        embedding = embed_with_retry(chunk["text"])
        if embedding is None:
            failed += 1
            continue
        collection.add(
            ids=[chunk["id"]],
            documents=[chunk["text"]],
            embeddings=[embedding],
            metadatas=[chunk["metadata"]],
        )
        inserted += 1

    print(f"\nDone. inserted={inserted} failed={failed} total={collection.count()}")
    if not args.no_report:
        report = write_report(collection, chunks, inserted, failed, args.reset, args)
        print(f"Evidence report: {report.relative_to(CAPSTONE2)}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
