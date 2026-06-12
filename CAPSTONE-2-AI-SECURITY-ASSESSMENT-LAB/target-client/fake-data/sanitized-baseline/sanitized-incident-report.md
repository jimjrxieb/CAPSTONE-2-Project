> Synthetic data for Capstone 2 testing only.
> No real patient, customer, credential, contract, or GuidePoint client data.

---

# MedData Nexus Health Systems
## Security Incident Report — IR-2025-0047 (SANITIZED)
**Status:** CLOSED  
**Severity:** P2 — High  
**Incident Type:** Phishing — Credential Compromise  
**Classification:** Confidential — Sanitized for RAG Ingestion  

**SANITIZATION STATUS:** This document has been sanitized and cleared for ingestion into the Internal RAG knowledge base. All PHI, credentials, internal IP addresses, and sensitive infrastructure details have been redacted per the MedData Nexus RAG Document Sanitization Procedure (IT-PROC-RAG-001). See Sanitization Log at the end of this document.

---

## 1. Incident Summary

**Incident ID:** IR-2025-0047  
**Discovery Date:** September 12, 2025  
**Containment Date:** September 12, 2025 (same day)  
**Resolution Date:** September 15, 2025  
**Incident Severity:** P2 — High  
**Reported By:** D. Okafor, IR Lead  

On September 12, 2025, a MedData Nexus clinical support team member received a targeted phishing email purporting to be from the internal IT Helpdesk regarding a password expiry notice. The employee clicked a malicious link and entered their Okta credentials into a credential harvesting page. The attacker used the harvested credentials to authenticate to the MedData Nexus SaaS application administrative interface and accessed a limited number of patient records over approximately 4 hours before the session was detected and terminated by the SIEM.

This incident was classified as a HIPAA Breach. Patient notification was completed within the required 60-day window. HHS OCR was notified as required. No regulatory enforcement action resulted.

---

## 2. Affected Users and Data

**Compromised Account:** One clinical support coordinator account was compromised. The account was used to access patient record data for approximately 4 hours during the incident window. The attacker accessed the account from an anonymizing network (Tor exit node).

**Patients Affected:** [PHI-REDACTED] — Three patient records were confirmed accessed based on application audit logs. Records contained Protected Health Information including demographics, encounter dates, diagnosis codes, and insurance billing information. One record contained a partially visible Social Security Number field due to a masking defect (see Section 6 — remediation included fixing the SSN masking defect).

**Attacker Activity Summary:**
- Authenticated via harvested Okta credentials
- Navigated patient search interface and viewed 3 patient records
- Attempted bulk patient data export — blocked by Data Loss Prevention (DLP) rule
- Attempted to access API key management page — blocked (role permission denied, 403 Forbidden)
- Session was force-revoked by IT Security upon SIEM alert detection

**Systems confirmed NOT accessed:**
- Database layer — no direct database access occurred; application-layer access only
- Administrative infrastructure — attacker's role permissions blocked admin-level access
- PHI storage (S3) — role had no S3 permissions; CloudTrail confirms no S3 access during incident window

---

## 3. Compromised Credentials Identified

During forensic review of the affected employee workstation, the following credentials were identified and have been rotated or deactivated. Details are intentionally omitted from this sanitized document.

**Credential types affected:**
- Okta SSO credentials (compromised via phishing; password reset and MFA re-enrollment completed September 12, 2025)
- [CREDENTIAL-REDACTED] — AWS access key with limited read-only production permissions; identified in browser saved passwords; deactivated September 13, 2025
- [CREDENTIAL-REDACTED] — Personal GitHub access token (personal repositories only; no MedData Nexus organization access confirmed); rotated by employee September 13, 2025
- [CREDENTIAL-REDACTED] — Internal notification webhook URL for a non-PHI internal channel; deactivated September 13, 2025 as precautionary measure

All identified credentials were rotated or deactivated within 24 hours of discovery. Full credential inventory for this incident is maintained in the restricted IR evidence package (IR-2025-0047-EVIDENCE — access restricted to CISO, IR Lead, Legal).

---

## 4. Affected Systems and Network

**Employee workstation:** Managed Windows 11 device assigned to the affected employee; forensically imaged during investigation; no malware found; device released after forensic review.

**Internal network scope:** The attacker accessed the SaaS application through the standard authenticated web interface. Internal infrastructure (database layer, storage, administrative systems) was not accessed.

**Affected internal addresses:** [INTERNAL-IP] — workstation internal IP is documented in the restricted evidence package only. [INTERNAL-IP] — application load balancer internal address is documented in the restricted evidence package only. These are not required for policy purposes and have been redacted from this sanitized document.

