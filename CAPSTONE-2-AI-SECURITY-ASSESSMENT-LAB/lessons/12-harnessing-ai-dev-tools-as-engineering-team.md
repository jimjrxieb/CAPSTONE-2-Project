# Lesson 12 - Harnessing AI Dev Tools As An Engineering Team

**Status: COMPLETE — 2026-06-08**
**Deliverable:** `CBBP-PLAN/COMPLY/meddata-ai-engineering-crew.md`
- Four boundaries defined for MedData Nexus engineering (goal, data, tool, authority)
- Crew table filled: 6 roles (Requirements → Build → Security Review → Test → BREAK → PROVE), each with AI tool assignment, allowed inputs, allowed tools, required human review, and evidence obligations
- Escalation map, shadow AI detection, guardrail status table, evidence artifact list
- CISO sentence specific to MDN-AI-002 shadow AI risk

## What To Master

Harnessing AI development tools means organizing AI assistants, agents, workflows, tools, reviews, and evidence so they behave like a controlled engineering function.

The goal is not:

> I can make Claude Code or Codex write code.

The goal is:

> I can design a governed AI engineering system where Codex, Claude Code, CrewAI-style agents, CI/CD, security tools, and humans work together with clear roles, boundaries, review gates, and evidence.

## Simple Definition

> Harnessing AI dev tools means turning individual AI assistants into a structured, role-based, evidence-producing engineering workflow.

## Why This Matters To GuidePoint

GuidePoint-style AI security work is not only about finding prompt injection.

It is also about helping clients answer:

- How do we safely use AI coding assistants?
- How do we assign AI agents to engineering tasks without giving them too much authority?
- How do we keep humans in control of architecture, risk, and production decisions?
- How do we prove AI-assisted work was reviewed?
- How do we balance autonomy and security?
- How do we secure MCP, tool calling, CrewAI-style workflows, Codex, Claude Code, Cursor, and similar systems?

That is the theory behind "harnessing AI."

## Core Concept

AI dev tools become useful at scale when they are treated like workers inside a workflow, not magic.

Every worker needs:

- a role
- a scope
- allowed tools
- prohibited actions
- input rules
- output expectations
- review gates
- logging
- escalation path
- quality checks

AI is no different.

## The AI Engineering Team Model

| Role | Human Equivalent | AI Tool Role | Human Authority |
|---|---|---|---|
| Product/Goal Owner | Defines the business outcome | Helps clarify requirements | Human owns final goal |
| Architect | Designs system boundaries | Drafts architecture options | Human approves architecture |
| Implementation Engineer | Writes code/configs | Codex/Claude Code generate patches | Human reviews and merges |
| Security Engineer | Reviews risk | AI suggests threat paths and controls | Human accepts/rejects risk |
| QA/Test Engineer | Creates test cases | AI drafts tests and edge cases | Human validates coverage |
| Red Team/BREAK Engineer | Attacks assumptions | AI generates misuse cases | Human approves risky tests |
| Compliance/PROVE Analyst | Packages evidence | AI summarizes logs/findings | Human signs off on claims |

Key phrase:

> AI can take roles in the workflow, but humans retain authority over goals, risk, exceptions, and production impact.

## Terms To Know

**Harness**
: The control system around AI tools: roles, prompts, permissions, data boundaries, review gates, tests, logs, and evidence.

**Agent**
: An AI system assigned a goal and often given tools or memory to complete tasks semi-autonomously.

**Agentic Workflow**
: A workflow where one or more AI agents plan, use tools, generate outputs, hand off work, or iterate toward a goal.

**CrewAI**
: A framework pattern for assigning specialized agents to roles, tasks, and workflows. The key idea is role-based agent collaboration.

**Coding Assistant**
: A tool like Codex, Claude Code, Cursor, Copilot, or Open Code that helps write, modify, explain, test, or review code.

**Tool Calling**
: When an AI system can invoke external tools such as file readers, shell commands, APIs, databases, browsers, scanners, or ticket systems.

**MCP**
: Model Context Protocol. A client/server pattern for giving AI tools structured access to external context and capabilities.

**Context Window**
: The information available to the model at the time it generates output.

**Context Engineering**
: Designing what information enters the model context, in what order, with what authority, and with what protections.

**Authority Boundary**
: The line between what AI may suggest and what it may actually do.

**Human-In-The-Loop**
: A required human review or approval point before an AI output can be acted on.

**Human-On-The-Loop**
: A human supervises an automated process and can intervene, but does not approve every step.

**Autonomy Budget**
: The allowed level of independence given to an AI agent for a task.

**Tool Surface**
: The set of actions available to the AI, such as reading files, writing files, running commands, opening PRs, or calling APIs.

**Prompt Injection**
: Untrusted text tries to override the intended instructions.

**Indirect Prompt Injection**
: Malicious instructions arrive through files, docs, tickets, webpages, logs, emails, or retrieved content.

**Evidence-Producing Workflow**
: A workflow designed so logs, reviews, test outputs, and decisions are captured as proof.

## Theory: The Four Boundaries

To harness AI dev tools, always define four boundaries.

