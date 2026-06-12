# AI Adoption Maturity Assessment — MedData Nexus Health Systems

> Filled workpaper for Capstone 2 COMPLY phase.
> Template: `CBBP-PLAN/PROVE/ai-adoption-maturity-model.md`
> Client: MedData Nexus Health Systems
> Assessor: jimjrxieb + Eugene (CAP2-AI-001, advisory)
> Date: 2026-06-08
> Input sources: `CBBP-PLAN/COMPLY/meddata-ai-adoption-intake.md`, `meddata-ai-inventory.md`, `meddata-ai-risk-assessment.md`

---

## Maturity Scale Reference

| Stage | Description | Evidence Required |
|---|---|---|
| Ad Hoc | AI usage exists through unsanctioned tools or personal accounts. No policy, no audit trail. | shadow AI indicators, no policy |
| Emerging | Approved pilots exist but controls are incomplete. Intent is documented; enforcement is not. | pilot scope, basic policy, limited monitoring |
| Scaling | AI workflows cross teams and have defined, enforced controls. | governance, monitoring, review gates, validation tests |
| Mature | AI lifecycle is governed, monitored, tested, and continuously improved. | metrics, incident feedback, red-team cadence, executive reporting |

---

## MedData Nexus — Maturity Rating by Dimension

| Dimension | Rating | Evidence | Gap | Recommendation |
|---|---|---|---|---|
| Business outcome clarity | Emerging | Use case defined; 30/60/90-day success criteria documented in COMPLY intake | No formal success criteria signed by business owner; no baseline measurement established | Document pilot success criteria (avg. evidence lookup time, audit prep hours) and get business owner sign-off before expanding |
| Approved AI tool inventory | Emerging | RAG chatbot (MDN-AI-001) and Eugene (CAP2-AI-001) registered; Eugene is local-only with no external LLM API path | No shadow AI audit performed; inventory is incomplete by definition | Complete shadow AI audit; require staff declaration of any AI tool use before pilot expands |
| Shadow AI visibility | **Ad Hoc** | No shadow AI audit performed; no network log review; no endpoint policy for AI service domains | Cannot confirm or deny whether staff send sensitive documents to external AI providers via personal accounts | Perform shadow AI audit (network logs, endpoint DLP, staff survey) and publish acceptable AI use policy before pilot expansion |
| Data classification for AI use | Emerging | Data tiers documented: Internal/Confidential allowed; PHI/ePHI, secrets, credentials explicitly prohibited; Restricted requires CISO authorization; corpus manifest planned | No ingestion validation implementing these rules — no PHI scanner, no secret scanner on corpus before ingest | Implement automated ingestion validation (detect-secrets, gitleaks, PHI pattern scanner) as a prerequisite for any corpus update |
| Human approval matrix | Emerging | Human-only decisions documented in COMPLY intake: risk acceptance, production expansion, Restricted-data auth, legal/compliance sign-off, incident declaration | HITL enforcement not technically implemented — human review can be skipped operationally; no approval recordkeeping system | Implement a HITL review checkpoint and reviewer identity log before high-risk outputs are distributed |
| AI-assisted development controls | **Ad Hoc** | RAG chatbot is not a developer AI use case; coding assistant governance not applicable to current scope | No SAST/SCA/secrets scan documented for the ingestion pipeline codebase; no dependency review process | Require pip-audit, Semgrep, and gitleaks on the ingestion pipeline before any corpus update is merged |
| RAG/vector DB controls | **Ad Hoc** | ChromaDB is the vector store; no controls implemented | No per-user/per-role access control; no output filtering; no ingestion validation — any authenticated user can retrieve any document regardless of classification tier | Implement collection-level access control (role → document tier); add output filter layer; add ingestion validation with PHI/secret scanning — S-rank priority |
| Prompt injection testing | **Ad Hoc** | BREAK scenarios planned but not executed; no test results exist | No evidence the system resists prompt injection, indirect injection, or RAG poisoning | Execute all BREAK scenarios before pilot expansion; document results as evidence; re-run after any corpus or model change |
| Monitoring and detection | **Ad Hoc** | No audit logging proven in baseline; no monitoring for unusual retrieval patterns or unexpected document access | No forensic trail if a data exposure occurs; no detection capability for injection attempts or unauthorized retrieval | Implement structured audit logging (query, chunk IDs, response, reviewer, timestamp) as a prerequisite for pilot expansion |
| Incident response and rollback | **Ad Hoc** | No AI-specific incident response plan; no corpus rollback procedure | If a data exposure or poisoning incident occurs, no documented response process, no isolation procedure, and no recovery playbook | Write an AI-specific IR runbook: exposure response, corpus rollback, model output quarantine, CISO escalation; test with tabletop exercise |
| Training and awareness | **Ad Hoc** | No staff training on approved vs. unapproved AI tools documented; no acceptable use policy communicated to users | Users may not know what data is prohibited, what review is required, or how to report AI incidents | Complete a brief AI acceptable use training for all pilot users before expansion: approved tools, prohibited data, HITL requirements, incident reporting |
| Evidence packaging | Emerging | COMPLY workpapers complete (intake, inventory, risk assessment); corpus manifest planned; BREAK evidence structure in place; baseline retrieval test script exists | No BREAK test results yet; no golden-question retrieval evidence run against clean baseline; no leadership-ready deliverable | Execute the baseline retrieval test; complete all BREAK scenarios; feed findings into client-findings report and executive summary |

---

## Dimension Detail — Highest Priority

### RAG / Vector DB Controls — Ad Hoc

**Current rating:** Ad Hoc

