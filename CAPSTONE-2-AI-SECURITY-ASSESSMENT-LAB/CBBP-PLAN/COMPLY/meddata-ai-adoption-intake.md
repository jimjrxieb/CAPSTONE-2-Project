# AI Adoption Intake — MedData Nexus Health Systems

> Filled workpaper for Capstone 2 COMPLY phase.
> Template: `templates/ai-adoption-intake-questionnaire.md`
> Client: MedData Nexus Health Systems
> Assessor: jimjrxieb + Eugene (CAP2-AI-001)
> Date: 2026-06-08
> Status: COMPLY — intake complete, scope findings documented below

---

## Business Outcome

| Question | MedData Nexus Answer |
|---|---|
| What business problem is AI supposed to solve? | Compliance analysts, legal staff, and clinical administrative staff spend significant time manually searching across PDFs, portals, and shared drives for policy evidence, HIPAA compliance artifacts, and vendor security responses during audits and vendor reviews. The RAG assistant is meant to cut that search time. |
| Why is AI the right tool? | Document volume and cross-document correlation exceed what manual search handles efficiently. Semantic retrieval over structured compliance documents is a well-scoped AI use case. |
| What workflow is painful today? | Manually locating the right policy section, SOC 2 evidence, or HIPAA assessment record across disconnected document stores — especially under audit or vendor review deadlines. |
| What does success look like in 30/60/90 days? | 30 days: baseline retrieval returns accurate results for approved document categories with no PHI/secrets in responses. 60 days: compliance team uses RAG as first-stop for audit evidence gathering; average evidence lookup time drops measurably. 90 days: governed pilot with retrieval logs, human review records, and corpus manifest available for auditor review. |
| What would unacceptable failure look like? | PHI exposed via retrieval response. Credentials or secrets surfaced from indexed documents. AI output used as legal or compliance evidence without human review. Unauthorized user accessing restricted corpus sections. |

---

## Current AI Usage

| Question | MedData Nexus Answer |
|---|---|
| Which AI tools are already used? | Internal RAG chatbot (pilot); Eugene (Capstone 2 assessment tool). No external LLM API is approved for MDN-AI-001. |
| Which tools are approved? | Internal RAG chatbot — pilot authorization only. Eugene — assessment use only. External AI tools are out of scope for MDN-AI-001 and require separate approval if introduced later. |
| Which tools are unapproved or suspected? | Possible ChatGPT personal-account use and Microsoft Copilot personal-license use by staff. This is not confirmed; no formal shadow AI audit has been completed. |
| Which teams are using AI? | Compliance, Legal, IT Security, Vendor Risk/Compliance. Clinical administrative staff have access to the pilot chatbot. |
| Are personal accounts used for company work? | Unknown. No shadow AI audit has been performed. This is a COMPLY finding trigger. |
| Are AI outputs used in production decisions? | The pilot chatbot produces summaries for human review. However, no HITL enforcement is documented. Risk exists if review is skipped before compliance or legal decisions are made. |

---

## Data Boundary

| Question | MedData Nexus Answer |
|---|---|
| What data can AI see? | Documents approved in `target-client/fake-data/corpus-manifest.md`. The manifest is authoritative for Public/Internal/Confidential/Restricted classification, owner, approver, approval date, and purpose. |
| What data is prohibited? | PHI/ePHI, real patient identifiers, credentials and secrets, unreviewed vendor free text, poisoned or unapproved documents, unsanitized incident reports. |
| Does the workflow include PII, PHI, secrets, contracts, or regulated data? | Yes. PHI-adjacent content (HIPAA policy documents, HIPAA assessment records) is in scope. Real PHI is prohibited but risk of inadvertent ingestion exists. Contracts (BAA templates, vendor agreements) are in scope. |
| Is data sent to third-party vendors? | No external LLM API is in scope for MDN-AI-001. Any later third-party AI processing would require new COMPLY approval, documented data-flow review, and CISO authorization before use. |
| Is data logged, retained, or used for training? | Logging is planned but not yet proven. Retention policy not documented. No use of retrieval data for model training is authorized. |
| Does RAG use sensitive internal documents? | Yes — the entire corpus is sensitive enterprise documentation. This is why corpus boundary control and access control on the vector DB are critical. |

