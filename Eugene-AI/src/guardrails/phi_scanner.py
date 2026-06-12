"""PHI pattern scanner — pre-ingestion and output filter. Implements F-004."""
from __future__ import annotations

import re
import structlog

log = structlog.get_logger()

PHI_PATTERNS: list[tuple[str, str]] = [
    ("ssn", r"\b\d{3}-\d{2}-\d{4}\b"),
    ("mrn", r"\bMRN[-:]?\s*\d{6,10}\b"),
    ("dob", r"\bDOB[-:]?\s*\d{2}/\d{2}/\d{4}\b"),
    ("icd10", r"\bICD-10[-:]?\s*[A-Z]\d{2}\.?\d*\b"),
    ("insurance_id", r"\b(INS|MEMBER)[-#]?\s*\d{8,12}\b"),
]

COMPILED = [(name, re.compile(pattern, re.IGNORECASE)) for name, pattern in PHI_PATTERNS]


class PHIDetectedError(ValueError):
    pass


def scan_document(content: str, doc_name: str) -> None:
    """Raise PHIDetectedError if a PHI pattern matches in document content."""
    for pattern_name, compiled in COMPILED:
        if compiled.search(content):
            log.warning(
                "phi_detected_on_ingest",
                doc_name=doc_name,
                pattern_type=pattern_name,
                reason="PHI_PATTERN_DETECTED",
            )
            raise PHIDetectedError(
                f"Document '{doc_name}' flagged: {pattern_name} PHI pattern detected. "
                f"Review before ingesting — de-identify or escalate to Privacy Officer."
            )


def filter_output(response: str) -> str:
    """Redact PHI patterns from model output before delivery to user."""
    for pattern_name, compiled in COMPILED:
        if compiled.search(response):
            log.warning("phi_detected_in_output", pattern_type=pattern_name)
            response = compiled.sub(f"[{pattern_name.upper()}-REDACTED]", response)
    return response
