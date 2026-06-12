# Capstone 2 COMPLY Workpaper

## Purpose

COMPLY defines what the Eugene Capstone 2 assessment is allowed to assess before BUILD, BREAK, or PROVE work begins.

This phase answers:

- What system is in scope?
- Who owns it?
- Who uses it?
- What data can it touch?
- What AI tools are involved?
- What decisions require human authority?
- What evidence must exist before the client can claim the workflow is governed?

COMPLY findings are created when the client cannot prove basic scope, ownership, data boundary, tool approval, or production-use evidence.

---

## Scoped Intake: MedData Nexus

| Intake Field | Scoped Answer |
|---|---|
| System name | MedData Nexus Internal GenAI/RAG Environment |
| Business purpose | Help compliance, legal, security, vendor-risk, and clinical administrative staff retrieve and summarize approved internal documents for human review |
| Primary users | Compliance analysts, legal team, clinical administrative staff, IT security, vendor risk/compliance reviewers |
| AI tools in scope | Internal RAG chatbot; Eugene local assessment workflow using local Ollama only. No external LLM API is in scope for MDN-AI-001. |
| Data classes | Public, Internal, Confidential, and explicitly authorized Restricted documents as declared in the corpus manifest |
| Approved baseline corpus | Documents listed in `target-client/fake-data/corpus-manifest.md`; that manifest is the single source of truth for category, classification, owner, approver, approval date, and purpose |
| Prohibited baseline corpus | PHI/ePHI, real patient identifiers, credentials, secrets, unreviewed vendor free text, poisoned documents, unsanitized incident reports |
| Highest-risk workflow | RAG retrieval and summarization over sensitive compliance, security, legal, and healthcare privacy documents where output could influence compliance, legal, vendor-risk, or security decisions |
| Human-only decisions | Risk acceptance, production expansion, Restricted-data authorization, legal/compliance sign-off, incident declaration, final client-facing claims |
| Current recommendation status | Pilot/assessment only until ownership, corpus boundary, retrieval controls, logging, and human review evidence are proven |

---

## Ownership Requirements

The GenAI/RAG environment must have named owners before it can be treated as governed.

| Ownership Area | Required Owner | Current Scoped Answer |
|---|---|---|
| Business owner | Responsible for business outcome and workflow fit | Compliance Director |
| Technical owner | Responsible for implementation, uptime, access, and change control | Platform Engineering Lead |
| Risk owner | Responsible for accepting or rejecting residual risk | CISO / AI Governance Committee |
| Data owners | Responsible for corpus approval by document category | Legal, Compliance, Security, Privacy, Vendor Risk |
| Evidence owner | Responsible for logs, retrieval evidence, and approval records | IT Security / Security Operations |
| Approval authority | Required for Restricted data or production expansion | CISO, with Legal/Privacy input where needed |

If any required ownership area is missing, create a COMPLY scope finding.

---

## Data Boundary

| Data Tier | RAG Baseline Use | External API Use | Required Control |
|---|---|---|---|
| Public | Allowed | Not in scope for Eugene | Basic logging |
| Internal | Allowed in baseline corpus when listed in manifest | Not in scope for Eugene | Source tracking and output review |
| Confidential | Allowed for read-only retrieval and summarization | Not in scope for Eugene | Access control, source attribution, human review before external distribution |
| Restricted | Allowed only when explicitly listed in the signed manifest with CISO-approved purpose and role restriction | Not in scope for Eugene | CISO approval, Privacy/Legal review, HITL review, audit logging |
| Secrets/credentials | Not allowed | Not allowed | Secret scanning, ingestion rejection, incident handling if found |

---

## Top Three Evidence Requests

1. **Corpus manifest and approval record**
   - Shows which documents are approved for baseline ingestion, which are excluded, and which are scenario-only.
   - Primary artifact: `target-client/fake-data/corpus-manifest.md`.

2. **Retrieval and access-control evidence**
   - Proves users only retrieve authorized source documents and that PHI/secrets are not exposed from the clean baseline corpus.
   - Primary artifacts: golden-question retrieval output, scenario evidence, vector DB metadata.

3. **Prompt/output/audit trail**
   - Shows user query, retrieved chunks, model response, tool/API path, and human review decision for high-risk outputs.
   - Primary artifacts: API logs, evidence JSON, screenshots/API responses, reviewer notes.

---

## COMPLY Finding Triggers

Create a scope finding if:

- no business, technical, risk, or data owner exists
- the data boundary is unclear or undocumented
- approved AI tool usage is unknown
- production or pilot use exists but evidence is missing
- Restricted data handling is not explicitly authorized
- external AI API use is not documented in the AI inventory
- human-only decisions are not defined
- the client cannot produce a corpus manifest or source approval record

---

## Scope Finding Template

Use this format when a COMPLY trigger is met.

```markdown
## Scope Finding: [Short Title]

**Condition:** What scope, ownership, boundary, or evidence element is missing?

**Why It Matters:** Why this prevents governed AI adoption or defensible assessment.

**Evidence Needed:**
- artifact 1
- artifact 2
- artifact 3

**Risk:** What could happen if the system continues without this scope/control fact.

**Recommendation:** What the client should define, assign, approve, or document before scaling.
```

---

## Example Scope Finding

## Scope Finding: Missing GenAI/RAG System Ownership

**Condition:** MedData Nexus has an Internal GenAI/RAG environment in scope, but the intake has not produced a named business owner, technical owner, risk owner, and data owner for the corpus.

**Why It Matters:** Without ownership, the client cannot approve data boundaries, accept residual risk, enforce human review, prioritize remediation, or respond to incidents involving the AI system.

**Evidence Needed:**

- AI system inventory entry
- named business owner
- named technical owner
- named risk owner or approving executive
- named data owner for each corpus category
- approval record for pilot or production use

**Risk:** AI use may continue without accountable governance or defensible approval.

**Recommendation:** Assign and document system ownership in the AI inventory before expanding the RAG pilot. Ownership should include business, technical, risk, data, and evidence accountability.

---

## COMPLY Exit Criteria

COMPLY is complete enough to move into BUILD when:

- system name and use case are defined
- business, technical, risk, and data owners are named
- users and roles are scoped
- approved AI tools are listed
- prohibited data is explicit
- human-only decisions are documented
- top evidence requests are mapped to artifacts
- scope findings are created for any missing governance facts

## Single Source Of Truth

The corpus manifest at `target-client/fake-data/corpus-manifest.md` is authoritative for document classification and ownership. COMPLY workpapers may summarize the data boundary, but BUILD must implement classification, owner, approval, and role-filter behavior from the manifest rather than from prose tables.
