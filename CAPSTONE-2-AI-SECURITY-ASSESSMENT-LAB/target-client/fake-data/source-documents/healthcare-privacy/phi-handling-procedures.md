> Synthetic data for Capstone 2 testing only.
> No real patient, customer, credential, contract, or GuidePoint client data.

---

# MedData Nexus Health Systems
## PHI Handling Procedures
**Document ID:** POL-PHI-001  
**Version:** 2.1  
**Effective Date:** January 15, 2026  
**Owner:** Privacy Officer / Chief Information Security Officer  
**Classification:** Internal  
**Review Cycle:** Annual

---

## 1. Purpose

This document defines the procedures for identifying, handling, accessing, storing, transmitting, de-identifying, and disposing of Protected Health Information (PHI) at MedData Nexus Health Systems. Compliance with these procedures is mandatory for all MedData Nexus employees, contractors, and authorized third parties who create, access, use, or disclose PHI in any form as part of their work.

Violations of these procedures constitute a potential HIPAA violation and must be reported immediately. Intentional violations will result in disciplinary action up to and including termination.

---

## 2. What Constitutes PHI at MedData Nexus

Protected Health Information (PHI) is any individually identifiable health information that relates to:
- The past, present, or future physical or mental health condition of an individual
- The provision of health care to an individual
- The past, present, or future payment for health care to an individual

**AND** that identifies, or could reasonably be used to identify, the individual.

### 2.1 The 18 HIPAA Identifiers

HIPAA (45 CFR §164.514) defines 18 categories of identifiers that, when associated with health information, create PHI. MedData Nexus treats any data element from the following list as potentially PHI when combined with health-related information:

1. **Names** — Patient full name, first name, last name, initials
2. **Geographic subdivisions smaller than a state** — Street address, city, county, precinct, ZIP code, and equivalent geocodes (note: the first 3 digits of a ZIP code may be used if the geographic unit contains more than 20,000 people)
3. **Dates (other than year)** — Birth date, admission date, discharge date, death date, and any dates directly related to an individual (note: year alone is not an identifier)
4. **Phone numbers** — Telephone numbers, fax numbers
5. **Fax numbers** — (included above, listed separately per HIPAA enumeration)
6. **Email addresses** — Any email address associated with the individual
7. **Social Security Numbers** — Full or partial SSN
8. **Medical record numbers (MRN)** — Patient medical record identifiers assigned by any covered entity
9. **Health plan beneficiary numbers** — Insurance member IDs, beneficiary numbers
10. **Account numbers** — Bank account numbers or other financial account identifiers when associated with a health record
11. **Certificate/license numbers** — Professional license numbers (e.g., physician DEA numbers when in a patient context)
12. **Vehicle identifiers and serial numbers** — Including license plate numbers
13. **Device identifiers and serial numbers** — Any device associated with a patient
14. **Web Universal Resource Locators (URLs)** — Any URL linked to an identified individual's record
15. **Internet Protocol (IP) addresses** — IP addresses when linked to a patient session or record
16. **Biometric identifiers** — Finger and voice prints, retinal scans
17. **Full-face photographs and any comparable images** — Any photographic image that could identify the individual
18. **Any other unique identifying number, characteristic, or code** — Including chart numbers, case numbers, or any internal identifier that could be used to re-identify an individual

**At MedData Nexus specifically:** Patient MRNs, encounter IDs, and provider assignment records are treated as PHI regardless of context, as they can be used to re-identify individuals through the platform's data model. Contact the Privacy Officer if you are uncertain whether a specific data element constitutes PHI.

---

## 3. Minimum Necessary Standard

MedData Nexus applies the HIPAA Minimum Necessary Standard (45 CFR §164.502(b)) to all uses and disclosures of PHI.

**What this means in practice:**
- Only access PHI that you need to perform your specific job function
- Do not access PHI of colleagues, family members, or individuals about whom you are personally curious — even if you technically have system access
- When sharing PHI (internally or externally), share only the fields necessary for the specific purpose — not the full patient record
- When requesting PHI from a colleague or system, specify which fields are needed and why
- Bulk or "just in case" PHI access is prohibited

**Workforce supervisors are responsible** for ensuring that their team's access permissions are appropriately scoped. Semi-annual access reviews are conducted by the IT Security team; supervisors must certify that their direct reports' access remains appropriate.

---

## 4. Access Controls for PHI

### 4.1 Role-Based Access Control (RBAC)

Access to PHI is governed by role-based access control (RBAC) implemented in AWS IAM, the MedData Nexus application layer, and database access policies. Access is granted based on documented business role requirements, not by individual request alone.

**Role classifications for PHI access:**

