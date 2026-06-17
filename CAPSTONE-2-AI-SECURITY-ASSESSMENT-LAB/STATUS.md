# Capstone 2 Status

## Current Position

Capstone 2 BUILD is complete for Eugene, a local RAG assistant for the fictional
MedData Nexus Health Systems environment. The Sprint 1 unauthorized-retrieval
identity finding was remediated, re-tested, and closed; the local platform,
generation, and CrewAI dry-run scope is packaged as completed BUILD work.

The project has moved beyond scaffold. It includes a synthetic client corpus, architecture workpapers, CBBP lifecycle documentation, implemented Eugene API/chatbox paths, guardrail modules, tests, evidence runners, BREAK scenarios, framework mappings, and client-facing deliverables.

## Completed Build Scope

- Target client and fake data package
- RAG architecture, data flow, and trust-boundary documentation
- Manifest-gated ingestion pipeline
- Prompt-injection, secret, and PHI scanning before ingestion
- Role-filtered retrieval for vendor risk, compliance, and IT security roles
- FastAPI `/query`, `/ingest`, `/evidence/*`, and `/health` routes
- Gradio chatbox with role selection, source citations, high-risk warning, and no upload/history surface
- Output filtering and human-in-the-loop review flags
- Structured audit and review logging
- Evidence runners for BUILD and BREAK validation
- Dockerfile, Kubernetes manifests, NetworkPolicy, and policy checks
- CKS-style local platform evidence
- AI development assistant harness for Codex and Claude Code
- Client findings report, executive summary, remediation roadmap, and AI adoption operating model

## Evidence Captured

Evidence files under `Eugene-AI/evidence/` show:

- Sprint 1 control checks
- Baseline RAG retrieval checks
- Chatbox BUILD checks
- Chatbox BREAK checks
- Corpus contamination BREAK checks
- Unauthorized retrieval BREAK checks
- HITL review bypass checks
- Platform control checks for dependency pins, model pins, Chroma auth, NetworkPolicy, and rate limiting
- Eugene helpfulness evaluation over scoped business questions

## Current Presentation Frame

This capstone should be presented as:

> A governed AI adoption and AI security assessment lab that builds a realistic internal RAG assistant, attacks its trust boundaries, and packages evidence in the style of a client-facing GuidePoint engagement.

The strongest talking points are:

- CBBP lifecycle: COMPLY, BUILD, BREAK, PROVE
- Local-first model and data boundary
- RAG-specific controls instead of generic chatbot claims
- Evidence-backed findings and framework mapping
- Human authority over risk decisions
- Safe AI-assisted development with Codex and Claude Code under a documented harness

## Future Work Outside BUILD

- Add external identity provider integration instead of static lab tokens if this lab becomes a production pilot
- Add remote GitHub CI run history after publishing
- Expand n8n intake/evidence workflow
- Add cloud AI service extension workpapers for Bedrock/SageMaker as a separate COMPLY boundary
- Polish PROVE packaging if a reviewer wants a different client-facing format

## Daily Work Path

1. Pick one scenario from `scenarios/`.
2. Run or update the matching evidence runner.
3. Update `CBBP-PLAN/PROVE/` with the evidence result.
4. Tighten one client-facing deliverable.
5. Practice explaining the finding in one engineering sentence and one CISO sentence.
