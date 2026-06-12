> Synthetic data for Capstone 2 testing only.
> No real patient, customer, credential, contract, or GuidePoint client data.

---

# MedData Nexus Health Systems
## Artificial Intelligence Usage Policy
**Document ID:** POL-AI-001  
**Version:** 2.0  
**Effective Date:** April 1, 2026  
**Owner:** Chief Information Security Officer  
**Classification:** Internal  
**Review Cycle:** Annual

---

## 1. Purpose

This policy governs the approved and prohibited uses of artificial intelligence (AI) tools and systems at MedData Nexus Health Systems, including the internally hosted RAG (Retrieval-Augmented Generation) chatbot deployed for compliance, legal, and clinical administrative staff. As AI tools become more embedded in daily workflows, it is essential that all personnel understand their responsibilities in ensuring AI is used safely, ethically, and in compliance with applicable regulations including HIPAA, SOC 2, and applicable state privacy laws.

This policy applies to all MedData Nexus employees, contractors, and third-party personnel who access MedData Nexus systems or data.

---

## 2. Scope

This policy applies to:

- The MedData Nexus Internal RAG Chatbot (deployed April 2026, hosted internally on AWS infrastructure)
- Any third-party AI tools approved for use on MedData Nexus data (see AI System Inventory, AI-INV-001)
- AI/ML models developed internally by the MedData Nexus Data Science team
- General-purpose AI tools (e.g., large language model APIs) accessed by employees in the course of their work

---

## 3. Approved Use Cases

The following use cases are approved for the Internal RAG Chatbot and other authorized AI tools. All outputs from AI tools must be treated as drafts requiring human review before any action is taken.

### 3.1 Policy and Procedure Search
Employees may use the Internal RAG Chatbot to search and retrieve relevant passages from MedData Nexus's internal policy library, standard operating procedures, and regulatory guidance documents. The chatbot is not authoritative — the official policy document repository remains the source of truth.

### 3.2 Compliance Evidence Lookup
Compliance analysts may use the chatbot to locate evidence artifacts, prior assessment results, and control narratives relevant to active audit activities. All retrieved evidence must be verified against the primary evidence repository (GP-S3 / SharePoint compliance folders) before submission to auditors or regulators.

### 3.3 Drafting Summaries for Human Review
Users may request AI-generated draft summaries of internal documents, meeting notes, or findings — provided the output is reviewed and edited by a qualified human before distribution. Draft summaries may not be forwarded externally without human review sign-off. Drafts involving regulatory interpretation must be reviewed by Legal or Compliance prior to use.

### 3.4 Template Population
AI tools may be used to pre-populate standard templates (BAA checklists, risk assessment forms, vendor questionnaire summaries) with retrieved data. All populated fields must be reviewed and approved by the requesting employee before submission.

### 3.5 Training and Awareness Research
HR and L&D teams may use approved AI tools to assist in developing training content, summarizing regulatory updates, or generating quiz questions for security awareness programs. All content must be reviewed by a subject matter expert before use.

---

## 4. Prohibited Uses

The following uses are explicitly prohibited. Violations are subject to disciplinary action up to and including termination, and may result in regulatory reporting obligations.

### 4.1 Clinical Decision Support
AI tools at MedData Nexus are not approved for use in any clinical decision-making context. No AI output may be used to diagnose, treat, prescribe for, or advise on patient care. Clinical coding assist tools (where separately approved with appropriate controls) are scoped exclusively to administrative coding functions and must have licensed clinical oversight.

### 4.2 PHI Processing Without Authorization
Protected Health Information (PHI) as defined under HIPAA (45 CFR §160.103) may not be submitted to any AI tool — internal or external — without explicit CISO authorization and a documented data handling agreement. This includes the Internal RAG Chatbot, which is not approved to process PHI unless a specific data handling review has been completed and documented in the AI System Inventory.

### 4.3 External Sharing of AI Outputs
AI-generated outputs derived from MedData Nexus internal documents may not be shared externally (with clients, vendors, regulators, or the public) without explicit human review and appropriate approval. AI outputs are not official MedData Nexus communications.

