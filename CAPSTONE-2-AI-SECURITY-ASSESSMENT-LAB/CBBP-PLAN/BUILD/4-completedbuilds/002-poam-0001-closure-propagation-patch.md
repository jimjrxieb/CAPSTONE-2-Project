# BUILD Plan 002 — POAM-0001 Closure-Propagation Patch

**Status:** APPROVED — released to army
**Approved by:** J · build-approver (senior CISSP/CISO) · 2026-06-12
**Approval scope:** C-rank implementation, dev/staging only.
**Drafted by:** Claude (Fable 5, verifier session) · 2026-06-12
**Source finding:** POAM-0001 (`GP-S3/6-seclab-reports/slot-5/memory/poam-registry.jsonl`)
**Rank:** C (documentation alignment — no code, no controls touched)
**Target:** `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/` (BUILD + PROVE docs only)
**Owner:** build-engineer (any worker session, on approval)

## Why This Patch Exists

POAM-0001 (unauthorized retrieval — identity-layer bypass, AC-3/AC-6, B-rank) was
**fixed and closed this morning**. Verified independently before drafting this plan:

| Claim | Verified | Evidence |
|---|---|---|
| Code fix in place | ✅ `extra="forbid"` on `QueryRequest` (`Eugene-AI/src/api/routes/query.py:28`); `identity_auth_denied` audit logging on both deny paths (`Eugene-AI/src/api/auth.py:25,47`); role derived from bearer token only, `secrets.compare_digest` | working tree, committed |
| BREAK re-run PASS | ✅ rating PASS, both layers held, identity probe 401 (was 200) | `Eugene-AI/evidence/break/unauthorized-retrieval-break-20260612T134146Z.json` |
| Registry closed | ✅ `status: CLOSED`, `closed_run: 20260612T134146Z`, closed by J (Gate 2) | `GP-S3/6-seclab-reports/slot-5/memory/poam-registry.jsonl` |
| Remediation logged | ✅ validated, `validation_run_id: 20260612T134146Z` | `GP-S3/6-seclab-reports/slot-5/memory/remediation-log.jsonl` |
| Tests green | ✅ 49 passed (+2 new: no-auth → 401, body role field → 422) | `implementedbuilds/001-poam-0001-identity-binding-impl.md` |

**The remaining problem is documentation drift.** The PROVE-side deliverables and
the BUILD board still present POAM-0001 as open. An auditor walking the chain of
custody today would find the registry saying CLOSED while the client-facing
deliverables say OPEN — that breaks the 3PAO trail. This patch makes the paper
match the registry.

## Drift Inventory (what this patch fixes)

| # | File | Current (stale) state | Patched state |
|---|---|---|---|
| 1 | `PROVE/risk-register.md` | POAM-0001 `Status: OPEN`, evidence points at failing 2026-06-10 run | `Status: CLOSED (2026-06-12)`, add `closed_run 20260612T134146Z`, evidence pointer → passing re-run JSON, keep the original detection line for history |
| 2 | `PROVE/client-scorecard/ciso-client-scorecard.md` | §1 "One gap remains"; §2 row 3 ⚠️ Partial; §3 "Partially succeeded"; §4 lists POAM-0001 open; §5 asks for owner + fix-by; §6 row PARTIAL | §1 posture updated (identity gap closed 2026-06-12, evidence cited); §2 row 3 → ✅ with both before/after evidence files; §3 row → "Blocked after fix (was: partially succeeded)"; §4 → closed entry with closure note; §5 ask updated (pilot approval only); §6 add PASS row for the re-run |
| 3 | `BUILD/BUILD-PIPELINE-STATUS.md` | Says plan 001 sits in `1-buildplanning/` "awaiting Gate 1"; P1 lists the fix as the open blocker | Board reflects reality: 001 completed Gate 2 + BREAK PASS; P1 cleared; this patch (002) becomes the item at Gate 1 |
| 4 | `BUILD/3-buildscodereview/001-poam-0001-identity-binding-fix.md` | Plan stalled in code-review stage; its own acceptance criteria say "on confirmed closure … move to `4-completedbuilds/`" | Move file → `4-completedbuilds/001-poam-0001-identity-binding-fix.md` (impl notes in `implementedbuilds/` stay put, matching sprint convention) |

No other files. Specifically **out of scope**: any change under `Eugene-AI/`
(code is already fixed and validated), the GP-S3 registry/logs (already correct),
and BREAK evidence files (immutable once written).

## Residual Risk — Flagged, Not Patched (J's call, B-rank)

The identity layer is now bound to the bearer token, but the tokens themselves are
**static, shared, per-role secrets** from settings — no expiry, no rotation, no
per-user identity (`user_id` is synthetic `"{role}:api-token"`). That is acceptable
for the controlled pilot and is already consistent with the scorecard's pilot-only
posture, but broad rollout or production should bind identity to a real IdP
(OIDC/JWT claims, per-user subjects, token lifetime).

**Recommendation:** open a new POA&M (next sequential ID — do not reuse POAM-0001)
or add it to the P3 pre-production blockers in `cks-platform-build-plan.md`.
Decision is risk-acceptance → stays with J. This plan only records the flag.

## Acceptance (Gate 2)

- All four drift items above applied; no edit anywhere else (`git diff --stat` shows only those files).
- `grep -ri "OPEN" PROVE/risk-register.md` returns no POAM-0001 hit.
- Scorecard §6 evidence index includes the `20260612T134146Z` PASS row; every referenced evidence path resolves.
- `3-buildscodereview/` no longer contains 001; `4-completedbuilds/` does.
- Residual-risk flag either has a new POA&M ID or an explicit "accepted for pilot" note from J.

## Pipeline

```
1-buildplanning/ (here) → Gate 1 sign-off → 2-approvedbuilds/ → worker applies doc patch
  → implementedbuilds/ notes → Gate 2 review (paths + diffs checked)
  → 4-completedbuilds/
```
