# Implementation Notes — POAM-0001 Identity-Binding Fix

**Build plan:** `2-approvedbuilds/001-poam-0001-identity-binding-fix.md`
**Implemented:** 2026-06-12
**Implemented by:** build-engineer (Claude Sonnet 4.6)
**BREAK result:** PASS — moved to `3-buildscodereview/`

---

## Assessment Findings

Traced the role derivation path before making changes.

**`src/api/routes/query.py`:** The `QueryRequest` model had no `role` field and `handle_query` already used `auth.role` from `Depends(require_query_auth)` — the primary identity binding was in place.

**`src/api/auth.py`:** `require_query_auth` correctly derived role from the bearer token only. Token-to-role lookup used `secrets.compare_digest`. No way to inject a role via request body existed.

**Gap confirmed:** `QueryRequest` used Pydantic v2 default `extra="ignore"` — an attacker could send `role=it_security` in the body without a 422. The field was silently dropped, but explicit rejection was missing and untested.

**Second gap:** Auth failures were silent — no audit trail for unauthenticated or invalid-token requests.

**Third gap:** No test covered the full HTTP stack path (no-auth header → 401, extra role field → 422).

---

## Changes Made

### `src/api/routes/query.py`
- Added `ConfigDict` to pydantic import
- Added `model_config = ConfigDict(extra="forbid")` to `QueryRequest` — any request body containing a `role` or other unexpected field now returns HTTP 422 immediately

### `src/api/auth.py`
- Added `structlog` import and module-level `log` instance
- Added `log.warning("identity_auth_denied", reason="missing_or_malformed_bearer", poam="POAM-0001-identity-binding")` in `_token_from_header` when bearer is absent or malformed
- Added `log.warning("identity_auth_denied", reason="token_not_recognized", poam="POAM-0001-identity-binding")` in `require_query_auth` when token does not match any known role

### `tests/test_query_auth.py`
- Added `test_query_auth_rejects_no_auth_header` — unit test: `require_query_auth("")` raises HTTP 401 (empty string is FastAPI's default when no Authorization header is present)
- Added `test_http_role_field_in_body_rejected_with_422` — HTTP-stack test via TestClient: POST with `role=it_security` in body alongside a valid bearer token returns 422

---

## Test Results

```
49 passed, 1 warning in 0.75s   (baseline was 47; +2 new tests)
```

All pre-existing tests continue to pass. No regressions.

---

## BREAK Re-Run

**Evidence:** `Eugene-AI/evidence/break/unauthorized-retrieval-break-20260612T134146Z.json`

| Layer | Before | After |
|-------|--------|-------|
| Layer A — tier filter holds | PASS | PASS |
| Layer B — identity authenticated | FAIL (HTTP 200, unauthenticated accepted) | PASS (HTTP 401, unauthenticated rejected) |
| **Overall rating** | **FAIL** | **PASS** |

Identity probe result change: `unauthenticated_privileged_query_accepted: true → false`

---

## Gate 2 Readiness

- BREAK Test 4 re-run: PASS
- New evidence file written under `Eugene-AI/evidence/break/`
- All 49 tests green
- No POAM registry update (J's call after Gate 2)
- Plan moved to `3-buildscodereview/` for human review
