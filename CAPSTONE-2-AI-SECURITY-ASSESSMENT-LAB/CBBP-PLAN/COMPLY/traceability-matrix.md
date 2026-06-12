# COMPLY Traceability Matrix

> **Client:** MedData Nexus Health Systems  
> **System:** MDN-AI-001 Eugene Internal RAG Assistant  
> **Purpose:** Reconcile COMPLY threats, client findings, governance findings, BUILD controls, BREAK tests, and PROVE evidence so DevSecOps can implement without reinterpreting GRC intent.  
> **Framework baseline:** OWASP LLM Top 10 2025, NIST AI RMF 1.0, NIST SP 800-53 Rev. 5, MITRE ATLAS where applicable.

---

## Count Reconciliation

| Lens | Count | Source |
|---|---:|---|
| Threat model entries | 17 | `CBBP-PLAN/COMPLY/meddata-threat-model.md` |
| Client findings | 10 | `deliverables/02-client-findings-report.md` — F-001 through F-010 |
| AI governance findings | 5 | `CBBP-PLAN/COMPLY/meddata-ai-inventory.md` — MDN-GOVERN-001 through MDN-GOVERN-005 |
| BUILD controls handed off | 7 first-sprint controls plus platform/CI controls | `CBBP-PLAN/BUILD/comply-to-build-handoff.md` and `CBBP-PLAN/COMPLY/comply-checklist.md` |
| Evidence packages created so far | 3 mini-loop packages plus live JSON evidence | `CBBP-PLAN/PROVE/loop*-*.md`, `Eugene-AI/evidence/` |

Different counts are expected because threats describe failure modes, findings group client-impacting gaps, governance IDs track inventory-level issues, and BUILD controls are implementation work packages.

---

## Threat To Evidence Matrix

| T-ID | Threat | Finding / Governance ID | BUILD Control | BREAK / Eval Coverage | PROVE Evidence |
|---|---|---|---|---|---|
| T-01 | Direct prompt injection | F-002 | BLD-001 input sanitization | Chatbox BREAK direct injection tests; corpus poison case also covers instruction-following defense | `CBBP-PLAN/PROVE/loop1-chatbox-rag-prove.md`; `Eugene-AI/evidence/break/chatbox-break-*.json` |
| T-02 | Indirect prompt injection via poisoned document | F-003, F-002 | BLD-002 manifest gate; BLD-001 sanitizer | Corpus contamination case CORPUS-BREAK-003 | `CBBP-PLAN/PROVE/loop3-rag-corpus-prove.md`; `Eugene-AI/evidence/break/corpus-contamination-break-*.json` |
| T-03 | Unauthorized retrieval across user role | F-001 | BLD-004 role-filtered retrieval | Baseline role retrieval eval; access-control unit coverage | `Eugene-AI/evidence/baseline-rag-eval-*.json`; targeted test suite |
| T-04 | Secrets / PHI exposure via retrieval | F-004 | BLD-003 secret/PHI scan; BLD-005 output filter | CORPUS-BREAK-004 and CORPUS-BREAK-005 | `CBBP-PLAN/PROVE/loop3-rag-corpus-prove.md`; `Eugene-AI/evidence/break/corpus-contamination-break-*.json` |
| T-05 | Source leakage | F-004 | BLD-005 output filter; source-citation shaping | Chatbox BREAK and baseline response checks | `CBBP-PLAN/PROVE/loop1-chatbox-rag-prove.md`; `Eugene-AI/evidence/eugene-helpfulness-eval-*.json` |
| T-06 | RAG corpus poisoning | F-003 | BLD-002 manifest-gated ingestion | CORPUS-BREAK-001 through CORPUS-BREAK-003 | `CBBP-PLAN/PROVE/loop3-rag-corpus-prove.md`; ingest evidence |
| T-07 | Human approval bypass | F-006, MDN-GOVERN-002 | BLD-007 HITL flagging and review decision records | HITL bypass BREAK runner | `CBBP-PLAN/PROVE/loop2-hitl-review-prove.md`; `Eugene-AI/evidence/break/hitl-review-bypass-*.json` |
| T-08 | Missing output filter | F-004 | BLD-005 output filter | Chatbox and query response tests | `CBBP-PLAN/PROVE/loop1-chatbox-rag-prove.md`; targeted test suite |
| T-09 | Missing audit logging | F-005, MDN-GOVERN-005 | BLD-006 structured audit log | Chatbox build check; HITL review checks | `CBBP-PLAN/PROVE/loop1-chatbox-rag-prove.md`; `CBBP-PLAN/PROVE/loop2-hitl-review-prove.md` |
| T-10 | Shadow AI | F-007, MDN-GOVERN-001 | AI dev sandbox approval log; shadow AI audit plan | Policy/procedure evidence pending | `CBBP-PLAN/PROVE/ai-dev-tool-boundary-evidence.md` |
| T-11 | Excessive agency | F-009, MDN-GOVERN-003 | Tool authority matrix; no tool execution in Eugene | Planned BREAK for tool-boundary bypass | `CBBP-PLAN/BUILD/ai-dev-assist-harness.md`; evidence pending |
| T-12 | Runtime drift | MDN-GOVERN-003 | Model version pinning and retest trigger | Static platform control check PASS; deployed runtime retest still required after any model/config change | `CBBP-PLAN/BUILD/model-decision-record.md`; `Eugene-AI/evidence/platform-control-check-*.json` |
| T-13 | Unsafe dependency via AI suggestion | F-010 | SCA gate, exact pins, dependency justification | Static SCA/pin control check PASS; live PR/CI bypass simulation still pending | `Eugene-AI/.github/workflows/sca.yml`; `Eugene-AI/evidence/platform-control-check-*.json` |
| T-14 | Vector store infrastructure exposure | F-001 | K8s NetworkPolicy, namespace isolation, Chroma service auth | Static platform control check PASS; deployed direct-access Chroma BREAK still pending | `Eugene-AI/deploy/k8s/networkpolicy.yaml`; `Eugene-AI/deploy/k8s/deployment-chromadb.yaml`; `Eugene-AI/evidence/platform-control-check-*.json` |
| T-15 | Embedding-layer leakage or manipulation | F-001, F-004 | Embedding access restriction, deletion workflow, collection isolation | Embedding-layer BREAK pending | `CBBP-PLAN/COMPLY/meddata-threat-model.md`; evidence pending |
| T-16 | Unbounded consumption | MDN-GOVERN-003 | Rate limiting, timeouts, resource limits | Unit/static rate-limit evidence PASS; deployed rapid-query BREAK still pending | `Eugene-AI/src/api/rate_limit.py`; `Eugene-AI/evidence/platform-control-check-*.json` |
| T-17 | User overreliance on AI summary | F-006, F-007 | AI-generated label, citations, HITL review state | Helpfulness eval and HITL review records | `Eugene-AI/evidence/eugene-helpfulness-eval-*.json`; `CBBP-PLAN/PROVE/loop2-hitl-review-prove.md` |

