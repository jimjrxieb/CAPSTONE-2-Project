# COMPLY to BUILD Handoff — DevSecOps Receiver Plan

> **Input:** `CBBP-PLAN/COMPLY/comply-checklist.md`, `CBBP-PLAN/COMPLY/traceability-matrix.md`  
> **Receiver:** BUILD / DevSecOps implementation team  
> **System:** MDN-AI-001 Internal RAG Chatbot + CAP2-AI-001 Eugene assessment lab  
> **Rule:** BUILD implements controls. BREAK validates controls. PROVE packages evidence.

---

## BUILD Mission

Turn the COMPLY package into a working, repeatable AI security assessment harness.

COMPLY found the MedData Nexus AI goals, wishlist, control gaps, threat model, risk ratings, and evidence requirements. BUILD receives those findings and creates implementation work that is small enough to review and test.

BUILD is not a free-form coding phase. It is a controlled receiver lane:

```text
COMPLY finding / wishlist / gap
  -> BUILD ticket
  -> Codex / Claude Code authorization check
  -> detailed implementation plan
  -> human review
  -> approved build
  -> BREAK validation
  -> PROVE evidence package
```

The first BUILD lane is not CrewAI. It is the deterministic RAG security path:

```text
approved corpus -> manifest-gated ingest -> role-filtered retrieval
-> Eugene query/assessment API -> output filter -> audit log
-> HITL review state -> evidence artifacts
```

CrewAI and n8n can orchestrate later. They do not replace the core controls.

## AI Dev-Tool Authorization Gate

Codex and Claude Code are allowed for this capstone build, but only inside the harness in `ai-dev-assist-harness.md`.

| Question | Decision |
| --- | --- |
| Are Codex and Claude Code allowed to assist BUILD? | Yes, for approved repo files, sanitized docs, synthetic data, and implementation planning. |
| Can they receive real client data, real PHI, real credentials, or uncontrolled sensitive context? | No. |
| Can they make final risk decisions? | No. Eugene and AI dev tools are advisory only. |
| Can they run broad local commands or cross local socket boundaries without review? | No. Human approval and narrow scope are required. |
| Where are tool-boundary exceptions recorded? | `../PROVE/ai-dev-tool-boundary-evidence.md`. |

If this gate changes, BUILD pauses and COMPLY must update the AI tool boundary before implementation continues.

## BUILD Review States

| State | Meaning | Move Forward When |
| --- | --- | --- |
| Proposed build | A plan exists, but no implementation should be trusted yet | Source finding and acceptance criteria are clear |
| Human-reviewed build | The plan was checked for scope, data boundary, and risk | Reviewer approves implementation |
| Approved build | The item is allowed to be implemented | Build artifacts and test hooks are created |
| Implemented build | The artifact exists locally | Unit/static evidence is captured |
| BREAK-ready build | The control can be attacked or validated | Scenario, runner, or test steps exist |
| PROVE-ready build | Evidence can support a claim in deliverables | Evidence path and limitation note are recorded |

This repo keeps the states as workpapers instead of separate folders so GitHub navigation stays compact. The state must still be visible in the ticket tables and status files.

---

## Sprint 1 — RAG Control Harness

| Ticket | Control | Build Artifact | Acceptance Criteria | COMPLY Source |
|---|---|---|---|---|
| BLD-001 | Input sanitization | `Eugene-AI/src/rag/sanitizer.py` | Known direct-injection strings rejected before retrieval | F-002, T-01 |
| BLD-002 | Manifest-gated ingestion | `Eugene-AI/src/rag/pipeline.py` | Only manifest-approved files enter ChromaDB; rejected files logged | F-003, T-02/T-06 |
| BLD-003 | Secret/PHI scan | `secret_scanner.py`, `phi_scanner.py` | Unsafe docs rejected or redacted; pattern type logged, not value | F-004, T-04 |
| BLD-004 | Role-filtered retrieval | `access_control.py`, `retriever.py` | Role x category access matrix blocks unauthorized chunks | F-001, T-03 |
| BLD-005 | Output filter | `output_filter.py` | PHI/secrets/internal leakage patterns redacted or blocked | F-004, T-05/T-08 |
| BLD-006 | Structured audit log | `audit/logger.py` | Every query writes required fields to append-only JSONL | F-005, T-09 |
| BLD-007 | HITL flagging | `api/routes/query.py` | Confidential/security/restricted source responses return `review_required=true` | F-006, T-07 |
| BLD-008 | Evidence endpoints | `api/routes/evidence.py` | Audit log and manifest evidence retrievable through gated endpoints | COMPLY evidence layer |
| BLD-009 | AI dev sandbox approval logging | BUILD/PROVE evidence note | Local-socket/escalated commands have scoped approval records | AI dev assist harness |
| BLD-025 | Query authentication | `src/api/auth.py`, `api/routes/query.py` | `/query` role claim comes from bearer token, not request body | F-001, T-03 |
| BLD-026 | Query rate limiting | `src/api/rate_limit.py` | Authenticated user is limited to configured requests per minute | T-16 |
| BLD-027 | Audit hash-chain validation | `audit/logger.py`, `api/routes/evidence.py` | Audit entries validate required fields and hash chain on read | F-005, T-09 |

