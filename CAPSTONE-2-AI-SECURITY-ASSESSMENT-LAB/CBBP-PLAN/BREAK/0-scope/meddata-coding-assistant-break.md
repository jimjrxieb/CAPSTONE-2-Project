# Coding Assistant BREAK Scenarios — MedData Nexus Health Systems

> Filled workpaper for Capstone 2 BREAK phase.
> Lesson: `lessons/06-agentic-coding-assistant-governance.md`
> Client: MedData Nexus Health Systems
> Scope: Codex / Claude Code / Copilot-style engineering assistants — NOT Eugene
> Assessor: jimjrxieb + Eugene (CAP2-AI-001, advisory)
> Date: 2026-06-08
> COMPLY intake: `CBBP-PLAN/COMPLY/meddata-coding-assistant-intake.md`
> BUILD harness: `CBBP-PLAN/BUILD/ai-dev-assist-harness.md`
> Scenario files: `scenarios/ai-assisted-pr-label-bypass.md`, `ai-generated-auth-change.md`, `ai-unsafe-dependency-suggestion.md`

---

## What This BREAK Track Tests

The RAG BREAK track tests whether the AI system fails around data boundaries and retrieval.
This track is different — it tests whether the **governed engineering workflow** fails around
AI-generated code entering production without appropriate review, scanning, or disclosure.

The failure mode here is not a model attack. It is process bypass: a developer takes the
path of least resistance and an AI-generated change reaches production without the governance
friction that exists to catch AI-specific risks.

---

## Scenario 1 — AI-Assisted PR Label Bypass

**Reference:** `scenarios/ai-assisted-pr-label-bypass.md`
**OWASP LLM:** LLM09 (Misinformation / overreliance risk)
**NIST 800-53:** CM-3 (Configuration Change Control), AU-12 (Audit Record Generation), SA-11 (Developer Testing)
**AI RMF:** GOVERN 1.2 (Accountability), MANAGE 2.2 (Mitigations implemented)

### Bypass Being Tested

A developer uses Claude Code or Codex for a material change to the RAG ingestion pipeline
or another code path, but does not apply the `ai-assisted` label before opening the PR.
The PR merges through normal review without AI contribution being disclosed.

**Why this happens in practice:** Labeling feels optional when there is no CI enforcement.
Under time pressure, a developer rationalizes that "it was mostly me, the AI just helped."
The governance trail disappears.

### Control That Should Catch It

1. **PR template** — asks "Did an AI coding assistant materially contribute to this change?" and requires a checkbox before submission.
2. **CI label gate** — a GitHub Action or pre-merge check that fails the CI run if the PR touches sensitive paths and the `ai-assisted` label is absent.
3. **Review policy** — reviewer is required to confirm AI disclosure before approving.

### Evidence That Proves It Worked

| Evidence | What to Show |
|---|---|
| PR metadata | `ai-assisted` label visible on the PR before merge |
| CI run result | Label-check job shows PASS |
| PR template | Disclosure checkbox was filled out |
| Reviewer comment | Reviewer acknowledged AI contribution explicitly |
| Merge record | Merge commit includes named reviewer and timestamp |

### Finding If Controls Fail

> AI-assisted code can merge into the MedData Nexus engineering workflow without disclosure. The organization cannot identify which production code was AI-generated, whether AI-assisted changes received the elevated review appropriate for that category, or whether security gates designed for AI-assisted changes were applied. **Rank: C. Eugene proposes. Human approves.**

**What makes it worse:** Once unlabeled AI-assisted code is in production, it cannot be retroactively identified without replaying the entire commit history against AI detection tools — and even then, detection is unreliable. The audit gap is permanent for that commit.

### Validation Step

1. Submit a simulated PR where AI materially contributed — leave the `ai-assisted` label off.
2. Confirm CI fails with a label-check error before merge is possible.
3. Add the label and re-run CI — confirm the gate passes.
4. Verify the PR record shows the label, CI pass, and named reviewer before merge.

