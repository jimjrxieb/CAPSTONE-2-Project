# AI Security Skill Map

> **Orientation:** the live proof is the Eugene / Capstone 2 lab. Start with `capstone-as-engagement.md`, then inspect `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/` and `Eugene-AI/`. The reusable templates are supporting material, not the main example.

This is the quick version of how my Capstone 2 work lines up with AI security consulting, especially the GuidePoint AI Security Engineer lane.

The capstone shows practical coverage across:

- AI Integration
- Cybersecurity
- DevSecOps
- Platform Engineering
- Cloud Architecture
- Compliance and Governance

My capstone shows applied work in the same problem space: AI workflows, security guardrails, DevSecOps checks, platform controls, and client-ready documentation.

## Where I Fit Right Now

### AI Integration

I built Eugene, a local RAG assistant for a fictional healthcare SaaS client.

What I can help with:

- AI workflow scoping
- RAG use-case design
- AI tool boundary documentation
- prompt/context risk review
- safe handoff between AI tools and human review
- practical AI adoption notes for non-AI teams

Proof points:

- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/README.md`
- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/COMPLY/meddata-ai-adoption-intake.md`
- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BUILD/eugene-build-harness.md`
- `Eugene-AI/src/rag/`

### Cybersecurity

The capstone is built around testing whether an AI/RAG workflow can be trusted.

What I can help with:

- AI/RAG security reviews
- prompt injection test planning
- corpus poisoning scenarios
- role-based access checks
- secret and PHI exposure checks
- findings writeups and remediation notes

Proof points:

- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/scenarios/`
- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BREAK/`
- `Eugene-AI/src/guardrails/`
- `Eugene-AI/src/evidence/`

### DevSecOps

I used the capstone to show how security can be built into the development workflow, especially when AI coding tools are involved.

What I can help with:

- AI-assisted PR review process
- CODEOWNERS and review gates
- dependency pinning and SCA checks
- evidence runners
- CI/CD security checklist work
- security acceptance criteria for AI-assisted code

Proof points:

- `Eugene-AI/.github/workflows/ai-assist-label-check.yml`
- `Eugene-AI/.github/workflows/sca.yml`
- `Eugene-AI/CODEOWNERS`
- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BUILD/ai-dev-assist-harness.md`

### Platform Engineering

The Eugene lab includes platform controls around the API, ChromaDB, Kubernetes manifests, and runtime boundaries.

What I can help with:

- container and Kubernetes review
- NetworkPolicy documentation
- service account review
- resource limit checks
- non-root and no-privileged policy checks
- platform control evidence

Proof points:

- `Eugene-AI/deploy/k8s/`
- `Eugene-AI/deploy/policies/`
- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BUILD/cks-platform-build-plan.md`
- `Eugene-AI/src/evidence/platform_control_check.py`

### Cloud Architecture

This capstone is local-first, but the control patterns map to cloud AI services.

What I can help with:

- cloud AI security requirements
- identity and token boundary notes
- logging and audit requirements
- private service exposure review
- AI workload threat modeling
- cloud migration checklist support

Current learning edge:

I am still building deeper production experience with Bedrock, SageMaker, Azure AI, and Vertex AI. The strong angle is that I understand the security pattern those systems need: identity, data boundaries, logging, least privilege, output validation, and evidence.

### Compliance And Governance

The capstone has a full governance lane, not just code.

What I can help with:

- AI system inventory
- AI adoption intake
- maturity assessment
- risk register support
- framework mapping
- executive summary drafting
- remediation roadmap drafting

Proof points:

- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/COMPLY/`
- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/PROVE/`
- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/deliverables/`

## How I Can Contribute To A Side Project

If Constant has a side project, I can be useful in these ways right away:

- write security notes and review checklists
- document architecture and data flows
- map risks to practical controls
- build small Python/FastAPI utilities
- write evidence scripts and validation checks
- review AI tool usage for data/security boundaries
- help organize GitHub docs so the project is easier to explain
- test the app like a security-minded user, not just a happy-path user

## The Way I Work

I work best when the goal is clear and the next step needs to be made practical.

My working style:

- ask what problem the project is solving
- write down the trust boundaries
- identify what can go wrong
- build or document one practical control
- test it
- capture evidence
- keep improving

That matches a consulting delivery process:

- Discovery: understand the current system and goals
- Strategy: define a roadmap and control path
- Implementation: build and document practical controls
- Optimization: keep testing, refining, and improving

## Short Pitch

> I can help on the AI security, DevSecOps, and documentation side. My capstone shows I can take an AI/RAG idea, scope it, build guardrails, test misuse cases, and turn the result into clear evidence and client-facing language. I am still learning, but I can contribute and I want to keep getting better.

## What I Should Keep Learning Next

- cloud AI services: Bedrock, SageMaker, Azure AI, Vertex AI
- Terraform/OpenTofu and policy-as-code
- stronger Kubernetes live validation
- MCP and agent tool security
- CI/CD security pipelines
- production logging and monitoring patterns
- real client communication and project delivery
