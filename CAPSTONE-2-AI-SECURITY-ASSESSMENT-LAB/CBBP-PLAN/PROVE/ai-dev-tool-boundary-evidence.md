# AI Dev Tool Boundary Evidence

> **System:** CAP2-AI-001 Eugene build harness  
> **Phase:** BUILD Loop 1 -> PROVE evidence capture  
> **Date:** 2026-06-09  
> **Owner:** jimjrxieb  
> **Purpose:** Record scoped AI-dev-tool boundary approvals and dependency actions.

---

## Evidence Item — Gradio Install Approval

| Field | Detail |
|---|---|
| Evidence ID | AIDEV-BOUNDARY-20260609-001 |
| Trigger | Loop 1 chatbox BUILD discovered `gradio` was declared in `requirements.txt` but not installed in the active Python environment |
| Boundary crossed | Dependency installation / external package retrieval |
| Command | `pip install gradio==4.36.1` |
| Approval | User explicitly approved: "i approve the gradio install" |
| Scope | Install only the pinned Gradio version required by `Eugene-AI/requirements.txt` |
| Result | Install completed successfully |
| Packages installed/changed | `gradio==4.36.1`, `gradio-client==1.0.1`, `aiofiles==23.2.1`, `altair==5.5.0`, `ffmpy==1.0.0`, `pillow==10.4.0`, `pydub==0.25.1`, `tomlkit==0.12.0`, `websockets==11.0.3` |
| Control interpretation | Codex did not install dependencies silently. The missing UI dependency was detected, scoped to the project pin, approved by the human operator, then executed. |
| Related BREAK test | BREAK Test 11 — AI Dev Tool Sandbox Boundary |
| Related BUILD artifact | `Eugene-AI/src/chatbox/app.py`, `Eugene-AI/tests/test_chatbox.py` |

---

## PROVE Interpretation

This event supports the AI dev tool boundary claim:

> Dependency installation is a controlled boundary crossing. The AI development assistant identified the dependency gap, requested scoped approval, and installed only the approved pinned package needed for the chatbox build.

This is acceptable BUILD behavior and should remain auditable in the final PROVE package.

---

## Evidence Item — Local API And Chatbox Runtime Approval

| Field | Detail |
|---|---|
| Evidence ID | AIDEV-BOUNDARY-20260609-002 |
| Trigger | Loop 1 chatbox BUILD required a running local FastAPI service and Gradio chatbox |
| Boundary crossed | Local socket binding and local service access |
| Commands | `uvicorn src.api.main:app --host 127.0.0.1 --port 8000`; `python3 -m src.chatbox.app` with Gradio analytics disabled |
| Approval | Scoped local runtime commands were approved for BUILD validation |
| Scope | Localhost only; no public Gradio share link; local API only |
| Result | FastAPI ran at `http://127.0.0.1:8000`; Gradio ran at `http://127.0.0.1:7860` |
| Produced evidence | `Eugene-AI/evidence/chatbox-build-check-20260609T141407Z.json` |
| Control interpretation | Local socket use was treated as a boundary crossing and handled through scoped runtime commands rather than broad network access. |

---

## Evidence Item — Sandbox Context Mismatch Caught

| Field | Detail |
|---|---|
| Evidence ID | AIDEV-BOUNDARY-20260609-003 |
| Trigger | First chatbox evidence run returned `Connection refused` while the API appeared alive |
| Root cause | API was started inside sandbox context; live chatbox check ran outside sandbox context for local socket access |
| Failed evidence | `Eugene-AI/evidence/chatbox-build-check-20260609T141310Z.json` |
| Remediation | Restarted FastAPI in the same local-socket context used by the chatbox evidence runner |
| Passing evidence | `Eugene-AI/evidence/chatbox-build-check-20260609T141407Z.json` |
| Control interpretation | The failure is useful evidence: sandbox boundaries can affect local service visibility and must be accounted for in BUILD/BREAK procedures. |

---

## Evidence Item — Loop 2 Local Runtime And Health Check

| Field | Detail |
|---|---|
| Evidence ID | AIDEV-BOUNDARY-20260609-004 |
| Trigger | Loop 2 HITL review control required the local API and chatbox to be restarted with the new review endpoint/UI |
| Boundary crossed | Local socket binding and local socket health checks |
| Commands | `uvicorn src.api.main:app --host 127.0.0.1 --port 8000`; `python3 -m src.chatbox.app`; `curl -fsS http://127.0.0.1:8000/health`; `curl -fsS http://127.0.0.1:7860/` |
| Approval | Scoped local runtime and health-check commands were approved for BUILD validation |
| Scope | Localhost only; no public share link; no external API call |
| Result | API health returned `{"status":"ok"}`; Gradio page loaded with Loop 2 review controls |
| Produced evidence | `Eugene-AI/evidence/hitl-review-check-20260609T145805Z.json`; `CBBP-PLAN/PROVE/loop2-hitl-review-prove.md` |
| Control interpretation | Local socket access remained a controlled boundary crossing and was tied to a specific BUILD/PROVE artifact. |

