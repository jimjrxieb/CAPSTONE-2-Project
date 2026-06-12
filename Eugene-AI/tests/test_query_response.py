from src.api.routes.query import _is_high_risk_source, build_eugene_response


def test_constant_yung_response_is_concise():
    response = build_eugene_response(
        "who is constant yung?",
        [
            {
                "doc_name": "hipaa-security-rule-assessment-2025",
                "chunk_index": 6,
                "text": "CISO (Constant Yung) designated as HIPAA Security Officer.",
            }
        ],
    )
    assert "Answer: Constant Yung" in response
    assert "HIPAA Security Officer" in response
    assert "Relevant context preview" not in response


def test_healthcare_privacy_category_is_high_risk_even_if_classification_internal():
    assert _is_high_risk_source({"category": "healthcare-privacy", "classification": "Internal"})


def test_approved_use_cases_response_is_useful():
    response = build_eugene_response(
        "What are the approved use cases for Eugene?",
        [
            {
                "doc_name": "ai-usage-policy-v2",
                "chunk_index": 1,
                "text": "## 3. Approved Use Cases Policy and procedure search. Compliance evidence lookup. Draft summaries. Template population. Training and awareness research.",
            }
        ],
    )
    assert "policy and procedure search" in response
    assert "compliance evidence lookup" in response
    assert "human review" in response


def test_clearbot_response_is_useful():
    response = build_eugene_response(
        "Is ClearBot approved?",
        [
            {
                "doc_name": "ai-system-inventory",
                "chunk_index": 2,
                "text": "ClearBot Enterprise status: Under Review — Not Approved for Production. Risk: High. No BAA. SOC 2 Type 2 not available.",
            }
        ],
    )
    assert "not authorized" in response
    assert "High risk" in response
    assert "no BAA" in response
