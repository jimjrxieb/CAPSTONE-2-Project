> Synthetic data for Capstone 2 testing only.
> No real patient, customer, credential, contract, or GuidePoint client data.

---

# MedData Nexus Health Systems
## AI Vendor Risk Assessment
**Document ID:** VRA-AI-2026-001  
**Assessment Date:** March 10, 2026  
**Prepared By:** IT Security / Vendor Risk Management team  
**Reviewed By:** Constant Yung, CISO; Simone Beaumont, Privacy Counsel  
**Classification:** Confidential  
**Distribution:** CISO, Legal, Compliance, Vendor Risk Management

---

## 1. Purpose

This assessment evaluates the security and privacy risk posture of third-party AI vendors currently in use or under evaluation by MedData Nexus Health Systems. Given the sensitive nature of data processed on the MedData Nexus platform — including clinical administrative records and workforce data — AI vendors represent a category of elevated risk requiring specialized assessment criteria beyond the standard vendor security questionnaire.

Assessment criteria include: data processing location and jurisdiction, sub-processor chain, BAA status, SOC 2 Type 2 availability, data retention practices, AI model training on customer data, prompt logging policies, security certifications, and overall risk rating.

Two vendors are assessed in this document: **NovaMind API** (document summarization) and **ClearBot Enterprise** (HR chatbot).

---

## 2. Assessment: NovaMind API

**Vendor Name:** NovaMind Technologies, Inc.  
**Service:** Document summarization API — used by MedData Nexus compliance team to generate draft summaries of vendor questionnaires, audit reports, and policy documents  
**Contract Status:** Active (MSA executed January 2025; annual renewal pending May 2026)  
**Primary Contact:** vendor-support@novamind-tech.fake  
**Assessment Version:** 1.1 (updated March 2026 to reflect prompt logging disclosure)

### 2.1 Vendor Profile

NovaMind Technologies, Inc. is a US-based AI software company headquartered in Austin, TX, providing large language model API services for enterprise document processing. The NovaMind API is used by MedData Nexus's compliance team to summarize vendor security questionnaire responses and generate first-draft summaries of policy documents for human review.

**Data processed:**
- Vendor questionnaire responses (Confidential tier)
- Draft policy summaries (Internal/Confidential tier)
- Security assessment executive summaries (Confidential tier)
- **PHI is explicitly excluded** from any submissions to NovaMind API per current operating procedures

### 2.2 Assessment Findings

| Assessment Criterion | Finding | Evidence Source |
|---------------------|---------|-----------------|
| **Data processing location** | US-only (AWS us-east-1, us-west-2) | NovaMind DPA, March 2025 |
| **Data sovereignty / jurisdiction** | United States — CCPA and federal privacy law applicable | NovaMind Privacy Policy v4.2 |
| **Sub-processors** | 3 disclosed: AWS (infrastructure), Anthropic (base model via API), Datadog (logging/monitoring) | NovaMind Sub-Processor List, January 2026 |
| **BAA status** | BAA executed January 15, 2025 | MedData Nexus BAA Registry, entry NM-001 |
| **SOC 2 Type 2** | Available — Security and Availability criteria; audit period Q1-Q4 2024; no exceptions noted | Clearview Assurance LLC (fictional auditor) SOC 2 report, received Feb 2025 |
| **ISO 27001** | Certified — issued November 2024, scope covers API infrastructure and data processing | Certificate MN-ISO-2024-0047 (fictional) |
| **Data retention** | Prompt inputs and outputs retained for **30 days** for abuse monitoring and service improvement; retention configurable to 0 days for Enterprise tier (requires contract amendment) | NovaMind Enterprise Terms, Section 4.3 |
| **AI model training on customer data** | No — NovaMind contractually commits not to use customer-submitted data to train or fine-tune production models | NovaMind DPA §6.4; confirmed via security questionnaire |
| **Prompt logging policy** | Prompts are logged for 30 days; accessible to NovaMind security and abuse teams; **not** accessible to other customers | NovaMind Security FAQ, March 2026 |
| **Encryption in transit** | TLS 1.3 required for all API calls | NovaMind API documentation |
| **Encryption at rest** | AES-256, AWS KMS managed keys | NovaMind SOC 2 report, CC6.1 |
| **Incident notification** | 72-hour notification per DPA (stricter than HIPAA 60-day for security incidents) | NovaMind DPA §8.2 |
| **Penetration testing** | Annual third-party penetration test; results shared with Enterprise customers on NDA | NovaMind security posture summary |

### 2.3 Risk Findings

**Finding NM-001 (Medium):** NovaMind retains prompt logs for 30 days by default. While the BAA is in place and NovaMind contractually prohibits PHI submission, the 30-day log retention creates a risk that inadvertently submitted sensitive data could persist. MedData Nexus cannot audit NovaMind's internal prompt log access controls.

