> Synthetic data for Capstone 2 testing only.
> No real patient, customer, credential, contract, or GuidePoint client data.

---

# MedData Nexus Health Systems
## Records Retention and Legal Hold Policy
**Document ID:** LEG-RET-001  
**Version:** 2.2  
**Effective Date:** January 10, 2026  
**Owner:** Legal and Compliance Department  
**Classification:** Internal

---

## 1. Purpose

This policy defines retention, disposal, and legal hold requirements for MedData Nexus business records, including compliance evidence, security assessment records, incident response records, AI system logs, and vendor-risk documentation.

## 2. Retention Schedule

| Record Type | Retention Period | Owner |
|---|---:|---|
| HIPAA policies and procedures | 6 years from creation or last effective date | Compliance |
| Security incident records | 6 years from incident closure | IT Security |
| SOC 2 audit evidence | 7 years | Compliance |
| Vendor risk assessments | Contract term plus 6 years | Vendor Risk Management |
| AI System Inventory entries | System life plus 6 years | AI Governance Committee |
| RAG chatbot query logs | 90 days unless escalated to an investigation | Security Operations |
| AI assessment evidence packages | 3 years or until POA&M closure, whichever is longer | IT Security |
| Legal hold records | Until released by Legal Counsel | Legal |

## 3. Legal Hold

When Legal Counsel issues a legal hold, normal deletion and disposal schedules are suspended for covered records. Employees must preserve documents, emails, logs, tickets, and AI-generated outputs that fall within the hold scope.

## 4. AI-Specific Records

AI system logs must preserve enough information to reconstruct:

- User identity.
- Query or prompt.
- Retrieved source document identifiers.
- Model or API path used.
- Output generated.
- Human reviewer action, when required.
- Final disposition or ticket reference.

AI-generated drafts are not official records unless they are approved, distributed externally, used for a regulatory submission, or attached to an incident, audit, legal, or risk-management workflow.
