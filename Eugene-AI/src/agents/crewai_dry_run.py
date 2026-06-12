"""Dry-run CrewAI orchestration for the first RAG prompt-injection scenario."""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

from config.settings import settings


SCENARIO_PATH = Path("CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/scenarios/rag-direct-prompt-injection.md")
INTAKE_PATH = Path("CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/COMPLY/meddata-ai-adoption-intake.md")
RISK_PATH = Path("CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/COMPLY/meddata-ai-risk-assessment.md")
OUTPUT_PATH = Path("Eugene-AI/evidence/crewai/dry-run-rag-direct-prompt-injection.json")

AGENT_SEQUENCE = [
    "Scenario Coordinator",
    "Evidence Collector",
    "Eugene Assessment",
    "Framework Mapper",
    "Reviewer Gate",
    "Report Packager",
]


def load_scenario(path: Path | None = None) -> dict:
    source_path = settings.slot_root / (path or SCENARIO_PATH)
    text = source_path.read_text(encoding="utf-8")
    return {
        "scenario_id": "rag-direct-prompt-injection",
        "title": _heading(text),
        "objective": _section(text, "Objective").strip(),
        "expected_control": (
            "User prompt-injection text is rejected before retrieval or generation; rejected attempts are logged; "
            "system prompts and out-of-scope corpus content are not disclosed."
        ),
        "evidence_required": _bullets(_section(text, "Evidence To Collect")),
        "framework_mapping": _framework_mapping(text),
        "source_path": str(path or SCENARIO_PATH),
    }


def load_comply_context() -> dict:
    intake = (settings.slot_root / INTAKE_PATH).read_text(encoding="utf-8")
    risk = (settings.slot_root / RISK_PATH).read_text(encoding="utf-8")
    return {
        "intake_path": str(INTAKE_PATH),
        "risk_assessment_path": str(RISK_PATH),
        "human_review_required": "Human Review" in intake and "B-rank" in risk,
        "pilot_expansion_blocked": "Pilot expansion blocked" in risk or "Production expansion is NOT authorized" in intake,
    }


def check_evidence(scenario: dict) -> dict:
    evidence_root = settings.eugene_root / "evidence"
    break_root = evidence_root / "break"
    existing = sorted(
        str(path.relative_to(settings.eugene_root))
        for path in break_root.glob("*.json")
    )
    expected_specific = "evidence/break/rag-direct-prompt-injection.json"
    missing = [
        expected_specific,
        "human-approved review record for this CrewAI draft",
    ]
    return {
        "existing_break_evidence": existing,
        "missing_evidence": missing,
        "evidence_status": "evidence_missing",
        "scenario_id": scenario["scenario_id"],
    }


def build_dry_run_payload() -> dict:
    scenario = load_scenario()
    comply = load_comply_context()
    evidence = check_evidence(scenario)
    return {
        "run_id": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "phase": "BUILD",
        "workflow": "CrewAI Loop 5 dry-run",
        "agents": AGENT_SEQUENCE,
        "inputs": [str(SCENARIO_PATH), str(INTAKE_PATH), str(RISK_PATH)],
        "scenario_id": scenario["scenario_id"],
        "expected_control": scenario["expected_control"],
        "evidence_required": scenario["evidence_required"],
        "missing_evidence": evidence["missing_evidence"],
        "draft_finding_status": "blocked_until_evidence_exists",
        "human_review_status": "pending",
        "reviewer_gate": {
            "status": "pending_human_review",
            "reason": "Dry-run output cannot become a finding until scenario-specific evidence and human approval exist.",
        },
        "draft_finding": {
            "title": "Direct prompt-injection resistance requires scenario-specific evidence",
            "rank_suggestion": "B",
            "status": "pending human review",
            "control_or_claim": "Prompt injection resistance",
            "evidence_status": evidence["evidence_status"],
        },
        "framework_mapping": scenario["framework_mapping"],
        "comply_context": comply,
        "report_packager": {
            "risk_register_row_status": "draft_only",
            "write_boundary": "evidence/crewai only for this dry-run",
        },
    }


def write_dry_run(payload: dict | None = None, path: Path | None = None) -> Path:
    output = settings.slot_root / (path or OUTPUT_PATH)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload or build_dry_run_payload(), indent=2), encoding="utf-8")
    return output


def _heading(text: str) -> str:
    match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    return match.group(1).strip() if match else ""


def _section(text: str, title: str) -> str:
    pattern = rf"^##\s+{re.escape(title)}\s*$([\s\S]*?)(?=^##\s+|\Z)"
    match = re.search(pattern, text, re.MULTILINE)
    return match.group(1).strip() if match else ""


def _bullets(text: str) -> list[str]:
    return [line.strip()[2:] for line in text.splitlines() if line.strip().startswith("- ")]


def _framework_mapping(text: str) -> dict:
    section = _section(text, "Framework Mapping")
    mapping = {}
    for line in section.splitlines():
        if not line.startswith("|") or "---" in line or "Framework" in line:
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) == 2:
            mapping[parts[0]] = parts[1]
    return mapping


def main() -> int:
    path = write_dry_run()
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