*Recommendation:* Negotiate zero-retention (0-day) prompt logging for the Enterprise contract at renewal (May 2026). Confirm via contract amendment before renewal execution. Add technical control to flag and block submissions containing potential PHI patterns (SSN, MRN, DOB formats) before API submission.

**Finding NM-002 (Low):** Anthropic is listed as a sub-processor (base model API). Anthropic's own sub-processor chain and data handling practices for API calls were not independently verified — MedData Nexus relies on NovaMind's representation of Anthropic's data handling.

*Recommendation:* Request NovaMind's sub-processor due diligence documentation for Anthropic. Confirm that Anthropic API usage is covered by NovaMind's DPA pass-through obligations.

### 2.4 Overall Risk Rating: **MEDIUM**

**Rationale:** NovaMind has acceptable security certifications (SOC 2 Type 2, ISO 27001), an executed BAA, US-only data processing, and a contractual commitment against customer data training. The primary risks are the 30-day default prompt log retention and the sub-processor chain visibility gap. These are manageable through contract negotiation and technical controls. PHI is not currently submitted to NovaMind, and operating procedures explicitly prohibit this.

**Approval Status:** Approved with conditions  
**Conditions:** (1) Zero-retention prompt logging negotiated at May 2026 renewal; (2) technical PHI pattern detection added before submission layer; (3) annual sub-processor review  
**Next Review Date:** May 2026 (contract renewal) or immediately upon any security incident

---

## 3. Assessment: ClearBot Enterprise

**Vendor Name:** ClearBot AI, Inc.  
**Service:** HR chatbot — used by MedData Nexus HR team to answer employee questions about benefits, leave policies, and HR procedures  
**Contract Status:** Trial — 90-day pilot (January – March 2026); full contract not yet executed  
**Primary Contact:** enterprise@clearbot-ai.fake  
**Assessment Version:** 1.0

### 3.1 Vendor Profile

ClearBot AI, Inc. is a startup AI company (founded 2023, Series A, headquarters San Francisco, CA) providing enterprise HR chatbot services. The ClearBot Enterprise product was deployed as a 90-day pilot by the MedData Nexus HR team in January 2026 to reduce HR helpdesk volume. The pilot was deployed without completing the standard AI vendor risk assessment, which is the subject of this review.

**Data processed during pilot:**
- Employee names and employee IDs (Internal tier)
- HR policy documents indexed in the ClearBot knowledge base (Internal tier)
- Leave request status queries (may include medical leave type — potential PHI-adjacent)
- Benefits enrollment status queries

**Concern flagged during assessment:** Employees submitting queries about medical leave (FMLA, disability accommodations) may inadvertently expose health condition information. This was not assessed prior to pilot deployment.

### 3.2 Assessment Findings

| Assessment Criterion | Finding | Evidence Source |
|---------------------|---------|-----------------|
| **Data processing location** | US and EU (Ireland) — multi-region by default; no US-only option on current pricing tier | ClearBot Privacy Policy v1.2 |
| **Data sovereignty / jurisdiction** | US federal + EU GDPR — data subject to Irish law when processed in EU region | ClearBot Terms of Service |
| **Sub-processors** | List not provided — requested January 20, 2026; not received as of March 10, 2026 | Vendor questionnaire — outstanding item |
| **BAA status** | **No BAA executed.** ClearBot does not offer a BAA as a standard contract term. BAA process "under review by ClearBot legal" per email dated February 3, 2026. | Vendor questionnaire; email correspondence |
| **SOC 2 Type 2** | **Not available.** ClearBot is SOC 2 Type 1 only (point-in-time assessment, Q3 2025). Type 2 not anticipated until Q4 2026. | ClearBot security overview document |
| **ISO 27001** | Not certified | ClearBot security overview document |
| **Data retention** | **Unclear.** ClearBot Terms of Service state "conversation data retained for service improvement purposes for up to 24 months." No configurable retention option documented. | ClearBot Terms of Service §7.2 |
| **AI model training on customer data** | **Unknown.** Security questionnaire response: "ClearBot may use aggregate, anonymized interaction data to improve our models. Customer data is not used to train models directly." Scope of "anonymized" not defined; no contractual prohibition on training. | ClearBot questionnaire response (unverified) |
| **Prompt logging policy** | All conversations logged; retention period up to 24 months; accessible to ClearBot product and support teams | ClearBot Terms of Service §7.2 |
| **Encryption in transit** | TLS 1.2 supported; TLS 1.3 not confirmed | ClearBot API documentation |
| **Encryption at rest** | AES-256 claimed; not independently verified (no SOC 2 Type 2 report) | ClearBot questionnaire (unverified claim) |
| **Incident notification** | Terms require notification "within a reasonable time" — no specific timeline | ClearBot Terms of Service §11.3 |
| **Penetration testing** | Annual, internal team only; no third-party penetration test as of assessment date | ClearBot questionnaire |

