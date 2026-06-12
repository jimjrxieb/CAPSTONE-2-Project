# Completed Build 002 — Sprint 2: Platform Validation, Live Generation, CrewAI

**Status:** COMPLETE
**Build ID:** CAP2-BUILD-S2
**Completed:** 2026-06-12 (Codex, autonomous loop)
**Detail:** `sprint2-plan.md` + `sprint2-status.md` (same folder)
**Gate 2 review:** passed — independent verification 2026-06-12 (all evidence PASS, T3→T5 gate respected, cluster torn down, git untouched)

## What shipped

| Task | What | Result |
|---|---|---|
| S2-T1 | Status docs synced to reality (Loop 4 drift fixed) | DONE |
| S2-T2 | K8s RBAC Role + RoleBinding (namespace-scoped, 0 ClusterRole) | DONE |
| S2-T3 | Deployed platform BREAK on real kind cluster — Chroma direct-access blocked (same/other ns), API-to-Chroma allowed, rapid-query throttled | PASS (4/4) |
| S2-T4 | Live `EUGENE_MODE=ollama` generation, model `llama3.2:3b` pinned by digest, injection re-test | PASS |
| S2-T5 | CrewAI Loop 5 dry-run — `blocked_until_evidence_exists`, gate respected | DONE |
| S2-T6 | PROVE packaging — zero dead evidence references | DONE |

## Evidence

- `Eugene-AI/evidence/break/platform-deployed-break-20260612T043154Z.json` — PASS
- `Eugene-AI/evidence/eugene-helpfulness-eval-ollama-20260612T044252Z.json` — PASS
- `Eugene-AI/evidence/crewai/dry-run-rag-direct-prompt-injection.json` — blocked_until_evidence_exists
- `Eugene-AI/evidence/platform-control-check-20260612T045321Z.json` — PASS

## Carried forward (NOT closed by this build)

**POAM-0001** — unauthorized-retrieval identity-layer bypass. Detected Sprint 1
BREAK (2026-06-10), still open. Routes to a new BUILD plan, not a hotfix. See
`../1-buildplanning/001-poam-0001-identity-binding-fix.md`.
