from src.evidence.corpus_contamination_break_runner import run_corpus_contamination_break


def test_corpus_contamination_break_runner_passes():
    payload = run_corpus_contamination_break()
    assert payload["overall_status"] == "PASS"
    assert payload["summary"]["pass"] == 5
    for case in payload["cases"]:
        assert case["framework_tags"]["owasp_llm"]
        assert case["framework_tags"]["nist_ai_rmf"]
        assert case["framework_tags"]["mitre_atlas"]
