> Synthetic data for Capstone 2 testing only.
> No real patient, customer, credential, contract, or GuidePoint client data.

---

# MedData Nexus Health Systems
## Vendor Security Assessment — NovaMind AI Platform
**Document ID:** VR-NOVAMIND-2025-001
**Assessment Date:** October 14, 2025
**Completed By:** NovaMind AI Inc. — Security Team
**Reviewed By:** MedData Nexus Vendor Risk Management
**Classification:** Confidential
**Distribution:** CISO, Vendor Risk Management, Legal Counsel

---

## Vendor Profile

| Field | Value |
|---|---|
| Vendor Name | NovaMind AI Inc. |
| Product | NovaMind Enterprise AI Platform v3.2 |
| Primary Contact | NovaMind Security Team (security@novamind-ai.fake) |
| Deployment Model | SaaS (AWS us-east-1, us-west-2) |
| Intended Use at MedData Nexus | Internal document summarization and policy drafting assistance |
| Data Classification Authorized | Internal (Tier 2) and Confidential (Tier 3) — PHI/Restricted data NOT authorized |
| Contract Status | Active — MSA signed 2024-08-01, renewal 2026-07-31 |
| BAA Status | **Executed — 2024-08-01** |
| Approval Status | **Approved — Low Risk** |

---

## Section 1 — Security Program

**Q1.1: Does NovaMind maintain a formal information security program?**
Yes. NovaMind maintains an ISO 27001-certified information security management system (ISMS). Certificate number: CERT-FAKE-ISO-27001-NM-2024. Last audit: August 2025. Next audit: August 2026.

**Q1.2: Does NovaMind have a named CISO or equivalent?**
Yes. VP of Security and Compliance (name withheld per vendor privacy policy). Contact routed through security@novamind-ai.fake.

**Q1.3: Has NovaMind experienced a security incident affecting customer data in the past 24 months?**
One incident in Q3 2024: a misconfigured S3 bucket in a staging environment was briefly publicly accessible. No production customer data was involved. Incident closed within 4 hours of detection. Root cause: IaC change review gap. Remediation: mandatory Checkov scan added to all IaC PRs. No breach notification required.

---

## Section 2 — Compliance and Certifications

| Certification | Status | Notes |
|---|---|---|
| SOC 2 Type 2 | **Current** — issued September 2025 | Covers Security, Availability, Confidentiality. Report available under NDA. |
| ISO 27001 | **Current** — certified August 2025 | |
| HIPAA Business Associate | **BAA executed** — 2024-08-01 | MedData Nexus is a covered entity; BAA on file with Legal Counsel |
| GDPR Data Processing Agreement | **DPA executed** — 2025-01-15 | Covers EU data subjects if any |
| FedRAMP | Not applicable — no federal authorization | NovaMind does not serve federal clients |

---

## Section 3 — Data Handling

**Q3.1: What data does NovaMind store from customer queries?**
Query text and model responses are retained for 30 days for quality and safety review, then permanently deleted. No long-term training on customer data without explicit opt-in contract addendum. MedData Nexus has not opted in to training data use.

**Q3.2: Is customer data used to train NovaMind's foundation models?**
No. Customer data is not used for model training by default. Training data use requires a separate signed addendum. MedData Nexus has not signed a training data addendum.

**Q3.3: Where is data processed and stored?**
AWS us-east-1 and us-west-2 only. No EU data processing for MedData Nexus tenant. Data residency confirmed by tenant configuration.

**Q3.4: Does NovaMind process PHI on behalf of MedData Nexus?**
NovaMind is not authorized to process PHI for MedData Nexus. The BAA covers the possibility but MedData Nexus policy restricts the internal AI assistant to Internal and Confidential data only. If MedData Nexus submits PHI, it would be a customer policy violation, not a NovaMind configuration issue.

---

## Section 4 — Encryption

| Control | Implementation |
|---|---|
| Data in transit | TLS 1.3 enforced on all API endpoints. TLS 1.2 minimum where legacy clients require it. |
| Data at rest | AES-256 for all stored query data and model artifacts |
| Key management | AWS KMS with customer-managed keys (CMK) available at additional cost. MedData Nexus uses NovaMind-managed keys (default). |
| Backup encryption | AES-256; backup keys rotated annually |

---

## Section 5 — Access Control

**Q5.1: How does NovaMind control employee access to customer data?**
Access to customer tenant data requires approval from the Security team and is logged. Break-glass access requires dual approval. All access is time-limited (4 hours maximum per session) and logged to an immutable audit trail.

**Q5.2: Does NovaMind enforce MFA for internal systems?**
Yes. Hardware MFA (YubiKey) required for all production system access. TOTP required for corporate systems.

**Q5.3: How is MedData Nexus tenant data isolated from other tenants?**
Separate AWS accounts per tenant (account-per-tenant model). No shared compute between tenants.

---

## Section 6 — Incident Response

**Q6.1: What is NovaMind's breach notification SLA to customers?**
72 hours for confirmed breach notification to customers, regardless of breach size. This exceeds HIPAA requirements and matches the BAA Article 5 obligation.

**Q6.2: Does NovaMind have a documented incident response plan?**
Yes. IRP reviewed annually. Last tabletop exercise: September 2025. NovaMind will provide IRP summary on request under NDA.

---

## Section 7 — Subprocessors

| Subprocessor | Purpose | Region | Controls |
|---|---|---|---|
| AWS (Amazon Web Services) | Infrastructure hosting | us-east-1, us-west-2 | AWS SOC 2, ISO 27001 — shared responsibility model |
| Datadog (metrics/logging) | Operational monitoring | us-east-1 | No customer query content; infrastructure metrics only |
| PagerDuty | On-call alerting | us-east-1 | No customer data transmitted |

No AI subprocessors. NovaMind operates its own foundation model inference infrastructure.

---

## Section 8 — Vulnerability Management

**Q8.1: How frequently does NovaMind conduct vulnerability scanning?**
Continuous scanning with Snyk (code/dependencies) and Tenable Nessus (infrastructure). Critical findings patched within 7 days. High findings within 30 days.

**Q8.2: Does NovaMind conduct penetration testing?**
Annual third-party penetration test. Last test: July 2025 by SecureStack Consulting (fictitious). No critical findings. Two high findings remediated within 30 days. Report available under NDA.

---

## MedData Nexus Vendor Risk Decision

| Field | Value |
|---|---|
| Risk Tier | **Low** |
| Approval Status | **Approved** |
| Data Classification Authorized | Internal (Tier 2) and Confidential (Tier 3) |
| PHI Authorized | No — requires separate CISO authorization and BAA addendum |
| Approval Date | 2025-10-28 |
| Approved By | Vendor Risk Management + Constant Yung, CISO |
| Next Review | 2026-10-01 |
| Conditions | (1) Annual re-review required. (2) PHI prohibition enforced by MedData policy, not NovaMind controls. (3) Notify Vendor Risk Management if NovaMind changes subprocessors or data residency. |

---

*Classification: Confidential*
*Distribution: CISO, Vendor Risk Management, Legal Counsel*
*Do not distribute externally without VP approval and signed NDA*
