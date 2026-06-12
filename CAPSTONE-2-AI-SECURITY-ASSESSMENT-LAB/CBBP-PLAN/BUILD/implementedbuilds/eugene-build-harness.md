# Eugene-AI Build Harness — Capstone 2

> **System:** CAP2-AI-001 — Eugene, Local AI Security Assessment Assistant
> **Build target:** `/home/jimmie/linkops-industries/GP-copilot/GP-SECLAB/target-application/slot-5/Eugene-AI/`
> **Model:** `llama3.2:3b` via Ollama (local, air-gapped)
> **Assessor:** jimjrxieb
> **Date:** 2026-06-08
> **COMPLY input:** `CBBP-PLAN/COMPLY/Cap2-Harness.md`, `CBBP-PLAN/COMPLY/meddata-ai-harness.md`, `CBBP-PLAN/COMPLY/comply-checklist.md`
> **Status:** BUILD phase — COMPLY complete; implementation begins here

---

## What This Document Is

This is the engineering translation of COMPLY.

Every decision in `Cap2-Harness.md` and `meddata-ai-harness.md` becomes a specific file, class, or configuration here. Every finding in `meddata-ai-harness.md` Section 5 (Guardrail Layer) maps to a specific Python module or CI gate below.

BUILD is complete when every item in the Implementation Checklist at the bottom of this document is checked and a corresponding BREAK test has returned PASS.

The receiver-side sprint plan lives in `comply-to-build-handoff.md`. Platform hardening lives in `cks-platform-build-plan.md`.

Model selection rationale lives in `model-decision-record.md`.

---

## System Architecture

```
                    ┌─────────────────────────────────────────┐
                    │             Eugene-AI System             │
                    │                                         │
  User Query ──────►│  Sanitizer → ChromaDB (role-filtered)  │
                    │       ↓                                 │
                    │  Prompt Assembler                       │
                    │       ↓                                 │
                    │  Ollama llama3.2:3b (local inference)   │
                    │       ↓                                 │
                    │  Output Filter → Audit Logger           │
                    │       ↓                                 │
  Response ◄────────│  HITL Gate (high-risk outputs)         │
                    │       ↓                                 │
                    │  CrewAI Assessment Crew (advisory)      │
                    └─────────────────────────────────────────┘

  Data sources: ChromaDB (eugene-meddata-nexus collection)
  External: no external LLM API path in scope for Eugene
  Audit: audit-log.jsonl (append-only)
  Human gate: all B/S-rank findings routed to jimjrxieb before becoming deliverables
```

---

## Model

| Field | Value |
| --- | --- |
| Model name | `llama3.2:3b` |
| Provider | Ollama (local) |
| Endpoint | `http://localhost:11434` |
| Context window | 8,192 tokens |
| Inference mode | Local only — no external API call |
| Version pinning | Pin via `OLLAMA_MODEL=llama3.2:3b` in `.env` |
| Re-test trigger | Any model version change requires BREAK tests 1–5 to re-run |

**Why 3B:** Data stays local. No external transmission. Suitable for structured assessment tasks with narrow prompts. Not suitable for open-ended reasoning — agents must use focused, structured prompts.

**Prompt design rule for 3B:** Every agent prompt must specify the exact output format. llama3.2:3b will drift on open-ended instructions. Use structured templates: `Return a JSON object with fields: finding, evidence_gap, rank, remediation.`

---

## Directory Structure — Eugene-AI/

