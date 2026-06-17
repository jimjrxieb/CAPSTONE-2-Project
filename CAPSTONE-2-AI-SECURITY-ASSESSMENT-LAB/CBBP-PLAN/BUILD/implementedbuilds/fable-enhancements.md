# BUILD Phase Review — Fable Enhancements

> **Reviewer:** Claude (Fable 5)
> **Date:** 2026-06-10
> **Scope:** All 7 BUILD workpapers, the 6 `crewai/` design docs, and — because BUILD claims must match code — the actual `Eugene-AI/` implementation: API routes, guardrails, audit logger, requirements, Dockerfile, deploy manifests, CI workflows, and the evidence files cited in `sprint1-status.md` (all verified present on disk).
> **Verdict:** The DevSecOps engineering here is real, not aspirational — the mini-CBBP loop pattern (build → break → prove per slice) is the best thing in the capstone, and the evidence trail checks out. Initial review found two material gaps: `/query` accepted a self-asserted role, and Eugene's "model" responses were deterministic keyword-matched drafts. The role issue has since been fixed with bearer-token role binding in `src/api/auth.py` and `src/api/routes/query.py`; the deterministic generation boundary remains documented until `EUGENE_MODE=ollama` evidence exists.

## Resolution Notes

- Fixed: `/query` now requires a bearer token and derives the retrieval role from `AuthContext`, not a user-submitted role field.
- Fixed: BUILD status tables now mark implemented controls as implemented and call out remote CI/live-cluster proof as pending hardening work.
- Still honest limitation: Eugene's Sprint 1 answer text is a deterministic advisory draft path. The eval validates retrieval, citations, audit status, HITL behavior, and draft shaping; it does not claim live model-generation quality.

---

## 1. What You Got Right

### 1.1 Mini-CBBP loops are the standout pattern

Running build → break → prove as small loops (Loop 1 chatbox, Loop 2 HITL review record, Loop 3 corpus contamination) instead of one big-bang phase is genuinely better practice than most consulting shops manage. Each loop closes with dated evidence. I verified every evidence file cited in `sprint1-status.md` exists on disk (`sprint1-control-check-*.json`, `hitl-review-bypass-*.json`, `corpus-contamination-break-*.json`, etc.). The HITL bypass BREAK with 7/7 attack cases — missing token, wrong token, unknown audit ID, weak rationale, invalid decision, unreviewed distribution block — is exactly how you prove a gate instead of asserting it.

### 1.2 COMPLY→BUILD traceability is mechanical, not decorative

`comply-to-build-handoff.md` maps every ticket to an F-ID and T-ID; `eugene-build-harness.md` maps every F-ID to a specific Python module and BREAK test; the modules exist at the stated paths (`src/guardrails/access_control.py`, `src/rag/sanitizer.py`, `src/audit/logger.py`, all verified). A reviewer can walk F-001 from COMPLY finding → BLD-004 → `access_control.py` → role-matrix evidence. That chain is the product.

### 1.3 Deterministic-first, CrewAI-later is the right call

The sequencing discipline — "Do not start with CrewAI. Start with the deterministic pipeline" (`crewai/implementation-roadmap.md`), repeated in `sprint1-status.md` ("Do not move to CrewAI yet") — matches the platform's three-tier law: human proof before agent proof. The CrewAI failure-mode rule in `security-boundaries.md` (correct output is `evidence_missing`, wrong output is `control_passed`) is a one-liner worth promoting to every GP-CONSULTING agent design.

### 1.4 The security hygiene that's implemented is actually implemented

Verified in code, not just docs: four-gate ingestion (manifest → secrets → PHI → embed), two-stage retrieval enforcement (role→collection filter + post-retrieval tier check), security headers middleware, docs disabled via env, CORS scoped to the Gradio origin, append-mode audit writes, non-root Dockerfile (`USER 10001`) with `HEALTHCHECK`, fully pinned `requirements.txt`, CODEOWNERS present, both CI workflows present, and the full `deploy/k8s/` + Kyverno policy set the CKS plan promised. The chatbox security rules (no file upload, no history persistence, system prompt never displayed) are the right privacy boundaries.

### 1.5 The 3B prompt-design rule shows real model-ops judgment

"Every agent prompt must specify the exact output format — llama3.2:3b will drift on open-ended instructions" is the kind of capacity-aware constraint most agent frameworks skip. The agent YAML definitions consistently enforce structured JSON output, narrow tasks, and `human_review_required: true`, with hard rules like "Never return PASS for an S-rank finding without human_review_status = approved."

