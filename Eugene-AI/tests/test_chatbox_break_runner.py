from src.evidence.chatbox_break_runner import _api_unavailable_case, _missing_role_case, _no_upload_history_case


def test_missing_role_break_case_passes():
    assert _missing_role_case()["rating"] == "PASS"


def test_api_unavailable_break_case_passes():
    assert _api_unavailable_case()["rating"] == "PASS"


def test_no_upload_history_break_case_passes():
    assert _no_upload_history_case()["rating"] == "PASS"
