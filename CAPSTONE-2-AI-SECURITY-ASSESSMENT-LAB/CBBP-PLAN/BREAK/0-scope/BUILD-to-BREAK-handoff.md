# BUILD to BREAK Handoff — MedData Nexus / Eugene

> Authored in plan mode. **Status:** APPROVED — BREAK Wave 2 released.
> Signed by J 2026-06-12. Falco deploy, CI scans, and scenario runs are go.

## Engagement

- Client: MedData Nexus Health Systems
- System: Eugene — internal RAG compliance assistant (MDN-AI-001)
- Slot: slot-5
- Date: 2026-06-12
- Engineer: build-engineer → break-orchestrator

## BUILD Artifacts Shipped

| Control ID | Artifact | What Was Deployed |
|---|---|---|
| SI-4 | output filter | PHI/secret redaction at response boundary |
| AC-3, AC-6 | role-filtered retrieval | role-scoped retrieval (POAM-0001 fix in flight) |
| AU-2, AU-10 | audit hash-chain | tamper-evident query/decision log |
| SI-7, CM-3 | manifest-gated ingestion | poisoned/unapproved doc rejection + owner alert |
| SC-7, SC-5 | NetworkPolicy + rate limit | Chroma isolation + per-token throttle (proven on kind) |
| IA-5 | query auth | bearer-token-derived identity |
| CM-6, CM-7 | K8s RBAC + Kyverno policies | namespace-scoped SA; admission policies |

## What Was Deferred (out of BREAK scope)

| Item | Reason | POA&M |
|---|---|---|
| Live AWS EKS, external secrets, TLS automation, prod ingress | Pre-production; pilot doesn't need them | P3 (tracked) |
| Full CrewAI orchestration | Advisory until controls stable | P4 |

## Two-Tier BREAK Scope

### Tier 1 — DevSecOps (CI/CD security tests, half-A)
Automated, self-proving, every pipeline. See `devsecops-test-matrix.md`.
- SAST (Semgrep/Bandit), SCA (pip-audit/Trivy), secrets (Gitleaks)
- IaC (Checkov), policy (Conftest), CIS K8s (kube-bench), recon (kube-hunter)
- AI dev-tool governance: the 4 ai-* scenarios validate `ai-dev-assist-harness` gates

### Tier 2 — Pentester (adversarial scenarios, break-and-watch)
Purposely break a control, confirm the alert fires. See `pentester-scenarios/`.
- 8 rag-* scenarios, each backed by OWASP LLM / MITRE ATLAS / CySA / NIST
- Alert backend: Falco + local SIEM (deployed in Wave 2) + Eugene audit log

## Known Fragile Areas (check first)

- **POAM-0001 identity layer** — unauthorized-retrieval bypass. Should close
  (Sonnet in flight) BEFORE the rag-unauthorized-retrieval scenario runs, so the
  scenario validates the fix instead of re-confirming the gap.
- **Audit-logging + source-leakage** — no runners yet; net-new in Wave 2.

## J Sign-Off Gate

- [x] **Approved by:** J · break-approver (senior CISSP/CISO) · 2026-06-12
- [x] **Approval scope:** half-A autonomous (Falco deploy, scans, detection-validation);
      half-B (any prohibited external tool) stays human-run. Dev/staging only.
- **Precondition met:** POAM-0001 CLOSED (run 20260612T134146Z) — unauthorized-retrieval
  scenario will validate the fix, not re-confirm the gap.

## Next Step (after sign-off)

```text
Read AGENTS.md. Engagement config at GP-CONSULTING/config/engagement.yaml.
Use CBBP-PLAN/BREAK/BUILD-to-BREAK-handoff.md as approved BREAK scope.
Wave 2: deploy Falco + local SIEM, wire the DevSecOps CI scans, build the 2 missing
runners, then run the pentester catalog — break each control, confirm the alert fires,
capture evidence under Eugene-AI/evidence/break/.
When done, fill in CBBP-PLAN/PROVE and the BREAK-to-PROVE handoff. Do not touch git.
```
