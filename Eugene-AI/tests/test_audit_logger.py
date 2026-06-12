import json

from config.settings import settings
import pytest

from src.audit.logger import AuditFieldError, read_validated_audit_entries, write_audit_entry


def test_audit_entry_contains_required_fields(tmp_path, monkeypatch):
    audit_path = tmp_path / "audit-log.jsonl"
    monkeypatch.setattr(settings, "audit_log_path", audit_path)

    audit_id = write_audit_entry(
        user_id="test-session",
        role="it_security",
        query_text="Who is the CISO?",
        retrieved_chunk_ids=["chunk-1"],
        source_references=[{"doc_name": "incident-response-plan-v3", "classification": "Confidential"}],
        model_response="Constant Yung",
        high_risk=True,
        reviewer_decision=None,
    )

    entry = json.loads(audit_path.read_text().strip())
    assert entry["audit_id"] == audit_id
    assert entry["prev_hash"] == ""
    assert entry["entry_hash"]
    for field in {
        "timestamp",
        "user_id",
        "role",
        "query_text",
        "retrieved_chunk_ids",
        "source_references",
        "model_response",
    }:
        assert field in entry


def test_audit_read_validation_rejects_missing_required_field(tmp_path, monkeypatch):
    audit_path = tmp_path / "audit-log.jsonl"
    monkeypatch.setattr(settings, "audit_log_path", audit_path)
    audit_path.write_text(
        json.dumps(
            {
                "audit_id": "AUD-1",
                "timestamp": "2026-06-10T00:00:00Z",
                "user_id": "u",
                "role": "it_security",
                "query_text": "q",
                "retrieved_chunk_ids": [],
                "source_references": [],
                "prev_hash": "",
                "entry_hash": "bad",
            }
        )
        + "\n",
        encoding="utf-8",
    )

    with pytest.raises(AuditFieldError, match="missing required fields"):
        read_validated_audit_entries()