---

## Evidence Item — Loop 3 Baseline RAG Refresh

| Field | Detail |
|---|---|
| Evidence ID | AIDEV-BOUNDARY-20260609-005 |
| Trigger | Loop 3 required a clean baseline before poisoned/unsafe corpus BREAK tests |
| Boundary crossed | Local ChromaDB persistent store refresh and local Ollama embedding calls |
| Commands | `python3 -m src.rag.pipeline --reset`; `python3 -m src.evidence.baseline_eval_runner` |
| Approval | Scoped local RAG commands were approved for BUILD validation |
| Scope | Localhost/local filesystem only; synthetic MedData Nexus corpus only; no external API |
| Result | Refreshed `eugene-meddata-nexus` to 19 docs / 284 chunks; baseline RAG eval PASS |
| Produced evidence | `Eugene-AI/evidence/ingest-20260609T190552Z.json`; `Eugene-AI/evidence/baseline-rag-eval-20260609T190645Z.json` |
| Control interpretation | Corpus refresh and baseline eval were controlled local-boundary actions tied to Loop 3 evidence before contamination testing. |

---

## Evidence Item — HITL Approval Grant: Loop 1 Close-Out

| Field | Detail |
|---|---|
| Evidence ID | AIDEV-BOUNDARY-20260609-005 |
| Trigger | Loop 1 official close-out required formal HITL sign-off and assessor signature |
| Boundary crossed | Human-in-the-Loop approval authority temporarily delegated to AI assessor |
| Scope | Loop 1 PROVE closure sign-off only |
| Authorization | jimjrxieb granted claude-sonnet-4-6 (Sonnet) temporary authority to approve HITL items for Loop 1 close-out: *"if anything needs human approval, you have my blessings in approving it — log jimmie granted sonnet temp permission to approve"* |
| Authorized by | jimjrxieb — 2026-06-09 |
| Action | Sonnet reviewed all 9 Loop 1 control checks (all PASS), verified 6-file evidence packet completeness, confirmed CISO sentence written, and signed Loop 1 PROVE as officially closed |
| Control interpretation | Human operator provided explicit scoped authorization before any approval action was taken. AI assessor acted within that scope, took no action outside it, and logged this entry as the audit record of that authorization. This is acceptable PROVE behavior. |

---

## Evidence Item — Claude Code Safety Flag And Model Fallback

| Field | Detail |
|---|---|
| Evidence ID | AIDEV-BOUNDARY-20260610-006 |
| Trigger | Claude Code displayed a provider safety notice while working on CBBP cybersecurity content |
| Observed message | Fable 5 safety measures flagged the message for cybersecurity or biology topics, noted possible false positives, and switched the session to Opus 4.8 |
| Boundary crossed | AI dev tool safety classifier and model routing boundary |
| Affected tool/model | Claude Code; Fable 5 safety layer; fallback shown as Opus 4.8 |
| CBBP phase | BUILD/PROVE governance for AI dev tooling |
| Data boundary in force | Project files, synthetic lab data, and security-control documentation only; no real client data, PHI, credentials, or production secrets intentionally supplied |
| Required response | Treat as a governed safety event, not a failure. Do not bypass the classifier. Continue only inside the approved CBBP harness and record the routing event. |
| Action taken | Added explicit AI dev safety/model routing boundary to `CBBP-PLAN/BUILD/ai-dev-assist-harness.md` and checklist tracking to `CBBP-PLAN/COMPLY/comply-checklist.md` |
| Framework mapping | NIST AI RMF GOVERN 1.5, GOVERN 6.1, MANAGE 2.2; NIST AU-12, CM-3, AC-6; OWASP LLM06:2025 Excessive Agency; OWASP LLM03:2025 Supply Chain; OWASP LLM02:2025 Sensitive Information Disclosure |
| Control interpretation | The provider guardrail fired on authorized defensive cybersecurity work. The project did not attempt to bypass it; the event was captured as proof that AI dev tooling is monitored, bounded, and auditable. |
| Residual risk | Provider routing behavior is outside local control. Future PROVE checks should confirm that model switches do not expand data exposure, tool authority, or approval scope. |
