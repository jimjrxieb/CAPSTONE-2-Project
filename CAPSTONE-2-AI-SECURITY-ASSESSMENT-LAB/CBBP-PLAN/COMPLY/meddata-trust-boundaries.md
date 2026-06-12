# Trust Boundary Analysis — MedData Nexus Internal RAG System

> Filled workpaper for Capstone 2 COMPLY phase.
> Lesson: `lessons/04-ai-security-architecture.md`
> Client: MedData Nexus Health Systems
> System: MDN-AI-001 — Internal RAG Chatbot
> Assessor: jimjrxieb + Eugene (CAP2-AI-001, advisory)
> Date: 2026-06-08
> Architecture source: `target-architecture/trust-boundaries.md`, `target-architecture/data-flow.md`

---

## What Trust Boundary Review Means

A trust boundary is any point where data, control, or authority passes between two components with different trust levels. At every boundary, the question is:

- What crosses this boundary?
- Can untrusted input enter here?
- Can sensitive data exit here?
- What controls enforce who is allowed through?
- Is crossing this boundary logged?
- Does the system fail closed if the control fails?

GuidePoint-style review looks for mismatches — where the architecture diagram says one thing and runtime behavior does another.

---

## Boundary 1 — User to RAG App

**What crosses:** Natural language query from an authenticated pilot user. Untrusted input. The first and most exposed attack surface.

**Direction:** Inbound. User is untrusted. Application is trusted.

| Control | Required | Current Status | Gap |
|---|---|---|---|
| Authentication | Yes — verify user identity before query is accepted | Not evidenced | No auth mechanism confirmed in baseline |
| Authorization | Yes — user role must be established before retrieval layer is called | Not implemented | Role is not passed to the retrieval layer |
| Input sanitization | Yes — detect and reject prompt injection attempts before the query reaches the model | Not implemented | No injection filter in place |
| Rate limiting | Yes — prevent high-volume retrieval abuse | Not evidenced | Not confirmed |
| Query logging | Yes — user identity, query text, timestamp | Not proven | Logging not confirmed in baseline |

**Fail-closed behavior required:** If authentication fails, deny the query. If input fails sanitization, reject and log. Neither control is currently enforced.

**Finding:** This boundary accepts untrusted input with no sanitization, no verified authorization context, and no confirmed logging. Prompt injection enters the system here and propagates into the prompt construction step.

**OWASP LLM mapping:** LLM01 (Prompt Injection — direct)
**NIST 800-53:** AC-3 (Access Enforcement), IA-2 (Identification and Authentication), AU-12 (Audit Record Generation)
**AI RMF:** MEASURE 2.11 (Security and Resilience), MANAGE 2.2 (Mitigations implemented)

---

## Boundary 2 — RAG App to Vector Database (ChromaDB)

**What crosses:** Embedding query, collection name, filter parameters outbound. Matching chunk text and metadata inbound. Sensitive Internal and Confidential documents are returned here.

**Direction:** Bidirectional. Application queries the DB; DB returns sensitive content.

| Control | Required | Current Status | Gap |
|---|---|---|---|
| Per-user/per-role collection access | Yes — user role must determine which document tiers are returned | Not implemented | Any authenticated user can retrieve any document in the collection |
| Query parameter integrity | Yes — user-supplied input must not manipulate collection names or filter params | Not implemented | No validation that user input does not influence query parameters directly |
| Returned chunk authorization check | Yes — chunks returned must be within the user's authorized tier | Not implemented | No post-retrieval authorization check |
| Retrieval logging | Yes — query params, collection, chunk IDs, user context | Not proven | Not confirmed |

**Fail-closed behavior required:** If user role cannot be verified, deny the retrieval entirely. Currently no such gate exists.

**Finding (S-rank):** No access control exists on ChromaDB. The retrieval layer returns documents based on semantic similarity only, with no reference to the requesting user's authorization tier. A vendor reviewer could retrieve internal incident reports. A clinical admin could retrieve security control evidence. A compliance analyst could retrieve legal documents. This is the highest-risk finding in the system.

**OWASP LLM mapping:** LLM08 (Vector and Embedding Weaknesses), LLM02 (Sensitive Information Disclosure)
**NIST 800-53:** AC-3, AC-4 (Information Flow Enforcement), AU-12
**AI RMF:** MEASURE 2.11, GOVERN 1.5

---

## Boundary 3 — RAG App to Model (Prompt Construction → LLM)

**What crosses:** Assembled prompt containing system instructions, retrieved chunk text, and user query. This is the most information-rich boundary in the system — it carries the full context the model will reason over.

