# Completed Build 001 — Sprint 1: RAG Control Harness

**Status:** COMPLETE
**Build ID:** CAP2-BUILD-S1
**Completed:** 2026-06-09
**Detail:** `sprint1-status.md` (full ticket + evidence tables, same folder)
**Gate 2 review:** passed (loops 1–3 BREAK-validated)

## What shipped

Eugene's deterministic RAG control harness — the controls that make the assistant
safe to run against real compliance documents.

| Ticket | Control | Result |
|---|---|---|
| BLD-001 | Input sanitization (prompt-injection rejection) | PASS |
| BLD-002 | Manifest-gated ingestion | PASS |
| BLD-003 | Secret/PHI scan before ingest | PASS |
| BLD-004 | Role-filtered retrieval | PASS |
| BLD-005 | Output filter (PHI/secret redaction) | PASS |
| BLD-006 | Structured audit log | PASS |
| BLD-007 | HITL flagging | PASS |
| BLD-008–014 | Evidence endpoints, chatbox path, HITL record, manifest ownership, evals, corpus alerting | PASS |
| BLD-025–029 | Query auth, rate limiting, audit hash-chain, Chroma auth/NetworkPolicy, platform static checks | PASS |

## Mini-loops closed

- Loop 1 (chatbox) — BUILD/BREAK/PROVE complete
- Loop 2 (HITL review record) — BUILD/BREAK/PROVE complete
- Loop 3 (RAG corpus integrity) — BUILD baseline + corpus-contamination BREAK complete

## Evidence

Under `Eugene-AI/evidence/` — see `sprint1-status.md` for the full file index.
