> Synthetic data for Capstone 2 testing only.
> No real patient, customer, credential, contract, or GuidePoint client data.

---

# MedData Nexus Health Systems
## AI System Inventory Register
**Document ID:** AI-INV-001  
**Version:** 1.3  
**Last Updated:** April 15, 2026  
**Owner:** Chief Information Security Officer  
**Maintained By:** IT Security / AI Governance Committee  
**Classification:** Confidential  
**Review Cycle:** Quarterly (full review) / Real-time (new system additions)

---

## 1. Purpose

This register documents all artificial intelligence and machine learning systems that process, store, or access MedData Nexus data, regardless of whether the system is internally developed, vendor-provided, or operated via third-party API. All AI systems used at MedData Nexus are required to be registered in this inventory per the AI Governance Policy (AI-GOV-001, Section 3).

Unregistered AI systems may not process MedData Nexus data. Use of an unregistered AI system on MedData Nexus data is a policy violation subject to disciplinary action.

**AI Governance Committee:** Meets quarterly to review this register, assess new systems, and review the status of systems under review. Members: CISO (chair), Privacy Officer, Compliance Director, Legal Counsel, CTO representative, Clinical Operations representative (as applicable).

---

## 2. AI System Inventory

### System 1: Internal RAG Chatbot

| Field | Value |
|-------|-------|
| **System Name** | MedData Nexus Internal RAG Chatbot |
| **System ID** | AI-SYS-001 |
| **Owner** | IT Security / Platform Engineering |
| **Business Owner** | Compliance Director (primary user community: compliance, legal, clinical admin) |
| **Purpose** | Retrieval-Augmented Generation chatbot allowing authorized staff to search and retrieve relevant passages from MedData Nexus's internal policy library, compliance evidence repository, and regulatory guidance documents. Produces draft summaries for human review. |
| **Vendor** | Self-hosted (MedData Nexus infrastructure) |
| **Model / Technology** | Internally operated LLM via API; vector database: ChromaDB (self-hosted on EKS); embedding model: internal |
| **Hosting Location** | AWS us-east-1 (VPC-isolated); no data leaves MedData Nexus infrastructure |
| **Data Classification Processed** | Internal, Confidential |
| **PHI Authorized** | No — PHI is explicitly prohibited per POL-PHI-001 §5 and POL-AI-001 §4.2. Documents must be de-identified or confirmed PHI-free before indexing. |
| **HIPAA Relevance** | Yes — system must be prevented from processing PHI; any inadvertent PHI ingestion constitutes a potential HIPAA technical safeguard gap |
| **BAA Required** | N/A — self-hosted, no PHI authorized |
| **SOC 2 Coverage** | Included in MedData Nexus SOC 2 scope as of 2026 audit cycle |
| **Risk Tier** | High |
| **Current Approval Status** | In Assessment — deployed April 2026; undergoing AI security assessment (Capstone 2 assessment scope) |
| **Review Date** | July 2026 (post-assessment; full governance review required before production approval) |
| **Conditions / Notes** | HITL (human-in-the-loop) review required for any output that will be used in an official document or submitted to a regulator. Inference logs reviewed monthly. Output classification guardrails implemented — system will not output Restricted-tier content without CISO authorization. Prompt injection monitoring active. |
| **Incident History** | None (deployed April 2026) |

---

### System 2: NovaMind API Document Summarizer

| Field | Value |
|-------|-------|
| **System Name** | NovaMind API Document Summarization Service |
| **System ID** | AI-SYS-002 |
| **Owner** | Compliance Team |
| **Business Owner** | Compliance Director |
| **Purpose** | Third-party LLM API used to generate first-draft summaries of vendor security questionnaires, audit reports, and policy documents. Summaries are reviewed and edited by compliance analysts before use. |
| **Vendor** | NovaMind Technologies, Inc. |
| **Model / Technology** | NovaMind proprietary LLM via REST API (HTTPS) |
| **Hosting Location** | NovaMind infrastructure — AWS us-east-1 and us-west-2 (US-only) |
| **Data Classification Processed** | Internal, Confidential |
| **PHI Authorized** | No — explicitly prohibited by operating procedure. PHI must not be submitted in API queries. Technical control (PHI pattern detection) targeted for implementation by May 2026. |
| **HIPAA Relevance** | Yes — BAA executed to cover potential inadvertent PHI submission; PHI submission is operationally prohibited |
| **BAA Required** | Yes — BAA executed January 15, 2025 (BAA registry entry: NM-001) |
| **SOC 2 Coverage** | NovaMind SOC 2 Type 2 available (Security + Availability, 2024 audit, no exceptions) |
| **Risk Tier** | Medium |
| **Current Approval Status** | Approved with conditions |
| **Approval Date** | February 1, 2025 |
| **Review Date** | May 2026 (contract renewal) |
| **Conditions / Notes** | Conditions for approval: (1) Zero-retention prompt logging to be negotiated at May 2026 contract renewal; (2) technical PHI pattern detection implemented before submission layer; (3) annual sub-processor review. Renewal must not proceed without condition 1 being met. |
| **AI Vendor Risk Assessment** | VRA-AI-2026-001 (NovaMind section) — Risk: Medium |
| **Incident History** | None |

