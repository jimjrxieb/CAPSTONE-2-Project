# AI System Inventory — MedData Nexus Health Systems

> Client-scoped AI system inventory for Capstone 2 COMPLY phase.
> Template: `templates/ai-inventory-register.md`
> Client: MedData Nexus Health Systems
> Scope: All AI systems operating in the MedData Nexus environment — assessed by Eugene (CAP2-AI-001)
> Assessor: jimjrxieb + Eugene
> Date: 2026-06-08
> Required by: GOVERN 5.2, CM-8 (System Component Inventory), NIST AI RMF GOVERN 1.1

---

## Purpose

This register answers the auditor question: "What AI systems are operating in the MedData Nexus environment, and do you know the risk posture of each one?"

A system not in this register is unauthorized. Discovery of an unregistered AI system is a GOVERN 1.1 FAIL — Eugene generates a B-rank finding and routes to CISO (Constant Yung) for immediate review.

---

## MedData Nexus AI System Registry

| System ID | Name | Role | Model / Stack | Version | Risk Tier | Status | Registration Date | Last Reviewed |
|---|---|---|---|---|---|---|---|---|
| MDN-AI-001 | Internal RAG Chatbot | Compliance document search and summarization for internal staff | ChromaDB vector store + local Ollama/Eugene inference only; no external LLM API path | v0.1 pilot | **High Risk** | Pilot (assessment in progress) | 2026-06-08 | 2026-06-08 |
| MDN-AI-002 | Shadow AI (suspected/unregistered) | Possible ad hoc staff usage via personal accounts; uncontrolled if confirmed | GPT-4 / MS Copilot (unverified, personal account assumption) | Unknown | **Critical Risk if confirmed** | Suspected unregistered use — GOVERN 1.1 finding trigger | Not registered | 2026-06-08 |
| CAP2-AI-001 | Eugene | AI security assessment assistant for this engagement | Local LLM via Ollama | v0.1 build target | Limited Risk | In Build (assessment tool only) | 2026-06-08 | 2026-06-08 |

---

## Per-System Risk Summary

### MDN-AI-001 — Internal RAG Chatbot

| Field | Value |
|---|---|
| **Autonomy Level** | Retrieval and summarization only — no write access, no system actions |
| **Decision Authority** | Advisory — produces retrievals and summaries; human reviews before any compliance or legal use |
| **Human Oversight** | Required for all high-risk outputs — NOT YET ENFORCED (COMPLY finding open) |
| **Data Processed** | Internal and Confidential documents: policies, compliance evidence, HIPAA assessment records, SOC 2 summaries, vendor-risk docs, legal/BAA templates, sanitized incident records |
| **Prohibited Data** | PHI/ePHI, real patient identifiers, credentials, secrets, unreviewed vendor free text, poisoned or unapproved documents |
| **HITL Enforced** | No — HITL enforcement is not yet implemented. COMPLY finding: open. |
| **Serving** | Pilot environment; not in production. Access limited to: compliance analysts, legal, IT security, vendor risk reviewers, clinical administrative staff. |
| **Monitoring** | Not proven — logging not confirmed in baseline. COMPLY finding: open. |
| **Known Gaps** | Deployed vector DB direct-access testing, embedding-layer testing, shadow AI audit, and full runtime BREAK coverage remain open. Local role filtering, prompt-injection rejection, corpus contamination handling, HITL review records, audit logging, and static platform controls have initial lab evidence. |
| **Business Owner** | Compliance Director (role identified; individual name pending) |
| **Technical Owner** | Platform Engineering Lead (role identified; individual name pending) |
| **Risk Owner** | CISO Constant Yung |
| **Data Owners** | Legal, Compliance, Security, Privacy, Vendor Risk (by document category — individual names pending) |
| **Authorization Status** | Pilot only — production deployment NOT authorized until S/B-rank findings remediated |

**AI RMF Coverage — Current Gaps:**

| Subcategory | Status | Gap |
|---|---|---|
| GOVERN 1.1 (policies established) | PARTIAL | No AI-specific use policy covering this chatbot |
| GOVERN 1.2 (accountability) | PARTIAL | Owners defined by role; individual names not yet assigned |
| GOVERN 1.5 (risk tolerance) | FAIL | No documented AI risk tolerance statement |
| MAP 1.1 (context established) | PASS | Use case, users, data classes, and scope documented |
| MAP 2.3 (limitations documented) | PARTIAL | Known gaps documented here; not yet communicated to users |
| MAP 3.1 (tested in context) | PARTIAL | Local mini-loop BREAK evidence exists; deployed/direct-access and embedding-layer tests remain open |
| MEASURE 2.5 (output trustworthiness) | FAIL | Retrieval accuracy not validated against approved corpus |
| MEASURE 2.7 (monitoring) | FAIL | No monitoring or logging proven |
| MEASURE 2.11 (security/resilience) | PARTIAL | Prompt injection, corpus contamination, unauthorized retrieval, and platform static checks have lab evidence; deployed platform BREAK remains open |
| MANAGE 1.1 (risks prioritized) | PARTIAL | Risk register started; scores not yet final |
| MANAGE 2.2 (HITL implemented) | FAIL | HITL not enforced |
| MANAGE 3.1 (incident response) | FAIL | No AI-specific IR plan exists |
| MANAGE 4.1 (post-deployment monitoring) | FAIL | No post-deployment monitoring planned |

---

