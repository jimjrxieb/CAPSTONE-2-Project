# Coding Assistant Governance Intake — MedData Nexus Health Systems

> Filled workpaper for Capstone 2 COMPLY phase.
> Lesson: `lessons/06-agentic-coding-assistant-governance.md`
> Client: MedData Nexus Health Systems
> Scope: Codex / Claude Code / Copilot-style engineering assistants used to build internal
>   applications and the AI ingestion pipeline — NOT Eugene (Eugene is the assessment model;
>   governed separately in `CBBP-PLAN/COMPLY/Cap2-Harness.md` and `BUILD/rag-pipeline-build.md`)
> Assessor: jimjrxieb + Eugene (CAP2-AI-001, advisory)
> Date: 2026-06-08

---

## Scope Clarification

This intake covers **coding assistants** — tools like Claude Code, Codex, and GitHub Copilot
that engineers use to write, review, and modify application code, the RAG ingestion pipeline,
CI scripts, and infrastructure configuration.

Eugene is not a coding assistant. Eugene is the assessment model being built and governed.
That separation matters:

| Role | Tool | Governed By |
|---|---|---|
| Build the lab / write pipeline code | Claude Code, Codex | This document + `BUILD/ai-dev-assist-harness.md` |
| Assess the RAG system | Eugene | `CBBP-PLAN/COMPLY/Cap2-Harness.md`, `BUILD/rag-pipeline-build.md` |

---

## Intake Questions — MedData Nexus Answers

| Question | Answer |
|---|---|
| Which coding assistants are approved? | Claude Code (CLI) — approved for Capstone 2 build work under the rules in `BUILD/ai-dev-assist-harness.md`. Codex — approved with the same rules. Personal GitHub Copilot — not approved for use on company code. |
| Are engineers using personal accounts? | Unknown — shadow AI audit not completed. Risk: developers may use personal Copilot or ChatGPT subscriptions for coding tasks, exposing repo content or generating code outside the governed workflow. |
| Which repos can the tools access? | Approved: `GP-SECLAB/target-application/slot-5/CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/` for build work. Not approved: production repos, client repos, any repo containing real credentials, customer data, or sensitive internal architecture. |
| Can the tool run commands? | Claude Code: yes — Bash tool access is available but scoped to the lab repo. Commands that affect production systems, delete data, or modify infrastructure outside the lab require explicit human confirmation. Codex: no direct command execution. |
| Can it open PRs? | Claude Code can assist with PR creation but a named human reviewer must approve and merge. AI cannot merge directly. |
| Can it modify auth, crypto, secrets, logging, or infrastructure? | Any change to auth, token handling, role checks, secrets management, logging pipelines, or infrastructure requires: (1) AI-assisted label on the PR, (2) named security reviewer, (3) passing SAST + dependency scan before merge. |
| Are AI-assisted PRs labeled? | Policy exists: AI-assisted label is required. Not enforced by a CI gate — a developer can omit the label and merge. This is a COMPLY gap. |
| Is security review required for sensitive changes? | Required by policy. CODEOWNERS or named reviewer is needed for auth, IAM, secrets, and infrastructure changes. Not yet evidenced as enforced in CI. |
| Are new dependencies reviewed? | Required: pip-audit, license check, and written human justification before merge. Not proven with scan evidence in current baseline. |
| Are prompt injection risks from code comments tested? | Not tested. Code comments and inline documentation are a vector for indirect prompt injection against coding assistants. BREAK scenario planned. |
| What evidence proves human review happened? | PR merge record with named reviewer and approval timestamp. Not yet proven for all changes — no sample AI-assisted PR with full evidence chain exists. |

---

## Evidence Requested — Status

| Evidence Artifact | Required | Current Status | Gap |
|---|---|---|---|
| Approved tool list | Yes | Defined in `BUILD/ai-dev-assist-harness.md` | Shadow AI audit incomplete — list may be missing tools |
| Repo access policy | Yes | Scoped in `BUILD/ai-dev-assist-harness.md` | Not enforced in CI or access control settings |
| PR template with AI disclosure question | Yes | Not implemented | No PR template requiring AI-assisted label |
| AI-assisted label policy | Yes | Policy stated, not enforced | No CI gate checks for missing label |
| CODEOWNERS file | Yes | Not confirmed | No CODEOWNERS file in the capstone repo |
| CI workflow with SAST/SCA/secrets gates | Yes | Not proven | No CI scan evidence for the ingestion pipeline |
| Dependency review evidence | Yes | Not proven | No pip-audit or license check output in baseline |
| Sample AI-assisted PR with full evidence | Yes | Not produced | No sample PR demonstrating the governed workflow |
| Exception register | Yes | Not implemented | No register tracking approved deviations from policy |

---

## Tool Authority Matrix

| Action | Claude Code / Codex | Approved? | Required Review |
|---|---|---|---|
| Read repo files | Yes | Yes — scoped to approved repo | None for read-only |
| Edit existing files | Yes | Yes — within approved scope | Human reviews diff before merge |
| Create new files | Yes | Yes | Human reviews before merge |
| Run CLI commands (build, test, lint) | Yes (Claude Code only) | Yes — scoped commands | Human confirms before destructive commands |
| Run security scans (pip-audit, Semgrep) | Yes (Claude Code only) | Yes | Scan results reviewed by human |
| Open PRs | Yes (assist only) | Yes — human must approve and merge | Named human reviewer required |
| Merge PRs | No | Not authorized | Human only |
| Push to main/master directly | No | Not authorized | Human only |
| Modify auth, IAM, secrets, infra | Yes (suggest only) | Yes — with elevated review | Named security reviewer + SAST gate |
| Access production systems | No | Not authorized | Human only |
| Access real client data or PHI | No | Not authorized | Blocked — out of scope |

---

## COMPLY Finding Triggers — Confirmed

| # | Trigger | Status |
|---|---|---|
| 1 | No PR template requiring AI-assisted disclosure | OPEN |
| 2 | No CI gate enforcing AI-assisted label before merge | OPEN |
| 3 | No CODEOWNERS or named reviewer enforcement for auth/infra changes | OPEN |
| 4 | No SAST/SCA/secrets scan gate proven in CI for pipeline code | OPEN |
| 5 | Shadow AI audit not completed — personal Copilot use possible | OPEN |
| 6 | No sample AI-assisted PR demonstrating the full governed workflow | OPEN |
| 7 | No exception register for approved deviations | OPEN |

---

## Scope Finding: No CI Enforcement of AI-Assisted PR Disclosure

**Condition:** MedData Nexus has a policy requiring that AI-assisted PRs be labeled. There is no CI gate that enforces this. A developer can omit the label and merge AI-assisted code without disclosure.

**Why It Matters:** Without enforced disclosure, the organization cannot prove which production code is AI-generated, whether it received the review appropriate for AI-assisted changes, or whether it passed the security gates designed for that category of change. An auditor cannot distinguish a human-written change from an AI-assisted one.

**Evidence Needed:**
- CI job or GitHub Action that checks for the `ai-assisted` label before a merge is permitted
- PR template with AI contribution disclosure question
- At least one sample AI-assisted PR with the label, CI scan results, and named reviewer on record

**Risk:** AI-generated code with insecure defaults, vulnerable dependencies, or auth logic errors enters production without the review tier it should receive.

**Recommendation:** Implement a CI gate (GitHub Action or pre-merge check) that blocks merge if the `ai-assisted` label is absent on PRs touching sensitive code paths. Add a PR template question: "Did an AI coding assistant materially contribute to this change?"