---

### System 3: ClearBot Enterprise HR Chatbot

| Field | Value |
|-------|-------|
| **System Name** | ClearBot Enterprise HR Chatbot |
| **System ID** | AI-SYS-003 |
| **Owner** | Human Resources |
| **Business Owner** | VP of Human Resources |
| **Purpose** | HR chatbot pilot — deployed to allow employees to self-serve answers to HR policy questions (benefits, leave, onboarding). Intended to reduce HR helpdesk ticket volume. |
| **Vendor** | ClearBot AI, Inc. |
| **Model / Technology** | ClearBot Enterprise LLM (proprietary) via SaaS |
| **Hosting Location** | ClearBot infrastructure — US and EU (Ireland) — EU processing was not authorized at pilot deployment |
| **Data Classification Processed** | Internal (employee data, HR policies) — PHI-adjacent risk identified (medical leave queries) |
| **PHI Authorized** | No — however, PHI-adjacent data (medical leave type, disability accommodation context) may have been processed during pilot without authorization |
| **HIPAA Relevance** | Yes — PHI-adjacent processing risk identified; no BAA in place |
| **BAA Required** | Yes — BAA not executed. This is an open compliance gap. |
| **SOC 2 Coverage** | SOC 2 Type 1 only (Q3 2025). Type 2 not available. |
| **Risk Tier** | High |
| **Current Approval Status** | Under Review — Not Approved for Production |
| **Pilot Status** | 90-day pilot concluded March 31, 2026. Pilot continuation suspended pending governance review. |
| **Review Date** | June 2026 (AI Governance Committee) |
| **Conditions / Notes** | DO NOT extend pilot or execute full contract until: (1) BAA executed; (2) complete sub-processor list received and reviewed; (3) contractual prohibition on model training with MedData Nexus data confirmed; (4) data retention reduced to maximum 90 days contractually; (5) EU data transfer mechanism assessed and documented; (6) SOC 2 Type 2 received and reviewed. HR team must not submit any PHI or PHI-adjacent queries pending resolution. See VRA-AI-2026-001 for full findings. |
| **AI Vendor Risk Assessment** | VRA-AI-2026-001 (ClearBot section) — Risk: High. Four significant findings including no BAA and ambiguous model training terms. |
| **Incident History** | Finding CB-005: Unauthorized EU data processing during pilot (under investigation by Legal) |

---

### System 4: Predictive Staffing Model

| Field | Value |
|-------|-------|
| **System Name** | Workforce Predictive Staffing Model |
| **System ID** | AI-SYS-004 |
| **Owner** | Data Science Team |
| **Business Owner** | VP of Operations |
| **Purpose** | Internal ML model that forecasts staffing demand by department and region based on historical workforce data, seasonal patterns, and growth projections. Outputs are used by HR and Operations for headcount planning. |
| **Vendor** | Internal — MedData Nexus Data Science Team |
| **Model / Technology** | XGBoost regression model; trained on internal workforce data; hosted on internal AWS infrastructure (SageMaker endpoint) |
| **Hosting Location** | AWS us-east-1 (MedData Nexus infrastructure); no external data transfer |
| **Data Classification Processed** | Internal — workforce aggregate data (headcount, role distribution, tenure, attrition rates). No individual employee identifying data in training features. |
| **PHI Authorized** | No — no PHI in scope. Workforce data is internal classification. |
| **HIPAA Relevance** | No — no PHI or health information processed |
| **BAA Required** | N/A — internal system |
| **SOC 2 Coverage** | Included in MedData Nexus SOC 2 scope |
| **Risk Tier** | Medium |
| **Current Approval Status** | Approved |
| **Approval Date** | October 1, 2025 |
| **Review Date** | October 2026 |
| **Conditions / Notes** | Annual model performance review required. Model card maintained at `/ml-governance/staffing-model/model-card-v1.md`. Data Science team must retrain annually or upon significant workforce restructuring. Bias review required before each retraining (age, gender, location demographic fairness). |
| **AI Vendor Risk Assessment** | N/A — internally developed |
| **Incident History** | None |

