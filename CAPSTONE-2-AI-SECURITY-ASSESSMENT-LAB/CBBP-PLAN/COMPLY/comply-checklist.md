# COMPLY Checklist — GRC to BUILD Handoff

> **Client:** MedData Nexus Health Systems  
> **System:** MDN-AI-001 / CAP2-AI-001 Eugene Internal RAG Assistant + CBBP assessment harness  
> **Purpose:** Track what COMPLY has scoped so BUILD can implement the harness without reinterpreting the assessment.  
> **Source inputs:** `README.md`, `target-client/meddata-nexus-health-systems.md`, SSP-RAG-2026-001, cloud architecture notes, COMPLY workpapers, client findings report.

---

## How To Use This

This checklist means: **is the requirement scoped and handed to BUILD?**

It does **not** mean the control is implemented. BUILD owns implementation. BREAK owns validation. PROVE owns evidence packaging.

| Status | Meaning |
|---|---|
| CHECK | Requirement is scoped in COMPLY and ready for BUILD |
| GAP | Requirement is known but needs a BUILD artifact or test to prove it |
| BLOCKER | Must be implemented and proven before pilot expansion |
| N/A | Not in first-build scope |

---

## Client Scope And SSP Coverage

| Item | COMPLY | BUILD Handoff | NIST / Framework Tie | Notes |
|---|---|---|---|---|
| Client system name and purpose | CHECK | Build Eugene internal RAG assistant path | AI RMF MAP 1.1 | SSP defines read-only retrieval and draft summarization |
| System boundary | CHECK | API, retrieval, ingest, evidence, HITL review path | NIST CA-3, SC-7 | SSP excludes EHR, patient apps, live clinical records |
| Data classes and prohibited data | CHECK | Ingest gate + scanners + metadata labels | NIST AC-4, SC-28, SI-12 | PHI/ePHI, secrets, credentials prohibited from baseline |
| Tools in scope | CHECK | ChromaDB, Ollama/Eugene, FastAPI, Gradio | AI RMF GOVERN 1.5 | Eugene is local/internal only; no external LLM API path |
| Human-only decisions | CHECK | HITL gate and approval record | NIST CA-5, PM-10 | Risk acceptance, expansion, Restricted data, findings sign-off |
| Evidence requirements | CHECK | Audit JSONL, ingest evidence, access matrix, BREAK results | NIST AU-2, AU-12 | Evidence must link to source paths and reviewer decisions |
| Scale/no-scale gate | CHECK | PROVE package must summarize pass/fail evidence | AI RMF MANAGE 4.1 | Current recommendation: no expansion until blockers pass |

---

## AI / RAG Harness Controls

| Control | COMPLY | BUILD Handoff | NIST / AI Mapping | SecAI+ Concept |
|---|---|---|---|---|
| Prompt injection defense | CHECK | Input sanitizer; reject known injection patterns | SI-10, OWASP LLM01, ATLAS AML.T0051 | Secure AI input handling |
| Indirect prompt injection defense | CHECK | Treat retrieved chunks as data; scan poisoned docs | SI-7, OWASP LLM01/LLM04 | RAG threat mitigation |
| Corpus manifest gate | CHECK | Manifest parser; approved-file allowlist; hash record | CM-3, SI-7 | AI data provenance |
| Pre-ingestion secret scan | CHECK | detect-secrets/gitleaks-style gate | SI-12, SC-28 | Secure AI data lifecycle |
| Pre-ingestion PHI scan | CHECK | PHI pattern scanner; reject or escalate | AC-4, SI-12, HIPAA concepts | Regulated data protection |
| Role-based retrieval | BLOCKER | Role claim required; category/tier filter before prompt assembly | AC-3, AC-4, OWASP LLM08/LLM02 | AI access control |
| Post-retrieval tier check | BLOCKER | Drop unauthorized chunks; log drops | AC-4, AU-12 | Defense in depth for RAG |
| Output filter | CHECK | Redact/block PHI, secrets, internal path leakage | AC-4, SI-12, OWASP LLM05/LLM02 | Secure AI output handling |
| Source citations | CHECK | Return doc name, classification, chunk ID | AU-3, AI RMF MEASURE 2.7 | Explainability and traceability |
| Structured audit log | BLOCKER | Append-only JSONL with user, role, query, chunks, response, path, decision | AU-2, AU-12, AU-9 | AI accountability evidence |
| HITL enforcement | BLOCKER | High-risk outputs require review state before distribution | CA-5, PM-10, AI RMF GOVERN 1.2 | Responsible AI governance |
| Model version pinning | CHECK | `OLLAMA_MODEL`, re-test on version change | CM-3, SA-22 | AI lifecycle control |
| External API boundary | N/A | No external LLM API is in scope for Eugene | SC-8, AC-4 | Third-party AI risk remains tracked under shadow AI and AI dev tools |
| AI dev sandbox approvals | CHECK | Escalated/local-socket commands are allowlisted by narrow prefix and recorded as evidence | AC-6, CM-3, AU-12 | AI tool lane enforcement |

---

## Kubernetes / CKS Platform Controls

The SSP and cloud architecture notes place the RAG platform on AWS Kubernetes. These controls are part of the COMPLY handoff even if the first local Eugene build only simulates them.