---

## Framework Mapping Snapshot

| Finding | Primary OWASP LLM 2025 | NIST AI RMF | NIST 800-53 / CKS Tie |
|---|---|---|---|
| F-001 ChromaDB role/access gap | LLM08, LLM02 | GOVERN 1.5, MEASURE 2.11 | AC-3, AC-4, SC-7, IA-2 |
| F-002 Prompt injection defense missing | LLM01 | MEASURE 2.11 | SI-10, AC-3 |
| F-003 Corpus approval/hash workflow missing | LLM04, LLM01 | MAP 3.1, MAP 3.2 | CM-3, SI-7 |
| F-004 Secrets/PHI/output filtering missing | LLM02, LLM05 | MEASURE 2.5, MEASURE 2.10 | AC-4, SI-12, SC-28 |
| F-005 Audit logging missing | Not direct OWASP; accountability control | MEASURE 2.7, MANAGE 4.1 | AU-2, AU-12, AU-9 |
| F-006 HITL enforcement missing | LLM09, LLM06 | GOVERN 1.2, MANAGE 2.2 | CA-5, PM-10 |
| F-007 Shadow AI not audited | LLM09, LLM02 | GOVERN 5.2 | CM-8, SA-4 |
| F-008 AI-assisted PR disclosure missing | LLM09 | GOVERN 1.5 | CM-3 |
| F-009 CODEOWNERS missing for sensitive paths | LLM06 | MANAGE 2.2 | SA-11, AC-6 |
| F-010 SCA gate missing for AI dependencies | LLM03 | MAP 4.1 | SR-3, SR-4 |

---

## BUILD Handoff Rule

BUILD treats this file as the reconciliation layer. If another workpaper has a stale count, stale OWASP number, or contradictory classification statement, this matrix and the corpus manifest take precedence until that source is patched.
