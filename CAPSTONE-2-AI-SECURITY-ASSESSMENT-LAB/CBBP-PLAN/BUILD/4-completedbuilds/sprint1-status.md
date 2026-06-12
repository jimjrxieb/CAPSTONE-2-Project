# Sprint 1 BUILD Status — RAG Control Harness

> **Date:** 2026-06-09  
> **Source:** `COMPLY/comply-checklist.md` and `BUILD/comply-to-build-handoff.md`  
> **Evidence:** `Eugene-AI/evidence/sprint1-control-check-20260609T132156Z.json`, `Eugene-AI/evidence/ingest-20260609T132905Z.json`, `Eugene-AI/evidence/sprint1-live-rag-check-20260609T133039Z.json`, `Eugene-AI/evidence/chatbox-build-check-20260609T142228Z.json`, `Eugene-AI/evidence/hitl-review-check-20260609T145805Z.json`
> **BREAK evidence:** `Eugene-AI/evidence/break/chatbox-break-20260609T142715Z.json`, `Eugene-AI/evidence/break/hitl-review-bypass-20260609T182603Z.json`, `Eugene-AI/evidence/break/corpus-contamination-break-20260609T193306Z.json`, `Eugene-AI/evidence/break/unauthorized-retrieval-break-20260610T131529Z.json`, `Eugene-AI/evidence/break/fable-redteam-20260610T131340Z.json`

---

## Result

Sprint 1 local control checks: **PASS**

Sprint 1 live RAG checks: **PASS**

Loop 1 chatbox BREAK checks: **PASS**

Loop 1 PROVE package: **COMPLETE**

Loop 2 HITL review record check: **PASS**

Loop 2 HITL bypass BREAK checks: **PASS**

Loop 3 baseline RAG eval: **PASS**

Loop 3 Eugene deterministic draft-path helpfulness eval: **PASS**

Loop 3 corpus contamination BREAK: **PASS**

Loop 4 unauthorized retrieval BREAK: **FAIL — identity layer bypass confirmed; Sprint 2 remediation/validation scope**

Fable red-team run: **FAIL — 5/6 probes bypassed or exposed residual control gaps; Sprint 2 remediation/validation scope**

This means the deterministic control modules can execute locally without ChromaDB/Ollama:

- input sanitization
- role/category/classification filtering
- output redaction for PHI and secrets
- manifest-gated baseline ingest dry run
- unsafe corpus rejection dry run
- structured audit log write

This does **not** mean BREAK is complete. It means BUILD Sprint 1 has a working local control harness and a live ChromaDB/Ollama retrieval path with evidence.

---

## Ticket Status

| Ticket | Control | Status | Evidence |
|---|---|---|---|
| BLD-001 | Input sanitization | Implemented locally | 3 prompt-injection payloads rejected |
| BLD-002 | Manifest-gated ingestion | Implemented locally | Clean baseline dry run: 17 docs, 263 chunks, 0 rejected |
| BLD-003 | Secret/PHI scan | Implemented locally | Unsafe dry run rejected `unsanitized-incident-report.md` |
| BLD-004 | Role-filtered retrieval | Implemented locally | Role x category/classification matrix generated |
| BLD-005 | Output filter | Implemented locally | DOB and API key patterns redacted |
| BLD-006 | Structured audit log | Implemented locally | Audit ID `AUD-20260609T132156Z-473F27` written |
| BLD-007 | HITL flagging | Implemented and live-checked | API query returned `high_risk=true` and `review_required=true`; audit ID `AUD-20260609T133039Z-B2CE63` |
| BLD-008 | Evidence endpoints | Implemented and unit-tested | IT Security token gate tested; review trail endpoint added |
| BLD-009 | Chatbox client path | PASS | Missing role blocked; invalid role blocked; role boundaries shown; high-risk warning shown; source citations shown; injection rejected |
| BLD-010 | HITL approval record | PASS | Authenticated review decision recorded and linked to audit ID `AUD-20260609T145805Z-71C1C0` |
| BRK-013 | HITL bypass validation | PASS | 7/7 bypass attempts passed: missing token, wrong token, unknown audit ID, weak rationale, invalid decision, valid append, unreviewed distribution block |
| BLD-011 | Manifest ownership contract | PASS | Baseline manifest requires owner, approver, approval date, classification, and purpose |
| BLD-012 | Baseline RAG eval | PASS | Golden retrieval, role boundary, and prompt-injection checks passed against refreshed 284-chunk corpus |
| BLD-013 | Eugene usefulness eval | PASS | 8/8 business questions returned expected facts, citations, audit IDs, and review status |
| BRK-014 | Corpus contamination and RAG owner alerting | PASS | 5/5 attacks stopped and tagged to OWASP LLM, NIST AI RMF, and MITRE ATLAS |
| BRK-015 | Unauthorized retrieval identity-layer validation | FAIL | `Eugene-AI/evidence/break/unauthorized-retrieval-break-20260610T131529Z.json`; tier filter held, but unauthenticated role self-assertion was accepted |
| BRK-016 | Fable red-team control challenge | FAIL | `Eugene-AI/evidence/break/fable-redteam-20260610T131340Z.json`; 5 bypassed probes covering query auth, role spoofing, canned answers, sanitizer bypass, and token timing |
| BLD-014 | Corpus alert routing | PASS | RAG Corpus Owner registry resolved; local alert log written; Slack payload preview generated |
| BLD-025 | Query authentication | Implemented | `/query` role is derived from bearer token; request-body role no longer trusted |
| BLD-026 | Query rate limiting | Implemented locally | In-process per-token limiter keyed on authenticated user ID |
| BLD-027 | Audit hash-chain validation | Implemented locally | Audit entries include `prev_hash` and `entry_hash`; evidence endpoint validates on read |
| BLD-028 | Chroma server auth / network isolation | Static control evidence PASS | Server-mode retriever uses token-authenticated Chroma HTTP client; K8s Chroma deployment enables token auth; NetworkPolicy allows only API-to-Chroma ingress |
| BLD-029 | Platform static control check | PASS | `Eugene-AI/evidence/platform-control-check-20260610T150713Z.json` covers T-12, T-13, T-14, and T-16 static controls |

