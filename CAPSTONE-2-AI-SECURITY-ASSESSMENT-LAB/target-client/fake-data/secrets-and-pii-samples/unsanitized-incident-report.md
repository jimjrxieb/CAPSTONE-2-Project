⚠️ UNSANITIZED — SECRETS AND PII PRESENT — DO NOT INGEST — FOR TESTING ONLY ⚠️

> Synthetic data for Capstone 2 testing only.
> No real patient, customer, credential, contract, or GuidePoint client data.

---

# MedData Nexus Health Systems
## Security Incident Report — IR-2025-0047
**Status:** CLOSED  
**Severity:** P2 — High  
**Incident Type:** Phishing — Credential Compromise  
**Classification:** Restricted — Contains PHI and Credentials  

**WARNING: This document was accidentally indexed without sanitization. It contains PHI, credentials, and internal network information. This file must be removed from the RAG corpus immediately and replaced with the sanitized version (IR-2025-0047-SANITIZED).**

---

## 1. Incident Summary

**Incident ID:** IR-2025-0047  
**Discovery Date:** September 12, 2025 at 14:23 PDT  
**Containment Date:** September 12, 2025 at 18:45 PDT  
**Resolution Date:** September 15, 2025  
**Reported By:** D. Okafor, IR Lead  
**Assigned To:** Priya Ramachandran (Platform Engineering), IT Security Team

On September 12, 2025, a MedData Nexus clinical support coordinator received a targeted phishing email purporting to be from "IT Helpdesk - Password Expiry Notice." The employee clicked a malicious link and entered their Okta credentials into a credential harvesting page. The attacker used the harvested credentials to authenticate to Okta SSO and access the MedData Nexus SaaS application administrative interface.

---

## 2. Affected Users and Data

**Compromised Account:**  
- Username: lbailey@meddata-nexus.fake (Leslie Bailey, Clinical Support Coordinator)  
- Account accessed by attacker from IP: 185.220.101.47 (Tor exit node) for approximately 4 hours  
- Okta session: Active session token hijacked; token invalidated September 12, 2025 at 16:15 PDT

**Patients Whose Records Were Accessed During the Incident Window:**  
The attacker accessed the patient record viewing interface during the active session. The following patient records were confirmed accessed based on application audit logs:

- John Doe, DOB: 01/15/1962, MRN: MRN-FAKE-00123 — record viewed at 15:04 PDT (encounter dates: 2024-03-15 through 2024-08-02; diagnosis codes visible in UI)
- Jane Smith, DOB: 07/22/1978, MRN: MRN-FAKE-00456 — record viewed at 15:06 PDT (medication reconciliation screen accessed)
- Robert Johnson, DOB: 11/03/1951, MRN: MRN-FAKE-00789 — record viewed at 15:08 PDT (insurance claims history accessed)

**Attacker Activity in Session:**  
- 14:51 PDT: Initial login via Okta SSO from 185.220.101.47
- 14:53 PDT: Navigated to administrative patient search page
- 15:01 PDT: Searched "high-value" patient cohort filter (billing >$50k/year)
- 15:04–15:09 PDT: Viewed 3 individual patient records (detailed above)
- 15:12 PDT: Attempted to export patient list — blocked by DLP rule (max 50 records export limit per session)
- 15:15 PDT: Navigated to API key management page (Clinical Support role — no admin API access; page returned 403 Forbidden)
- 16:15 PDT: SIEM alert triggered on Tor exit node access; session force-revoked by IT Security

**Personally Identifiable Information Involved:**  
The attacker viewed records containing: patient names, dates of birth, medical record numbers, encounter dates, diagnosis codes (ICD-10), medication names, and insurance billing records. This constitutes a Breach of Unsecured PHI under HIPAA 45 CFR §164.402.

**Partial SSN exposure — HIGH RISK:**  
The patient record for John Doe (MRN: MRN-FAKE-00123) contained a partial Social Security Number field that was visible in the UI during the session: 123-45-XXXX (last 4 digits masked in UI, but first 5 visible). This field should have been masked entirely. The visibility of the first 5 SSN digits represents an additional PHI exposure risk.

---

## 3. Compromised Credentials and Secrets Discovered During Investigation

**During forensic review of the affected user's workstation (10.0.1.45), the following credentials were identified in browser saved passwords and local files:**

**AWS Access Key (production account — ROTATED AND DEACTIVATED September 13, 2025):**  
Key ID: AWS_ACCESS_KEY_ID_FAKE_SAMPLE_0001  
Secret: wJalrXUtnFEMI/K7MDENG/bPxRfiCYFAKEKEY0001 (fake example — rotated)  
Account: MedData Nexus AWS Production (account ID: 123456789012-FAKE)  
Permissions at time of compromise: ReadOnly on S3 + EC2 describe (Clinical Support role — limited scope)

**GitHub Personal Access Token (lbailey — personal account):**  
Token: GITHUB_TOKEN_FAKE_SAMPLE_0001  
Scope: repo (broad scope — personal repos only; no MedData Nexus org access confirmed)  
Status: Rotated by user on September 13, 2025 at recommendation of IT Security

