# Target Architecture

This folder describes the **assessed target system**: the fictional MedData Nexus internal RAG environment.

It is not the Eugene source-code folder. Eugene lives in `../../Eugene-AI/` and acts as the local API/chatbox/assessment harness used to build, test, and explain the target system controls.

## Files

| File | Purpose |
|---|---|
| [architecture-overview.md](architecture-overview.md) | High-level MedData Nexus RAG system scope and ownership |
| [data-flow.md](data-flow.md) | Document ingestion, vector storage, retrieval, model response, and evidence flow |
| [trust-boundaries.md](trust-boundaries.md) | Boundaries where identity, data, model context, output, AI tooling, and human approval must be controlled |

## Mental Model

- **MedData Nexus** = fictional client / target environment
- **Internal RAG system** = the system being assessed
- **Eugene** = the local assistant, API, chatbox, and evidence harness built for the capstone
- **CBBP-PLAN/** = the assessment lifecycle workpapers

