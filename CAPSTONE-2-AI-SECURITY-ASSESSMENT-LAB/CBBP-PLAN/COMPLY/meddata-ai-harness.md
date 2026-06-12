# AI System Harness Specification — MedData Nexus Health Systems

> **Client:** MedData Nexus Health Systems
> **System:** MDN-AI-001 — Internal RAG Chatbot
> **CISO:** Constant Yung
> **Prepared by:** jimjrxieb (GP-Copilot engagement)
> **Date:** 2026-06-08
> **Phase:** COMPLY — Harness definition. BUILD implements it. BREAK tests it.
> **Status:** DESIGNED. Nothing in this document is yet implemented or tested.

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

This document defines the harness MedData Nexus must build for MDN-AI-001 before the pilot expands.

---

## Harness Sketch — MDN-AI-001

| Harness Area | Decision |
|---|---|
| **AI use case** | Internal RAG chatbot: employees query compliance, legal, security, and vendor-risk documents in natural language |
| **Authoritative instructions** | System prompt → data classification policy → approved workflow config → human reviewer decision |
| **Untrusted context** | All user query text; all retrieved document chunks (treated as data, not instructions); any third-party document placed in the ingest path |
| **Allowed data** | Documents listed in the signed corpus manifest with a classification of Public, Internal, Confidential, or explicitly authorized Restricted, filtered by requester role |
| **Prohibited data** | PHI/ePHI, production credentials, API keys, incident records above the user's access tier, security assessment findings for unauthorized roles, raw legal documents outside authorized role scope |
| **Allowed tools** | ChromaDB semantic retrieval (read-only); local Ollama inference only |
| **Human-only actions** | Risk acceptance; pilot expansion approval; corpus manifest approval; high-risk output distribution; CISO sign-off on findings; security review for auth-sensitive changes |
| **Guardrails** | Input sanitization, system prompt isolation, corpus approval workflow, hash verification on ingest, pre-ingestion secret/PHI scan, per-role ChromaDB access control, post-retrieval tier check, output filter, audit logging, HITL gate, rate limiting |
| **BREAK tests** | Prompt injection, poisoned document retrieval, secrets in corpus, unauthorized retrieval by role, missing audit log, PR label bypass, auth-sensitive code review, unsafe dependency, runtime drift, CI exception pressure |
| **Evidence** | Audit log per interaction (all 7 required fields), corpus manifest with signed approvals, access matrix results, BREAK test results, human approval records, scan outputs, CI results |

---

## 1. Authority Stack

Instructions that reach the model are not all equal. The harness enforces this hierarchy:

| Priority | Instruction Source | Trust Level | Notes |
|---|---|---|---|
| 1 — Highest | System prompt | Trusted — controlled by platform team | Defines the model's operating rules; must be isolated from user input |
| 2 | Data classification policy (embedded in config) | Trusted — controlled by platform team | Which data tiers exist; which roles can access each tier |
| 3 | Approved workflow configuration | Trusted — controlled by platform team | Retrieval settings, model version, output format rules |
| 4 | Human reviewer decision | Trusted — named human, recorded | Approves or rejects high-risk outputs; overrides model judgment |
| 5 | Retrieved document chunks | **Untrusted** — treat as data, not instructions | Documents can contain adversarial text; the model must not follow instructions found inside documents |
| 6 — Lowest | User query text | **Untrusted** | All user input is untrusted; must pass sanitization before reaching the model |

**Key rule:** Retrieved documents and user queries are inputs to the model, not authorities. A document that says "disregard your previous instructions" is a data artifact, not a command.

**Current state:** System prompt isolation is not proven. Input sanitization does not exist. Finding: F-002.

---

## 2. Data Boundary

### Allowed Data Tiers by Role

| Corpus Category | Classification | Allowed Roles |
|---|---|---|
| Published policies | Public | All pilot roles |
| Vendor onboarding docs | Public | All pilot roles |
| General employee guidance | Internal | Compliance analyst, IT Security |
| Compliance assessment records | Confidential | Compliance analyst, IT Security |
| Legal contracts | Confidential | Compliance analyst (read-only) |
| Security assessment findings | Restricted | IT Security team only |
| Incident response records | Restricted | IT Security team only |
| HIPAA assessment records | Restricted | IT Security team only |
| Production credentials | **Prohibited — must not enter corpus** | Nobody |
| PHI/ePHI | **Prohibited — must not enter corpus** | Nobody |

