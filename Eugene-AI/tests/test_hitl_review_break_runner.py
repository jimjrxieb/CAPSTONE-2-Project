from src.evidence.hitl_review_break_runner import (
    _invalid_decision_case,
    _missing_token_case,
    _unreviewed_distribution_case,
    _weak_rationale_case,
)


def test_missing_token_break_case_passes():
    assert _missing_token_case("AUD-20260609T000000Z-ABC123")["rating"] == "PASS"


def test_weak_rationale_break_case_passes():
    assert _weak_rationale_case("AUD-20260609T000000Z-ABC123")["rating"] == "PASS"


def test_invalid_decision_break_case_passes():
    assert _invalid_decision_case("AUD-20260609T000000Z-ABC123")["rating"] == "PASS"


def test_unreviewed_distribution_break_case_passes(tmp_path, monkeypatch):
    from config.settings import settings

    monkeypatch.setattr(settings, "review_log_path", tmp_path / "review-log.jsonl")
    assert _unreviewed_distribution_case("AUD-20260609T000000Z-ABC123")["rating"] == "PASS"
