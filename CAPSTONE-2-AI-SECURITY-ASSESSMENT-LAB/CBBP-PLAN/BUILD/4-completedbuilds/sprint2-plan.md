# Sprint 2 BUILD Plan — Platform Validation, Live Generation, CrewAI Loop 5

> **Status:** APPROVED → COMPLETE (2026-06-12). All tasks verified.
> **Template:** conforms to `GP-CONSULTING/docs/GPCONSULT-BuildDocs/templates/sprint-template.md`
> **Scope rank:** C-rank within this sprint. Dev/staging only. Log everything.
> **Source:** `sprint1-status.md` DevSecOps Call, `cks-platform-build-plan.md`, `crewai/implementation-roadmap.md`
> **Worker:** single session (Codex or Claude). Sequential — see Depends On column.
> **Authored:** 2026-06-11 (Claude). Executed: 2026-06-12 (Codex, autonomous loop).

---

## Loop-Runner Prompt

A self-looping session (Claude YOLO/Ralph) uses this prompt. For Codex or a
non-looping session, J re-prompts it per iteration. State lives in the Task
Status table, so a cold session orients from this file alone.

```text
Read AGENTS.md and this sprint file. Find the next TODO task in the Task Status
table whose dependencies are all DONE. Complete ONLY that task. Run its
acceptance command. If it passes, flip the task to DONE and exit. If it fails,
leave it TODO, write a Blocked note under the task, and exit. Do not touch git.
Do not start a second task.
```

---

## Path Convention

All paths in this file are relative to the slot-5 root:

```text
slot-5/
  CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/   ← CBBP-PLAN, scenarios, deliverables
  Eugene-AI/                                ← implementation, evidence, deploy
```

---

## Ground Rules

1. **No git operations.** Ever. J reviews and commits.
2. **Capped test runners only.** `Eugene-AI/scripts/test-targeted.sh` first; `test-full-capped.sh` only at checkpoint boundaries. Never raw `pytest tests -q`.
3. **Evidence naming:** keep the existing pattern — `<check-name>-<ISO-run-id>.json` under `Eugene-AI/evidence/` (BREAK runs under `evidence/break/`).
4. **Attack scripts in T3 target Eugene's own lab in a local cluster.** That is dev, in sprint scope, C-rank — run them yourself. Nothing leaves the lab.
5. **CrewAI guardrails (T5):** tools read-only except writes under `evidence/` and `CBBP-PLAN/PROVE/`. No external API calls. No shell commands. No final findings — everything lands `pending human review`.
6. **Task order is a dependency chain.** T3 must pass before T5 — the CrewAI gate in `crewai/implementation-roadmap.md` requires platform validation stable.

---

## Context — What Sprint 1 Already Delivered

Loops 1–4 are complete with evidence (the status docs lag reality — fixing that is T1):

| Loop | Evidence |
|---|---|
| 1 — chatbox | `evidence/break/chatbox-break-20260609T142715Z.json` |
| 2 — HITL bypass | `evidence/break/hitl-review-bypass-20260609T182603Z.json` |
| 3 — corpus contamination | `evidence/break/corpus-contamination-break-20260609T193306Z.json` |
| 4 — unauthorized retrieval | `evidence/break/unauthorized-retrieval-break-20260610T131529Z.json` |
| — fable red-team | `evidence/break/fable-redteam-20260610T131340Z.json` |
| platform static controls | `evidence/platform-control-check-20260610T150713Z.json` |

Remaining gaps, in order: doc drift, RBAC role files, **deployed** platform BREAK (static ≠ live), live Ollama generation evidence, CrewAI dry-run, PROVE packaging.

---

## T1 — Sync Status Docs to Reality

**Why:** `sprint1-status.md` says Loop 4 is "the next engineering step." Loop 4 evidence is dated 2026-06-10. A reviewer tracing claims hits a contradiction on the first read.

**Files:**
- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BUILD/sprint1-status.md`
- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/STATUS.md`

**Steps:**
1. Add Loop 4 (unauthorized retrieval) and the fable red-team run to the sprint1 ticket and evidence tables, with PASS/FAIL read from the evidence JSONs themselves — do not assume PASS, open the files.
2. Update the DevSecOps Call section: Loop 4 complete; next step is this sprint.
3. Update `STATUS.md` Current Position to reference Sprint 2.

**Acceptance:** no remaining text claims Loop 4 is pending; every evidence file referenced in the tables exists on disk.

