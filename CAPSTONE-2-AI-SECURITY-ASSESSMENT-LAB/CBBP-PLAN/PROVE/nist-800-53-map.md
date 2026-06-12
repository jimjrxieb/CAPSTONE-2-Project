# NIST 800-53 Mapping

| Scenario | Control | Control Family | Why It Applies | Evidence | Remediation |
|---|---|---|---|---|---|
| Direct prompt injection | SI-3, SI-10 | System and Information Integrity | Malicious or malformed input must be detected and rejected before retrieval/generation. | `Eugene-AI/evidence/break/chatbox-break-20260609T142715Z.json`; `Eugene-AI/evidence/eugene-helpfulness-eval-ollama-20260612T044252Z.json` | Maintain sanitizer patterns, output filtering, and rejection logging. |
| Chroma direct access and namespace isolation | SC-7, AC-4 | System and Communications Protection; Access Control | Vector DB traffic must be constrained to the authorized API path. | `Eugene-AI/evidence/break/platform-deployed-break-20260612T043154Z.json` | Keep default-deny NetworkPolicy and allow only API-to-Chroma traffic. |
| API least privilege | AC-6, CM-7 | Access Control; Configuration Management | The API pod should not receive unnecessary Kubernetes API privileges. | `Eugene-AI/evidence/platform-control-check-20260611T194349Z.json` | Keep namespace Role empty and bind only the Eugene API service account. |
| Rapid-query rate limit | SI-4, SC-5 | System and Information Integrity; System and Communications Protection | High-volume query bursts must be detected and rejected after the configured cap. | `Eugene-AI/evidence/platform-control-check-20260611T194349Z.json`; `Eugene-AI/evidence/break/platform-deployed-break-20260612T043154Z.json` | Keep per-token rate limit and rerun deployed rapid-query BREAK after config changes. |
