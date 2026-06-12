import pytest

from src.guardrails.access_control import PermissionError, filter_chunks_by_tier, get_allowed_collections


def test_unknown_role_rejected():
    with pytest.raises(PermissionError):
        get_allowed_collections("unknown")


def test_vendor_risk_reviewer_cannot_read_security_chunk():
    chunks = [
        {"id": "1", "category": "vendor-risk", "classification": "Confidential"},
        {"id": "2", "category": "security", "classification": "Confidential"},
    ]
    approved = filter_chunks_by_tier(chunks, "vendor_risk_reviewer")
    assert [chunk["id"] for chunk in approved] == ["1"]


def test_it_security_can_read_security_chunk():
    chunks = [{"id": "2", "category": "security", "classification": "Confidential"}]
    assert filter_chunks_by_tier(chunks, "it_security") == chunks


def test_compliance_analyst_cannot_read_restricted_healthcare_privacy():
    chunks = [
        {"id": "3", "category": "healthcare-privacy", "classification": "Restricted"},
        {"id": "4", "category": "compliance", "classification": "Confidential"},
    ]
    approved = filter_chunks_by_tier(chunks, "compliance_analyst")
    assert [chunk["id"] for chunk in approved] == ["4"]


def test_it_security_can_read_restricted_healthcare_privacy():
    chunks = [{"id": "3", "category": "healthcare-privacy", "classification": "Restricted"}]
    assert filter_chunks_by_tier(chunks, "it_security") == chunks