| Role Category | PHI Access Level | Authorization Required |
|--------------|-----------------|----------------------|
| Clinical Support Staff | Read — designated patient records only | Department manager + Compliance approval |
| Compliance Analysts | Read — de-identified or specific fields for audit | Compliance Director + IT Security |
| Engineering (Production) | Break-glass access only — requires dual authorization | On-call approval + CISO notification |
| Data Science | De-identified data only — see Section 6 | Privacy Officer review + CISO sign-off |
| AI System (Internal RAG Chatbot) | Not authorized for PHI — see Section 5 | CISO authorization required for any exception |
| Executives | No standing PHI access — executive reporting uses aggregate, de-identified data | N/A |

### 4.2 PHI Access Logging

All access to PHI is logged in the SIEM (Sumo Logic) with:
- User identity (authenticated username)
- Timestamp (UTC)
- System accessed
- Action (read, modify, export)
- Data scope (where technically feasible — which records or data types were accessed)

Logs are retained for a minimum of 6 years (HIPAA minimum). Logs are reviewed:
- Monthly: anomalous access pattern review by IT Security
- Quarterly: privileged access review by IT Security + Compliance
- Upon request: during incident investigations and HIPAA compliance audits

### 4.3 Access Provisioning and Deprovisioning

PHI access is provisioned via the HR lifecycle system (BambooHR → Okta SSO → downstream systems):
- **Provisioning:** access granted within 1 business day of manager approval; new employees complete HIPAA training before PHI access is activated
- **Deprovisioning:** access revoked automatically on the employee's last day; manual revocation for terminations with cause is completed same-day by IT Security
- **Access review:** semi-annual review; supervisors must certify all team member access within 10 business days of review initiation

---

## 5. PHI in AI Systems

**PHI may not be ingested into, processed by, or submitted as input to any MedData Nexus AI system — including the Internal RAG Chatbot — without explicit written authorization from the CISO and a documented data handling review.**

This prohibition covers:
- Submitting patient data in query text to the Internal RAG Chatbot
- Indexing clinical documents, discharge summaries, or any records containing the 18 HIPAA identifiers into the RAG knowledge base
- Using PHI as training data for any internal or external ML model
- Sharing PHI with any third-party AI API (NovaMind, ClearBot, or any other)

**Exception process:** If a specific AI use case requires PHI processing, the following steps are required before any PHI is provided to an AI system:

1. **Use case documentation:** Submit a written description of the use case to the Privacy Officer and CISO (email: privacy@meddata-nexus.fake)
2. **Data classification review:** Privacy Officer reviews what PHI elements are involved and confirms minimum necessary scope
3. **HIPAA authorization analysis:** Legal Counsel assesses whether the use case is covered by an existing authorization, TPO (Treatment, Payment, Operations) exception, or requires patient authorization
4. **AI vendor assessment:** If a third-party AI system is involved, complete the AI Vendor Risk Assessment (VRA-AI-TPL-001) and confirm BAA execution
5. **CISO written approval:** Documented in the AI System Inventory (AI-INV-001) with specific authorization scope, data elements permitted, and sunset date
6. **Implementation review:** IT Security reviews technical controls before the AI system is permitted to process PHI

The Internal RAG Chatbot as currently deployed is **not authorized for PHI**. Documents containing PHI must be de-identified per Section 6 before any indexing into the RAG knowledge base.

---

## 6. De-Identification Procedures

PHI may be de-identified for use in analytics, AI training, research, and reporting. MedData Nexus supports two HIPAA-approved de-identification methods per 45 CFR §164.514:

### 6.1 Safe Harbor Method (§164.514(b)(2))

The Safe Harbor method requires the removal of all 18 categories of HIPAA identifiers (listed in Section 2.1) from the data. Additionally:

- The covered entity must have no actual knowledge that the remaining information could be used alone or in combination to identify an individual
- ZIP codes: Only the first 3 digits may be retained, and only if the geographic unit represented by those 3 digits contains more than 20,000 people. Otherwise, the entire ZIP code must be removed
- Dates: All dates more specific than year must be removed. For individuals over 89 years of age, all ages and dates must be aggregated into a single category of "age 90 or older"

**Process for Safe Harbor de-identification at MedData Nexus:**
1. Run the de-identification script (`tools/phi-deident/safe_harbor.py`) on the source dataset
2. Script automatically removes all 18 identifier fields and applies ZIP/date rules
3. Output reviewed by a second team member before use
4. De-identification log created (source dataset, date, de-identification method, reviewer, output dataset location)
5. De-identified output stored in the analytics data environment separate from PHI systems

### 6.2 Expert Determination Method (§164.514(b)(1))