```
Eugene-AI/
├── README.md                         ← entry point; build status; run commands
├── requirements.txt                  ← pinned dependencies
├── .env.example                      ← env var template (no real secrets)
├── config/
│   ├── settings.py                   ← all config loaded from env; no hardcoded values
│   └── harness.yaml                  ← agent roles, task templates, model settings
├── src/
│   ├── rag/
│   │   ├── __init__.py
│   │   ├── pipeline.py               ← ingest: manifest check → scan → embed → store
│   │   ├── retriever.py              ← query: role filter → ChromaDB → tier check
│   │   ├── sanitizer.py              ← input: injection pattern detection + rejection
│   │   └── output_filter.py          ← output: credential + PHI pattern interception
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── intake_agent.py           ← COMPLY completeness check
│   │   ├── assessment_agent.py       ← Eugene RAG finding drafter
│   │   ├── framework_mapper.py       ← OWASP LLM / MITRE ATLAS / NIST mapping
│   │   ├── reviewer_gate.py          ← evidence completeness + human review routing
│   │   ├── report_packager.py        ← PROVE evidence packaging
│   │   └── crew.py                   ← CrewAI crew assembly
│   ├── api/
│   │   ├── __init__.py
│   │   ├── main.py                   ← FastAPI app; docs disabled in prod
│   │   └── routes/
│   │       ├── query.py              ← POST /query
│   │       ├── ingest.py             ← POST /ingest (manifest-gated)
│   │       └── evidence.py           ← GET /evidence/*
│   ├── chatbox/
│   │   └── app.py                    ← Gradio UI; calls /query; shows source citations
│   ├── audit/
│   │   └── logger.py                 ← 7-field structured JSONL audit log
│   └── guardrails/
│       ├── __init__.py
│       ├── access_control.py         ← per-role ChromaDB collection filter (F-001)
│       ├── secret_scanner.py         ← detect-secrets patterns on ingest (F-004)
│       └── phi_scanner.py            ← PHI pattern detection on ingest + output (F-004)
└── tests/
    ├── test_sanitizer.py             ← injection pattern rejection
    ├── test_access_control.py        ← role × tier matrix
    ├── test_output_filter.py         ← credential pattern interception
    └── test_audit_logger.py          ← required field presence
```

---

## RAG Pipeline

### Ingestion Pipeline (`src/rag/pipeline.py`)

Every document passes through four gates before entering ChromaDB. Any gate failure rejects the document and logs the reason.

```
Document file
    │
    ▼
[Gate 1] Corpus manifest check
    — Is this document in target-client/fake-data/corpus-manifest.md?
    — Does the SHA-256 hash match the manifest entry?
    — FAIL → reject; log: document_name, reason=NOT_IN_MANIFEST, timestamp
    │
    ▼
[Gate 2] Secret scanner (detect-secrets patterns)
    — Does the document contain API key, token, password, or connection string patterns?
    — FAIL → reject; log: document_name, reason=SECRET_PATTERN_DETECTED, pattern_type (not value)
    │
    ▼
[Gate 3] PHI scanner
    — Does the document contain SSN, MRN, DOB, diagnosis code, or insurance ID patterns?
    — FAIL → reject (or flag for human review if classification is ambiguous)
    — Log: document_name, reason=PHI_PATTERN_DETECTED, pattern_type
    │
    ▼
[Gate 4] Chunk + embed + store
    — Chunk with metadata: doc_name, category, classification, is_poisoned, source_file, chunk_id
    — Embed with pinned `nomic-embed-text:v1`; embedding model changes require full re-ingest and baseline eval
    — Store in ChromaDB collection: eugene-meddata-nexus
    — Log: document_name, chunk_count, collection, timestamp, ingest_run_id
```

### Retrieval Pipeline (`src/rag/retriever.py`)

Every query passes through two access checks before chunks reach the prompt assembler.

```
Incoming query + user_role
    │
    ▼
[Check 1] Role → allowed collections map
    — vendor_risk_reviewer: [public, vendor_docs]
    — compliance_analyst: [public, internal, compliance]
    — it_security: [public, internal, compliance, confidential, security]
    — Filter: only query allowed collections for this role
    │
    ▼
[Check 2] Post-retrieval tier check
    — For each returned chunk: verify chunk.classification ≤ role's max tier
    — Any chunk above max tier: drop silently; log the drop with reason=TIER_EXCEEDED
    │
    ▼
Prompt assembler
    — System prompt (trusted, isolated from user text)
    — Retrieved chunks (treated as data, not instructions)
    — User query (untrusted, sanitized)
    │
    ▼
Ollama llama3.2:3b
```

---

## Agents — CrewAI Crew

### Agent Design Rule for llama3.2:3b

Each agent gets a single, narrow task with a structured output template. The model is 3B — it cannot reliably handle multi-step open-ended instructions. Every task specifies the exact JSON output shape.

---

### Agent 1 — Intake Completeness Agent

