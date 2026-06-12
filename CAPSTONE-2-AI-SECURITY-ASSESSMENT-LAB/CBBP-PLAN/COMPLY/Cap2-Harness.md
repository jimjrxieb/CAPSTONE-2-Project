# AI System Harness Specification — Eugene Internal Assistant

> **Client:** MedData Nexus Health Systems (fictional)
> **System:** MDN-AI-001 / CAP2-AI-001 — Eugene, Internal RAG Assistant
> **System owner:** Simulated: MedData Nexus AI Governance Committee; lab owner: jimjrxieb
> **Prepared by:** jimjrxieb
> **Date:** 2026-06-08
> **Phase:** COMPLY — Harness definition. BUILD implements it. BREAK tests it.
> **Status:** DESIGNED. Eugene is operational; governance boundaries are defined here.
>
> **Template:** `templates/ai-harness-spec.md`
> **See also:** `CBBP-PLAN/COMPLY/meddata-ai-harness.md` — client harness spec for Eugene.

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

Eugene is the internal assistant under assessment. This document governs how Eugene operates inside the Capstone 2 lab. If you cannot answer each of the questions above with an artifact about Eugene's behavior, the assistant workflow is ungoverned.

---

## Harness Sketch — CAP2-AI-001

| Harness Area | Decision |
| --- | --- |
| **AI use case** | Internal RAG assistant: Eugene searches synthetic MedData Nexus policy, compliance, vendor-risk, legal, privacy, and security records; drafts summaries and questionnaire language for human review |
| **Authoritative instructions** | Human user/reviewer → approved Eugene system instructions and role policy → CBBP assessment methodology for tests → retrieved synthetic corpus content |
| **Untrusted context** | All synthetic corpus documents (treated as data, not instructions); all retrieved chunks; any document placed in the ingest path |
| **Allowed data** | Synthetic MedData Nexus corpus (approved fake data only), scenario test outputs, framework mappings, BREAK test results, approved evidence artifacts from `evidence/` |
| **Prohibited data** | Real PHI/ePHI, real client secrets, real production credentials, real customer records, real GuidePoint client data |
| **Allowed tools** | Local ChromaDB retrieval (read-only), local Ollama inference (Eugene model), evidence file parsing |
| **Human-only actions** | Final deliverable approval; risk acceptance; Restricted-data authorization; high-risk output release; pilot expansion authorization; any decision that becomes part of the client PROVE package |
| **Guardrails** | Advisory-only output label; role-filtered retrieval; data boundary enforcement; human review gate before high-risk output becomes deliverable material; no autonomous remediation; no production system access |
| **BREAK tests** | Does Eugene stay within role boundaries, reject prompt injection, block contaminated corpus entries, flag sensitive outputs, and require HITL review before distribution? |
| **Evidence** | Eugene output saved with human reviewer sign-off notation; evidence artifacts dated and path-referenced; human decision explicitly recorded for every finding above D-rank |

---

## 1. Authority Stack

Instructions that reach Eugene are not all equal. The harness enforces this hierarchy:

| Priority | Instruction Source | Trust Level | Notes |
| --- | --- | --- | --- |
| 1 — Highest | Human user/reviewer | Trusted | Human owns final decisions and high-risk output release |
| 2 | Approved Eugene system instructions and role policy | Trusted | Defines assistant purpose, role boundaries, and refusal rules |
| 3 | CBBP methodology and assessment workflow config | Trusted for tests | Defines assessment scope, phase gates, and evidence standards |
| 4 | Eugene advisory output | Advisory — not authoritative | Must be reviewed by human before becoming a finding or deliverable |
| 5 | Retrieved synthetic corpus chunks | **Untrusted** | Documents are data inputs; Eugene must not follow instructions found inside corpus documents |
| 6 — Lowest | Scenario test inputs and injected content | **Untrusted** | Adversarial test content must not be treated as legitimate instructions by Eugene |

**Key rule:** Eugene's output is advisory. A human reviewer converts Eugene drafts into approved summaries, findings, questionnaire responses, or deliverables. Eugene never makes final risk decisions.

