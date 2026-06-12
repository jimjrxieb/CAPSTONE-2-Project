"""Corpus-owner alert records for RAG ingest control failures."""
from __future__ import annotations

import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

import requests

from config.settings import settings


DEFAULT_FRAMEWORK_TAGS = {
    "owasp_llm": [
        "LLM01 Prompt Injection",
        "LLM02 Sensitive Information Disclosure",
        "LLM04 Data and Model Poisoning",
        "LLM08 Vector and Embedding Weaknesses",
    ],
    "nist_ai_rmf": ["MAP 3.2", "MEASURE 2.7", "MANAGE 2.3", "GOVERN 1.5"],
    "mitre_atlas": ["AML.T0024.000 Exfiltration via Retrieval", "AML.T0051 Prompt Injection"],
}


def write_corpus_alert(
    *,
    alert_type: str,
    severity: str,
    owner: str,
    findings: list[dict],
    action_required: str,
    framework_tags: dict | None = None,
) -> dict:
    owner_record = resolve_corpus_owner(owner)
    alert = {
        "alert_id": f"CORPUS-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}-{uuid.uuid4().hex[:6].upper()}",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "alert_type": alert_type,
        "severity": severity,
        "owner": owner,
        "owner_contact": owner_record,
        "findings": findings,
        "action_required": action_required,
        "framework_tags": framework_tags or DEFAULT_FRAMEWORK_TAGS,
        "delivery": {"local_log": "written", "slack": "disabled"},
    }
    log_path = Path(settings.corpus_alert_log_path)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(alert) + "\n")
    if settings.slack_alerts_enabled:
        alert["delivery"]["slack"] = send_slack_alert(alert)
    return alert


def resolve_corpus_owner(owner: str) -> dict:
    registry_path = Path(settings.corpus_owner_registry_path)
    if not registry_path.exists():
        return {"name": owner, "slack_channel": "", "email": "", "registry_status": "missing"}
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    record = registry.get(owner, {"name": owner, "slack_channel": "", "email": ""})
    record["registry_status"] = "resolved" if owner in registry else "not_found"
    return record


def build_slack_payload(alert: dict) -> dict:
    owner_contact = alert.get("owner_contact", {})
    source_paths = ", ".join(item.get("source_path", "unknown") for item in alert.get("findings", [])[:5])
    owasp = ", ".join(alert.get("framework_tags", {}).get("owasp_llm", []))
    ai_rmf = ", ".join(alert.get("framework_tags", {}).get("nist_ai_rmf", []))
    atlas = ", ".join(alert.get("framework_tags", {}).get("mitre_atlas", []))
    return {
        "channel": owner_contact.get("slack_channel", "#rag-corpus-alerts"),
        "username": "Eugene Corpus Guard",
        "text": f"{alert.get('severity')} corpus alert: {alert.get('alert_type')} ({alert.get('alert_id')})",
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": (
                        f"*{alert.get('severity')} Eugene corpus alert*\n"
                        f"*Type:* {alert.get('alert_type')}\n"
                        f"*Owner:* {alert.get('owner')} ({owner_contact.get('slack_channel', 'no channel')})\n"
                        f"*Sources:* {source_paths}\n"
                        f"*Action:* {alert.get('action_required')}"
                    ),
                },
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": f"*OWASP:* {owasp} | *AI RMF:* {ai_rmf} | *ATLAS:* {atlas}",
                    }
                ],
            },
        ],
    }


def send_slack_alert(alert: dict) -> str:
    if not settings.slack_webhook_url:
        return "skipped_no_webhook"
    response = requests.post(settings.slack_webhook_url, json=build_slack_payload(alert), timeout=10)
    response.raise_for_status()
    return "sent"
