# Capstone As The Example

This is the real example: **Capstone 2 — Eugene AI Security Assessment Lab**.

The fictional/client-safe target is MedData Nexus, a healthcare SaaS company adopting an internal AI/RAG assistant. The assistant is **Eugene**. The capstone shows how I would approach an AI security consulting engagement: understand the system, define the risk, build controls, test failure modes, and package evidence.

## The Client Problem

MedData Nexus wants to use an internal AI assistant to help employees search policies, compliance records, security notes, vendor-risk context, and AI governance docs.

The risk is obvious:

- the assistant could expose PHI, secrets, legal records, or security details to the wrong role
- prompt injection could try to override the system instructions
- poisoned documents could enter the corpus
- AI-generated output could be treated as final without human review
- the vector database or API could become a new data-exposure path
- AI coding tools could introduce changes without review

That is exactly the kind of problem real clients will have as they add AI into production workflows.

## What I Built

I built Eugene as a local AI/RAG security lab:

- FastAPI query API
- Gradio chatbox
- ChromaDB-backed retrieval
- role-based retrieval boundaries
- bearer-token role binding
- input sanitization
- secret and PHI scanning on ingest
- output filtering
- human-in-the-loop review flags
- structured audit evidence
- Kubernetes / CKS-style platform hardening artifacts
- GitHub guardrails for AI-assisted development
- CrewAI design docs with strict human-review boundaries
- BREAK runners for prompt injection, HITL bypass, corpus contamination, unauthorized retrieval, and platform controls

Main code path:

- `../Eugene-AI/`
- `../CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BUILD/`
- `../CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BREAK/`
- `../CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/PROVE/`

## How It Maps To A Consulting Engagement

| Engagement Stage | What I Did In The Capstone | Output |
|---|---|---|
| Discovery | Scoped the AI/RAG workflow, data types, users, trust boundaries, and risks | AI adoption intake, system inventory, threat model |
| Strategy | Turned risks into a control roadmap | COMPLY findings, build backlog, CBBP plan |
| Implementation | Built Eugene and its guardrails | FastAPI/RAG/chatbox code, CI gates, CODEOWNERS, K8s/policy artifacts |
| Optimization | Broke and retested the controls, then packaged evidence | BREAK runners, evidence JSON, status docs, reviewer notes |

## Why This Matters

This capstone touches the same lanes AI security consulting teams care about:

- **AI Integration:** RAG assistant, model boundary, safe human handoff
- **Cybersecurity:** prompt injection, poisoning, unauthorized retrieval, secret/PHI checks
- **DevSecOps:** CI guardrails, SCA, CODEOWNERS, AI-assisted PR controls
- **Platform Engineering:** Docker/Kubernetes hardening, NetworkPolicy, Kyverno-style policy checks
- **Cloud Architecture:** identity, logging, least privilege, private service exposure patterns
- **Compliance & Governance:** NIST AI RMF, OWASP LLM, NIST 800-53-style evidence, POA&M language

The strongest part is not that Eugene is perfect. It is that I built a repeatable loop:

1. Define what should be true.
2. Build the control.
3. Try to break it.
4. Capture evidence.
5. Say honestly what still needs work.

That is useful on real client work.

## What Is Honest / Still Learning

I would not present this as senior production experience.

I would present it as proof that I can:

- reason about AI security boundaries
- build practical controls
- write evidence-driven docs
- use AI dev tools with guardrails
- find and fix gaps instead of hiding them
- explain technical work in client language

Known limits:

- Eugene currently uses a deterministic draft path unless live local generation evidence is added.
- Platform checks are strong local/static proof, but live deployed-cluster proof is the next hardening step.
- CrewAI is intentionally skeleton/unwired until deterministic controls stay stable.
- I am still building deeper production cloud AI experience.

## What I Would Say To Constant

> The capstone is the example. I built Eugene, an AI/RAG security lab, and ran it through a consulting-style loop: discovery, strategy, implementation, validation, and evidence. I can help with AI security, DevSecOps, validation checks, documentation, and turning messy technical work into client-ready deliverables. I am still early, but this is the kind of work I want to keep doing.