---

## Live RAG Evidence

| Check | Result | Evidence |
|---|---|---|
| Live ingest | PASS | 17 docs, 263 chunks inserted, 0 rejected |
| IT Security retrieval | PASS | CISO query retrieved authorized security/compliance/governance sources |
| Vendor Risk filtering | PASS | Security/HIPAA query returned 0 unauthorized chunks |
| Compliance filtering | PASS | PHI classification query did not return healthcare-privacy/security chunks |
| API query path | PASS | Response included 5 source citations, audit ID, high-risk HITL flag |
| Chatbox client path | PASS | UI client logic exercised through local API; audit ID `AUD-20260609T142228Z-0EBDA3`; answer is concise with citations |
| Chatbox BREAK | PASS | 6/6 cases passed: missing role, injection, high-risk warning, citations, API unavailable, no upload/history |
| Loop 1 PROVE | COMPLETE | `CBBP-PLAN/PROVE/loop1-chatbox-rag-prove.md` |
| HITL review record | PASS | Wrong token rejected; correct token accepted; review log written; review linked to existing audit ID |
| HITL bypass BREAK | PASS | `Eugene-AI/evidence/break/hitl-review-bypass-20260609T182603Z.json` |
| Manifest-backed ingest refresh | PASS | `Eugene-AI/evidence/ingest-20260609T190552Z.json`; 19 docs, 284 chunks, 0 manifest alerts |
| Baseline RAG eval | PASS | `Eugene-AI/evidence/baseline-rag-eval-20260609T190645Z.json` |
| Eugene deterministic draft-path helpfulness eval | PASS | `Eugene-AI/evidence/eugene-helpfulness-eval-20260609T192240Z.json`; validates retrieval, citations, audit IDs, review status, and deterministic draft shaping, not live model generation |
| Corpus contamination BREAK | PASS | `Eugene-AI/evidence/break/corpus-contamination-break-20260609T193306Z.json` |
| Corpus alert delivery | PASS | `Eugene-AI/evidence/corpus-alert-delivery-check-20260609T193758Z.json`; channel `#rag-corpus-alerts` |
| Loop 4 unauthorized retrieval BREAK | FAIL | `Eugene-AI/evidence/break/unauthorized-retrieval-break-20260610T131529Z.json`; identity layer failed before Sprint 2 remediation |
| Fable red-team run | FAIL | `Eugene-AI/evidence/break/fable-redteam-20260610T131340Z.json`; 5 bypassed probes, 1 informational finding |
| Platform static controls | PASS | `Eugene-AI/evidence/platform-control-check-20260610T150713Z.json`; deployed Chroma direct-access and rapid-query BREAK remain pending |

---

## Remaining Sprint 1 Work

| Item | Why It Remains |
|---|---|
| Live ChromaDB retrieval run | Complete for Sprint 1 |
| Live Ollama embedding/model path | Complete for embeddings using pinned `nomic-embed-text:v1`; generation model remains deterministic/local draft path until `EUGENE_MODE=ollama` evidence exists |
| API route replay evidence | Complete for query route, source citations, audit ID, and HITL flag |
| Chatbox client evidence | Complete for BUILD Loop 1 |
| HITL approval record sample | Complete for Loop 2 local control slice |

---

## DevSecOps Call

Mini CBBP Loop 1 BUILD/BREAK/PROVE is complete for the chatbox path.

Mini CBBP Loop 2 BUILD/BREAK/PROVE is complete for the authenticated HITL review-record path.

Mini CBBP Loop 3 BUILD baseline is complete: Eugene is scoped as the internal RAG assistant, manifest ownership metadata is enforced, the live corpus was refreshed, baseline RAG eval passed, and the deterministic draft path returned expected facts, citations, audit IDs, and review status for 8/8 business-use questions before poisoning tests.

Mini CBBP Loop 3 BREAK is complete for corpus contamination: unsigned, unapproved, poisoned, fake-secret, and PHI-like documents are blocked or rejected before embedding and alert the RAG Corpus Owner.

Local test execution should use capped runners by default:

```text
Eugene-AI/scripts/test-targeted.sh
Eugene-AI/scripts/test-full-capped.sh
```

Do not use raw `pytest tests -q` during normal mini-loop iteration. Use the targeted runner first, then the full capped runner only at checkpoint boundaries.

Loop 4 BREAK is complete as evidence, with identity-layer failures documented. Sprint 2 is the active engineering step: remediate/validate RBAC and platform controls, run deployed Chroma direct-access and rapid-query BREAK, gather live Ollama generation evidence, then enter CrewAI only after the T3 gate is satisfied.