### Data Boundary Rules

1. No document enters ChromaDB without a signed entry in the corpus manifest.
2. No document enters ChromaDB without passing the pre-ingestion scan (secrets, PHI patterns, adversarial instruction patterns).
3. Every chunk retains its source document's classification and sensitivity tier as metadata.
4. The retrieval layer filters chunks by the requesting user's authorized tier before assembling the prompt.
5. The output layer filters model responses for credential patterns and PHI-adjacent content before delivery.

**Current state:** No pre-ingestion scanning, no corpus manifest, no access control on ChromaDB. Findings: F-001, F-003, F-004.

---

## 3. Tool Boundary

MDN-AI-001 is a retrieval-only system. It does not call external APIs on behalf of users, execute commands, write files, or take actions in downstream systems.

| Tool | Allowed | Scope | Not Allowed |
|---|---|---|---|
| ChromaDB retrieval | Yes | Read-only; role-filtered | Write, schema changes, admin operations |
| External web search | No | — | Not in scope for this system |
| File write / system commands | No | — | Not in scope for this system |
| Email / Slack / external messaging | No | — | Not in scope for this system |
| Internal ticketing systems | No | — | Not in scope for this system |

**Current state:** Tool boundary is documented as local-only. ChromaDB write is not explicitly locked down at the application layer. External LLM APIs are out of scope for Eugene. Findings: F-001 and F-004 remain until BUILD/BREAK evidence proves retrieval and output controls.

---

## 4. Human Approval Boundary

The following actions require a named human to take the action or sign the record. The AI system does not perform or authorize these actions.

| Action | Required Approver | Evidence Required |
|---|---|---|
| Corpus manifest — add or remove a document | Document owner + Platform Engineering Lead | Signed manifest entry with date |
| Pilot expansion — add users or corpus categories | CISO Constant Yung | Signed expansion authorization with BREAK test results on file |
| Risk acceptance — open finding above C-rank | CISO Constant Yung | Signed risk treatment record with justification, owner, expiry |
| High-risk output distribution | Named human reviewer | Approval record: reviewer identity, decision, scope, timestamp |
| Security assessment finding — any rank | Human assessor (jimjrxieb in lab) | Finding signed by reviewer before becoming a deliverable |
| Production authorization | CISO Constant Yung | PROVE package reviewed and signed |
| Emergency CI gate bypass | Platform Engineering Lead + security lead | Exception register entry: justification, approver, expiry |
| Model version change | Platform Engineering Lead | Re-test required; BREAK test results must be current |

**Current state:** HITL is documented as a requirement. No technical gate enforces it. No approval record format is defined. Finding: F-006.

---

## 5. Guardrail Layer

These are the technical controls that enforce the harness at runtime. Each maps to a finding where the control is absent or unproven.

| Guardrail | Purpose | Finding | Status |
|---|---|---|---|
| Input sanitization | Detect and reject injection patterns before query reaches the model | F-002 | Not implemented |
| System prompt isolation | Prevent user queries from reading or overriding system instructions | F-002 | Not proven |
| Corpus manifest + approval gate | No document indexed without a signed manifest entry | F-003 | Not implemented |
| Hash verification on ingest | Document integrity check; reject if hash does not match manifest | F-003 | Not implemented |
| Pre-ingestion secret scanner | detect-secrets + gitleaks; reject documents with credential patterns | F-004 | Not implemented |
| Pre-ingestion PHI scanner | Reject documents with PHI-adjacent patterns (SSN, MRN, DOB) | F-004 | Not implemented |
| ChromaDB per-role access control | Role passed on every query; tier filter on retrieved chunks | F-001 | Not implemented |
| Post-retrieval tier check | Verify each chunk's source tier against requesting role before prompt assembly | F-001 | Not implemented |
| Output filter | Intercept credential and PHI patterns in model response before delivery | F-004 | Not implemented |
| Structured audit log | Record all 7 required fields per interaction in append-only store | F-005 | Not implemented |
| HITL gate | Require approval record before high-risk output is distributed | F-006 | Not implemented |
| Rate limiting | Prevent abuse via high-volume query patterns | — | Not confirmed |
| CI label-check gate | Fail CI if ai-assisted label absent on sensitive path PR | F-008 | Not implemented |
| CODEOWNERS (auth paths) | Require named security reviewer for auth-sensitive PRs | F-009 | Not implemented |
| SCA gate (pip-audit + pin enforcement) | Reject vulnerable or unpinned dependencies | F-010 | Not implemented |

