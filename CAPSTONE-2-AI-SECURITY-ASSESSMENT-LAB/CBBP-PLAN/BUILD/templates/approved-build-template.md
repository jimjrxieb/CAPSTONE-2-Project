# BUILD Plan NNN — Short Title

**Status:** APPROVED
**Approved by:** Name / role / date
**Approval scope:** Code, config, docs, evidence, or platform; dev/staging/local only unless explicitly approved otherwise
**Source finding:** Finding ID, POA&M ID, risk-register ID, COMPLY threat ID, wishlist item, or BUILD ticket
**Rank:** S, A, B, C, or advisory
**Target:** Exact files or folders this build may touch
**Owner:** Build engineer or worker role

## Why This Build Exists

State the client goal, finding, threat, or evidence gap that created this work.
Do not introduce new scope here. If the work cannot trace back to COMPLY or a
human-approved POA&M/build item, it is not ready.

## Approved Context

Codex may use:

- approved repository files
- sanitized documentation
- generated fake data
- synthetic MedData Nexus corpus
- local Eugene implementation and evidence

Codex must not use:

- real client data
- real PHI
- real credentials
- uncontrolled sensitive context
- external LLM APIs for Eugene retrieved context unless COMPLY approves a new boundary

## Proposed Change

Describe the exact implementation or documentation change.

1. First concrete step.
2. Second concrete step.
3. Final concrete step.

## Files In Scope

- `path/to/file-or-folder`

## Out Of Scope

- Runtime code not listed above
- Evidence JSON files unless this build explicitly generates new evidence
- Registry or remediation logs unless this build explicitly names them
- Production identity, cloud service, or external API integrations unless this build explicitly names them

## Acceptance Checks

- Check 1
- Check 2
- Check 3
- `git diff --stat` shows only approved files, except generated evidence explicitly named by this plan

## BREAK Handoff

| Scenario | Runner or evidence | Expected result |
|---|---|---|
| Scenario name | `path/to/runner-or-evidence` | PASS condition |

If BREAK is already complete, name the immutable evidence file and explain that
this build only propagates the result.

## PROVE Handoff

| Claim | PROVE artifact | Evidence to cite |
|---|---|---|
| Claim to close | `path/to/prove-file.md` | `path/to/evidence.json` |

## Residual Risk

State what remains after this build. If it is accepted for the controlled pilot,
say so. If it needs new work, route it to a new POA&M or future BUILD item. Do
not reuse a closed POA&M ID for a new risk.

## Worker Instructions

Before editing, the worker must report:

- what is already implemented
- what remains phase-2
- what evidence already exists
- what exact files are in scope
- what is out of scope
- what BREAK/PROVE evidence will close the task

If any required field above is missing, stop and report the missing fields
instead of implementing.

## Pipeline

```text
1-buildplanning/ -> Gate 1 sign-off -> 2-approvedbuilds/
  -> worker implementation -> implementedbuilds/ notes if needed
  -> 3-buildscodereview/ or Gate 2 review
  -> 4-completedbuilds/ or 4R-remediationRebuilds/
```
