"""Append-only HITL review records for Eugene audit items."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path

from config.settings import settings


class ReviewDecision(str, Enum):
    approve = "approve"
    reject = "reject"
    escalate = "escalate"


def audit_id_exists(audit_id: str) -> bool:
    log_path = Path(settings.audit_log_path)
    if not log_path.exists():
        return False
    for line in log_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            if json.loads(line).get("audit_id") == audit_id:
                return True
        except json.JSONDecodeError:
            continue
    return False


def write_review_decision(
    *,
    audit_id: str,
    reviewer_id: str,
    decision: ReviewDecision,
    rationale: str,
) -> dict:
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "audit_id": audit_id,
        "reviewer_id": reviewer_id,
        "decision": decision.value,
        "rationale": rationale.strip(),
    }
    log_path = Path(settings.review_log_path)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
    return entry


def read_review_decisions(limit: int = 50) -> list[dict]:
    log_path = Path(settings.review_log_path)
    if not log_path.exists():
        return []
    entries = []
    for line in log_path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            entries.append(json.loads(line))
    return entries[-limit:]


def review_exists_for_audit_id(audit_id: str, allowed_decisions: set[str] | None = None) -> bool:
    log_path = Path(settings.review_log_path)
    if not log_path.exists():
        return False
    for line in log_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        entry = json.loads(line)
        if entry.get("audit_id") != audit_id:
            continue
        if allowed_decisions is None or entry.get("decision") in allowed_decisions:
            return True
    return False
