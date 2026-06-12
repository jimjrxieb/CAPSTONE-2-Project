# RAG Corpus Intake — MedData Nexus Health Systems

> Filled workpaper for Capstone 2 COMPLY phase.
> Lesson: `lessons/05-rag-and-data-security.md`
> Client: MedData Nexus Health Systems
> System: MDN-AI-001 — Internal RAG Chatbot
> Assessor: jimjrxieb + Eugene (CAP2-AI-001, advisory)
> Date: 2026-06-08

---

## RAG Corpus Intake Questions — MedData Nexus Answers

| Question | MedData Nexus Answer |
|---|---|
| What documents are in the corpus? | Policies, compliance evidence, SOC 2 summaries, HIPAA assessment records, vendor-risk documents, legal/BAA templates, security findings, sanitized incident records. Full list in `target-client/fake-data/corpus-manifest.md`. |
| Who approved them for ingestion? | Data owners by category: Legal (legal/BAA templates), Compliance (compliance evidence, HIPAA records), Security (security findings, sanitized incident records), Privacy (HIPAA assessment records), Vendor Risk (vendor-risk documents). Individual owner names pending — roles identified only. |
| What sensitivity level do they have? | Classification is controlled by `target-client/fake-data/corpus-manifest.md`. The current lab corpus includes Public, Internal, Confidential, and explicitly authorized Restricted records. PHI/ePHI, real patient identifiers, credentials, and secrets remain explicitly prohibited unless a Restricted-data use case is separately approved and documented. |
| Is PII, PHI, secrets, legal text, or customer data present? | PHI-adjacent content is present (HIPAA policy documents, HIPAA assessment records). Real PHI is prohibited but ingestion validation to enforce this is not implemented. Legal text (BAA templates, vendor agreements) is in scope. No real credentials or secrets should be present. |
| How are documents chunked and tagged? | Documents split into chunks by the ingestion pipeline (`evidence/ingest_meddata_to_chromadb.py`). Each chunk tagged with: source document name, document tier, corpus category, owner role, ingest timestamp. |
| Can users retrieve documents they should not see? | Yes — ChromaDB has no per-user/per-role access control. Any authenticated user can retrieve any document in the collection. S-rank finding. |
| Can poisoned documents enter the corpus? | Yes — no ingestion validation or document hash verification exists. Any file placed in the ingest directory is indexed. |
| Are citations or source references validated? | Not confirmed. Source attribution in responses is not verified in baseline. |
| Are outputs filtered before display? | No. No output filter layer is implemented. Responses pass directly to the user. |
| Are retrieval events logged? | Not proven. Logging is planned but no audit log evidence exists in baseline. |

---

## Evidence Requested — Status

| Evidence Artifact | Required | Current Status | Gap |
|---|---|---|---|
| Corpus manifest — approved documents with data owner sign-off | Yes | Present — `target-client/fake-data/corpus-manifest.md` | BUILD must enforce owner, approver, approval date, classification, and purpose fields |
| Ingestion logs — record of every document indexed | Yes | Not confirmed | No logging evidence for the ingestion pipeline |
| Document owner list — named individual per corpus category | Yes | Roles identified; individual names pending | Owner names must be assigned before pilot expansion |
| Sensitivity classification — tier per document | Yes | Defined in corpus manifest | BUILD must reject missing or contradictory manifest metadata |
| Vector DB ACLs — per-user/per-role collection access | Yes | Not implemented | S-rank finding — blocks pilot expansion |
| Retrieval filter code — code that enforces user role on query | Yes | Not implemented | No retrieval filter exists |
| Prompt template — current system prompt version | Yes | Exists; version history and isolation not verified | System prompt isolation not confirmed |
| Output sanitizer code | Yes | Not implemented | No output filter layer |
| RAG test results — prior prompt injection or retrieval tests | Yes | Not executed | All BREAK scenarios are planned, none run |
| Audit logs — query, retrieved chunks, response, reviewer | Yes | Not proven | Logging not confirmed in baseline |

---

## Evidence Gaps — Finding Triggers

| # | Gap | Finding Trigger | Rank |
|---|---|---|---|
| 1 | No corpus manifest with signed data owner approval | Cannot prove documents are authorized for ingestion | B |
| 2 | No ingestion logs | Cannot prove what was indexed or when | B |
| 3 | No vector DB ACLs | Any user retrieves any document — no access enforcement | S |
| 4 | No retrieval filter code | User role is not applied to retrieval query | S |
| 5 | No output sanitizer | Sensitive content reaches user without inspection | B |
| 6 | No RAG test results | Controls are claimed but never validated | B |
| 7 | No audit logs | No forensic trail if data exposure occurs | B |
| 8 | Prompt template isolation unverified | System prompt may be extractable by adversarial query | B |

---

## Corpus Ownership Matrix

| Category | Corpus Documents | Required Owner | Owner Named? |
|---|---|---|---|
| Compliance | Compliance evidence, SOC 2 summaries | Compliance Director | Role only — individual pending |
| Legal | BAA templates, vendor agreements | Legal Counsel | Role only — individual pending |
| Healthcare/Privacy | HIPAA assessment records, privacy policies | Privacy Officer | Role only — individual pending |
| Security | Security findings, sanitized incident records | CISO / IT Security | CISO = Constant Yung |
| Vendor Risk | Vendor-risk documents, vendor questionnaires | Vendor Risk Lead | Role only — individual pending |

**Requirement:** All individual owners must be named and must sign the corpus manifest before any document in their category is indexed. This is a COMPLY exit criterion.

---

## COMPLY Exit Criteria for RAG Corpus

| Criterion | Status |
|---|---|
| Corpus manifest created and approved by named data owners | Not complete — individual names pending |
| Prohibited data list explicit and enforced | Documented, not technically enforced |
| Vector DB access control implemented and tested | Not implemented |
| Output filter implemented and tested | Not implemented |
| Audit logging proven with a sample log entry | Not proven |
| At least one RAG BREAK scenario executed with evidence | Not executed |

**Status: COMPLY requirements documented and manifest source of truth declared. Technical enforcement belongs to BUILD/BREAK evidence — do not expand pilot until controls are proven.**
