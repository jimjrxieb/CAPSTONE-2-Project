# 06 — Client Report

**Client:** `<client name>`
**Stage:** Optimization (report)
**Date:** `<YYYY-MM-DD>`
**Input:** [05-validation-checklist.md](05-validation-checklist.md)

Two parts: a one-page exec summary (what the founder/CTO reads) and a POA&M of open items (what engineering and the auditor track). Keep the exec summary to one page — risk-first, business language, no jargon.

---

## Part 1 — Executive Summary (1 page)

**To:** `<buyer name + role>`
**From:** ConstantLaunch
**Re:** `<engagement name>` — outcome

### Bottom line
`<One or two sentences: are they ready / cleared? Directly answer the goal and the top worry from stage 01.>`

### What changed
- `<before → after, in plain terms>`
- `<how many gaps closed + validated; how many tracked>`
- `<the headline improvement the buyer cares about>`

### Risk posture: before → after
| | Start | Now |
|---|---|---|
| `<top risk #1>` | `<before>` | `<after>` |
| `<top risk #2>` | `<before>` | `<after>` |
| `<top risk #3>` | `<before>` | `<after>` |

### Open item(s)
`<The honest list of what's still open, with risk level and whether it blocks the goal. If none, say so.>`

### The ask
1. `<decision you need from them>`
2. `<decision you need from them>`
3. `<next step — schedule the audit / approve the fix window / etc.>`

---

## Part 2 — POA&M (open items)

One block per open finding. Track it the way an auditor expects — control, risk, owner, date, closure test.

| Field | Value |
|---|---|
| **POA&M ID** | POAM-`<NNNN>` |
| **Control** | `<control ID + name; add OWASP LLM ID for AI items>` |
| **Finding** | `<verbatim from validation — what failed and the impact>` |
| **Risk** | `<Low / Medium / High>` |
| **Detected** | `<validation run date — link stage 05>` |
| **Remediation** | `<the fix>` |
| **Owner** | `<named role — never just "engineering">` |
| **Scheduled completion** | `<absolute date — never "next sprint">` |
| **Closure criteria** | `<the specific test that must pass to close this>` |

`<copy the block per open item>`

**Everything else is closed and validated** — `<confirm no other open items, or list them>`.

---

## What the client walks away with
- `<evidence package mapped to their framework>`
- `<the test suite, handed over so they can re-run it>`
- `<the hardened system + the gates that keep it that way>`
- `<honestly-tracked open items with dates and closure tests>`

The closing principle: **tested and proven beats configured and assumed.**
