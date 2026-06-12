> Synthetic data for Capstone 2 testing only.
> No real patient, customer, credential, contract, or GuidePoint client data.

---

# MedData Nexus Health Systems
## SOC 2 Type 2 Audit Summary — 2025
**Document ID:** COMP-SOC2-2025-001  
**Audit Period:** January 1, 2025 – December 31, 2025  
**Auditor:** Clearview Assurance LLC, Information Systems Audit Practice  
**Report Date:** February 14, 2026  
**Classification:** Confidential  
**Audience:** MedData Nexus Executive Team, Board Audit Committee, Clients (NDA required)

---

## 1. Executive Summary

MedData Nexus Health Systems engaged Clearview Assurance LLC to perform a SOC 2 Type 2 examination of its cloud-hosted healthcare SaaS platform for the period January 1 through December 31, 2025. The examination assessed controls relevant to the Security, Availability, and Confidentiality Trust Service Criteria (TSC), as defined by the AICPA.

**Overall Opinion:** The report contains a **qualified opinion** on the Security Trust Service Criteria due to one exception noted (CC6.7 — encryption of data in transit for a legacy internal API). All other Trust Service Criteria received an **unqualified (clean) opinion**.

This is MedData Nexus's third consecutive SOC 2 Type 2 report. The CC6.7 exception is new this year and represents a regression from the prior year report. Management has acknowledged the finding and has a documented remediation plan targeting Q2 2026.

### Summary Results Table

| Trust Service Criteria | Criteria Assessed | Exceptions | Opinion |
|----------------------|------------------|------------|---------|
| Security (CC Series) | 21 | 1 (CC6.7) | Qualified |
| Availability (A Series) | 7 | 0 | Unqualified |
| Confidentiality (C Series) | 5 | 0 | Unqualified |
| **Overall** | **33** | **1** | **Qualified** |

---

## 2. Scope of Examination

**System Description:** The MedData Nexus Healthcare SaaS Platform, including:
- Web application and API layer (hosted on AWS EKS, us-east-1 and us-west-2 regions)
- Relational data stores (Amazon RDS PostgreSQL, encrypted at rest)
- Object storage (Amazon S3, encrypted at rest with KMS)
- Internal administrative systems with access to production data
- Identity and access management systems (Okta SSO, AWS IAM)
- Monitoring and logging infrastructure (Sumo Logic SIEM)

**In-Scope Locations:** AWS cloud infrastructure (us-east-1, us-west-2); corporate headquarters (Seattle, WA); Vancouver, BC office (administrative functions only).

**Out of Scope:** Client-managed systems, client data not stored within MedData Nexus infrastructure, third-party subprocessor environments (assessed separately under vendor risk program).

---

## 3. Security Trust Service Criteria (CC Series)

### 3.1 Control Environment (CC1)
**Result: No exceptions noted.**  
The organization demonstrates a commitment to integrity and ethical values. Formal organizational structure with defined roles and responsibilities. Board Audit Committee oversight confirmed. Code of conduct acknowledged annually by all employees.

### 3.2 Communication and Information (CC2)
**Result: No exceptions noted.**  
Internal communication of security objectives is documented and distributed. External communication processes with clients regarding security incidents are defined in the client service agreement and incident response plan. Security awareness training completed by 91% of workforce (2% improvement from 2024).

### 3.3 Risk Assessment (CC3)
**Result: No exceptions noted.**  
Annual enterprise risk assessment conducted (most recent: September 2025). Risk register maintained and reviewed quarterly by the CISO and executive team. Risk appetite and tolerance levels formally documented and approved by the Board.

### 3.4 Monitoring Activities (CC4)
**Result: No exceptions noted.**  
Continuous monitoring via SIEM (Sumo Logic) covering application logs, authentication events, and infrastructure metrics. Quarterly internal control reviews conducted. Vulnerability scanning performed weekly using Tenable Nessus; results tracked in risk register.

### 3.5 Control Activities — Logical Access (CC6)
**Result: One exception noted (CC6.7).**

Criteria CC6.1 through CC6.6 and CC6.8: No exceptions noted. MFA enforced for all user-facing systems via Okta. RBAC implemented and reviewed semi-annually. Privileged access management controls in place with PAM tooling. Access provisioning and deprovisioning tied to HR lifecycle events.

**Exception — CC6.7: Encryption of Data in Transit (Legacy Internal API)**

*Criteria language (CC6.7):* The entity restricts the transmission of data to authorized internal and external parties using controls to protect against unauthorized access. The entity implements encryption for the transmission of confidential information.

*Exception observed:* During the audit period, Clearview Assurance identified that one internal API endpoint — the `nexus-data-bridge` service (used for data synchronization between the SaaS application and a legacy ETL pipeline) — transmitted data over HTTP without TLS encryption within the internal AWS VPC. This endpoint transmitted internal user identifiers and session tokens during the audit period.

*Impact:* While the endpoint was within a private VPC and not internet-accessible, data in transit was not encrypted, creating risk of interception by any entity with access to the VPC network layer (e.g., a compromised EC2 instance or EKS pod).