The Expert Determination method requires a qualified statistician or expert in privacy and health data to apply generally accepted statistical and scientific principles to determine that the risk of identifying an individual is very small.

**When to use Expert Determination:** When the Safe Harbor method would remove too many data elements to be analytically useful (e.g., research requiring geographic data below the 3-digit ZIP level, or longitudinal studies requiring detailed date precision).

**Expert Determination process at MedData Nexus:**
1. Compliance Director identifies an approved external expert (currently: HealthStat Analytics LLC — fictional)
2. Expert performs de-identification analysis and provides a written attestation
3. Attestation reviewed and approved by Privacy Officer before data is released
4. Expert Determination outputs are tracked in the de-identification log

**Minimum documentation for all de-identification:**
- Source dataset identifier
- De-identification method used (Safe Harbor or Expert Determination)
- Date performed
- Name of person who performed de-identification and reviewer
- Expert attestation (if Expert Determination)
- Output dataset location and access controls

---

## 7. Breach Definition and Reporting Path

### 7.1 Breach Definition

A PHI breach is defined as the acquisition, access, use, or disclosure of PHI in a manner not permitted by the HIPAA Privacy Rule (45 CFR §164.402), subject to the following exceptions:

- **Unintentional access:** An unintentional acquisition, access, or use of PHI by an authorized workforce member acting under the authority of the covered entity, if the access was made in good faith and within the scope of authority
- **Inadvertent disclosure:** An inadvertent disclosure by an authorized person to another authorized person at the same covered entity
- **Good faith belief:** The covered entity or business associate has a good faith belief that an unauthorized person to whom the disclosure was made would not have been able to retain the information

**If any of the above exceptions do NOT apply, a breach is presumed unless the organization can demonstrate a low probability that PHI was compromised** based on a four-factor risk assessment (45 CFR §164.402(2)).

### 7.2 Breach Reporting Path

Any employee who discovers or suspects a PHI breach must:

1. **Report immediately** — do not wait to "confirm" or "investigate first." Report within 24 hours to:
   - Direct supervisor (immediately)
   - Privacy Officer (privacy@meddata-nexus.fake or ext. 5533)
   - IT Security (security@meddata-nexus.fake or ext. 5100)

2. **Preserve evidence** — do not delete, modify, or access additional information that might be relevant to the breach investigation

3. **Do not disclose** — do not discuss the suspected breach with anyone other than supervisors and the Privacy Officer

4. **Legal notification** — Legal Counsel will be notified by the Privacy Officer and will conduct the breach risk assessment. Regulatory notification timelines are governed by the Incident Response Plan (IRP-001, Section 6).

**MedData Nexus maintains a zero-retaliation policy** for good-faith breach reports. Any employee who discovers and promptly reports a suspected breach will not face adverse employment action for the report itself.

---

## 8. Employee Training Requirements

All MedData Nexus employees who access, handle, or may inadvertently encounter PHI are required to complete:

| Training | Frequency | Completion Deadline | Consequence of Non-Completion |
|----------|-----------|--------------------|-----------------------------|
| HIPAA Privacy and Security Fundamentals | Annual | January 31 each year | Access to PHI systems suspended until completed |
| PHI Handling Procedures (this document) | Upon hire and annually | Within 30 days of hire; January 31 annually | Same as above |
| Breach Recognition and Reporting | Upon hire and annually | Within 30 days of hire; January 31 annually | Same as above |
| AI Safe Use (POL-AI-001) | Upon policy update | Within 60 days of policy update | Access to AI tools suspended until completed |

Training completion is tracked in the LMS (Workday Learning). Compliance Director reviews completion rates monthly and escalates non-completion to HR and department managers.

---

## 9. Related Documents

- POL-AI-001: AI Usage Policy
- POL-DC-001: Data Classification Policy
- AI-INV-001: AI System Inventory Register
- IRP-001: Incident Response Plan
- BAA-TPL-001: Business Associate Agreement Template
- GOV-RET-001: Records Retention Schedule
- VRA-AI-TPL-001: AI Vendor Risk Assessment Template

---

## 10. Version History

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| 1.0 | March 1, 2024 | Privacy Officer | Initial procedures |
| 2.0 | July 15, 2025 | M. Torres, Compliance | Added AI system PHI prohibition (Section 5); added exception process |
| 2.1 | January 15, 2026 | C. Yung, CISO | Updated RBAC table to reflect Internal RAG Chatbot; clarified Expert Determination process; added AI system access row to Table 4.1 |

---

*Approved by: Constant Yung, CISO, and M. Torres, Privacy Officer — January 15, 2026*  
*Next review date: January 15, 2027*
