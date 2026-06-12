from src.evidence import baseline_eval_runner as runner


def test_injection_cases_are_rejected():
    for payload in runner.INJECTION_CASES:
        assert runner._run_injection_case(payload)["pass"]


def test_retrieval_case_passes_when_expected_doc_seen(monkeypatch):
    def fake_retrieve(query, role, top_k=None):
        return [
            {
                "id": "chunk-1",
                "doc_name": "ai-usage-policy-v2",
                "category": "policies",
                "classification": "Internal",
            }
        ]

    monkeypatch.setattr(runner, "retrieve", fake_retrieve)
    result = runner._run_retrieval_case(
        {
            "id": "BASE-RAG-TEST",
            "role": "compliance_analyst",
            "query": "approved use cases",
            "expected_sources": ["ai-usage-policy-v2"],
            "forbidden_categories": ["security"],
        }
    )
    assert result["pass"]
    assert result["expected_seen"] == ["ai-usage-policy-v2"]


def test_retrieval_case_fails_when_forbidden_category_seen(monkeypatch):
    def fake_retrieve(query, role, top_k=None):
        return [
            {
                "id": "chunk-1",
                "doc_name": "incident-response-plan-v3",
                "category": "security",
                "classification": "Confidential",
            }
        ]

    monkeypatch.setattr(runner, "retrieve", fake_retrieve)
    result = runner._run_retrieval_case(
        {
            "id": "BASE-RAG-TEST",
            "role": "compliance_analyst",
            "query": "incident response",
            "expected_sources": ["incident-response-plan-v3"],
            "forbidden_categories": ["security"],
        }
    )
    assert not result["pass"]
    assert result["forbidden_seen"] == ["security"]
