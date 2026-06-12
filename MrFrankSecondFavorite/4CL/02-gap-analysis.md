# 02 — Gap Analysis

**Client:** `<client name>`
**Stage:** Discovery
**Date:** `<YYYY-MM-DD>`
**Input:** [01-intake-questionnaire.md](01-intake-questionnaire.md)

Goal: record where the client stands today, mapped to the framework(s) and the controls behind them. This is the "where you are vs. where you need to be" picture.

Status legend: 🔴 missing · 🟡 partial · 🟢 in place

---

## Gap table

| Area | Finding (what's wrong / missing) | Framework criterion | NIST control | Status |
|---|---|---|---|---|
| `<e.g. AI tenant isolation>` | `<finding>` | `<e.g. SOC 2 CC6.1>` | `<e.g. AC-3, AC-4>` | 🔴 |
| `<area>` | `<finding>` | `<criterion>` | `<control>` | 🔴 |
| `<area>` | `<finding>` | `<criterion>` | `<control>` | 🟡 |
| `<area>` | `<finding>` | `<criterion>` | `<control>` | 🟢 |
| `<add rows as needed>` | | | | |

> For AI items, add the OWASP LLM ID alongside the NIST control (e.g. `SI-10 / OWASP LLM01`).

---

## Headline (write this last)

- **How many areas need work:** `<X of Y>`
- **The highest-risk gaps and why:** `<usually highest blast radius — what's the worst outcome?>`
- **What's deal/deadline-blocking:** `<the items that gate the goal from stage 01>`
- **Recommended priority order:** `<what to fix first, and the reason>`

The recommendation here drives the roadmap. Priority = blast radius first, then deadline dependency.

→ Next: **[03-roadmap.md](03-roadmap.md)**.
