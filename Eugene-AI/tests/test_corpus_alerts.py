import json

from config.settings import settings
from src.rag.alerts import build_slack_payload, resolve_corpus_owner, write_corpus_alert


def test_corpus_alert_resolves_owner_and_writes_local_log(tmp_path, monkeypatch):
    registry = tmp_path / "owners.json"
    registry.write_text(
        json.dumps(
            {
                "RAG Corpus Owner": {
                    "name": "RAG Corpus Owner",
                    "email": "owner@example.invalid",
                    "slack_channel": "#rag-corpus-alerts",
                }
            }
        ),
        encoding="utf-8",
    )
    alert_log = tmp_path / "corpus-alert-log.jsonl"
    monkeypatch.setattr(settings, "corpus_owner_registry_path", registry)
    monkeypatch.setattr(settings, "corpus_alert_log_path", alert_log)
    monkeypatch.setattr(settings, "slack_alerts_enabled", False)

    alert = write_corpus_alert(
        alert_type="MANIFEST_CONTRACT_VIOLATION",
        severity="HIGH",
        owner="RAG Corpus Owner",
        findings=[{"source_path": "source-documents/security/rogue.md", "reason": "UNAPPROVED_FILE_ON_DISK"}],
        action_required="Quarantine the document.",
    )

    assert alert["owner_contact"]["slack_channel"] == "#rag-corpus-alerts"
    assert alert["delivery"]["slack"] == "disabled"
    assert json.loads(alert_log.read_text(encoding="utf-8").strip())["alert_id"] == alert["alert_id"]


def test_slack_payload_includes_framework_tags(tmp_path, monkeypatch):
    monkeypatch.setattr(settings, "corpus_owner_registry_path", tmp_path / "missing.json")
    alert = {
        "alert_id": "CORPUS-1",
        "severity": "HIGH",
        "alert_type": "UNSAFE_DOCUMENT_REJECTED",
        "owner": "RAG Corpus Owner",
        "owner_contact": {"slack_channel": "#rag-corpus-alerts"},
        "findings": [{"source_path": "poisoned.md", "reason": "InjectionDetectedError"}],
        "action_required": "Remove the document.",
        "framework_tags": {
            "owasp_llm": ["LLM04 Data and Model Poisoning"],
            "nist_ai_rmf": ["MANAGE 2.3"],
            "mitre_atlas": ["AML.T0051 Prompt Injection"],
        },
    }
    payload = build_slack_payload(alert)
    assert payload["channel"] == "#rag-corpus-alerts"
    assert "LLM04" in payload["blocks"][1]["elements"][0]["text"]
    assert "AML.T0051" in payload["blocks"][1]["elements"][0]["text"]


def test_resolve_corpus_owner_reports_missing_registry(tmp_path, monkeypatch):
    monkeypatch.setattr(settings, "corpus_owner_registry_path", tmp_path / "missing.json")
    owner = resolve_corpus_owner("RAG Corpus Owner")
    assert owner["registry_status"] == "missing"
