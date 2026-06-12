# AI Adoption Readiness Rubric

Use this rubric to decide whether the client is ready to scale AI adoption.

Scoring:

- 0 = not started
- 1 = notes only
- 2 = working draft
- 3 = demo-ready
- 4 = interview-ready
- 5 = client-ready

## 1. COMPLY Readiness

| Item | Score | Evidence |
|---|---:|---|
| AI business outcome is defined | 0 | `templates/ai-adoption-intake-questionnaire.md` |
| approved AI tools are inventoried | 0 | `CBBP-PLAN/COMPLY/meddata-ai-inventory.md` |
| shadow AI risk is assessed | 0 | `CBBP-PLAN/COMPLY/meddata-ai-adoption-maturity.md` |
| data classes are mapped to allowed AI use | 0 | `target-architecture/data-flow.md` |
| human-only decisions are documented | 0 | `target-architecture/trust-boundaries.md` |

## 2. BUILD Readiness

| Item | Score | Evidence |
|---|---:|---|
| AI coding assistant guardrails are documented | 0 | `deliverables/04-ai-adoption-operating-model.md` |
| review gates are defined | 0 | `deliverables/04-ai-adoption-operating-model.md` |
| CI/security gates are defined | 0 | `deliverables/04-ai-adoption-operating-model.md` |
| RAG/vector DB controls are defined | 0 | `target-architecture/trust-boundaries.md` |
| logging and evidence paths are defined | 0 | `evidence/README.md` |

## 3. BREAK Readiness

| Item | Score | Evidence |
|---|---:|---|
| prompt injection tests exist | 0 | `scenarios/` |
| RAG poisoning tests exist | 0 | `scenarios/rag-poisoned-document.md` |
| sensitive data misuse test exists | 0 | `scenarios/rag-secrets-in-corpus.md` |
| AI-assisted PR bypass test exists | 0 | `scenarios/ai-assisted-pr-label-bypass.md` |
| unsafe dependency test exists | 0 | `scenarios/ai-unsafe-dependency-suggestion.md` |
| auth-sensitive generated code test exists | 0 | `scenarios/ai-generated-auth-change.md` |
| runtime drift test exists | 0 | `scenarios/ai-runtime-drift.md` |

## 4. PROVE Readiness

| Item | Score | Evidence |
|---|---:|---|
| AI adoption maturity rating is documented | 0 | `CBBP-PLAN/PROVE/ai-adoption-maturity-model.md` |
| findings are written in client language | 0 | `deliverables/02-client-findings-report.md` |
| operating model is written | 0 | `deliverables/04-ai-adoption-operating-model.md` |
| remediation roadmap includes 30/60/90-day actions | 0 | `deliverables/03-remediation-roadmap.md` |
| executive recommendation is clear | 0 | `deliverables/01-executive-summary.md` |

## Pass Criteria

The AI adoption track is ready when:

- COMPLY items average 4+.
- BUILD items average 4+.
- BREAK has at least five validated scenarios.
- PROVE contains a scale/no-scale recommendation.
- You can explain the adoption maturity and top three risks in two minutes.