### 1.6 Honest status language (mostly)

`sprint1-status.md` explicitly says "This does **not** mean BREAK is complete" and distinguishes local control checks from live RAG checks. The evidence contract's quality rules (no finding without evidence ID, no PROVE claim from chat memory) are auditor-grade. The one place honesty slips is the helpfulness eval — see 3.2.

---

## 2. What's Out of Date

### 2.1 The harness Implementation Checklist contradicted reality (resolved)

Initial review found that `eugene-build-harness.md` undersold implemented work by leaving review-critical controls marked as **Not started**. `sprint1-status.md` and the code on disk already showed those controls implemented with PASS evidence.

Resolution: the implementation checklist now reflects the implemented controls, separates local/static proof from remote CI/live-cluster proof, and labels deterministic generation honestly.

### 2.2 Ticket IDs collide between the two tracking documents

`comply-to-build-handoff.md` defines BLD-009 as "AI dev sandbox approval logging" and BLD-010–016 as Sprint 2 BREAK tickets. `sprint1-status.md` reuses BLD-009 for "Chatbox client path," BLD-010 for "HITL approval record," BLD-011 for "Manifest ownership contract," and introduces BRK-013/BRK-014. The same ID now means two different things depending on the file. Pick one registry (the handoff is the natural owner), renumber the sprint1 additions, and never reuse an ID — same rule as `poam_id` in the platform's audit trail standard.

### 2.3 Dependency pins are old, and two are unused with known CVEs

Pinning is right (good); the pinned versions are 2024-era and two should be deleted outright:

| Package | Pinned | Problem |
| --- | --- | --- |
| `python-jose==3.3.0` | **Never imported anywhere in `src/` or `config/`** (verified by grep) | Known CVEs (CVE-2024-33663, CVE-2024-33664 — algorithm confusion); effectively unmaintained. Remove. |
| `passlib==1.7.4` | **Never imported** | Unmaintained since 2020. Remove. |
| `crewai==0.30.11` | Used in `crew.py` | Very old; CrewAI moved fast through 2025 and dropped the LangChain dependency — current versions use a native `LLM` class. The `ChatOllama`-via-`langchain_ollama` pattern in `crew.py` is the deprecated integration style. |
| `langchain==0.2.5` / `langchain-community==0.2.5` | Pulled in for CrewAI | 0.3.x line since late 2024; only needed because of the old CrewAI pattern. |
| `gradio==4.36.1` | Chatbox | Gradio 4.x accumulated multiple security advisories; Gradio 5 (late 2024) was largely a security-hardening release. For a security capstone, the UI framework's own CVE history matters. |
| `fastapi==0.111.0`, `chromadb==0.5.3`, `ollama==0.2.1` | Used | Functional but a year+ old; refresh and re-run pip-audit as one batch. |

Unused dependencies with CVEs are exactly what your own SCA gate (BLD-017) exists to catch — removing them is also a free demo of the gate working.

### 2.4 `nomic-embed-text:latest` violates your own pinning rule

`model-decision-record.md` pins the generation model and defines a re-test rule for any model change — then specifies the embedding model as `:latest`. An embedding model update silently changes retrieval behavior for the entire corpus, which is precisely the T-12 runtime-drift threat COMPLY documented, and embeddings drift matters *more* than generation drift in a RAG system (every stored vector becomes stale). Pin a version/digest and add "embedding model change requires full re-ingest + baseline RAG eval re-run" to the re-test rule.

### 2.5 Two agent registries disagree

`eugene-build-harness.md` defines **5** agents (Intake, Assessment, Framework Mapper, Reviewer Gate, Report Packager). `crewai/agent-role-map.md` defines **9** (adding Evidence Request, Build Readiness, Scenario Coordinator, Evidence Collector). The rosters overlap but neither references the other, and `crew.py` implements the harness's 5. Make `agent-role-map.md` the single registry, mark which agents are implemented vs. planned, and have the harness link to it instead of duplicating YAML.

---

## 3. What Can Be Improved

### 3.1 `/query` role self-assertion was the highest-priority gap (resolved)

Initial review found that `POST /query` accepted `role` as a plain field in the request body with no token or identity check. Any caller could claim `it_security` and retrieve confidential/security-tier chunks.

