# Tier 1 — DevSecOps Security Test Matrix

> The automated, shift-left tier. These run in CI/CD every pipeline, are
> standard-backed, and **self-prove for PROVE** — the scan output *is* the
> evidence. This is the "DevSecOps" persona: no human attacker, just gates.
>
> half-A (agent-runnable). Evidence → `Eugene-AI/evidence/break/` + CI artifacts.

## Pipeline Security Scans

| Tool | What it scans | Standard | NIST control | CI workflow | Status |
|---|---|---|---|---|---|
| Semgrep / Bandit | SAST — code flaws | OWASP Top 10, CWE Top 25 | SA-11 | `security-scan.yml` (Wave 2) | to wire |
| pip-audit / Trivy | SCA — dependency CVEs | — | SI-2, RA-5 | `sca.yml` | ✅ exists |
| Gitleaks | secrets in repo | — | IA-5 | `security-scan.yml` | to wire |
| Checkov | IaC — `deploy/k8s/` | CIS, NIST | CM-6 | `security-scan.yml` | to wire |
| Conftest | policy — `deploy/policies/` | OPA/Rego | CM-7 | `security-scan.yml` | to wire |
| kube-bench | CIS Kubernetes Benchmark v1.8 | CKS / CIS K8s | CM-6 | post-deploy job | to wire |
| kube-hunter | cluster recon (read-only) | CKS | RA-5 | post-deploy job | to wire |

**Reading a row:** a tool runs in CI, maps to a recognized standard, anchors to a
NIST control, and its output is the PROVE evidence by a simple call. A clean run
proves the control; a finding becomes a tracked BUILD item. Nothing here needs a
human pentester.

Crosswalk reference: `REFERENCE/control-families/ConfigurationManagement/framework-maps/cis-benchmark-crosswalk.md`.

## AI Dev-Tool Governance Checks (the 4 ai-* scenarios)

These belong in the DevSecOps tier — they govern AI coding tools (Copilot/Codex)
in the pipeline, not Eugene's RAG runtime. Each validates an `ai-dev-assist-harness`
guardrail. Backed by **NIST AI RMF GOVERN/MANAGE** + the repo's `AI-DEV-ASSIST-GUARDRAILS`.

| Scenario | What it validates | Gate / control | Standard |
|---|---|---|---|
| `ai-assisted-pr-label-bypass` | AI-authored PR must carry the assist label; CI blocks unlabeled | `ai-assist-label-check.yml` | AI RMF GOVERN 4.2 |
| `ai-unsafe-dependency-suggestion` | AI-suggested dep must pass pip-audit before merge | SCA gate | SI-2, AI RMF MANAGE 4.1 |
| `ai-generated-auth-change` | AI change to auth path requires human review (CODEOWNERS) | CODEOWNERS + review | AC-6, AI RMF GOVERN 2.2 |
| `ai-runtime-drift` | deployed image/config matches the reviewed source | drift check | CM-6, AI RMF MEASURE 2.7 |

**Validation method:** purposely submit the violating change (unlabeled AI PR,
unsafe dep, unreviewed auth edit, drifted image) → confirm the CI gate blocks it.
This is "break-and-watch" applied to the pipeline instead of the app. Evidence:
the CI run that rejected it.

## Self-Proving for PROVE

Tier 1 is the cheap, high-volume evidence layer. The PROVE client scorecard rows
for "pipeline passes security scans" (SA-11, SI-2, IA-5) and "platform controls
hold" (CM-6, CM-7) are satisfied by these scan outputs directly — no narrative,
no manual collection. Run the pipeline, keep the artifacts, point the scorecard at
them.