```yaml
role: "AI Governance Intake Reviewer"
goal: >
  Review COMPLY workpapers and identify any missing ownership, data boundary,
  tool approval, or evidence fields. Return a structured gap list only.
  Do not invent facts. Do not mark a field complete if the value is TBD or blank.
backstory: >
  You are a senior AI governance analyst at a GuidePoint-style MSSP.
  You have reviewed dozens of AI adoption intakes. You know exactly what a
  governed AI system needs before pilot expansion: named owners, defined data
  tiers, approved tools, prohibited data listed explicitly, and human-only
  decisions documented. You produce gap lists, not summaries.
task: |
  Read the following COMPLY workpaper sections.
  For each required field, output whether it is SATISFIED, PARTIAL, or MISSING.
  Return JSON: {"gaps": [{"field": str, "status": str, "note": str}]}
  Do not add commentary outside the JSON.
allowed_inputs:
  - CBBP-PLAN/COMPLY/meddata-ai-adoption-intake.md
  - CBBP-PLAN/COMPLY/meddata-ai-inventory.md
  - CBBP-PLAN/COMPLY/meddata-rag-corpus-intake.md
human_review_required: true
authority: "advisory — human reviews output before COMPLY is closed"
```

---

### Agent 2 — RAG Assessment Agent (Eugene)

```yaml
role: "AI Security Assessor"
goal: >
  Given a security scenario and retrieved evidence context, draft a structured
  security finding. Include: what failed, what control was expected, what the
  evidence shows, and the risk rank. Do not fabricate evidence. If evidence
  is missing, say so explicitly.
backstory: >
  You are Eugene, a local AI security assessment assistant deployed in a
  GuidePoint-style AI security assessment lab. Your job is to help a human
  assessor draft structured findings from retrieved context. You do not make
  final risk decisions. You do not accept or close risk. You draft findings
  and flag what is missing. The human assessor reviews every output you produce
  before it becomes part of a client deliverable.
task: |
  Given the following scenario metadata and retrieved context chunks, draft
  a structured finding.
  Return JSON:
  {
    "finding_draft": str,
    "evidence_gap": str or null,
    "expected_control": str,
    "observed_failure": str,
    "rank_suggestion": "S|B|C|D",
    "remediation_draft": str,
    "human_review_required": true
  }
  If evidence is missing, set evidence_gap to a description of what is needed.
  Never set human_review_required to false for S or B rank.
allowed_inputs:
  - retrieved chunks from ChromaDB (sanitized, role-filtered)
  - scenario metadata from scenarios/*.md
  - evidence artifacts from evidence/
human_review_required: true
authority: "advisory — C-rank max. All S/B route to jimjrxieb immediately."
```

---

### Agent 3 — Framework Mapper Agent

```yaml
role: "AI Security Framework Compliance Mapper"
goal: >
  Map a confirmed finding to the correct OWASP LLM Top 10, MITRE ATLAS,
  NIST AI RMF, and NIST 800-53 control IDs. Provide a one-sentence rationale
  for each mapping. Do not map to a framework ID without a rationale.
backstory: >
  You are a compliance analyst who has spent years mapping security findings
  to control frameworks for FedRAMP, HIPAA, and SOC 2 engagements. You know
  that framework mappings are only useful if they are specific and justified.
  A finding that says "maps to everything" maps to nothing.
task: |
  Given the following finding summary, return framework mappings.
  Return JSON:
  {
    "owasp_llm": [{"id": str, "rationale": str}],
    "mitre_atlas": [{"id": str, "rationale": str}],
    "nist_ai_rmf": [{"id": str, "rationale": str}],
    "nist_800_53": [{"id": str, "rationale": str}]
  }
  Use only IDs you can justify. Return an empty list if no mapping applies.
  Do not return more than 3 IDs per framework.
allowed_inputs:
  - confirmed finding drafts (reviewed by human)
  - framework reference in templates/800-53-to-ai-rmf.md
human_review_required: true
authority: "advisory — human spot-checks all mappings before PROVE"
```

---

### Agent 4 — Reviewer Gate Agent

