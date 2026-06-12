# CrewAI Workflow

## Purpose

Use CrewAI where structured role-based review improves repeatability.

The BUILD source of truth for CrewAI is `CBBP-PLAN/BUILD/crewai/`.

This workflow folder should hold future runnable CrewAI implementation notes or exports. The CBBP BUILD folder defines the governance, agent roles, evidence contract, and implementation sequence.

## Proposed Agents

| Agent | Responsibility |
|---|---|
| Evidence Collector | Gather prompts, retrieved chunks, logs, and config evidence |
| Threat Modeler | Identify attack paths and trust boundary issues |
| Framework Mapper | Map findings to OWASP LLM, MITRE ATLAS, AI RMF, and 800-53 |
| Remediation Planner | Write prioritized fixes |
| Report Writer | Produce client-ready findings and executive summary |

## Security Rules

- Agents get scoped tools only.
- Evidence collection stays deterministic where possible.
- Human review is required for high-impact findings.
- Outputs must be schema-checked before downstream use.