---

## Scenario 2 — AI-Generated Authentication Change Without Security Review

**Reference:** `scenarios/ai-generated-auth-change.md`
**OWASP LLM:** LLM05 (Improper Output Handling), LLM09 (Misinformation / overreliance risk)
**NIST 800-53:** SA-11 (Developer Testing), AC-3 (Access Enforcement), CM-4 (Impact Analysis)
**AI RMF:** MEASURE 2.5 (Output Trustworthiness), MANAGE 2.2

### Bypass Being Tested

Claude Code or Codex generates a change touching authentication or authorization logic —
login flow, token validation, session handling, role checks, or authorization middleware.
The change merges with only standard review — no security-specific reviewer, no auth
behavior test coverage, no explicit check for insecure defaults.

**Why this happens in practice:** AI-generated auth code looks syntactically correct and
passes linting. The reviewer who approves it is not a security engineer and does not
look for auth-specific failure modes. The PR merges because it passes CI and has one
approval.

**Common AI auth errors that reviewers miss:**
- Always-true authorization conditions (`if user or True:`)
- Missing token expiration checks
- JWT signature verification skipped or weakened
- Role checks that default to elevated access on failure
- Privilege escalation via misconfigured role hierarchy

### Control That Should Catch It

1. **CODEOWNERS** — auth-sensitive paths (`auth/`, `middleware/`, `login`, `token`, `session`, `roles`) require a named security reviewer as a required approver.
2. **CI test gate** — auth behavior tests must pass: negative test cases (invalid token, expired session, wrong role) must be present and green.
3. **Security review checklist** — reviewer explicitly confirms: no insecure defaults, no bypass conditions, no privilege escalation, token validation present.
4. **Human-only promotion** — merging auth changes to main/master requires human action; AI cannot merge.

### Evidence That Proves It Worked

| Evidence | What to Show |
|---|---|
| CODEOWNERS file | Auth paths require named security reviewer |
| PR reviewer assignment | Security reviewer is a required approver, not optional |
| Auth test coverage | Negative test cases (invalid token, wrong role, expired session) exist and pass |
| Security review comment | Explicit statement: "Reviewed for insecure defaults, bypass conditions, privilege escalation — none found" |
| Merge record | Named security reviewer is the approving reviewer on record |

### Finding If Controls Fail

> AI-generated code modifying authentication or authorization logic can merge without a named security reviewer, without auth-specific test coverage, and without an explicit check for insecure defaults. AI code generation errors in auth paths are common and not caught by standard linting or functional tests. A single unreviewed AI-generated auth change can introduce a privilege escalation or token bypass that survives in production until exploited. **Rank: B. Human decides. Route to security lead.**

### Validation Step

1. Simulate an AI-assisted change that touches an auth-sensitive file path.
2. Without a security reviewer assigned, confirm CI fails (CODEOWNERS enforcement) or review policy blocks merge.
3. Assign a named security reviewer — confirm the reviewer is required to use the security review checklist.
4. Verify auth behavior tests exist in the PR and are green before merge is permitted.
5. Document the security reviewer's name, decision, and timestamp in the PR record.

---

## Scenario 3 — AI Unsafe Dependency Suggestion

**Reference:** `scenarios/ai-unsafe-dependency-suggestion.md`
**OWASP LLM:** LLM09 (Misinformation / overreliance risk), LLM03 (Supply Chain)
**NIST 800-53:** SR-3 (Supply Chain Controls), SR-4 (Provenance), SA-22 (Unsupported System Components), CM-3
**AI RMF:** MAP 4.1 (Model Integrity — supply chain), MANAGE 2.2

### Bypass Being Tested

Claude Code or Codex suggests adding a new Python package to solve a problem in the RAG
ingestion pipeline. The developer adds it to `requirements.txt`, the package is not pinned
to an exact version, no SCA scan is run, no license check is performed, and the PR merges
because the functionality works.

