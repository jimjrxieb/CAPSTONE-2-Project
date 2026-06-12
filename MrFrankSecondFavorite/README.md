# MrFrankSecondFavorite

Quick material for showing my Capstone 2 / Eugene work to GuidePoint-style AI security reviewers, mentors, and trusted side-project collaborators.

Plain English: **the capstone is the example.** Eugene is the system I built. CBBP is the method I used to scope it, build it, break it, and prove it. This folder is the TLDR of that work.

## Read First

1. **[capstone-as-engagement.md](capstone-as-engagement.md)** — start here. This explains Eugene / Capstone 2 as the real worked example.
2. **[ai-sec.md](ai-sec.md)** - maps the capstone to AI security, DevSecOps, platform, cloud, and governance skills.
3. **[4CL/](4CL/)** — side-startup delivery lens: how the capstone maps to Discovery → Strategy → Implementation → Optimization.
4. [mentor-quick-guide.md](mentor-quick-guide.md) - broader walkthrough of my AI security capstone work.
5. [4CL/01-intake-questionnaire.md](4CL/01-intake-questionnaire.md) through [4CL/06-client-report.md](4CL/06-client-report.md) - reusable templates derived from the capstone flow.

## Short Version

I built **Eugene**, a local AI/RAG security assessment lab for a fictional healthcare SaaS client. The point was not just to make a chatbot. The point was to show the full consulting loop:

- scope the AI workflow
- document trust boundaries
- build practical guardrails
- test failure modes
- capture evidence
- explain the risk clearly

The strongest fit is AI security, RAG security, DevSecOps, platform engineering, cloud security patterns, and compliance/governance support. The AI-security piece — OWASP LLM, NIST AI RMF, red-teaming — is the core signal for GuidePoint and senior AI security reviewers.

## What Reviewers Should Look At

The main proof is the capstone:

- `../CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/README.md` - reviewer path for the capstone.
- `../CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BUILD/` - Eugene build plan, guardrails, evidence status, CrewAI boundaries.
- `../Eugene-AI/` - FastAPI/RAG/chatbox implementation, guardrails, tests, evidence runners.
- `capstone-as-engagement.md` - the same work translated into a clean consulting story.
- `ai-sec.md` - skill map for AI security / GuidePoint-style review.
- `4CL/01-intake-questionnaire.md` through `4CL/06-client-report.md` - reusable blank templates that came from the capstone process.
- `4CL/07-agent-build-plan.md` - future path for GP-CONSULTING as a supervised agentic support bench.

## Where GP-COPILOT Fits

This folder is the TLDR. The bigger `GP-COPILOT/` workspace is the operating system behind it:

- **Capstone 2 / Eugene** is the proof that I can scope, build, test, and explain an AI security workflow.
- **GP-CONSULTING** is the agentic support bench: COMPLY, BUILD, BREAK, and PROVE helpers that organize research, controls, tests, evidence, and reporting under human review.
- **Trusted side-project / client work** brings real client problems.
- **My role** is to take a scoped problem, clear the work package, produce evidence, and hand back something a client or senior engineer can review.

Casual version: the client gets the gates, I go in as Jinwoo, and GP-CONSULTING is the shadow army helping me move faster. Professional version: I use governed AI agents as supervised delivery assistants, not autonomous decision-makers.

## GuidePoint Angle

This does not replace a four-year degree, and I do not need to pretend it does. The point is different: the capstone gives a hiring manager evidence that I can do the work cycle.

GuidePoint's AI Security lane needs people who can help clients safely design, assess, deploy, govern, and operate AI systems. Eugene shows applied reps in that direction:

- AI/RAG security architecture
- vector database and retrieval trust boundaries
- prompt injection and corpus poisoning testing
- AI-assisted developer guardrails for Codex and Claude Code
- human-in-the-loop review
- audit evidence and client-ready reporting
- OWASP LLM, NIST AI RMF, NIST 800-53-style mapping
- Python/FastAPI automation and evidence runners
- Kubernetes/CKS-style hardening patterns

The honest story is: I am still early, but I am building real projects that force me to learn the same skills senior AI security, MLOps, AppSec, and cloud security engineers use.

## Best Conversation Starter

> I built Eugene as an AI/RAG security capstone: scoped the system, built guardrails, tested failure modes, and packaged evidence. I can help on AI security, DevSecOps, validation, and client-ready documentation. I'm still learning, but this shows how I think and how I execute.
