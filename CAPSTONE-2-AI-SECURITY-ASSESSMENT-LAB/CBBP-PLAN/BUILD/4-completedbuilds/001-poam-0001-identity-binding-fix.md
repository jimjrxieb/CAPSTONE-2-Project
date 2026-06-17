# BUILD Plan 001 — POAM-0001 Identity-Binding Fix

**Status:** APPROVED — released to army
**Approved by:** J · build-approver (senior CISSP/CISO) · 2026-06-12
**Approval scope:** C-rank implementation, dev/staging only. B-rank risk-acceptance stays with the human.
**Source finding:** POAM-0001 (risk register + `GP-S3/6-seclab-reports/slot-5/memory/poam-registry.jsonl`)
**Detected:** Sprint 1 BREAK, 2026-06-10
**Target:** `GP-SECLAB/target-application/slot-5/Eugene-AI/`
**Owner:** build-engineer (implementation-agent)
**Rank:** B (carries a B-rank finding — but the *fix implementation* is C-rank in staging; the risk-acceptance decision stays human)

## Why This Build Exists

The unauthorized-retrieval BREAK proved a real gap: Eugene's role filter trusts an
identity assertion that can be manipulated, so a user could retrieve documents
above their authorization level (e.g. Vendor Risk reading IT Security material).
This is the single open item blocking broad rollout. Pilot with trusted users is
OK; widening access is not, until this closes.

## Proposed Change

Bind the retrieval identity to the **authenticated bearer token**, not to anything
in the request body. The role used for filtering must be derived server-side from
the validated token claims — the request must not be able to assert its own role.

1. Trace where retrieval resolves the caller's role today (likely the `/query`
   path and the retriever role filter).
2. Make the role a function of the authenticated token only. Reject or ignore any
   role/identity field supplied in the request body.
3. Add a server-side check: token identity ↔ requested scope mismatch → deny + audit.
4. Re-run the unauthorized-retrieval BREAK to confirm the bypass is closed.

## Files Likely Touched

Assessment-first. Expected, if confirmed at implementation:
- the FastAPI `/query` route (role derivation)
- the retriever role-filter module
- the auth/token validation helper

## Acceptance (Gate 2 + BREAK)

- Re-run `unauthorized-retrieval-break` → identity-bypass case now BLOCKED.
- New evidence file under `Eugene-AI/evidence/break/`.
- On confirmed closure: update POAM-0001 `status` → CLOSED with `closed_run`,
  append the remediation-log entry, and move this plan to `4-completedbuilds/`.

## Pipeline

```
1-buildplanning/ (here)  → Gate 1 sign-off → 2-approvedbuilds/ → army builds
  → implementedbuilds/ → Gate 2 review + BREAK re-run
  → 4-completedbuilds/  (or 4R-remediationRebuilds/ if the fix doesn't hold)
```