| CKS / Platform Item | COMPLY | BUILD Handoff | NIST Tie | Notes |
|---|---|---|---|---|
| Kubernetes RBAC | CHECK | Service accounts and least-privilege roles for API, ingest, ChromaDB | AC-3, AC-6 | Retrieval API must not have admin rights to vector DB |
| Namespace isolation | CHECK | Separate RAG app, ChromaDB, ingest job, and monitoring boundaries | SC-7, AC-4 | SSP says ChromaDB limited to RAG namespace |
| NetworkPolicy | CHECK | Deny-by-default; allow API → retrieval → ChromaDB only | SC-7 | Blocks direct vector DB access outside namespace |
| Pod security standards | CHECK | Non-root, read-only root FS where possible, drop capabilities | CM-6, SI-7 | Required for Kubernetes-hosted pilot |
| Secrets management | CHECK | No secrets in images, repo, corpus, or env defaults | IA-5, SC-28 | Use secret manager/K8s secrets; fake values only in lab |
| Admission control / OPA | CHECK | OPA Gatekeeper or Kyverno policies for images, labels, privileged pods | CM-6, CM-7 | "OPA -- check" belongs here for BUILD |
| Image scanning | CHECK | Trivy/Grype or equivalent in CI before deploy | RA-5, SI-2 | Include base images and app dependencies |
| SBOM / dependency review | CHECK | SBOM plus pip-audit and exact pins | SR-3, SR-4 | Covers AI-suggested dependencies |
| Container runtime monitoring | GAP | Falco or EDR-style runtime signal for abnormal pod behavior | SI-4 | Needed for production-like pilot, not local MVP |
| Kubernetes audit logs | CHECK | Capture API server events affecting RAG namespace and secrets | AU-2, AU-12 | Required for incident reconstruction |
| TLS / service encryption | CHECK | TLS for app/API paths; no plaintext service exposure | SC-8, SC-13 | SSP references controlled internal access |
| Resource limits | CHECK | CPU/memory requests and limits for API, ingest, ChromaDB | SC-5, CM-6 | Prevent noisy-neighbor and basic abuse conditions |

---

## AI-Assisted Engineering Controls

| Control | COMPLY | BUILD Handoff | NIST / AI Mapping | SecAI+ Concept |
|---|---|---|---|---|
| Approved AI dev tools | CHECK | Codex, Claude Code, Copilot-style tools governed by harness | AI RMF GOVERN 1.5 | Secure AI use in DevSecOps |
| Shadow AI audit | GAP | Network/DLP review and staff declaration | CM-8, SA-4 | Enterprise AI governance |
| AI-assisted PR label | CHECK | CI fails sensitive PRs without `ai-assisted` label | CM-3 | AI change transparency |
| CODEOWNERS for sensitive paths | CHECK | Auth, role checks, secrets, logging, infra need security reviewer | SA-11, AC-6 | Human review of AI-assisted code |
| SAST gate | CHECK | Semgrep or equivalent on app and pipeline code | SA-11, SI-10 | Secure coding validation |
| SCA gate | CHECK | pip-audit/license check/exact version pinning | SR-3, SR-4 | AI supply-chain risk |
| Secrets scan gate | CHECK | gitleaks/detect-secrets in CI | SI-12 | Prevent credential exposure |
| Exception register | CHECK | CI bypass requires approver, justification, expiry | CA-5, CM-3 | Governance and accountability |
| Sandbox approval log | CHECK | Record approved Codex/Claude command prefixes, purpose, and evidence generated | AU-2, AU-12, AC-6 | Tool boundary assurance |
| AI dev safety/model routing log | CHECK | Record provider safety flags, refusals, model fallback, and routing changes that affect CBBP work | AI RMF GOVERN 1.5, GOVERN 6.1; AU-12; CM-3 | Prove AI dev tools stayed in approved scope |

---

## BUILD Must Produce

| Artifact | Required For | Owner |
|---|---|---|
| Eugene API/query route with retrieval, filtering, HITL flagging | Internal RAG assistant path | DevSecOps / BUILD |
| Manifest-gated ingestion pipeline | Corpus integrity | DevSecOps / BUILD |
| Role x category access matrix | F-001 validation | DevSecOps + GRC review |
| Prompt injection test evidence | F-002 validation | BREAK |
| Poisoned document ingest/retrieval evidence | F-003 validation | BREAK |
| Secret/PHI rejection evidence | F-004 validation | BREAK |
| Audit log sample with required fields | F-005 validation | BUILD/BREAK |
| HITL approval record sample | F-006 validation | GRC + BUILD |
| CI security gate results | F-008/F-010 validation | DevSecOps |
| Kubernetes/CKS control plan | Platform pilot readiness | DevSecOps / Platform |
| AI dev sandbox approval record | PROVE tool-boundary evidence | DevSecOps / GRC |
| AI dev safety/model routing record | PROVE evidence for provider safety flags, refusals, and fallback events | DevSecOps / GRC |
| PROVE evidence index | Client-ready package | GRC |

---

## COMPLY Assessment Result

COMPLY is ready to hand to BUILD.

The client need is understood, the SSP has been considered, the target system and tools are scoped, AI/RAG risks are mapped, and the CKS-style platform requirements are now captured for DevSecOps implementation.

The hard blockers remain:

- role-based retrieval control
- post-retrieval tier enforcement
- structured audit logging
- HITL enforcement
- ingestion manifest/scanning proof
- Kubernetes access/network/admission control plan before any production-like pilot

Until those are implemented and proven: **controlled assessment only; no pilot expansion.**