### MDN-AI-002 — Shadow AI (Suspected / Unregistered if Confirmed)

| Field | Value |
|---|---|
| **Autonomy Level** | Unknown — suspected personal-account use; no organizational control if confirmed |
| **Decision Authority** | Unknown — staff may use outputs directly in work products without review |
| **Human Oversight** | Not enforced — no organizational visibility |
| **Data Processed** | Unknown — could include Internal, Confidential, or Restricted MedData Nexus documents |
| **HITL Enforced** | No |
| **Serving** | Possible external commercial LLM use (ChatGPT, Microsoft Copilot) via personal accounts |
| **Monitoring** | Not evidenced |
| **Known Gaps** | No shadow AI audit exists. If personal-account use is confirmed, data may have been transmitted to external providers without authorization, BAA coverage, or audit trail. |
| **Risk Owner** | CISO Constant Yung (immediate escalation required) |
| **Authorization Status** | **GOVERN 1.1 finding trigger — suspected unregistered use. B-rank if confirmed. Escalate to CISO for discovery.** |

**Finding Trigger — GOVERN 1.1: Shadow AI Audit Missing**

Personal AI account usage is unknown because no shadow AI audit has been performed. This creates an evidence gap: MedData Nexus cannot prove whether staff are or are not sending sensitive work material to unapproved AI services.

Required actions:
1. Perform shadow AI audit (network logs, endpoint policy, staff survey)
2. Publish acceptable AI use policy
3. Include AI tool usage in security awareness training
4. Require personal-account AI tool declaration from all staff handling Internal/Confidential/Restricted data

---

### CAP2-AI-001 — Eugene (Assessment Tool — GP-Copilot Owned)

| Field | Value |
|---|---|
| **Autonomy Level** | Advisory only — produces findings and framework mappings; never executes fixes |
| **Decision Authority** | None — all B/S-rank findings route to jimjrxieb for human decision |
| **Human Oversight** | Always — all outputs reviewed before inclusion in client deliverables |
| **Data Processed** | Synthetic MedData Nexus documents (fake-data corpus), RAG retrieval context, BREAK scenario evidence, framework mapping inputs |
| **HITL Enforced** | Yes for lab high-risk output records — BUILD added review-decision logging before any high-risk Eugene output is treated as deliverable-ready. Final client-facing use still requires human approval by jimjrxieb. |
| **Serving** | Local API `/query`; Ollama localhost:11434 for local generation path |
| **Monitoring** | Evidence capture under `evidence/`, structured audit logs, HITL review records, and corpus-owner alert logs |
| **Known Limitations** | Advisory only; not an autonomous assessor; final judgment is human-owned; uses synthetic data only — never real MedData Nexus production data |
| **Authorization Scope** | Capstone 2 lab only — not authorized for production deployment without separate registration |

---

## Unregistered AI System Discovery Checklist

Run at start of each COMPLY phase or when a new AI system is suspected:

```bash
# Ask client IT security: what AI tools are accessed from corporate networks?
# Review endpoint protection logs for known AI service domains:
#   api.openai.com, copilot.microsoft.com, claude.ai, gemini.google.com

# If K8s environment: find AI-related deployments
kubectl get deployments -A -o json | \
  jq '.items[] | select(.metadata.name | test("ai|llm|model|ollama|rag|chatbot|vector"; "i")) | {ns: .metadata.namespace, name: .metadata.name}'

# If Python environment: find AI library usage
grep -r "openai\|anthropic\|langchain\|chromadb\|pinecone\|weaviate\|llamaindex" . --include="*.py" --include="requirements*.txt"

# Compare against this register — any system found but not registered → GOVERN 1.1 FAIL
```

---

## Audit Trail

| Date | Change | Who | AI RMF Reference |
|---|---|---|---|
| 2026-06-08 | Initial inventory created for MedData Nexus COMPLY phase | jimjrxieb | GOVERN 1.1 |
| 2026-06-08 | MDN-AI-001 (RAG Chatbot) registered as High Risk pilot | jimjrxieb | GOVERN 1.1, MAP 1.1 |
| 2026-06-08 | MDN-AI-002 (Shadow AI) added as suspected/unregistered-if-confirmed finding trigger | jimjrxieb | GOVERN 1.1 |
| 2026-06-08 | CAP2-AI-001 (Eugene) registered as assessment tool | jimjrxieb | GOVERN 1.1 |
| 2026-06-10 | CAP2-AI-001 HITL claim updated to reflect technical review records plus human final authority | jimjrxieb + Eugene | GOVERN 1.2, MANAGE 2.2 |

---

## Open Findings from This Inventory

| ID | System | Finding | Rank | Owner | Due |
|---|---|---|---|---|---|
| MDN-GOVERN-001 | MDN-AI-002 | Shadow AI audit missing — personal-account AI usage unknown and unverified | B | CISO Constant Yung | Immediate |
| MDN-GOVERN-002 | MDN-AI-001 | HITL enforcement not implemented — human review required but not technically enforced | B | Platform Engineering Lead | Before pilot expansion |
| MDN-GOVERN-003 | MDN-AI-001 | No AI-specific risk tolerance statement documented | C | CISO Constant Yung | Before pilot expansion |
| MDN-GOVERN-004 | MDN-AI-001 | No AI-specific incident response plan | B | IT Security | 30 days |
| MDN-GOVERN-005 | MDN-AI-001 | Audit logging not proven in baseline | B | Platform Engineering Lead | Before pilot expansion |