This matters beyond the bug itself: it reproduces the client's S-rank finding pattern one layer up. F-001 was "access control enforced at the retrieval layer, not just UI" — and BLD-004 built exactly that tier filtering, correctly. But the *identity* the filter trusts is unauthenticated, so the control reduces to UI-level enforcement again. The Vendor Risk and Compliance filtering evidence in `sprint1-status.md` is real but proves "the filter works when the caller is honest about their role."

Resolution: `src/api/auth.py` now requires bearer tokens, maps each token to an `AuthContext`, and `src/api/routes/query.py` derives retrieval role from that authenticated context. The request body no longer carries role authority. The remaining improvement is to keep this covered by the unauthorized-retrieval BREAK runner and preserve the finding as a good example of CBBP catching and fixing a real design flaw.

### 3.2 Eugene's answers are canned — and the eval claims don't say so

`build_eugene_response` → `_draft_answer` in `query.py` is a hardcoded if/elif chain keyed to the demo questions ("constant yung" → canned CISO answer, "clearbot" → canned vendor answer, "soc 2" → canned CC6.7 answer…). The code comments admit this honestly ("deterministic assessment draft until local inference is enabled"). But `sprint1-status.md` reports "Eugene helpfulness eval: PASS — 8/8 business questions returned expected facts" and the DevSecOps call says "Eugene answered 8/8 business-use questions correctly." An 8/8 eval against answers hardcoded for those 8 questions is the eval validating itself — a reviewer who opens `query.py` will discount every helpfulness claim in the package.

Two honest paths, both fine:

1. **Wire the model.** `crew.py` already constructs `ChatOllama`; the ingest path already uses Ollama embeddings. Route the assembled prompt (system + retrieved chunks + sanitized query) through `llama3.2:3b`, keep the deterministic path as an explicit `EUGENE_MODE=deterministic` fallback, and re-run the eval against actual generation with RAG grounding. This is also the step that makes the "MLOps merged with DevSecOps" story true — right now the model named in the model decision record never generates anything.
2. **Relabel the claims.** If generation stays deferred, change the eval language everywhere to "deterministic draft-path eval" and add an explicit "generation model not yet wired" line to sprint status and any PROVE claim that touches helpfulness.

Option 1 is strongly preferred — the capstone's thesis is securing an AI model, and currently the lab secures a keyword router.

### 3.3 Rate limiting was specified and is now implemented

Initial review called out the missing limiter. `src/api/rate_limit.py` now provides a small in-process limiter and `/query` keys it on authenticated `auth.user_id`, not a self-reported session. This is sufficient for the local capstone lab. A production version should move rate state to Redis or an API gateway so limits survive process restarts and multi-replica deployments.

### 3.4 The audit logger's validation can never fail

`logger.py` builds the entry dict from its own function parameters, then checks `REQUIRED_FIELDS - set(entry.keys())` — but the dict is constructed with every field hardcoded, so the check is structurally incapable of failing. It's a control that always passes, which is weak evidence ("the logger raises on missing fields" can't be demonstrated). Also: the docstring says "7-field" while the entry writes 11 fields, and COMPLY promised a *tamper-resistant* store (AU-9) while append-only here is convention (`open("a")`) with nothing preventing later edits. Fixes, in order of value: (1) validate at read/packaging time too — the PROVE packager should reject audit entries missing required fields, which makes the control testable; (2) add a per-entry hash chain (`prev_hash` field) for cheap tamper-evidence; (3) rename to match reality ("structured audit logger, 11 fields, 7 required").

### 3.5 ChromaDB auth is wired in code; live proof remains

`config/settings.py` now exposes `CHROMA_AUTH_TOKEN`, and `src/rag/retriever.py`
supplies token auth when Eugene runs against a remote Chroma host. The k8s
package also includes network isolation artifacts. Earlier review notes asked
for a production-like cluster BREAK run, but the completed BUILD boundary now
stops at local/static capstone platform evidence.

**Closeout note:** This was a reviewer recommendation for a production-like
cluster proof. It is no longer an active BUILD blocker for the local capstone.
The completed BUILD boundary uses local/static platform evidence and does not
claim a managed cloud deployment.

### 3.6 The sanitizer is a regex blocklist — say so, and bound the claim

Eight regex patterns will stop the three BREAK payloads and not much else (paraphrase, encoding, multilingual, "ignore the above" all walk through). As Gate 1 of defense-in-depth that's a legitimate layer — the real protections are retrieval filtering and treating chunks as data. The risk is claim inflation: "injection rejected — PASS" in the evidence reads stronger than eight regexes support. Add one sentence to the harness ("pattern blocklist; bypassable by design; relied-upon control is context isolation + output filtering"), expand the BREAK payload set to ~15 including paraphrases, and record the expected-bypass cases as documented residual risk rather than letting BREAK imply resistance.

