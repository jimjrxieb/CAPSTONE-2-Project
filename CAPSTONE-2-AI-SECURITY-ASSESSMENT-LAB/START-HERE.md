# Start Here

This is the quick review path for Capstone 2.

## What This Is

Eugene is a local AI security assessment lab for a fictional healthcare SaaS client. The lab builds a RAG assistant, tests it against AI-specific risks, and packages the evidence like a client engagement.

Use this project to evaluate three things:

- Can the AI system be scoped clearly?
- Can the controls be built and tested?
- Can the results be explained to security leadership?

## 15-Minute Review Path

1. Read [README.md](README.md) for the project story and folder map.
2. Read [STATUS.md](STATUS.md) for what is complete and what is still phase 2.
3. Read [HIRING-MANAGER-NOTES.md](HIRING-MANAGER-NOTES.md) for the honest hiring signal.
4. Read [deliverables/01-executive-summary.md](deliverables/01-executive-summary.md) for the business recommendation.
5. Skim [CBBP-PLAN/COMPLY/README.md](CBBP-PLAN/COMPLY/README.md) for scope and governance.
6. Skim [CBBP-PLAN/BUILD/README.md](CBBP-PLAN/BUILD/README.md) for the controlled BUILD flow.
7. Skim [CBBP-PLAN/BUILD/build-readiness-rubric.md](CBBP-PLAN/BUILD/build-readiness-rubric.md) for the BUILD scorecard.
8. Skim [CBBP-PLAN/BREAK/meddata-break-validation.md](CBBP-PLAN/BREAK/meddata-break-validation.md) for test coverage.
9. Skim [CBBP-PLAN/PROVE/meddata-prove-package.md](CBBP-PLAN/PROVE/meddata-prove-package.md) for evidence and scale recommendation.
10. Skim [readiness-rubrics/guidepoint-readiness-rubric.md](readiness-rubrics/guidepoint-readiness-rubric.md) for the role-alignment scorecard.

## What To Look For

The strongest parts of the project are:

- CBBP lifecycle: COMPLY, BUILD, BREAK, PROVE
- synthetic client and fake corpus, no real sensitive data
- RAG trust-boundary mapping
- Codex and Claude Code governance
- CrewAI role and evidence-boundary planning
- Kubernetes/CKS-style platform hardening
- repeatable evidence runners in `../Eugene-AI/src/evidence/`
- client-facing deliverables in `deliverables/`

## Main Folders

| Folder | Review Question |
| --- | --- |
| `target-architecture/` | Is the system understandable? |
| `CBBP-PLAN/COMPLY/` | Is the AI use case scoped and governed? |
| `CBBP-PLAN/BUILD/` | Are COMPLY gaps translated into approved build work? |
| `CBBP-PLAN/BREAK/` | Are the claims tested against misuse? |
| `CBBP-PLAN/PROVE/` | Is there evidence for the recommendation? |
| `deliverables/` | Can this be explained to a client? |
| `evidence/` | What baseline proof exists, and where is current Eugene evidence? |
| `lessons/` | What did I learn and practice? |
| `readiness-rubrics/` | Is the project interview-ready? |
| `scenarios/` | What failure modes did I test? |
| `target-client/` | What synthetic client data drives the lab? |

## Short Defense

> I built Eugene to prove I can secure the workflow around AI, not just operate a model. The capstone defines AI boundaries, builds guardrails, tests RAG and coding assistant failure modes, and turns the evidence into a client-ready recommendation.
