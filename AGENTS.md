# AGENTS

This repository is a capstone lab for governed AI security assessment. Treat it like a public portfolio project: keep the work clear, evidence-backed, and safe to show to senior AI security, MLOps, AppSec, and cloud security reviewers.

## Start Here

For general orientation, read:

1. `README.md`
2. `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/START-HERE.md`
3. `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/README.md`
4. `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/STATUS.md`

For BUILD work, read this exact sequence before proposing or changing implementation:

1. `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BUILD/README.md`
2. `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BUILD/BUILD-PIPELINE-STATUS.md`
3. `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BUILD/terminal-codex-handoff.md`
4. `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BUILD/4-completedbuilds/sprint1-status.md`
5. `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BUILD/implementedbuilds/build-readiness-rubric.md`
6. `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BUILD/comply-to-build-handoff.md`
7. `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/COMPLY/traceability-matrix.md`

For continuing an approved BUILD from a fresh terminal Codex session, also read:

1. The approved build file under `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BUILD/2-approvedbuilds/`
2. `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BUILD/templates/approved-build-template.md`

If the approved build lacks source traceability, target files, out-of-scope boundaries, acceptance checks, or BREAK/PROVE handoff, stop and report the missing fields instead of implementing.

After reading those files, report:

- what is already implemented
- what remains phase-2
- what evidence already exists
- what the next safest BUILD task should be
- what BREAK test or PROVE evidence would close that task
- if continuing an approved build: what exact files are in scope, what is out of scope, and what acceptance checks will be run

For BREAK work, read this exact sequence before proposing or running any pentest:

1. `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BREAK/PENTEST-PIPELINE-STATUS.md`
2. `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BREAK/1-pentestplanning/SPRINT-PROGRAM-DESIGN.md`
3. `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BREAK/1-pentestplanning/SPRINT-PROGRAM-PLAN.md`
4. `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BREAK/0-scope/pentester-scenarios/README.md`
5. `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BREAK/0-scope/pentester-scenarios/04-rag-unauthorized-retrieval.md` (the break-and-watch exemplar every break-plan follows)
6. `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BREAK/0-scope/BUILD-to-BREAK-handoff.md`

For executing an approved pentest sprint from a fresh terminal Codex session, also read:

1. The signed sprint file under `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BREAK/2-pentestapproved/`
2. The break-plan it references under `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BREAK/0-scope/pentester-scenarios/`

BREAK rules a fresh session must respect:

- The pentest agent attacks and watches; it never provisions. If a scenario needs Falco/SIEM or a cluster, the deploy agent stands it up first.
- BREAK runs are local-lab only. Never reach for external offensive tooling (`nmap`, `sqlmap`, `nuclei`, `hydra`, etc.) — the PreToolUse hook blocks it by design.
- A control that blocks but does not log is half a control: confirm the alert fired (Falco/SIEM + audit entry), not just that the attack was denied.
- A security failure becomes a POA&M routed to BUILD — never "fixed" inside BREAK.

After reading the BREAK sequence, report: which scenarios already have alert-backed evidence, which need a re-run with the alert backend live, which need a net-new runner built, and what the next safest BREAK task is.

## CBBP Method

The project uses CBBP:

```text
COMPLY -> BUILD -> BREAK -> PROVE
```

- COMPLY defines the client goal, system boundary, owners, data classes, AI tool rules, risks, wishlist, and gaps.
- BUILD turns COMPLY outputs into approved implementation work.
- BREAK tests whether the built controls survive misuse and realistic failure modes.
- PROVE packages evidence, limitations, framework mapping, findings, and recommendations.

Do not skip phases. If BUILD needs a new scope decision, update or reference COMPLY first. If a build claim needs proof, send it to BREAK/PROVE instead of overclaiming.

## BUILD Model

BUILD is a mini GP-COPILOT delivery loop:

```text
COMPLY finding / wishlist / gap
  -> BUILD ticket
  -> Codex / Claude Code authorization check
  -> detailed implementation plan
  -> human review
  -> approved build
  -> BREAK validation
  -> PROVE evidence package
```

Every meaningful BUILD item should trace both ways:

```text
COMPLY finding -> BUILD ticket -> implemented artifact -> BREAK test -> PROVE evidence -> client deliverable
```

If a task cannot trace backward to COMPLY or forward to BREAK/PROVE, pause and clarify the scope.

## AI Dev-Tool Rules

Codex and Claude Code are allowed for this capstone, but only as governed development assistants.

Allowed context:

- approved repository files
- sanitized documentation
- generated fake data
- synthetic MedData Nexus corpus
- local Eugene implementation and evidence

Not allowed:

- real client data
- real PHI
- real credentials
- uncontrolled sensitive context
- autonomous risk acceptance
- final security findings without human review

AI tools may draft code, docs, plans, tests, and evidence helpers. A human owns scope, approval, and final risk judgment.

## Safety Boundaries

- Do not add real secrets, real client data, real PHI, or real credentials.
- Do not publish personal interview-prep notes. `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/interview-defense/` is intentionally ignored.
- Do not use external LLM APIs for Eugene retrieved context unless a new COMPLY boundary is approved.
- Do not claim production maturity for local capstone evidence.
- Do not treat CrewAI or n8n as implemented production orchestration unless the code and evidence prove it.
- Do not move or rename folders without updating all public references.

## Public Review Standard

This repo should be understandable to a hiring manager or senior engineer without private context.

Before finishing a change, check:

- `rg -n "TODO|TBD|PLACEHOLDER|FIXME|interview-defense|constant-pressure-test" CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB README.md MrFrankSecondFavorite`
- `find CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB -name '__pycache__' -o -name '*.pyc' -o -name '.pytest_cache'`
- `git status --short`

Intentional exceptions:

- code may contain logic that rejects placeholder strings
- local ignored files may exist under `interview-defense/`

## Current High-Level State

Capstone 2 is public-review ready as a local AI security assessment lab.

Implemented/local evidence exists for:

- Eugene API and chatbox
- local RAG pipeline
- manifest-gated ingestion
- input sanitization
- secret and PHI scanning
- role-filtered retrieval
- output filtering
- HITL review flags
- audit logging
- AI-assisted dev-tool governance
- CKS-style platform artifacts
- several BREAK/evidence runners

Known phase-2 work includes:

- remote GitHub CI proof
- external identity provider integration
- expanded n8n/CrewAI automation
- cloud AI service extensions under a new COMPLY boundary

## Commit Hygiene

Keep commits focused and explainable. Do not commit ignored local runtime state, personal prep notes, ChromaDB databases, cache files, or real secrets.
