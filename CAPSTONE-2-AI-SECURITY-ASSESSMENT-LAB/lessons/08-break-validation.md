# Lesson 08 - BREAK Validation

## What To Master

BREAK is where claims get tested.

Do not ask only:

> Does the policy exist?

Ask:

> What happens when someone tries to bypass it?

## Questions I Should Ask

- What control is supposed to stop this failure?
- How can I test it safely?
- What exact input or action triggers the test?
- What evidence will prove pass, partial, or fail?
- What would a false pass look like?
- What happens under pressure for speed?
- What happens when runtime differs from documentation?
- What near miss should become a new test?

## BREAK Tests To Master

- prompt injection
- RAG poisoned document
- secrets in corpus
- unauthorized retrieval
- AI-assisted PR label bypass
- auth-sensitive generated code
- unsafe dependency suggestion
- runtime drift
- missing audit logging
- CI exception pressure

## What I Need To Know

The best BREAK result is not always "pass."

A strong fail can be more valuable because it shows:

- the assessment found a real gap
- the risk can be explained
- remediation can be prioritized
- validation can be repeated

## Capstone Practice

Open:

- `scenarios/ai-runtime-drift.md`
- `scenarios/ai-assisted-pr-label-bypass.md`
- `evidence/README.md`

Task:

For one scenario, define:

- test command or manual step
- expected control
- observed result
- evidence path
- rating
- remediation

## Finding Trigger

Create a finding if:

- control cannot be tested
- control fails
- evidence is missing
- written claim contradicts runtime
- bypass succeeds without alert or approval

## CISO Sentence

> The control is documented, but the organization has not proven it works when users, runtime behavior, or delivery pressure challenge it.

