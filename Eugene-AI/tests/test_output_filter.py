from src.rag.output_filter import filter_model_output


def test_output_filter_redacts_phi_and_secret():
    response, findings = filter_model_output(
        "Patient DOB: 01/02/1970. api_key=abc123abc123abc123abc123"
    )
    assert "[DOB-REDACTED]" in response
    assert "[API_KEY-REDACTED]" in response
    assert "api_key" in findings
