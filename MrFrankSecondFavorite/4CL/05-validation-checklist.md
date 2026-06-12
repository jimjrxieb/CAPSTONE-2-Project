# 05 — Validation Checklist

**Client:** `<client name>`
**Stage:** Optimization (validate)
**Date:** `<YYYY-MM-DD>`
**Input:** [04-build-log.md](04-build-log.md)

Goal: test every control that was built. A control isn't done until a test confirms it. This is the stage that makes the final report trustworthy.

Result legend: ✅ holds · ⚠️ partial · ❌ failed

> **Adversarial-test rule:** for any active attack test (injection, cross-tenant attempts, network reachability), the consultant *writes* the test, an authorized human *runs* it against the client's environment, and both *review* the output. Never fire attack tooling automatically. Confirm you have written authorization to test before running anything active.

---

## Test entry template (copy per control)

### `<control / what you're testing>` — `<result>`
- **Test:** `<what you tried — be specific about the attack/check>`
- **Result:** `<what happened>`
- **Disposition:** `<holds → done | partial/failed → goes to POA&M with a fix path>`

---

## AI feature tests *(if AI in scope)*

### Cross-tenant / data-isolation — `<result>`
- **Test:** `<attempt to retrieve another tenant's data; empty-context query; "show all customers" prompt>`
- **Result:** `<...>`

### Prompt injection — `<result>`
- **Test:** `<direct + indirect injection payloads in user input and retrieved docs>`
- **Result:** `<...>`

### Output filtering — `<result>`
- **Test:** `<seed corpus with fake secrets/PII; ask questions that would surface them>`
- **Result:** `<...>`

## Platform tests

### NetworkPolicy enforcement — `<result>`
- **Test:** `<attempt connections that should be blocked; confirm allowed paths incl. DNS still work>`

### Container hardening — `<result>`
- **Test:** `<scan for root/privileged containers + missing limits>`

### RBAC / IAM least privilege — `<result>`
- **Test:** `<audit effective permissions; attempt a privileged action from an app identity>`

## CI / code tests

### Pipeline gates — `<result>`
- **Test:** `<open a PR with a vulnerable dep + hardcoded secret + SAST-detectable flaw; confirm it's blocked>`

`<add tests for any other controls built>`

---

## Scoreboard

| Control | Result |
|---|---|
| `<control>` | `<✅/⚠️/❌>` |
| `<control>` | `<✅/⚠️/❌>` |

- **Tested:** `<N>` · **Hold:** `<N>` · **Partial/failed:** `<N>`
- **Anything that could leak/lose data:** `<does it hold? — call this out explicitly>`
- **Each partial/failed item →** carry to the POA&M in the report. No silent gaps.

→ Next: **[06-client-report.md](06-client-report.md)**.