### 4.4 Autonomous Decision-Making
No AI tool may make autonomous decisions that affect patient care, employment status, vendor approval, or regulatory compliance status. AI tools assist human decision-makers — they do not replace them.

### 4.5 Use of Unapproved AI Tools
Employees may not use personal AI accounts, consumer-grade AI tools (e.g., public LLM web interfaces), or unapproved third-party AI APIs to process MedData Nexus internal, confidential, or restricted data. The AI System Inventory (AI-INV-001) lists all approved tools.

### 4.6 Prompt Injection Attempts
Attempting to manipulate AI system behavior through crafted inputs ("prompt injection"), attempting to extract system prompts or retrieved context, or attempting to use AI tools to access data beyond the user's authorization level are prohibited and constitute a security incident.

---

## 5. User Responsibilities

All users of MedData Nexus AI tools are responsible for:

1. **Verification:** Treating all AI outputs as drafts. Verifying factual claims against primary sources before acting on them.
2. **Data hygiene:** Not submitting sensitive, confidential, or restricted data to AI tools unless explicitly authorized for that specific tool and use case.
3. **Reporting:** Reporting any unexpected, anomalous, or concerning AI behavior to the IT Security team within 24 hours (see Section 7).
4. **Training:** Completing the annual AI Awareness and Safe Use training module (assigned in the LMS by January 31 each year).
5. **Output ownership:** Recognizing that they are responsible for any action taken based on AI output. "The AI said so" is not an acceptable justification for a policy violation or patient harm.

---

## 6. Data Handling Rules

### 6.1 Data Classification Alignment
AI tools must be used in alignment with the MedData Nexus Data Classification Policy (POL-DC-001). The applicable data tier determines what may and may not be submitted to an AI tool:

| Data Tier | May be submitted to Internal RAG Chatbot? | May be submitted to Approved External AI APIs? |
|-----------|------------------------------------------|------------------------------------------------|
| Public | Yes | Yes |
| Internal | Yes | With manager approval |
| Confidential | Yes (read-only retrieval) | No, unless specific authorization exists |
| Restricted (incl. PHI) | No — CISO authorization required | No |

### 6.2 Logging and Retention
All queries submitted to the Internal RAG Chatbot are logged with user identity, timestamp, and query text. Logs are retained for 90 days in the security information and event management (SIEM) platform and reviewed monthly by the IT Security team for anomalous patterns.

### 6.3 Output Retention
AI-generated outputs that are incorporated into official documents, evidence packages, or communications must be retained as part of the associated record per the applicable retention schedule. The AI-generated origin must be noted in the document metadata.

---

## 7. Escalation Path for Anomalous AI Behavior

If any user observes AI behavior that is unexpected, appears to be manipulated, outputs data the user should not have access to, or generates content that appears to violate policy or patient safety, the user must:

1. **Stop using the tool immediately** and do not retry the query.
2. **Preserve the output** (screenshot or copy the full response) and note the exact query submitted.
3. **Report within 24 hours** to IT Security via the internal ticketing system (ServiceNow → Security Incident → AI System Anomaly) or directly to the CISO (security@meddata-nexus.fake).
4. **Do not share** the anomalous output with anyone other than IT Security and authorized reviewers.

AI system anomalies are treated as potential security incidents and are subject to the Incident Response Plan (IRP-001).

---

## 8. Version History

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| 1.0 | January 15, 2025 | M. Torres, Compliance | Initial policy — general AI tool usage guidance |
| 2.0 | April 1, 2026 | C. Yung, CISO | Added RAG chatbot-specific rules (Sections 3.1-3.2, 4.6, 6.1-6.3, Section 7); updated prohibited uses to include prompt injection; aligned data handling table with POL-DC-001 v2 |

---

## 9. Related Documents

- POL-DC-001: Data Classification Policy
- AI-INV-001: AI System Inventory Register
- IRP-001: Incident Response Plan
- POL-PHI-001: PHI Handling Procedures
- BAA-TPL-001: Business Associate Agreement Template

---

*Approved by: Constant Yung, CISO — April 1, 2026*  
*Next review date: April 1, 2027*
