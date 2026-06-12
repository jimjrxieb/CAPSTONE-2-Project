> Synthetic data for Capstone 2 testing only.
> No real patient, customer, credential, contract, or GuidePoint client data.

---

# MedData Nexus Health Systems
## Data Classification Policy
**Document ID:** POL-DC-001  
**Version:** 2.0  
**Effective Date:** March 1, 2026  
**Owner:** Chief Information Security Officer  
**Classification:** Internal  
**Review Cycle:** Annual

---

## 1. Purpose

MedData Nexus Health Systems handles a wide range of data types across its healthcare SaaS platform, internal operations, and client-facing services. The sensitivity of this data varies significantly — from publicly available press releases to protected health information subject to HIPAA. This policy establishes a four-tier data classification framework that governs how data is labeled, handled, stored, transmitted, and used — including use within AI systems.

All MedData Nexus employees, contractors, and vendors with access to MedData Nexus data are required to understand and apply this classification framework. Mishandling of classified data, regardless of intent, may constitute a reportable breach and is subject to disciplinary action.

---

## 2. Classification Tiers

### Tier 1: Public

**Definition:** Data that is approved for unrestricted public release. Disclosure of this data causes no harm to MedData Nexus, its clients, employees, or patients.

**Examples:**
- Press releases and official news announcements
- Published marketing materials and website content
- Job postings and publicly listed product documentation
- Published regulatory filings (non-sensitive portions)
- Conference presentations approved for external distribution

**Handling Requirements:**
- No special protection required
- May be stored, shared, and transmitted without restriction
- No access controls required beyond standard system authentication

**AI System Rules:** May be submitted to any approved AI tool without restriction.

---

### Tier 2: Internal

**Definition:** Data intended for use within MedData Nexus only. Not sensitive enough to cause regulatory or reputational harm if disclosed, but not intended for public distribution.

**Examples:**
- Internal policies and procedures (non-PHI, non-contract)
- Organizational charts and internal directories
- General IT documentation and system architecture overviews (non-sensitive)
- Internal training materials
- Workforce planning documents (aggregate, non-identifying)
- Meeting notes not containing confidential or restricted content

**Handling Requirements:**
- Must be stored on MedData Nexus-approved systems
- May be shared internally without restriction; external sharing requires manager approval
- Must not be posted publicly without CISO or Marketing approval
- Must be labeled "Internal" in document headers or metadata

**AI System Rules:** May be submitted to the Internal RAG Chatbot without restriction. May be submitted to approved external AI APIs only with manager approval.

---

### Tier 3: Confidential

**Definition:** Sensitive business data whose unauthorized disclosure could cause financial harm, competitive disadvantage, regulatory penalty, or damage to client relationships. This tier includes most business-critical data at MedData Nexus.

**Examples:**
- Vendor and customer contracts (including MSAs, SOWs, and pricing schedules)
- Business Associate Agreements (BAAs)
- Financial statements, revenue figures, and budget forecasts
- Intellectual property, proprietary algorithms, and source code
- Merger, acquisition, and partnership discussions
- Employee compensation, performance review data, and HR investigation records
- Security assessment findings (prior to public disclosure or remediation)
- Audit reports, SOC 2 reports, and internal audit findings
- System architecture details that could assist an attacker

**Handling Requirements:**
- Must be stored on MedData Nexus-approved systems with access controls enforced
- Encryption required at rest (AES-256 minimum) and in transit (TLS 1.2 minimum)
- Access limited to employees and contractors with a documented business need
- Must be labeled "Confidential" in document headers
- External sharing requires VP-level or above approval plus a signed NDA or contractual confidentiality obligation
- Printing requires approval and printed copies must be secured
- Disposal: shredding (physical) or cryptographic erasure (digital)

**AI System Rules:** May be submitted to the Internal RAG Chatbot for read-only retrieval and summarization. May not be submitted to external AI APIs unless a specific authorization is documented in the AI System Inventory (AI-INV-001). AI-generated outputs derived from Confidential data must be reviewed before external distribution.

---

### Tier 4: Restricted

**Definition:** Highly sensitive data whose unauthorized disclosure could cause severe harm — including regulatory penalties, patient harm, legal liability, or reputational damage. This is the highest classification tier.

**Examples:**
- **Protected Health Information (PHI):** Any individually identifiable health information as defined by HIPAA (45 CFR §160.103), including the 18 HIPAA identifiers (see POL-PHI-001 for complete list)
- **Electronic Protected Health Information (ePHI):** PHI stored or transmitted in electronic form
- Authentication credentials, cryptographic keys, API secrets, and access tokens
- Cardholder data (PAN, CVV, expiration date) — PCI DSS scope
- Social Security Numbers and government-issued ID numbers
- Biometric data
- Legal holds, active litigation materials, and privileged attorney-client communications
- Regulatory breach notifications and incident reports containing PHI
- Internal security incident investigation details during active investigation

