"""Pre-ingestion secret scanner. Implements F-004."""
from __future__ import annotations

import re
import structlog

log = structlog.get_logger()

SECRET_PATTERNS: list[tuple[str, str]] = [
    ("aws_key", r"(?i)(aws_secret_access_key|aws_access_key_id)\s*=\s*[A-Z0-9+/]{20,}"),
    ("api_key", r"(?i)(api_key|apikey|api-key)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{20,}"),
    ("password", r"(?i)(password|passwd|pwd)\s*[:=]\s*['\"]?.{8,}"),
    ("token", r"(?i)(token|secret)\s*[:=]\s*['\"]?[A-Za-z0-9_\-\.]{20,}"),
    ("private_key", r"-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    ("connection_string", r"(?i)(mongodb|postgresql|mysql|redis):\/\/[^:]+:[^@]+@"),
]

COMPILED = [(name, re.compile(pattern)) for name, pattern in SECRET_PATTERNS]


class SecretDetectedError(ValueError):
    pass


def scan_document(content: str, doc_name: str) -> None:
    """Raise SecretDetectedError if a secret pattern matches. Log pattern type, not value."""
    for pattern_name, compiled in COMPILED:
        if compiled.search(content):
            log.warning(
                "secret_detected_on_ingest",
                doc_name=doc_name,
                pattern_type=pattern_name,
                reason="SECRET_PATTERN_DETECTED",
            )
            raise SecretDetectedError(
                f"Document '{doc_name}' rejected: {pattern_name} pattern detected. "
                f"Remove secrets before ingesting."
            )
