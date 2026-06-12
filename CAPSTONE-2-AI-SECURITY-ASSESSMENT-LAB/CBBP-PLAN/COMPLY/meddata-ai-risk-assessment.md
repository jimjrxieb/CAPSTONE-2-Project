# AI System Risk Assessment — MedData Nexus Internal RAG Chatbot

> Filled and scored workpaper for Capstone 2 COMPLY phase.
> Template: `templates/ai-risk-assessment.md`
> Maps to: MAP 3.5, MAP 5.1, GOVERN 1.3, GOVERN 1.4, RA-3
> Client: MedData Nexus Health Systems
> System Assessed: MDN-AI-001 — Internal RAG Chatbot
> Assessment Trigger: Initial — Capstone 2 engagement kickoff
> Risk posture: Preliminary inherent risk until BUILD/BREAK evidence confirms control behavior

---

## System Reference

| Field | Value |
|---|---|
| **System ID** | MDN-AI-001 |
| **System Name** | MedData Nexus Internal RAG Chatbot |
| **Assessment Date** | 2026-06-08 |
| **Assessor** | jimjrxieb + Eugene (CAP2-AI-001, advisory) |
| **Assessment Trigger** | Initial — first formal assessment of this system before any pilot expansion decision |
| **Risk Tier Going In** | High Risk (assigned at registration — validated below) |

---

## Section 1 — Intended Use vs Actual Capability

**Intended use (from registration):**
```
Internal RAG chatbot for compliance analysts, legal, IT security, vendor risk reviewers, 
and clinical administrative staff. Retrieves and summarizes approved Internal and 
Confidential-tier documents for human review. Read-only. No write access. No system 
actions. No external LLM API is in scope for Eugene. HITL required 
for all high-risk outputs.
```

**Capability gap analysis:**

| Intended Capability | Tested? | Test Method | Result |
|---|---|---|---|
| Returns only authorized documents | Planned | `scenarios/rag-unauthorized-retrieval.md` | NOT YET RUN — gap assumed open |
| Does not expose PHI or secrets | Planned | `scenarios/rag-secrets-in-corpus.md` | NOT YET RUN — gap assumed open |
| Resists direct prompt injection | Planned | `scenarios/rag-direct-prompt-injection.md` | NOT YET RUN — gap assumed open |
| Resists RAG poisoning via corpus | Planned | `scenarios/rag-poisoned-document.md` | NOT YET RUN — gap assumed open |
| Applies output filter before response delivery | Planned | `scenarios/rag-missing-output-filter.md` | NOT YET RUN — control not implemented |
| Enforces per-user/per-role vector DB access | Planned | `scenarios/rag-vector-db-access-gap.md` | NOT YET RUN — control not implemented |
| Logs all queries and responses | Not tested | Audit log review | NOT PROVEN — logging not confirmed in baseline |
| Attributes retrieved sources in responses | Not tested | Manual retrieval review | NOT CONFIRMED |
| Resists indirect prompt injection via poisoned doc | Planned | `scenarios/rag-direct-prompt-injection.md` (indirect variant) | NOT YET RUN |

---

## Section 2 — AI-Specific Risk Identification

Score = L × I. L and I rated 1–5. Score → Rank via GP-Copilot rank system.

These scores are preliminary inherent-risk scores based on COMPLY intake and known evidence gaps. They are not final validated findings until BUILD implementation records and BREAK test evidence confirm the control behavior.

### Likelihood and Impact Anchors

| Score | Likelihood Anchor | Impact Anchor |
|---|---|---|
| 1 | Requires exceptional access, rare timing, or highly specialized capability | Cosmetic issue or inconvenience; no sensitive data or governance effect |
| 2 | Requires privileged access, multiple steps, or uncommon system knowledge | Minor workflow disruption or limited internal correction |
| 3 | Plausible for an authenticated user or routine operator mistake | Confidential data, audit readiness, or business process impact |
| 4 | Likely through normal use, common misuse, or low-skill adversarial input | High-risk compliance, legal, security, or regulated workflow impact |
| 5 | Can occur through ordinary authorized use with no adversarial sophistication | Restricted/regulated data exposure, reportable incident, or pilot expansion blocker |

### NIST AI 600-1 Mapping Note

The risk group headings below are practical assessment dimensions. They map to NIST AI 600-1 GAI risk areas as follows:

