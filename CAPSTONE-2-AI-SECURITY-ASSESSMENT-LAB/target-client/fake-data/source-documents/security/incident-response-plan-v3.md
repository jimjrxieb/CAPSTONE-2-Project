> Synthetic data for Capstone 2 testing only.
> No real patient, customer, credential, contract, or GuidePoint client data.

---

# MedData Nexus Health Systems
## Incident Response Plan
**Document ID:** IRP-001  
**Version:** 3.0  
**Effective Date:** February 1, 2026  
**Owner:** Chief Information Security Officer  
**Classification:** Confidential  
**Review Cycle:** Annual and after every P1/P2 incident

---

## 1. Purpose and Scope

This Incident Response Plan (IRP) defines the structured process MedData Nexus Health Systems follows to detect, respond to, contain, and recover from information security incidents. It applies to all information systems, data, and personnel within the MedData Nexus environment, including cloud infrastructure, on-premises systems, third-party integrations, and AI/ML systems.

The plan follows the PICERL framework: Preparation, Identification, Containment, Eradication, Recovery, and Lessons Learned. This structure aligns with NIST SP 800-61r2 (Computer Security Incident Handling Guide) and applicable HIPAA breach notification requirements (45 CFR §164.400 – §164.414).

This is version 3 of the IRP. Changes from v2 include: addition of the AI/ML Incident Playbook (Section 7), updated regulatory notification timelines to reflect state law changes, and updated IR team roster.

---

## 2. Incident Response Team

### 2.1 Core IR Team

| Role | Name | Contact | Responsibilities |
|------|------|---------|-----------------|
| **CISO / IR Executive Sponsor** | Constant Yung | ciso@meddata-nexus.fake / (206) 555-0147 | Final authority on severity classification, external notifications, public statements |
| **IR Lead** | Darnell Okafor | dokafor@meddata-nexus.fake / (206) 555-0212 | Incident coordination, timeline management, stakeholder updates, after-action reports |
| **Platform Engineering Lead** | Priya Ramachandran | pramachandran@meddata-nexus.fake / (206) 555-0318 | Technical containment, forensic preservation, system recovery |
| **Legal Counsel (Privacy)** | Simone Beaumont | sbeaumont@meddata-nexus.fake / (206) 555-0455 | HIPAA breach determination, regulatory notification decisions, litigation hold |
| **Compliance Director** | M. Torres | mtorres@meddata-nexus.fake / (206) 555-0533 | Compliance obligations, evidence packaging, audit trail |
| **Communications Lead** | Kevin Hargrave | khargrave@meddata-nexus.fake / (206) 555-0629 | Internal communications, client notifications (post-legal review), media (if applicable) |
| **HR Business Partner** | Andrea Wills | awills@meddata-nexus.fake / (206) 555-0704 | Workforce-related incidents (insider threat, social engineering), disciplinary process |

### 2.2 On-Call Escalation

Security incidents outside business hours are initially triaged by the on-call DevSecOps engineer (rotating schedule published in PagerDuty). The on-call engineer has authority to initiate containment actions up to P2 severity without pre-approval. P1 incidents require CISO notification within 1 hour regardless of time of day.

**PagerDuty escalation policy:**
1. On-call DevSecOps Engineer (immediate)
2. Platform Engineering Lead (15 minutes if no acknowledgment)
3. IR Lead (30 minutes if no acknowledgment)
4. CISO (1 hour if no acknowledgment)

### 2.3 External Contacts

| Contact | Organization | Use Case |
|---------|-------------|---------|
| FBI Cyber Division | FBI Seattle Field Office | Ransomware, nation-state threats, wire fraud |
| HHS Office for Civil Rights | OCR Breach Portal | HIPAA breach notification |
| Washington State AG | WA Attorney General | State breach notification |
| Incident Response Retainer | CyberForge IR LLC (fictional) | External IR support for P1 incidents |
| Cyber Insurance | Hartford Cyber (fictional) | All P1 incidents, ransomware, extortion |

