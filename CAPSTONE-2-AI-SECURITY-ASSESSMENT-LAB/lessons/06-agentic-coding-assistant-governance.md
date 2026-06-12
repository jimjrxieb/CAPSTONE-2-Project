# Lesson 06 - Agentic Coding Assistant Governance

**Status: COMPLETE — 2026-06-08**
**Scope note:** This lesson covers Codex / Claude Code / Copilot-style engineering assistants only.
Eugene (the assessment model) is governed separately in `CBBP-PLAN/COMPLY/Cap2-Harness.md` and `BUILD/rag-pipeline-build.md`.
**COMPLY deliverable:** `CBBP-PLAN/COMPLY/meddata-coding-assistant-intake.md`
**BREAK deliverable:** `CBBP-PLAN/BREAK/meddata-coding-assistant-break.md`

## What To Master

Coding assistants are not just autocomplete. They can influence architecture, dependencies, auth logic, tests, scripts, and deployment workflows.

The security question is:

> What can the assistant see, suggest, modify, execute, or cause a human to trust?

## Questions I Should Ask

- Which coding assistants are approved?
- Are engineers using personal accounts?
- Which repos can the tools access?
- Can the tool run commands?
- Can it open PRs?
- Can it modify auth, crypto, secrets, logging, or infrastructure?
- Are AI-assisted PRs labeled?
- Is security review required for sensitive changes?
- Are new dependencies reviewed?
- Are prompt injection risks from code comments and docs tested?
- What evidence proves human review happened?

## Evidence To Request

- approved tool list
- repo access policy
- PR template
- AI-assisted label policy
- CODEOWNERS
- CI workflow
- SAST/SCA/IaC/secrets scan logs
- dependency review evidence
- sample AI-assisted PR
- exception register

## What I Need To Know

The value is not "engineers use Codex."

The value is:

> Engineers can use Codex or Claude Code inside a governed workflow where sensitive data is protected, risky changes are reviewed, CI gates run, and evidence proves the review happened.

## Capstone Practice

Start with:

- `scenarios/ai-assisted-pr-label-bypass.md`
- `scenarios/ai-generated-auth-change.md`
- `scenarios/ai-unsafe-dependency-suggestion.md`

Task:

For each scenario, identify:

- what bypass is being tested
- what control should catch it
- what evidence proves it worked
- what finding exists if it fails

## Finding Trigger

Create a finding if:

- AI-assisted PRs can merge without disclosure
- auth-sensitive AI-generated code lacks security review
- dependencies can be added without SCA and human justification
- the tool has over-broad repo or command access

## CISO Sentence

> AI coding assistants can accelerate development, but the current workflow does not yet prove that AI-generated high-risk changes receive the review and scanning needed before merge.

