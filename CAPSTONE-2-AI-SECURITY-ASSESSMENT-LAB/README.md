# Capstone 2: Eugene AI Security Assessment Lab

Eugene is a local AI security assessment lab for a fictional healthcare SaaS client, MedData Nexus Health Systems. The project builds and assesses an internal RAG assistant, then packages the work like a client-facing AI security engagement.

The point of this capstone is not just to run a chatbot. The point is to show how an AI security engineer can scope the system, build guardrails, break the assumptions, prove the controls, and explain the result to engineering and security leadership.

## Reviewer Path

If you are reviewing this quickly, use this order:

1. [STATUS.md](STATUS.md) - current state, completed scope, and remaining phase-2 work
2. [HIRING-MANAGER-NOTES.md](HIRING-MANAGER-NOTES.md) - what this proves and what it does not overclaim
3. [target-client/meddata-nexus-health-systems.md](target-client/meddata-nexus-health-systems.md) - fictional client and business context
4. [target-architecture/architecture-overview.md](target-architecture/architecture-overview.md) - target RAG architecture
5. [CBBP-PLAN/COMPLY/README.md](CBBP-PLAN/COMPLY/README.md) - scope, owners, risk, and governance intake
6. [CBBP-PLAN/BUILD/README.md](CBBP-PLAN/BUILD/README.md) - COMPLY-to-BUILD receiver model and controlled build flow
7. [CBBP-PLAN/BUILD/build-readiness-rubric.md](CBBP-PLAN/BUILD/build-readiness-rubric.md) - BUILD readiness scorecard
8. [CBBP-PLAN/BREAK/meddata-break-validation.md](CBBP-PLAN/BREAK/meddata-break-validation.md) - adversarial validation plan
9. [CBBP-PLAN/PROVE/meddata-prove-package.md](CBBP-PLAN/PROVE/meddata-prove-package.md) - evidence package and recommendation
10. [deliverables/01-executive-summary.md](deliverables/01-executive-summary.md) - executive-level result
11. [readiness-rubrics/guidepoint-readiness-rubric.md](readiness-rubrics/guidepoint-readiness-rubric.md) - self-check against the GuidePoint AI security role

For the runnable implementation, see `../Eugene-AI/README.md`.

## One-Line Pitch

Capstone 2 builds Eugene as a local RAG assistant, tests it against AI-specific failure modes, maps findings to OWASP LLM, MITRE ATLAS, NIST AI RMF, and NIST 800-53, and produces client-ready security deliverables.

## What This Project Proves

This capstone demonstrates that I can:

- assess AI/RAG architecture and trust boundaries
- define AI adoption scope, owners, data classes, and human authority
- build a guarded local RAG workflow
- govern Codex and Claude Code as AI development assistants
- test prompt injection, corpus poisoning, unauthorized retrieval, sensitive output, and HITL bypass paths
- generate repeatable evidence instead of relying on claims
- map technical AI risk to security frameworks
- communicate risk through findings, roadmap, and executive summary

## CBBP Method

The project uses **CBBP: COMPLY, BUILD, BREAK, PROVE**.

| Phase | Purpose | Main Folder |
| --- | --- | --- |
| COMPLY | Define scope, ownership, data boundaries, approved tools, control requirements, and evidence expectations | `CBBP-PLAN/COMPLY/` |
| BUILD | Implement Eugene, RAG controls, AI dev-tool guardrails, CI checks, and platform hardening | `CBBP-PLAN/BUILD/` |
| BREAK | Test whether the controls survive misuse and realistic AI failure modes | `CBBP-PLAN/BREAK/`, `scenarios/` |
| PROVE | Package evidence, framework mapping, risk register, findings, and recommendations | `CBBP-PLAN/PROVE/`, `deliverables/` |

## Target System

The assessment target is Eugene, a RAG assistant over sensitive compliance, vendor-risk, legal, privacy, and security documents.

```text
Synthetic MedData Nexus corpus
  -> manifest-gated ingestion
  -> secret / PHI / prompt-injection scanning
  -> ChromaDB retrieval
  -> role-filtered context
  -> Eugene API and chatbox
  -> source-cited advisory response
  -> output filter + HITL flag + audit log
```

The broader adoption target includes AI coding assistant and analyst workflow governance:

```text
AI adoption intake
  -> maturity model and risk assessment
  -> approved tool and data boundaries
  -> Codex / Claude Code guardrails
  -> RAG and coding assistant BREAK tests
  -> PROVE package and scale / no-scale recommendation
```

