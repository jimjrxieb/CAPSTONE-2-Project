from src.evidence.sprint1_control_check import run_control_check


def test_sprint1_control_check_passes(tmp_path, monkeypatch):
    from config.settings import settings

    monkeypatch.setattr(settings, "audit_log_path", tmp_path / "audit-log.jsonl")
    payload = run_control_check()
    assert payload["overall_status"] == "PASS"
