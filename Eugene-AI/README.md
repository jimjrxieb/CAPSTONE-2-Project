# Eugene-AI

Local AI security assessment assistant for Capstone 2.

**Model:** llama3.2:3b via Ollama (local, no external transmission)
**System ID:** CAP2-AI-001
**Role:** Advisory only - all findings require human review before becoming deliverables
**Build harness:** `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BUILD/eugene-build-harness.md`

---

## What Eugene Demonstrates

Eugene is a governed RAG assistant over a synthetic healthcare SaaS corpus. It is designed to show how an AI security engineer can build, test, and evidence a controlled assistant before recommending whether a client should pilot, scale, or pause an AI workflow.

The system includes:

- Manifest-gated corpus ingestion
- Prompt-injection, secret, and PHI scanning
- Role-filtered ChromaDB retrieval
- Deterministic advisory answer shaping for repeatable evidence
- Source citations
- Output filtering
- Human-in-the-loop review flags
- Structured audit logging
- FastAPI service and Gradio chatbox
- Evidence runners for BUILD/BREAK/PROVE
- Docker, Kubernetes, NetworkPolicy, and policy artifacts

---

## Prerequisites

```bash
# Ollama running with llama3.2:3b
ollama pull llama3.2:3b
ollama serve

# ChromaDB running
# (started by ingest script or docker-compose)

# Python 3.11+
python3 --version
```

---

## Setup

```bash
cd Eugene-AI
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env - set real tokens; do not commit .env
```

---

## Run - RAG Pipeline

```bash
# Ingest clean baseline corpus
python3 -m src.rag.pipeline --reset

# Run baseline retrieval evaluation
python3 -m src.evidence.baseline_eval_runner

# Ingest poisoned scenario (BREAK test 2)
python3 -m src.rag.pipeline --reset --poisoned

# Ingest unsafe scenario (BREAK test 3)
python3 -m src.rag.pipeline --reset --unsafe
```

---

## Run - API

```bash
uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --reload
# Docs endpoint is disabled in production (DISABLE_DOCS=true)
```

---

## Run - Chatbox

```bash
python3 -m src.chatbox.app
# Opens at http://localhost:7860
```

## Chatbox Roles

| Role | Retrieval Boundary |
| --- | --- |
| `vendor_risk_reviewer` | Vendor-risk records and approved vendor documentation only. Restricted from security, HIPAA, incident, legal, and broader compliance corpora. |
| `compliance_analyst` | Policies, compliance records, vendor-risk context, legal templates, and AI governance records. Restricted from security and healthcare-privacy corpora. |
| `it_security` | All approved baseline corpus categories, including security and healthcare-privacy records. High-risk outputs still require human review. |

The chatbox has no file upload path and does not persist chat history. All answers are advisory and must keep source citations plus audit IDs.

---

## Run - Tests

```bash
pytest tests/ -v
```

Targeted evidence checks:

```bash
python3 -m src.evidence.sprint1_control_check
python3 -m src.evidence.chatbox_build_check
python3 -m src.evidence.chatbox_break_runner
python3 -m src.evidence.corpus_contamination_break_runner
python3 -m src.evidence.unauthorized_retrieval_break_runner
python3 -m src.evidence.hitl_review_break_runner
python3 -m src.evidence.platform_control_check
python3 -m src.evidence.eugene_helpfulness_eval
```

---

## Build Status

| Component | Status |
| --- | --- |
| Corpus ingested (clean baseline) | Complete |
| Baseline retrieval confirmed | Complete |
| Per-role access control | Sprint 1 PASS |
| Input sanitization | Sprint 1 PASS |
| Secret scanner | Sprint 1 PASS |
| PHI scanner | Sprint 1 PASS |
| Audit logger | Sprint 1 PASS |
| HITL flagging | Sprint 1 PASS |
| FastAPI app | Sprint 1 PASS |
| Gradio chatbox | Loop 1 BUILD PASS |
| Chatbox BREAK tests | PASS evidence captured |
| Corpus contamination BREAK tests | PASS evidence captured |
| Unauthorized retrieval BREAK tests | PASS evidence captured |
| Platform control static checks | PASS evidence captured |
| CrewAI agents | Advisory scaffold present |
| CI gates | Present locally; remote run pending GitHub publish |

Full checklist: `CBBP-PLAN/BUILD/eugene-build-harness.md` - Implementation Checklist

---

## Architecture

```text
User / Chatbox
  -> FastAPI /query
  -> auth + rate limit
  -> query sanitizer
  -> ChromaDB retrieval
  -> role/tier filtering
  -> deterministic advisory draft or local model path
  -> output filter
  -> HITL flag
  -> audit log
  -> response with citations
```

Runtime boundary:

- Eugene context stays local.
- `.env` is local only and ignored by git.
- External LLM APIs are not in scope for retrieved context.
- Any future external model path requires a new COMPLY boundary and approval.

---

## Key Files

| Path | Role |
| --- | --- |
| `src/api/routes/query.py` | Main guarded query path |
| `src/rag/pipeline.py` | Manifest-gated ingestion |
| `src/rag/retriever.py` | ChromaDB retrieval and role-filter handoff |
| `src/guardrails/access_control.py` | Role/category access matrix |
| `src/rag/sanitizer.py` | Prompt-injection detection |
| `src/guardrails/secret_scanner.py` | Secret pattern detection |
| `src/guardrails/phi_scanner.py` | PHI pattern detection |
| `src/rag/output_filter.py` | Output redaction |
| `src/audit/logger.py` | Structured JSONL audit log |
| `src/audit/review.py` | HITL review records |
| `src/evidence/` | Repeatable evidence runners |
| `deploy/k8s/` | Kubernetes deployment artifacts |
| `deploy/policies/` | Admission/policy controls |

---

## Security Rules

- Do not put real secrets, real PHI, or real credentials in any file in this repo
- Do not commit `.env` - it is in `.gitignore`
- Do not enable `HAIKU_API_ENABLED=true` without human approval and sanitized context
- Eugene is advisory - do not publish its output as a finding without human sign-off
- All B/S-rank findings route to jimjrxieb before becoming deliverables

## Known Limits

- Deterministic advisory mode is used for repeatable evidence; generation-model quality testing is phase 2.
- Static platform control evidence does not replace a deployed-cluster BREAK run.
- Local token auth is a lab control; enterprise production would need identity provider integration.
- The corpus is synthetic and intentionally safe for public demonstration.
