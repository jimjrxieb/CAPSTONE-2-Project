# GuidePoint AI Security Engineer Role Map

## Purpose

Use this file to study for the mock interview with Constant.

The goal is not to sound like an AI enthusiast. The goal is to sound like a security engineer who can help a client adopt AI without losing control of data, tools, decisions, and evidence.

## Core Thesis

> AI adoption becomes defensible when the workflow is scoped, built with controls, tested under misuse, and proven with evidence.

CBBP is my working lifecycle, but it is not arbitrary. It is backed by NIST RMF, NIST AI RMF, and NIST 800-53 control thinking:

- NIST RMF gives the governance discipline: categorize, select, implement, assess, authorize, monitor.
- NIST AI RMF gives the AI-specific lens: govern, map, measure, manage.
- NIST 800-53 gives the control language for access control, audit logging, risk assessment, configuration, incident response, and system integrity.
- CBBP turns those frameworks into a practical delivery flow I can explain and execute during an assessment.

Use CBBP as the structure:

| Phase | Interview Meaning | NIST Backing | Capstone Proof |
|---|---|---|---|
| COMPLY | Define scope, owners, data boundaries, tool authority, and evidence requirements | RMF Categorize/Select; AI RMF Govern/Map; 800-53 RA, PM, PL, AC | `CBBP-PLAN/COMPLY/` |
| BUILD | Implement the harness, RAG pipeline, evidence collectors, and workflow guardrails | RMF Implement; AI RMF Manage; 800-53 AC, AU, CM, SI, SC | `CBBP-PLAN/BUILD/` |
| BREAK | Test whether the AI workflow fails under prompt injection, poisoning, access gaps, and coding-assistant bypasses | RMF Assess; AI RMF Measure; 800-53 CA, RA, SI, AU | `CBBP-PLAN/BREAK/`, `scenarios/` |
| PROVE | Package evidence, framework mappings, risk register, and scale/no-scale recommendation | RMF Authorize/Monitor; AI RMF Manage/Govern; 800-53 CA, RA, PM, AU | `CBBP-PLAN/PROVE/`, `deliverables/` |

## One-Sentence Role Translation

GuidePoint wants someone who can assess, secure, and explain AI systems in a way that engineers can implement and leaders can trust.

## My Positioning

> I am building a repeatable AI security assessment lab around Eugene. It uses synthetic client data, a governed RAG pipeline, AI-specific BREAK scenarios, evidence capture, framework mapping, and client-ready reporting. The point is not that I can run a chatbot. The point is that I can make an AI workflow assessable, testable, and defensible.

## Requirement Map

| Job Requirement | What It Means | My Capstone Proof |
|---|---|---|
| AI security architecture and assessment | Review GenAI, RAG, model-serving, and agentic workflows for control gaps | `target-architecture/`, `CBBP-PLAN/COMPLY/meddata-trust-boundaries.md` |
| Threat modeling for AI systems | Identify prompt injection, poisoning, unsafe tool use, data leakage, and human overtrust | `CBBP-PLAN/COMPLY/meddata-threat-model.md` |
| Secure AI integration guidance | Help teams use AI tools through approved paths with data boundaries and review gates | `CBBP-PLAN/BUILD/ai-dev-assist-harness.md` |
| RAG and vector database security | Secure corpus ingestion, retrieval filtering, source attribution, access control, and output filtering | `CBBP-PLAN/COMPLY/meddata-rag-corpus-intake.md`, `CBBP-PLAN/BREAK/meddata-rag-break.md` |
| Agentic coding assistant governance | Govern Codex, Claude Code, Copilot-style tools, PR labels, reviews, dependencies, and CI gates | `CBBP-PLAN/COMPLY/meddata-coding-assistant-intake.md`, `CBBP-PLAN/BREAK/meddata-coding-assistant-break.md` |
| Evidence and GRC engineering | Build APIs/scripts/logs that prove controls operated | `CBBP-PLAN/BUILD/crewai/evidence-contract.md`, `evidence/` |
| Framework mapping | Translate findings into OWASP LLM, MITRE ATLAS, NIST AI RMF, and NIST 800-53 | `CBBP-PLAN/PROVE/` |
| Executive advisory | Convert technical findings into scale, conditional scale, pause, or remediate-first recommendations | `deliverables/`, `lessons/10-executive-advisory.md` |

## Clean Tool Framing