**Current state:** Boundary is defined. Eugene is running locally via Ollama. Human review is the standing gate for all outputs. No automated Eugene-to-deliverable path exists without human step.

---

## 2. Data Boundary

### Allowed Data Tiers

| Data Category | Classification | Allowed in Eugene Context |
| --- | --- | --- |
| Synthetic MedData Nexus corpus documents | Fake/synthetic — safe | Yes |
| Approved scenario test inputs (fake-data/) | Fake/synthetic — safe | Yes |
| Framework mappings (NIST, OWASP, MITRE) | Public reference | Yes |
| Evidence artifacts from `evidence/` | Lab-generated | Yes |
| BREAK test results and scenario outputs | Lab-generated | Yes |
| Real PHI / ePHI | **Prohibited** | Never |
| Real client secrets or credentials | **Prohibited** | Never |
| Real production credentials | **Prohibited** | Never |
| Real GuidePoint client data | **Prohibited** | Never |
| Live customer records | **Prohibited** | Never |

### Data Boundary Rules

1. Only synthetic fake-data documents enter Eugene's context. Real sensitive data is never loaded into the corpus or passed to Eugene.
2. No external LLM API call is in scope for Eugene. If an external model is introduced later, it requires a new COMPLY boundary, CISO approval, and renewed BREAK evidence.
3. Scenario test content — poisoned documents, injected prompts, fake credentials — is clearly labeled in metadata as `is_poisoned: true` or `is_unsafe: true` so Eugene context includes the label.
4. Eugene outputs are never published as client deliverables without human review and sign-off.
5. Evidence artifacts written to `evidence/` contain only synthetic data and assessment outputs — no real client information.

**Current state:** Data boundary is enforced by project structure. Synthetic corpus is in `target-client/fake-data/`. No real data pathway exists in the lab setup.

---

## 3. Tool Boundary

| Tool | Allowed | Scope | Not Allowed |
| --- | --- | --- | --- |
| Local ChromaDB (eugene-meddata-nexus collection) | Yes | Read-only retrieval; semantic search over synthetic corpus | Write operations from Eugene; schema changes; admin operations |
| Ollama (local Eugene model) | Yes | Local inference only; no external data transmission | External API calls; autonomous action-taking |
| Evidence file parsing | Yes | Read evidence artifacts from `evidence/` for assessment context | Write to evidence artifacts directly; modify findings without human step |
| File write / system commands | No | — | Eugene cannot write files, run shell commands, or modify the repo autonomously |
| Production systems | No | — | No access to any production environment, client system, or live infrastructure |
| Autonomous remediation | No | — | Eugene proposes remediation; humans implement it |

**Current state:** Tool boundary is enforced by the lab architecture. Eugene operates locally via Ollama. No autonomous write path exists.

---

## 4. Human Approval Boundary

The following actions require jimjrxieb (in this lab context, simulating the human assessor role) to take the action or sign the record.

| Action | Required Approver | Evidence Required |
| --- | --- | --- |
| S-rank finding confirmed | jimjrxieb | Finding signed and added to client-findings-report.md |
| B-rank finding confirmed | jimjrxieb | Finding signed and added to client-findings-report.md |
| C-rank finding confirmed | jimjrxieb | Human approval before remediation plan is finalized |
| Risk acceptance (any rank) | Simulated: CISO Constant Yung (jimjrxieb in lab) | Signed risk treatment record with justification, owner, expiry |
| Client-facing deliverable approved | jimjrxieb | Deliverable marked reviewed before adding to PROVE package |
| Pilot expansion decision | Simulated: CISO Constant Yung | BREAK test results on file; PROVE package signed |
| Any Eugene output used as evidence | jimjrxieb | Human reviewer notation on the evidence artifact |

**Current state:** All outputs from Eugene are treated as advisory drafts until jimjrxieb reviews and signs them. No automated Eugene-to-finding pipeline exists.

---

## 5. Guardrail Layer