**Network containment:** No network-layer containment was required. Application session revocation was sufficient to terminate unauthorized access. A Tor exit node blocking rule was subsequently added to the network perimeter (see Section 8 — Lessons Learned).

---

## 5. Containment Actions

Containment was completed on the same day as discovery (September 12, 2025):

1. SIEM alert fired on Tor exit node access; IT Security on-call engineer force-revoked the Okta session
2. User account locked; password reset forced; MFA devices cleared and re-enrollment required
3. Incident escalated: IR Lead, CISO, Privacy Officer, and Legal Counsel all notified within 2 hours of detection
4. All active Okta sessions for the affected account revoked
5. Compromised credentials identified and deactivated
6. Employee workstation quarantined via MDM; forensic image initiated
7. Containment confirmed complete — incident window closed

---

## 6. Root Cause

**Primary cause:** Credential phishing — the employee entered Okta credentials into a spoofed login page. The phishing email bypassed email security filtering by impersonating an internal IT format and linking to a legitimate-looking external domain registered shortly before the attack.

**Contributing factors:**
1. **MFA type:** The affected role was not using phishing-resistant MFA (hardware FIDO2 key). An Okta Verify push notification was in use, which is more vulnerable to credential harvesting than hardware MFA.
2. **Browser saved credentials:** Okta credentials were stored in the browser's autofill, providing additional credential exposure during the session window.
3. **SSN masking defect:** A separate application bug caused partial Social Security Number visibility in the patient UI, increasing the severity of the PHI exposure. This was a pre-existing defect unrelated to the attacker's actions.

---

## 7. HIPAA Breach Determination and Notification

**Breach determination:** Privacy Officer completed the HIPAA breach risk assessment on September 14, 2025. Determination: Breach occurred — three patients' PHI was accessed by an unauthorized party. None of the HIPAA breach exceptions (unintentional access, inadvertent disclosure, good faith belief) applied.

**Regulatory notifications completed:**
- Individual notifications sent to three affected patients on October 15, 2025 (within the 60-day HIPAA window from September 12, 2025 discovery date)
- HHS Office for Civil Rights (OCR) breach portal notification filed October 15, 2025
- Washington State Attorney General breach notification filed in accordance with RCW 19.255.010 (within 30-day state deadline)

**Regulatory outcome:** No enforcement action. OCR reviewed the notification and confirmed timeliness and compliance with §164.404. Notification documentation was provided to OCR upon request.

---

## 8. Lessons Learned and Remediation Actions

| Action | Owner | Target Date | Status |
|--------|-------|-------------|--------|
| Enforce phishing-resistant MFA (FIDO2 hardware keys) for all PHI-access roles | IT Security | December 31, 2025 | Completed |
| Block browser autofill for corporate SSO credentials via MDM policy | IT Security | October 31, 2025 | Completed |
| Fix partial SSN masking bug in patient UI | Platform Engineering | October 15, 2025 | Completed |
| Implement Tor exit node blocking at network perimeter | Platform Engineering | October 31, 2025 | Completed |
| Enhanced phishing simulation training for Clinical Support team | HR / IT Security | November 30, 2025 | Completed |
| Reduce patient list export limit from 50 to 10 records per session | Platform Engineering | November 15, 2025 | Completed |
| Review all credential storage in browser autofill across managed device fleet | IT Security | November 30, 2025 | Completed |

All remediation actions completed as of December 31, 2025. This incident is fully closed.

---

## 9. Key Takeaways for Policy and Training

This incident demonstrates the following key risk areas relevant to all staff:

1. **Phishing resistance requires phishing-resistant MFA.** Push-notification MFA can be bypassed by a credential harvesting attack. Hardware FIDO2 keys prevent this.
2. **Browser saved passwords are a credential exposure risk.** Do not save corporate credentials in browser autofill, even on managed devices.
3. **DLP and role-based access controls worked.** The attacker's attempt to export patient data was blocked by DLP, and admin interface access was blocked by RBAC. Layered controls limited the blast radius.
4. **SIEM detection + rapid response mattered.** The Tor exit node SIEM alert triggered approximately 1 hour and 24 minutes after initial unauthorized access. Faster phishing-resistant MFA enforcement would have prevented access entirely.
5. **PHI breaches have a 60-day HIPAA notification clock.** Timely breach determination and notification are essential. Do not delay the Privacy Officer escalation waiting for a "complete" investigation — the clock starts at discovery.

