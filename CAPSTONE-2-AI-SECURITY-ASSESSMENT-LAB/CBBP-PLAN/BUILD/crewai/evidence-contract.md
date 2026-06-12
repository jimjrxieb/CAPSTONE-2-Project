# CrewAI Evidence Contract

## Purpose

Define the structured evidence CrewAI expects from BUILD scripts and APIs so PROVE can package defensible results.

CrewAI should consume evidence. It should not be the only system creating evidence.

## Evidence Record Shape

Every evidence record should use this shape:

```json
{
  "evidence_id": "EV-CAP2-0001",
  "timestamp": "2026-06-08T00:00:00Z",
  "phase": "BREAK",
  "scenario_id": "rag-direct-prompt-injection",
  "system_id": "MDN-AI-001",
  "control_or_claim": "Prompt injection resistance",
  "source_type": "api_response",
  "source_path": "evidence/break/rag-direct-prompt-injection.json",
  "collector": "baseline_retrieval_test.py",
  "summary": "Prompt injection test output captured with retrieved source IDs.",
  "result": "fail",
  "human_review_required": true,
  "human_review_status": "pending"
}
```

## Evidence Sources CrewAI Should Expect

| Evidence Type | BUILD Source | PROVE Use |
|---|---|---|
| Corpus manifest | `target-client/fake-data/corpus-manifest.md` or evidence API | prove corpus boundary |
| Ingestion logs | ingestion script output | prove what entered the vector DB |
| Retrieval logs | retrieval API/test output | prove what chunks were returned |
| Prompt/output logs | Eugene API/chatbox logging | prove what model received and returned |
| Output filter logs | output filter API/script | prove sensitive output handling |
| HITL review records | n8n/manual approval record | prove human review |
| BREAK scenario results | scenario runner output | prove controls were tested |
| Framework mappings | `CBBP-PLAN/PROVE/*.md` | prove findings map to standards |
| Scan results | SAST/SCA/secrets/IaC tools | prove coding assistant guardrails |

## Planned Evidence Endpoints

These endpoints are build targets, not current claims.

```text
GET /api/evidence/corpus-manifest
GET /api/evidence/ingestion-logs
GET /api/evidence/retrieval-test-results
GET /api/evidence/audit-logs
GET /api/evidence/output-filter-results
GET /api/evidence/hitl-review-records
GET /api/evidence/break-scenario-results
GET /api/evidence/dependency-scan-results
GET /api/evidence/secrets-scan-results
```

## Evidence Quality Rules

- No final finding without evidence ID.
- No B/S-rank finding without human review status.
- No framework mapping without finding ID.
- No PROVE claim based only on memory or chat history.
- Raw evidence should be append-only once captured.
- If evidence is missing, CrewAI must say `evidence_missing`, not infer a pass.

## Human Review Status Values

Use one:

- `not_required`
- `pending`
- `approved`
- `rejected`
- `needs_more_evidence`

