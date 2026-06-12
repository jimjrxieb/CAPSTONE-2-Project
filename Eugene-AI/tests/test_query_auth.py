import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient

from config.settings import settings
from src.api.auth import require_query_auth
from src.api.rate_limit import check_rate_limit, reset_rate_limits


def test_query_auth_rejects_missing_bearer():
    with pytest.raises(HTTPException) as response:
        require_query_auth("not-a-bearer-token")
    assert response.value.status_code == 401


def test_query_auth_rejects_no_auth_header():
    """Empty string is what FastAPI passes when no Authorization header is present."""
    with pytest.raises(HTTPException) as response:
        require_query_auth("")
    assert response.value.status_code == 401


def test_query_auth_maps_token_to_role(monkeypatch):
    monkeypatch.setattr(settings, "vendor_risk_token", "vendor-token")
    context = require_query_auth("Bearer vendor-token")
    assert context.role == "vendor_risk_reviewer"
    assert context.user_id == "vendor_risk_reviewer:api-token"


def test_query_auth_rejects_role_spoof_token(monkeypatch):
    monkeypatch.setattr(settings, "vendor_risk_token", "vendor-token")
    monkeypatch.setattr(settings, "it_security_token", "it-token")
    context = require_query_auth("Bearer vendor-token")
    assert context.role == "vendor_risk_reviewer"
    assert context.role != "it_security"


def test_rate_limit_blocks_after_configured_limit():
    reset_rate_limits()
    check_rate_limit("user-1", limit=2)
    check_rate_limit("user-1", limit=2)
    with pytest.raises(HTTPException) as response:
        check_rate_limit("user-1", limit=2)
    assert response.value.status_code == 429


def test_http_role_field_in_body_rejected_with_422(monkeypatch):
    """POAM-0001: role field in request body must be explicitly rejected (extra='forbid')."""
    from src.api.main import app
    monkeypatch.setattr(settings, "admin_token", "test-admin-token")
    monkeypatch.setattr(settings, "vendor_risk_token", "vendor-test-token")
    client = TestClient(app, raise_server_exceptions=False)
    resp = client.post(
        "/query",
        json={"query": "test query", "session_id": "test", "role": "it_security"},
        headers={"Authorization": "Bearer vendor-test-token"},
    )
    assert resp.status_code == 422
