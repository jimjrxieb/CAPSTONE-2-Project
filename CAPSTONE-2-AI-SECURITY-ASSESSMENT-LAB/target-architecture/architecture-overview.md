# Target Architecture Overview

## Purpose

Document the fictional MedData Nexus internal RAG target and how Eugene assesses it.

This folder describes the **target system under assessment**. Eugene's source code and implemented controls live in `../../Eugene-AI/`.

## Target Architecture

```text
Sensitive compliance/security docs
  -> RAG preparation pipeline
  -> chunks + metadata + embeddings
  -> vector database
  -> chatbot retrieval layer
  -> Eugene assessment API
  -> findings + mappings + roadmap
```

## Required Notes

- What documents are in scope?
- What data is sensitive?
- Who can query the system?
- What does Eugene assess?
- Where are logs stored?
- Where is human review required?

## System Ownership

| Area | Owner |
|---|---|
| System name | MedData Nexus Internal GenAI/RAG Environment |
| Business owner | Compliance Director |
| Technical owner | Platform Engineering Lead |
| Risk owner | CISO / AI Governance Committee |
| Data owners | Legal, Compliance, Security, Privacy, and Vendor Risk teams by corpus category |
| Evidence owner | IT Security / Security Operations |
| Approval authority | CISO for Restricted data, production expansion, and external API authorization |

## System Scope

In scope:

- local RAG ingestion over approved synthetic MedData Nexus documents
- corpus manifest and document approval boundary
- vector database collection for the clean baseline and scenario variants
- Eugene assessment API/chatbox
- prompt, retrieval, output, and review evidence capture
- BREAK scenarios for prompt injection, poisoned documents, secrets in corpus, unauthorized retrieval, source leakage, vector DB access gaps, missing output filtering, and missing audit logging

Out of scope for the first build:

- real patient data
- real customer contracts
- real credentials or API keys
- live production healthcare systems
- autonomous risk acceptance
- external API processing of Restricted data

## Data Boundary

| Data Type | Baseline RAG Status | Notes |
|---|---|---|
| Internal policy documents | Allowed | Source tracked in corpus manifest |
| Confidential compliance/security/legal/vendor documents | Allowed for read-only retrieval and draft summarization | Human review required before external distribution |
| Sanitized incident records | Allowed | Specific identifiers and credentials must be redacted |
| PHI/ePHI or Restricted data | Not allowed in baseline | Requires explicit CISO authorization and documented handling terms |
| Secrets and credentials | Not allowed | Used only in unsafe scenario tests |
| Poisoned documents | Not allowed in baseline | Used only for BREAK testing |

## Human Review Points

Human review is required before:

- acting on high-risk Eugene findings
- accepting residual risk
- expanding from pilot to production
- authorizing Restricted-data processing
- using external API paths for Confidential or Restricted context
- distributing legal, compliance, vendor-risk, or security conclusions outside the assessment team
