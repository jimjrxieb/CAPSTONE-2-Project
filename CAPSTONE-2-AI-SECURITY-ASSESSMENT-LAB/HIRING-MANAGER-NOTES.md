# Hiring Manager Notes

This capstone is meant to show applied ability, judgment, and learning velocity. It is not presented as a replacement for a four-year degree or years of enterprise production ownership.

What it should show is that I can learn quickly, build working security artifacts, explain tradeoffs clearly, and keep improving under review.

## What This Project Demonstrates

### I Can Structure Ambiguous AI Security Work

AI security work can get vague fast. This project turns it into a process:

- define scope and owners
- identify data boundaries
- build guardrails
- test realistic failure modes
- capture evidence
- map findings to frameworks
- explain the result to decision makers

That is the point of CBBP: COMPLY, BUILD, BREAK, PROVE.

### I Can Build, Not Just Talk

The companion `Eugene-AI/` project includes:

- Python/FastAPI API routes
- Gradio chatbox
- RAG ingestion and retrieval code
- prompt-injection checks
- PHI and secret scanning
- role-filtered retrieval
- output filtering
- audit logging
- evidence runners
- tests
- Docker/Kubernetes manifests
- policy and CI checks

This is hands-on work, even though it is still a lab.

### I Understand Guardrails Around AI Dev Tools

The project includes a governed workflow for using Codex and Claude Code:

- approved context only
- no real client data
- no real credentials
- human review for security-sensitive changes
- AI-assisted PR label checks
- CODEOWNERS review
- dependency and platform gates
- evidence capture when the tool crosses a boundary

The message is simple: I am not trying to hide that I use AI tools. I am showing how to use them safely.

### I Can Think Like A Consultant

The capstone includes:

- client intake
- maturity assessment
- threat model
- findings report
- executive summary
- remediation roadmap
- operating model
- reviewer-ready explanation notes

That matters for GuidePoint-style work because the job is not only technical. The work has to help a client make a better decision.

## What I Would Not Overclaim

I would not claim this is a production AI platform.

I would not claim I am already a senior AI security engineer.

I would not claim this replaces formal education or enterprise experience.

The honest claim is stronger:

> I built a serious capstone lab to prove I can learn fast, build security controls, test AI/RAG failure modes, document evidence, and communicate risk in a client-ready way.

## Why This Matters For The GuidePoint Role

The AI Security Engineer role needs people who can work across:

- AppSec
- cloud/platform security
- AI/RAG security
- AI governance
- agentic coding assistant risk
- customer advisory
- evidence-backed reporting

This capstone touches each of those areas in a practical way.

The best signal is not perfection. The best signal is that the project is scoped, documented, tested, honest about limits, and easy to continue improving.

## Strong Interview Framing

> I know this does not replace a degree or years of production experience. What it does show is how I work: I take a real security problem, break it into scope, build, test, evidence, and communication. I used AI tools, but I also built guardrails around them. I am hungry to keep learning, and this is the kind of work I want to do every day.

## Best Proof Points To Show

- `START-HERE.md` for the quick review path
- `README.md` for the full capstone story
- `CBBP-PLAN/BUILD/ai-dev-assist-harness.md` for Codex and Claude Code governance
- `CBBP-PLAN/BUILD/eugene-build-harness.md` for Eugene build controls
- `CBBP-PLAN/BREAK/meddata-break-validation.md` for adversarial validation
- `CBBP-PLAN/PROVE/meddata-prove-package.md` for evidence packaging
- `deliverables/01-executive-summary.md` for business communication
- `../Eugene-AI/src/evidence/` for repeatable evidence runners
- `../Eugene-AI/deploy/k8s/` and `../Eugene-AI/deploy/policies/` for platform hardening
