# AI Adoption Operating Model

## Purpose

This deliverable explains how MedData Nexus should govern, secure, test, and prove AI adoption across RAG, coding assistants, and analyst workflows.

## Executive Summary

AI adoption should not scale until the organization can prove:

- what AI tools are approved
- what data AI can access
- what actions AI can take
- where human approval is required
- what technical controls enforce the workflow
- what BREAK testing proves the controls held
- what evidence supports expansion

## Operating Model

| Area | Requirement | Evidence |
|---|---|---|
| ownership | named business, security, and technical owners | RACI / decision record |
| approved tools | approved AI vendors, models, and coding assistants | tool inventory |
| data boundary | allowed and prohibited data classes | data classification matrix |
| human authority | actions requiring human review or approval | human decision matrix |
| technical guardrails | identity, RBAC, logging, CI gates, DLP, review gates | config exports / policies |
| adversarial testing | prompt injection, RAG poisoning, bypass, drift tests | BREAK results |
| evidence | logs, reports, findings, approvals, POA&M records | PROVE package |

## AI Coding Assistant Guardrails

Minimum controls:

- approved tools only
- SSO and team-based access
- repo scope restrictions
- prohibited data rules
- AI-assisted PR label
- security review for auth, crypto, access control, secrets, and logging changes
- SAST/SCA/IaC/secrets scans
- dependency justification for new packages
- human approval for production promotion
- audit trail for high-impact AI-assisted work

## RAG Guardrails

Minimum controls:

- corpus inventory
- source owner and sensitivity classification
- ingestion approval
- vector database access controls
- retrieval filtering
- poisoned document tests
- secrets/PII scanning
- output validation
- citation and provenance checks
- audit logging

## Agentic Workflow Guardrails

Minimum controls:

- tool allowlist
- least-privilege execution
- no production action without approval
- command review before execution
- rate limits and abuse detection
- tool-call logging
- rollback and kill-switch procedures

## Pilot-To-Scale Criteria

Scale only when:

- COMPLY scope is clear
- BUILD controls are implemented
- BREAK tests are run
- critical findings are remediated or accepted
- PROVE package supports the decision

## Recommendation Language

Scaling without evidence is distributed risk.

Scaling with CBBP creates an AI operating model.

