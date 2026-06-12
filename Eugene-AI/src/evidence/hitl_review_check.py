"""Generate BUILD Loop 2 evidence for HITL review record controls."""
from __future__ import annotations

import argparse
import asyncio
import json
from datetime import datetime, timezone
from pathlib import Path

from config.settings import settings
from src.api.routes.evidence import ReviewDecisionRequest, post_review_decision, require_it_security
from src.audit.logger import write_audit_entry


def run_hitl_review_check() -> dict:
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    if not settings.it_security_token:
        settings.it_security_token = "dev-it"

    audit_id = write_audit_entry(
        user_id="evidence-runner",
        role="it_security",
        query_text="Loop 2 HITL evidence control check.",
        retrieved_chunk_ids=["evidence-control-chunk"],
        source_references=[{"doc_name": "loop2-control-check", "classification": "Confidential"}],
        model_response="Synthetic high-risk advisory output for HITL evidence verification.",
        api_path="evidence-runner",
        high_risk=True,
        reviewer_decision=None,
    )

    checks = {
        "wrong_token_rejected": False,
        "correct_token_accepted": False,
        "review_record_written": False,
        "review_links_to_existing_audit_id": False,
    }

    try:
        require_it_security("Bearer wrong")
    except Exception:
        checks["wrong_token_rejected"] = True

    require_it_security(f"Bearer {settings.it_security_token}")
    review_payload = ReviewDecisionRequest(
        audit_id=audit_id,
        reviewer_id="loop2-reviewer",
        decision="escalate",
        rationale="Escalating this high-risk output as part of Loop 2 HITL control verification.",
    )
    review_response = asyncio.run(post_review_decision(review_payload, None))
    checks["correct_token_accepted"] = review_response.get("status") == "recorded"

    review_log_path = Path(settings.review_log_path)
    review_log = review_log_path.read_text(encoding="utf-8") if review_log_path.exists() else ""
    checks["review_record_written"] = "loop2-reviewer" in review_log
    checks["review_links_to_existing_audit_id"] = audit_id in review_log

    return {
        "run_id": run_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "phase": "BUILD",
        "loop": "Mini CBBP Loop 2 - HITL Review Record",
        "audit_id": audit_id,
        "review_log_path": str(settings.review_log_path),
        "checks": checks,
        "overall_status": "PASS" if all(checks.values()) else "FAIL",
    }


def write_evidence(payload: dict) -> Path:
    evidence_dir = settings.eugene_root / "evidence"
    evidence_dir.mkdir(parents=True, exist_ok=True)
    path = evidence_dir / f"hitl-review-check-{payload['run_id']}.json"
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Eugene HITL review BUILD checks.")
    parser.add_argument("--no-evidence", action="store_true")
    args = parser.parse_args()
    payload = run_hitl_review_check()
    print(json.dumps(payload, indent=2))
    if not args.no_evidence:
        path = write_evidence(payload)
        print(f"Evidence written: {path}")
    return 0 if payload["overall_status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
