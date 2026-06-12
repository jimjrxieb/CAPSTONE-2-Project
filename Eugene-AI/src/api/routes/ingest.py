"""POST /ingest — admin-gated corpus ingestion."""
from __future__ import annotations

from fastapi import APIRouter, Depends, Header, HTTPException
from pydantic import BaseModel

from config.settings import settings
from src.rag.pipeline import ingest_corpus, write_evidence

router = APIRouter()


class IngestRequest(BaseModel):
    reset: bool = False
    poisoned: bool = False
    unsafe: bool = False
    dry_run: bool = False


def require_admin(authorization: str = Header(...)) -> None:
    token = authorization.removeprefix("Bearer ").strip()
    if token != settings.admin_token:
        raise HTTPException(status_code=403, detail="Admin token required")


@router.post("")
async def ingest(req: IngestRequest, _: None = Depends(require_admin)) -> dict:
    summary = ingest_corpus(
        reset=req.reset,
        include_poisoned=req.poisoned,
        include_unsafe=req.unsafe,
        dry_run=req.dry_run,
    )
    evidence_path = write_evidence(summary)
    summary["evidence_path"] = str(evidence_path)
    return summary


@router.get("/status")
async def ingest_status(_: None = Depends(require_admin)) -> dict:
    return {
        "collection": settings.chroma_collection,
        "chroma_persist_path": str(settings.chroma_persist_path),
        "manifest_path": str(settings.corpus_manifest_path),
    }