**Evidence:** ChromaDB is deployed as the vector store for the MedData Nexus RAG pilot. There is no per-user or per-role access control on the collection. No output filtering layer inspects responses before delivery. No ingestion validation prevents PHI or secrets from entering the corpus.

**Gap:** Any authenticated user of the chatbot can retrieve any document in the ChromaDB collection regardless of their authorization level. A compliance analyst could retrieve legal documents, a clinical admin could retrieve security findings, and a vendor reviewer could retrieve internal incident records. If PHI or secrets were inadvertently indexed, they would be retrievable by any user. This is the S-rank finding from the risk assessment (score: 20).

**Recommendation:** Implement collection-level access control in ChromaDB: map user roles to authorized document tiers and enforce that mapping on every retrieval call. Add an output filter layer before response delivery. Add ingestion validation (PHI scanner + secret scanner) as a required gate before any document enters the collection. Test with `scenarios/rag-vector-db-access-gap.md` before the pilot expands. CISO Constant Yung must sign off on residual risk before production authorization.

---

### Shadow AI Visibility — Ad Hoc

**Current rating:** Ad Hoc

**Evidence:** No shadow AI audit has been performed. MedData Nexus cannot confirm or deny whether compliance, legal, clinical, or IT staff are using personal AI accounts (ChatGPT, Microsoft Copilot) for company work.

**Gap:** If staff are using personal accounts to process Internal, Confidential, or Restricted MedData Nexus documents, those documents may have been transmitted to external LLM providers without authorization, BAA coverage, or an audit trail. This is unquantifiable until the audit is performed.

**Recommendation:** Perform a shadow AI audit before any pilot expansion decision. Steps: (1) review network logs for connections to known AI service domains (api.openai.com, copilot.microsoft.com, claude.ai, gemini.google.com); (2) check endpoint DLP policy coverage for AI service categories; (3) conduct a staff survey on AI tool usage. Publish and distribute an acceptable AI use policy. Add AI tool usage to the next security awareness training cycle.

---

### Human Approval Matrix — Emerging (enforcement gap)

**Current rating:** Emerging

**Evidence:** Human-only decisions are documented: risk acceptance, production expansion authorization, Restricted-data handling approval, legal/compliance sign-off on AI-generated content, incident declaration, and final distribution of AI-produced content to external parties.

**Gap:** Documentation exists; enforcement does not. There is no technical checkpoint, no approval queue, and no recordkeeping system that prevents an unreviewed AI output from being distributed. The approval matrix is a policy claim, not a proven control.

**Recommendation:** Implement a mandatory review checkpoint before high-risk outputs are distributed. At minimum: a structured log entry requiring reviewer identity, decision (approved/rejected/modified), and timestamp for each high-risk interaction. Validate with a BREAK test that simulates a skipped review step.

---

## Overall Maturity Rating

**Rating: Emerging (2 / 4)**

Intent and scope are clearly defined. The use case is scoped, the data boundary is documented, and owners are named by role. The pilot is registered. These are Emerging-stage signals.

However, most technical controls are Ad Hoc or absent. The vector DB has no access control. Audit logging is not proven. Shadow AI is not audited. Prompt injection is not tested. Incident response does not exist. Six of twelve dimensions rated Ad Hoc.

---

## Scale Recommendation

**Recommendation: Pilot Only**

Continue limited, assessment-environment use only. Production deployment is not authorized.

Conditions blocking advancement:

| Condition | Required Before |
|---|---|
| S-rank: vector DB access control not implemented | Any pilot expansion |
| B-rank: no audit logging | Any pilot expansion |
| B-rank: no output filtering | Any pilot expansion |
| B-rank: no PHI/secret ingestion validation | Any pilot expansion |
| B-rank: HITL not enforced | Any pilot expansion |
| Ad Hoc: no shadow AI audit | Any pilot expansion |
| Ad Hoc: no AI incident response plan | Production authorization |
| Ad Hoc: no staff training | Production authorization |

**Advancement path:** Remediate S-rank and B-rank findings → execute all BREAK scenarios → prove controls hold → get CISO sign-off → reassess maturity → authorize conditional pilot expansion.

---

## CBBP Interpretation — MedData Nexus Current State

| Phase | Status | Assessment |
|---|---|---|
| COMPLY | Strong | Scope, data boundary, ownership, and risk intent are documented. COMPLY workpapers are complete. |
| BUILD | Not started | Approved workflow and technical controls are defined on paper but not implemented. |
| BREAK | Not started | All BREAK scenarios are planned but none have been executed. No test evidence exists. |
| PROVE | Not ready | Cannot produce a defensible scale recommendation until BUILD controls are implemented and BREAK evidence is collected. |

**Bottom line for a CISO:** The organization has done the intake work well. They know what the system is supposed to do and what data it should not touch. What they cannot yet prove is that any of those boundaries actually hold under test conditions.

---

## Finding Trigger — AI Scaling Faster Than Governance

**Condition:** MedData Nexus is running an active RAG pilot over sensitive compliance, healthcare, and legal documents with no access control on the vector DB, no audit logging, no output filtering, and no tested controls. The system is in use while the controls that should govern that use do not exist.

**CISO sentence:** AI usage is moving faster than the governance needed to control data exposure, human approval, and evidence for safe expansion.

**Risk:** A data exposure incident — PHI surfaced, secrets retrieved, poisoned document followed — would be discovered without a forensic trail and without a response plan.

**Recommendation:** Freeze pilot expansion. Implement S-rank and B-rank remediations. Execute BREAK scenarios to validate. Then reassess.
