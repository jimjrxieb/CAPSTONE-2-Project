# For ConstantLaunch

This folder shows how my **Capstone 2 Eugene AI Security Assessment Lab** maps to ConstantLaunch delivery.

The capstone is the example. Eugene is the system. The numbered files are the clean client-facing model: intake, gap analysis, roadmap, build log, validation, report, and a future agent build path.

---

## The Simple Fit

ConstantLaunch runs engagements as **Discovery → Strategy → Implementation → Optimization**. Eugene maps cleanly to that process:

- **Discovery:** scoped an internal AI/RAG assistant, users, data, risks, and trust boundaries.
- **Strategy:** mapped findings into a control roadmap.
- **Implementation:** built the FastAPI/RAG/chatbox system plus guardrails, CI gates, and platform artifacts.
- **Optimization:** ran validation tests, captured evidence, and documented what still needs hardening.

That is the value: I can take an AI/security problem from messy idea to built control to evidence-backed explanation.

## The Delivery Model

The files in this folder are the lightweight version of the capstone workflow:

| File | ConstantLaunch Step | What it does |
|---|---|---|
| [01-intake-questionnaire.md](01-intake-questionnaire.md) | Discovery | Turns the first client conversation into scoped facts, systems, data, owners, and constraints |
| [02-gap-analysis.md](02-gap-analysis.md) | Discovery / Strategy | Converts current state into risks, gaps, control needs, and evidence questions |
| [03-roadmap.md](03-roadmap.md) | Strategy | Prioritizes the work into waves with owners, dates, and acceptance checks |
| [04-build-log.md](04-build-log.md) | Implementation | Records what changed, why it changed, and what evidence proves it exists |
| [05-validation-checklist.md](05-validation-checklist.md) | Optimization | Tests whether the controls actually work instead of assuming they work |
| [06-client-report.md](06-client-report.md) | Optimization | Packages findings, residual risk, POA&M, and executive language |
| [07-agent-build-plan.md](07-agent-build-plan.md) | Future internal enablement | Shows how GP-CONSULTING could become a supervised delivery assistant |

This is the capstone plan translated into ConstantLaunch language: understand the system, decide the control path, build the controls, test them, and package the proof.

Under the hood, these files map back to `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/`: the full capstone workpapers. This folder is the cleaner ConstantLaunch version.

## How GP-CONSULTING Takes Load Off Constant

ConstantLaunch brings the client and the gate: the real business problem, timeline, and outcome the client needs.

I bring the working method and the GP-CONSULTING support bench:

| ConstantLaunch need | GP-CONSULTING assist | Human-owned result |
|---|---|---|
| Intake and scope | Drafts discovery questions, data boundaries, system inventory, stakeholder map | Consultant-approved scope |
| Gap analysis | Maps risks to controls, frameworks, and evidence needs | Reviewed findings |
| Roadmap | Turns findings into build tasks, owners, acceptance criteria, and timeline | Prioritized delivery plan |
| Build support | Drafts guardrails, CI gates, policy notes, docs, and implementation checklists | Engineer-reviewed changes |
| Validation | Drafts safe test plans and evidence runners; active testing remains human-approved | Tested controls |
| Reporting | Drafts executive summary, POA&M, client report, and handoff notes | Client-ready deliverable |

The agents do not replace Constant's judgment. They reduce blank-page work, keep evidence attached, and help one motivated engineer move faster without losing human review.

Casual internal metaphor: Constant finds the gates, I go in as Jinwoo, and GP-CONSULTING is the shadow army. Professional version: supervised AI agents help draft, organize, and validate delivery artifacts while the human owns scope, risk, testing, and final signoff.

## Why this is useful to ConstantLaunch

It maps to all six service lanes:

| ConstantLaunch Lane | What this framework brings |
|---|---|
| **AI Integration** | RAG/AI workflow scoping, trust-boundary docs, safe AI↔human handoff |
| **Cybersecurity** | AI/RAG security reviews, prompt-injection & poisoning tests, findings writeups |
| **DevSecOps** | CI security gates, SCA, secret scanning, AI-assisted-dev governance (CODEOWNERS, PR review gates) |
| **Platform Engineering** | Container/K8s hardening, NetworkPolicy, least-privilege, control evidence |
| **Cloud Architecture** | Cloud AI security requirements: identity, data boundaries, logging, least privilege, output validation |
| **Compliance & Governance** | SOC 2 / HIPAA / NIST mapping, gap analysis, POA&M, exec summaries, remediation roadmaps |

**The standout:** the AI-security layer is not theoretical. Eugene includes prompt-injection tests, corpus contamination tests, unauthorized retrieval checks, human-review gates, audit evidence, and AI-assisted-dev guardrails.

---

## What's in this folder

Start one level up with [../README.md](../README.md), then read [../capstone-as-engagement.md](../capstone-as-engagement.md). This folder is the ConstantLaunch delivery translation and reusable template path.

---

## The pitch

> I built Eugene as an AI/RAG security capstone and ran it like a real engagement: discovery, control strategy, implementation, validation, and evidence. It maps directly to ConstantLaunch's AI Integration, Cybersecurity, DevSecOps, Platform Engineering, Cloud Architecture, and Compliance/Governance lanes. I am still early, but this shows how I think, build, test, and explain the work.

---

*The full capstone uses a deeper internal method. This folder keeps the client-facing version simple: Discovery → Strategy → Implementation → Optimization.*
