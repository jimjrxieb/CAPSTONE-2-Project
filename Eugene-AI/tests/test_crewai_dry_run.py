from src.agents import crewai_dry_run as dry_run


def test_scenario_loader_extracts_required_fields():
    scenario = dry_run.load_scenario()

    assert scenario["scenario_id"] == "rag-direct-prompt-injection"
    assert "prompt-injection" in scenario["expected_control"]
    assert "Full API response JSON" in scenario["evidence_required"]
    assert "NIST 800-53" in scenario["framework_mapping"]


def test_evidence_checker_blocks_without_specific_scenario_evidence():
    scenario = dry_run.load_scenario()
    evidence = dry_run.check_evidence(scenario)

    assert evidence["evidence_status"] == "evidence_missing"
    assert "evidence/break/rag-direct-prompt-injection.json" in evidence["missing_evidence"]


def test_dry_run_writer_creates_pending_human_review_output(tmp_path):
    payload = dry_run.build_dry_run_payload()
    output = dry_run.write_dry_run(payload, tmp_path / "dry-run.json")

    assert output.exists()
    assert payload["draft_finding_status"] == "blocked_until_evidence_exists"
    assert payload["human_review_status"] == "pending"
    assert payload["agents"] == dry_run.AGENT_SEQUENCE
