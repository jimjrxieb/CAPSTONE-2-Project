"""Generate Sprint 1 live RAG evidence using ChromaDB and Ollama embeddings."""
from __future__ import annotations

import argparse
import asyncio
import json
from datetime import datetime, timezone
from pathlib import Path

from config.settings import settings
from src.api.auth import AuthContext
from src.api.routes.query import QueryRequest, handle_query
from src.rag.retriever import retrieve

LIVE_QUERIES = [
    {
        "id": "LR-001",
        "role": "it_security",
        "query": "Who is the CISO at MedData Nexus?",
        "expect_any_category": ["security", "compliance", "ai-governance"],
        "forbid_categories": [],
    },
    {
        "id": "LR-002",
        "role": "vendor_risk_reviewer",
        "query": "What security incidents and HIPAA response steps are documented?",
        "expect_any_category": [],
        "forbid_categories": ["security", "healthcare-privacy", "compliance", "legal-contracts"],
    },
    {
        "id": "LR-003",
        "role": "compliance_analyst",
        "query": "What is the data classification tier for PHI?",
        "expect_any_category": ["policies", "compliance", "ai-governance"],
        "forbid_categories": ["healthcare-privacy", "security"],
    },
]


def run_live_retrieval_checks() -> dict:
    retrieval_results = []
    for item in LIVE_QUERIES:
        chunks = retrieve(item["query"], item["role"], top_k=5)
        categories = [chunk.get("category", "") for chunk in chunks]
        forbidden_seen = sorted(set(categories).intersection(item["forbid_categories"]))
        expected_ok = True
        if item["expect_any_category"]:
            expected_ok = bool(set(categories).intersection(item["expect_any_category"]))
        retrieval_results.append(
            {
                "id": item["id"],
                "role": item["role"],
                "query": item["query"],
                "retrieved_count": len(chunks),
                "categories": categories,
                "chunk_ids": [chunk.get("id", "") for chunk in chunks],
                "forbidden_seen": forbidden_seen,
                "pass": expected_ok and not forbidden_seen,
            }
        )
    return {
        "checks": retrieval_results,
        "pass": all(item["pass"] for item in retrieval_results),
    }


async def run_api_query_check() -> dict:
    req = QueryRequest(
        query="Who is the CISO at MedData Nexus?",
        session_id="sprint1-live-rag-check",
    )
    response = await handle_query(req, AuthContext(user_id="live-check:it_security", role="it_security"))
    return {
        "response_preview": response.response[:300],
        "source_count": len(response.sources),
        "sources": response.sources,
        "audit_id": response.audit_id,
        "high_risk": response.high_risk,
        "review_required": response.review_required,
        "pass": response.audit_id.startswith("AUD-") and response.high_risk and response.review_required,
    }


async def run_live_check() -> dict:
    retrieval = run_live_retrieval_checks()
    api_query = await run_api_query_check()
    return {
        "run_id": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "phase": "BUILD",
        "sprint": "Sprint 1",
        "collection": settings.chroma_collection,
        "chroma_persist_path": str(settings.chroma_persist_path),
        "retrieval": retrieval,
        "api_query": api_query,
        "overall_status": "PASS" if retrieval["pass"] and api_query["pass"] else "FAIL",
    }


def write_evidence(payload: dict) -> Path:
    evidence_dir = settings.eugene_root / "evidence"
    evidence_dir.mkdir(parents=True, exist_ok=True)
    path = evidence_dir / f"sprint1-live-rag-check-{payload['run_id']}.json"
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Run live Sprint 1 RAG checks.")
    parser.add_argument("--no-evidence", action="store_true")
    args = parser.parse_args()
    payload = asyncio.run(run_live_check())
    print(json.dumps(payload, indent=2))
    if not args.no_evidence:
        path = write_evidence(payload)
        print(f"Evidence written: {path}")
    return 0 if payload["overall_status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