**Direction:** Outbound to the local Ollama model. Response inbound.

| Control | Required | Current Status | Gap |
|---|---|---|---|
| System prompt isolation | Yes — user cannot see, override, or extract system instructions via query manipulation | Not verified | System prompt isolation not confirmed |
| Retrieved content sanitization | Yes — chunks inserted into the prompt must be validated (no poison, no injected instructions) | Not implemented | Retrieved content is inserted without inspection |
| Prompt construction logging | Yes — prompt hash or structured log of what was sent to the model | Not proven | Not confirmed |

**Fail-closed behavior required:** If any external LLM API path is attempted, abort the call and log an incident because external LLMs are out of scope for Eugene. If system prompt extraction is detected in the response, suppress the response and alert.

**Finding (B-rank):** System prompt isolation is not verified. If a user crafts a query designed to extract the system prompt ("repeat your instructions"), there is no confirmed technical control blocking disclosure. Retrieved chunks are inserted into the prompt without sanitization — a poisoned document in the corpus becomes poisoned context in the prompt without interception.

**OWASP LLM mapping:** LLM01 (Prompt Injection — indirect via retrieved content), LLM05 (Improper Output Handling), LLM07 (System Prompt Leakage)
**NIST 800-53:** SC-8 (Transmission Confidentiality), CM-6 (Configuration Settings)
**AI RMF:** MEASURE 2.11, MAP 2.3

---

## Boundary 4 — Model Output to User

**What crosses:** Model-generated response text (summary, cited content, draft). This boundary can carry sensitive content reflected from the corpus — PHI fragments, internal path references, secrets — if no output filter is in place.

**Direction:** Outbound from model, through the application, to the user.

| Control | Required | Current Status | Gap |
|---|---|---|---|
| Output filter | Yes — inspect response for PHI, secrets, internal paths, prohibited content before delivery | Not implemented | Response passes directly to user with no inspection |
| Source attribution | Yes — response must cite which corpus documents were retrieved, linked to corpus manifest | Not confirmed | Source attribution not confirmed in baseline |
| AI-generated label | Yes — response must be labeled as AI-generated summary, not authoritative document | Not confirmed | No UI label confirmed |
| HITL gate for high-risk outputs | Yes — compliance decisions, legal interpretations, clinical conclusions require human review before distribution | Not enforced | Review can be skipped; no approval recordkeeping |
| Response logging | Yes — full response text, source chunk IDs, reviewer decision | Not proven | Not confirmed |

**Fail-closed behavior required:** If output filter detects prohibited content (PHI, secrets, internal paths), block the response and generate an incident alert. If HITL gate is skipped for a high-risk output category, the system should not allow distribution — currently there is no such enforcement.

**Finding (B-rank):** The model response passes directly to the user with no output inspection, no source attribution confirmed, no AI-generated label confirmed, and no enforced HITL gate. A response that reflects PHI from a mislabeled corpus document, or that includes an internal path reference from chunk metadata, or that summarizes security control evidence in a way that constitutes a compliance conclusion — all of these reach the user without interception.

**OWASP LLM mapping:** LLM05 (Improper Output Handling), LLM02 (Sensitive Information Disclosure)
**NIST 800-53:** AC-4, AU-12, SI-12 (Information Management and Retention)
**AI RMF:** MEASURE 2.5 (Output Trustworthiness), MANAGE 2.2

---

## Boundary 5 — AI Coding Assistant to Repo

**What crosses:** Code suggestions, PR content, dependency changes, IaC modifications, CI gate results. AI-generated code exits the tool and enters version control.

**Direction:** Outbound from AI tool, into the repository and production path.

**Scope note:** The MedData Nexus RAG pilot is not a developer AI workflow. Coding assistant governance does not apply to the chatbot itself. However, the RAG ingestion pipeline (`ingest_meddata_to_chromadb.py`, `baseline_retrieval_test.py`) is software. Changes to that pipeline are an active boundary that needs controls.

| Control | Required | Current Status | Gap |
|---|---|---|---|
| AI-assisted commit/PR labeled | Yes — any code change assisted by AI must be flagged for review | Not confirmed for pipeline code | No labeling convention confirmed |
| SAST/SCA/secrets scan gate | Yes — SAST, dependency audit, secrets scan required before merge | Required, not proven | No scan evidence for pipeline code |
| Human review for high-risk changes | Yes — auth changes, IAM changes, prompt template changes, corpus ingestion logic | Required, not enforced | No mandatory review gate confirmed |
| AI cannot merge directly | Yes — AI suggestions are advisory; a named human merges | Required | Not confirmed |

