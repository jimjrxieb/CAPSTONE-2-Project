# Model Decision Record — Eugene Local Inference

> **Date:** 2026-06-09  
> **Decision owner:** jimjrxieb  
> **System:** CAP2-AI-001 Eugene assessment lab  
> **Status:** Accepted for BUILD

---

## Decision

Use `llama3.2:3b` as Eugene's local assessment model.

Use `nomic-embed-text:v1` for embeddings. Do not use `:latest` for generation or embeddings in evidence-producing runs.

---

## Rationale

Eugene is intended to process assessment context that external API-based tools should not touch. The model must run locally so retrieved context, synthetic client evidence, and assessment drafts stay on the server.

`llama3.2:3b` is preferred over `llama3.2:1b` for this harness because Eugene needs stronger instruction following and summarization for:

- RAG-grounded advisory drafts
- structured finding output
- framework mapping drafts
- remediation language
- evidence-gap identification

`llama3.2:1b` remains acceptable for later narrow utility tasks such as classification, label extraction, or quick risk flagging, but it is not the default assessment model.

---

## Security Boundary

Codex and Claude Code may build and test the harness using approved repository context.

Eugene local inference handles sensitive assessment context that should not leave the host.

External LLM APIs are out of scope for Eugene. Adding one later requires a new COMPLY boundary, CISO approval, and renewed BREAK evidence.

---

## Re-Test Rule

Any change to `OLLAMA_MODEL`, `OLLAMA_EMBED_MODEL`, prompt template, retrieval filter, or output parser requires:

1. Sprint 1 control check re-run.
2. Full corpus re-ingest if the embedding model changed.
3. Baseline RAG eval re-run.
4. Live RAG check re-run.
5. BREAK tests 1 through 5 re-run before PROVE claims are updated.

## Generation Mode

Current Sprint 1 evidence uses `EUGENE_MODE=deterministic`: live retrieval and source grounding are exercised, but final answer text is drafted by a deterministic response shaper. Generation quality claims require a later run with `EUGENE_MODE=ollama`, `llama3.2:3b` reachable, and a generation-specific eval artifact.
