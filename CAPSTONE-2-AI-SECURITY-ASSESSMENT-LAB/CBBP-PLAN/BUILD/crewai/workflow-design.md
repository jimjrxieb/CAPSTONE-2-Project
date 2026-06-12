# CrewAI Workflow Design

## Purpose

Define the end-to-end assessment workflow CrewAI should coordinate once Eugene, evidence collectors, and BREAK scenarios are available.

## Workflow 1 — COMPLY Completeness Check

```text
Input:
  CBBP-PLAN/COMPLY/*.md

Agents:
  Intake Completeness Agent
  Evidence Request Agent
  Reviewer Gate Agent

Output:
  COMPLY gap list
  evidence request list
  human review status
```

### Required Checks

- system name exists
- business, technical, risk, and data owners exist or gaps are documented
- users and roles are listed
- AI tools are listed
- prohibited data is listed
- highest-risk workflow is identified
- top evidence requests are listed
- assumptions pending evidence are separated from confirmed facts

## Workflow 2 — BUILD Readiness Check

```text
Input:
  CBBP-PLAN/BUILD/
  evidence/
  target-client/fake-data/

Agents:
  Build Readiness Agent
  Evidence Request Agent
  Reviewer Gate Agent

Output:
  BUILD readiness checklist
  missing API/script/collector list
  blocked BREAK scenarios
```

### Required Checks

- corpus manifest exists
- ingestion path is documented
- retrieval test path is documented
- evidence directory exists
- planned evidence APIs are defined
- Eugene API/chatbox status is known
- CrewAI can call only approved local tools or endpoints

## Workflow 3 — BREAK Scenario Coordination

```text
Input:
  scenarios/*.md
  evidence collectors
  Eugene assessment endpoint

Agents:
  Scenario Coordinator Agent
  Evidence Collector Agent
  Eugene Assessment Agent
  Reviewer Gate Agent

Output:
  scenario evidence record
  draft finding
  missing-control statement
  human review status
```

### Required Checks

- test objective is known
- expected control is known
- test prompt/input is captured
- retrieved chunks are captured
- model output is captured
- guardrail result is captured
- logs show who/what/when
- finding is marked draft until reviewed

## Workflow 4 — PROVE Packaging

```text
Input:
  reviewed findings
  evidence records
  framework templates

Agents:
  Framework Mapper Agent
  Report Packager Agent
  Reviewer Gate Agent

Output:
  CBBP-PLAN/PROVE/risk-register.md
  CBBP-PLAN/PROVE/owasp-llm-map.md
  CBBP-PLAN/PROVE/mitre-atlas-map.md
  CBBP-PLAN/PROVE/nist-ai-rmf-map.md
  CBBP-PLAN/PROVE/nist-800-53-map.md
  deliverables/*
```

### Required Checks

- each finding has evidence
- each evidence item has a source path or API response ID
- each framework mapping has a rationale
- each B/S-rank finding has human review
- final recommendation is scale, conditional scale, pilot only, pause, or remediate first

## Workflow Rule

CrewAI may prepare the work queue and draft outputs. The human assessor owns final acceptance.