```bash
grep -rn "unauthorized" CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BUILD/sprint1-status.md
```

---

## T2 — Kubernetes RBAC Role Files

**Why:** `cks-platform-build-plan.md` requires "service account + role files." Only `serviceaccount.yaml` exists.

**Files (new):**
- `Eugene-AI/deploy/k8s/role.yaml`
- `Eugene-AI/deploy/k8s/rolebinding.yaml`

**Steps:**
1. Read `deploy/k8s/serviceaccount.yaml` and `deployment-api.yaml` to see what the API pod actually needs. Eugene's API does not call the Kubernetes API — the Role should be minimal (empty rules or read-only on its own ConfigMap if the design requires it). Least privilege means least.
2. Bind the Role to the existing service account in the Eugene namespace only. No ClusterRole, no ClusterRoleBinding.
3. Add both files to the platform static control check if `scripts/` has a platform check runner that enumerates manifests.

**Acceptance:**

```bash
ls Eugene-AI/deploy/k8s/role.yaml Eugene-AI/deploy/k8s/rolebinding.yaml
grep -c "ClusterRole" Eugene-AI/deploy/k8s/role.yaml Eugene-AI/deploy/k8s/rolebinding.yaml   # expect 0
```

---

## T3 — Deployed Platform BREAK (the pending item)

**Why:** Static checks confirm the YAML says the right things. Nothing yet proves the controls hold on a running cluster. `sprint1-status.md` names exactly two pending checks: **deployed Chroma direct-access** and **rapid-query**.

**Pre-req:** a local cluster (kind or k3s). If neither is available on this machine, stop, write what's missing in the handoff note, and continue to T4 — do not fake the evidence.

**Steps:**
1. Create cluster, apply `deploy/k8s/` in order (namespace → configmap → secret from template with throwaway values → chromadb → api → services → networkpolicy → role/rolebinding from T2).
2. Apply `deploy/policies/` if Kyverno/OPA is installed; if not, record policies as "validated statically only" in the evidence JSON — do not silently skip.
3. **Chroma direct-access BREAK:** from a pod *outside* the allowed path (e.g. a curl pod in the same namespace without the API label, and one in another namespace), attempt to reach the Chroma service port directly. Expected: connection blocked by NetworkPolicy. From the API pod: expected allowed.
4. **Rapid-query BREAK:** script N rapid `/query` calls with a single valid token against the deployed API. Expected: rate limiter returns 429 (or the configured rejection) after the cap.
5. Write one evidence file: `Eugene-AI/evidence/break/platform-deployed-break-<run-id>.json` recording cluster type, manifests applied, each attempt, expected vs actual, PASS/FAIL per check.
6. Tear the cluster down. Leave no running cluster behind.

**Acceptance:**

```bash
ls Eugene-AI/evidence/break/platform-deployed-break-*.json
python3 -c "import json,glob; d=json.load(open(sorted(glob.glob('Eugene-AI/evidence/break/platform-deployed-break-*.json'))[-1])); print(d.get('overall_status'))"
```

Both BREAK checks PASS, or a documented blocker in the handoff note.

---

## T4 — Live Ollama Generation Evidence

**Why:** Embeddings run pinned `nomic-embed-text:v1`, but generation still uses the deterministic draft path. The named gap: no `EUGENE_MODE=ollama` evidence exists.

**Steps:**
1. Confirm Ollama is running locally and note the exact generation model + tag (pinned — never `latest`). Record the model digest in the evidence.
2. Run the existing helpfulness eval (`eugene-helpfulness-eval` runner) with `EUGENE_MODE=ollama`. Same 8 business questions, same expectations: facts, citations, audit IDs, review status.
3. Live generation may phrase answers differently than the deterministic path — the eval must check for required facts/citations/audit-ID presence, not exact string match. If the existing runner does exact matching, adapt the assertions and say so in the evidence file.
4. Write `Eugene-AI/evidence/eugene-helpfulness-eval-ollama-<run-id>.json`.
5. Run one prompt-injection payload through the live generation path and confirm the input sanitizer and output filter still hold with a real model behind them. Append the result to the same evidence file.

**Acceptance:**

```bash
ls Eugene-AI/evidence/eugene-helpfulness-eval-ollama-*.json
grep -l "EUGENE_MODE" Eugene-AI/evidence/eugene-helpfulness-eval-ollama-*.json
```

If Ollama is not available: documented blocker in handoff note, task stays open.

---

## T5 — CrewAI Loop 5: Dry-Run Orchestration

