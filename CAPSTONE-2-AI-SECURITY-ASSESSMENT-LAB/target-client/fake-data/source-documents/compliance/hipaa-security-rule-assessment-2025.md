> Synthetic data for Capstone 2 testing only.
> No real patient, customer, credential, contract, or GuidePoint client data.

---

# MedData Nexus Health Systems
## HIPAA Security Rule Gap Assessment — 2025
**Document ID:** COMP-HIPAA-2025-001  
**Assessment Date:** October 15, 2025  
**Assessor:** Internal Compliance Team, supported by external HIPAA counsel  
**Classification:** Confidential  
**Review Cycle:** Annual (next assessment due Q4 2026)

---

## Executive Summary

MedData Nexus Health Systems conducted its annual HIPAA Security Rule gap assessment in October 2025, covering all three safeguard categories: Administrative, Physical, and Technical. The assessment evaluated the organization's compliance with 45 CFR Part 164, Subpart C (Security Standards for the Protection of Electronic Protected Health Information).

**Overall Assessment Result: Partially Compliant**

The organization demonstrates strong implementation of Administrative Safeguards. Physical safeguards have two identified gaps requiring remediation. Technical Safeguards have three gaps, one of which is rated High risk and requires immediate attention. No material breaches or incidents were attributable to safeguard failures during the assessment period.

### Executive Summary Table

| Safeguard Category | Controls Assessed | Fully Implemented | Partially Implemented | Not Implemented | Gaps Identified |
|--------------------|------------------|-------------------|-----------------------|-----------------|-----------------|
| Administrative | 9 | 8 | 1 | 0 | 1 (Low) |
| Physical | 6 | 4 | 1 | 1 | 2 (1 Med, 1 Low) |
| Technical | 8 | 5 | 2 | 1 | 3 (1 High, 2 Med) |
| **Total** | **23** | **17** | **4** | **2** | **6** |

---

## 1. Administrative Safeguards (45 CFR §164.308)

Administrative safeguards are the policies, procedures, and workforce controls that protect ePHI. MedData Nexus has mature administrative safeguard implementation, with documented policies covering all required areas.

### 1.1 Security Management Process (§164.308(a)(1))
**Status:** Fully Implemented  
Risk analysis conducted annually (most recent: September 2025). Risk management plan in place. Sanction policy documented in HR-POL-004. Information system activity reviews performed monthly via SIEM dashboard.

### 1.2 Assigned Security Responsibility (§164.308(a)(2))
**Status:** Fully Implemented  
CISO (Constant Yung) designated as HIPAA Security Officer. Role documented in governance charter and organizational chart. Contact information registered with HHS.

### 1.3 Workforce Security (§164.308(a)(3))
**Status:** Fully Implemented  
Authorization and supervision procedures documented. Workforce clearance process (background checks for roles with PHI access). Termination procedures include same-day access revocation enforced via automated IAM workflow.

### 1.4 Information Access Management (§164.308(a)(4))
**Status:** Fully Implemented  
Access authorization tied to role-based access controls (RBAC) in AWS IAM and application layer. PHI access requires documented business justification. Minimum necessary standard enforced via data classification controls.

### 1.5 Security Awareness and Training (§164.308(a)(5))
**Status:** Partially Implemented — Gap Identified  
Annual security awareness training completed by 91% of workforce (target: 100%). Malicious software protection training is included in the annual curriculum. Log-in monitoring training was added in 2025 but has not been fully rolled out to all clinical support staff.

**Gap ADM-01:**
- **Gap Description:** Security awareness training completion rate is 91%, below the 100% target. Clinical support staff team (approximately 40 employees) has not completed the updated AI-safe-use module added in April 2026.
- **Risk Rating:** Low
- **Remediation Target:** January 31, 2026
- **Owner:** Director of Human Resources, IT Security team
- **Remediation Plan:** Automated LMS reminder campaign; mandatory completion deadline enforced by HR with manager escalation for non-compliance.

### 1.6 Security Incident Procedures (§164.308(a)(6))
**Status:** Fully Implemented  
Incident response plan (IRP-001) is current (v3, 2026). Incident reporting procedures communicated to all staff. SIEM alerting configured for anomalous ePHI access patterns.

### 1.7 Contingency Plan (§164.308(a)(7))
**Status:** Fully Implemented  
Data backup plan (daily encrypted backups to S3 with cross-region replication), disaster recovery plan (RTO: 4 hours, RPO: 1 hour for critical systems), emergency mode operation procedures, and testing and revision procedures documented. Annual DR exercise completed June 2025 — all recovery time objectives met.

### 1.8 Evaluation (§164.308(a)(8))
**Status:** Fully Implemented  
This annual gap assessment serves as the formal periodic technical and nontechnical evaluation. External HIPAA counsel reviews findings and validates assessor conclusions.

