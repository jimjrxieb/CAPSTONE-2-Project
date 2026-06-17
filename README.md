# Eugene AI Security Assessment Lab

Capstone project for governed AI security assessment, secure RAG engineering, and safe use of AI development tools.

This repository contains a complete local lab for building and assessing **Eugene**, a fictional healthcare SaaS internal RAG assistant. The project is written as a GuidePoint-style client engagement: define the AI adoption boundary, build the target system, break the assumptions, prove the results with evidence, and package the findings for security leadership.

## Executive Summary

Eugene is a local AI security assessment assistant for a synthetic client, MedData Nexus Health Systems. It retrieves from a controlled policy, compliance, vendor-risk, security, and healthcare-privacy corpus, then produces advisory answers that require human review before they can become findings or client deliverables.

The capstone demonstrates three things:

- **AI security consulting:** intake, threat modeling, framework mapping, risk register, executive summary, remediation roadmap, and adoption operating model.
- **Secure RAG/MLOps execution:** manifest-gated ingestion, role-filtered retrieval, source citations, output filtering, audit logging, evidence runners, API/chat UI, container/Kubernetes manifests, and policy checks.
- **Governed AI-assisted development:** Codex and Claude Code are treated as bounded engineering assistants with explicit data boundaries, review gates, approval checkpoints, and evidence capture.

## Repository Map

| Path | Purpose |
| --- | --- |
| `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/` | Consulting workpapers, CBBP lifecycle, lessons, scenarios, framework maps, and client-ready deliverables |
| `Eugene-AI/` | Runnable local RAG assistant, API, chatbox, guardrails, tests, evidence runners, Docker/Kubernetes assets |
| `.env.example` | Slot-level environment template with no real secrets |

## Capstone Scope

The project answers this engagement question:

> Can a healthcare SaaS organization safely pilot and scale an internal RAG assistant over sensitive business documents while also using AI development tools in a controlled engineering workflow?

The scope includes:

- Synthetic healthcare SaaS target client and fake corpus
- Local-only Eugene assistant using Ollama and ChromaDB
- RAG data flow, trust boundaries, and architecture review
- Prompt injection, poisoned corpus, unauthorized retrieval, sensitive data, audit logging, and HITL review scenarios
- AI coding assistant governance scenarios for Codex and Claude Code
- Framework mapping to OWASP LLM Top 10, MITRE ATLAS, NIST AI RMF, and NIST 800-53
- Evidence-backed deliverables for findings, executive summary, remediation roadmap, and AI adoption operating model

Out of scope:

- Real client data, real PHI, real credentials, or production secrets
- Autonomous model approval of security findings
- External LLM API transmission of Eugene retrieved context without a new COMPLY boundary
- Production-grade identity provider integration

## What I Built

### Eugene Target System

- FastAPI service with `/query`, `/ingest`, `/evidence/*`, and `/health` routes
- Gradio chatbox with role selection, source citations, high-risk warning, and no upload/history surface
- ChromaDB retrieval path with local embedding function and role-based post-retrieval filtering
- Deterministic advisory draft path for repeatable evidence tests
- Local model boundary documented for `llama3.2:3b` via Ollama

### Guardrails

- Manifest-gated corpus ingestion
- Prompt-injection scanner before query handling and before document embedding
- Secret and PHI scanners before ingestion
- Role-based corpus access control for `vendor_risk_reviewer`, `compliance_analyst`, and `it_security`
- Output filtering for sensitive values
- Human-in-the-loop review flagging for high-risk sources and outputs
- Structured JSONL audit logging
- API auth/rate-limit controls
- ChromaDB token-auth and NetworkPolicy design for deployed mode
- GitHub Actions for dependency audit and AI-assisted PR labeling
- CODEOWNERS coverage for security-sensitive areas

### Evidence Harnesses

- Sprint 1 control check for sanitizer, access control, output filter, ingest dry run, unsafe-document rejection, and audit logging
- Chatbox BUILD and BREAK checks
- Baseline RAG retrieval evaluation
- Corpus contamination BREAK tests
- Unauthorized retrieval BREAK tests
- HITL review bypass BREAK tests
- Platform control evidence for model pins, dependency pins, Chroma auth, NetworkPolicy, and rate limiting
- Eugene helpfulness evaluation over business-use questions

## Certification Alignment — CompTIA SecAI+ (CY0-001)

This lab was built to double as hands-on proof for the CompTIA SecAI+ (CY0-001)
exam domains. Every claim below is backed by a runnable artifact in this repo —
scenario, scanner, evidence runner, or control mapping — not just narrative.