| Assessment Dimension | Primary AI 600-1 Risk Area |
|---|---|
| Accuracy and Reliability | Confabulation; Information Integrity |
| Bias and Fairness | Harmful Bias and Homogenization |
| Privacy | Data Privacy |
| Robustness and Adversarial Inputs | Information Security; Information Integrity |
| Transparency and Explainability | Human-AI Configuration; Information Integrity |
| Security and Resilience | Information Security; Value Chain and Component Integration |

### Accuracy and Reliability

| Risk | L (1-5) | I (1-5) | Score | Rank | Mitigation |
|---|---|---|---|---|---|
| Retrieves irrelevant or out-of-scope chunks | 3 | 3 | 9 | C | Chunking strategy review, golden-question eval suite, metadata filters |
| Hallucinates document content not in corpus | 2 | 4 | 8 | C | RAG grounding (retrieved context must be cited), output source attribution required |
| Returns stale or superseded policy version | 3 | 3 | 9 | C | Corpus manifest with version control; document owner review before ingestion |
| Fails to retrieve relevant evidence when it exists | 2 | 4 | 8 | C | Retrieval eval — recall testing against expected-retrieval set |

### Bias and Fairness

| Risk | L (1-5) | I (1-5) | Score | Rank | Mitigation |
|---|---|---|---|---|---|
| Inconsistent retrieval across document types or categories | 3 | 2 | 6 | C | Eval suite tests same query across different corpus sections |
| Favors certain corpus sections due to chunking density | 2 | 2 | 4 | D | Normalized chunk sizes in ingestion pipeline |

### Privacy

| Risk | L (1-5) | I (1-5) | Score | Rank | Mitigation |
|---|---|---|---|---|---|
| PHI in indexed documents exposed via retrieval response | 3 | 5 | **15** | **B** | PHI exclusion in corpus boundary; ingestion validation; secret/PHI scanner on corpus before ingest |
| PII in chunk metadata visible to unauthorized users | 3 | 4 | **12** | **B** | Metadata schema review; strip PII from chunk metadata fields |
| Credentials or secrets in indexed documents retrieved | 3 | 5 | **15** | **B** | Secret scanning on corpus before ingest (`gitleaks`, `detect-secrets`); reject documents with detected secrets |

### Robustness and Adversarial Inputs

| Risk | L (1-5) | I (1-5) | Score | Rank | Mitigation |
|---|---|---|---|---|---|
| Direct prompt injection — attacker overrides system prompt via user query | 4 | 4 | **16** | **B** | System prompt isolation; input sanitization; prompt injection test suite |
| Indirect prompt injection via poisoned document in corpus | 3 | 4 | **12** | **B** | Corpus approval workflow; ingestion validation; document hash verification |
| RAG poisoning — attacker plants documents to steer responses | 2 | 5 | **10** | C | Corpus manifest with approval records; ingestion gating; document source verification |
| Source leakage — response reveals internal file paths, document names, or metadata | 4 | 3 | **12** | **B** | Output filter strips internal path references; source attribution limited to approved display fields |
| Adversarial input suppresses a correct finding or retrieval | 2 | 4 | 8 | C | RAG grounding — retrieved context fetched independently of query framing |

### Transparency and Explainability

| Risk | L (1-5) | I (1-5) | Score | Rank | Mitigation |
|---|---|---|---|---|---|
| No source attribution in response — user cannot verify what was retrieved | 4 | 3 | **12** | **B** | Source attribution required in every response; linked to corpus manifest entry |
| No audit log — queries and responses not recorded | 4 | 4 | **16** | **B** | Structured audit log: user query, retrieved chunk IDs, model response, tool path, review decision |
| User cannot distinguish AI summary from authoritative document | 3 | 3 | 9 | C | Response header must label output as AI-generated summary; source document link required |

### Security and Resilience

| Risk | L (1-5) | I (1-5) | Score | Rank | Mitigation |
|---|---|---|---|---|---|
| Per-user/per-role vector DB access control is not evidenced | 4 | 5 | **20** | **S** | Implement collection-level access control in ChromaDB; enforce user context on every retrieval call |
| Unauthorized retrieval — user accesses documents above their authorization tier | 3 | 5 | **15** | **B** | User role → document tier mapping; access control enforced at retrieval layer, not just UI |
| Output filtering is not evidenced — sensitive content may pass directly to response without inspection | 4 | 4 | **16** | **B** | Output filter layer required before response delivery; regex + LLM-based content inspection |
| External API receives unauthorized or unsanitized context | 2 | 4 | 8 | C | API boundary: only approved/sanitized context exits the internal environment; no raw corpus documents to external provider |

---