### 3.7 The MLOps half of the story is thinner than the DevSecOps half

You described this capstone as "DevSecOps and MLOps turned agents and merged together." The DevSecOps lane is strong (gates, CI, k8s, evidence). The MLOps lane is missing its standard artifacts: no **model card** for Eugene (you have these for JADE/KATIE in GP-MODEL-OPS — reuse the template), no versioned **prompt registry** (the re-test rule triggers on "prompt template change" but prompts aren't versioned artifacts anywhere), no **generation eval baseline** (only retrieval evals exist — blocked on 3.2), no experiment tracking (Cap2-Harness mentioned optional MLflow; even a one-run trace would do). Adding model card + prompt versioning + post-3.2 generation eval makes the merged-disciplines claim defensible in an interview.

### 3.8 CrewAI sequencing says one thing, the repo does another

The roadmap says "Do not create this code until the API/evidence interfaces exist" — yet `src/agents/crew.py` (170 lines, all 5 agents) exists and `crewai` + the LangChain stack are in `requirements.txt`, inflating the pip-audit surface for code the sprint explicitly defers. Either move the CrewAI deps to a separate `requirements-crew.txt` installed only when Loop 4+ begins, or update the roadmap to acknowledge the skeleton exists and is intentionally unwired. Minor, but it's the kind of doc-vs-repo mismatch this capstone teaches clients to catch.

### 3.9 Small fixes

- `src/guardrails/access_control.py` defines a custom `PermissionError`, shadowing the Python builtin — any unrelated builtin `PermissionError` (e.g., a file-permission failure) caught in `query.py` would 403 as a role failure. Rename to `AccessControlError`.
- Harness model table says llama3.2:3b context window is 8,192 — the model supports 128K; 8,192 is an Ollama `num_ctx` default. Say "configured context: 8,192 (`num_ctx`)" so the spec states a decision, not a wrong capability.
- `Dockerfile` pins `python:3.11-slim` by tag; pin by digest to satisfy your own supply-chain bar (SR-4, and your Kyverno disallow-latest policy's spirit).
- `comply-to-build-handoff.md` Sprint 2 table double-counts work now done in Loops 1–3 (BLD-014 audit-log replay, BLD-015 HITL bypass are effectively complete). Reconcile after fixing the ticket registry (2.2).

---

## Priority Order

| # | Action | Why first | Effort |
| --- | --- | --- | --- |
| 1 | Keep `/query` bearer-token role binding covered by unauthorized-retrieval BREAK evidence (3.1) | This was the highest-risk design bug and is now the best build-break-fix story | Done locally; repeat before final PROVE |
| 2 | Wire real Ollama generation behind `EUGENE_MODE`, re-run helpfulness eval, or keep deterministic claims clearly labeled (3.2) | Eval integrity; do not let deterministic draft shaping masquerade as model quality | 0.5-1 day |
| 3 | Unify ticket registry (2.2) | Avoid duplicate BLD IDs across handoff and sprint status docs | 1 hr |
| 4 | Remove `python-jose`/`passlib`, refresh pins, re-run pip-audit (2.3) | Unused deps with CVEs; free demo of your own SCA gate | 1 hr |
| 5 | Pin embedding model + extend re-test rule (2.4) | Silent retrieval drift; violates own standard | 15 min |
| 6 | Repeat rate-limit evidence and run live Chroma auth BREAK case (3.3, 3.5) | Local controls exist; production-like cluster proof is optional future work outside this BUILD | 0.5 day |
| 7 | Audit logger: packaging-time validation + hash chain (3.4); sanitizer claim-bounding (3.6) | Strengthens evidence quality before PROVE closes | 0.5 day |
| 8 | Model card, prompt registry, generation eval baseline (3.7); CrewAI dep split (3.8); small fixes (3.9) | Completes the MLOps half of the merged-disciplines story | 1 day |

**Bottom line:** The engineering discipline — mini-loops, traceability, evidence-first — is the hard part and it's genuinely in place; I verified the evidence files and the module paths rather than taking the docs' word. The original unauthenticated query-path issue has been fixed. The biggest remaining honesty boundary is Eugene's deterministic draft path: keep it clearly labeled, or wire live local generation and capture generation-specific evidence.
