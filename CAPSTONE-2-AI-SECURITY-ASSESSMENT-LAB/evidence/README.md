# Evidence

This folder holds early Capstone 2 evidence artifacts and the original local scripts used to prove the first MedData Nexus baseline.

Most current Eugene evidence now lives in `../../Eugene-AI/evidence/`. Keep this folder because it shows the first assessment pattern: ingest a clean synthetic corpus, run a baseline retrieval check, and save dated artifacts before adversarial testing.

## Files

| File | Purpose |
| --- | --- |
| `ingest_meddata_to_chromadb.py` | Original local ingestion runner for the synthetic MedData Nexus corpus. |
| `baseline_retrieval_test.py` | Original baseline retrieval check over the clean corpus. |
| `meddata-ingest-clean-*.md` | Dated ingest evidence from the clean baseline. |
| `baseline-clean-baseline-*.json` | Dated retrieval evidence used to compare later RAG behavior. |

## Evidence Standard

Each evidence artifact should answer five questions:

- what was tested
- what command or workflow produced it
- what system state was used
- what result was observed
- what finding, control, or rubric item it supports

## Current Evidence Map

| Evidence Type | Primary Location |
| --- | --- |
| Early clean ingest and baseline retrieval | `evidence/` |
| Eugene API, chatbox, HITL, corpus, platform, and BREAK evidence | `../../Eugene-AI/evidence/` |
| PROVE summaries and framework mapping | `../CBBP-PLAN/PROVE/` |
| Client-facing interpretation | `../deliverables/` |

## Folder Rules

- Commit sanitized JSON, Markdown summaries, and reproducible evidence outputs.
- Do not commit `__pycache__/`, `.pytest_cache/`, ChromaDB database files, local logs with machine-specific noise, or any real client data.
- Use dated names for new scenario evidence, for example `2026-06-11-rag-direct-prompt-injection/`.
- Keep evidence factual. Interpretation belongs in `../CBBP-PLAN/PROVE/` and `../deliverables/`.
