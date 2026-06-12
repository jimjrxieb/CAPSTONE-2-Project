# n8n Workflow

## Purpose

Use n8n for intake, routing, approvals, notifications, and evidence collection around the Eugene assessment.

## Proposed Workflow

```text
AI system intake form
  -> risk tier routing
  -> evidence request checklist
  -> Eugene assessment trigger
  -> human approval for high-risk output
  -> findings package creation
  -> notification / ticket
```

## Controls To Document

- credential isolation
- approval gates
- execution logs
- error handling
- evidence retention
- restricted workflow editing
