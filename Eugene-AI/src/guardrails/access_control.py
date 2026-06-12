"""Per-role ChromaDB access control. Implements F-001."""
from __future__ import annotations

import structlog

log = structlog.get_logger()

ROLE_COLLECTIONS: dict[str, list[str]] = {
    "vendor_risk_reviewer": ["vendor-risk"],
    "compliance_analyst": ["policies", "compliance", "legal-contracts", "vendor-risk", "ai-governance"],
    "it_security": [
        "policies",
        "compliance",
        "security",
        "legal-contracts",
        "healthcare-privacy",
        "vendor-risk",
        "ai-governance",
        "sanitized-baseline",
    ],
}

CLASSIFICATION_RANK: dict[str, int] = {
    "public": 0,
    "internal": 1,
    "confidential": 2,
    "restricted": 3,
    "poisoned-test-only": 99,
    "unsafe-test-only": 99,
}

ROLE_MAX_CLASSIFICATION: dict[str, str] = {
    "vendor_risk_reviewer": "Confidential",
    "compliance_analyst": "Confidential",
    "it_security": "Restricted",
}


class PermissionError(Exception):
    pass


def get_allowed_collections(role: str) -> list[str]:
    if role not in ROLE_COLLECTIONS:
        raise PermissionError(f"Unknown role: {role!r}")
    return ROLE_COLLECTIONS[role]


def get_role_max_classification(role: str) -> str:
    if role not in ROLE_MAX_CLASSIFICATION:
        raise PermissionError(f"Unknown role: {role!r}")
    return ROLE_MAX_CLASSIFICATION[role]


def filter_chunks_by_tier(chunks: list[dict], role: str) -> list[dict]:
    """Drop chunks whose category or classification exceeds the role's authorization."""
    allowed = get_allowed_collections(role)
    max_rank = _classification_rank(get_role_max_classification(role))
    approved: list[dict] = []
    for chunk in chunks:
        category = chunk.get("category", "unknown")
        classification = str(chunk.get("classification", "Internal"))
        if category in allowed and _classification_rank(classification) <= max_rank:
            approved.append(chunk)
        else:
            log.warning(
                "chunk_tier_exceeded",
                role=role,
                category=category,
                classification=classification,
                chunk_id=chunk.get("id"),
                reason="TIER_EXCEEDED",
            )
    return approved


def _classification_rank(classification: str) -> int:
    normalized = classification.strip().lower().replace(" ", "-")
    return CLASSIFICATION_RANK.get(normalized, CLASSIFICATION_RANK["restricted"])
