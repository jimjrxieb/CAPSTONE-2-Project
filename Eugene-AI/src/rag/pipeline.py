"""Manifest-gated ingestion pipeline for Eugene's MedData Nexus corpus."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import chromadb
from chromadb.config import Settings as ChromaSettings

from config.settings import settings
from src.guardrails.phi_scanner import PHIDetectedError, scan_document as scan_phi
from src.guardrails.secret_scanner import SecretDetectedError, scan_document as scan_secrets
from src.rag.alerts import write_corpus_alert
from src.rag.sanitizer import InjectionDetectedError, scan_document_for_injection
from src.rag.document_store import (
    OllamaEmbeddingFunction,
    collect_corpus_documents,
    load_manifest_entries,
    make_chunks,
    validate_baseline_manifest_contract,
)


def ingest_corpus(*, reset: bool = False, include_poisoned: bool = False, include_unsafe: bool = False, dry_run: bool = False) -> dict:
    manifest_alerts = validate_baseline_manifest_contract()
    manifest_entries = load_manifest_entries()
    documents = collect_corpus_documents(
        include_poisoned=include_poisoned,
        include_unsafe=include_unsafe,
        manifest_entries=manifest_entries,
    )
    accepted_chunks: list[dict] = []
    rejected: list[dict] = []
    for document in documents:
        content = document.path.read_text(encoding="utf-8")
        try:
            scan_document_for_injection(content, document.rel_path)
            scan_secrets(content, document.rel_path)
            scan_phi(content, document.rel_path)
        except (InjectionDetectedError, SecretDetectedError, PHIDetectedError) as exc:
            rejected.append({"source_path": document.rel_path, "reason": exc.__class__.__name__})
            continue
        accepted_chunks.extend(make_chunks(document))

    summary = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "collection": settings.chroma_collection,
        "reset": reset,
        "include_poisoned": include_poisoned,
        "include_unsafe": include_unsafe,
        "manifest_alerts": manifest_alerts,
        "documents_seen": len(documents),
        "chunks_ready": len(accepted_chunks),
        "rejected": rejected,
        "dry_run": dry_run,
    }
    if manifest_alerts:
        summary["corpus_alert"] = write_corpus_alert(
            alert_type="MANIFEST_CONTRACT_VIOLATION",
            severity="HIGH",
            owner="RAG Corpus Owner",
            findings=manifest_alerts,
            action_required="Quarantine unapproved or unsigned corpus documents before ingest continues.",
        )
        summary["ingest_blocked"] = True
        return summary
    summary["ingest_blocked"] = False
    if rejected:
        summary["corpus_alert"] = write_corpus_alert(
            alert_type="UNSAFE_DOCUMENT_REJECTED",
            severity="HIGH",
            owner="RAG Corpus Owner",
            findings=rejected,
            action_required="Remove, sanitize, or formally approve rejected documents before ingest.",
        )
    if dry_run:
        return summary

    settings.chroma_persist_path.mkdir(parents=True, exist_ok=True)
    client = chromadb.PersistentClient(
        path=str(settings.chroma_persist_path),
        settings=ChromaSettings(anonymized_telemetry=False, allow_reset=True),
    )
    if reset and any(c.name == settings.chroma_collection for c in client.list_collections()):
        client.delete_collection(settings.chroma_collection)
    collection = client.get_or_create_collection(
        name=settings.chroma_collection,
        embedding_function=OllamaEmbeddingFunction(),
        metadata={"corpus": "meddata-nexus", "embed_model": settings.ollama_embed_model},
    )
    existing = set(collection.get(include=[])["ids"])
    inserted = 0
    for chunk in accepted_chunks:
        if chunk["id"] in existing:
            continue
        collection.add(
            ids=[chunk["id"]],
            documents=[chunk["text"]],
            metadatas=[chunk["metadata"]],
        )
        inserted += 1
    summary["inserted"] = inserted
    summary["collection_count"] = collection.count()
    return summary


def write_evidence(summary: dict) -> Path:
    evidence_dir = settings.eugene_root / "evidence"
    evidence_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = evidence_dir / f"ingest-{timestamp}.json"
    path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return path


def _main() -> int:
    parser = argparse.ArgumentParser(description="Ingest manifest-approved MedData Nexus documents.")
    parser.add_argument("--reset", action="store_true")
    parser.add_argument("--poisoned", action="store_true")
    parser.add_argument("--unsafe", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-evidence", action="store_true")
    args = parser.parse_args()
    summary = ingest_corpus(
        reset=args.reset,
        include_poisoned=args.poisoned,
        include_unsafe=args.unsafe,
        dry_run=args.dry_run,
    )
    print(json.dumps(summary, indent=2))
    if not args.no_evidence:
        path = write_evidence(summary)
        print(f"Evidence written: {path}")
    return 0 if not summary["rejected"] and not summary.get("manifest_alerts") else 1


if __name__ == "__main__":
    raise SystemExit(_main())