## Folder Map

| Folder | What It Contains | Why It Matters |
| --- | --- | --- |
| `target-architecture/` | Architecture overview, data flow, trust boundaries | Shows how the system is scoped before testing |
| `CBBP-PLAN/COMPLY/` | Intake, inventory, maturity model, risk assessment, trust boundaries, threat model | Shows governance and scope discipline |
| `CBBP-PLAN/BUILD/` | COMPLY-to-BUILD handoff, BUILD rubric, Eugene harness, AI dev-tool authorization, RAG build, CKS platform plan, CrewAI design | Shows how findings become approved build work |
| `CBBP-PLAN/BREAK/` | RAG, coding assistant, and master BREAK validation plans | Shows how claims are tested |
| `CBBP-PLAN/PROVE/` | Risk register, framework maps, evidence packages, scale recommendation | Shows the proof package |
| `deliverables/` | Numbered executive summary, findings report, remediation roadmap, AI adoption operating model | Shows client-ready consulting output |
| `evidence/` | Early local ingest and baseline retrieval evidence scripts/results, with pointers to current Eugene evidence | Shows repeatable evidence patterns |
| `lessons/` | 12-part GuidePoint-style learning path | Shows what was learned and practiced |
| `readiness-rubrics/` | GuidePoint and AI adoption readiness scorecards | Shows where the capstone is strong and where phase-2 work remains |
| `scenarios/` | RAG and AI adoption abuse cases | Shows realistic AI security testing |
| `target-client/` | Synthetic client profile and fake data corpus | Makes the lab reproducible without real client data |
| `templates/` | Reusable AI intake, inventory, harness, risk, and mapping templates | Makes the method portable |
| `workflows/` | Future workflow notes for CrewAI and n8n | Shows orchestration direction |

## Lessons Learned

The `lessons/` folder is part of the capstone, not extra notes. It documents the working mindset I practiced while building the lab:

- ask better client intake questions before touching tools
- separate policy claims from runtime evidence
- treat model context, retrieval, tools, and outputs as separate trust boundaries
- make human approval explicit for security decisions
- write findings that include evidence, impact, owner, and remediation
- explain AI risk in business language without hiding technical detail
- use AI dev tools aggressively but inside a governed harness

Start with [lessons/README.md](lessons/README.md).

## Guardrails Built Into The Capstone

Eugene and the AI-assisted development workflow include:

- local-only Eugene boundary
- no real PHI, real credentials, or real client data
- manifest-gated corpus ingestion
- secret and PHI scanners
- prompt-injection scanner
- role-filtered retrieval
- output filtering
- high-risk HITL review flag
- structured audit logs
- AI-assisted PR label check
- CODEOWNERS review for sensitive code
- dependency pinning and SCA workflow
- Kubernetes hardening plan and policy checks

## Scenario Coverage

RAG scenarios:

- direct prompt injection
- poisoned document
- source leakage
- unauthorized retrieval
- secrets in corpus
- vector database access gap
- missing output filtering
- missing audit logging

AI adoption scenarios:

- AI-assisted PR label bypass
- unsafe dependency suggestion
- generated authentication change
- runtime drift

Scenario index: [scenarios/README.md](scenarios/README.md).

## Deliverables

The client-facing package lives in `deliverables/`:

- [01-executive-summary.md](deliverables/01-executive-summary.md)
- [02-client-findings-report.md](deliverables/02-client-findings-report.md)
- [03-remediation-roadmap.md](deliverables/03-remediation-roadmap.md)
- [04-ai-adoption-operating-model.md](deliverables/04-ai-adoption-operating-model.md)

These are written to show consulting judgment: what failed, why it matters, how to fix it, and what leadership should do next.

## Interview Language

> I built a repeatable AI security assessment lab called Eugene. It includes a synthetic healthcare SaaS client, a local RAG assistant, AI development assistant governance, BREAK scenarios, evidence capture, framework mapping, and client-ready deliverables. The main value is the operating model around the AI system: define the boundary, build controls, test misuse cases, and prove whether the client is ready to scale.

## Honest Limits

This is a capstone lab, not a production deployment.

Known phase-2 items:

- deployed-cluster live validation for ChromaDB direct-access rejection
- identity provider integration instead of static lab tokens
- optional generation-model quality evaluation after deterministic evidence mode
- cloud AI service extensions such as Bedrock, SageMaker, Azure AI, or Vertex AI under a new COMPLY boundary
- more complete n8n workflow automation
