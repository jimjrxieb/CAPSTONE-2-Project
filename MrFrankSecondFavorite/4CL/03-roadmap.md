# 03 — Remediation Roadmap

**Client:** `<client name>`
**Stage:** Strategy
**Date:** `<YYYY-MM-DD>`
**Input:** [02-gap-analysis.md](02-gap-analysis.md)

Goal: turn the gaps into a prioritized plan with owners and dates. Group into waves so the client sees a sequence, not a pile.

---

## How priority was decided

State the filters you used, in order. Default:

1. **Blast radius** — worst outcome if it fails. Data leakage / loss of isolation tops everything.
2. **Deadline dependency** — what blocks the goal/deal/audit from stage 01.

> `<note any client-specific priority calls here>`

---

## Wave 1 — Days 0–`<N>`: `<theme, e.g. stop the bleeding>`

| Item | Control | Owner | Target |
|---|---|---|---|
| `<fix>` | `<control>` | `<who>` | `<day/date>` |
| `<fix>` | `<control>` | `<who>` | `<day/date>` |

## Wave 2 — Days `<N>`–`<M>`: `<theme, e.g. build the controls>`

| Item | Control | Owner | Target |
|---|---|---|---|
| `<fix>` | `<control>` | `<who>` | `<day/date>` |
| `<fix>` | `<control>` | `<who>` | `<day/date>` |

## Wave 3 — Days `<M>`–`<end>`: `<theme, e.g. prove it + package evidence>`

| Item | Control | Owner | Target |
|---|---|---|---|
| Re-run all validation after fixes ship | (all) | `<who>` | `<date>` |
| Assemble evidence package mapped to framework | CA-2 | `<who>` | `<date>` |
| Exec summary + POA&M of remaining items | CA-5 | `<who>` | `<date>` |

---

## Ownership split

- **ConstantLaunch owns:** `<the specialized security engineering, test suites, policy-as-code, evidence packaging>`
- **Client owns:** `<app-code changes, their cloud accounts/IAM, business risk decisions>`

State this explicitly. It sets expectations and leaves the client a system they can keep running.

## The principle for the final wave

Earlier waves *build* controls. The last wave *validates and proves* them. Nothing enters the evidence package until a test confirms it works.

→ Next: **[04-build-log.md](04-build-log.md)**.
