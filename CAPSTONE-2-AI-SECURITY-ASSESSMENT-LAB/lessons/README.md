# GuidePoint Mindset Lessons

These lessons document what I practiced while building Capstone 2. They are written for a GuidePoint-style AI Security / AI Adoption consultant: scope first, build second, break claims, prove with evidence, and explain risk clearly.

## How To Read This Folder

Use the lessons as the learning track behind the capstone:

1. Read the lesson.
2. Answer the client-facing questions.
3. Apply the idea to one capstone artifact.
4. Capture evidence or mark the gap honestly.
5. Defend the result in business language.

Reference files:

- [Lesson Glossary](lesson-glossary.md)
- [GuidePoint AI Security Engineer Role Map](guidepoint-ai-security-engineer-role-map.md)

## Lesson Index

| # | Lesson | What It Trained | Capstone Output |
| --- | --- | --- | --- |
| 01 | [GuidePoint Consultant Mindset](01-guidepoint-consultant-mindset.md) | Client-first advisory thinking | Interview and findings language |
| 02 | [Client Intake And Scope](02-client-intake-and-scope.md) | Asking the right scope questions | `CBBP-PLAN/COMPLY/meddata-ai-adoption-intake.md` |
| 03 | [AI Adoption Maturity](03-ai-adoption-maturity.md) | Rating readiness to scale AI | `CBBP-PLAN/COMPLY/meddata-ai-adoption-maturity.md` |
| 04 | [AI Security Architecture](04-ai-security-architecture.md) | Data flow and trust boundaries | `target-architecture/`, `CBBP-PLAN/COMPLY/meddata-trust-boundaries.md` |
| 05 | [RAG And Data Security](05-rag-and-data-security.md) | Corpus, retrieval, and sensitive data risk | `CBBP-PLAN/COMPLY/meddata-rag-corpus-intake.md`, RAG scenarios |
| 06 | [Agentic Coding Assistant Governance](06-agentic-coding-assistant-governance.md) | Codex/Claude/Copilot control model | `CBBP-PLAN/BUILD/ai-dev-assist-harness.md` |
| 07 | [Threat Modeling AI Workflows](07-threat-modeling-ai-workflows.md) | AI failure paths and framework mapping | `CBBP-PLAN/COMPLY/meddata-threat-model.md` |
| 08 | [BREAK Validation](08-break-validation.md) | Testing whether controls actually hold | `CBBP-PLAN/BREAK/meddata-break-validation.md` |
| 09 | [Evidence And PROVE](09-evidence-and-prove.md) | Evidence-backed findings and recommendations | `CBBP-PLAN/PROVE/`, `deliverables/` |
| 10 | [Executive Advisory](10-executive-advisory.md) | Explaining risk to leaders | `deliverables/01-executive-summary.md`, `deliverables/03-remediation-roadmap.md` |
| 11 | [Building The AI Harness](11-building-the-ai-harness.md) | Translating governance into controls | `CBBP-PLAN/BUILD/eugene-build-harness.md` |
| 12 | [Harnessing AI Dev Tools As An Engineering Team](12-harnessing-ai-dev-tools-as-engineering-team.md) | Safe team use of AI dev tools | `CBBP-PLAN/COMPLY/meddata-ai-engineering-crew.md` |

## What I Learned

- AI security starts with ownership, data boundaries, and human authority.
- A RAG system must treat corpus content as untrusted input, not trusted instruction.
- Coding assistants need the same kind of governance as other production-impacting engineering tools.
- A policy is not enough; the workflow has to catch bypasses and drift.
- Evidence matters more than claims. If the control is not tested, it is not proven.
- A good AI security finding needs a business impact, technical cause, owner, remediation, and validation path.
- Framework mapping is useful only when it is specific and justified.

## Daily North Star

> My job is to turn AI adoption from scattered experiments into governed, tested, evidence-backed workflows.

## Completion Status

All 12 lessons are complete and mapped to capstone artifacts.

The learning track supports the final capstone story:

- COMPLY workpapers define scope and risk.
- BUILD artifacts translate those rules into controls.
- BREAK artifacts test realistic AI failure modes.
- PROVE artifacts package evidence and recommendations.
