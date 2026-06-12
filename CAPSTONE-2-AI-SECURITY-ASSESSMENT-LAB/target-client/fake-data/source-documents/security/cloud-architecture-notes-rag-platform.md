> Synthetic data for Capstone 2 testing only.
> No real patient, customer, credential, contract, or GuidePoint client data.

---

# MedData Nexus Health Systems
## RAG Platform Cloud Architecture Notes
**Document ID:** ARCH-RAG-2026-001  
**Version:** 0.9  
**Date:** April 12, 2026  
**Owner:** Platform Engineering  
**Classification:** Confidential

---

## 1. Architecture Summary

The Internal RAG Chatbot is hosted in AWS using Kubernetes-managed application services and a self-hosted vector database. The platform is designed for internal use by compliance, legal, security, and clinical administrative teams.

```text
Approved document repository
  -> ingestion job
  -> chunking and metadata labeling
  -> embeddings
  -> ChromaDB vector store
  -> retrieval API
  -> prompt builder
  -> model inference path
  -> output validation
  -> user response and evidence logs
```

## 2. Primary Components

| Component | Description | Security Notes |
|---|---|---|
| Document repository | Approved Markdown source documents | Source approval required before ingestion |
| Ingestion job | Parses, chunks, labels, and embeds documents | Must reject poisoned, restricted, or unsanitized content |
| ChromaDB | Stores embeddings and metadata | Network access limited to RAG namespace |
| Retrieval API | Queries ChromaDB and returns source chunks | Must enforce metadata filters |
| Prompt builder | Combines user question and retrieved chunks | Retrieved text must be treated as untrusted data |
| Eugene assessment API | Produces draft security findings and mappings | Advisory only; human review required |
| Evidence store | Stores prompts, retrieved chunk IDs, model outputs, and review status | Required for PROVE package |

## 3. Trust Boundaries

- User browser to chatbot API.
- Chatbot API to retrieval API.
- Retrieval API to ChromaDB.
- Ingestion job to document repository.
- Prompt builder to model inference path.
- Model output to user and evidence store.
- Assessment workflow to ticketing and approval systems.

## 4. Network Assumptions

- Internal access requires VPN and SSO.
- ChromaDB is not internet-exposed.
- Administrative access requires a managed device and privileged role.
- External AI APIs are not called by default for Restricted or Confidential data.
- Any Haiku API path must receive only approved or sanitized context and must be documented in the AI System Inventory.

## 5. Architecture Risks

- If metadata filtering fails, users may retrieve documents outside their authorized scope.
- If prompt construction treats retrieved text as instruction, poisoned documents may override system behavior.
- If evidence logging is incomplete, the organization cannot reconstruct what was retrieved or why an answer was generated.
- If the vector database is reachable outside the RAG namespace, embeddings and source chunks may be exposed.