## Section 3 — Risk Score Summary

| Score | Rank | Action |
|---|---|---|
| 20-25 | S | Human only. Immediate escalation to CISO. |
| 12-19 | B | Human decides. Eugene provides intel. |
| 6-11 | C | Eugene proposes. Human approves. |
| 2-5 | D | Auto with logging. |
| 1 | E | Auto. |

**Top risks this assessment — ranked by score:**

| # | Risk | L | I | Score | Rank | Assigned To | Due |
|---|---|---|---|---|---|---|---|
| 1 | Vector DB access control not evidenced | 4 | 5 | **20** | **S** | Platform Engineering Lead | Before pilot expansion |
| 2 | Direct prompt injection | 4 | 4 | **16** | **B** | Platform Engineering Lead | 14 days |
| 3 | No audit logging | 4 | 4 | **16** | **B** | Platform Engineering Lead | 14 days |
| 4 | Output filter not evidenced | 4 | 4 | **16** | **B** | Platform Engineering Lead | 14 days |
| 5 | PHI exposed via retrieval | 3 | 5 | **15** | **B** | Compliance Director + Platform Eng | 7 days |
| 6 | Secrets in indexed documents retrieved | 3 | 5 | **15** | **B** | Platform Engineering Lead | 7 days |
| 7 | Unauthorized retrieval across user role | 3 | 5 | **15** | **B** | Platform Engineering Lead | 14 days |
| 8 | No source attribution in responses | 4 | 3 | **12** | **B** | Platform Engineering Lead | 14 days |
| 9 | Indirect prompt injection via poisoned doc | 3 | 4 | **12** | **B** | Platform Engineering Lead | 14 days |
| 10 | Source leakage in responses | 4 | 3 | **12** | **B** | Platform Engineering Lead | 14 days |

**S-rank count:** 1 → Immediate CISO escalation required. Pilot expansion blocked.
**B-rank count:** 9 → Human decision required. Eugene provides context. All route to CISO Constant Yung.
**C-rank count:** 6 → Eugene proposes mitigations. Human approves before implementation.

---

## Section 4 — Risk Acceptance or Treatment

### Risk MDN-RISK-001 — Vector DB Access Control Not Evidenced (Score 20, S-rank)

**Risk statement:** Per-user/per-role access control for ChromaDB retrieval is not evidenced in COMPLY. Until BUILD/BREAK proves otherwise, the assessment assumes any authenticated RAG chatbot user may be able to retrieve documents above their authorization level. A compliance analyst could retrieve legal documents; a clinical admin could retrieve security findings; a vendor reviewer could retrieve incident reports.

**Treatment choice:**
- [x] Mitigate: implement collection-level access control and user context enforcement at the retrieval layer

**Mitigation:**
```
1. Implement user role → document tier mapping in the retrieval service.
2. Pass authenticated user context on every ChromaDB query; filter results to authorized collections only.
3. Test with BREAK scenario: rag-vector-db-access-gap.md — confirm unauthorized tier docs are not returned.
4. Log every retrieval with user ID, role, query, and returned chunk IDs.
```

**Residual risk after mitigation:**
Likelihood: 2 × Impact: 5 = Score: 10 → Rank: C

**Accepted by:** CISO Constant Yung (required before pilot expansion — signature pending)

---

### Risk MDN-RISK-002 — PHI / Secrets in Indexed Documents Not Excluded by Evidence (Score 15, B-rank)

**Risk statement:** The corpus ingestion pipeline has not yet produced evidence proving that documents are free of PHI or secrets before indexing. A document containing real patient identifiers or credentials that is accidentally included in the corpus could become retrievable by chatbot users.

**Treatment choice:**
- [x] Mitigate: add PHI detection and secret scanning to the ingestion pipeline before any document is indexed

**Mitigation:**
```
1. Run detect-secrets and gitleaks on every document before ingest.
2. Run a PHI pattern scanner (regex for SSN, DOB, MRN formats) before ingest.
3. Reject and quarantine any document that fails either scan.
4. Require corpus manifest approval from data owner before ingest runs.
5. Test with BREAK scenario: rag-secrets-in-corpus.md.
```

**Residual risk after mitigation:**
Likelihood: 1 × Impact: 5 = Score: 5 → Rank: D

**Accepted by:** CISO Constant Yung (required — signature pending)

---

### Risk MDN-RISK-003 — Audit Logging Not Proven (Score 16, B-rank)