---

## 3. Severity Classification

| Severity | Label | Definition | Example | Initial Response SLA |
|----------|-------|-----------|---------|---------------------|
| P1 | Critical | Active breach, ransomware, confirmed PHI exposure, AI system compromise | Ransomware on production; confirmed PHI exfiltration; AI system outputting unretrieved PHI | CISO notification: 1 hour; IR team assembled: 2 hours |
| P2 | High | Potential breach under investigation, significant system compromise, suspected insider threat | Suspicious admin access to PHI database; anomalous AI chatbot behavior; credential theft suspected | IR Lead notification: 2 hours; initial containment: 4 hours |
| P3 | Medium | Isolated system compromise, policy violation, failed attack | Single workstation malware (isolated); failed phishing attempt with no payload delivery; policy violation | IT Security notification: 4 hours; investigation: 24 hours |
| P4 | Low | Minor policy deviation, spam, no-harm-done events | Employee using unapproved AI tool with non-sensitive data; excessive failed login attempts | Ticket created: 24 hours; investigation: 72 hours |

---

## 4. PICERL Response Framework

### Phase 1: Preparation

**Objective:** Ensure MedData Nexus is ready to respond before an incident occurs.

**Standing preparation activities:**
- IR team roster maintained and tested quarterly (tabletop exercise minimum once per year)
- Incident response retainer (CyberForge IR LLC) active with signed SOW
- Forensic tooling deployed on all production hosts (Velociraptor agent — passive collection)
- Evidence preservation guides distributed to IR team and stored in team wiki
- SIEM alerting rules reviewed quarterly; alert fatigue review performed semi-annually
- Playbooks (including AI/ML playbook, Section 7) reviewed after each P1/P2 incident and annually
- Legal hold procedures reviewed with Legal Counsel annually
- Contact lists verified quarterly; on-call rotation tested monthly
- Cyber insurance policy reviewed annually; coverage confirmed for ransomware, regulatory penalties, and forensic costs

---

### Phase 2: Identification

**Objective:** Detect and confirm that a security incident has occurred.

**Detection sources:**
- SIEM alerts (Sumo Logic) — primary detection source for automated threats
- User reports via ServiceNow Security Incident ticket or security@meddata-nexus.fake
- Vendor notification (third-party breach affecting MedData Nexus data)
- Threat intelligence feeds (subscribed via CISA AIS, FS-ISAC)
- External reporting (HackerOne responsible disclosure program, law enforcement)

**Identification steps:**
1. Receiving party creates ServiceNow Security Incident ticket within 30 minutes of awareness
2. On-call engineer performs initial triage: confirm event is an incident (not a false positive), assess severity per Section 3
3. If P1 or P2: immediately notify IR Lead and CISO; activate communication tree
4. If P3 or P4: continue investigation; escalate if severity changes
5. Document all findings, timestamps, and actions in the incident ticket from this point forward
6. Do not share incident details outside the IR team without Legal Counsel approval until breach determination is made

**Initial evidence collection (Identification phase):**
- Export SIEM logs for the relevant time window (minimum: 72 hours before detection)
- Capture current system state (memory, running processes, network connections) before any changes
- Note all systems potentially in scope and document their current status
- Preserve authentication logs from Okta for any accounts potentially involved

---

### Phase 3: Containment

**Objective:** Stop the spread of the incident and limit further damage.

**Short-term containment (immediate, within 2 hours for P1):**
- Isolate affected systems from the network using AWS Security Group rules (do not power off — preserve forensic state)
- Revoke or rotate compromised credentials via Okta and AWS IAM
- Block identified malicious IPs or domains at the network perimeter
- For AI system incidents: disable the affected AI endpoint at the API gateway level
- Preserve disk snapshots of affected EC2 instances (EBS snapshot) before any remediation

**Long-term containment (within 24 hours for P1, 72 hours for P2):**
- Deploy patched or clean replacement systems in isolation
- Verify clean backup availability for recovery planning
- Confirm scope of compromise — are additional systems affected?
- Brief executive stakeholders on containment status
- Legal Counsel begins breach determination analysis

