# Risk Register

| ID | Scenario | Risk | Likelihood | Impact | Rank | Owner | Remediation | Status |
|---|---|---|---|---|---|---|---|---|
| POAM-0001 | Unauthorized retrieval — identity-layer bypass | A user can retrieve documents above their authorization level by manipulating the identity assertion behind role filtering | Medium | High (PHI / compliance-doc exposure across roles) | B | Eugene platform owner | CLOSED 2026-06-12: retrieval identity is bound to the authenticated bearer token; request-body role assertion is rejected; unauthorized-retrieval BREAK re-run passed | CLOSED |

> Detection evidence: `Eugene-AI/evidence/break/unauthorized-retrieval-break-20260610T131529Z.json`
> Closure evidence: `Eugene-AI/evidence/break/unauthorized-retrieval-break-20260612T134146Z.json`
> Detected: Sprint 1 BREAK (2026-06-10). Closed: 2026-06-12, `closed_run=20260612T134146Z`.
> Routing: BUILD plan 001 implemented the identity-binding fix; this register now reflects the closed POA&M state.
