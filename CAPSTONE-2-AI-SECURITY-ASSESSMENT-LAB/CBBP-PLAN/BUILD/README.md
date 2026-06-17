# BUILD Phase

BUILD is where the COMPLY package becomes controlled implementation work.

COMPLY found the client goals, wishlist, gaps, risks, and evidence requirements. BUILD turns those into approved build plans, sprint-sized implementation loops, AI dev-tool guardrails, and artifacts that BREAK can test.

This folder is a mini version of the GP-COPILOT delivery model:

```text
1-COMPLY findings and wishlist
  -> 2-BUILD scoped plan
  -> AI tool authorization check
  -> Codex / Claude Code implementation plan
  -> human review
  -> approved build work
  -> mini CBBP sprint loop
  -> BREAK validation
  -> PROVE evidence
```

## BUILD Rules

- BUILD does not invent scope. It receives scope from COMPLY.
- BUILD does not prove controls. BREAK and PROVE do that.
- BUILD does not let AI tools act as owners. Codex and Claude Code can draft plans and code, but a human approves build scope and accepts risk.
- BUILD output must be specific enough that BREAK can test it without guessing.

## Review Order

Files are now organized into pipeline stages (see `BUILD-PIPELINE-STATUS.md`).
Paths below reflect the stage each doc lives in.

| Order | File | Purpose |
| ---: | --- | --- |
| 1 | `comply-to-build-handoff.md` | Converts COMPLY findings, threats, and wishlist items into BUILD tickets. (root) |
| 2 | `BUILD-PIPELINE-STATUS.md` | Current kanban board for what is done, approved, under review, or deferred. |
| 3 | `terminal-codex-handoff.md` | Worker instructions for continuing an approved build from a fresh terminal Codex session. |
| 4 | `templates/approved-build-template.md` | Required fields for future approved builds. |
| 5 | `implementedbuilds/ai-dev-assist-harness.md` | Defines whether Codex / Claude Code are allowed and what boundaries they must follow. |
| 6 | `implementedbuilds/build-readiness-rubric.md` | Scores whether BUILD is controlled, reviewable, and ready for BREAK. |
| 7 | `implementedbuilds/eugene-build-harness.md` | Detailed implementation plan for Eugene's API, RAG path, guardrails, evidence, and workflow controls. |
| 8 | `implementedbuilds/rag-pipeline-build.md` | RAG-specific build plan and evidence path. |
| 9 | `4-completedbuilds/sprint1-status.md` | Sprint 1 implementation status and evidence. (also `sprint2-status.md`, `sprint2-plan.md`) |
| 10 | `4-completedbuilds/cks-platform-build-plan.md` | Container, Kubernetes, NetworkPolicy, and policy-control build path. |
| 11 | `crewai/` | Future agentic workflow design with human-control boundaries. (root) |

## Continuing An Approved Build

A fresh terminal Codex session should not rely on chat history. Give it the
approved build path and require it to read `AGENTS.md` plus
`terminal-codex-handoff.md` before editing.

Use this prompt shape:

```text
Read AGENTS.md and continue the approved build:
CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BUILD/2-approvedbuilds/<file>.md

Follow CBBP. Do not change anything outside the approved scope. If the approved
build lacks source traceability, target files, out-of-scope boundaries,
acceptance checks, or BREAK/PROVE handoff, stop and report what is missing.
```

Approved builds should follow `templates/approved-build-template.md`. At minimum
they must name status, approver, source traceability, target files, out-of-scope
boundaries, acceptance checks, BREAK handoff, PROVE handoff, and residual risk.

When an approved build has been implemented and its acceptance checks have
passed, move that build file out of `2-approvedbuilds/` and into
`4-completedbuilds/`. Anything left in `2-approvedbuilds/` is still approved
work, not completed work.

## Mini CBBP Build Loop

Each meaningful BUILD item should move through this loop:

| Step | Question | Output |
| --- | --- | --- |
| COMPLY input | What client goal, gap, threat, or finding created this build? | Finding ID, threat ID, wishlist item, or harness requirement |
| BUILD plan | What exactly will be built or changed? | Implementation plan, affected files, acceptance criteria |
| AI tool authorization | Are Codex or Claude Code allowed to help? | Data boundary, tool permissions, approval limits |
| Human review | Is the plan safe and scoped? | Approved / rejected / needs remediation |
| Implement | What artifact was built? | Code, config, workflow, policy, evidence runner, or doc |
| BREAK handoff | How will we try to break it? | Scenario, runner, expected failure/pass criteria |
| PROVE handoff | What evidence closes the claim? | JSON, Markdown, audit log, matrix, screenshot, report section |

## BUILD Lanes

| Lane | What It Builds | Primary Evidence |
| --- | --- | --- |
| Eugene RAG control harness | ingest, retrieval, role filtering, sanitizer, output filter, audit log, HITL flag | `sprint1-status.md`, `../PROVE/loop*-*.md`, `../../../Eugene-AI/evidence/` |
| AI dev-tool governance | Codex / Claude Code boundaries, approval prompts, CI labels, CODEOWNERS, SCA | `ai-dev-assist-harness.md`, `../PROVE/ai-dev-tool-boundary-evidence.md` |
| Platform / CKS controls | Docker, Kubernetes manifests, NetworkPolicy, policy checks, rate limit, model pinning | `cks-platform-build-plan.md`, `../../../Eugene-AI/deploy/`, platform evidence |
| Agentic workflow design | CrewAI roles, tool boundaries, evidence contracts, human approval design | `crewai/` |

## What Makes BUILD Strong

BUILD is strong when a reviewer can trace every implementation back to COMPLY and forward to BREAK/PROVE:

```text
COMPLY finding -> BUILD ticket -> implemented artifact -> BREAK test -> PROVE evidence -> client deliverable
```

If a build item cannot be traced in both directions, it is not ready.