---

### System 5: Clinical Coding Assist (Pilot — Pending Approval)

| Field | Value |
|-------|-------|
| **System Name** | CodeAssist Health Clinical Coding Assist |
| **System ID** | AI-SYS-005 |
| **Owner** | Clinical Operations |
| **Business Owner** | Chief Medical Informatics Officer |
| **Purpose** | AI-assisted ICD-10 and CPT coding tool — proposed for use by medical coding staff to suggest billing codes based on clinical documentation. Intended to reduce coding time and improve accuracy. |
| **Vendor** | CodeAssist Health, Inc. (fictional) |
| **Model / Technology** | CodeAssist proprietary clinical NLP model; SaaS deployment |
| **Hosting Location** | CodeAssist infrastructure — US-only per vendor documentation (not independently verified) |
| **Data Classification Processed** | **Restricted — PHI** (clinical notes, diagnoses, procedure descriptions, patient identifiers required for coding context) |
| **PHI Authorized** | Pending — PHI processing authorization requires: CISO approval + executed BAA + Legal review + Clinical Operations governance sign-off |
| **HIPAA Relevance** | Critical — processes PHI directly. This is a HIPAA-regulated activity. BAA is a legal requirement before any PHI is shared with vendor. |
| **BAA Required** | Yes — BAA not executed. BAA negotiation in progress (CodeAssist legal, initiated March 1, 2026). |
| **SOC 2 Coverage** | SOC 2 Type 2 in progress — audit period Q1 2026; report estimated Q3 2026. Not currently available. |
| **Risk Tier** | Critical |
| **Current Approval Status** | Pending CISO Approval + BAA Execution + Legal Review |
| **Review Date** | Governance Committee review scheduled May 2026 — approval decision deferred until BAA executed and SOC 2 report received |
| **Conditions / Notes** | **No PHI may be shared with CodeAssist until all of the following are complete:** (1) BAA executed and reviewed by Legal; (2) CodeAssist SOC 2 Type 2 report received and reviewed by IT Security; (3) AI Vendor Risk Assessment completed; (4) Clinical informatics governance review completed; (5) CISO written approval issued; (6) Pilot scope defined with explicit data element permissions and minimum necessary limitations. Clinical Operations has been notified that this system is in a pending state and may not be used with real patient data until approval is complete. Proof-of-concept may proceed with fully de-identified synthetic patient data only. |
| **AI Vendor Risk Assessment** | VRA-AI-2026-002 (planned; not yet completed — blocked pending SOC 2 and BAA) |
| **Incident History** | None — system not yet in use with real data |

---

## 3. Register Summary

| System ID | System Name | Risk Tier | PHI Processing | BAA Status | Approval Status |
|-----------|------------|-----------|----------------|------------|-----------------|
| AI-SYS-001 | Internal RAG Chatbot | High | Not authorized | N/A (self-hosted) | In Assessment |
| AI-SYS-002 | NovaMind API Summarizer | Medium | Not authorized | Executed (NM-001) | Approved (conditions) |
| AI-SYS-003 | ClearBot HR Chatbot | High | PHI-adjacent risk | Not executed — GAP | Under Review — Not Approved |
| AI-SYS-004 | Predictive Staffing Model | Medium | No PHI | N/A (internal) | Approved |
| AI-SYS-005 | CodeAssist Clinical Coding | Critical | Pending authorization | Not executed — in negotiation | Pending CISO + Legal + BAA |

---

## 4. Version History

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| 1.0 | January 15, 2026 | IT Security | Initial inventory — 3 systems (AI-SYS-001, 002, 004) |
| 1.1 | February 1, 2026 | IT Security | Added AI-SYS-003 (ClearBot pilot identified post-deployment) |
| 1.2 | March 15, 2026 | IT Security | Added AI-SYS-005 (CodeAssist pilot request from Clinical Ops); updated ClearBot status to Under Review per VRA findings |
| 1.3 | April 15, 2026 | IT Security | Updated AI-SYS-001 status to In Assessment; added Capstone 2 assessment note; updated NovaMind conditions |

---

*Approved by: Constant Yung, CISO — April 15, 2026*  
*Next full register review: July 2026 (Quarterly AI Governance Committee)*  
*Classification: Confidential — maintained by IT Security*