*Test period of non-compliance:* January 1 – October 14, 2025. Clearview Assurance confirmed that the endpoint was updated to require TLS 1.3 on October 15, 2025, following identification during the HIPAA Security Rule gap assessment. The exception is noted for the full audit period per SOC 2 reporting standards.

*Management response:* See Section 6.

### 3.6 Change Management (CC7)
**Result: No exceptions noted.**  
Formal change management process (ServiceNow ITSM) with testing and approval gates before production deployment. Emergency change procedures defined and tested. Change freeze periods observed during high-risk periods.

### 3.7 Risk Mitigation (CC8, CC9)
**Result: No exceptions noted.**  
Vendor risk assessments performed for all critical subprocessors. Business continuity and disaster recovery plans tested annually (June 2025 DR exercise — all RTO/RPO targets met). Cyber insurance maintained with coverage reviewed annually.

---

## 4. Availability Trust Service Criteria (A Series)

**Result: No exceptions noted.**

| Criteria | Description | Result |
|----------|-------------|--------|
| A1.1 | Performance monitoring — current and historical capacity | Passed |
| A1.2 | Environmental protections (AWS infrastructure) | Passed |
| A1.3 | Recovery and restoration of data | Passed |
| A1.4 | Infrastructure monitoring | Passed |
| A1.5 | Data backup and restoration | Passed |
| A1.6 | Processing completeness | Passed |
| A1.7 | Results of backups tested | Passed |

**Key metrics (audit period):**
- Platform availability (SaaS application): 99.94% (SLA: 99.9%)
- Planned maintenance windows: 8 (all within approved windows)
- Unplanned outages: 2 (total downtime: 47 minutes; both resolved within 30-minute RTO)
- Backup restoration test success rate: 100% (4 tests conducted)

---

## 5. Confidentiality Trust Service Criteria (C Series)

**Result: No exceptions noted.**

| Criteria | Description | Result |
|----------|-------------|--------|
| C1.1 | Identifies and maintains confidential information | Passed |
| C1.2 | Destroys confidential information when no longer needed | Passed |
| C1.3 | Restricts access to confidential information | Passed |
| C1.4 | Protects confidential information during processing | Passed |
| C1.5 | Confidentiality of information in transit | Passed* |

*C1.5 is assessed against the same control as CC6.7 for confidential information transmitted via external-facing channels. The C1.5 finding relates exclusively to external transmissions; the CC6.7 exception relates to internal API transmissions. All external transmissions of confidential data met C1.5 requirements throughout the audit period.

---

## 6. Management Response to CC6.7 Exception

**Prepared by:** Constant Yung, CISO, MedData Nexus Health Systems  
**Date:** February 10, 2026

MedData Nexus acknowledges the CC6.7 exception identified by Clearview Assurance. The `nexus-data-bridge` internal API endpoint was identified during our October 2025 HIPAA Security Rule gap assessment (as documented in COMP-HIPAA-2025-001) and has been remediated.

**Remediation steps completed (as of October 15, 2025):**
- TLS 1.3 enabled on `nexus-data-bridge` service endpoint
- HTTP listener disabled; HTTPS enforced at the load balancer level
- Service mesh (Istio) mTLS policy applied to enforce encrypted pod-to-pod communication for this service
- Penetration test validation completed December 2025 (report: SECTEST-2025-Q4-001)

**Additional actions (in progress):**
- Full inventory of all internal API endpoints to identify any remaining unencrypted transmissions (target completion: March 31, 2026)
- Automated TLS certificate scanning integrated into CI/CD pipeline to prevent future regressions (target: Q2 2026)
- Updated CI/CD policy to reject deployment of services without TLS configuration (target: Q2 2026)

MedData Nexus is committed to maintaining an unqualified Security opinion in the 2026 SOC 2 Type 2 examination. The remediation plan for the CC6.7 TLS 1.3 migration will be completed by Q2 2026, prior to the start of the 2026 audit period.

---

## 7. Auditor Information

**Firm:** Clearview Assurance LLC  
**Practice:** Information Systems Audit and Assurance  
**Engagement Partner:** R. Pemberton, CPA, CISA  
**Audit Period:** January 1 – December 31, 2025  
**Report Issued:** February 14, 2026  
**AICPA Standards:** AT-C Section 205; SOC 2 criteria per AICPA TSC (2017)

---

## 8. Distribution and Use Restrictions

This SOC 2 Type 2 summary is prepared for use by MedData Nexus management and by clients and prospective clients of MedData Nexus who have a need to understand the controls relevant to their use of the MedData Nexus platform. Distribution of this report to any other parties requires written approval from the MedData Nexus CISO.

Recipients of this report are advised that the report covers the specific system boundaries, audit period, and Trust Service Criteria described herein. Recipients should not rely on this report for assessments of systems, periods, or criteria not described.

---

*Classification: Confidential*  
*Document prepared for: MedData Nexus Executive Team, Board Audit Committee, and authorized client distribution*  
*Retained by: MedData Nexus Compliance — minimum 7 years*
