# Engagement Kit

Blank, reusable templates for running an AI security / consulting engagement end to end.

These templates were pulled from the Eugene / Capstone 2 workflow: intake, gap analysis, roadmap, build log, validation, and report. The real example is [capstone-as-engagement.md](capstone-as-engagement.md).

The point: an engagement starts from a template, not a blank page. Copy this folder per client, fill it in stage by stage, and you have a consistent, evidence-first delivery every time.

---

## How to use

1. Copy the six numbered template files from `4CL/` to a working location for the new client.
2. Work the files in order — each stage feeds the next.
3. Anything in `<angle brackets>` is a fill-in. `[ ]` is a checkbox.
4. Keep the control IDs. They're what turn "we did some security work" into auditor-ready evidence.

---

## The files (in order)

| # | File | Stage | Use it to |
|---|---|---|---|
| 1 | [01-intake-questionnaire.md](4CL/01-intake-questionnaire.md) | Discovery | Turn the first conversation into scope |
| 2 | [02-gap-analysis.md](4CL/02-gap-analysis.md) | Discovery | Record where the client stands vs. where they need to be |
| 3 | [03-roadmap.md](4CL/03-roadmap.md) | Strategy | Prioritize fixes into waves with owners + dates |
| 4 | [04-build-log.md](4CL/04-build-log.md) | Implementation | Record each control built, what changed, why |
| 5 | [05-validation-checklist.md](4CL/05-validation-checklist.md) | Optimization (validate) | Test each control; nothing is "done" until it passes |
| 6 | [06-client-report.md](4CL/06-client-report.md) | Optimization (report) | 1-page exec summary + POA&M of open items |

---

## The two rules that keep quality high

- **Map every action to a control.** Before you do a thing, name the control it satisfies. After, label the output as evidence for that control. This is what an auditor and a security-minded customer both want to see.
- **Tested beats assumed.** A control isn't done when it's configured — it's done when a test confirms it works. That's why stage 5 exists between building and reporting.

---

## Control quick-reference (the ones that come up most)

| Control | Name | Shows up as |
|---|---|---|
| AC-3 / AC-4 | Access Enforcement / Information Flow | Tenant isolation, data boundaries |
| AC-6 | Least Privilege | RBAC, IAM scope-down |
| AU-2 / AU-6 | Event Logging / Audit Review | Logging + a review cadence |
| CM-3 | Change Management | PR review gates, CODEOWNERS |
| CM-6 / CM-7 | Config Settings / Least Functionality | Container hardening, baselines |
| IA-5 | Authenticator Management | Secrets management, rotation |
| SA-11 | Developer Testing | SAST / CI security gates |
| SC-7 | Boundary Protection | NetworkPolicy, segmentation |
| SI-2 / RA-5 | Flaw Remediation / Vuln Monitoring | Image + dependency scanning |
| SI-10 | Input Validation | Prompt injection + output filtering (AI) |
| CA-2 / CA-5 | Control Assessment / POA&M | Gap analysis, open-item tracking |

For AI work, pair these with **OWASP LLM Top 10** (LLM01 injection, LLM06 sensitive-info disclosure, etc.) and **NIST AI RMF** so the AI-specific risks have framework language too.
