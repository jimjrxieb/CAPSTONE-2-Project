# Lesson 10 - Executive Advisory

**Status: COMPLETE — 2026-06-08**
**Deliverable:** executive-ready risk explanation practice
- Fixed Two-Minute Defense: removed false past-tense claim of executed BREAK tests. Accurate version states pipeline was built and baseline retrieval run; adversarial tests are designed but pending execution.
- Added five capstone practice items (CISO sentence, engineering sentence, remediation priority, honest limitation, scale/no-scale recommendation) grounded in actual project state.

## What To Master

The final skill is translation.

You must explain technical AI risk in language a CISO, engineering leader, or hiring manager can trust.

## Questions I Should Ask Myself

- What is the risk in one sentence?
- What business outcome could be affected?
- What evidence proves the issue?
- What is the highest-priority fix?
- What can wait?
- What would I tell engineering?
- What would I tell security?
- What would I tell leadership?
- What would I not overclaim?

## Executive Structure

Use this format:

1. What we assessed.
2. What worked.
3. What failed or remains unproven.
4. Why it matters.
5. What to fix first.
6. Whether to pilot, scale conditionally, pause, or remediate.

## Reviewer Questions

### Why does this capstone map to GuidePoint work?

This capstone maps to GuidePoint because it is not just a chatbot demo. It is a client-style AI security assessment lifecycle. I define scope and data boundaries, build a governed RAG and assessment workflow, test AI-specific failure modes, map findings to NIST RMF, NIST AI RMF, NIST 800-53, OWASP LLM, and MITRE ATLAS, then package the evidence into a risk register, remediation roadmap, and scale/no-scale recommendation.

### What would you do first with a real client?

I would start with COMPLY: identify the business use case, system owner, technical owner, risk owner, users, data classes, AI tools, third-party model paths, and the highest-risk workflow. Then I would ask for the evidence that should already exist: architecture diagrams, corpus manifest, access controls, logging, approval records, incident process, and any pilot authorization. I would avoid testing or recommending scale until scope and evidence are clear.

### How would you assess a RAG system you did not build?

I would treat the RAG system as a data-boundary and retrieval-governance problem. First I would inspect what documents are in the corpus, who approved them, how they are classified, how they are chunked and tagged, and whether retrieval enforces user roles. Then I would test the claims: unauthorized retrieval, poisoned documents, secrets in corpus, source leakage, missing output filtering, and missing audit logging.

### How would you secure Codex or Claude Code for engineers?

I would treat AI-generated code as a draft that must go through a governed engineering workflow. The controls are approved tool use, repo scope, no real secrets or client data in prompts, AI-assisted PR disclosure, CODEOWNERS review for auth/IAM/crypto/logging changes, dependency review, SAST/SCA/IaC/secrets scans, and evidence that a human reviewed the change before merge.

### What is the difference between a policy and evidence?

A policy says what should happen. Evidence proves what actually happened. A policy may say AI-generated high-risk changes require review, but evidence is the PR label, reviewer approval, CODEOWNERS enforcement, CI scan logs, and merge record showing the control operated. In this capstone, PROVE exists because leadership cannot make a defensible scale decision from policy language alone.

### How would you explain prompt injection to a CISO?

Prompt injection is when untrusted text manipulates the AI system into ignoring its intended rules. In a RAG system, the risky version is indirect prompt injection: a malicious instruction hidden inside a document gets retrieved and treated like an instruction instead of data. The business risk is that the assistant may reveal sensitive information, suppress a finding, or produce an answer the organization cannot trust.

### How would you handle a team that wants to bypass CI for speed?

I would acknowledge the delivery pressure but separate speed from control bypass. For normal low-risk changes, optimize the pipeline so CI is fast. For auth, IAM, crypto, logging, dependency, infrastructure, or AI-generated changes, CI and review gates are not optional because they are the evidence trail. If the team needs emergency change handling, define an emergency path with approval, logging, time-boxed exception, and post-change validation.

### What would make you recommend pausing AI adoption?

I would recommend pausing expansion if the organization cannot define the data boundary, cannot name owners, cannot prove logging, cannot enforce human review for high-risk outputs, or if BREAK testing shows sensitive data exposure, unauthorized retrieval, prompt injection success, or unreviewed AI-generated security-sensitive code reaching merge. Pause does not mean abandon AI. It means remediate the control gap before scaling risk.

### What would make you recommend conditional scale?

I would recommend conditional scale when the business use case is valid and the highest-risk controls are either working or have concrete remediation gates. That means owners are assigned, data classes are defined, approved AI paths are documented, logging and evidence capture work, human review is enforced for high-risk outputs, BREAK findings are remediated or accepted by the right risk owner, and PROVE can support the decision with evidence.

## Strong GuidePoint Answer Shape

> I would start with scope and evidence. First I would identify the use case, data boundary, users, model/tool access, and business impact. Then I would map the architecture and trust boundaries, validate the most important controls through BREAK testing, and package findings into a remediation roadmap. I would avoid saying the client is ready to scale until the evidence supports that decision.

## Capstone Practice

Open:

- `deliverables/01-executive-summary.md`
- `deliverables/03-remediation-roadmap.md`

Task:

Write:

- one CISO sentence
- one engineering sentence
- one remediation priority
- one honest limitation
- one scale/no-scale recommendation

## CISO Sentence Pattern

> The AI workflow can <business-impact-risk> because <condition>, and the current controls do not yet prove <missing assurance>.

Example:

> The AI coding workflow can introduce high-risk changes without reliable traceability because AI-assisted work is not consistently labeled, and the current controls do not yet prove human review occurred before merge.

## Final Mindset

GuidePoint does not need me to pretend I know everything.

GuidePoint needs me to show I can:

- ask better questions
- inspect the evidence
- test the claim
- explain the risk
- recommend the next move
