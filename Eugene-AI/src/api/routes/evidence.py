"""GET /evidence/* — audit log and corpus manifest endpoints. IT Security token required."""
from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field

from config.settings import settings
from src.api.auth import require_it_security
from src.audit.logger import AuditFieldError, read_validated_audit_entries
from src.audit.review import ReviewDecision, audit_id_exists, read_review_decisions, write_review_decision

router = APIRouter()


class ReviewDecisionRequest(BaseModel):
    audit_id: str = Field(min_length=8)
    reviewer_id: str = Field(min_length=2)
    decision: ReviewDecision
    rationale: str = Field(min_length=12, max_length=1000)


@router.get("/audit-log")
async def get_audit_log(
    limit: int = 50,
    _: None = Depends(require_it_security),
) -> dict:
    log_path = Path(settings.audit_log_path)
    if not log_path.exists():
        return {"entries": [], "total": 0}
    try:
        all_entries = read_validated_audit_entries()
    except AuditFieldError as e:
        raise HTTPException(status_code=500, detail=f"Audit log validation failed: {e}")
    return {"entries": all_entries[-limit:], "total": len(all_entries)}


@router.get("/corpus-manifest")
async def get_corpus_manifest(_: None = Depends(require_it_security)) -> dict:
    manifest_path = Path(settings.corpus_manifest_path)
    if not manifest_path.exists():
        raise HTTPException(status_code=404, detail="Corpus manifest not found")
    return {"manifest": manifest_path.read_text(), "path": str(manifest_path)}


@router.post("/review-decision")
async def post_review_decision(
    req: ReviewDecisionRequest,
    _: None = Depends(require_it_security),
) -> dict:
    if not audit_id_exists(req.audit_id):
        raise HTTPException(status_code=404, detail="Audit ID not found")
    entry = write_review_decision(
        audit_id=req.audit_id,
        reviewer_id=req.reviewer_id,
        decision=req.decision,
        rationale=req.rationale,
    )
    return {"status": "recorded", "review": entry}


@router.get("/review-decisions")
async def get_review_decisions(
    limit: int = 50,
    _: None = Depends(require_it_security),
) -> dict:
    entries = read_review_decisions(limit=limit)
    return {"entries": entries, "total": len(entries)}
