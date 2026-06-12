"""Shared document, manifest, chunking, and embedding helpers for Eugene RAG."""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import requests

from config.settings import settings

_MANIFEST_PATH_RE = re.compile(r"`([^`]+\.md)`")
_CLASSIFICATION_RE = re.compile(
    r"\*\*Classification:\*\*\s*([^*\n]+)|Classification:\s*([^\n]+)",
    re.IGNORECASE,
)
_BASELINE_SECTION_RE = re.compile(
    r"## Baseline Corpus(?P<section>.*?)(?:\n## |\Z)",
    re.IGNORECASE | re.DOTALL,
)

CATEGORY_CLASSIFICATION = {
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


class ManifestViolationError(ValueError):
    pass


@dataclass(frozen=True)
class CorpusDocument:
    path: Path
    rel_path: str
    category: str
    poisoned: bool = False
    unsafe: bool = False
    classification: str = ""
    owner: str = ""
    approved_by: str = ""
    approval_date: str = ""


@dataclass(frozen=True)
class ManifestRecord:
    category: str
    file: str
    classification: str
    owner: str
    approved_by: str
    approval_date: str
    purpose: str


class OllamaEmbeddingFunction:
    """Chroma-compatible embedding function backed by local Ollama."""

    def __init__(self, url: str | None = None, model: str | None = None):
        self.url = (url or settings.ollama_endpoint).rstrip("/")
        self.model = model or settings.ollama_embed_model

    def name(self) -> str:
        return f"ollama-{self.model}"

    def __call__(self, input: list[str]) -> list[list[float]]:
        return [embed_text(text, self.url, self.model) for text in input]


def embed_text(text: str, url: str | None = None, model: str | None = None) -> list[float]:
    endpoint = (url or settings.ollama_endpoint).rstrip("/")
    embed_model = model or settings.ollama_embed_model
    response = requests.post(
        f"{endpoint}/api/embeddings",
        json={"model": embed_model, "prompt": text},
        timeout=30,
    )
    if response.status_code == 404:
        response = requests.post(
            f"{endpoint}/api/embed",
            json={"model": embed_model, "input": text},
            timeout=30,
        )
        response.raise_for_status()
        embeddings = response.json().get("embeddings", [])
        if not embeddings:
            raise RuntimeError("Ollama embed response did not include embeddings")
        return embeddings[0]
    response.raise_for_status()
    return response.json()["embedding"]


def load_manifest_entries(manifest_path: Path | None = None) -> set[str]:
    path = manifest_path or settings.corpus_manifest_path
    if not path.exists():
        raise ManifestViolationError(f"Corpus manifest not found: {path}")
    entries = set(_MANIFEST_PATH_RE.findall(path.read_text(encoding="utf-8")))
    return {
        entry
        for entry in entries
        if _is_corpus_relative_path(entry)
    }


def load_baseline_manifest_records(manifest_path: Path | None = None) -> list[ManifestRecord]:
    path = manifest_path or settings.corpus_manifest_path
    if not path.exists():
        raise ManifestViolationError(f"Corpus manifest not found: {path}")
    text = path.read_text(encoding="utf-8")
    match = _BASELINE_SECTION_RE.search(text)
    if not match:
        raise ManifestViolationError("Baseline Corpus section not found in corpus manifest")
    rows = _parse_markdown_table(match.group("section"))
    records: list[ManifestRecord] = []
    for row in rows:
        file_value = _extract_single_manifest_path(row.get("file", ""))
        if not file_value or not _is_corpus_relative_path(file_value):
            continue
        records.append(
            ManifestRecord(
                category=row.get("category", "").strip(),
                file=file_value,
                classification=row.get("classification", "").strip(),
                owner=row.get("owner", "").strip(),
                approved_by=row.get("approved by", "").strip(),
                approval_date=row.get("approval date", "").strip(),
                purpose=row.get("purpose", "").strip(),
            )
        )
    return records


def validate_baseline_manifest_contract(manifest_path: Path | None = None, corpus_root: Path | None = None) -> list[dict]:
    scan_root = corpus_root or (manifest_path.parent if manifest_path is not None else settings.corpus_data_path)
    records = load_baseline_manifest_records(manifest_path)
    findings: list[dict] = []
    seen: set[str] = set()
    for record in records:
        missing = [
            field
            for field, value in {
                "category": record.category,
                "classification": record.classification,
                "owner": record.owner,
                "approved_by": record.approved_by,
                "approval_date": record.approval_date,
                "purpose": record.purpose,
            }.items()
            if not value
        ]
        if record.file in seen:
            findings.append({"source_path": record.file, "reason": "DUPLICATE_MANIFEST_ENTRY"})
        seen.add(record.file)
        if missing:
            findings.append(
                {
                    "source_path": record.file,
                    "reason": "MISSING_MANIFEST_METADATA",
                    "missing_fields": missing,
                }
            )
        if record.classification and _classification_rank_or_none(record.classification) is None:
            findings.append(
                {
                    "source_path": record.file,
                    "reason": "INVALID_CLASSIFICATION",
                    "classification": record.classification,
                }
            )
    if not records:
        findings.append({"source_path": "corpus-manifest.md", "reason": "NO_BASELINE_RECORDS"})
    approved_files = {record.file for record in records}
    for source_path in detect_unapproved_baseline_files(corpus_root=scan_root, approved_files=approved_files):
        findings.append({"source_path": source_path, "reason": "UNAPPROVED_FILE_ON_DISK"})
    return findings


def detect_unapproved_baseline_files(
    *,
    corpus_root: Path | None = None,
    approved_files: set[str] | None = None,
) -> list[str]:
    root = corpus_root or settings.corpus_data_path
    approved = approved_files if approved_files is not None else {record.file for record in load_baseline_manifest_records()}
    candidates: list[str] = []
    for prefix in ("source-documents", "sanitized-baseline"):
        base = root / prefix
        if not base.exists():
            continue
        for path in base.rglob("*.md"):
            rel_path = path.relative_to(root).as_posix()
            if rel_path not in approved:
                candidates.append(rel_path)
    return sorted(candidates)


def collect_corpus_documents(
    *,
    include_poisoned: bool = False,
    include_unsafe: bool = False,
    corpus_root: Path | None = None,
    manifest_entries: set[str] | None = None,
) -> list[CorpusDocument]:
    root = corpus_root or settings.corpus_data_path
    allowed = manifest_entries if manifest_entries is not None else load_manifest_entries()
    baseline_records = {record.file: record for record in load_baseline_manifest_records()}
    documents: list[CorpusDocument] = []
    for rel_path in sorted(allowed):
        if rel_path.startswith("poisoned-documents/") and not include_poisoned:
            continue
        if rel_path.startswith("secrets-and-pii-samples/") and not include_unsafe:
            continue
        path = root / rel_path
        if not path.exists():
            raise ManifestViolationError(f"Manifest entry missing on disk: {rel_path}")
        record = baseline_records.get(rel_path)
        documents.append(
            CorpusDocument(
                path=path,
                rel_path=rel_path,
                category=_category_for_rel_path(rel_path),
                poisoned=rel_path.startswith("poisoned-documents/"),
                unsafe=rel_path.startswith("secrets-and-pii-samples/"),
                classification=record.classification if record else "",
                owner=record.owner if record else "",
                approved_by=record.approved_by if record else "",
                approval_date=record.approval_date if record else "",
            )
        )
    return documents


def check_manifest(doc_path: Path, *, corpus_root: Path | None = None, manifest_entries: set[str] | None = None) -> str:
    root = corpus_root or settings.corpus_data_path
    rel_path = doc_path.relative_to(root).as_posix()
    allowed = manifest_entries if manifest_entries is not None else load_manifest_entries()
    if rel_path not in allowed:
        raise ManifestViolationError(f"{rel_path} is not approved in the corpus manifest")
    return rel_path


def make_chunks(document: CorpusDocument, *, max_chars: int = 3500) -> list[dict]:
    text = document.path.read_text(encoding="utf-8")
    classification = document.classification or _infer_classification(text, document.category)
    sections = split_markdown(text, max_chars=max_chars)
    chunks: list[dict] = []
    for index, section in enumerate(sections):
        chunk_id = f"meddata::{document.category}::{document.path.stem}::chunk-{index:03d}"
        chunks.append(
            {
                "id": chunk_id,
                "text": section,
                "metadata": {
                    "corpus": "meddata-nexus",
                    "category": document.category,
                    "classification": classification,
                    "owner": document.owner,
                    "approved_by": document.approved_by,
                    "approval_date": document.approval_date,
                    "doc_name": document.path.stem,
                    "source_file": document.path.name,
                    "source_path": document.rel_path,
                    "sha256": sha256_file(document.path),
                    "chunk_id": chunk_id,
                    "chunk_index": index,
                    "chunk_count": len(sections),
                    "is_poisoned": document.poisoned,
                    "is_unsafe": document.unsafe,
                    "ingested_at": datetime.now(timezone.utc).isoformat(),
                },
            }
        )
    return chunks


def split_markdown(text: str, *, max_chars: int = 3500) -> list[str]:
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
        current_size = sum(len(item) + 1 for item in current)
        if current and (starts_new_section or current_size + len(line) > max_chars):
            flush()
        current.append(line)
    flush()
    return chunks or [text]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def _category_for_rel_path(rel_path: str) -> str:
    parts = rel_path.split("/")
    if rel_path.startswith("source-documents/") and len(parts) >= 3:
        return parts[1]
    if rel_path.startswith("sanitized-baseline/"):
        return "sanitized-baseline"
    if rel_path.startswith("poisoned-documents/"):
        return "poisoned"
    if rel_path.startswith("secrets-and-pii-samples/"):
        return "unsafe"
    return parts[0]


def _is_corpus_relative_path(entry: str) -> bool:
    valid_prefixes = (
        "source-documents/",
        "sanitized-baseline/",
        "poisoned-documents/",
        "secrets-and-pii-samples/",
    )
    return entry.startswith(valid_prefixes)


def _infer_classification(text: str, category: str) -> str:
    match = _CLASSIFICATION_RE.search(text)
    if match:
        return (match.group(1) or match.group(2)).strip("*_ ")
    return CATEGORY_CLASSIFICATION.get(category, "Internal")


def _parse_markdown_table(section: str) -> list[dict[str, str]]:
    lines = [line.strip() for line in section.splitlines() if line.strip().startswith("|")]
    if len(lines) < 3:
        return []
    headers = [_normalize_header(cell) for cell in _split_table_row(lines[0])]
    rows: list[dict[str, str]] = []
    for line in lines[2:]:
        cells = _split_table_row(line)
        if len(cells) != len(headers):
            continue
        rows.append({headers[index]: cells[index].strip() for index in range(len(headers))})
    return rows


def _split_table_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _normalize_header(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().lower())


def _extract_single_manifest_path(value: str) -> str:
    matches = _MANIFEST_PATH_RE.findall(value)
    return matches[0] if matches else ""


def _classification_rank_or_none(classification: str) -> int | None:
    normalized = classification.strip().lower().replace(" ", "-")
    known = {"public", "internal", "confidential", "restricted"}
    if normalized not in known:
        return None
    return {"public": 0, "internal": 1, "confidential": 2, "restricted": 3}[normalized]