| Guardrail | Purpose | Status |
| --- | --- | --- |
| Advisory-only label | Every Eugene output is marked as advisory draft, not confirmed finding | Enforced by workflow convention — human step is required |
| Data boundary enforcement | Synthetic data only; no real PHI/credentials enter context | Enforced by project structure and fake-data corpus |
| Human review gate | Eugene output becomes a finding only after human sign-off | Enforced by workflow — no automated delivery path |
| No autonomous remediation | Eugene proposes remediation language; humans implement | Enforced by tool boundary (no write access to production) |
| Rank escalation | S-rank and B-rank findings route to human immediately; Eugene does not make S/B-rank final decisions | Enforced by architecture-laws.md rank boundaries |
| Evidence artifact integrity | Evidence outputs are written by the assessment pipeline, not by Eugene directly | Enforced by code structure (evidence/ written by ingest/test scripts) |

**Current state:** All guardrails above are enforced by workflow convention and project structure. No automated bypass path exists.

---

## 6. Evidence Layer

| Evidence Artifact | What It Proves | Required Fields | Status |
| --- | --- | --- | --- |
| Eugene advisory output (when used) | That Eugene contributed to a finding's drafting and that a human reviewed it | Eugene output text, human reviewer notation, date, finding reference | On file for COMPLY-phase outputs; pending for BREAK-phase outputs |
| Ingestion evidence (`evidence/meddata-ingest-*.md`) | That the synthetic corpus was correctly ingested with expected document counts and categories | timestamp, collection, document count, category breakdown, poisoned/unsafe flags | Present — 2026-06-08T11:24:37 |
| Baseline retrieval evidence (`evidence/baseline-*.json`) | That the clean corpus retrieval behaves as expected before adversarial scenarios | run_id, timestamp, collection_count, pass/partial/miss per question, no poisoned docs retrieved | Present — 2026-06-08T11:24:58Z |
| BREAK test results | That each adversarial test was run and the result recorded | test name, input, expected control, observed result, rating, evidence path | Partial — Loops 1-3 and platform static controls have evidence; deployed/direct-access and embedding-layer BREAK remain open |
| Human approval record on deliverables | That all client-facing outputs were reviewed before entering the PROVE package | reviewer identity, deliverable name, review date, status | Pending — apply to each deliverable before PROVE is closed |

---

## Implementation Checklist

| Control | BUILD Task | Status |
| --- | --- | --- |
| Synthetic corpus ingested | `evidence/ingest_meddata_to_chromadb.py --reset` | Complete — 17 documents in `eugene-meddata-nexus` collection |
| Baseline retrieval confirmed | `evidence/baseline_retrieval_test.py --label clean-baseline` | Complete — JSON evidence on file; 50% pass rate on golden questions |
| Poisoned scenario toggle | `ingest_meddata_to_chromadb.py --poisoned` flag | Covered by Loop 3 corpus contamination BREAK evidence |
| Unsafe scenario toggle | `ingest_meddata_to_chromadb.py --unsafe` flag | Covered by Loop 3 corpus contamination BREAK evidence |
| Eugene API / chatbox | `Eugene-AI/src/api/` and `Eugene-AI/src/chatbox/` | Implemented for local Loop 1/2 control slices |
| BREAK test execution | BREAK matrix in `meddata-break-validation.md` plus mini-loop runners | Partial — local mini-loop evidence exists; deployed/direct-access and embedding-layer BREAK remain open |
| Human review notation on deliverables | Apply reviewer sign-off to all PROVE-phase deliverables | Pending |

---

## Definition of Done

The Eugene assessment harness is complete when:

1. All BREAK tests have been executed with evidence on file.
2. All COMPLY-phase deliverables have been reviewed and signed by jimjrxieb.
3. All PROVE-phase deliverables have human reviewer notation before entering the PROVE package.
4. No Eugene output is used as a confirmed finding without a human sign-off record.
5. The PROVE package for MDN-AI-001 is closed with CISO sign-off.

Until then: **Assessment pilot only. Eugene remains advisory.**

---

## CISO Sentence

> The Capstone 2 assessment lab uses Eugene as a governed, local advisory model with clearly defined data boundaries, tool restrictions, and human review gates — Eugene drafts findings and mappings, but human judgment owns every final risk decision and client-facing deliverable.