### 1.9 Business Associate Contracts (§164.308(b)(1))
**Status:** Fully Implemented  
BAA inventory maintained in the Vendor Risk Management system. 47 active BAAs on file. New vendor onboarding workflow requires BAA execution before any PHI access is provisioned. Annual BAA review completed; 3 BAAs updated in 2025 to add AI processing clauses.

---

## 2. Physical Safeguards (45 CFR §164.310)

Physical safeguards control physical access to systems that store or process ePHI. MedData Nexus is primarily a cloud-native environment; the primary data center is AWS. Physical risks are concentrated at corporate office locations and a small co-location facility.

### 2.1 Facility Access Controls (§164.310(a)(1))
**Status:** Partially Implemented — Gap Identified  
Corporate headquarters (Seattle, WA) has badge access, security camera coverage, and visitor log. The Vancouver, BC office location (Canadian operations) currently relies on building management security only. MedData Nexus has not independently validated badge access controls or implemented its own visitor log at the Vancouver location.

**Gap PHY-01:**
- **Gap Description:** Vancouver office does not have MedData Nexus-controlled facility access controls. Reliance on building management controls is not independently verified. Visitor log is not maintained by MedData Nexus staff.
- **Risk Rating:** Medium
- **HIPAA Reference:** §164.310(a)(1)
- **Remediation Target:** March 31, 2026
- **Owner:** VP of Operations (Canada)
- **Remediation Plan:** Procurement of keycard access system integrated with corporate IAM; visitor log procedure to be implemented and enforced by office manager; annual audit of facility access records.

### 2.2 Workstation Use (§164.310(b))
**Status:** Fully Implemented  
Workstation use policy published and acknowledged by all employees. PHI may only be accessed on managed devices. BYOD prohibited for PHI access. Screen lock enforcement via MDM (30-second auto-lock).

### 2.3 Workstation Security (§164.310(c))
**Status:** Fully Implemented  
All managed devices enrolled in MDM (Jamf for macOS, Intune for Windows). Full disk encryption enabled (FileVault / BitLocker). Remote wipe capability confirmed. Physical security (cable locks) required for shared workspaces.

### 2.4 Device and Media Controls (§164.310(d)(1))
**Status:** Not Implemented — Gap Identified  
Formal media disposal and reuse procedures have not been documented or implemented for decommissioned hardware. IT asset disposition (ITAD) is handled ad hoc by the IT team without a standardized process or chain of custody.

**Gap PHY-02:**
- **Gap Description:** No formal documented procedure for hardware disposal. Decommissioned laptops and servers are processed without a consistent data sanitization standard or certificate of destruction.
- **Risk Rating:** Low
- **HIPAA Reference:** §164.310(d)(1)
- **Remediation Target:** February 28, 2026
- **Owner:** IT Operations Manager
- **Remediation Plan:** Develop formal ITAD procedure aligned with NIST SP 800-88; engage certified ITAD vendor; implement certificate of destruction workflow in IT asset management system.

### 2.5 Accountability (§164.310(d)(2)(iii))
**Status:** Fully Implemented  
Hardware assets tracked in ServiceNow CMDB. Movements of portable media logged. Annual physical asset inventory conducted.

### 2.6 Data Backup and Storage (§164.310(d)(2)(iv))
**Status:** Fully Implemented  
ePHI backed up daily to encrypted S3 buckets (separate from primary storage). Backup integrity checks performed weekly. Restoration tested quarterly.

---

## 3. Technical Safeguards (45 CFR §164.312)

Technical safeguards are the technologies and policies that protect ePHI and control access to it. Three gaps were identified in this category, including one High-risk finding.

### 3.1 Access Control (§164.312(a)(1))
**Status:** Fully Implemented  
Unique user identification enforced. Emergency access procedure documented (break-glass accounts with dual authorization). Automatic logoff enforced via session timeout (15 minutes for PHI-handling applications). Encryption and decryption of ePHI implemented.

### 3.2 Audit Controls (§164.312(b))
**Status:** Partially Implemented — Gap Identified  
SIEM (Sumo Logic) captures application access logs for the primary SaaS platform. However, audit logging is not currently enabled for the internal PostgreSQL RDS instances that store non-PHI operational data with incidental PHI fields.

**Gap TEC-01:**
- **Gap Description:** Database-level audit logging is not consistently enabled across all RDS instances. Two legacy RDS clusters (rds-ops-prod-01, rds-analytics-prod-01) do not have CloudTrail Data Events or RDS audit logging enabled. This creates a gap in the audit trail for ePHI access at the database layer.
- **Risk Rating:** Medium
- **HIPAA Reference:** §164.312(b)
- **Remediation Target:** January 15, 2026
- **Owner:** Platform Engineering Lead
- **Remediation Plan:** Enable RDS audit logging and CloudTrail data events for all RDS instances containing ePHI; route logs to centralized SIEM; alert on anomalous query patterns.

