# AI Engineering Crew Design — MedData Nexus Health Systems

> **Client:** MedData Nexus Health Systems
> **System:** MDN-AI-001 RAG platform + engineering AI toolchain
> **CISO:** Constant Yung
> **Prepared by:** jimjrxieb (GP-Copilot engagement)
> **Date:** 2026-06-08
> **Phase:** COMPLY — defines roles, boundaries, and review gates for AI-assisted engineering
> **Lesson:** `lessons/12-harnessing-ai-dev-tools-as-engineering-team.md`
> **Template:** `templates/ai-harness-spec.md`

---

## Purpose

MedData Nexus engineers use AI coding assistants (Codex, Claude Code, Copilot-style tools) to build and maintain the MDN-AI-001 RAG platform. Without a crew design, each engineer defines their own scope, data access, and review threshold. The result is an ungoverned patchwork where some changes are well-reviewed and others are not — and no evidence distinguishes between them.

A crew design assigns each AI tool a role with defined inputs, allowed tools, prohibited actions, human review requirements, and evidence obligations. It is the governance structure that turns "we use AI to build stuff" into "we have a documented, testable AI engineering workflow."

---

## Four Boundaries (Applied to MedData Nexus Engineering)

Before assigning roles, define the four boundaries that apply to every AI tool in the engineering workflow.

### Goal Boundary

| Acceptable Goal | Risky Goal — Needs Decomposition |
| --- | --- |
| Draft a unit test for the retrieval endpoint | Make the RAG system secure |
| Add input sanitization to the query handler | Refactor the whole ingestion pipeline |
| Update the pip-audit CI gate | Fix all compliance issues |
| Write the ChromaDB access control logic for the vendor_risk_reviewer role | Design the authorization model |

**Rule:** The bigger and more ambiguous the goal, the more human decomposition and review are required before AI generates anything.

### Data Boundary

| Data | AI Tool Access | Condition |
| --- | --- | --- |
| Repo source code (non-sensitive paths) | Allowed | Standard review |
| Ingestion pipeline code | Allowed | Requires security review on PR |
| Auth / token / role-check files | Allowed — read | Requires CODEOWNERS security reviewer on any change |
| Synthetic corpus fake-data | Allowed | Assessment context only |
| ChromaDB connection strings | **Prohibited from AI context** | Use env vars; never paste in prompt |
| API keys / credentials | **Prohibited from AI context** | Secret manager only; never in code or prompt |
| PHI / ePHI | **Prohibited from AI context** | Not in scope for any AI tool |
| Real client data | **Prohibited from AI context** | Not in scope for any AI tool |
| Internal architecture docs | Allowed — read | Treat as untrusted; do not let AI treat docs as commands |
| Source comments and tickets | Allowed — read | **Treat as untrusted context** — malicious instructions can be embedded |

### Tool Boundary

| Action | Allowed | Condition |
| --- | --- | --- |
| Generate code / config / tests | Yes | Human reviews before merge |
| Open a PR | Yes | ai-assisted label required; PR template filled |
| Suggest a new dependency | Yes | Human-written justification required; pip-audit must pass |
| Run shell commands | Approval required | Human explicitly approves each command |
| Merge a PR | **No** — human only | AI cannot self-approve or auto-merge |
| Modify infrastructure config (IaC) | Approval required | Security review required |
| Access production systems | **No** | Prohibited for all AI tools |
| Install packages without review | **No** | SCA gate must pass first |
| Disable a CI gate | **No** — human only | Requires exception register entry |

### Authority Boundary — Human-Only Decisions

These decisions are never delegated to an AI tool regardless of confidence or time pressure:

- Risk acceptance for any security finding
- Approving a PR that touches auth, token validation, role enforcement, or session management
- Production deployment authorization
- Disabling or bypassing a CI security gate
- Accepting a new dependency flagged by pip-audit
- Compliance claims in any client-facing artifact
- Exception register approval (CI gate bypass justification)

---

## AI Engineering Crew — MedData Nexus