**Handling Requirements:**
- Must be stored on MedData Nexus-approved systems with strict need-to-know access controls
- Encryption required at rest (AES-256) and in transit (TLS 1.2 minimum, TLS 1.3 preferred)
- Multi-factor authentication required for all access
- Access must be individually authorized and logged; access logs reviewed quarterly
- Must be labeled "Restricted" in document headers and metadata
- External sharing: only permitted under an executed BAA (for PHI) or equivalent data protection agreement; requires CISO approval
- De-identification required before any use in training data, analytics, or AI systems (see POL-PHI-001 for de-identification procedures)
- Disposal: NIST SP 800-88 compliant data destruction; certificate of destruction required
- Incident involving Restricted data must be treated as a potential breach immediately

**AI System Rules:**
- Restricted data **may not** be submitted to the Internal RAG Chatbot without explicit CISO authorization and documentation of the specific use case in the AI System Inventory.
- Restricted data **may not** be submitted to any external AI API or third-party AI system without: (a) executed BAA covering the specific data type, (b) CISO written approval, and (c) documented entry in AI System Inventory.
- AI systems that output data appearing to be Restricted tier must trigger an immediate incident report (see POL-AI-001, Section 7).
- **Human-in-the-loop (HITL) review is mandatory** before any AI output involving Restricted tier data is acted upon or distributed.

---

## 3. Labeling Requirements

All MedData Nexus documents must include the appropriate classification label. Acceptable label formats:

| Tier | Header Label | Email Subject Prefix |
|------|-------------|---------------------|
| Public | `Classification: Public` | `[PUBLIC]` |
| Internal | `Classification: Internal` | `[INTERNAL]` |
| Confidential | `Classification: Confidential` | `[CONFIDENTIAL]` |
| Restricted | `Classification: Restricted` | `[RESTRICTED]` |

Documents containing data from multiple tiers must be classified at the highest applicable tier. When in doubt, classify higher and consult the Data Governance team.

---

## 4. Retention Alignment

Data retention is governed by the MedData Nexus Records Retention Schedule (GOV-RET-001). Classification tier informs minimum retention requirements and governs when and how data must be disposed:

| Tier | Minimum Retention | Disposal Method |
|------|------------------|-----------------|
| Public | Per record type in retention schedule | Standard deletion |
| Internal | Per record type in retention schedule | Standard deletion |
| Confidential | Per record type + legal hold if applicable | Cryptographic erasure or shredding |
| Restricted (PHI/ePHI) | 6 years from creation or last use (HIPAA minimum) | NIST 800-88 compliant destruction |

---

## 5. AI System Handling Matrix (Summary)

| Data Tier | Internal RAG Chatbot | Approved External AI APIs | Unapproved AI Tools |
|-----------|---------------------|--------------------------|---------------------|
| Public | Permitted | Permitted | Not recommended |
| Internal | Permitted | Manager approval required | Prohibited |
| Confidential | Permitted (read/summarize) | Authorization required (AI-INV-001) | Prohibited |
| Restricted | CISO authorization required + HITL | CISO + BAA + AI-INV-001 entry required | Prohibited |

---

## 6. Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| Data Owner (business unit VP) | Assigns classification to data created within their domain; approves exceptions |
| Data Steward (department manager) | Enforces classification within their team; approves internal sharing requests |
| IT Security / CISO | Sets and enforces policy; approves Restricted tier AI use cases; reviews audit logs |
| All Employees | Apply labels correctly; follow handling rules; report classification violations |
| Third-party Vendors | Comply with applicable tier requirements per contract and BAA |

---

## 7. Version History

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| 1.0 | September 1, 2024 | IT Security Team | Initial policy — three-tier framework |
| 2.0 | March 1, 2026 | C. Yung, CISO | Added Restricted tier; expanded AI system handling rules; added HITL requirement for Restricted AI outputs; aligned with AI Governance Policy v1 |

---

## 8. Related Documents

- POL-AI-001: AI Usage Policy
- POL-PHI-001: PHI Handling Procedures
- AI-INV-001: AI System Inventory Register
- AI-GOV-001: AI Governance Policy
- GOV-RET-001: Records Retention Schedule
- BAA-TPL-001: Business Associate Agreement Template

---

*Approved by: Constant Yung, CISO — March 1, 2026*  
*Next review date: March 1, 2027*
