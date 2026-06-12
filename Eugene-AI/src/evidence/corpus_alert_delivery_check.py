"""Generate evidence that corpus alerts route to an owner and can be sent to Slack."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from config.settings import settings
from src.rag.alerts import build_slack_payload, write_corpus_alert


def run_delivery_check() -> dict:
    alert = write_corpus_alert(
        alert_type="MANIFEST_CONTRACT_VIOLATION",
        severity="HIGH",
        owner="RAG Corpus Owner",
        findings=[{"source_path": "source-documents/security/rogue.md", "reason": "UNAPPROVED_FILE_ON_DISK"}],
        action_required="Quarantine unapproved or unsigned corpus documents before ingest continues.",
    )
    slack_payload = build_slack_payload(alert)
    checks = {
        "owner_resolved": alert.get("owner_contact", {}).get("registry_status") == "resolved",
        "local_alert_log_written": Path(settings.corpus_alert_log_path).exists(),
        "slack_payload_has_channel": bool(slack_payload.get("channel")),
        "slack_payload_has_framework_tags": "LLM" in json.dumps(slack_payload) and "AML." in json.dumps(slack_payload),
        "slack_network_disabled_by_default": alert.get("delivery", {}).get("slack") == "disabled",
    }
    return {
        "run_id": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "phase": "BUILD",
        "loop": "Mini CBBP Loop 3 - Corpus Alert Delivery",
        "alert": alert,
        "slack_payload_preview": slack_payload,
        "checks": checks,
        "overall_status": "PASS" if all(checks.values()) else "FAIL",
    }


def write_evidence(payload: dict) -> Path:
    evidence_dir = settings.eugene_root / "evidence"
    evidence_dir.mkdir(parents=True, exist_ok=True)
    path = evidence_dir / f"corpus-alert-delivery-check-{payload['run_id']}.json"
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Eugene corpus alert delivery check.")
    parser.add_argument("--no-evidence", action="store_true")
    args = parser.parse_args()
    payload = run_delivery_check()
    print(json.dumps(payload, indent=2))
    if not args.no_evidence:
        path = write_evidence(payload)
        print(f"Evidence written: {path}")
    return 0 if payload["overall_status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
