# 000 — Consulting Army: North-Star Build Plan

**Status:** Draft — awaiting human review (per BuildPlans lifecycle).
**Date opened:** 2026-06-11
**Owner:** J (supervisor of the shadow army)
**Scope:** Turn GP-CONSULTING from a CBBP framework-with-agents into a **releasable agentic workforce** that runs CBBP against any client app or model — with humans owning B/S-rank and the agents clearing C-rank-and-below grunt work.

**The thesis (the moat):** the product is not the agents — agents get more capable on their own (Claude Code → Codex → eventually Mythos). The durable value is the **harness and guardrails** that make that power safe to point at a real client. "Who has the best harness and guardrails for Claude Code" is the arc reactor for the suit — the thing that lets the operator channel the shadow monarch's power without being consumed by it. Every item in this plan ladders up to that: a flawless, control-mapped, human-gated harness around increasingly powerful agents.

---

## 1. The operating model (who does what)

The mental model: a guild that takes contracts, and a shadow army that does the work inside them.

| Role | Rank authority | Does |
|---|---|---|
| **Constant + senior experts** (the guild / "guidemaster") | B/S-rank | Talk to the client, run intake like a CISO/CEO would, scope the engagement, accept risk, sign off deliverables. This is the client-facing front of **COMPLY**. |
| **J** (supervisor) | commands the army; escalates B/S to the guild | Points the army at the target, reviews the C-rank gates, supervises the shadows. |
| **The shadow army** (CBBP agents) | **C-rank max — hardcoded** | The grunt work: assessment drafts, gap analysis, build tasks, scans, validation scripts, evidence packaging. Propose; never approve risk. |

**The pitch this encodes:** Constant pays for the tokens / local-model server. J + the shadow army take care of the C-rank-and-below load so the senior experts spend their time on clients and judgment, not grunt work. When a C-rank gate needs clearing, the army goes in.

**The hard boundary stays:** every agent is capped at C-rank. The army drafts and proposes; a human (the guild for client-facing calls, J for internal gates) approves. That cap is what makes this safe to release on a real client — it's the difference between "agentic workforce with guardrails" and "autonomous risk."

### Where everyone lives (the phase map)

The CBBP phases are not just a workflow — they're territory, and each has a resident.

| Phase | Resident | Role |
|---|---|---|
| **1-COMPLY** | **Constant** + GRC agents + audit agents | Constant's house. He runs client intake CISO/CEO-style; the GRC/audit agents support. Output: scope + the client's wishlist. The client-facing front. |
| **2-BUILD** | **J** + the shadow army | J's house. DevSecOps / CKS / CICD. Constant hands J the instructions + wishlist; J and the shadows build. |
| **3-BREAK** | **J** + the shadow army | J's house too. The **BB (Build↔Break) loop** runs here. Eventually Mythos-driven — which is *why* the guardrails here must be flawless: it's where the most powerful, most dangerous capability runs. |
| **4-PROVE** | **Constant** | Constant's review surface. He sees results, delivers them to the client, or uses SME status to correct/enhance the shadows' work. The goal: maximum load taken off Constant. |

### Model/tool routing (which shadow for which job)

| Tool | Use for | Why |
|---|---|---|
| **Claude Code** | Default driver across BUILD/BREAK; interactive supervision | Best harness target; where the guardrail investment compounds |
| **Codex** | Heavy code-change execution within build tasks | Throughput on implementation |
| **BERU** (local/air-gapped) | Anything too sensitive for an external API — client-confidential or regulated data | Data never leaves the environment |
| **Mythos** (future, 3-BREAK) | The most powerful adversarial validation | Requires the flawless harness — that's the whole point of hardening BREAK now |

### Reference-only, not operational

`4CL/` is a **reference checklist** to confirm the army covers the six lanes — it is not part of the operational pipeline. The real decoupling work happens on the agents in `<phase>/agents/` and `.claude/agents/`.

---

## 2. Where the army stands today — six-lane capability audit

Lanes are ConstantLaunch's service lanes (the coverage rubric). Rating answers: *can the agents do the C-rank grunt work for this lane today?*