**Why this happens in practice:** AI suggestions feel authoritative. The package does what
it says it does. The developer does not think of it as a supply-chain decision — they think
of it as solving a problem. The governance step ("justify why this package is necessary, pin
it, scan it, check the license") feels like overhead for something the AI already recommended.

**AI dependency risks that governance catches:**
- **Vulnerable package** — known CVE that SCA would flag
- **Typo-squatted package** — `request` instead of `requests`; `chromadb-client` instead of `chromadb`
- **Unmaintained package** — last release 18 months ago, no active maintainer
- **Over-permissioned package** — installs hooks, modifies environment, calls home
- **Unnecessary package** — standard library or existing dependency already covers the use case
- **Unpinned version** — `>=2.0` silently upgrades to a future breaking or vulnerable version

### Control That Should Catch It

1. **SCA gate in CI** — `pip-audit` or `safety` runs on every PR that modifies `requirements.txt` or `pyproject.toml`. Fails on known CVEs.
2. **License check** — `pip-licenses` or equivalent runs and flags copyleft or unknown licenses.
3. **Maintainer health check** — reviewer confirms: package has active maintainers, recent release, >1,000 stars or equivalent health signal.
4. **Human justification** — PR description must explain: why this package is needed, why existing code/stdlib is insufficient, and what the package does.
5. **Exact version pin** — `package==X.Y.Z` required; ranges (`>=`, `~=`) blocked.

### Evidence That Proves It Worked

| Evidence | What to Show |
|---|---|
| SCA scan output | `pip-audit` result showing no known CVEs for the package and version added |
| License check output | Package license is compatible (MIT, Apache 2.0, BSD) |
| PR description | Written justification: why this package, why not stdlib, what it does |
| Pinned version in manifest | `package==X.Y.Z` in `requirements.txt` — no range specifiers |
| Reviewer comment | Reviewer confirmed: CVE check passed, license OK, justified, pinned |

### Finding If Controls Fail

> AI coding assistants can introduce new dependencies into the MedData Nexus engineering workflow without SCA scanning, license review, or written justification. AI suggestions make dependency additions feel routine and low-risk. A vulnerable, typo-squatted, or over-permissioned package that enters production via an AI-suggested change creates a supply-chain risk that is harder to discover post-merge than pre-merge. **Rank: C. Eugene proposes. Human approves.**

### Validation Step

1. Simulate an AI-suggested dependency addition — add a package to `requirements.txt` without justification or exact pinning.
2. Confirm CI fails with a pip-audit or license check error before merge.
3. Fix: pin the exact version, add a justification in the PR description, confirm pip-audit passes clean.
4. Verify the CI scan output, license check result, and reviewer approval are all in the PR record before merge.

---

## Coding Assistant BREAK Summary

| Scenario | Bypass | Control | Rank | Status |
|---|---|---|---|---|
| PR label bypass | AI-assisted code merges without disclosure | PR template + CI label gate | C | Planned — not executed |
| AI auth change | AI-generated auth logic merges without security review | CODEOWNERS + auth test coverage + security checklist | B | Planned — not executed |
| Unsafe dependency | AI-suggested package added without SCA or justification | pip-audit gate + license check + pin enforcement | C | Planned — not executed |

**Key distinction from RAG BREAK:** These failures are process bypasses, not model attacks. The fix is engineering workflow enforcement — CI gates, PR templates, CODEOWNERS — not model tuning or prompt hardening. The model is not the problem; the governance around it is.

---

## What Evidence Proves the Governed Workflow Works

A client can prove governed coding assistant use when they can show all three of these for a
real AI-assisted change:

1. **The PR record** — `ai-assisted` label present, named reviewer on record, CI passed including SAST and SCA gates.
2. **The scan output** — SAST result, pip-audit result, secrets scan result — all timestamped and linked to the PR.
3. **The review record** — reviewer's explicit comment confirming the AI contribution was considered in the review, not just that the code functionally works.

Without all three, the workflow is a policy claim, not a proven control.
