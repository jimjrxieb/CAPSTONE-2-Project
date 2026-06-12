# Lesson 05 - RAG And Data Security

**Status: COMPLETE — 2026-06-08**
**COMPLY deliverable:** `CBBP-PLAN/COMPLY/meddata-rag-corpus-intake.md`
**BREAK deliverable:** `CBBP-PLAN/BREAK/meddata-rag-break.md`
**Scenarios filled:** `scenarios/rag-direct-prompt-injection.md`, `rag-poisoned-document.md`, `rag-secrets-in-corpus.md`, `rag-unauthorized-retrieval.md`

## What To Master

RAG risk is data boundary risk.

A RAG system can fail even when the model behaves well if retrieval, corpus governance, or output handling is weak.

## Questions I Should Ask

- What documents are in the corpus?
- Who approved them for ingestion?
- What sensitivity level do they have?
- Is PII, PHI, secrets, legal text, or customer data present?
- How are documents chunked and tagged?
- Can users retrieve documents they should not see?
- Can poisoned documents enter the corpus?
- Are citations or source references validated?
- Are outputs filtered before display?
- Are retrieval events logged?

## Evidence To Request

- corpus manifest
- ingestion logs
- document owner list
- sensitivity classification
- vector DB ACLs
- retrieval filter code
- prompt template
- output sanitizer code
- RAG test results
- audit logs

## What I Need To Know

RAG security is not just prompt injection.

It includes:

- corpus provenance
- ingestion integrity
- access control
- retrieval filtering
- metadata correctness
- source leakage
- secrets in corpus
- poisoned documents
- output validation

## Capstone Practice

Start with:

- `scenarios/rag-direct-prompt-injection.md`

Then move to:

- `scenarios/rag-poisoned-document.md`
- `scenarios/rag-secrets-in-corpus.md`
- `scenarios/rag-unauthorized-retrieval.md`

Task:

For one RAG scenario, write:

- attack path
- expected control
- evidence captured
- finding
- remediation
- validation step

## Finding Trigger

Create a finding if:

- corpus ownership is missing
- sensitive docs are retrievable by unauthorized users
- poisoned content affects model behavior
- outputs can leak source material
- logs cannot show what was retrieved

## CISO Sentence

> The RAG assistant can expose or misuse sensitive internal documents because retrieval governance and validation are not strong enough to prove users only receive authorized information.