| Lane | Coverage | Built today | Proven on target | Gap to close |
|---|---|---|---|---|
| Compliance & Governance | 🟢 Strong | NIST 800-53 + CSF/FedRAMP/SOC2/CMMC lenses; COMPLY orchestrator + 7 specialists; PROVE poam/gap/validate/report/evidence-api/vendor-normalization | Portfolio + Eugene | — (the spine; most mature) |
| Platform Engineering | 🟢 Strong | BUILD platform-ops crew; BREAK rbac-audit, container-hardening, kube-bench, health checks | Portfolio (slot-1) | — (Katie is the deployed K8s agent) |
| Cybersecurity (core) | 🟢 Strong | BREAK run-all/src scanners, scan-and-map, DAST; red-team + detection-validation agents | Portfolio | — |
| DevSecOps | 🟡 Good | build-engineer CI gates; gha-ci-fixer; SAST/SCA/secret scanners; harden-cicd playbook | Portfolio | Drop-in per-client CI pipeline scaffold (build-from-scratch, not just fix-existing) |
| AI Integration | 🟡 Strong method / thin tooling | 02-AI-RMF-LENS (AI RMF, OWASP LLM, ATLAS, red-team playbooks); comply-ai-risk agent; AI intake/harness/boundary templates | **Eugene (slot-5)** | AI break-runners (injection, corpus poison, PHI/secret scan) live *inside Eugene*; not generalized into reusable 3-BREAK collectors / an AI red-team crew |
| Cloud Architecture | 🟠 Partial | Cloud intake/scoping questionnaires; checkov/terraform + infra-scanner remediation playbooks; FedRAMP lens | lab only | **Weakest.** No dedicated cloud agent; no runnable Prowler/IAM-analysis/Terraform-security collector crew |

### Agent roster today (the army as it stands)
- **COMPLY (8):** orchestrator, scope-intake, control-scope, ai-risk, ssp-review, gap-analysis, evidence-trace, handoff-router
- **BUILD (6):** build-orchestrator, build-planner, build-review, comply-to-build, dev-environment, implementation
- **BREAK (2):** red-team, detection-validation
- **PROVE (4):** evidence-collector, poam-generation, reporting, risk-classification

### Two structural findings
1. **The army is COMPLY-heavy and BREAK-light.** COMPLY has an orchestrator + 7 specialists; BREAK has 2 agents. For a balanced army, BREAK (and to a lesser extent PROVE) need their specialist crews fleshed out to mirror COMPLY's orchestrator+specialists pattern.
2. **Two lanes have method but not portable tooling.** AI Integration's real grunt-work tools live in Eugene, not in GP-CONSULTING; Cloud has playbooks but no executable agent. These are the highest-leverage gaps because the *capability is proven* — it just isn't generalized into the army yet.

**Bottom line:** 2.5 of 6 lanes are army-ready. The path to "releasable on any client" is: generalize AI tooling, build the cloud crew, balance the BREAK roster, and decouple from internal paths.

---

## 3. CBBP-aligned build roadmap

Organized by phase, because the army is organized by phase. Each item is C-rank grunt-work the agents will own once built.

### COMPLY — the front the guild drives
COMPLY is the most complete. Remaining work is packaging, not capability.
- [ ] **Decouple intake/scoping from internal paths.** The COMPLY crew should take a client `engagement-root` + framework set, not assume slot/GP-S3 paths. (Foundation for "any client.")
- [ ] **Client-intake bridge.** A thin contract so the guild's CISO/CEO-style intake feeds the scope-intake agent directly (questionnaire → scoped engagement).

### BUILD — make it true
BUILD has a full crew + comply-to-build contract.
- [ ] **DevSecOps lane:** a reusable, drop-in CI security pipeline scaffold (SAST + SCA + secret + IaC + image gates) the build crew can drop into a new client repo — not just gha-ci-fixer for existing pipelines.
- [ ] **Cloud lane:** a cloud-build agent for IAM least-privilege, encryption, and Terraform-security baselines.

### BREAK — prove it stays true (biggest roster gap)
- [ ] **Generalize Eugene's AI break-runners into a reusable AI red-team crew** under `3-BREAK`: prompt-injection, corpus-poisoning, unauthorized-retrieval, output-safety. This is the single highest-value item — it turns a proven capability into army tooling and lights up the AI Integration lane.
- [ ] **Cloud break crew:** runnable Prowler / IAM-analysis / Terraform-scan collectors with control mapping.
- [ ] **Balance the roster:** add specialist BREAK agents to match COMPLY's depth (e.g. a break-orchestrator that routes to scanner / red-team / detection-validation specialists). Keep the half-A (deploy detection) vs half-B (human-run attacks) split — that boundary is a release-safety feature.

### PROVE — show the guild and the client
PROVE has generators + evidence-api.
- [ ] **One-command evidence package per engagement** keyed to `engagement-root`, so a finished engagement emits the client report + POA&M + evidence bundle without manual assembly.
- [ ] **Dual-format output** (CISO summary + operator handoff) wired into the reporting agent as default.

