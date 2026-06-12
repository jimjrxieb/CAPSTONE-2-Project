# Data Flow — MedData Nexus Internal RAG System

> Last updated: 2026-06-08
> Scope: baseline COMPLY-phase target architecture. Current Eugene implementation evidence lives in `../../Eugene-AI/evidence/` and `../CBBP-PLAN/BUILD/sprint1-status.md`.

## Ingestion Path (corpus → vector DB)

```
1. Document source
   Approved Internal/Confidential documents: policies, compliance evidence,
   SOC 2 summaries, HIPAA assessment records, vendor-risk docs, legal/BAA
   templates, security findings, sanitized incident records.
   Prohibited: PHI/ePHI, credentials, secrets, unapproved or poisoned docs.

2. Ingestion pipeline
   Parses and validates documents before processing.
   REQUIRED: PHI pattern scan + secret scan before ingest.
   REQUIRED: corpus manifest entry + data owner sign-off before ingest.

3. Chunking
   Documents split into chunks with configurable overlap.
   Chunk size affects retrieval accuracy — oversized chunks include noise;
   undersized chunks lose context.

4. Metadata labeling
   Each chunk tagged with: source document name, document tier (Internal/
   Confidential), corpus category, owner, ingest timestamp.
   REQUIRED: No PII in metadata fields (e.g., no real author names or
   system paths that reveal internal structure).

5. Embedding
   Chunks converted to vector embeddings via embedding model.
   Embeddings stored with metadata in ChromaDB collection.

6. Vector DB storage (ChromaDB)
   Single collection in current pilot.
   REQUIRED: per-role retrieval control and post-retrieval filtering.
```

## Retrieval and Inference Path (user query → response)

```
7. User query
   Untrusted natural language input from an authenticated pilot user.
   REQUIRED: input sanitization for prompt injection.
   REQUIRED: user role verified and passed to retrieval layer.

8. Retrieval (ChromaDB query)
   Embedding of user query compared to stored chunk embeddings.
   Top-k matching chunks returned with metadata.
   REQUIRED: query filtered by user role → authorized
   document tiers only.

9. Prompt construction
   System instructions + retrieved chunks + user query assembled into
   final prompt.
   REQUIRED: system prompt must be isolated — user cannot override or
   extract it via query manipulation.
   REQUIRED: retrieved chunks sanitized before insertion into prompt.

10. Model inference (LLM / Eugene)
    Local model (Ollama) or approved external API (Claude Haiku, sanitized
    context only).
    External API: only approved/sanitized context exits the internal boundary.
    No raw corpus documents to external provider.

11. Output validation
    REQUIRED: output filter inspects response for PHI,
    secrets, internal file paths, and prohibited content before delivery.
    REQUIRED: response labeled as AI-generated summary; source documents
    cited with corpus manifest reference.

12. Logging and evidence capture
    REQUIRED: structured log entry per interaction:
      - user_id and role
      - query text
      - retrieved chunk IDs and source references
      - model response (or hash)
      - tool/API path used
      - human review decision and reviewer identity (for high-risk outputs)
      - timestamp (ISO 8601)
```

## Data Classification at Each Step

| Step | Data Present | Sensitive? | Current Control | Gap |
|---|---|---|---|---|
| Document source | Internal/Confidential docs | Yes | Corpus manifest | Ingestion validation must stay enforced |
| Chunking | Same | Yes | None | Chunk boundaries can split sensitive context incorrectly |
| Metadata | Source references | Possibly | Not defined | PII in metadata not ruled out |
| Vector DB | Embeddings + chunk text | Yes | Role-scoped retrieval in Eugene build | Direct DB access still needs live platform proof |
| User query | Untrusted input | No (query only) | Sanitizer in Eugene build | Regex/blocklist is defense-in-depth, not sole control |
| Retrieval result | Confidential chunk text | Yes | Role filter + post-retrieval tier filter | Must remain covered by unauthorized retrieval tests |
| Prompt | System instructions + chunks | Yes | Deterministic draft path for Sprint 1 | Live generation mode needs separate evidence |
| Model response | AI-generated summary | Yes (can reflect corpus) | Output filter + HITL flag | High-risk decisions still require human approval |
| Logs | Query + response | Yes | Structured audit evidence | Packaging-time validation/hash-chain hardening remains future work |
