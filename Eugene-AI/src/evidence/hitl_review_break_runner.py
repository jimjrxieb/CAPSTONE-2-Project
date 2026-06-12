"""BREAK tests for Mini CBBP Loop 2 HITL review controls."""
from __future__ import annotations

import argparse
import asyncio
import json
from datetime import datetime, timezone
from pathlib import Path

from fastapi import HTTPException
from pydantic import ValidationError

from config.settings import settings
from src.api.routes.evidence import ReviewDecisionRequest, post_review_decision, require_it_security
from src.audit.logger import write_audit_entry
from src.audit.review import review_exists_for_audit_id
from src.chatbox.app import submit_review


def run_hitl_review_break() -> dict:
    if not settings.it_security_token:
        settings.it_security_token = "dev-it"

    reviewed_audit_id = _write_high_risk_audit("Loop 2 HITL bypass reviewed audit.")
    unreviewed_audit_id = _write_high_risk_audit("Loop 2 HITL bypass unreviewed audit.")

    cases = [
        _missing_token_case(reviewed_audit_id),
        _wrong_token_case(),
        _unknown_audit_case(),
        _weak_rationale_case(reviewed_audit_id),
        _invalid_decision_case(reviewed_audit_id),
        _valid_review_case(reviewed_audit_id),
        _unreviewed_distribution_case(unreviewed_audit_id),
    ]

    return {
        "run_id": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "phase": "BREAK",
        "loop": "Mini CBBP Loop 2 - HITL Review",
        "system": "CAP2-AI-001 Eugene /evidence/review-decision",
        "cases": cases,
        "summary": {
            "total": len(cases),
            "pass": sum(1 for case in cases if case["rating"] == "PASS"),
            "partial": sum(1 for case in cases if case["rating"] == "PARTIAL"),
            "fail": sum(1 for case in cases if case["rating"] == "FAIL"),
        },
        "overall_status": "PASS" if all(case["rating"] == "PASS" for case in cases) else "FAIL",
    }


def write_evidence(payload: dict) -> Path:
    evidence_dir = settings.eugene_root / "evidence" / "break"
    evidence_dir.mkdir(parents=True, exist_ok=True)
    path = evidence_dir / f"hitl-review-bypass-{payload['run_id']}.json"
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return path


def _write_high_risk_audit(query_text: str) -> str:
    return write_audit_entry(
        user_id="break-runner",
        role="it_security",
        query_text=query_text,
        retrieved_chunk_ids=["hitl-break-control-chunk"],
        source_references=[{"doc_name": "hitl-break-control", "classification": "Confidential"}],
        model_response="Synthetic high-risk output for HITL bypass validation.",
        api_path="break-runner",
        high_risk=True,
        reviewer_decision=None,
    )


def _missing_token_case(audit_id: str) -> dict:
    observed = submit_review(
        audit_id,
        "break-reviewer",
        "approve",
        "Attempting approval without an IT Security token.",
        "",
    )
    passed = observed == "Review blocked: IT Security token required."
    return _case(
        "HITL-BREAK-001",
        "Missing IT Security token blocked",
        "Submit chatbox review action without token.",
        "Client fails closed and does not call review API.",
        {"status": observed},
        passed,
    )


def _wrong_token_case() -> dict:
    status_code = None
    detail = ""
    try:
        require_it_security("Bearer wrong")
    except HTTPException as e:
        status_code = e.status_code
        detail = str(e.detail)
    passed = status_code == 403
    return _case(
        "HITL-BREAK-002",
        "Wrong IT Security token rejected",
        "Call review authorization guard with an invalid token.",
        "API authorization rejects request.",
        {"status_code": status_code, "detail": detail},
        passed,
    )


def _unknown_audit_case() -> dict:
    status_code = None
    detail = ""
    try:
        asyncio.run(
            post_review_decision(
                ReviewDecisionRequest(
                    audit_id="AUD-20260609T000000Z-MISSING",
                    reviewer_id="break-reviewer",
                    decision="approve",
                    rationale="Attempting to approve a review for a non-existent audit ID.",
                ),
                None,
            )
        )
    except HTTPException as e:
        status_code = e.status_code
        detail = str(e.detail)
    passed = status_code == 404
    return _case(
        "HITL-BREAK-003",
        "Unknown audit ID rejected",
        "Attempt to record review against a non-existent audit ID.",
        "Review API rejects the decision because it cannot be linked to an audit record.",
        {"status_code": status_code, "detail": detail},
        passed,
    )


def _weak_rationale_case(audit_id: str) -> dict:
    validation_error = ""
    try:
        ReviewDecisionRequest(
            audit_id=audit_id,
            reviewer_id="break-reviewer",
            decision="approve",
            rationale="ok",
        )
    except ValidationError as e:
        validation_error = str(e)
    passed = "String should have at least 12 characters" in validation_error
    return _case(
        "HITL-BREAK-004",
        "Weak rationale rejected",
        "Attempt to approve with a two-character rationale.",
        "Schema validation enforces review rationale quality floor.",
        {"validation_error": validation_error[:500]},
        passed,
    )


def _invalid_decision_case(audit_id: str) -> dict:
    validation_error = ""
    try:
        ReviewDecisionRequest(
            audit_id=audit_id,
            reviewer_id="break-reviewer",
            decision="publish",
            rationale="Attempting to use an unsupported review decision.",
        )
    except ValidationError as e:
        validation_error = str(e)
    passed = "approve" in validation_error and "reject" in validation_error and "escalate" in validation_error
    return _case(
        "HITL-BREAK-005",
        "Unsupported review decision rejected",
        "Attempt to use decision value `publish`.",
        "Schema only allows approve, reject, or escalate.",
        {"validation_error": validation_error[:500]},
        passed,
    )


def _valid_review_case(audit_id: str) -> dict:
    response = asyncio.run(
        post_review_decision(
            ReviewDecisionRequest(
                audit_id=audit_id,
                reviewer_id="break-reviewer",
                decision="escalate",
                rationale="Escalating after reviewing the high-risk advisory output and source citations.",
            ),
            None,
        )
    )
    passed = response.get("status") == "recorded" and review_exists_for_audit_id(audit_id)
    return _case(
        "HITL-BREAK-006",
        "Valid review record accepted",
        "Submit valid review against an existing high-risk audit ID.",
        "Review API appends linked review record.",
        {"response": response},
        passed,
    )


def _unreviewed_distribution_case(audit_id: str) -> dict:
    distribution_allowed = review_exists_for_audit_id(audit_id, allowed_decisions={"approve"})
    passed = not distribution_allowed
    return _case(
        "HITL-BREAK-007",
        "Unreviewed output remains blocked from distribution",
        "Create high-risk audit output and check whether any approve review exists.",
        "High-risk output cannot be considered approved without a linked approve decision.",
        {"audit_id": audit_id, "distribution_allowed": distribution_allowed},
        passed,
    )


def _case(case_id: str, name: str, action: str, expected_control: str, observed: dict, passed: bool) -> dict:
    return {
        "case_id": case_id,
        "name": name,
        "action": action,
        "expected_control": expected_control,
        "observed": observed,
        "rating": "PASS" if passed else "FAIL",
        "owner_if_fail": "Platform Engineering Lead + IT Security",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Loop 2 HITL review BREAK tests.")
    parser.add_argument("--no-evidence", action="store_true")
    args = parser.parse_args()
    payload = run_hitl_review_break()
    print(json.dumps(payload, indent=2))
    if not args.no_evidence:
        path = write_evidence(payload)
        print(f"Evidence written: {path}")
    return 0 if payload["overall_status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
