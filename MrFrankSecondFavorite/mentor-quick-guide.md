# Mr. Frank Quick Guide - Capstone 2

> **Start with `capstone-as-engagement.md` for the capstone story.** Eugene / Capstone 2 is the worked example. The reusable templates are supporting material. This guide is the broader capstone walkthrough.

This folder is the short version for reviewing what I built and why it matters for the GuidePoint Security AI Security Engineer role.

Start with `README.md`, then read `ai-sec.md`. That file maps the same capstone work to AI integration, cybersecurity, DevSecOps, platform engineering, cloud architecture, and compliance/governance.

## The Simple Story

I built a client-style AI security assessment lab around **Eugene**, a local RAG assistant for a fictional healthcare SaaS company called MedData Nexus.

The project is not just "I used AI tools." The point is:

- define what AI is allowed to do
- build the system with controls
- attack the assumptions
- prove what worked with evidence
- explain the risk like a consultant

My method is **CBBP**:

- **COMPLY:** define scope, data boundaries, approvals, and risk rules
- **BUILD:** build Eugene, guardrails, workflows, and deployment controls
- **BREAK:** test prompt injection, corpus poisoning, unauthorized retrieval, unsafe output, and AI coding assistant misuse
- **PROVE:** package findings, framework maps, evidence, executive summary, and remediation roadmap

## Why It Fits GuidePoint AI Security

The GuidePoint role is about helping customers safely design, assess, deploy, govern, and operate AI systems.

This capstone lines up well because it shows:

- AI/RAG security architecture
- RAG and vector database trust boundaries
- prompt injection and corpus poisoning tests
- AI-assisted development governance
- Codex and Claude Code guardrails
- human-in-the-loop review
- evidence-based security reporting
- OWASP LLM, MITRE ATLAS, NIST AI RMF, and NIST 800-53 mapping
- Python/FastAPI/security automation
- Kubernetes and CKS-style deployment hardening
- client-facing reports and executive communication

## Best Folders To Review

### Start Here

- `README.md`
- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/README.md`
- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/STATUS.md`
- `Eugene-AI/README.md`

These give the overall story, scope, current status, and what Eugene does.

### Codex and Claude Code Guardrails

- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BUILD/ai-dev-assist-harness.md`
- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/PROVE/ai-dev-tool-boundary-evidence.md`
- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/lessons/12-harnessing-ai-dev-tools-as-engineering-team.md`
- `Eugene-AI/.github/workflows/ai-assist-label-check.yml`
- `Eugene-AI/CODEOWNERS`

This is where I show that Codex and Claude Code are treated as governed dev tools, not uncontrolled agents.

### Eugene RAG Assistant

- `Eugene-AI/src/api/routes/query.py`
- `Eugene-AI/src/rag/pipeline.py`
- `Eugene-AI/src/rag/retriever.py`
- `Eugene-AI/src/rag/sanitizer.py`
- `Eugene-AI/src/rag/output_filter.py`
- `Eugene-AI/src/guardrails/access_control.py`
- `Eugene-AI/src/guardrails/secret_scanner.py`
- `Eugene-AI/src/guardrails/phi_scanner.py`
- `Eugene-AI/src/audit/logger.py`

This is the working Python security engineering part: API, RAG pipeline, access control, scanning, output filtering, and audit logging.

### CrewAI Planning

- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BUILD/crewai/README.md`
- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BUILD/crewai/agent-role-map.md`
- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BUILD/crewai/security-boundaries.md`
- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BUILD/crewai/evidence-contract.md`
- `Eugene-AI/src/agents/crew.py`

This shows how I thought about agent roles, evidence boundaries, and keeping agents advisory instead of letting them approve risk.

### Harnesses and Evidence

- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/COMPLY/Cap2-Harness.md`
- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BUILD/eugene-build-harness.md`
- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BUILD/rag-pipeline-build.md`
- `Eugene-AI/src/evidence/`
- `Eugene-AI/evidence/`

This is the proof work: repeatable checks, generated evidence, BREAK tests, and platform control validation.

### BREAK Scenarios

- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/scenarios/`
- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BREAK/meddata-rag-break.md`
- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BREAK/meddata-coding-assistant-break.md`
- `Eugene-AI/src/evidence/chatbox_break_runner.py`
- `Eugene-AI/src/evidence/corpus_contamination_break_runner.py`
- `Eugene-AI/src/evidence/unauthorized_retrieval_break_runner.py`
- `Eugene-AI/src/evidence/hitl_review_break_runner.py`

This is where I test whether the system survives misuse instead of just claiming it is secure.

### CKS / Kubernetes Hardening

- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BUILD/cks-platform-build-plan.md`
- `Eugene-AI/deploy/k8s/`
- `Eugene-AI/deploy/policies/`
- `Eugene-AI/src/evidence/platform_control_check.py`

This maps to cloud/AppSec/platform security: non-root, resource limits, no privileged containers, ChromaDB auth, NetworkPolicy, service accounts, and deployment hardening.

### Client Deliverables

- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/deliverables/02-client-findings-report.md`
- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/deliverables/01-executive-summary.md`
- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/deliverables/03-remediation-roadmap.md`
- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/deliverables/04-ai-adoption-operating-model.md`
- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/PROVE/meddata-prove-package.md`

This is the consulting side: findings, business risk, roadmap, and executive-level language.

## Strong Interview Angle

Casual version:

> I built Eugene as a local RAG security lab, then wrapped it in a consulting workflow. I used Codex and Claude Code, but I also built guardrails around them: data boundaries, review gates, CODEOWNERS, AI-assisted PR labeling, evidence logs, and BREAK tests. The goal was to show how a company can use AI dev tools aggressively without losing control of security, human approval, or auditability.

More GuidePoint version:

> This project demonstrates governed AI adoption. I can help a client define AI usage boundaries, build secure RAG and AI-assisted development workflows, test those workflows against realistic failure modes, map findings to control frameworks, and package the evidence into customer-ready security recommendations.

## What I Would Tell A Senior AI Security Engineer

The strongest part is not just the model. It is the operating model around the model.

I built:

- local-only AI boundary for Eugene
- synthetic healthcare corpus
- RAG ingestion controls
- role-filtered retrieval
- prompt injection and poisoned document tests
- secret and PHI scanning
- audit logging
- HITL review
- Kubernetes hardening
- AI dev tool governance for Codex and Claude Code
- evidence runners that prove control behavior

The honest phase-2 gaps are also clear:

- deployed-cluster live validation still needs to be run
- real identity provider integration would replace static lab tokens
- generation-model quality eval is future work
- cloud AI service versions like Bedrock/SageMaker would need their own COMPLY boundary

That honesty helps. It shows I know the difference between a lab, a pilot, and production.
