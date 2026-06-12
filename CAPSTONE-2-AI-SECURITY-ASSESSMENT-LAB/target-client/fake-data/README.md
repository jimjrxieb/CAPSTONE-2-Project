# Fake Data

This folder is the workspace for synthetic MedData Nexus documents used in Capstone 2.

## Hard Rule

All data in this folder must be synthetic.

Do not place real patient data, real PII, real PHI, real credentials, real API keys, real tokens, real contracts, real customer data, or real GuidePoint client information here.

## Git Tracking Rule

Git tracks the folder structure and this README only.

Actual generated documents, poisoned documents, secret-like samples, retrieval fixtures, and sanitized output are ignored by `.gitignore` to prevent accidental credential or sensitive-data exposure.

## Folder Map

```text
target-client/fake-data/
├── README.md
├── corpus-manifest.md
├── source-documents/
│   ├── policies/
│   ├── compliance/
│   ├── security/
│   ├── legal-contracts/
│   ├── healthcare-privacy/
│   ├── vendor-risk/
│   └── ai-governance/
├── poisoned-documents/
├── secrets-and-pii-samples/
├── expected-retrieval/
└── sanitized-baseline/
```

## Folder Purpose

| Folder | Purpose |
|---|---|
| `source-documents/` | Normal synthetic client documents for the RAG corpus |
| `poisoned-documents/` | Synthetic documents containing malicious prompt-injection payloads |
| `secrets-and-pii-samples/` | Synthetic unsafe examples used to test detection and filtering |
| `expected-retrieval/` | Expected retrieval fixtures for known questions |
| `sanitized-baseline/` | Cleaned/remediated versions of unsafe documents |

Use [corpus-manifest.md](corpus-manifest.md) as the source of truth for which documents belong in the clean baseline corpus, which documents are scenario-only, and which files must never be ingested as source knowledge.

## Synthetic Data Label

Every generated document should include:

```text
Synthetic data for Capstone 2 testing only.
No real patient, customer, credential, contract, or GuidePoint client data.
```

## Safe Fake Credential Pattern

If a test requires fake credentials, use obvious placeholders that scanners and humans can identify as fake:

```text
FAKE_API_KEY_DO_NOT_USE_000000
FAKE_SECRET_FOR_TESTING_ONLY
EXAMPLE_TOKEN_NOT_REAL
```

Never use realistic cloud-provider key formats unless the scanner test specifically requires it, and keep those files ignored.