**Sprint 1 exit:** unit tests pass and dry-run ingest can produce evidence without a running production cluster.

---

## Sprint 2 — BREAK Evidence Harness

| Ticket | Scenario | Build Artifact | Acceptance Criteria |
|---|---|---|---|
| BLD-010 | Direct prompt injection | `tests/` + BREAK runner | Three injection payloads rejected and logged |
| BLD-011 | Poisoned document | ingest scenario flag + evidence output | Poisoned doc is rejected or marked scenario-only and never trusted as instruction |
| BLD-012 | Unauthorized retrieval | access matrix script | Low-privilege roles cannot retrieve security/legal/restricted chunks |
| BLD-013 | Secrets in corpus | unsafe ingest scenario | Fake credentials/PHI rejected before indexing and absent from responses |
| BLD-014 | Missing audit logging | query replay script | Five sample queries produce complete audit entries |
| BLD-015 | HITL bypass | high-risk query sample | High-risk response cannot be packaged without pending/approved review state |
| BLD-016 | AI dev tool lane check | approval log and command transcript | Local socket/escalated commands are scoped, approved, and tied to evidence |

**Sprint 2 exit:** each BREAK scenario has dated JSON/Markdown evidence under `evidence/`.

---

## Sprint 3 — DevSecOps And CKS Platform Controls

| Ticket | Control | Build Artifact | Acceptance Criteria | NIST Tie |
|---|---|---|---|---|
| BLD-017 | CI SCA gate | `.github/workflows/sca.yml` | `pip-audit` runs; non-pinned dependencies fail | SR-3, SR-4 |
| BLD-018 | AI-assisted PR label | `.github/workflows/ai-assist-label-check.yml` | Sensitive path PRs require `ai-assisted` label | CM-3 |
| BLD-019 | CODEOWNERS | `Eugene-AI/CODEOWNERS` | Auth, guardrail, logging, infra paths require security reviewer | SA-11 |
| BLD-020 | Container build | `Dockerfile` | Non-root app image; no secrets; healthcheck defined | CM-6, SI-7 |
| BLD-021 | Kubernetes manifests | `deploy/k8s/` | Namespace, Deployment, Service, ConfigMap, Secret template | AC-3, SC-7 |
| BLD-022 | NetworkPolicy | `deploy/k8s/networkpolicy.yaml` | Deny-by-default; API can reach only approved services | SC-7 |
| BLD-023 | OPA/Kyverno policies | `deploy/policies/` | Privileged pods, latest tags, missing limits rejected | CM-6, CM-7 |
| BLD-024 | Image/SBOM scan | CI workflow | Trivy/Grype and SBOM generation run before deploy | RA-5, SR-4 |

**Sprint 3 exit:** platform pilot can be reviewed against CKS-style hardening requirements before any production-like deployment.

---

## Current Receiver Assessment

| Area | BUILD Status | Notes |
|---|---|---|
| COMPLY package | Ready | `comply-checklist.md` is the handoff checklist |
| Eugene API | Implemented for Sprint 1 | Query route, evidence route, token-bound roles, HITL flags, citations, and replayable evidence exist |
| RAG pipeline | Sprint 1 live PASS | Local dry-run and live Chroma/Ollama retrieval evidence exist |
| Guardrail tests | Sprint 1 local PASS | Unit tests cover sanitizer, access control, output filter, audit log, manifest checks, Sprint 1 control check |
| BREAK runners | Implemented as targeted runners | Chatbox, HITL bypass, corpus contamination, unauthorized retrieval, and fable red-team evidence exist; unified wrapper remains future polish |
| CKS/platform artifacts | Static controls PASS | Dockerfile, K8s manifests, NetworkPolicy, Kyverno policies, and platform control evidence exist; live cluster proof remains next platform step |
| CrewAI | Skeleton only | Keep unwired until deterministic controls and Loop 4/platform validation remain stable |

---

## BUILD Definition Of Done

BUILD is complete only when:

1. Sprint 1 controls are implemented and unit-tested.
2. Sprint 2 BREAK evidence can be generated from scripts.
3. Sprint 3 platform controls exist as reviewable manifests/policies.
4. No hard blocker from `comply-checklist.md` remains unimplemented.
5. PROVE has evidence paths for every claim BUILD makes.

Current state: items 1-3 are met for a local capstone review package. Remaining hardening work is live cluster validation, remote GitHub CI proof, and optional model-generation evidence.

Until those phase-2 items are closed, the system remains a controlled assessment build, not a pilot-expansion candidate.
