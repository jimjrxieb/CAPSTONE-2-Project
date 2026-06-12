"""Model output guardrail for secrets and PHI."""
from __future__ import annotations

from src.guardrails.phi_scanner import filter_output as redact_phi
from src.guardrails.secret_scanner import COMPILED as SECRET_PATTERNS


def filter_model_output(response: str) -> tuple[str, list[str]]:
    """Redact sensitive patterns and return the redacted response plus finding labels."""
    filtered = redact_phi(response)
    findings: list[str] = []
    for pattern_name, compiled in SECRET_PATTERNS:
        if compiled.search(filtered):
            findings.append(pattern_name)
            filtered = compiled.sub(f"[{pattern_name.upper()}-REDACTED]", filtered)
    return filtered, findings
