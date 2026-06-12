# Lesson 01 - GuidePoint Consultant Mindset

**Status: COMPLETE — 2026-06-08**

## What To Master

A consultant is not hired to be impressed by technology. A consultant is hired to reduce uncertainty.

The GuidePoint mindset:

- understand the client's goal
- identify the risk surface
- separate claims from evidence
- test the controls
- explain the business impact
- recommend the next practical move

## The Core Shift

Do not think:

> Can I use AI well?

Think:

> Can I help a client use AI safely, prove what is working, and make better decisions?

## Questions I Should Ask

- What business outcome is driving this AI project?
- Who owns the system?
- Who owns the risk?
- What data does AI touch?
- What can AI do without a human?
- What would be unacceptable if AI got it wrong?
- What control is supposed to prevent that?
- What evidence proves the control works?
- What would I tell a CISO in one sentence?

## What I Need To Know

- AI security is advisory plus engineering evidence.
- A framework citation is not proof.
- Runtime behavior matters more than written claims.
- Human approval is a control only if it is required, recorded, and reviewed.
- AI adoption risk lives in people, process, tools, data, models, vendors, and workflows.

## Capstone Practice

Open:

- `CBBP-PLAN/ai-adoption-at-scale-cbbp.md`
- `readiness-rubrics/guidepoint-readiness-rubric.md`
- `readiness-rubrics/ai-adoption-readiness-rubric.md`

Task:

Write a two-minute explanation of Capstone 2 as if a GuidePoint interviewer asked:

> What did you build, and why does it matter to a client?

## Strong Answer Shape

> I built an AI security assessment lab that treats AI adoption like a client engagement. The RAG assistant is the technical target, but the real deliverable is the assessment workflow: intake, architecture review, trust-boundary mapping, adversarial testing, framework mapping, findings, remediation, and executive evidence. The point is to show I can help a client move from AI experimentation to governed AI adoption.

## Daily Drill

Finish this sentence:

> A GuidePoint client does not need me to hype AI. They need me to...
>
> Properly govern their AI tools and applications. AI does accelerate delivery, but it also expands the attack surface through prompts, retrieved data, coding assistants, plugins, and user overtrust. My focus is on hardening the path — defining approved AI workflows, setting data boundaries, and limiting model authority so engineers can move fast without exposing sensitive data, IP, or regulated information. Guardrails and access controls on the corpus and vector store help contain the risk. For high-volume, low-stakes tasks, local models can handle summarization and classification. For high-risk reasoning, code changes, and compliance decisions, a human stays in the loop. The goal is to test whether those controls actually work and package the evidence so leadership can decide with confidence.

## Grade

**Score: 3.2 / 5**

## What Is Strong

- You correctly led with governance instead of hype.
- You named the real business tension: AI increases speed but expands the attack surface.
- You identified practical control themes: guardrails, data limits, and reducing unnecessary model authority.
- You are thinking about the human role: engineers should own judgment, not the model.

## What Is Missing

- **Client outcome:** Say what the client is trying to achieve, not only what tools engineers want to use.
- **Evidence:** GuidePoint-style consulting needs proof. Add language like "test the controls" and "package evidence."
- **Risk decision:** The client needs help deciding whether to pilot, scale, pause, or remediate.
- **Cleaner tool framing:** Avoid naming a specific subscription tier in the core answer. Say "approved enterprise AI coding assistants" unless the client specifically asks about Codex or Claude Code.
- **Business language:** "NDA" is useful, but broaden it to sensitive data, IP, regulated data, customer data, and contractual obligations.
- **Clarity:** The local model point is interesting, but it needs cleaner wording. The idea is: local models can support summarization/classification in controlled workflows, while high-risk reasoning and code changes still require human review and stronger validation.

## Stronger Version

> A GuidePoint client does not need me to hype AI. They need me to help them adopt AI without losing control of their data, systems, people, and evidence. AI can make engineers and analysts faster, but it also expands the attack surface through prompts, retrieved data, coding assistants, vendors, plugins, and human overtrust. My role is to help define the approved workflow, set data boundaries, require human review for high-risk actions, test whether the guardrails actually work, and package the evidence so leadership can decide whether to pilot, scale, remediate, or pause.

## Retry Space

Rewrite your answer in 4-6 sentences.

Rules:

- Start with what the client needs.
- Mention speed and risk.
- Mention data/tool boundaries.
- Mention human review.
- Mention evidence.
- End with the decision you help the client make.

> A GuidePoint client does not need me to hype AI. They need me to apply proper guardrails and harnesses so their engineers can build faster without losing control of sensitive data or approval workflows. AI tools create delivery pressure and expand the attack surface at the same time — through prompts, retrieved data, coding assistants, plugins, and vendor integrations. Just as we enforce policy as code for infrastructure, we need policy as prompts and policy as workflow for AI. My job is to define what the model is allowed to touch, require human review for high-risk outputs, and test whether those guardrails actually hold.

## Retry Grade

**Score: 2.7 / 5**

## What Improved

- You started with what the client needs.
- You mentioned speed and risk.
- You introduced a useful idea: policy as prompts.

## What Still Needs Work

- **Data/tool boundaries:** Say what data, tools, prompts, plugins, repositories, or systems AI is allowed to touch.
- **Human review:** State clearly that high-risk outputs and code changes require human approval.
- **Evidence:** Mention testing controls and packaging proof for leadership.
- **Decision:** End with the business decision you help the client make: pilot, scale, remediate, or pause.
- **Clarity:** Clean up wording like "aswell" and "faster and best applications."

## Stronger Retry Version

> A GuidePoint client does not need me to hype AI. They need me to help their engineers use AI faster without losing control of sensitive data, tools, or approval workflows. AI can improve delivery speed, but it also creates a new attack surface through prompts, retrieved data, coding assistants, plugins, and user overtrust. My role is to define approved AI workflows, apply guardrails like policy-as-code and policy-as-prompts, require human review for high-risk outputs, and test whether those controls actually work. I package that evidence so leadership can decide whether to pilot, scale, remediate, or pause the AI rollout.

## Retry Space 2

Rewrite your answer again in 4-6 sentences.

Rules:

- Start with what the client needs.
- Mention speed and risk.
- Mention data/tool boundaries.
- Mention human review.
- Mention evidence.
- End with the decision you help the client make.

> A GuidePoint client does not need me to hype AI. They need me to help them adopt AI without losing control of their data, tools, or decision-making. AI can make engineers and analysts faster, but it also expands the attack surface through prompts, retrieved data, coding assistants, plugins, and vendor integrations. My role is to define what AI is allowed to touch — which data tiers, which tools, which workflows — and enforce those boundaries so sensitive, regulated, and contractual data stays inside approved paths. High-risk outputs and code changes require human review; I make that review mandatory and recorded, not optional. Then I test whether those guardrails actually hold, package the evidence, and give leadership what they need to decide: pilot, scale conditionally, remediate first, or pause.
