# Lesson 07 - Threat Modeling AI Workflows

**Status: COMPLETE — 2026-06-08**
**Deliverable:** `CBBP-PLAN/COMPLY/meddata-threat-model.md`

## What To Master

AI threat modeling asks:

> How can untrusted input, unsafe data, excessive authority, or human overtrust cause harm?

## Threat Categories

- prompt injection
- indirect prompt injection
- RAG poisoning
- secrets disclosure
- source leakage
- unauthorized retrieval
- tool misuse
- excessive agency
- unsafe dependency suggestion
- model/vendor outage
- runtime drift
- human approval bypass
- shadow AI

## Questions I Should Ask

- What are the assets?
- Who are the users?
- Who could abuse the workflow?
- What untrusted inputs enter the system?
- What data could be exposed?
- What decisions or actions can AI influence?
- What tools or APIs can AI reach?
- What controls assume humans will behave correctly?
- What happens when the team wants speed over review?
- What would an attacker try first?

## Evidence To Request

- data flow diagram
- trust boundary map
- user roles
- model/tool permissions
- RAG corpus controls
- API exposure
- logging and monitoring rules
- prior incident or near-miss records

## What I Need To Know

Use frameworks after the thinking, not before it.

Frameworks help organize the finding, but the threat model starts with the system:

- input
- context
- tools
- data
- output
- action
- human decision

## Capstone Practice

Pick one scenario and write the threat model in this format:

| Element | Answer |
|---|---|
| Asset | |
| Threat actor | |
| Entry point | |
| Trust boundary | |
| Failure mode | |
| Control expected | |
| Evidence needed | |

## Finding Trigger

Create a finding if:

- the client cannot name the AI threat path
- AI has access beyond the use case
- trust boundaries are assumed but not enforced
- no tests exist for likely abuse paths

## CISO Sentence

> The AI workflow has not been threat modeled against how attackers or users could manipulate inputs, retrieved context, tool access, or human trust.