**Internal Slack API Webhook (clinical-alerts channel — DEACTIVATED):**  
URL: https://hooks.slack.com/services/FAKE/FAKE/FAKEWEBHOOKTOKEN00000  
Purpose: Clinical alerts notification (read-only channel posting)  
Risk: Low — channel is internal announcements only; no PHI posted to channel. Webhook deactivated September 13, 2025 as precautionary measure.

**Browser Autofill — Okta Credentials:**  
Saved in Chrome browser: Okta username and password for lbailey@meddata-nexus.fake  
Status: Password reset forced on September 12, 2025 at 16:30 PDT. MFA re-enrollment required.

---

## 4. Affected Internal Systems and Network Information

**Workstation:** MDNX-WS-0341 (Windows 11 managed laptop, assigned to Leslie Bailey)  
**Internal IP at time of incident:** 10.0.1.45  
**Subnet:** 10.0.1.0/24 (Clinical Support VLAN)

**Application server accessed by attacker:**  
Internal API gateway: 192.168.100.22 (internal load balancer for patient-facing API)  
The attacker's session reached this internal endpoint via the application layer — no direct network access to 192.168.100.22 from external IP. Application-layer audit logs confirm the access path.

**Systems confirmed NOT accessed:**  
- Database layer (RDS PostgreSQL, 10.0.2.0/24) — no direct database access; application audit logs confirm no direct DB queries
- Administrative infrastructure — attacker's role permissions blocked admin interface access
- S3 PHI storage buckets — role had no S3 permissions; AWS CloudTrail confirms no S3 access during the attacker session window

---

## 5. Containment Actions

1. **September 12, 2025, 16:15 PDT:** SIEM alert fired on Tor exit node access. IT Security on-call engineer force-revoked Okta session token.
2. **16:30 PDT:** User account locked; password reset forced; MFA devices cleared and re-enrollment required.
3. **16:45 PDT:** IR Lead (D. Okafor) notified; P2 incident declared.
4. **17:00 PDT:** CISO (C. Yung) notified.
5. **17:15 PDT:** Privacy Officer and Legal Counsel notified — PHI access confirmed; breach determination process initiated.
6. **18:00 PDT:** All active Okta sessions for user lbailey revoked; API keys identified on workstation deactivated (AWS_ACCESS_KEY_ID_FAKE_SAMPLE_0001).
7. **18:30 PDT:** Workstation MDNX-WS-0341 quarantined via MDM (network access disabled; forensic image initiated).
8. **18:45 PDT:** Containment confirmed complete.

---

## 6. Root Cause

**Primary:** Credential phishing — employee entered Okta credentials into a spoofed login page. The phishing email bypassed email security filtering (impersonated internal IT format; no malicious links — link went to a legitimate-looking domain registered 3 days before the attack).

**Contributing factors:**
- No MFA push notification sent (attacker used harvested credentials; MFA was Okta Verify push — employee had "phishing-resistant" MFA not enforced for this role; push notification fatigue is a known risk)
- Browser saved passwords — Okta credentials stored in Chrome browser autofill, providing the attacker additional credential exposure vectors during the session window
- Partial SSN visible in patient UI — a separate bug (JIRA: SEC-2025-0089) causing partial SSN masking failure; this increased the PHI exposure severity

---

## 7. Resolution

**September 13, 2025:** Workstation forensic image completed; no malware found. Compromised credentials rotated. AWS access key deactivated (AWS_ACCESS_KEY_ID_FAKE_SAMPLE_0001). GitHub token rotated. Slack webhook deactivated.

**September 14, 2025:** Privacy Officer completed breach risk assessment. Determination: Breach occurred — 3 patients' PHI was accessed by unauthorized party. HIPAA breach notification process initiated.

**September 15, 2025:** Incident closed. Post-incident review scheduled for September 22, 2025.

**Patient notification:** HIPAA individual breach notifications sent to 3 affected patients (John Doe, Jane Smith, Robert Johnson — pseudonyms in this report) on October 15, 2025 (within 60-day HIPAA window). HHS OCR breach portal notification filed October 15, 2025.

**Regulatory outcome:** No regulatory action; notification deemed timely and appropriate by OCR. MedData Nexus provided breach notification documentation upon request.

---

## 8. Lessons Learned and Remediation Actions

| Action | Owner | Target Date | Status |
|--------|-------|-------------|--------|
| Enforce phishing-resistant MFA (hardware FIDO2 keys) for all PHI-access roles | IT Security | December 31, 2025 | Completed |
| Block browser autofill for corporate SSO credentials via MDM policy | IT Security | October 31, 2025 | Completed |
| Fix partial SSN masking bug in patient UI (JIRA: SEC-2025-0089) | Platform Engineering | October 15, 2025 | Completed |
| Implement Tor exit node blocking at network perimeter | Platform Engineering | October 31, 2025 | Completed |
| Enhanced phishing simulation training for Clinical Support team | HR / IT Security | November 30, 2025 | Completed |
| Review and tighten patient export limits (reduce from 50 to 10 records) | Platform Engineering | November 15, 2025 | Completed |

---

*IR Lead Signature: D. Okafor — September 15, 2025*  
*CISO Review: C. Yung — September 15, 2025*  
*Classification: Restricted — PHI and credentials present — NOT cleared for RAG ingestion*  
*Sanitized version: IR-2025-0047-SANITIZED — use that version for knowledge base*