| SecAI+ Domain (exam weight) | Demonstrated in this lab |
| --- | --- |
| **1 — Basic AI Concepts (17%)** | Local RAG pipeline (ChromaDB + local embedding function), Ollama `llama3.2:3b` deployment, role-filtered retrieval, manifest-gated ingestion, prompt-engineering harness, FastAPI serving layer |
| **2 — Securing AI Systems (40%)** | Prompt-injection defense with BREAK tests, corpus poisoning / contamination BREAK tests, unauthorized-retrieval access control, output filtering for sensitive data, PHI + secret pre-ingestion scanners, ChromaDB token-auth and NetworkPolicy boundary, dependency-audit supply-chain gate, documented agentic trust boundaries |
| **3 — AI-Assisted Security (24%)** | End-to-end AI-assisted security-assessment workflow, HITL-gated analysis, structured JSONL audit logging for behavioral tracking, AI-assisted PR labeling in CI, automated evidence runners as continuous validation |
| **4 — AI Governance, Risk & Compliance (19%)** | NIST AI RMF, NIST 800-53, OWASP LLM Top 10, and MITRE ATLAS mappings; risk register; POA&M; findings report and executive summary; AI dev-tool governance model; corpus data classification; vendor risk for Ollama/ChromaDB |

This lab is one half of a two-part proof: the **hands-on lab** (this repo) and the
**GP-CONSULTING framework library** (control cards, framework crosswalks, AI-RMF /
AI-600-1 references) that the lab instantiates from. Together they map to all four
SecAI+ domains.

Targeted hardening in progress to take Domains 2–4 from strong to comprehensive:
adversarial scenarios for model inversion, membership inference, and embedding
inversion; and assessment artifacts for output watermarking, AI-enabled threat
landscape, AI-assisted incident response, bias/fairness, and regulatory context
(EU AI Act, HIPAA AI guidance).

## CBBP Method

This capstone uses **CBBP: COMPLY, BUILD, BREAK, PROVE**.

| Phase | What It Means Here |
| --- | --- |
| COMPLY | Define client scope, approved data, AI tool boundaries, intake, risk model, and control expectations |
| BUILD | Implement Eugene, guardrails, API/chatbox, corpus pipeline, deployment artifacts, and AI dev-assist harness |
| BREAK | Attack the claims with prompt injection, poisoned documents, unauthorized retrieval, unsafe outputs, and workflow bypasses |
| PROVE | Package evidence, mappings, risk register, findings report, executive summary, and remediation plan |

## AI Dev Tool Governance

This project intentionally embraces Codex and Claude Code, while treating them as controlled engineering tools:

- They can operate on approved repo files, sanitized docs, and generated fake data.
- They cannot receive real client data, real PHI, real credentials, or uncontrolled sensitive context.
- Security-sensitive changes require human review.
- Broad local command access, external network use, and destructive operations require explicit approval.
- Provider safety flags, model routing changes, and permission prompts are recorded as governance signals, not hidden.
- Eugene remains advisory; the human assessor owns final risk decisions.

Primary harness: `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BUILD/ai-dev-assist-harness.md`.

## What I Learned And Executed

- How to scope an AI security assessment as a consulting engagement rather than just a coding project
- How to turn AI risk language into concrete build gates and evidence checks
- How to separate trusted system instructions from untrusted user and corpus content
- How RAG systems fail through corpus poisoning, retrieval overreach, weak source governance, and missing review gates
- How to map technical AI failures to business risk and control frameworks
- How to build repeatable evidence so a finding can survive senior-engineer or CISO review
- How to use AI development tools productively while preserving data boundaries, review authority, and auditability

## How To Run

```bash
cd Eugene-AI
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Run targeted checks:

```bash
pytest tests/ -v
python3 -m src.evidence.sprint1_control_check
python3 -m src.evidence.platform_control_check
```

Run the API:

```bash
uvicorn src.api.main:app --host 127.0.0.1 --port 8000
```

Run the chatbox:

```bash
python3 -m src.chatbox.app
```

See `Eugene-AI/README.md` for full setup and test commands.

## Current Status

This project is ready to present as a capstone lab. The core Eugene security controls, evidence runners, synthetic client package, consulting deliverables, and local CKS-style platform build scope are present. BUILD is complete for the local capstone. Future work sits outside this BUILD boundary: external identity provider integration if this becomes a production pilot, remote GitHub CI run history after publishing, expanded workflow automation, and cloud AI service extensions under a new COMPLY boundary.

## GitHub Publishing Notes

The parent `GP-SECLAB` repository ignores `target-application/`, so this folder should be pushed as its own standalone GitHub repository from `slot-5`.

Before publishing, keep generated artifacts out of git:

- `.env`
- `.venv/`
- `__pycache__/`
- `.pytest_cache/`
- `*.pyc`
- `Eugene-AI/evidence/chroma/`
- local audit logs that contain machine-specific run history

Evidence JSON summaries can be committed when they are sanitized and useful for the capstone story.
