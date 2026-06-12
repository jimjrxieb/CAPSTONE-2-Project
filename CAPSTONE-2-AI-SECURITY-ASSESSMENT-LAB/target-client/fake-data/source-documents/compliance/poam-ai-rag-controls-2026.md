> Synthetic data for Capstone 2 testing only.
> No real patient, customer, credential, contract, or GuidePoint client data.

---

# MedData Nexus Health Systems
## AI/RAG Plan of Action and Milestones
**Document ID:** POAM-AI-RAG-2026-001  
**Version:** 1.0  
**Prepared Date:** April 20, 2026  
**Owner:** IT Security / Compliance  
**Classification:** Confidential

---

## 1. Purpose

This POA&M tracks remediation work required before the Internal RAG Chatbot can move beyond controlled pilot use. Items are based on AI governance review, HIPAA Security Rule considerations, SOC 2 control expectations, and RAG security assessment findings.

## 2. Open Items

| POA&M ID | Gap | Risk | Owner | Target Date | Status |
|---|---|---|---|---|---|
| AI-RAG-001 | Retrieval authorization not validated with role-based users | High | Platform Engineering | May 15, 2026 | Open |
| AI-RAG-002 | Prompt-injection testing not completed against poisoned documents | High | IT Security | May 22, 2026 | Open |
| AI-RAG-003 | Output filter for secrets and PHI not validated | High | AI Platform Team | May 29, 2026 | Open |
| AI-RAG-004 | ChromaDB network policy not independently reviewed | Medium | Cloud Security | May 30, 2026 | In Progress |
| AI-RAG-005 | Audit log retention and reviewer action logging not proven | Medium | Security Operations | June 7, 2026 | Open |
| AI-RAG-006 | External AI API use path lacks final data-boundary approval | Medium | AI Governance Committee | June 14, 2026 | Open |

## 3. Required Evidence

Each item must include:

- Control owner.
- Remediation action.
- Test method.
- Evidence artifact.
- Reviewer name and date.
- Residual risk decision.

## 4. Scale Gate

The Internal RAG Chatbot may not scale beyond the pilot until High-risk POA&M items are closed or formally accepted by the CISO with documented compensating controls.