```yaml
role: "Evidence and Review Gate Auditor"
goal: >
  Check whether a finding has sufficient evidence and required human approvals
  before it can advance to PROVE. Reject any finding that lacks an evidence ID,
  source path, or required human review for S/B-rank. Never mark a finding
  approved on behalf of a human.
backstory: >
  You are a senior internal auditor. You have stopped more than one report
  from going to a client because the evidence did not support the claim.
  Your job is to be the last gate before findings become deliverables. You
  are not popular during deadline crunches, and that is the point.
task: |
  Given the following finding and evidence record, return a gate decision.
  Return JSON:
  {
    "gate_result": "PASS|FAIL|PENDING_HUMAN",
    "missing_evidence": [str] or [],
    "missing_approvals": [str] or [],
    "notes": str
  }
  PASS only if evidence_id exists, source_path exists, and human_review_status
  is "approved" for S/B-rank findings.
  PENDING_HUMAN if the finding is S or B rank and human_review_status is "pending".
  FAIL if evidence is missing entirely.
  Never return PASS for an S-rank finding without human_review_status = "approved".
allowed_inputs:
  - finding drafts
  - evidence records from evidence/
  - human review records
human_review_required: true
authority: "gate only — cannot approve S/B-rank findings"
```

---

### Agent 5 — Report Packager Agent

```yaml
role: "PROVE Evidence Packager"
goal: >
  Given reviewed and gate-approved findings, draft risk register rows and
  executive summary bullets for the PROVE package. Produce structured output
  only. Do not publish or deliver — produce drafts for human review.
backstory: >
  You are a consulting analyst who has packaged dozens of security assessment
  reports for GuidePoint-style engagements. You know that a risk register row
  needs: finding ID, title, rank, score, status, owner, milestone, and evidence
  path. You know that an executive summary bullet needs: the business risk in
  plain language, the current state, and the recommended action. You do not
  use framework acronyms in executive bullets.
task: |
  Given the following approved findings, return structured PROVE outputs.
  Return JSON:
  {
    "risk_register_rows": [
      {
        "finding_id": str,
        "title": str,
        "rank": str,
        "score": int,
        "status": "OPEN|REMEDIATED|ACCEPTED",
        "owner": str,
        "milestone": str,
        "evidence_path": str
      }
    ],
    "executive_bullets": [str]
  }
  Executive bullets must be one sentence each, no acronyms, business language only.
  Do not include any finding that does not have gate_result = PASS.
allowed_inputs:
  - gate-approved findings
  - evidence index
  - existing client-findings-report.md for reference
human_review_required: true
authority: "advisory — CISO Constant Yung reviews PROVE package before it is closed"
```

---

## Chatbox (`src/chatbox/app.py`)

Gradio-based chat UI. Runs locally. Calls the FastAPI `/query` endpoint.

```
UI features:
  - Text input field (user query)
  - Role selector dropdown (vendor_risk_reviewer / compliance_analyst / it_security)
  - Response display with source citations
  - "This is an advisory output. Human review required for high-risk responses." banner
  - No history persistence across sessions (privacy boundary)
  - No file upload (data enters through the ingestion pipeline, not chat UI)

Security rules built into UI:
  - Role selector is required — query blocked if no role selected
  - Responses tagged HIGH-RISK display a review-required warning
  - System prompt text never displayed to user
  - Source citations show document name and classification tier; not chunk text
```

---

## API (`src/api/`)

**Base URL:** `http://localhost:8000`

**Docs endpoint:** Disabled in production (`DISABLE_DOCS=true` in `.env`)

| Endpoint | Method | Auth | Purpose |
| --- | --- | --- | --- |
| `/query` | POST | Bearer token (role claim) | Submit a RAG query; returns response + source citations + audit_id |
| `/ingest` | POST | Admin token | Ingest a document (passes all 4 pipeline gates) |
| `/ingest/status` | GET | Admin token | Check ingest job status |
| `/evidence/audit-log` | GET | IT Security token | Return paginated audit log entries |
| `/evidence/corpus-manifest` | GET | Admin token | Return current corpus manifest |
| `/health` | GET | None | Liveness check (no data returned) |
| `/docs` | — | Disabled | FastAPI docs — off in production |

**POST /query request shape:**
```json
{
  "query": "string — user's natural language question",
  "role": "vendor_risk_reviewer | compliance_analyst | it_security",
  "session_id": "string — for audit correlation"
}
```

**POST /query response shape:**
```json
{
  "response": "string — model answer",
  "sources": [
    {"doc_name": "string", "classification": "string", "chunk_id": "string"}
  ],
  "audit_id": "string — references the audit log entry",
  "high_risk": true/false,
  "review_required": true/false
}
```

---

## Audit Logger (`src/audit/logger.py`)

