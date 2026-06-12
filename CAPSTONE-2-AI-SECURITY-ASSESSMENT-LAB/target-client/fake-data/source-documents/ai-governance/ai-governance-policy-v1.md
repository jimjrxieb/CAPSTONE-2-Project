> Synthetic data for Capstone 2 testing only.
> No real patient, customer, credential, contract, or GuidePoint client data.

---

# MedData Nexus Health Systems
## AI Governance Policy
**Document ID:** AI-GOV-001  
**Version:** 1.0  
**Effective Date:** January 1, 2026  
**Owner:** Chief Information Security Officer  
**Classification:** Internal  
**Review Cycle:** Annual and upon any material AI system deployment

---

## 1. Purpose and Context

MedData Nexus Health Systems operates in a regulated healthcare environment where the use of artificial intelligence and machine learning systems carries significant risk — to patient safety, data privacy, regulatory compliance, and organizational integrity. Uncontrolled AI adoption creates HIPAA exposure, SOC 2 control gaps, and operational risk that must be systematically managed.

This AI Governance Policy establishes a mandatory framework for the acquisition, deployment, monitoring, and retirement of all AI and ML systems that process, access, or could influence MedData Nexus data or operations. It applies without exception to systems developed internally and systems operated by third-party vendors.

This policy reflects the organization's commitment to the principles of responsible AI: human oversight, transparency, proportionate risk management, and protection of the individuals whose data the organization is entrusted to protect.

---

## 2. Scope

This policy applies to:

- All AI and machine learning systems that process MedData Nexus data in any form
- All AI systems used by MedData Nexus employees, contractors, or authorized third parties in the course of MedData Nexus business — regardless of whether those systems are owned, licensed, or accessed via API
- All internal ML model development by the MedData Nexus Data Science team
- AI capabilities embedded in otherwise non-AI software (e.g., AI-assisted features in HR software, EHR systems, or contract management tools)

**This policy does not apply to:**
- Purely rule-based automation systems with no statistical or probabilistic components (e.g., if/then workflow automation)
- Standard data analytics tools producing descriptive statistics (e.g., BI dashboards with no predictive or generative component)

When in doubt about whether a system is in scope, consult the IT Security team before use or acquisition.

---

## 3. AI System Registration Requirement

**All AI systems that process MedData Nexus data must be registered in the AI System Inventory Register (AI-INV-001) before any data is processed.**

This is a hard requirement with no exceptions. No grace period is offered for systems already in use at the time this policy takes effect (January 1, 2026) — existing systems must be registered by February 28, 2026 or decommissioned.

### 3.1 Registration Process

To register an AI system:

1. **Submit a registration request** to IT Security (itsecurity@meddata-nexus.fake) with: system name, vendor (or "internal"), purpose description, data types to be processed, intended user population, and risk tier estimate
2. **IT Security conducts initial review** (5 business days): confirms data classification of data to be processed; identifies BAA requirement; assigns preliminary risk tier
3. **Risk assessment completed** per Section 4 (timeline varies by tier)
4. **AI Governance Committee reviews** and approves, approves with conditions, or rejects
5. **System added to AI-INV-001** with status, conditions, and review date

### 3.2 Consequences of Non-Registration

Deploying or using an AI system on MedData Nexus data without registration is a policy violation and may constitute a HIPAA technical safeguard gap (if PHI is involved). Violations will be:
- Reported to the employee's manager and HR
- Documented in the employee's personnel record
- Assessed for regulatory impact by Legal Counsel
- Subject to disciplinary action up to termination

Systems discovered in use without registration will be immediately suspended pending assessment.

---

## 4. Risk Tiers

All registered AI systems are assigned a risk tier based on the sensitivity of data processed, regulatory exposure, and potential impact of system failure or misuse. Risk tier determines approval authority and monitoring requirements.

### Tier: Critical

**Definition:** AI systems that process PHI or other Restricted-tier data; AI systems whose failure could directly harm patient safety; AI systems with clinical decision-making capability or influence over clinical workflows.

**Examples at MedData Nexus:** Clinical coding assist tools, any AI system that receives or generates PHI as part of its operation, AI systems used in direct patient care workflows.

**Requirements:**
- Board Audit Committee awareness (annual reporting)
- CISO written approval required
- Legal Counsel review required (BAA, regulatory authorization)
- Clinical governance review required (if clinical data involved)
- SOC 2 Type 2 report from vendor required (or equivalent)
- BAA execution required before any data processing
- Quarterly monitoring and annual re-assessment
- HITL (human-in-the-loop) review mandatory for all AI outputs before any action is taken

### Tier: High

**Definition:** AI systems that process Confidential-tier data; AI systems with broad data access across multiple organizational functions; AI systems accessible to a large population of users; AI systems with significant potential reputational or operational impact if compromised.

