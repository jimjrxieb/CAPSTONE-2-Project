# Terminal Codex Approved-Build Handoff

Use this file when a fresh terminal Codex session needs to continue approved BUILD work without private context.

## Worker Prompt

```text
Read AGENTS.md first.

Then read the BUILD orientation sequence required by AGENTS.md.

Continue the approved build at:
CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BUILD/2-approvedbuilds/<approved-build-file>.md

Do not invent scope. Implement only the approved build. If the approved build lacks source traceability, target files, out-of-scope boundaries, acceptance checks, or BREAK/PROVE handoff, stop and report what is missing instead of implementing.

Before editing, report:
- what is already implemented
- what remains phase-2
- what evidence already exists
- what exact files the approved build allows touching
- what is out of scope
- what BREAK/PROVE evidence will close the task

After implementation, run the acceptance checks listed in the approved build plus the AGENTS.md public-review checks.
```

## What Must Be In Place

An approved build is worker-ready only when all required fields are complete:

| Requirement | Must answer |
|---|---|
| Status | Is this explicitly `APPROVED`, and who approved it? |
| Approval scope | Is this code, config, docs, evidence, or platform work? Is it dev/staging only? |
| Source traceability | What COMPLY finding, threat, POA&M, risk-register item, wishlist item, or BUILD ticket created the work? |
| Target files | What exact files or folders may be touched? |
| Out of scope | What must not be touched, even if related? |
| Data boundary | What context may Codex use, and what context is prohibited? |
| Implementation plan | What must be changed in plain engineering terms? |
| Acceptance checks | What commands, greps, evidence checks, or file-path checks prove the build was completed? |
| BREAK handoff | What existing or new BREAK test validates the claim? What is the expected result? |
| PROVE handoff | What risk register, scorecard, deliverable, or evidence package must cite the result? |
| Residual risk | What remains after this build, and is it accepted, deferred, or routed to a new POA&M? |

If any row is missing, the worker should not fill it in silently. The correct response is a short blocker report naming the missing fields.

## Approved-Build Folder Contract

| Folder | Meaning | Worker behavior |
|---|---|---|
| `1-buildplanning/` | Drafted or proposed work | Do not implement unless the user explicitly promotes it or provides approval. |
| `2-approvedbuilds/` | Approved work ready for implementation | Read the build file, confirm scope, implement only that scope. |
| `implementedbuilds/` | Implementation notes and control design already built | Use as context and evidence, not as new scope. |
| `3-buildscodereview/` | Built work awaiting review | Do not continue implementation unless review asks for changes. |
| `4-completedbuilds/` | Gate 2 passed or closed work | Use as historical evidence. |
| `4R-remediationRebuilds/` | Failed review or failed BREAK rework | Implement only if a new approval points here. |

## Worker Closeout Checklist

Before returning final status, the worker should confirm:

- `git diff --stat` shows only approved files or clearly justified generated evidence.
- Every evidence file cited by the build exists locally.
- The approved acceptance checks passed, or failures are reported with exact output meaning.
- The BUILD board, PROVE docs, and evidence paths tell the same story.
- No real secrets, real PHI, real client data, or uncontrolled sensitive context was introduced.
- The public-review checks listed in AGENTS.md were run.

Intentional exceptions are allowed only where AGENTS.md names them, such as
ignored local preparation notes or code that rejects placeholder strings.