**Evidence preservation requirements:**
- All containment actions must be documented with exact commands, timestamps, and the name of the engineer who executed them
- Do not delete any logs, modify evidence, or patch/update systems before forensic imaging is complete
- Chain of custody document initiated at this phase (template: IR-CHAIN-OF-CUSTODY-TPL-001)
- Forensic imaging performed by Platform Engineering Lead or CyberForge IR (if P1 retainer activated)

---

### Phase 4: Eradication

**Objective:** Remove the threat actor, malware, or vulnerability that caused the incident.

**Eradication activities:**
- Root cause analysis: identify how the attacker gained access, what vulnerability or misconfiguration was exploited
- Remove malware, backdoors, or unauthorized access paths identified during forensic analysis
- Patch or mitigate the exploited vulnerability across all affected and potentially affected systems
- Reset all credentials that may have been exposed or used by the attacker
- Review adjacent systems: did the attacker attempt lateral movement? Are other systems at risk?
- Validate eradication: run clean vulnerability scan and behavioral analysis on restored environment

**For credential compromise:**
- All potentially compromised credentials must be rotated; do not attempt to preserve any possibly-exposed secret
- AWS IAM roles and policies reviewed for any changes made during the incident window
- Okta session revocation for all affected accounts; MFA re-enrollment required

---

### Phase 5: Recovery

**Objective:** Restore systems to normal operations safely.

**Recovery steps:**
1. Restore from verified clean backup or deploy freshly provisioned infrastructure (prefer clean deploy over backup restoration for compromised systems)
2. Verify integrity of restored data against known-good checksums
3. Monitor restored systems intensively for 72 hours post-recovery (elevated SIEM alerting)
4. Gradually restore full functionality (phased return to production)
5. Communicate recovery status to internal stakeholders; prepare client communication if applicable (Legal review required)
6. Verify that all gaps identified in the incident are closed before declaring incident resolved

**Return-to-production gate:**
- Platform Engineering Lead signs off on technical recovery
- IR Lead confirms incident scope is fully addressed
- Legal Counsel confirms no outstanding regulatory obligations require delay
- CISO approves incident closure

---

### Phase 6: Lessons Learned

**Objective:** Document what happened, what worked, what failed, and how to prevent recurrence.

**After-action requirements:**
- Lessons Learned report completed within 14 days of incident closure for P1/P2; 30 days for P3/P4
- Report must include: incident timeline, root cause, affected systems, containment effectiveness, recovery time, regulatory impact, and specific improvement actions with owners and dates
- Report reviewed by CISO, IR Lead, and Legal Counsel before distribution
- Improvement actions tracked in the risk register with quarterly status reviews
- Tabletop exercise incorporating lessons learned conducted within 6 months of any P1 incident
- IRP updated if lessons learned identify gaps in the plan

---

## 5. Communication Tree

### Internal Communications

| Event | Recipients | Channel | Timing |
|-------|-----------|---------|--------|
| P1 incident declared | CISO, IR Lead, Legal, Compliance, CTO, CFO | Phone + encrypted Slack | Within 1 hour |
| P2 incident declared | CISO, IR Lead, Legal, Compliance | Phone + encrypted Slack | Within 2 hours |
| PHI breach suspected | Legal Counsel + CISO simultaneously | Phone only (no email) | Immediately upon suspicion |
| Incident status updates (P1/P2) | All core IR team | Encrypted Slack #incident-response | Every 2 hours while active |
| Incident resolved | Executive team, all IR team | Email + Slack | Within 2 hours of closure |

### External Communications

**No external communication about an incident may be made without explicit Legal Counsel approval.** This includes communications to clients, vendors, regulators, media, or law enforcement. The Communications Lead prepares all external statements; Legal Counsel and CISO approve before release.

---

## 6. Regulatory Notification Timelines

### HIPAA Breach Notification (45 CFR §164.404 – §164.408)