Append-only JSONL file at `evidence/audit-log.jsonl`. Every RAG interaction writes one entry.

**Required fields — all 7 must be present or the logger raises an error:**

```json
{
  "audit_id": "AUD-20260608T112458Z-0001",
  "timestamp": "2026-06-08T11:24:58Z",
  "user_id": "string",
  "role": "string",
  "query_text": "string",
  "retrieved_chunk_ids": ["string"],
  "source_references": [{"doc_name": "string", "classification": "string"}],
  "model_response": "string (or hash for restricted-tier deployments)",
  "api_path": "internal | haiku-external",
  "high_risk": true/false,
  "reviewer_decision": "string or null — required if high_risk=true"
}
```

**Append-only enforcement:** File is opened in append mode (`"a"`). No update or delete operation is exposed. Log rotation writes to a new dated file, never overwrites.

---

## Guardrails — COMPLY-to-BUILD Translation

Every finding from `meddata-ai-harness.md` Section 5 maps to a specific implementation here.

### F-001 — ChromaDB Per-Role Access Control (`guardrails/access_control.py`)

```python
ROLE_COLLECTIONS = {
    "vendor_risk_reviewer": ["public", "vendor_docs"],
    "compliance_analyst": ["public", "internal", "compliance"],
    "it_security": ["public", "internal", "compliance", "confidential", "security"],
}

def get_allowed_collections(role: str) -> list[str]:
    if role not in ROLE_COLLECTIONS:
        raise PermissionError(f"Unknown role: {role}")
    return ROLE_COLLECTIONS[role]

def filter_chunks_by_tier(chunks: list, role: str) -> list:
    allowed = get_allowed_collections(role)
    approved = [c for c in chunks if c["category"] in allowed]
    dropped = [c for c in chunks if c["category"] not in allowed]
    if dropped:
        log_tier_violation(dropped, role)
    return approved
```

BREAK test: Test 4 — must pass for all role × restricted-category combinations.

### F-002 — Input Sanitization (`rag/sanitizer.py`)

```python
INJECTION_PATTERNS = [
    r"ignore (your )?(previous |all )?instructions",
    r"repeat (your )?system prompt",
    r"you are now",
    r"SYSTEM OVERRIDE",
    r"disregard (your )?(previous )?instructions",
    r"act as (a )?(different|new|unrestricted)",
    r"forget (your )?(previous )?instructions",
    r"do not follow",
]

def sanitize_query(query: str) -> str:
    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, query, re.IGNORECASE):
            raise InjectionDetectedError(f"Injection pattern detected")
    return query
```

BREAK test: Test 1 — all three injection patterns rejected.

### F-003 — Corpus Manifest Gate (`rag/pipeline.py`)

```python
def check_manifest(doc_path: str, doc_hash: str) -> bool:
    manifest = load_manifest()
    entry = manifest.get(doc_path)
    if not entry:
        raise ManifestViolationError(f"{doc_path} not in manifest")
    if entry["sha256"] != doc_hash:
        raise ManifestViolationError(f"Hash mismatch for {doc_path}")
    return True
```

BREAK test: Test 2 — poisoned document rejected at ingest gate.

### F-004 — Secret and PHI Scanner (`guardrails/secret_scanner.py`, `guardrails/phi_scanner.py`)

```python
# secret_scanner.py — pre-ingest
SECRET_PATTERNS = [
    r"(?i)(aws_secret_access_key|aws_access_key_id)\s*=\s*[A-Z0-9+/]{20,}",
    r"(?i)(api_key|apikey|api-key)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{20,}",
    r"(?i)(password|passwd|pwd)\s*[:=]\s*['\"]?.{8,}",
    r"(?i)(token|secret)\s*[:=]\s*['\"]?[A-Za-z0-9_\-\.]{20,}",
    r"-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----",
]

# phi_scanner.py — pre-ingest + output filter
PHI_PATTERNS = [
    r"\b\d{3}-\d{2}-\d{4}\b",           # SSN
    r"\bMRN[-:]?\s*\d{6,10}\b",          # MRN
    r"\bDOB[-:]?\s*\d{2}/\d{2}/\d{4}\b", # DOB
    r"\bICD-10[-:]?\s*[A-Z]\d{2}\.?\d*\b", # Diagnosis code
]
```

BREAK test: Test 3 — document with fake credential rejected at ingest; absent from all responses.

