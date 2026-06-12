# RAG Pipeline Build Plan

## Purpose

Build a repeatable RAG pipeline for the Eugene Capstone 2 assessment lab.

This is not just a one-off local demo. The goal is to create a build path another engineer can follow with the same synthetic data and get the same assessment workflow, evidence, and failure modes.

## Build Target

```text
target-client/fake-data/
  -> corpus manifest
  -> document validation
  -> chunking
  -> metadata labeling
  -> embeddings
  -> vector database
  -> retrieval API
  -> Eugene assessment API/chatbox
  -> evidence capture
```

## Repeatability Requirements

- Corpus membership is defined in `target-client/fake-data/corpus-manifest.md`.
- Clean baseline, poisoned, unsafe, and sanitized recovery states are separate.
- Ingestion is scriptable from repo files, not manual copy/paste.
- Every chunk keeps source path, document name, category, classification, and scenario flags.
- Golden-question retrieval tests prove the baseline collection works.
- Evidence outputs are written to `evidence/`.
- A new engineer can rebuild the baseline from scratch with documented commands.

## BUILD Tasks

| Task | Output | Status |
|---|---|---|
| Define synthetic corpus | `target-client/fake-data/corpus-manifest.md` | Implemented |
| Create ingestion script | `Eugene-AI/src/rag/pipeline.py` | Implemented |
| Create baseline retrieval test | `Eugene-AI/src/evidence/baseline_eval_runner.py` | Implemented |
| Build Eugene API | `Eugene-AI/src/api/` | Implemented |
| Build Eugene chatbox | `Eugene-AI/src/chatbox/app.py` | Implemented |
| Add retrieval endpoint | `Eugene-AI/src/api/routes/query.py` | Implemented |
| Add assessment endpoint | Query route returns advisory deterministic assessment draft; dedicated scenario endpoint deferred | Implemented for Sprint 1 scope |
| Add logging/evidence capture | `Eugene-AI/src/audit/logger.py`, `Eugene-AI/evidence/` | Implemented |
| Add poisoned/unsafe scenario toggles | `Eugene-AI/src/evidence/corpus_contamination_break_runner.py` | Implemented |
| Add CKS/platform build plan | `CBBP-PLAN/BUILD/cks-platform-build-plan.md` | Implemented as reviewable plan and static platform check |

## COMPLY Receiver Backlog

BUILD consumes `CBBP-PLAN/COMPLY/comply-checklist.md` through:

- `comply-to-build-handoff.md` — sprint backlog and acceptance criteria
- `eugene-build-harness.md` — Eugene API/RAG implementation spec
- `cks-platform-build-plan.md` — Kubernetes/CKS platform hardening artifacts
- `ai-dev-assist-harness.md` — AI-assisted engineering controls

## Baseline Commands

Local commands from `Eugene-AI/`:

```bash
python3 -m src.rag.pipeline
python3 -m src.evidence.baseline_eval_runner
python3 -m src.evidence.eugene_helpfulness_eval
```

Scenario commands:

```bash
python3 -m src.evidence.chatbox_break_runner
python3 -m src.evidence.hitl_review_break_runner
python3 -m src.evidence.corpus_contamination_break_runner
python3 -m src.evidence.unauthorized_retrieval_break_runner
python3 -m src.evidence.platform_control_check
```

Evidence already captured includes Sprint 1 control checks, live RAG checks, chatbox BREAK, HITL bypass BREAK, corpus contamination BREAK, unauthorized retrieval BREAK, and platform static control checks under `Eugene-AI/evidence/`.

## Model Boundary

Eugene is the Capstone 2 local assessment assistant. It may draft findings, mappings, and remediation language, but it does not own final judgment.

External LLM APIs are out of scope for Eugene. Any future external model path requires a new COMPLY boundary and renewed BREAK evidence.

Codex and Claude Code are build assistants under `CBBP-PLAN/BUILD/ai-dev-assist-harness.md`.

## Definition Of Done

The RAG pipeline is BUILD-ready when:

- a clean baseline corpus can be rebuilt from repo data
- golden-question retrieval passes at an acceptable level
- poisoned and unsafe variants are reproducible
- Eugene can query retrieved context through a local API/chatbox
- prompts, retrieved chunks, outputs, and reviewer decisions are captured as evidence
- the build steps are clear enough for another engineer to reproduce

Current limitation: final answer text is generated through Eugene's deterministic draft path unless `EUGENE_MODE=ollama` is explicitly wired and a generation-specific evidence run is captured.
