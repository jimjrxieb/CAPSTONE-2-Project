# 01 — Intake Questionnaire

**Client:** `<client name>`
**Stage:** Discovery
**Date:** `<YYYY-MM-DD>`
**Conducted by:** `<your name>`

Goal of this doc: turn the first conversation into a scoped engagement. Ask these, write the answers, and you'll know what you're being asked to do and what's at stake.

> Tip: don't just collect answers — listen for the *real* driver (a deal, an audit deadline, a customer's fear). That driver sets priority later.

---

## Business context
- **What are you trying to achieve, and by when?** `<answer>`
- **Who is the buyer of this work (technical owner + business owner)?** `<answer>`
- **What happens if it's late or doesn't happen?** `<answer>`
- **Is there a hard deadline driving this (deal, audit, launch)?** `<answer>`

## System & data
- **What does the system do, in one sentence?** `<answer>`
- **What's the most sensitive data it touches?** `<answer>`
- **Is it multi-tenant? How is tenant separation enforced today?** `<answer>`
- **Where does it run (cloud, K8s, serverless, on-prem)?** `<answer>`
- **What's the tech stack?** `<answer>`

## AI / ML specifics *(skip if no AI in scope)*
- **What model, and where does it run (hosted API, self-hosted)?** `<answer>`
- **What can the AI access (data sources, tools, retrieval)?** `<answer>`
- **How is access scoped per user/tenant at query time?** `<answer>`
- **Has anyone tested it for prompt injection or data leakage?** `<answer>`
- **Is there a human in the loop before AI output reaches an end user?** `<answer>`
- **Where does untrusted input enter the prompt (user text, retrieved docs)?** `<answer>`

## Current security posture
- **Any existing compliance work or certifications?** `<answer>`
- **What security gates exist in CI/CD today (SAST, SCA, secret scan)?** `<answer>`
- **How are secrets managed? Any known secrets in source control?** `<answer>`
- **What logging/audit exists? Is anyone reviewing it?** `<answer>`
- **How is access control handled (cloud IAM, K8s RBAC)?** `<answer>`
- **When was the last time anything was tested adversarially?** `<answer>`

## Scope & constraints
- **What's explicitly in scope? Out of scope?** `<answer>`
- **What can the client's team own vs. what do they need from you?** `<answer>`
- **Any change-freeze windows, prod-access limits, or authorization needed for testing?** `<answer>`

---

## Engagement summary (fill after the call)

- **Primary goal:** `<one sentence>`
- **Hard deadline:** `<date or "none">`
- **Top worry (the real driver):** `<the thing that keeps the buyer up at night>`
- **Frameworks in play:** `<SOC 2 / HIPAA / FedRAMP / NIST AI RMF / OWASP LLM / ...>`
- **Recommended first focus:** `<highest blast-radius + deadline-driving item>`

→ Next: fill in **[02-gap-analysis.md](02-gap-analysis.md)**.