### Cross-cutting — what makes it "releasable on any client"
- [ ] **Harden the harness + guardrails (the moat — first-class, ongoing).** This is the arc reactor, not a side task. Concretely: keep every agent C-rank capped; keep the BREAK half-A (deploy detection) vs half-B (human-runs-attacks) split and the attack-tool-blocking hook; make the guardrails strong enough that an increasingly powerful driver (Codex now, Mythos later) cannot exceed its lane. **3-BREAK is the priority** — it's where the most dangerous capability will run, so its guardrails must be flawless *before* Mythos arrives, not after.
- [ ] **Decouple from GP-S3 / slot / internal naming** → per-client `engagement-root` config. (This is the gate on "any client" for every lane.)
- [ ] **Orchestration runtime** (section 4).
- [ ] **PROVE-on-target validation:** run the full loop against Eugene (model) and Portfolio (app) end-to-end, capture the evidence in `GP-SECLAB/target-application/` as the proof the army works.

---

## 4. Runtime decision — CrewAI vs Codex vs Claude Code

The existing design principle (playbook-as-brain) already answers this, and we keep it:

> **The agent contracts are the source of truth. The runtime is swappable.** Each agent is a portable Markdown contract (`<phase>/agents/<name>/README.md`); the runtime (Claude Code subagent, Codex, or CrewAI) is just a binding that reads the same contract and the same normalized-state files.

**Recommendation: support two runtimes, don't pick one.**

| Runtime | Use it for | Status |
|---|---|---|
| **Claude Code subagents** | Interactive engagements, J supervising live, development | ✅ working today (`.claude/agents/`) |
| **CrewAI** | Autonomous / headless / scheduled runs on Constant's local model — the "shadow army runs while you sleep" mode | 🟡 scaffold exists (`2-BUILD/runners/crewai/`); needs wiring to normalized state + a local-model backend |
| **Codex** | Heavy code-change execution within a build task | 🟡 used in past tickets; keep as an executor option |

**Why both:** Claude Code is how J drives the army interactively now. CrewAI is the path to the autonomous-workforce-on-a-local-model vision Constant pays the server for. Both must read/write the same contracts and normalized YAML — so neither becomes a lock-in and the army stays portable. The CrewAI runner must never become the source of truth; it executes the contracts, it doesn't replace them.

**Next runtime step:** wire the existing CrewAI scaffold to one full phase (BREAK is the best candidate — it's the roster gap and the AI red-team crew is the showcase) against a local model, reading the same agent contracts.

---

## 5. Open decisions (human call — not executed)

These are J's calls, flagged here rather than done:

1. **Rename GP-CONSULTING → CONSULTING-ARMY?** The "army" framing is strong for the pitch. But the directory is referenced across thousands of files, the parent `CLAUDE.md`, rules, and memory. **Recommendation: keep the directory name `GP-CONSULTING`, adopt "Consulting Army" as the product/branding name.** Rename the *concept and READMEs*, not the path — a path rename is high-risk for low benefit. Revisit only if there's a clean reason.
2. **Update GP-COPILOT top-level README/goals to the agentic-army framing?** Worth doing, as a deliberate edit after this plan is approved — so the stated mission matches the build direction. Propose: a focused README update, reviewed, not a sweeping rewrite.
3. **Where does PROVE-on-target evidence live?** Recommendation: keep using `GP-SECLAB/target-application/slot-N/` as the proving ground (Eugene = model proof, Portfolio = app proof); the army's job is validated there before it's "releasable."

---

## 6. Definition of done (for "releasable agentic workforce")

The army is releasable on a new client when:
- [ ] All six lanes have at least C-rank grunt-work coverage (AI generalized, cloud crew built).
- [ ] The full CBBP loop runs against a target via an `engagement-root` with no internal-path coupling.
- [ ] BREAK roster is balanced (orchestrator + specialists, AI red-team crew live).
- [ ] One runtime (Claude Code) drives it interactively; CrewAI runs at least one phase headless on a local model.
- [ ] The loop is proven end-to-end on Eugene (model) and Portfolio (app), with evidence captured.
- [ ] Every agent is still C-rank capped; humans own every B/S decision.

When those hold, the claim "an agentic workforce backed by NIST and other standards that runs CBBP against any client, with human-owned risk gates" is **defensible with file paths** — not aspirational.

---

## 7. Sequencing (highest leverage first)

**Running through all of it (the moat):** harness + guardrail hardening is not a step — it's the discipline applied at every step. Each new agent or collector ships with its C-rank cap, control mapping, and (in BREAK) the human-run boundary intact. Nothing below is "done" if it weakened the harness.

1. **Decouple to `engagement-root`** — unblocks "any client" for every lane.
2. **Generalize Eugene's AI break-runners into a 3-BREAK AI red-team crew** — turns proven capability into army tooling; lights up the AI lane (the differentiator), under flawless BREAK guardrails.
3. **Build the cloud crew** — closes the weakest lane.
4. **Balance the BREAK roster** (break-orchestrator + specialists) — and harden it, because this is the seat Mythos will eventually take.
5. **Wire CrewAI to BREAK on a local model** — proves the autonomous-workforce mode.
6. **Full-loop PROVE-on-target** against Eugene + Portfolio — the proof.

