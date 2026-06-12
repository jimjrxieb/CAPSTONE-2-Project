# BUILD Pipeline Status — Capstone 2 / Eugene

> The kanban board for this engagement's BUILD phase. Canonical workflow:
> `GP-CONSULTING/2-BUILD/BUILD-PIPELINE.md`. This board answers one question:
> **what is done, and what is left to build?**

Last updated: 2026-06-12

---

## Where Everything Sits

| Stage | Contents |
|---|---|
| `1-buildplanning/` | `001-poam-0001-identity-binding-fix.md` (awaiting Gate 1), `cks-platform-build-plan.md` (future platform work) |
| `2-approvedbuilds/` | — |
| `implementedbuilds/` | `eugene-build-harness.md`, `rag-pipeline-build.md`, `ai-dev-assist-harness.md`, `model-decision-record.md`, `build-readiness-rubric.md`, `fable-enhancements.md` |
| `3-buildscodereview/` | — (`human-review/` for reviewer notes) |
| `4-completedbuilds/` | `001-sprint1-...md` + `sprint1-status.md`; `002-sprint2-...md` + `sprint2-plan.md` + `sprint2-status.md` |
| `4R-remediationRebuilds/` | — |

**At BUILD root** (navigation + phase input): `README.md`, `BUILD-PIPELINE-STATUS.md`
(this board), `comply-to-build-handoff.md` (the COMPLY→BUILD entry doc), and
`crewai/` (self-contained CrewAI design package).

---

## DONE (Gate 2 passed)

- **Sprint 1 — RAG control harness.** Input sanitization, role-filtered retrieval,
  PHI/secret output redaction, manifest-gated ingestion, HITL flagging, audit
  hash-chain, query auth, rate limiting, Chroma auth + NetworkPolicy. Loops 1–3
  BREAK-validated. → `4-completedbuilds/001`.
- **Sprint 2 — platform + generation + CrewAI.** K8s RBAC, deployed platform BREAK
  on a real cluster (Chroma isolation + rate-limit proven live), live Ollama
  generation with a pinned model, CrewAI Loop 5 dry-run. Independently verified.
  → `4-completedbuilds/002`.

---

## WHAT'S LEFT TO BUILD

Prioritized. This is the answer to "what's left."

### P1 — Blocks broad rollout (the one real open item)
- **POAM-0001 — identity-binding fix.** Bind retrieval role to the authenticated
  token, not the request body. Then re-run the unauthorized-retrieval BREAK.
  → plan drafted at `1-buildplanning/001`, **awaiting Gate 1 sign-off** by build-approver.

### P2 — PROVE completeness (not strictly BUILD, but open)
- **Night-shift operator handoff.** The client scorecard exists
  (`../PROVE/client-scorecard/`); its dual-format companion does not. PROVE is not
  complete until both ship.

### P3 — Pre-production pilot blockers (future, not needed for a controlled pilot)
From `cks-platform-build-plan.md` "Not First-Sprint": live AWS EKS deployment,
external secret-manager integration, live TLS automation, Falco runtime tuning,
production ingress hardening. None block a controlled pilot; all block production.

### P4 — Optional / advisory
- **Full CrewAI orchestration** beyond the dry-run. The roadmap keeps CrewAI
  advisory/unwired until controls stay stable under repeat runs. Dry-run is done;
  full wiring is a deliberate later step, not a gap.

---

## Next Action

The only thing sitting at a gate is **POAM-0001**. To move it:

1. build-approver (human or Opus, senior CISSP/CISO) reviews
   `1-buildplanning/001-poam-0001-identity-binding-fix.md`.
2. Sign → moves to `2-approvedbuilds/` → army implements the identity binding.
3. Re-run the BREAK; on closure, update the POA&M registry and move to `4-completedbuilds/`.

Everything else is either done or deliberately deferred to the production phase.