### F-005 — Audit Logging

Implemented in `audit/logger.py` above. All 7 required fields must be present or the logger raises.

BREAK test: Test 5 — submit 5 queries; all 7 required fields present in each entry.

### F-006 — HITL Gate (`api/routes/query.py`)

```python
HIGH_RISK_CLASSIFICATIONS = ["confidential", "security", "restricted"]

def check_hitl_required(sources: list, query_text: str) -> bool:
    for source in sources:
        if source["classification"] in HIGH_RISK_CLASSIFICATIONS:
            return True
    return False

# In query route:
if check_hitl_required(sources, query):
    response_obj["high_risk"] = True
    response_obj["review_required"] = True
    response_obj["reviewer_decision"] = None  # must be filled before distribution
    audit_entry["high_risk"] = True
    audit_entry["reviewer_decision"] = None
```

---

## Security Configuration

**`.env.example`** — no real secrets; all values are placeholders:

```env
# Model
OLLAMA_ENDPOINT=http://localhost:11434
OLLAMA_MODEL=llama3.2:3b
OLLAMA_EMBED_MODEL=nomic-embed-text:v1
EUGENE_MODE=deterministic

# ChromaDB
CHROMA_HOST=localhost
CHROMA_PORT=8001
CHROMA_COLLECTION=eugene-meddata-nexus
CHROMA_AUTH_TOKEN=replace-with-local-token

# API
API_HOST=127.0.0.1
API_PORT=8000
QUERY_RATE_LIMIT_PER_MINUTE=60
DISABLE_DOCS=true
CORS_ORIGINS=http://localhost:7860

# Audit
AUDIT_LOG_PATH=evidence/audit-log.jsonl

# Auth (replace with real token store — do not use these values)
ADMIN_TOKEN=replace-with-admin-token
IT_SECURITY_TOKEN=replace-with-it-security-token
COMPLIANCE_ANALYST_TOKEN=replace-with-compliance-token
VENDOR_RISK_TOKEN=replace-with-vendor-token
ADMIN_TOKEN=REPLACE_WITH_REAL_TOKEN
IT_SECURITY_TOKEN=REPLACE_WITH_REAL_TOKEN

```

**Security headers (FastAPI middleware):**
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY`
- `Content-Security-Policy: default-src 'self'`
- CORS restricted to `CORS_ORIGINS` from env

**Rate limiting:** 60 requests per minute per `user_id`. Block and log on exceed.

---

## CI/CD Gates (Coding Assistant Guardrails — F-008, F-009, F-010)

These go in the Eugene-AI repo as GitHub Actions workflows.

### `.github/workflows/ai-assist-label-check.yml`

```yaml
name: AI-Assisted PR Label Check
on:
  pull_request:
    paths:
      - 'src/**'
      - 'requirements.txt'
      - 'config/**'
jobs:
  label-check:
    runs-on: ubuntu-latest
    steps:
      - name: Check ai-assisted label
        run: |
          LABELS=$(gh pr view ${{ github.event.pull_request.number }} \
            --json labels --jq '.labels[].name')
          if echo "$LABELS" | grep -q "ai-assisted"; then
            echo "Label present — OK"
          else
            echo "ERROR: ai-assisted label required for changes to src/, requirements.txt, or config/"
            exit 1
          fi
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### `CODEOWNERS`

```
# Auth-sensitive paths require security reviewer
src/api/routes/query.py     @jimjrxieb
src/guardrails/             @jimjrxieb
src/audit/                  @jimjrxieb
config/                     @jimjrxieb
```

### `.github/workflows/sca.yml`

```yaml
name: SCA Gate
on: [pull_request]
jobs:
  pip-audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install pip-audit
        run: pip install pip-audit==2.7.3
      - name: Run pip-audit
        run: pip-audit -r requirements.txt --strict
      - name: Enforce pinned versions
        run: |
          if grep -E '^[a-zA-Z].*[>~^*]' requirements.txt | grep -v '=='; then
            echo "ERROR: Unpinned dependency found. Use == for all packages."
            exit 1
          fi
```

---

## Implementation Checklist

Track BUILD progress against this list. Each item maps to a COMPLY finding and a BREAK test.