| Tool / System | What It Is | What To Say |
|---|---|---|
| Eugene | Capstone 2 assessment assistant | Eugene drafts findings and mappings from controlled context. Human review owns final judgment. |
| RAG pipeline | Retrieval and evidence context path | The RAG pipeline is the target control surface: corpus, chunks, metadata, retrieval filters, logs, and output handling. |
| Codex / Claude Code | Build assistants | They help build the lab under governed AI dev-assist rules. They are not risk owners. |
| CrewAI | Operational orchestration layer | CrewAI can coordinate assessment tasks and evidence packaging after deterministic evidence paths exist. |
| n8n | Approval/routing workflow | n8n is useful for HITL approvals, notifications, and evidence movement. |
| Haiku / external API path | Optional external model path | Only approved or sanitized context should leave the local environment; Restricted data requires explicit authorization. |

Do not blur these roles. Constant may pressure test this.

## Strongest Fit Answer

Question:

> Why are you a fit for this AI Security Engineer role?

Answer:

> This role maps directly to the work I am building. My focus is governed AI adoption and AI security assessment. I use CBBP as my practical delivery lifecycle, but it is backed by NIST RMF, NIST AI RMF, and 800-53 control language. COMPLY defines scope, data boundaries, owners, human authority, and evidence requirements; BUILD implements the harness, controls, evidence paths, and workflow; BREAK tests prompt injection, RAG poisoning, unauthorized retrieval, missing logging, coding-assistant bypasses, unsafe dependencies, and auth-sensitive AI-generated changes; PROVE packages the evidence into findings, framework mappings, a risk register, and a scale/no-scale recommendation. The value I bring is not just using AI tools. It is helping clients use AI tools safely and prove the controls work.

## Constant Pressure Points

### If He Asks: "Why Eugene?"

Say:

> I am not positioning Eugene as smarter than a frontier model. Eugene is the governed local assessment path for the capstone. Its value is containment, repeatability, and traceability. It drafts findings and mappings from controlled context, but human review owns the final assessment.

Avoid:

- "Eugene knows NIST."
- "Eugene replaces a consultant."
- "The model decides the risk."

### If He Asks: "Why CrewAI?"

Say:

> CrewAI is not the core security control and not the chatbot. I would use it as an orchestration layer around the assessment workflow: intake completeness, evidence requests, BREAK scenario coordination, framework mapping, and PROVE packaging. It helps repeatability, but it still consumes evidence and routes high-risk outputs to human review.

Avoid:

- starting the build with CrewAI before evidence APIs exist
- making CrewAI the source of truth
- letting agents mark findings final

### If He Asks: "How Do You Secure Codex Or Claude Code?"

Say:

> I treat AI-generated code as a draft. The controls are repo scope, approved context, no real secrets or client data, human review for security-sensitive files, AI-assisted PR disclosure, CODEOWNERS, SAST/SCA/secrets scans, dependency review, and evidence that the review happened before merge.

Capstone proof:

- `CBBP-PLAN/COMPLY/meddata-coding-assistant-intake.md`
- `CBBP-PLAN/BREAK/meddata-coding-assistant-break.md`
- `scenarios/ai-assisted-pr-label-bypass.md`
- `scenarios/ai-generated-auth-change.md`
- `scenarios/ai-unsafe-dependency-suggestion.md`

### If He Asks: "How Would You Assess A RAG System You Did Not Build?"

Say:

> I would start with scope and evidence. First I would identify the corpus, data classes, users, owners, model path, vector DB, retrieval filters, logging, and human review requirements. Then I would test the highest-risk claims: whether unauthorized users can retrieve restricted documents, whether poisoned content changes behavior, whether secrets can enter the corpus, whether outputs are filtered, and whether logs can reconstruct what happened.

Capstone proof:

- `CBBP-PLAN/COMPLY/meddata-rag-corpus-intake.md`
- `CBBP-PLAN/COMPLY/meddata-trust-boundaries.md`
- `CBBP-PLAN/BREAK/meddata-rag-break.md`

### If He Asks: "What Makes This GRC Engineering?"

Say:

> The evidence request becomes a build requirement. In COMPLY I define what proof should exist. In BUILD I create evidence collectors, logs, schemas, and APIs. In BREAK I generate test evidence. In PROVE I map that evidence to findings and controls. That is the engineering part: the system can produce proof, not just policy language.

Capstone proof:

- `CBBP-PLAN/BUILD/crewai/evidence-contract.md`
- `CBBP-PLAN/PROVE/risk-register.md`
- `CBBP-PLAN/PROVE/nist-ai-rmf-map.md`

## Failure Response Rubric

Use this anytime Constant asks "what if it breaks?"

```text
1. Isolate   - Which layer failed: input, retrieval, model, tool, output, approval, or logging?
2. Diagnose  - What does the evidence say? If no log exists, that is the first finding.
3. Contain   - Stop bad output or unsafe action from moving downstream.
4. Remediate - Fix the control at the failed layer.
5. Verify    - Re-run the scenario and package the proof.
```