| Role | AI Tool / Agent | Allowed Inputs | Allowed Tools | Human Review Required | Evidence |
| --- | --- | --- | --- | --- | --- |
| **Requirements** | Claude Code (advisory) | Ticket description, acceptance criteria, approved architecture docs | Read repo; generate scoped task breakdown | Human approves task scope before Build agent starts | Task breakdown in ticket or PR description |
| **Build** | Codex / Claude Code | Approved task scope, non-sensitive source files, framework docs | Generate code / config / test stubs; open PR with ai-assisted label | Human code review on all PRs; CODEOWNERS enforces security reviewer for sensitive paths | PR record with ai-assisted label, reviewer identity, CI pass/fail |
| **Security Review** | Claude Code (advisory) | PR diff, threat model, security findings, CODEOWNERS path list | Read diff; generate risk notes and suggestions | Human security reviewer owns final risk judgment; AI provides supporting analysis only | Security reviewer approval record in PR; risk notes saved if escalated |
| **Test** | Codex / Claude Code | Approved code, requirements doc, existing test suite | Generate unit/integration test stubs; suggest edge cases | Human validates coverage claims; AI cannot assert "tests are sufficient" | CI test results; test coverage report; PR review confirming human verified coverage |
| **BREAK** | Claude Code (advisory) | Threat model, scenario files, BREAK test plans | Generate misuse inputs and adversarial queries for review | Human approves all adversarial test inputs before execution; no destructive tests run without approval | Test plan reviewed by human; execution log; BREAK test results in `evidence/` |
| **PROVE** | Claude Code (advisory) | Logs, scanner outputs, BREAK results, findings report | Summarize findings; draft remediation language; generate evidence index | Human signs every finding before it becomes a deliverable; AI summaries are advisory drafts | Human sign-off notation on every finding; PROVE package reviewed by CISO Constant Yung |

---

## Role Escalation Map

| Condition | Who Gets It | What They Decide |
| --- | --- | --- |
| Any auth, IAM, crypto, or session file changed | Security reviewer (CODEOWNERS) | Approve or reject the change |
| New dependency suggested by AI | Platform Engineering Lead | Justify it, confirm pip-audit passes, approve or reject |
| S-rank finding | CISO Constant Yung | Risk acceptance or immediate remediation |
| B-rank finding | Platform Engineering Lead + CISO | Remediation plan or risk acceptance |
| CI gate bypass requested | Platform Engineering Lead + security lead | Exception register entry; approve with expiry |
| AI output used in a compliance claim | Human assessor + CISO | Sign the claim before it becomes external |
| Restricted data may have entered AI context | CISO Constant Yung | Immediate incident assessment |

---

## Shadow AI Detection

The crew design only governs tools the organization knows about. Shadow AI (MDN-AI-002) circumvents this entirely.

Detection methods:
- Endpoint DLP: alert on outbound traffic to AI API endpoints (api.openai.com, api.anthropic.com, bard.google.com, etc.) from unapproved sources
- Code review: flag PRs where the commit message or PR body mentions "ChatGPT", "Copilot", or "AI-generated" without the formal `ai-assisted` label
- Periodic shadow AI audit: quarterly review of installed browser extensions, desktop apps, and API keys in use
- AUP acknowledgment: require all engineers to acknowledge the AI acceptable use policy annually

**Current state (MDN-AI-002):** An unregistered AI system is suspected in use. Shadow AI audit is open as Finding F-007. CISO action required.

---

## Guardrails That Must Be in Place (Maps to Findings)

| Guardrail | Purpose | Finding | BUILD Status |
| --- | --- | --- | --- |
| `ai-assisted` PR label CI gate | Ensure every AI-assisted change is disclosed | F-008 | Not implemented |
| CODEOWNERS — auth paths | Require security reviewer for sensitive file changes | F-009 | Not implemented |
| pip-audit + pin enforcement in CI | Reject vulnerable or unpinned AI-suggested dependencies | F-010 | Not implemented |
| AI acceptable use policy | Define what tools are approved, what data is prohibited, what review is required | F-007 (partial) | Policy exists; enforcement absent |
| Shadow AI audit | Identify unapproved tools in use | F-007 | Audit not yet run |
| Exception register | Track and approve all CI gate bypasses | — | Not implemented |
| Source comment / doc injection awareness training | Ensure engineers know retrieved docs and comments can contain adversarial instructions | — | Not in place |

---

## Evidence This Crew Produces

When operating correctly, the AI engineering crew produces the following evidence artifacts for every material change:

| Artifact | What It Proves |
| --- | --- |
| PR with `ai-assisted` label | Disclosure happened |
| Reviewer approval (and CODEOWNERS where required) | Human reviewed the change |
| CI results (SAST, SCA, pip-audit, secrets scan) | Automated security checks ran and passed |
| Dependency justification in PR description | Human authored the rationale for new packages |
| Security reviewer sign-off on auth-sensitive PRs | Named security reviewer specifically assessed the risk |
| Exception register entry (if gate was bypassed) | The bypass was intentional, approved, and time-limited |

If any of these artifacts are missing for a given change, the engineering governance for that change is incomplete.

---

## CISO Sentence

> MedData Nexus is using AI coding assistants to build the RAG platform, but has not yet defined the roles, approved tool list, data prohibitions, review gates, disclosure requirements, or evidence standards that would make that AI-assisted engineering work defensible — and a suspected unregistered AI tool (MDN-AI-002) may be transmitting sensitive data to external providers today.