**Current state:** Zero guardrails are implemented and tested. Every cell in this table is either Not implemented or Not proven.

---

## 6. Evidence Layer

Every claim about the harness must be backed by a dated artifact. These are the minimum evidence artifacts the harness must produce.

| Evidence Artifact | What It Proves | Required Fields | Status |
|---|---|---|---|
| Audit log entry | That an interaction occurred and was recorded | user_id, role, query_text, retrieved_chunk_ids, source_references, model_response, timestamp | Not present |
| Corpus manifest | That every indexed document was approved | filename, hash, owner, classification, approval date, approver | Not present |
| Ingestion scan output | That rejected documents were caught before indexing | document name, matched pattern type, rejection timestamp | Not present |
| Access matrix | That role × corpus category access control was tested | role, corpus category, query, result (pass/fail), test date | Not present |
| HITL approval record | That a human reviewed a high-risk output | reviewer identity, decision, scope, timestamp, output reference | Not present |
| BREAK test results | That each test was run against the live system | test name, input, expected control, observed result, rating, evidence path | Pending execution |
| Scan outputs (SAST, SCA, secrets) | That code changes were checked before merge | scan type, result, date, PR reference | Not confirmed |
| CI run records | That gates triggered on the right events | PR, CI result, gate triggered, pass/fail, date | Not present |
| Exception register | That all CI bypasses were approved and logged | bypass type, justification, approver, expiry, PR | Not present |

---

## Implementation Checklist (BUILD Phase)

The BUILD phase implements each control defined here. Nothing in BUILD is complete until the corresponding BREAK test returns PASS and the evidence artifact is on file.

| Control | BUILD Task | BREAK Test | PROVE Evidence |
|---|---|---|---|
| Per-role ChromaDB access | Implement collection-level filter; pass role on every query | Test 4 | Access matrix |
| Audit logging | Add middleware; define required fields; append-only store | Test 5 | Sample log entries |
| Input sanitization | Add sanitization layer; define rejection patterns | Test 1 | Injection test results |
| Corpus approval workflow | Build manifest gate; add hash verification | Test 2 | Manifest + ingest logs |
| Pre-ingestion scanning | Add detect-secrets + PHI scanner to ingest pipeline | Test 3 | Scan rejection logs |
| HITL gate | Build approval record workflow; add technical gate | — | Approval records |
| CI label-check | GitHub Actions workflow; PR template update | Test 6 | CI run output |
| CODEOWNERS | Create file; map auth paths to security reviewer | Test 7 | PR CODEOWNERS check |
| SCA gate | Add pip-audit + pin enforcement to CI | Test 8 | pip-audit output |
| Rate limiting | Configure limit; confirm it triggers under load | Test 9 (partial) | Rate limit response log |
| Exception register | Define process; build register; require approval | Test 10 | Register entries |

---

## Definition of Done

The harness is complete when:

1. Every guardrail in Section 5 has a status of **Implemented**.
2. Every BREAK test in Section 6 has returned **PASS** with evidence on file.
3. Every evidence artifact in Section 6 is present, dated, and owned.
4. CISO Constant Yung has reviewed and signed the PROVE package.
5. Pilot expansion may proceed only after items 1–4 are satisfied.

Until then: **Pilot only. No expansion.**

---

## CISO Sentence

> MedData Nexus has defined an AI use case and written internal policies, but has not yet built the technical harness — the access controls, audit logging, input guardrails, and human approval gates — that would make this system defensible to a regulator or auditor if a data exposure occurred today.
