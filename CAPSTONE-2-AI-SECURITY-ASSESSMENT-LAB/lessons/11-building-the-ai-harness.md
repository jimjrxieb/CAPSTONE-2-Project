# Lesson 11 - Building The AI Harness

**Status: COMPLETE — 2026-06-08**
**Deliverable:** `CBBP-PLAN/COMPLY/meddata-ai-harness.md`
- Client-facing AI harness specification for MDN-AI-001 (the MedData Nexus RAG chatbot)
- Covers all 6 harness components: authority stack, data boundary, tool boundary, human approval boundary, guardrail layer, evidence layer
- Maps every guardrail to its finding (F-001 through F-010) and its BREAK test
- Includes BUILD implementation checklist and definition of done
- Note: `Cap2-Harness.md` in COMPLY governs Eugene (the assessment tool, CAP2-AI-001) — a separate document; `meddata-ai-harness.md` governs the client system being assessed

## What To Master

An AI harness is the control layer around the model.

It is how a company turns prompting into governed work.

The model is not the harness. The prompt is not the harness. The harness is the full structure that decides:

- what instructions have authority
- what context is trusted or untrusted
- what data the AI can see
- what tools the AI can use
- what actions require human approval
- what gets logged
- what tests prove the workflow works
- what evidence supports the final decision

## Simple Definition

> An AI harness is the governed workflow that connects human intent, policy, prompts, data, tools, guardrails, approvals, tests, and evidence.

## Why This Matters To GuidePoint

A client does not only need help writing prompts.

A client needs help answering:

- Can our employees use AI safely?
- Can our engineers use coding assistants without exposing sensitive data?
- Can our RAG system retrieve only authorized information?
- Can our agents use tools without excessive authority?
- Can we prove human review happened?
- Can we detect when the live system drifts from the written policy?

That is harness work.

## Prompt Versus Harness

| Layer | What It Does | Risk If Missing |
|---|---|---|
| Prompt | Expresses intent or instruction | AI may misunderstand or over-follow weak instructions |
| Policy-as-prompt | Turns rules into model instructions | Prompt can be bypassed or contradicted by context |
| Harness | Enforces workflow boundaries around the AI | No reliable control, evidence, or accountability |

Key phrase:

> A prompt asks the AI to behave. A harness makes the workflow governable.

## Harness Components

### 1. Authority Stack

Define which instructions win.

Example order:

1. System/developer rules
2. Client policy
3. Approved workflow instructions
4. Human task request
5. Retrieved documents and files
6. Tool outputs
7. Untrusted user input

Security point:

> Files, comments, tickets, logs, and retrieved documents can be prompt-shaped, but they should not automatically have authority.

### 2. Data Boundary

Define what the AI can see.

Questions:

- Can the AI see source code?
- Can it see customer data?
- Can it see PHI, PII, secrets, contracts, or incident records?
- Is data sent to a vendor?
- Is it logged?
- Is it retained?
- Is it used for training?

### 3. Tool Boundary

Define what the AI can do.

Questions:

- Can it read files?
- Can it write files?
- Can it run commands?
- Can it call APIs?
- Can it open PRs?
- Can it modify infrastructure?
- Can it access production?

### 4. Human Approval Boundary

Define what AI cannot decide alone.

Human-only examples:

- risk acceptance
- production deployment
- disabling a security control
- approving auth changes
- approving new high-risk dependencies
- sharing sensitive client data
- final compliance claims

### 5. Guardrail Layer

Guardrails are the controls that constrain the workflow.

Examples:

- input validation
- output validation
- prompt injection checks
- secret scanning
- SAST/SCA/IaC checks
- dependency review
- CODEOWNERS
- PR labels
- rate limits
- RAG source filtering
- vector database access controls
- tool allowlists

### 6. Evidence Layer

The harness must prove what happened.

Evidence examples:

- prompt and output logs
- retrieved document IDs
- tool-call logs
- CI results
- PR review notes
- human approval record
- scanner output
- test results
- runtime configuration checks
- findings and remediation records

## Questions I Should Ask

- What is the AI being asked to do?
- Which instructions have authority?
- Which context is untrusted?
- What data can the AI see?
- What tools can the AI use?
- What actions require human approval?
- What controls enforce the policy?
- What tests try to break the harness?
- What logs prove the workflow operated correctly?
- What decision does the evidence support: pilot, scale, remediate, or pause?

## What I Need To Know

The harness is where AI adoption becomes real.

Without a harness:

- policy stays theoretical
- prompts become fragile
- AI output is over-trusted
- tools can be over-permissioned
- human review can be skipped
- evidence is incomplete

With a harness:

- AI work has boundaries
- controls can be tested
- failures can be detected
- humans retain authority
- leadership can make evidence-backed decisions

## CBBP Mapping

| CBBP Phase | Harness Work |
|---|---|
| COMPLY | Define authority, policy, data boundaries, human-only decisions, and evidence requirements |
| BUILD | Implement prompts, configs, tool permissions, CI gates, logging, and approval workflows |
| BREAK | Test prompt injection, tool misuse, bypasses, unsafe dependencies, auth changes, and runtime drift |
| PROVE | Package logs, results, findings, mappings, approvals, and scale/no-scale recommendation |

## Capstone Practice

Open:

- `deliverables/04-ai-adoption-operating-model.md`
- `templates/ai-adoption-intake-questionnaire.md`
- `scenarios/ai-assisted-pr-label-bypass.md`
- `scenarios/ai-runtime-drift.md`

Task:

Create a harness sketch for one workflow:

| Harness Area | Answer |
|---|---|
| AI use case | |
| authoritative instructions | |
| untrusted context | |
| allowed data | |
| prohibited data | |
| allowed tools | |
| human-only actions | |
| guardrails | |
| BREAK tests | |
| evidence | |

## Finding Trigger

Create a finding if:

- the client has prompts but no enforcement
- files or retrieved documents can override policy
- AI tool access is over-broad
- human approval is required by policy but not recorded
- logs cannot reconstruct prompts, outputs, retrieval, or tool calls
- the harness cannot prove whether controls operated

## CISO Sentence

> The organization has AI instructions, but not yet a complete harness that proves data boundaries, tool permissions, human approvals, and runtime controls are operating as intended.

## Daily Drill

Finish this sentence:

> A prompt tells AI what to do, but a harness...

