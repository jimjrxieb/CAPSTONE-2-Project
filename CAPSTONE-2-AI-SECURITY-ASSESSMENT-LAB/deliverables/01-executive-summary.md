# Executive Summary — AI Security Assessment
## MedData Nexus Health Systems

> Prepared for: CISO Constant Yung
> Prepared by: jimjrxieb + Eugene (CAP2-AI-001, advisory)
> Date: 2026-06-08
> System assessed: MDN-AI-001 — Internal RAG Chatbot + Coding Assistant Workflow
> Assessment framework: CBBP (COMPLY / BUILD / BREAK / PROVE)

---

## Scale Recommendation

**Do not scale. Continue pilot only. Conditions for expansion are defined below.**

This is not a judgment about whether the technology works. The RAG chatbot functions. The coding assistant workflow produces output. The recommendation to hold is based on what is not yet proven: no control protecting this system from data exposure, unauthorized access, or manipulation has been tested and confirmed working.

Scaling before the controls are proven distributes uncontrolled risk to every user and every document category added to the corpus.

---

## Business Risk

MedData Nexus is deploying an AI system over a corpus that includes compliance documentation, legal records, security findings, and policy frameworks — some of which are adjacent to Protected Health Information. The system uses Claude Haiku via an external API, creating a data boundary that requires explicit control of what reaches the model.

The primary business risk is not a technical failure. It is a governance failure: the organization is operating an AI pilot without the ability to answer the question a regulator, auditor, or affected employee would ask after an incident:

> "Who accessed what, when, what did the AI return, and who reviewed it before it was acted on?"

Today, that question cannot be answered. There is no audit log, no access control proven to work, and no HITL enforcement that would prevent an AI-generated conclusion from being acted on without review.

---

## Key Findings

| Finding | Rank | Implication |
|---|---|---|
| No role-based access control on ChromaDB | **S** | Any pilot user can retrieve documents above their clearance level using a normal question |
| No audit logging | B | No forensic record exists if a data exposure occurs today |
| No prompt injection defense | B | Adversarial inputs reach the model without interception |
| No corpus approval workflow | B | Any document placed in the ingest directory becomes retrievable |
| No pre-ingestion secret/PHI scanning | B | Credentials or PHI-adjacent content in a document enter the corpus and can be retrieved |
| No HITL enforcement | B | AI-generated conclusions can be acted on without a review record |
| Shadow AI not audited (MDN-AI-002) | B | An unregistered AI system may be transmitting sensitive data to external providers now |

**None of these controls are in place. None have been tested. The BREAK test execution phase has not yet run.**

The COMPLY phase (intake, inventory, maturity assessment, architecture review, corpus review, and threat modeling) produced these findings from architecture analysis and stakeholder interviews. The BREAK phase will confirm them with test evidence. Based on the architecture review, all seven findings above are expected to be confirmed as FAIL when tested.

---

## What the Assessment Found

### The controls are documented but not enforced.

The MedData Nexus team has written policies covering human review requirements, approved data tiers, and acceptable use expectations. None of these policies have a technical gate behind them. The gap between what the policy says and what the system does is the entire exposure surface.

### The data boundary is not working.

ChromaDB has no access control layer. The vector database returns chunks based on semantic similarity to the query — not based on who is asking or whether they are authorized to see the result. A vendor risk reviewer can ask a compliance question and receive a chunk from the IT Security assessment findings category. This is architectural. It was never built.

### The governance gap enables every other risk.

Without audit logging, no data exposure is forensically traceable. Without HITL enforcement, no AI conclusion is provably reviewed before action. Without a corpus approval workflow, no document is provably clean before retrieval. The governance gaps compound the technical control gaps — they remove the fallback accountability that would otherwise partially compensate.

### An unregistered AI system (MDN-AI-002) is in use.

During intake, a suspected unregistered AI system was identified. It is not in the approved AI inventory. GOVERN 1.1 is a FAIL. The data transmitted, the scope of use, and the exposure surface are unknown. This requires a shadow AI audit before any further pilot expansion — not because the tool is necessarily harmful but because the organization does not know what data is leaving the environment and to whom.

---

## What Needs to Happen

Three gates must clear before pilot expansion:

**Gate 1: Execute the BREAK tests.** All 10 BREAK tests are designed and ready. They have not been run. Evidence cannot be produced without execution. This is the immediate next action.

**Gate 2: Remediate F-001 and F-005.** ChromaDB access control (F-001) and structured audit logging (F-005) are the two structural controls that all other security depends on. Access control determines who can see what. Audit logging determines whether anyone can know what happened. Both must be in place and tested before any new user or corpus category is added.

**Gate 3: Close or formally accept all B-rank pilot expansion blockers.** Five B-rank findings remain. Each must be either remediated with BREAK test confirmation or formally accepted by CISO Constant Yung with a documented risk treatment decision, owner, and expiry date.

---

## Conditions for Expansion Authorization

The pilot may expand when all of the following are true:

1. All 10 BREAK tests have been executed with evidence on file.
2. BREAK test 4 (unauthorized retrieval) returns PASS for all role × corpus category combinations.
3. BREAK test 5 (audit logging) returns PASS with all required fields present in every log entry.
4. F-002, F-003, F-004, F-006 are each remediated or formally risk-accepted with CISO signature.
5. F-007 shadow AI audit is complete and MDN-AI-002 is either registered or decommissioned.
6. CISO Constant Yung has reviewed and signed the PROVE package.

---

## What the Team Did Right

The MedData Nexus team scoped the pilot deliberately. The corpus categories are defined. User roles are documented. The system is running on a limited basis with a named set of pilot users. The intent to govern AI adoption correctly is present.

The gap is between intent and proof. This assessment provides the path from intent to defensible.

---

## CISO Sentence

> MedData Nexus is operating an AI pilot over sensitive compliance and legal documents without the access controls, audit logging, or human enforcement mechanisms that would make expansion defensible to a regulator — and none of the controls designed to protect the system have been tested against real attack scenarios.