**Risk statement:** The RAG chatbot has not produced evidence proving that user queries, retrieved chunk IDs, model responses, and human review decisions are logged. If a data exposure incident occurs before logging is implemented and verified, there may be no forensic record to determine what was accessed, by whom, or when.

**Treatment choice:**
- [x] Mitigate: implement structured audit logging on every RAG interaction

**Mitigation:**
```
Structured log entry per interaction:
  - timestamp (ISO 8601)
  - user_id and role
  - query text
  - retrieved chunk IDs and source document references
  - model response (truncated or hashed if length is a concern)
  - tool/API path used
  - human review decision (if applicable) and reviewer ID
Store logs in tamper-resistant store (append-only); retain per HIPAA requirements.
```

**Residual risk after mitigation:**
Likelihood: 1 × Impact: 4 = Score: 4 → Rank: D

**Accepted by:** CISO Constant Yung (required — signature pending)

---

## Section 5 — AI RMF Subcategory Coverage After Mitigation

| AI RMF Subcategory | Current Status | Evidence | Post-Mitigation Target |
|---|---|---|---|
| GOVERN 1.1 (policies established) | PARTIAL | AI inventory registered; no formal AI use policy yet | PASS after policy published |
| GOVERN 1.2 (accountability) | PARTIAL | Owners defined by role; individual names pending | PASS after named owners documented |
| GOVERN 1.5 (risk tolerance) | FAIL | No risk tolerance statement | PASS after CISO signs risk acceptance |
| MAP 1.1 (context established) | PASS | Use case, users, data classes, and scope documented in COMPLY workpapers | Maintain |
| MAP 2.3 (limitations documented) | PARTIAL | Gaps documented in inventory; not yet communicated to users | PASS after user-facing limitation disclosure added to chatbot UI |
| MAP 3.1 (tested in context) | PARTIAL | Local mini-loop BREAK evidence exists; deployed/direct-access and embedding-layer tests remain open | PASS after full BREAK matrix completed |
| MEASURE 2.5 (output trustworthiness) | PARTIAL | Golden-question/helpfulness eval exists for the deterministic local draft path | PASS after full generation/retrieval eval suite is documented |
| MEASURE 2.7 (monitoring) | PARTIAL | Local structured audit log and review evidence exist; production monitoring cadence remains open | PASS after audit logging and monitoring cadence are implemented and verified |
| MEASURE 2.11 (security/resilience) | PARTIAL | Prompt injection, corpus contamination, unauthorized retrieval, HITL, and static platform checks have lab evidence | PASS after deployed direct-access, embedding-layer, and rapid-query BREAK scenarios pass |
| MANAGE 1.1 (risks prioritized) | PARTIAL | Risk register started; this document is the scored input | PASS after risk register finalized with this assessment |
| MANAGE 2.2 (HITL implemented) | FAIL | HITL not enforced | PASS after HITL review checkpoint implemented and tested |
| MANAGE 3.1 (incident response) | FAIL | No AI-specific IR plan | PASS after AI IR runbook written and tested |
| MANAGE 4.1 (post-deployment monitoring) | FAIL | No post-deployment monitoring planned | PASS after monitoring cadence defined and tooling in place |

---

## Risk Tier Determination

**Before mitigations:** 1 S-rank preliminary inherent risk, 9 B-rank preliminary inherent risks, 6 C-rank preliminary inherent risks.

**Risk tier: HIGH RISK.**

Production deployment is NOT authorized.

Pilot expansion requires:
1. S-rank (vector DB access control) → mitigated to C-rank
2. All B-rank findings → mitigated to C or lower
3. CISO Constant Yung sign-off on residual risk acceptance
4. All 12 BREAK scenarios executed with passing evidence
5. Audit logging implemented and verified
6. HITL enforcement implemented and tested

**After all mitigations (projected):**
Highest residual = D-rank. Risk tier: **Moderate Risk (pilot authorized with monitoring).**

Full production authorization requires an additional review cycle after 60-day monitored pilot.

---

## Assessor Notes

Eugene is the assessment brain for this engagement. All B/S-rank findings route to jimjrxieb for human review before inclusion in client deliverables. Eugene does not accept, reject, or sign off on risk — that authority belongs to CISO Constant Yung.

This document feeds:
- `CBBP-PLAN/PROVE/risk-register.md` — risk ID entries for each finding above
- `deliverables/02-client-findings-report.md` — translated into client-facing findings
- `deliverables/03-remediation-roadmap.md` — remediation sequence and milestones
- `deliverables/01-executive-summary.md` — CISO-level narrative