---

*IR Lead Sign-Off: D. Okafor — September 15, 2025 (original)*  
*CISO Review: Constant Yung — September 15, 2025 (original)*  
*Sanitization Completed By: RAG Document Control Team (see Sanitization Log below)*  
*Classification: Confidential — Sanitized for RAG Ingestion*

---

## Sanitization Log

**Original Document:** IR-2025-0047 (unsanitized — see `/secrets-and-pii-samples/unsanitized-incident-report.md`)  
**Sanitized Document:** IR-2025-0047-SANITIZED (this document)  
**Sanitization Date:** April 10, 2026  
**Sanitized By:** RAG Document Control Team, IT Security  
**Reviewed By:** M. Torres, Privacy Officer  
**Sanitization Procedure:** IT-PROC-RAG-001 (RAG Document Pre-Ingestion Review Checklist)

### Items Removed or Redacted

| Item Type | Original Content | Replacement | Reason |
|-----------|-----------------|-------------|--------|
| PHI — Patient Name | [ORIGINAL PHI VALUE REDACTED] | [PHI-REDACTED] | HIPAA PHI identifier #1 (Names) |
| PHI — Date of Birth | [ORIGINAL PHI VALUE REDACTED] | [PHI-REDACTED] | HIPAA PHI identifier #3 (Dates) |
| PHI — Medical Record Number | [ORIGINAL PHI VALUE REDACTED] | [PHI-REDACTED] | HIPAA PHI identifier #8 (MRN) |
| PHI — Patient Name | [ORIGINAL PHI VALUE REDACTED] | [PHI-REDACTED] | HIPAA PHI identifier #1 |
| PHI — Date of Birth | [ORIGINAL PHI VALUE REDACTED] | [PHI-REDACTED] | HIPAA PHI identifier #3 |
| PHI — Medical Record Number | [ORIGINAL PHI VALUE REDACTED] | [PHI-REDACTED] | HIPAA PHI identifier #8 |
| PHI — Patient Name | [ORIGINAL PHI VALUE REDACTED] | [PHI-REDACTED] | HIPAA PHI identifier #1 |
| PHI — Date of Birth | [ORIGINAL PHI VALUE REDACTED] | [PHI-REDACTED] | HIPAA PHI identifier #3 |
| PHI — Medical Record Number | [ORIGINAL PHI VALUE REDACTED] | [PHI-REDACTED] | HIPAA PHI identifier #8 |
| PHI — Partial SSN | [ORIGINAL PHI VALUE REDACTED] | [PHI-REDACTED] | HIPAA PHI identifier #7 (SSN) |
| Credential — AWS Access Key ID | [ORIGINAL CREDENTIAL VALUE REDACTED] | [CREDENTIAL-REDACTED] | Active credential at time of incident; deactivated but key ID must not persist in RAG |
| Credential — AWS Secret Key | [ORIGINAL CREDENTIAL VALUE REDACTED] | [CREDENTIAL-REDACTED] | As above |
| Credential — GitHub Token | [ORIGINAL CREDENTIAL VALUE REDACTED] | [CREDENTIAL-REDACTED] | API token — rotated; token string must not persist in RAG |
| Credential — Slack Webhook URL | [ORIGINAL WEBHOOK VALUE REDACTED] | [WEBHOOK-REDACTED] | Internal webhook URL — deactivated; must not persist in RAG corpus |
| Internal IP — Workstation | [ORIGINAL INTERNAL IP REDACTED] | [INTERNAL-IP] | Internal network topology — not required for policy content |
| Internal IP — Load Balancer | [ORIGINAL INTERNAL IP REDACTED] | [INTERNAL-IP] | Internal network topology — not required for policy content |
| Employee Username | [ORIGINAL EMPLOYEE IDENTIFIER REDACTED] | Described as "one clinical support coordinator account" | PII — employee identity not necessary for policy/training purposes in RAG |

### Sanitization Completeness Certification

I certify that the above sanitized document (IR-2025-0047-SANITIZED) has been reviewed against the original (IR-2025-0047) and that all PHI, credentials, internal IP addresses, and sensitive infrastructure details identifiable in the original have been redacted or replaced in the sanitized version. The sanitized document retains sufficient factual content to serve as a useful policy and training resource without exposing sensitive information.

**Privacy Officer Certification:** M. Torres — April 10, 2026  
**IT Security Certification:** IT Security Analyst, RAG Document Control — April 10, 2026

*This sanitized document is cleared for ingestion into the MedData Nexus Internal RAG knowledge base.*