**Examples at MedData Nexus:** Internal RAG chatbot, HR chatbot (given access to sensitive workforce data), AI systems processing vendor contracts or financial data.

**Requirements:**
- CISO written approval required
- IT Security risk assessment required
- SOC 2 Type 2 report or equivalent vendor security evidence required
- BAA required if PHI-adjacent or if BAA risk analysis indicates requirement
- Quarterly monitoring; semi-annual re-assessment
- HITL review required for high-stakes outputs (regulatory submissions, client communications)
- Incident reporting: any anomaly within 24 hours (see Section 7)

### Tier: Medium

**Definition:** AI systems that process Internal-tier data; systems with limited scope and user population; systems whose failure would have limited operational impact; vendor AI APIs with verified security credentials and no PHI exposure.

**Examples at MedData Nexus:** Predictive staffing model, document summarization API (NovaMind) with verified no-PHI constraint, internal analytics models on aggregate data.

**Requirements:**
- IT Security approval required
- Vendor security questionnaire and basic due diligence
- BAA required if any PHI risk exists
- Annual monitoring and re-assessment
- Incident reporting: any anomaly within 72 hours

### Tier: Low

**Definition:** AI systems that process only Public-tier data; proof-of-concept systems with no production data; AI tools used for internal productivity with no access to MedData Nexus proprietary data.

**Examples at MedData Nexus:** AI writing tools used to draft marketing copy from public sources; internal code completion tools operating only on open-source code.

**Requirements:**
- Business owner approval
- Brief IT Security notification (no full assessment required)
- Annual confirmation that data processed remains Public-tier
- Incident reporting: within 5 business days if scope changes

---

## 5. Approval Authority by Tier

| Risk Tier | Primary Approval Authority | Additional Required Reviews |
|-----------|--------------------------|----------------------------|
| Critical | Board Audit Committee + CISO + Legal Counsel | Clinical governance (if clinical); Privacy Officer |
| High | CISO | IT Security risk assessment; Legal Counsel if PHI-adjacent |
| Medium | IT Security (VP level or above) | Business owner sign-off |
| Low | Business owner | IT Security notification |

**Approval is not retroactive.** A system in use without approval at the appropriate level must be suspended until proper approval is obtained.

---

## 6. Prohibited AI Uses

The following uses of AI systems are prohibited at MedData Nexus, regardless of risk tier or approval status. No business justification overrides these prohibitions.

### 6.1 Autonomous PHI Processing Without Human Review

No AI system may process PHI as the sole decision-maker for any action affecting patient records, clinical workflows, or health information without a licensed clinician or authorized healthcare professional reviewing and approving the AI's output. AI may assist human decision-making with PHI — it may not replace it.

### 6.2 AI-Generated Clinical Advice Without Licensed Clinician Review

No AI system may provide clinical advice, diagnosis, treatment recommendations, or clinical coding determinations without review and approval by a licensed clinician (for clinical decisions) or certified medical coder (for coding determinations). AI-generated clinical content that has not been reviewed by a licensed professional may not be shared with patients, included in health records, or submitted to payers.

### 6.3 Unregistered AI Systems

AI systems that are not listed in AI-INV-001 may not process MedData Nexus data. Period. This prohibition applies even if the system would qualify for Low-tier approval — registration is required regardless of tier.

### 6.4 AI Systems Processing Data Outside Approved Scope

AI systems may only process the data types and data elements approved in their AI-INV-001 entry. An AI system approved for Internal-tier data may not be used to process Confidential or Restricted data without a new approval cycle.

### 6.5 Shadow AI

"Shadow AI" — use of personal AI accounts, consumer AI tools, or unapproved AI APIs to process MedData Nexus proprietary data — is prohibited. This includes use of personal ChatGPT, Gemini, Copilot, or similar accounts to process MedData Nexus internal documents, client data, or any non-public information.

### 6.6 AI Manipulation Attempts

