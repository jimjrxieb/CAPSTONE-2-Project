# CrewAI Build Plan

## Purpose

Use CrewAI as the operational orchestration layer around the Eugene assessment workflow.

CrewAI is not the RAG model, not the chatbot, and not the final decision authority. It coordinates repeatable assessment tasks so COMPLY questions, BUILD evidence collectors, BREAK scenarios, and PROVE packages connect cleanly.

## Role In Capstone 2

```text
Codex / Claude Code
  -> help build the lab under AI dev-assist governance

RAG pipeline
  -> retrieves scoped MedData Nexus evidence

Eugene
  -> drafts assessment findings and framework mappings from controlled context

CrewAI
  -> coordinates assessment roles, task order, evidence checks, and handoffs

n8n
  -> routes approvals, notifications, and human review workflow

PROVE
  -> packages final evidence, mappings, risk register, and recommendations
```

## Build Principle

CrewAI agents may coordinate work, but they do not create authority.

Every high-risk output still requires human review. Every claim must point to evidence. Every model-generated recommendation remains advisory until approved by the human assessor.

## Where This Fits In CBBP

| CBBP Phase | CrewAI Responsibility |
|---|---|
| COMPLY | Check whether intake, ownership, data boundary, and evidence-request fields are complete |
| BUILD | Verify required collectors, APIs, logs, and guardrail files exist |
| BREAK | Coordinate scenario execution and collect failure evidence |
| PROVE | Assemble evidence-to-control mappings, risk register entries, and report-ready summaries |

## Files In This Build Package

| File | Purpose |
|---|---|
| `agent-role-map.md` | Defines each CrewAI agent, allowed inputs, outputs, and authority limits |
| `workflow-design.md` | Defines the assessment workflow CrewAI should coordinate |
| `evidence-contract.md` | Defines the structured evidence CrewAI expects from BUILD APIs/scripts |
| `implementation-roadmap.md` | Defines when to implement CrewAI and what must exist first |
| `security-boundaries.md` | Defines prompt, data, tool, and human-review boundaries for CrewAI |

## Definition Of Done

CrewAI is BUILD-ready when:

- each agent has a narrow role and scoped inputs
- tasks produce structured outputs, not free-form untraceable claims
- every finding draft includes evidence references
- B/S-rank outputs route to human review
- PROVE artifacts can be populated from evidence records
- CrewAI can be disabled without breaking the core RAG/Eugene assessment path

