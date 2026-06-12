# AI System Harness Specification — [CLIENT NAME]

> **Client:** [Client name and business unit]
> **System:** [System ID] — [System name and purpose]
> **System owner:** [Named owner]
> **Prepared by:** [Assessor name / engagement]
> **Date:** [YYYY-MM-DD]
> **Phase:** COMPLY — Harness definition. BUILD implements it. BREAK tests it.
> **Status:** [DESIGNED / PARTIALLY IMPLEMENTED / IMPLEMENTED / TESTED]

---

## What This Document Is

A harness is not a prompt. A harness is not a policy PDF.

A harness is the full control structure that surrounds your AI system and answers these questions with a technical artifact, not a verbal assurance:

- Who has authority to instruct the model?
- What data is the model allowed to see?
- What can the model do without a human in the loop?
- What requires a human to sign off?
- What controls enforce these rules at runtime?
- What logging proves the controls operated?
- What test proves the harness held under adversarial conditions?

If you cannot answer each of those questions with an artifact, you have instructions — not a harness.

---

## Harness Sketch — [SYSTEM ID]

| Harness Area | Decision |
|---|---|
| **AI use case** | [What the system does; who uses it; what decisions it influences] |
| **Authoritative instructions** | [Ordered list: e.g. system prompt → policy → approved workflow config → human reviewer decision] |
| **Untrusted context** | [What inputs are untrusted: user query text, retrieved docs, third-party content, etc.] |
| **Allowed data** | [What data tiers and categories the model is permitted to see] |
| **Prohibited data** | [What must never enter the model context: PHI, credentials, restricted-tier docs, etc.] |
| **Allowed tools** | [What actions the AI can take: retrieval, API calls, file read, etc.] |
| **Human-only actions** | [What the AI cannot decide alone: risk acceptance, production deployment, output distribution, etc.] |
| **Guardrails** | [Controls that enforce boundaries at runtime: input sanitization, access control, output filter, logging, etc.] |
| **BREAK tests** | [List of adversarial tests designed to verify each control] |
| **Evidence** | [Artifacts required to prove the harness operated: logs, scan outputs, approval records, test results] |

---

## 1. Authority Stack

Instructions that reach the model are not all equal. The harness enforces this hierarchy:

| Priority | Instruction Source | Trust Level | Notes |
|---|---|---|---|
| 1 — Highest | [E.g. System prompt] | Trusted | [Who controls it; isolation requirements] |
| 2 | [E.g. Client policy config] | Trusted | [What it governs] |
| 3 | [E.g. Approved workflow instructions] | Trusted | [Scope] |
| 4 | [E.g. Human reviewer decision] | Trusted | [Named human; recorded] |
| 5 | [E.g. Retrieved document chunks] | **Untrusted** | [Must not follow instructions found in documents] |
| 6 — Lowest | [E.g. User query text] | **Untrusted** | [Must pass sanitization before reaching model] |

**Key rule:** [State the authority rule for this system — e.g. "Retrieved documents are inputs, not commands."]

**Current state:** [IMPLEMENTED / NOT PROVEN / NOT IMPLEMENTED] — [Finding reference if applicable]

---

## 2. Data Boundary

### Allowed Data Tiers by Role

| Data Category | Classification | Allowed Roles |
|---|---|---|
| [Category] | [Public / Internal / Confidential / Restricted / Prohibited] | [Role names or "All" or "Nobody"] |
| [Category] | | |
| [Category] | | |
| [Prohibited category — must not enter system] | **Prohibited** | Nobody |

### Data Boundary Rules

1. [Rule 1 — e.g. no document enters the corpus without manifest approval]
2. [Rule 2 — e.g. all documents must pass pre-ingestion scanning]
3. [Rule 3 — e.g. every chunk retains its classification tier as metadata]
4. [Rule 4 — e.g. retrieval filters by user role before prompt assembly]
5. [Rule 5 — e.g. output layer filters before delivery to user]

**Current state:** [IMPLEMENTED / NOT PROVEN / NOT IMPLEMENTED] — [Finding references]

---

## 3. Tool Boundary

| Tool | Allowed | Scope | Not Allowed |
|---|---|---|---|
| [Tool name] | Yes / No | [What it can do] | [What it cannot do] |
| [Tool name] | Yes / No | | |

**Current state:** [IMPLEMENTED / NOT PROVEN / NOT IMPLEMENTED] — [Finding references if applicable]

---

## 4. Human Approval Boundary

The following actions require a named human to take the action or sign the record. The AI system does not perform or authorize these actions.

| Action | Required Approver | Evidence Required |
|---|---|---|
| [Action] | [Named role] | [Record type with required fields] |
| [Action] | | |
| [Action] | | |

**Current state:** [IMPLEMENTED / NOT PROVEN / NOT IMPLEMENTED] — [Finding reference]

---

## 5. Guardrail Layer

| Guardrail | Purpose | Finding | Status |
|---|---|---|---|
| [Guardrail name] | [What it prevents] | [Finding ID or —] | [Not implemented / Not proven / Implemented] |
| [Guardrail name] | | | |

**Current state:** [Summary — e.g. X of Y guardrails implemented and tested.]

---

## 6. Evidence Layer

| Evidence Artifact | What It Proves | Required Fields | Status |
|---|---|---|---|
| [Artifact name] | [Claim it supports] | [Required fields] | [Present / Not present / Pending] |
| [Artifact name] | | | |

---

## Implementation Checklist (BUILD Phase)

| Control | BUILD Task | BREAK Test | PROVE Evidence |
|---|---|---|---|
| [Control] | [What must be built] | [Test number or name] | [Evidence artifact] |
| [Control] | | | |

---

## Definition of Done

The harness is complete when:

1. Every guardrail in Section 5 has a status of **Implemented**.
2. Every BREAK test in the Implementation Checklist has returned **PASS** with evidence on file.
3. Every evidence artifact in Section 6 is present, dated, and owned.
4. [Named approver] has reviewed and signed the PROVE package.
5. [Scale condition] may proceed only after items 1–4 are satisfied.

Until then: **[Current authorization level — e.g. Pilot only. No expansion.]**

---

## CISO Sentence

> [Organization] has [current state — e.g. defined an AI use case and written internal policies], but has not yet built the technical harness — [missing controls] — that would make this system defensible to a regulator or auditor if a [risk event] occurred today.