Attempting to manipulate AI system behavior (prompt injection, adversarial inputs designed to bypass safety controls, attempts to extract system prompts or retrieve data outside the user's authorization) is prohibited and constitutes a security incident (see Section 7).

---

## 7. Monitoring and Audit Requirements

### 7.1 Ongoing Monitoring

| Risk Tier | Monitoring Frequency | Responsible Party |
|-----------|---------------------|------------------|
| Critical | Continuous (SIEM integration required) | IT Security |
| High | Monthly inference log review; quarterly assessment | IT Security |
| Medium | Quarterly review | IT Security + Business Owner |
| Low | Annual confirmation | Business Owner |

### 7.2 Quarterly AI Governance Committee Review

The AI Governance Committee meets quarterly to:
- Review AI-INV-001 for completeness and accuracy
- Assess the status of systems Under Review or In Assessment
- Review incident history for all High and Critical systems
- Approve or reject new system registrations at High tier and above
- Review vendor risk assessment findings for systems up for renewal

Committee composition: CISO (chair), Privacy Officer, Compliance Director, Legal Counsel, CTO representative, Clinical Operations representative (as applicable). Quorum: 4 members including CISO.

### 7.3 Annual Reassessment

All High and Critical systems must undergo a full reassessment annually, including:
- Refresh of the vendor risk assessment (or internal security review)
- Review of inference logs and anomaly reports from the past year
- Confirmation of continued BAA validity and vendor compliance
- Update of AI-INV-001 entry with current status and conditions

### 7.4 Drift and Behavioral Monitoring

For AI systems where behavioral drift is a material risk (e.g., models that update or fine-tune continuously), MedData Nexus will implement behavioral monitoring:
- Baseline behavior established at approval time
- Regular adversarial test suite run against production system (minimum quarterly for High/Critical)
- Significant behavioral change triggers re-assessment
- Output quality monitoring — anomalous output patterns trigger incident report

---

## 8. Incident Reporting for AI System Anomalies

Any AI system anomaly — including unexpected outputs, suspected manipulation, data outside expected context appearing in outputs, or system behavior inconsistent with its approved purpose — must be reported immediately.

**Reporting path:**
- Report within **24 hours** of discovery for High and Critical systems
- Report within **72 hours** for Medium systems
- Report via ServiceNow (Security Incident → AI System Anomaly category) or directly to IT Security (security@meddata-nexus.fake)
- For any anomaly involving potential PHI exposure: immediate notification to CISO and Privacy Officer by phone

AI system anomalies are treated as potential security incidents under IRP-001. The Prompt Injection Abuse playbook (IRP-001 Section 7.3) applies to suspected manipulation attempts.

**Zero retaliation for good-faith reporting.** Employees who report AI anomalies in good faith will not face adverse action.

---

## 9. Vendor AI Requirements

Any vendor or contractor that uses AI or ML systems to process MedData Nexus data as part of their service delivery must:

1. **Disclose AI use:** Proactively disclose any AI or ML processing of MedData Nexus data as part of their security questionnaire response
2. **Complete AI Vendor Assessment:** Complete the MedData Nexus AI Vendor Risk Assessment questionnaire (VRA-AI-TPL-001) before contract execution or AI capability deployment
3. **Execute a BAA:** If PHI is or may be processed, a BAA must be executed before any data processing occurs
4. **Prohibit training on customer data:** Contractually commit to not using MedData Nexus data to train, fine-tune, or improve AI models without explicit written consent
5. **Maintain SOC 2 Type 2:** Vendors operating AI systems at Medium risk or above must maintain a current SOC 2 Type 2 report covering the AI system
6. **Notify of AI system changes:** Vendors must notify MedData Nexus within 30 days of any material change to AI models or systems processing MedData Nexus data (e.g., model replacement, new sub-processors, data retention policy changes)

Failure to meet these requirements is grounds for contract suspension or termination.

---

## 10. Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| CISO | Policy owner; approves High/Critical systems; chairs AI Governance Committee; incident escalation |
| Privacy Officer | Reviews PHI-adjacent AI use cases; BAA adequacy review; breach determination for AI incidents |
| Compliance Director | Regulatory mapping; SOC 2 and HIPAA alignment; evidence packaging for AI governance audits |
| Legal Counsel | BAA negotiation and review; regulatory notification decisions; vendor contract review for AI clauses |
| IT Security Team | Vendor risk assessments; AI-INV-001 maintenance; monitoring; incident response |
| Data Science Team | Responsible for internal model governance, model cards, and retraining documentation |
| Business Owners (all departments) | Register all AI tools used by their team; ensure team compliance; approve Low-tier systems |
| All Employees | Follow AI Usage Policy (POL-AI-001); report anomalies; do not use unregistered AI tools |

---

## 11. Related Documents

- POL-AI-001: AI Usage Policy
- POL-DC-001: Data Classification Policy
- POL-PHI-001: PHI Handling Procedures
- AI-INV-001: AI System Inventory Register
- IRP-001: Incident Response Plan (including AI/ML Playbook, Section 7)
- BAA-TPL-001: Business Associate Agreement Template
- VRA-AI-TPL-001: AI Vendor Risk Assessment Template

---

## 12. Version History

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| 1.0 | January 1, 2026 | C. Yung, CISO | Initial policy |

*Next review scheduled: January 1, 2027, or within 60 days of any Critical AI system deployment*

---

*Approved by: Constant Yung, CISO — January 1, 2026*  
*Board Audit Committee awareness: confirmed February 2026 Board meeting*  
*Classification: Internal*
