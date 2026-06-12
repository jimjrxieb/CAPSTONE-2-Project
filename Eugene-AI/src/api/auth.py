"""Bearer-token authentication helpers for Eugene API routes."""
from __future__ import annotations

import secrets
from dataclasses import dataclass

import structlog
from fastapi import Header, HTTPException

from config.settings import settings

log = structlog.get_logger()


@dataclass(frozen=True)
class AuthContext:
    user_id: str
    role: str


def _token_from_header(authorization: str) -> str:
    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer" or not token.strip():
        log.warning(
            "identity_auth_denied",
            reason="missing_or_malformed_bearer",
            poam="POAM-0001-identity-binding",
        )
        raise HTTPException(status_code=401, detail="Bearer token required")
    return token.strip()


def _role_tokens() -> dict[str, str]:
    return {
        "vendor_risk_reviewer": settings.vendor_risk_token,
        "compliance_analyst": settings.compliance_analyst_token,
        "it_security": settings.it_security_token,
    }


def require_query_auth(authorization: str = Header("")) -> AuthContext:
    token = _token_from_header(authorization)
    for role, expected in _role_tokens().items():
        if expected and secrets.compare_digest(token, expected):
            return AuthContext(user_id=f"{role}:api-token", role=role)
    log.warning(
        "identity_auth_denied",
        reason="token_not_recognized",
        poam="POAM-0001-identity-binding",
    )
    raise HTTPException(status_code=403, detail="Valid role-bearing token required")


def require_it_security(authorization: str = Header("")) -> None:
    token = _token_from_header(authorization)
    if not settings.it_security_token:
        raise HTTPException(status_code=503, detail="IT Security token is not configured")
    if not secrets.compare_digest(token, settings.it_security_token):
        raise HTTPException(status_code=403, detail="IT Security token required")