| # | Control | Module | Finding | BREAK Test | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | Corpus ingested (clean baseline) | `rag/pipeline.py` | — | — | Complete |
| 2 | Baseline retrieval confirmed | `rag/retriever.py` | — | — | Complete |
| 3 | Per-role ChromaDB access control | `guardrails/access_control.py` | F-001 | Test 4 | Implemented; baseline eval evidence |
| 4 | Input sanitization + injection detection | `rag/sanitizer.py` | F-002 | Test 1 | Implemented; chatbox BREAK evidence |
| 5 | Corpus manifest gate + hash verification | `rag/pipeline.py` | F-003 | Test 2 | Implemented; corpus BREAK evidence |
| 6 | Secret scanner on ingest | `guardrails/secret_scanner.py` | F-004 | Test 3 | Implemented; corpus BREAK evidence |
| 7 | PHI scanner on ingest + output filter | `guardrails/phi_scanner.py` | F-004 | Test 3 | Implemented; corpus/output tests |
| 8 | Structured audit log with hash chain | `audit/logger.py` | F-005 | Test 5 | Implemented; read-time validation added |
| 9 | HITL gate on high-risk outputs | `api/routes/query.py`, `api/routes/evidence.py` | F-006 | HITL bypass | Implemented; Loop 2 PASS |
| 10 | FastAPI app (docs disabled) | `api/main.py` | — | Test 9 | Implemented |
| 11 | Gradio chatbox | `chatbox/app.py` | — | Chatbox BREAK | Implemented |
| 12 | Per-user query rate limiting | `api/rate_limit.py` | T-16 | Test 9 | Implemented locally |
| 13 | CrewAI agents | `agents/crew.py` | — | — | Skeleton only; unwired until Loop 4+ |
| 14 | CI label-check gate | `.github/workflows/ai-assist-label-check.yml` | F-008 | Test 6 | Implemented locally; remote GitHub CI run pending |
| 15 | CODEOWNERS file | `CODEOWNERS` | F-009 | Test 7 | Implemented |
| 16 | SCA gate (pip-audit + pin enforcement) | `.github/workflows/sca.yml` | F-010 | Test 8 | Implemented locally; remote GitHub CI run pending |
| 17 | Poisoned corpus scenario toggle | `rag/pipeline.py` | — | Test 2 | Implemented; corpus contamination BREAK evidence |
| 18 | Unsafe corpus scenario toggle | `rag/pipeline.py` | — | Test 3 | Implemented; corpus contamination BREAK evidence |
| 19 | Eugene API endpoint | `api/routes/query.py` | — | Tests 1–5 | Implemented with token-bound role |
| 20 | Output filter (credential + PHI patterns) | `rag/output_filter.py` | F-004 | Test 3 | Implemented |

Status note: Sprint 1 uses `EUGENE_MODE=deterministic`. The current evidence validates retrieval, role filtering, citations, audit IDs, HITL status, and deterministic draft shaping. It does not claim live LLM generation quality until an `EUGENE_MODE=ollama` evidence run exists.

Injection note: the sanitizer is a pattern blocklist and is intentionally treated as one defense-in-depth layer. The relied-upon controls are role-scoped retrieval, context isolation, output filtering, audit evidence, and human review.

---

## Build Sequence

Do not skip steps. Each step is a prerequisite for the next.

```
Step 1 — rag/pipeline.py        Manifest check → secret scan → PHI scan → ingest
Step 2 — guardrails/            access_control.py, secret_scanner.py, phi_scanner.py
Step 3 — audit/logger.py        7-field JSONL logger; append-only
Step 4 — rag/retriever.py       Role filter → ChromaDB → tier check → prompt assemble
Step 5 — rag/sanitizer.py       Injection pattern detection + rejection
Step 6 — rag/output_filter.py   Credential + PHI pattern interception
Step 7 — api/main.py            FastAPI app; middleware; docs disabled
Step 8 — api/routes/query.py    POST /query with HITL gate and audit logging
Step 9 — chatbox/app.py         Gradio UI calling /query
Step 10 — agents/               CrewAI agents (assessment, mapping, gate, packaging)
Step 11 — CI gates              label-check, SCA, CODEOWNERS
Step 12 — BREAK tests           Execute all 10; record evidence; update checklist above
```

**Definition of done:** BUILD is complete when all 20 checklist items are marked Complete and all 10 BREAK tests have returned PASS with dated evidence artifacts in `evidence/`.
