> Synthetic data for Capstone 2 testing only.
> No real patient, customer, credential, contract, or GuidePoint client data.

---

# MedData Nexus Health Systems
## Internal RAG Chatbot System Security Plan Excerpt
**Document ID:** SSP-RAG-2026-001  
**Version:** 1.0  
**Effective Date:** April 15, 2026  
**Owner:** IT Security / Platform Engineering  
**Classification:** Confidential  
**System Name:** MedData Nexus Internal RAG Chatbot

---

## 1. System Purpose

The Internal RAG Chatbot provides read-only retrieval and draft summarization over approved MedData Nexus policy, compliance, security, vendor-risk, privacy, and legal template documents. It is intended to reduce analyst search time while preserving the official document repository as the source of truth.

The chatbot is not approved for clinical decision support, automated regulatory submission, autonomous legal interpretation, or processing of PHI unless explicit CISO authorization and AI System Inventory approval are completed.

## 2. System Boundary

In scope:

- Web chatbot interface available on managed devices through VPN and SSO.
- Retrieval API that queries the approved ChromaDB collection.
- Document ingestion job for approved Markdown source documents.
- Eugene assessment API used by the capstone to review risks and draft findings.
- Evidence capture for prompts, retrieved sources, outputs, and reviewer decisions.

Out of scope:

- Production EHR systems.
- Patient-facing applications.
- Live clinical records.
- External consumer AI tools.
- Unapproved third-party AI APIs.

## 3. Data Types

Approved for baseline ingestion:

- Internal policy documents.
- Compliance summaries.
- Security assessment summaries.
- Vendor risk assessments.
- Legal templates.
- Sanitized incident summaries.

Not approved for baseline ingestion:

- PHI or ePHI.
- Real patient identifiers.
- API keys, passwords, access tokens, or signing secrets.
- Unreviewed vendor questionnaire free text.
- Documents containing embedded model instructions or prompt-injection payloads.

## 4. Core Controls

| Control Area | Implementation |
|---|---|
| Identity | SSO required; chatbot users inherit Okta identity and role claims |
| Authorization | Retrieval filters enforce user role, data classification, and approved corpus scope |
| Data boundary | Restricted data is excluded unless CISO authorization is documented |
| Prompt construction | Retrieved content is treated as data, not system instruction |
| Output handling | Outputs are drafts; high-risk outputs require human review |
| Logging | Query, retrieved source IDs, model response, and reviewer action are logged |
| Evidence | Assessment runs produce JSON evidence artifacts and client-facing findings |

## 5. Open Control Gaps

- Retrieval authorization has not yet been validated against role-based test users.
- Prompt-injection resistance has not yet been proven through poisoned corpus testing.
- Output filtering for secrets and PHI requires BREAK validation.
- ChromaDB access control must be confirmed before production-scale use.

## 6. Authorization Statement

The Internal RAG Chatbot is approved only for controlled assessment and pilot use. Expansion beyond the pilot requires completion of the CBBP PROVE package, including retrieval test evidence, prompt-injection results, secrets-in-corpus validation, audit logging validation, and executive scale/no-scale recommendation.