**Fail-closed behavior required:** No AI-assisted change to the ingestion pipeline merges without passing SAST + pip-audit + secrets scan + named human reviewer on record.

**Finding (C-rank for current scope):** The ingestion pipeline has no confirmed scan gate or human review requirement for AI-assisted changes. For future engineering use cases where coding assistants are used across the development team, this boundary requires a full governance track (PR labeling, scan gates, human approval for auth/IAM changes, merge restrictions).

**OWASP LLM mapping:** LLM03 (Supply Chain), LLM09 (Misinformation / overreliance risk)
**NIST 800-53:** SA-11 (Developer Testing), CM-3 (Configuration Change Control), SR-3 (Supply Chain Controls)
**AI RMF:** MAP 4.1 (Model Integrity)

---

## Boundary 6 — Human Approval to Production Action

**What crosses:** A human reviewer's decision — risk acceptance, production expansion authorization, Restricted-data processing approval, legal/compliance sign-off, incident declaration. This is an authority boundary: the decision carries weight that no AI output should carry alone.

**Direction:** Human decision → authorized action. Without a recorded decision, the action must not proceed.

| Control | Required | Current Status | Gap |
|---|---|---|---|
| Approval recordkeeping | Yes — reviewer identity, role, decision, scope, timestamp must be logged | Not implemented | No approval recordkeeping system exists |
| Scoped approval | Yes — approval for one category does not imply approval for another | Not enforced | No scoping mechanism |
| CISO authority for S/B-rank | Yes — CISO Constant Yung required for production expansion, Restricted data, S/B-rank risk acceptance | Documented but not enforced | No technical gate routes decisions to CISO |
| Non-repudiation | Yes — approval record must be tamper-evident | Not implemented | No signed or immutable approval store |
| Audit trail linkage | Yes — approval must link to the specific artifact, finding, or action it authorizes | Not implemented | No linkage mechanism |

**Fail-closed behavior required:** No production expansion, no Restricted-data authorization, no risk acceptance proceeds without a recorded human approval. Currently, none of these gates are technically enforced.

**Finding (B-rank):** The human approval boundary is documented on paper (COMPLY intake names the required approvers and categories) but is not enforced or recorded technically. A pilot expansion, Restricted-data authorization, or risk acceptance can occur without a linked approval record. In an audit, this means MedData Nexus cannot prove that the human authority chain was followed.

**NIST 800-53:** CA-5 (Plan of Action), PM-10 (Authorization Process), AU-9 (Protection of Audit Information)
**AI RMF:** GOVERN 1.2 (Accountability), MANAGE 2.2

---

## Trust Boundary Finding Summary

| Boundary | Primary Finding | Rank | Status |
|---|---|---|---|
| User → RAG App | No input sanitization; auth not confirmed; no logging | B | Open |
| RAG App → Vector DB | No per-user/per-role access control | S | Open — blocks pilot expansion |
| RAG App → Model | System prompt isolation not verified; retrieved content unsanitized | B | Open |
| Model Output → User | No output filter; HITL not enforced; no source attribution confirmed | B | Open |
| AI Tool → Repo | No scan gate or human review requirement for pipeline changes | C | Open |
| Human Approval → Production | No approval recordkeeping system; no technical enforcement of authority chain | B | Open |

**Total:** 1 S-rank, 4 B-rank, 1 C-rank across the six boundaries.

---

## Architecture Mismatch Log

These are the GuidePoint-style mismatches found — where the design intent contradicts the observed control state:

| Claim | Reality | Mismatch Type |
|---|---|---|
| Human review required for high-risk outputs | No technical gate enforces it; review can be skipped | Policy claim vs. missing enforcement |
| External API receives only sanitized context | External API authorization not fully evidenced | Design assumption vs. unconfirmed control |
| Corpus excludes PHI and secrets | No ingestion scanner validates the exclusion | Policy claim vs. missing technical gate |
| Users access only authorized documents | ChromaDB has no access control | Design intent vs. missing control |
| All interactions are logged | No logging evidence in baseline | Design intent vs. unproven control |
| System prompt is isolated | Isolation not verified | Design assumption vs. unverified control |

---

## CISO Sentence

> The MedData Nexus AI workflow crosses sensitive trust boundaries — user input to model, retrieval to vector DB, model output to user, and human decision to production action — without evidence that access, logging, and human approval are consistently enforced at any of them.