### 1. Goal Boundary

What is the AI trying to accomplish?

Good:

> Draft a unit test for this function.

Risky:

> Make the app secure.

The bigger the goal, the more human review and decomposition are needed.

### 2. Data Boundary

What can the AI see?

Questions:

- Can it read source code?
- Can it read secrets?
- Can it read customer data?
- Can it read internal tickets?
- Can it read production logs?
- Can it send data to a third-party model?

### 3. Tool Boundary

What can the AI do?

Questions:

- Can it write files?
- Can it run commands?
- Can it install dependencies?
- Can it call external APIs?
- Can it modify infrastructure?
- Can it open or merge PRs?

### 4. Authority Boundary

What can AI decide?

Human-only decisions:

- risk acceptance
- disabling security controls
- production deployment
- auth/authorization design approval
- compliance claims
- customer-impacting decisions
- exception approval

## The Harness Structure

Use this structure when designing an AI engineering workflow.

```text
Human goal
  -> scoped task
  -> approved context
  -> AI role assignment
  -> tool permissions
  -> generated output
  -> automated checks
  -> human review
  -> evidence capture
  -> decision
```

## CrewAI-Style Mental Model

CrewAI is useful because it forces you to think in roles.

Example AI engineering crew:

| Agent | Purpose | Inputs | Output | Must Not Do |
|---|---|---|---|---|
| Requirements Agent | Clarify task and acceptance criteria | human goal, ticket | scoped requirements | invent business goals |
| Architect Agent | Propose design options | requirements, architecture docs | design note | approve architecture |
| Build Agent | Draft code/config | approved task, repo context | patch | merge or deploy |
| Security Agent | Review risk | diff, policies, threat model | risk notes | accept risk |
| Test Agent | Create tests | code, requirements | test cases | claim complete coverage without evidence |
| BREAK Agent | Generate misuse cases | system design, controls | attack plan | run destructive tests without approval |
| PROVE Agent | Package evidence | logs, reviews, scans | report | claim compliance without human signoff |

The important part is not the framework name. The important part is the control design:

> role, scope, tool access, output, review, evidence.

## Codex And Claude Code Harness Model

For tools like Codex and Claude Code, the harness should define:

- which repos are approved
- which data is prohibited
- what commands require approval
- what files are security-sensitive
- what changes require extra review
- when an `ai-assisted` label is required
- what CI gates must run
- how dependency additions are reviewed
- how source comments and docs are treated as untrusted context
- how evidence is captured in PRs, logs, and reports

## Questions I Should Ask A Client

- Which AI dev tools are engineers using today?
- Are those tools approved or shadow AI?
- Which repos and systems can the tools access?
- What data is prohibited from AI context?
- Can the AI run commands or modify files?
- Can the AI install dependencies?
- Can the AI open, approve, or merge PRs?
- What changes require security review?
- Are AI-assisted PRs labeled?
- What CI checks apply to AI-generated code?
- How do you detect malicious instructions in source comments, docs, tickets, or logs?
- What evidence proves human review happened?
- What happens when speed pressure conflicts with the CI gate?

## What I Need To Know

Harnessing AI is an architecture and governance problem.

It combines:

- AI adoption
- AppSec
- secure SDLC
- CI/CD
- identity and access management
- data governance
- prompt/context engineering
- agentic workflow design
- evidence and auditability
- human factors

The job is not to make AI autonomous.

The job is to choose where autonomy is useful, where it is dangerous, and where human authority must remain.

## Capstone Practice

Open:

- `deliverables/04-ai-adoption-operating-model.md`
- `scenarios/ai-assisted-pr-label-bypass.md`
- `scenarios/ai-generated-auth-change.md`
- `scenarios/ai-unsafe-dependency-suggestion.md`
- `scenarios/ai-runtime-drift.md`

Task:

Design an AI engineering crew for MedData Nexus.

Fill this table:

| Role | AI Tool/Agent | Allowed Inputs | Allowed Tools | Human Review Required | Evidence |
|---|---|---|---|---|---|
| Requirements | | | | | |
| Build | | | | | |
| Security Review | | | | | |
| Test | | | | | |
| BREAK | | | | | |
| PROVE | | | | | |

## Finding Trigger

Create a finding if:

- AI assistants are used without approved scope
- AI can touch sensitive repos without extra review
- AI-generated code can merge without disclosure
- AI can add dependencies without review
- AI can run commands without approval boundaries
- source comments/docs can steer the tool as instructions
- no evidence proves human review occurred

## CISO Sentence

> The organization is using AI development tools like extra engineers, but it has not yet defined the roles, permissions, review gates, and evidence needed to control their work.

## Interview Answer

If asked:

> What does harnessing AI mean to you?

Answer:

> Harnessing AI means designing the operating system around the model. For AI development tools, that means defining agent roles, approved context, tool permissions, human review gates, CI/security checks, and evidence capture. Codex or Claude Code can help generate code, tests, and analysis, but the harness decides what they can see, what they can do, what requires approval, and what proof exists before the work is trusted.

## Daily Drill

Finish this sentence:

> Harnessing AI dev tools as an engineering team means...

