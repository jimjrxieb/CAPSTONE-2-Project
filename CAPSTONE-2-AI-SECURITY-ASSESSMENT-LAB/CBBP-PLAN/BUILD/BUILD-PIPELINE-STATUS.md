# BUILD Pipeline Status — Capstone 2 / Eugene

> The kanban board for this engagement's BUILD phase. Canonical workflow:
> `GP-CONSULTING/2-BUILD/BUILD-PIPELINE.md`. This board answers one question:
> **what is done, and what is left to build?**

Last updated: 2026-06-12

---

## Where Everything Sits

| Stage | Contents |
|---|---|
| `1-buildplanning/` | — |
| `2-approvedbuilds/` | — |
| `templates/` | `approved-build-template.md` for future worker-ready builds |
| `implementedbuilds/` | `eugene-build-harness.md`, `rag-pipeline-build.md`, `ai-dev-assist-harness.md`, `model-decision-record.md`, `build-readiness-rubric.md`, `fable-enhancements.md`, `001-poam-0001-identity-binding-impl.md` |
| `3-buildscodereview/` | — (`human-review/` for reviewer notes) |
| `4-completedbuilds/` | `001-sprint1-...md` + `sprint1-status.md`; `002-sprint2-...md` + `sprint2-plan.md` + `sprint2-status.md`; `001-poam-0001-identity-binding-fix.md`; `002-poam-0001-closure-propagation-patch.md`; `cks-platform-build-plan.md` |
| `4R-remediationRebuilds/` | — |

**At BUILD root** (navigation + phase input): `README.md`,
`BUILD-PIPELINE-STATUS.md` (this board), `terminal-codex-handoff.md` (fresh
worker instructions), `comply-to-build-handoff.md` (the COMPLY→BUILD entry doc),
and `crewai/` (self-contained CrewAI design package).

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
- **POAM-0001 — identity-binding fix.** Query identity is bound to the
  authenticated bearer token, request-body role assertion is rejected, and the
  unauthorized-retrieval BREAK re-run passed.
  → `4-completedbuilds/001-poam-0001-identity-binding-fix.md`;
  evidence `Eugene-AI/evidence/break/unauthorized-retrieval-break-20260612T134146Z.json`.
- **Terminal Codex handoff contract.** Fresh workers now have a repo-native
  prompt, required context checklist, approved-build folder contract, and
  reusable template.
  → `terminal-codex-handoff.md`; `templates/approved-build-template.md`.
- **POAM-0001 closure propagation patch.** PROVE risk register, CISO scorecard,
  and BUILD board now agree that POAM-0001 is closed.
  → `4-completedbuilds/002-poam-0001-closure-propagation-patch.md`.
- **CKS-style platform build plan.** Local Kubernetes-style manifests, policy
  checks, NetworkPolicy, Chroma auth, rate limiting, and platform evidence are
  complete for this capstone BUILD.
  → `4-completedbuilds/cks-platform-build-plan.md`;
  evidence `Eugene-AI/evidence/platform-control-check-20260612T045321Z.json`.

---

## BUILD Closeout

There is no remaining approved BUILD work for the local capstone.

What remains is outside BUILD:

- PROVE packaging polish, if a reviewer wants a different client-facing format.
- External identity provider integration, if this lab is later turned into a
  production pilot.
- Cloud deployment work, if a new COMPLY boundary approves a managed cloud
  target.

Those items should not sit in `2-approvedbuilds/` unless a new approved build
file is created for them.

---

## Next Action

BUILD is complete. Next work should start in BREAK or PROVE unless a human opens
a new approved BUILD file with fresh COMPLY traceability.