---

## Tool Authority

| Capability | Authorized? | Notes |
|---|---|---|
| AI can read files | Yes | Via RAG ingestion pipeline — approved corpus only |
| AI can write files | No | Read-only retrieval and summarization; humans write final artifacts |
| AI can run commands | No | No shell or system access authorized |
| AI can call APIs | Yes (limited) | Internal RAG API only; no external LLM API path for Eugene |
| AI can open PRs | No | Not a developer workflow use case |
| AI can retrieve from vector databases | Yes | ChromaDB — requires access control enforcement (current gap) |
| AI can access production systems | No | Assessment environment only; production systems are out of scope |

---

## Human Review

| Question | MedData Nexus Answer |
|---|---|
| What outputs require human review? | High-risk compliance decisions, legal interpretations, any output that could influence clinical or regulatory action, outputs involving Restricted-tier documents, any vendor risk conclusion. |
| What actions are human-only? | Risk acceptance, production expansion authorization, Restricted-data handling approval, legal/compliance sign-off on findings, incident declaration, final client-facing distribution of AI-produced content. |
| Who approves high-risk changes? | CISO Constant Yung, with Legal/Privacy input where required. AI Governance Committee for production expansion. |
| How is approval recorded? | Not yet documented — approval workflow and recordkeeping are a COMPLY finding gap. |
| What happens if review is skipped? | No automated guardrail prevents distribution of unreviewed output. Skipping review is operationally possible. COMPLY finding: HITL enforcement is not yet implemented or validated. |

---

## Security Controls

| Control | Status | Notes |
|---|---|---|
| Prompts and outputs logged | Not proven | Planned but no logging evidence exists in baseline |
| AI-assisted PRs labeled | N/A | Not a developer workflow use case |
| SAST/SCA/IaC/secrets scans required | Required for pipeline code | Must run on ingestion pipeline before any corpus change |
| Dependencies reviewed | Required | Pipeline Python dependencies must pass pip-audit before merge |
| Prompt injection tests run | Planned | BREAK scenario: `scenarios/rag-direct-prompt-injection.md` |
| RAG poisoning tests run | Planned | BREAK scenario: `scenarios/rag-poisoned-document.md` |
| Vector DB boundaries tested | Planned | BREAK scenario: `scenarios/rag-vector-db-access-gap.md` |
| AI incident response plan | Not documented | COMPLY finding: no AI-specific IR plan exists |

---

## Evidence

| Question | MedData Nexus Answer |
|---|---|
| What artifacts prove the workflow is governed? | Corpus manifest, retrieval evidence (golden-question output), audit logs, HITL decision records, corpus approval records signed by data owners. |
| Where are logs stored? | Planned: `evidence/` under Capstone 2 lab. Not yet proven for the production pilot. |
| Where are review notes stored? | Not defined — COMPLY finding gap. |
| Where are test results stored? | BREAK evidence under `evidence/`; scenario evidence files. |
| Who signs off on pilot expansion? | CISO Constant Yung. Must be documented before any expansion from pilot to broader deployment. |

---

## Assumptions Pending Evidence

The following items are working assumptions for COMPLY scoping. They must be confirmed through target-client evidence, BUILD implementation records, or BREAK/PROVE test results before they are treated as facts.

| Assumption | Evidence Needed | Current Treatment |
|---|---|---|
| Personal ChatGPT or Copilot accounts may be used by staff | Shadow AI audit, network logs, endpoint policy review, staff survey | Finding trigger, not confirmed incident |
| RAG pilot logging is planned but not operationally proven | Audit log sample, log storage location, retention policy | Evidence gap |
| HITL is expected for high-risk outputs | Workflow design, approval log, named approvers | Requirement not yet enforced |