**Gate:** T3 must be PASS (or its blocker accepted by J) before starting. This is the roadmap's own rule.

**Why:** `src/agents/crew.py` is an intentionally unwired 170-line skeleton. The first build ticket is fully specified in `crewai/implementation-roadmap.md` — implement exactly that, nothing more.

**Steps:**
1. Read `crewai/implementation-roadmap.md`, `crewai/agent-role-map.md`, `crewai/security-boundaries.md`, `crewai/evidence-contract.md` first. The design is done — do not redesign it.
2. Wire the six roles from the minimum viable crew: Scenario Coordinator, Evidence Collector, Eugene Assessment, Framework Mapper, Reviewer Gate, Report Packager. Dependencies from `requirements-crew.txt` only — do not add packages to the main `requirements.txt`.
3. Dry-run inputs (read-only):
   - `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/scenarios/rag-direct-prompt-injection.md`
   - `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/COMPLY/meddata-ai-adoption-intake.md`
   - `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/COMPLY/meddata-ai-risk-assessment.md`
4. Dry-run output: `Eugene-AI/evidence/crewai/dry-run-rag-direct-prompt-injection.json` containing scenario ID, expected control, evidence required, missing evidence, and draft finding status `blocked_until_evidence_exists`.
5. The Reviewer Gate agent marks output pending human review. No agent marks anything final.
6. Targeted tests for the crew tools (scenario loader, evidence checker, prove writer) via `scripts/test-targeted.sh`.

**Acceptance:**

```bash
ls Eugene-AI/evidence/crewai/dry-run-rag-direct-prompt-injection.json
python3 -c "import json; d=json.load(open('Eugene-AI/evidence/crewai/dry-run-rag-direct-prompt-injection.json')); assert d['draft_finding_status']=='blocked_until_evidence_exists'; print('OK')"
```

---

## T6 — PROVE Packaging Polish

**Why:** roadmap step 8 is "Partial." The PROVE shells exist; the final package must index everything Sprint 1 + 2 produced.

**Files:**
- `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/PROVE/meddata-prove-package.md` (finalize)
- Touch the loop/map files only where they reference missing or renamed evidence.

**Steps:**
1. Build a complete evidence index: every claim in the PROVE files maps to a file that exists under `Eugene-AI/evidence/`. Fix dead references; add Sprint 2 evidence (T3, T4, T5 outputs).
2. Confirm the dual-format rule: the package must contain (or link) both an executive/CISO-style summary and an operator-style handoff. If the operator format is missing, add it — bullets, one block per system, next 3 actions with owner.
3. Verify framework maps (`owasp-llm-map.md`, `nist-ai-rmf-map.md`, `mitre-atlas-map.md`, `nist-800-53-map.md`) reference the new platform-deployed and ollama evidence where relevant.

**Acceptance:** every evidence path referenced in `CBBP-PLAN/PROVE/*.md` resolves to an existing file:

```bash
grep -rhoE "evidence/[A-Za-z0-9_./-]+\.(json|jsonl)" CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/PROVE/ | sort -u | while read p; do [ -f "Eugene-AI/$p" ] || echo "MISSING: $p"; done
```

Expect zero MISSING lines.

---

## Completion Protocol

1. Write `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BUILD/sprint2-status.md` in the same format as `sprint1-status.md`: ticket table, evidence table, DevSecOps Call.
2. Any task blocked (no cluster, no Ollama): leave a handoff note in sprint2-status.md — what's done, what's blocked, exact command to resume.
3. Run `scripts/test-full-capped.sh` once, at the end. Record the result.
4. Do not touch git. Report completion to J.

| ID | Task | Depends On | Status |
|---|---|---|---|
| S2-T1 | Sync status docs to reality | — | DONE |
| S2-T2 | K8s RBAC role files | — | DONE |
| S2-T3 | Deployed platform BREAK | — | DONE |
| S2-T4 | Live Ollama generation evidence | — | DONE |
| S2-T5 | CrewAI Loop 5 dry-run | T3 | DONE |
| S2-T6 | PROVE packaging polish | T3, T4, T5 | DONE |

**Verified 2026-06-12** by independent verification pass: all evidence files
exist and PASS; T3→T5 gate respected; kind cluster torn down; git untouched.
Residual risk carried forward: unauthorized-retrieval identity-layer bypass
(`evidence/break/unauthorized-retrieval-break-20260610T131529Z.json`) is a
pilot-expansion blocker → route to a future BUILD task, do not standalone-fix.