| Notification Type | Timeline | Recipient | Requirement |
|------------------|----------|-----------|-------------|
| Individual notification | 60 days after breach discovery | Affected individuals | Required for any PHI breach affecting 1+ individuals |
| HHS notification (small breach) | 60 days after calendar year end | HHS Secretary | For breaches affecting <500 individuals |
| HHS notification (large breach) | 60 days after breach discovery | HHS Secretary | For breaches affecting 500+ individuals |
| Media notification | 60 days after breach discovery | Prominent media in affected state | For breaches affecting 500+ individuals in a state |
| Business associate notification to covered entity | 60 days after discovery | Covered entity | If MedData Nexus is a Business Associate |

**Internal HIPAA timeline trigger:** Legal Counsel makes breach determination within 5 business days of incident containment. Clock starts at the date MedData Nexus (as a covered entity or business associate) discovers the breach.

### State Breach Notification Laws

| Jurisdiction | Law | Timeline | Threshold |
|-------------|-----|----------|-----------|
| Washington State | RCW 19.255.010 | 30 days after discovery | Any personal data breach |
| California (CCPA/CPRA) | Cal. Civ. Code §1798.82 | Expedient time, no specific deadline | Personal information breach |
| Canada (PIPEDA/PHIPA Ontario) | PIPEDA + Ontario PHIPA | Expedient notice (PIPEDA); within 24 hours of assessment (PHIPA, if risk of harm) | Personal health information |

**Note:** MedData Nexus operates in Washington State and maintains Canadian operations (British Columbia). Any breach involving Canadian personal health information must be reported per both PIPEDA and applicable provincial health privacy law. Legal Counsel will identify applicable jurisdictions during breach determination.

---

## 7. AI/ML Incident Playbook

This playbook covers security incidents specific to MedData Nexus's AI and machine learning systems, including the Internal RAG Chatbot, NovaMind document summarization API, and internally developed ML models.

### 7.1 AI System Compromise

**Triggers:** Evidence that an AI system has been accessed by an unauthorized party, that model weights or system prompts have been modified, that AI system credentials have been exfiltrated, or that an AI system is producing outputs inconsistent with its intended behavior in a way that suggests external manipulation.

**Initial Response:**
1. Disable the affected AI endpoint at the API gateway level immediately (do not modify the system itself)
2. Preserve the current state: capture API gateway logs, model serving logs, any inference logs for the 72 hours prior to detection
3. Notify CISO and IR Lead — treat as P1 if PHI may have been exposed; P2 if internal/confidential data only
4. Do NOT restart or redeploy the model until forensic review of the serving environment is complete

**Investigation checklist:**
- [ ] Were model weights modified? Compare checksums against last known-good registry artifact
- [ ] Were system prompt or retrieval configurations changed? Review version control history
- [ ] What queries were submitted in the 72 hours prior to detection? Review inference logs
- [ ] Were any anomalous data exfiltration patterns observed? Check outbound network connections from serving infrastructure
- [ ] Was the API key or authentication token for the AI endpoint compromised? Check Okta and API gateway access logs
- [ ] Did the AI system output any data that should not have been in its retrieval context? Review output logs

**Recovery:** Redeploy from a known-good model artifact in the model registry. Validate model checksums before and after. Conduct adversarial probing of the restored system before returning to production.

---

### 7.2 Training Data Poisoning

**Triggers:** Evidence that unauthorized data was injected into training datasets, that model behavior has systematically shifted in a way not explained by legitimate retraining, or that a malicious actor claims to have poisoned training data.

**Initial Response:**
1. Suspend all training runs immediately
2. Preserve current training datasets, data pipeline logs, and data ingestion logs
3. Notify IR Lead and CISO — severity classification depends on data sensitivity in training corpus and impact of behavioral shift

