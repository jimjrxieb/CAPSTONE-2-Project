# AI Security Scenarios

Each scenario should produce:

- test objective
- attack path
- expected failure mode
- evidence collected
- Eugene finding
- OWASP LLM mapping
- MITRE ATLAS mapping
- NIST AI RMF mapping
- NIST 800-53 mapping
- remediation
- validation step
- reviewer-ready explanation in engineering and CISO language

## Scenario List

### RAG Scenarios

1. Direct prompt injection.
2. Poisoned document.
3. Source leakage.
4. Unauthorized retrieval.
5. Secrets in corpus.
6. Vector DB access gap.
7. Missing output filtering.
8. Missing audit logging.

### AI Adoption Scenarios

1. AI-assisted PR label bypass.
2. AI unsafe dependency suggestion.
3. AI-generated authentication change.
4. AI runtime drift.

## First Slice Rule

Complete `rag-direct-prompt-injection.md` to client-grade first.

Before expanding all eight scenarios, the prompt-injection slice should include real evidence, framework mapping, remediation, validation, and reviewer-ready answers:

- why Eugene belongs in the assessment workflow despite known model limits
- why the lab finding transfers to client assessment procedure
- what the finding means to a CISO in one sentence

## Adoption Slice Rule

Complete `ai-assisted-pr-label-bypass.md` and `ai-runtime-drift.md` before calling the adoption track interview-ready.

Those two scenarios prove the consulting point:

- AI adoption is not secure because a policy exists.
- AI adoption is secure when the workflow catches bypasses and runtime drift.
