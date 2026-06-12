"""Structured JSONL audit logger with hash-chain tamper evidence. Implements F-005.

Append-only by convention. Read-time validation verifies required fields and
prev_hash/entry_hash linkage so PROVE can reject incomplete or edited entries.
"""
from __future__ import annotations

import hashlib
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

from config.settings import settings

REQUIRED_FIELDS = {
    "timestamp",
    "user_id",
    "role",
    "query_text",
    "retrieved_chunk_ids",
    "source_references",
    "model_response",
}


class AuditFieldError(ValueError):
    pass


def _canonical_json(entry: dict) -> str:
    return json.dumps(entry, sort_keys=True, separators=(",", ":"))


def _hash_entry(entry: dict) -> str:
    material = {k: v for k, v in entry.items() if k != "entry_hash"}
    return hashlib.sha256(_canonical_json(material).encode("utf-8")).hexdigest()


def _last_entry_hash(log_path: Path) -> str:
    if not log_path.exists():
        return ""
    lines = [line for line in log_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if not lines:
        return ""
    return str(json.loads(lines[-1]).get("entry_hash", ""))


def write_audit_entry(
    *,
    user_id: str,
    role: str,
    query_text: str,
    retrieved_chunk_ids: list[str],
    source_references: list[dict],
    model_response: str,
    api_path: str = "internal",
    high_risk: bool = False,
    reviewer_decision: str | None = None,
) -> str:
    """Write one audit entry. Returns the audit_id."""
    audit_id = f"AUD-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}-{uuid.uuid4().hex[:6].upper()}"
    entry = {
        "audit_id": audit_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "user_id": user_id,
        "role": role,
        "query_text": query_text,
        "retrieved_chunk_ids": retrieved_chunk_ids,
        "source_references": source_references,
        "model_response": model_response,
        "api_path": api_path,
        "high_risk": high_risk,
        "reviewer_decision": reviewer_decision,
    }

    missing = REQUIRED_FIELDS - set(entry.keys())
    if missing:
        raise AuditFieldError(f"Missing required audit fields: {missing}")

    log_path = Path(settings.audit_log_path)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    entry["prev_hash"] = _last_entry_hash(log_path)
    entry["entry_hash"] = _hash_entry(entry)
    with log_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")

    return audit_id


def read_validated_audit_entries(limit: int | None = None) -> list[dict]:
    log_path = Path(settings.audit_log_path)
    if not log_path.exists():
        return []
    entries: list[dict] = []
    previous_hash = ""
    for line_no, line in enumerate(log_path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        entry = json.loads(line)
        missing = REQUIRED_FIELDS - set(entry.keys())
        if missing:
            raise AuditFieldError(f"Audit entry line {line_no} missing required fields: {sorted(missing)}")
        if entry.get("prev_hash", "") != previous_hash:
            raise AuditFieldError(f"Audit hash chain broken at line {line_no}")
        expected_hash = _hash_entry(entry)
        if entry.get("entry_hash") != expected_hash:
            raise AuditFieldError(f"Audit entry hash mismatch at line {line_no}")
        previous_hash = str(entry["entry_hash"])
        entries.append(entry)
    return entries[-limit:] if limit else entries