### 3.3 Integrity (§164.312(c)(1))
**Status:** Fully Implemented  
ePHI integrity verified through checksums at upload and download. Application-layer validation prevents unauthorized modification. S3 Object Lock enabled on backup buckets.

### 3.4 Person or Entity Authentication (§164.312(d))
**Status:** Partially Implemented — Gap Identified  
MFA is enforced for all corporate SSO (Okta). However, two legacy internal application APIs accept service account tokens without MFA equivalent controls, and one internal administrative web interface was identified during the assessment as accessible with only a username and password (no MFA).

**Gap TEC-02:**
- **Gap Description:** One internal administrative interface (meddata-ops-admin.internal, used for platform configuration) does not enforce MFA. Service account credentials for two legacy API integrations are long-lived tokens with no rotation schedule.
- **Risk Rating:** Medium
- **HIPAA Reference:** §164.312(d)
- **Remediation Target:** December 31, 2025
- **Owner:** IT Security, Platform Engineering
- **Remediation Plan:** Enforce Okta MFA on all internal web interfaces; implement 90-day rotation for service account tokens via AWS Secrets Manager; deprecate legacy API token authentication in favor of OAuth 2.0.

### 3.5 Transmission Security (§164.312(e)(1))
**Status:** Not Implemented for One System — Gap Identified  
All external-facing APIs and client portals use TLS 1.2 or higher. However, one internal microservice-to-microservice communication path within the EKS cluster transmits ePHI fields over an unencrypted channel (HTTP within the cluster network). While the cluster network is isolated, in-transit encryption is not applied.

**Gap TEC-03 (HIGH RISK):**
- **Gap Description:** The patient-data-sync microservice communicates with the legacy ingestion-api service over HTTP within the EKS cluster. While this traffic is within the AWS VPC and not externally accessible, it transmits ePHI fields (patient ID, encounter dates) in cleartext. An attacker with cluster access (e.g., via a compromised pod) could intercept this traffic.
- **Risk Rating:** High
- **HIPAA Reference:** §164.312(e)(1)
- **Remediation Target:** November 30, 2025
- **Owner:** Platform Engineering Lead, DevSecOps team
- **Remediation Plan:** Implement mutual TLS (mTLS) for all pod-to-pod communication containing ePHI using service mesh (Istio); enforce NetworkPolicy to restrict lateral movement; validate via penetration test after implementation.

### 3.6 Encryption and Decryption (§164.312(e)(2)(ii))
**Status:** Fully Implemented  
AES-256 at rest for all S3 buckets and RDS instances (AWS KMS managed keys). TLS 1.2/1.3 for all external transmission channels. Key management via AWS KMS with annual key rotation.

---

## 4. Gap Summary and Remediation Tracking

| Gap ID | Safeguard | HIPAA Reference | Description | Risk | Target Date | Owner | Status |
|--------|-----------|----------------|-------------|------|-------------|-------|--------|
| ADM-01 | Administrative | §164.308(a)(5) | Training completion below 100% | Low | Jan 31, 2026 | HR / IT Security | In Progress |
| PHY-01 | Physical | §164.310(a)(1) | Vancouver office access controls | Medium | Mar 31, 2026 | VP Operations (CA) | Not Started |
| PHY-02 | Physical | §164.310(d)(1) | No formal ITAD procedure | Low | Feb 28, 2026 | IT Operations | In Progress |
| TEC-01 | Technical | §164.312(b) | RDS audit logging gaps | Medium | Jan 15, 2026 | Platform Engineering | In Progress |
| TEC-02 | Technical | §164.312(d) | MFA gaps on legacy interfaces | Medium | Dec 31, 2025 | IT Security / Platform | Remediated |
| TEC-03 | Technical | §164.312(e)(1) | ePHI in-cluster HTTP transmission | **High** | Nov 30, 2025 | Platform Engineering | Remediated |

*Note: TEC-02 and TEC-03 are marked Remediated pending validation in Q1 2026 assessment.*

---

## 5. Assessor Sign-Off

This assessment was conducted by the MedData Nexus Internal Compliance Team with review by external HIPAA counsel (Baker & Monroe LLP, Healthcare Practice Group — fictional).

| Role | Name | Signature | Date |
|------|------|-----------|------|
| HIPAA Security Officer / CISO | Constant Yung | *on file* | October 15, 2025 |
| Compliance Director | M. Torres | *on file* | October 15, 2025 |
| External HIPAA Counsel | J. Whitmore (Baker & Monroe LLP) | *on file* | October 20, 2025 |

---

*Next assessment scheduled: October 2026*  
*Classification: Confidential — Do not distribute outside MedData Nexus compliance, legal, and executive teams without CISO approval*
