# CrewAI Agent Role Map

## Purpose

Define the agents used to coordinate the Capstone 2 assessment workflow.

These agents are operational roles. They do not replace Eugene, Codex, Claude Code, n8n, or the human assessor.

## Agent Summary

| Agent | Main Job | Primary Phase | Human Review Required |
|---|---|---|---|
| Intake Completeness Agent | Check whether COMPLY scope fields are complete | COMPLY | Yes for findings |
| Evidence Request Agent | Convert missing controls into evidence requests | COMPLY / BUILD | Yes |
| Build Readiness Agent | Check whether required BUILD files/APIs/scripts exist | BUILD | Yes |
| Scenario Coordinator Agent | Select and sequence BREAK scenarios | BREAK | Yes |
| Evidence Collector Agent | Gather structured evidence outputs | BREAK / PROVE | Yes |
| Eugene Assessment Agent | Send controlled context to Eugene and capture draft output | BREAK / PROVE | Yes |
| Framework Mapper Agent | Map findings to OWASP LLM, MITRE ATLAS, AI RMF, and 800-53 | PROVE | Yes |
| Report Packager Agent | Draft risk register and report-ready summaries | PROVE | Yes |
| Reviewer Gate Agent | Check whether claims have evidence and required approval | PROVE | Always |

---

## Agent Details

### Intake Completeness Agent

**Allowed inputs:**

- `CBBP-PLAN/COMPLY/meddata-ai-adoption-intake.md`
- `CBBP-PLAN/COMPLY/meddata-ai-inventory.md`
- `CBBP-PLAN/COMPLY/meddata-rag-corpus-intake.md`
- `CBBP-PLAN/COMPLY/meddata-trust-boundaries.md`

**Outputs:**

- missing owner list
- missing data-boundary fields
- missing AI tool approvals
- missing evidence requests

**Not allowed:**

- deciding that COMPLY is complete without human review
- converting assumptions into confirmed facts

### Evidence Request Agent

**Allowed inputs:**

- COMPLY finding triggers
- control gaps
- evidence request sections from lessons and workpapers

**Outputs:**

- evidence request list
- expected evidence owner
- expected source path or API
- PROVE artifact destination

**Not allowed:**

- fabricating evidence
- marking missing evidence as pass

### Build Readiness Agent

**Allowed inputs:**

- `CBBP-PLAN/BUILD/`
- `evidence/`
- `target-client/fake-data/corpus-manifest.md`
- planned API contracts

**Outputs:**

- build readiness checklist
- missing collector/API/script list
- blocker list before BREAK

**Not allowed:**

- running destructive commands
- changing source files without human-approved build workflow

### Scenario Coordinator Agent

**Allowed inputs:**

- `scenarios/`
- COMPLY findings
- RAG/coding-assistant risk register entries

**Outputs:**

- selected scenario list
- test objective
- expected control
- required evidence

**Not allowed:**

- changing test results
- skipping high-risk scenarios because they are inconvenient

### Evidence Collector Agent

**Allowed inputs:**

- evidence API responses
- evidence files
- logs
- test output

**Outputs:**

- normalized evidence records
- evidence index updates
- missing evidence warnings

**Not allowed:**

- editing raw evidence after capture
- treating screenshots or prose as the only evidence when structured logs should exist

### Eugene Assessment Agent

**Allowed inputs:**

- sanitized retrieved context
- scenario metadata
- evidence records
- approved framework mapping hints

**Outputs:**

- draft finding
- draft impact statement
- draft remediation
- draft framework mapping

**Not allowed:**

- final risk acceptance
- production approval
- autonomous remediation
- sending restricted data to external APIs

### Framework Mapper Agent

**Allowed inputs:**

- confirmed finding drafts
- evidence records
- framework templates

**Outputs:**

- `CBBP-PLAN/PROVE/owasp-llm-map.md`
- `CBBP-PLAN/PROVE/mitre-atlas-map.md`
- `CBBP-PLAN/PROVE/nist-ai-rmf-map.md`
- `CBBP-PLAN/PROVE/nist-800-53-map.md`

**Not allowed:**

- inventing framework citations without rationale
- mapping a finding without evidence

### Report Packager Agent

**Allowed inputs:**

- approved findings
- risk register entries
- evidence index
- framework mappings

**Outputs:**

- draft risk register updates
- draft executive summary bullets
- draft remediation roadmap items

**Not allowed:**

- publishing client deliverables without human approval

### Reviewer Gate Agent

**Allowed inputs:**

- all draft outputs
- evidence index
- human review records

**Outputs:**

- pass/fail review gate result
- missing evidence list
- missing approval list

**Not allowed:**

- overriding human review requirement
- approving B/S-rank findings

