# Lesson 09 - Evidence And PROVE

**Status: COMPLETE — 2026-06-08**
**Deliverables:**
- `CBBP-PLAN/PROVE/meddata-prove-package.md` — evidence packet (T-03 full example), PROVE exit criteria, evidence index
- `deliverables/02-client-findings-report.md` — 10 findings, all ranked, all open, COMPLY-phase evidence
- `deliverables/03-remediation-roadmap.md` — immediate/30/60/90-day remediation sequence with gates
- `deliverables/01-executive-summary.md` — CISO-facing scale/no-scale recommendation

## What To Master

PROVE is where confidence becomes defensible.

Evidence is not decoration. Evidence is the difference between:

> We think this is secure.

and:

> Here is what we tested, what happened, what failed, what held, and what we recommend.

## Questions I Should Ask

- What claim am I proving?
- What artifact supports that claim?
- Is the artifact dated?
- Does it name the system?
- Does it show owner or approver?
- Does it show runtime behavior or only intent?
- Can someone reproduce the result?
- What gap remains?
- What POA&M or remediation item follows?

## Evidence To Collect

- screenshots
- API responses
- logs
- CI output
- scanner reports
- PR reviews
- config exports
- architecture diagrams
- data flow diagrams
- test inputs and outputs
- model/version metadata
- human approval notes

## What I Need To Know

Good evidence has:

- path
- date
- owner
- system
- procedure
- result
- interpretation

Bad evidence sounds like:

- "The team does this."
- "It should be configured."
- "Policy says it is required."
- "We believe the vendor handles it."

## Capstone Practice

Open:

- `evidence/README.md`
- `deliverables/02-client-findings-report.md`
- `deliverables/03-remediation-roadmap.md`
- `deliverables/04-ai-adoption-operating-model.md`

Task:

For one scenario, create an evidence packet:

- test input
- result
- screenshot/log placeholder
- framework mapping
- finding
- remediation
- validation step

## Finding Trigger

Create a finding if:

- evidence is missing
- evidence does not match the claim
- evidence is stale
- evidence lacks owner/date/system
- evidence proves only design intent, not operation

## CISO Sentence

> The organization cannot yet defend the AI control because the available evidence does not prove the control operated in the assessed workflow.