---

## COMPLY Finding Triggers — Active

The following COMPLY finding triggers are active for MedData Nexus. These are scope/evidence gaps until BREAK or discovery confirms behavior.

| # | Trigger | Status |
|---|---|---|
| 1 | Shadow AI audit not performed — personal-account AI tool use unknown and unverified | OPEN |
| 2 | HITL enforcement not implemented — skipping human review is operationally possible | OPEN |
| 3 | Approval workflow and recordkeeping not documented | OPEN |
| 4 | No AI-specific incident response plan | OPEN |
| 5 | Prompt and output logging not proven in baseline | OPEN |
| 6 | Review note storage location not defined | OPEN |
| 7 | Pilot expansion sign-off criteria not formally documented | OPEN |

---

## Scope Finding: Missing HITL Enforcement and Approval Records

**Condition:** MedData Nexus's RAG pilot lacks documented HITL enforcement. Human review is required for high-risk outputs (compliance decisions, legal interpretations, Restricted data outputs) but no technical or procedural guardrail prevents distribution of unreviewed AI output.

**Why It Matters:** Without enforced human review, AI-generated summaries can influence legal, compliance, or clinical decisions without accountability. This is a GOVERN 1.2 gap (no accountable reviewer assigned) and a HIPAA risk if PHI-adjacent content is distributed without oversight.

**Evidence Needed:**
- HITL workflow design document
- Approval routing record for at least one high-risk output example
- Named approver for each output category (legal, compliance, clinical, vendor risk)
- Technical enforcement or process checkpoint that requires approval before distribution

**Risk:** AI output influences a regulated decision without a recorded human review. Discovery in audit produces a reportable compliance gap.

**Recommendation:** Define and document the HITL approval matrix before expanding the pilot beyond the current user group. Assign a named approver per output category. Implement a review checkpoint (even a simple approval log) before any AI-produced content is used in a compliance or legal submission.

---

## Scope Finding: No Shadow AI Audit Performed

**Condition:** MedData Nexus has not performed a shadow AI audit. Personal-account use of ChatGPT and Microsoft Copilot by compliance, legal, and clinical staff is unknown and unverified.

**Why It Matters:** If staff are using personal AI accounts for company work, sensitive documents (HIPAA records, vendor contracts, internal policies) may be transmitted to external LLM providers without authorization, BAA coverage, or audit trail.

**Evidence Needed:**
- Shadow AI audit results (network log review, endpoint policy check, staff survey)
- Acceptable use policy that explicitly covers personal AI tool use
- Evidence that staff have been informed of approved vs. prohibited AI tools

**Risk:** Possible unreported transmission of sensitive or regulated data to external AI providers. Potential HIPAA violation if PHI-adjacent content is processed outside a covered arrangement.

**Recommendation:** Complete a shadow AI audit before expanding the internal RAG pilot. Publish and enforce an acceptable AI use policy. Include personal-account AI usage in the next security awareness training cycle.

---

## COMPLY Exit Criteria — Status

| Criterion | Status |
|---|---|
| System name and use case defined | COMPLETE |
| Business, technical, risk, and data owners named | PARTIAL — owners defined by role; individual names not yet assigned for all categories |
| Users and roles scoped | COMPLETE |
| Approved AI tools listed | COMPLETE |
| Prohibited data explicit | COMPLETE |
| Human-only decisions documented | COMPLETE (documentation exists; enforcement is the gap) |
| Top evidence requests mapped to artifacts | COMPLETE |
| Scope findings created for missing governance facts | COMPLETE — 7 open findings documented above |

**COMPLY Status: READY TO ADVANCE TO BUILD remediation/design with open findings tracked.**

Production expansion is NOT authorized until HITL enforcement, shadow AI audit, and logging evidence are closed.
