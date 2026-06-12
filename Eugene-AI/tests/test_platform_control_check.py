from src.evidence.platform_control_check import run_platform_control_check


def test_platform_control_check_passes():
    payload = run_platform_control_check()
    assert payload["overall_status"] == "PASS"
