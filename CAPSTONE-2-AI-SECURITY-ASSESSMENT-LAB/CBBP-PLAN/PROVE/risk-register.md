# Risk Register

| ID | Scenario | Risk | Likelihood | Impact | Rank | Owner | Remediation | Status |
|---|---|---|---|---|---|---|---|---|
| POAM-0001 | Unauthorized retrieval — identity-layer bypass | A user can retrieve documents above their authorization level by manipulating the identity assertion behind role filtering | Medium | High (PHI / compliance-doc exposure across roles) | B | Eugene platform owner (name TBD) | Bind retrieval identity to the authenticated token instead of the request body; re-run unauthorized-retrieval BREAK to confirm closure | OPEN |

> Evidence: `Eugene-AI/evidence/break/unauthorized-retrieval-break-20260610T131529Z.json`
> Detected: Sprint 1 BREAK (2026-06-10). Carried forward through Sprint 2 as a pilot-expansion blocker.
> Routing: re-scope as a BUILD task in the next sprint (identity binding), not a standalone hotfix.