Interview line:

> I do not trust a fix I have not re-tested. A control is not proven because it exists on a diagram; it is proven when the evidence shows it operated.

## Common Failure Scenarios

### Confident But Wrong AI Answer

Root issue:

- grounding failure
- missing source attribution
- weak output validation

Answer:

> I would check whether retrieval returned the right source documents and whether the model was allowed to answer without evidence. The fix is grounding: answer only from provided context, cite the source, and return insufficient evidence when the context does not support the answer.

### Prompt Injection From A Retrieved Document

Root issue:

- untrusted corpus content treated like instruction

Answer:

> Retrieved content is data, not authority. I would separate system instructions from retrieved text, sanitize or label untrusted content, run the poisoned-document scenario, and verify that the model ignores instructions embedded in the corpus.

### Unauthorized RAG Retrieval

Root issue:

- vector DB or retrieval layer lacks role-aware filtering

Answer:

> The control belongs at retrieval, not just the UI. I would require user role to document tier mapping on every query, log returned chunk IDs, and test whether a lower-privileged user can retrieve legal, security, or Restricted-tier content.

### AI-Generated Auth Change Without Security Review

Root issue:

- coding assistant governance failure

Answer:

> AI-generated security-sensitive code should trigger elevated review. I would require PR disclosure, CODEOWNERS review for auth/IAM/crypto/logging paths, CI scans, and evidence that a human approved the change before merge.

### Missing Audit Logs

Root issue:

- PROVE failure

Answer:

> If the workflow cannot reconstruct who asked what, what was retrieved, what the model returned, and who approved it, the organization cannot defend the control. The fix is structured audit logging and retention before pilot expansion.

## Terms To Use Cleanly

| Term | Plain Meaning |
|---|---|
| Harness | The governed workflow around the model: data, tools, prompts, approvals, tests, and evidence |
| Context boundary | What the model can see and what part of that context has authority |
| Tool surface | The actions or APIs the model/agent can cause |
| HITL | Human review or approval where risk, authority, or irreversibility is high |
| Grounding | Requiring model output to be supported by retrieved/provided evidence |
| Indirect prompt injection | Malicious instructions hidden in retrieved content or documents |
| RAG poisoning | Bad or adversarial documents entering the corpus and steering responses |
| Excessive agency | An agent has broader tools or autonomy than the task requires |
| Fail closed | Stop safely when evidence, validation, or approval is missing |
| PROVE | The evidence package that supports the final decision |

## Cloud AI Services Answer

If asked about Bedrock, SageMaker, Azure AI Foundry, Azure OpenAI, or Vertex:

> My current capstone is vendor-agnostic, but the security pattern transfers. I would assess identity, secrets, data flow, model access, logging, monitoring, prompt/output handling, tool permissions, and inherited controls from the provider. The key question is not only which model is used; it is what data crosses the boundary, who can invoke it, what gets logged, and what evidence proves the controls worked.

Follow-up improvements to build later:

- vendor AI service intake questions
- inherited-control matrix
- Bedrock or Azure OpenAI threat model
- external API data-boundary test

## Vocabulary To Keep Ready

- trusted security advisor
- AI security architecture
- secure AI integration
- RAG architecture
- vector database security
- corpus governance
- evidence-backed assessment
- threat modeling
- data security and privacy controls
- agentic workflow
- context engineering
- tool authority
- least privilege
- human review gate
- control validation
- remediation roadmap
- scale/no-scale recommendation

## What Not To Overclaim

Do not say:

- Eugene is production-ready.
- Eugene replaces a human assessor.
- CrewAI proves controls by itself.
- The system is ready to scale before BREAK evidence exists.
- Haiku or any external API can receive sensitive data by default.
- Shadow AI is confirmed unless the evidence proves it.

Say instead:

- "This is preliminary until BUILD/BREAK evidence confirms it."
- "That is an assumption pending evidence."
- "The model drafts; the human decides."
- "The control is not proven until the evidence shows it operated."

## Daily Drill

Finish these out loud:

1. GuidePoint is not hiring me to merely use Codex or Claude Code. They are hiring me to...
2. Eugene is useful in this capstone because...
3. A RAG system fails when...
4. CrewAI belongs in this build as...
5. PROVE matters because...
6. I would recommend pausing AI adoption when...
7. I would recommend conditional scale when...

## Three Lines To Memorize

> The harness is the governance layer around the model.

> AI output is a draft until evidence and human review support it.

> A control is not proven because it exists; it is proven when the workflow produces evidence under test.