### 3.3 Risk Findings

**Finding CB-001 (Critical):** No BAA has been executed. MedData Nexus is a HIPAA Covered Entity. The ClearBot HR chatbot is processing queries that may include Protected Health Information (specifically: medical leave type, disability accommodation context). Operating a PHI-adjacent AI system without a BAA is a HIPAA violation risk.

*Recommendation:* **Suspend the ClearBot pilot immediately** until a BAA is executed or it is confirmed that no PHI-adjacent data will be processed. Do not proceed to full contract without executed BAA.

**Finding CB-002 (High):** Data retention of up to 24 months with no configurable option is excessive. Conversation data includes employee identifiers and may include PHI-adjacent content. ClearBot's sub-processor list has not been provided; it is unknown which downstream parties may have access to retained data.

*Recommendation:* Require documented data retention policy (maximum 90 days) and complete sub-processor list as preconditions for any contract execution.

**Finding CB-003 (High):** ClearBot's statement that customer data is not used "directly" for model training, combined with the claim of using "aggregate, anonymized" interaction data, is ambiguous. Without a contractual prohibition, MedData Nexus cannot confirm that employee conversation data will not be used in model training.

*Recommendation:* Require explicit contractual prohibition on use of MedData Nexus employee conversation data for any model training, fine-tuning, or product improvement, regardless of claimed anonymization.

**Finding CB-004 (Medium):** SOC 2 Type 1 only. Type 1 assessments provide no evidence that controls operated effectively over a period of time. Without a Type 2 report, MedData Nexus cannot independently verify that ClearBot's claimed security controls are functioning.

*Recommendation:* Require SOC 2 Type 2 as a precondition for full contract execution. Estimated availability Q4 2026 — if timeline is acceptable, proceed only after report is received and reviewed.

**Finding CB-005 (Medium):** EU data processing without MedData Nexus's knowledge or consent during pilot. Employee data (including names and identifiers) may have been transferred to EU region. Data transfer mechanism (Standard Contractual Clauses or equivalent) was not in place during the pilot period.

*Recommendation:* Investigate scope of EU data transfers during pilot; assess whether data transfer impact assessment (DTIA) is required; notify Legal Counsel for GDPR exposure analysis.

### 3.4 Overall Risk Rating: **HIGH**

**Rationale:** ClearBot presents multiple unacceptable risk conditions: no BAA, unclear data retention, ambiguous model training clause, EU data transfers without authorization, and unverified security controls. The combination of no BAA with PHI-adjacent data processing is a direct HIPAA compliance risk.

**Approval Status:** Under Review — **Do Not Approve for Full Contract**  
**Immediate Action Required:** Suspend pilot or confirm PHI/PHI-adjacent data is fully excluded before pilot continuation; initiate BAA negotiation; obtain complete sub-processor list  
**Next Review Date:** Upon receipt of: (1) executed BAA, (2) sub-processor list, (3) contractual training prohibition, (4) clarified retention policy — then re-assess

---

## 4. Summary Comparison Table

| Criterion | NovaMind API | ClearBot Enterprise |
|-----------|-------------|---------------------|
| BAA Status | Executed | Not executed — CRITICAL gap |
| SOC 2 Type 2 | Available (2024) | Type 1 only |
| ISO 27001 | Certified | Not certified |
| Data Retention | 30 days (configurable to 0) | Up to 24 months (not configurable) |
| Model Training on Customer Data | No (contractual prohibition) | Unknown / ambiguous |
| Sub-Processor Disclosure | Full list provided | Not provided |
| Data Processing Location | US only | US + EU (unauthorized) |
| Incident Notification | 72 hours | "Reasonable time" (undefined) |
| Pen Testing | Annual (third-party) | Annual (internal only) |
| **Overall Risk Rating** | **Medium** | **High** |
| **Approval Status** | Approved with conditions | Under Review — Not Approved |

---

## 5. Assessor Sign-Off

| Role | Name | Date |
|------|------|------|
| Lead Assessor | IT Security Analyst, Vendor Risk Management | March 10, 2026 |
| CISO Review | Constant Yung | March 12, 2026 |
| Privacy Counsel Review | Simone Beaumont | March 12, 2026 |

---

*Classification: Confidential*  
*Retained by: Vendor Risk Management — minimum 5 years*  
*Next scheduled review cycle: Q1 2027 (or upon any material contract change or vendor security incident)*
