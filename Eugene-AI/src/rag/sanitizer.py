"""Input sanitization — injection pattern detection. Implements F-002."""
from __future__ import annotations

import re
import structlog

log = structlog.get_logger()

INJECTION_PATTERNS: list[str] = [
    r"ignore (your )?(previous |all )?instructions",
    r"repeat (your )?system prompt",
    r"you are now",
    r"SYSTEM OVERRIDE",
    r"disregard (your )?(previous )?instructions",
    r"act as (a )?(different|new|unrestricted)",
    r"forget (your )?(previous )?instructions",
    r"do not follow",
    r"override (your )?(previous )?instructions",
    r"new persona",
    r"jailbreak",
    r"DAN mode",
]

COMPILED = [re.compile(p, re.IGNORECASE) for p in INJECTION_PATTERNS]


class InjectionDetectedError(ValueError):
    pass


def sanitize_query(query: str) -> str:
    """Raise InjectionDetectedError if any pattern matches. Return query unchanged if clean."""
    for pattern, compiled in zip(INJECTION_PATTERNS, COMPILED):
        if compiled.search(query):
            log.warning(
                "injection_detected",
                pattern=pattern,
                query_preview=query[:80],
            )
            raise InjectionDetectedError(
                f"Query rejected: injection pattern detected. "
                f"This attempt has been logged."
            )
    return query


def scan_document_for_injection(content: str, doc_name: str) -> None:
    """Raise InjectionDetectedError if a corpus document contains instruction-injection text."""
    for pattern, compiled in zip(INJECTION_PATTERNS, COMPILED):
        if compiled.search(content):
            log.warning(
                "document_injection_detected",
                pattern=pattern,
                doc_name=doc_name,
            )
            raise InjectionDetectedError(
                f"Document '{doc_name}' rejected: prompt-injection pattern detected."
            )
