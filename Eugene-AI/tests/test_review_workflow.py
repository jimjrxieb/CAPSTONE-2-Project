import json
import asyncio

import pytest
from fastapi import HTTPException

from config.settings import settings
from src.api.routes.evidence import ReviewDecisionRequest, post_review_decision, require_it_security
from src.audit.logger import write_audit_entry
from src.audit.review import ReviewDecision, write_review_decision


def test_review_decision_is_append_only(tmp_path, monkeypatch):
    review_path = tmp_path / "review-log.jsonl"
    monkeypatch.setattr(settings, "review_log_path", review_path)

    entry = write_review_decision(
        audit_id="AUD-20260609T000000Z-ABC123",
        reviewer_id="reviewer-1",
        decision=ReviewDecision.escalate,
        rationale="Escalating high-risk advisory output for final approval.",
    )

    recorded = json.loads(review_path.read_text(encoding="utf-8").strip())
    assert recorded == entry
    assert recorded["decision"] == "escalate"


def test_evidence_endpoint_requires_it_security_token(tmp_path, monkeypatch):
    monkeypatch.setattr(settings, "audit_log_path", tmp_path / "audit-log.jsonl")
    monkeypatch.setattr(settings, "review_log_path", tmp_path / "review-log.jsonl")
    monkeypatch.setattr(settings, "it_security_token", "dev-it")

    audit_id = write_audit_entry(
        user_id="chatbox",
        role="it_security",
        query_text="Who is the CISO?",
        retrieved_chunk_ids=["chunk-1"],
        source_references=[{"doc_name": "doc", "classification": "Confidential"}],
        model_response="High-risk output.",
        high_risk=True,
    )

    payload = {
        "audit_id": audit_id,
        "reviewer_id": "reviewer-1",
        "decision": "approve",
        "rationale": "Reviewed retrieved sources and approved advisory draft.",
    }

    with pytest.raises(HTTPException) as wrong_token:
        require_it_security("Bearer wrong")
    assert wrong_token.value.status_code == 403

    require_it_security("Bearer dev-it")
    accepted = asyncio.run(post_review_decision(ReviewDecisionRequest(**payload), None))
    assert accepted["status"] == "recorded"

    review_log = (tmp_path / "review-log.jsonl").read_text(encoding="utf-8")
    assert audit_id in review_log


def test_review_rejects_unknown_audit_id(tmp_path, monkeypatch):
    monkeypatch.setattr(settings, "audit_log_path", tmp_path / "audit-log.jsonl")
    monkeypatch.setattr(settings, "review_log_path", tmp_path / "review-log.jsonl")
    monkeypatch.setattr(settings, "it_security_token", "dev-it")

    with pytest.raises(HTTPException) as response:
        asyncio.run(
            post_review_decision(
                ReviewDecisionRequest(
                    audit_id="AUD-20260609T000000Z-MISSING",
                    reviewer_id="reviewer-1",
                    decision="reject",
                    rationale="Rejecting because the referenced audit item does not exist.",
                ),
                None,
            )
        )
    assert response.value.status_code == 404
