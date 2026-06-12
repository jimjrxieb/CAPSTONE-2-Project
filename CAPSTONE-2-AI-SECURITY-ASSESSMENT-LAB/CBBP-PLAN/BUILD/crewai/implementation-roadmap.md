# CrewAI Implementation Roadmap

## Purpose

Define when and how to implement CrewAI without skipping the core Eugene/RAG build.

## Current Decision

CrewAI is an orchestration layer. It should be implemented after the minimum evidence and Eugene interfaces exist.

An unwired CrewAI skeleton may exist in `Eugene-AI/src/agents/` for Loop 4+ planning. Sprint 1 does not depend on it, and the optional agent dependency set is isolated in `Eugene-AI/requirements-crew.txt`.

Do not start with CrewAI. Start with the deterministic pipeline:

1. synthetic corpus
2. ingestion
3. retrieval
4. Eugene assessment endpoint
5. evidence capture
6. BREAK scenario execution
7. PROVE packaging
8. CrewAI orchestration

## Build Sequence

| Step | Build Item | Required Before CrewAI? | Status |
|---|---|---:|---|
| 1 | Corpus manifest and fake-data corpus | Yes | Implemented |
| 2 | Chroma ingestion script | Yes | Implemented |
| 3 | Baseline retrieval test | Yes | Implemented |
| 4 | Evidence output directory/schema | Yes | Implemented |
| 5 | Eugene API/chatbox | Yes | Implemented for Sprint 1 |
| 6 | Evidence APIs or collector scripts | Yes | Implemented |
| 7 | BREAK scenario runner | Yes | Implemented as targeted runners |
| 8 | PROVE maps and risk register | Partial | Shells moved to `CBBP-PLAN/PROVE/`; final packaging polish remains |
| 9 | CrewAI task orchestration | No | Skeleton only; intentionally unwired |

Current gate: CrewAI should stay advisory and unwired until unauthorized retrieval, platform validation, and evidence packaging remain stable under repeat runs.

## Minimum Viable CrewAI

The first implementation should coordinate one RAG scenario end to end:

```text
Scenario: rag-direct-prompt-injection

1. Scenario Coordinator Agent loads scenario metadata.
2. Evidence Collector Agent checks required evidence sources exist.
3. Eugene Assessment Agent sends controlled context to Eugene.
4. Framework Mapper Agent drafts OWASP / AI RMF / 800-53 mappings.
5. Reviewer Gate Agent marks output pending human review.
6. Report Packager Agent drafts a risk-register row.
```

## Suggested Local Structure Later

Do not operationalize this code until the API/evidence interfaces exist.

```text
crewai-assessment/
  pyproject.toml
  src/
    crewai_assessment/
      agents.py
      tasks.py
      crews.py
      tools/
        evidence_api.py
        scenario_loader.py
        eugene_client.py
        prove_writer.py
      schemas/
        evidence_record.py
        finding_record.py
  tests/
```

## Implementation Guardrails

- CrewAI tools should be read-only except for approved output files under `evidence/` and `CBBP-PLAN/PROVE/`.
- CrewAI should not directly modify COMPLY source workpapers without human approval.
- CrewAI should not call external APIs unless the context is approved/sanitized.
- CrewAI should not run shell commands except through scoped, reviewed tools.
- CrewAI should not mark findings final.

## First Build Ticket

Build a dry-run CrewAI workflow that reads:

- `scenarios/rag-direct-prompt-injection.md`
- `CBBP-PLAN/COMPLY/meddata-ai-adoption-intake.md`
- `CBBP-PLAN/COMPLY/meddata-ai-risk-assessment.md`

And writes:

- `evidence/crewai/dry-run-rag-direct-prompt-injection.json`

The output must include:

- scenario ID
- expected control
- evidence required
- missing evidence
- draft finding status: `blocked_until_evidence_exists`