**Investigation checklist:**
- [ ] What data was ingested since the last validated training run? Review data ingestion pipeline logs
- [ ] Were there any unauthorized modifications to data staging buckets (S3 access logs)?
- [ ] Does the model exhibit systematic bias or behavior change consistent with poisoning? Conduct red-team evaluation
- [ ] Was the data validation gate (test_data_quality.py or equivalent) bypassed?
- [ ] Are there unauthorized commits to training data version control?

**Recovery:** Roll back to last validated training checkpoint. Re-run training data validation suite on all data ingested since last clean checkpoint. Retrain from validated baseline. Validate model behavior against held-out test set before promotion.

---

### 7.3 Prompt Injection Abuse

**Triggers:** User reports of unexpected AI chatbot behavior; SIEM alert on anomalous query patterns; AI chatbot outputs data outside its expected context; review of inference logs reveals crafted inputs attempting to override system instructions.

**Prompt injection** is an attack where a malicious actor crafts an input query designed to override the AI system's instructions, cause it to ignore safety guardrails, or output data it should not have access to. This can occur through direct user queries or indirectly through malicious content embedded in documents that are retrieved during RAG.

**Initial Response:**
1. Preserve the full inference log for the affected query, including the query text, retrieved context, and full model output
2. Assess whether the output constituted a policy violation: Did the model output Restricted or Confidential data? Did it override a safety instruction?
3. If data exfiltration is suspected (model output data it should not have accessed): escalate to P1/P2; apply AI System Compromise checklist
4. If behavioral manipulation only (no data leak): treat as P3 and begin policy analysis

**Investigation checklist:**
- [ ] What was the exact query text? Was it submitted by a user or embedded in a retrieved document (indirect injection)?
- [ ] What was the full system output? Did it violate data classification rules?
- [ ] Is there evidence of coordinated or repeated injection attempts by the same user or IP?
- [ ] Did the retrieved documents contain embedded instructions (policy or document poisoning)?
- [ ] Is the attack pattern covered by existing safety guardrails? If not, what guardrail needs to be added?

**Containment and remediation:**
- If a specific user is identified as conducting intentional prompt injection: revoke AI system access immediately; refer to HR and Legal for disciplinary/legal review
- If document poisoning (indirect injection via RAG corpus): identify and quarantine the poisoned document(s); re-index the knowledge base after removing poisoned content; investigate how the document was ingested
- Update AI system safety instructions and retrieval filter rules to address the specific injection technique observed
- Conduct full red-team evaluation of the AI system post-remediation

---

## 8. Evidence Preservation Requirements

All IR activities must produce a defensible evidence record. MedData Nexus follows NIST SP 800-86 guidelines for evidence collection.

**Chain of custody principles:**
- Evidence is never modified after collection
- All copies are hash-verified (SHA-256)
- Every person who handles evidence is documented
- Evidence storage is access-controlled and logged

**Required evidence artifacts per incident:**
- Incident ticket with complete activity log (ServiceNow)
- System snapshots (EBS snapshots for EC2; RDS automated snapshots)
- Log exports from SIEM (Sumo Logic query exports, retained minimum 2 years)
- Network flow logs (VPC Flow Logs for affected subnets)
- Forensic memory capture (where applicable)
- Chain of custody document (template: IR-CHAIN-OF-CUSTODY-TPL-001)

**PHI breach evidence (additional requirements):**
- Legal hold initiated on all evidence related to a potential PHI breach
- Evidence package prepared for HHS OCR submission if notification is required
- Breach determination document signed by Legal Counsel and CISO

---

## 9. Version History

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| 1.0 | March 2023 | IT Security | Initial IRP — PICERL framework |
| 2.0 | January 2025 | D. Okafor (IR Lead) | Updated team roster; added HIPAA notification timelines; added state law table |
| 3.0 | February 2026 | C. Yung (CISO), D. Okafor | Added AI/ML Incident Playbook (Section 7); updated state law timelines; added Canadian privacy law; updated on-call procedures |

---

*Approved by: Constant Yung, CISO — February 1, 2026*  
*Next mandatory review: February 1, 2027 or after any P1 incident, whichever is sooner*
