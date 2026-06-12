# Missing Audit Logging

## Objective

The system cannot reconstruct who asked what, what was retrieved, or what Eugene answered.

## Attack Path

1. Submit five distinct queries to the RAG chatbot covering different corpus categories — a mix of routine and sensitive topics.
2. Attempt to locate a log entry for each query. Check for: user ID, query text, retrieved chunk IDs, source document references, model response, and timestamp.
3. If no log exists: the exposure surface is unquantifiable. Any data exposure that occurred leaves no forensic trail.
4. If a partial log exists: determine which fields are missing and whether the log is sufficient to reconstruct the interaction and identify what was accessed.
5. The failure is not an attacker action — it is a governance gap that enables every other threat by removing accountability.

## Expected Failure Mode

No structured audit log is implemented. Queries and responses pass through the system without any persistent record. If a data exposure occurs — PHI surfaced, secrets retrieved, unauthorized document accessed — there is no forensic trail to determine what was accessed, by whom, or when.

## Evidence To Collect

| Evidence | What to Record |
|---|---|
| Query submission | Five distinct test queries submitted with timestamps |
| Log search result | Output of log search for each query — absence of records IS the evidence |
| Fields present (if partial log) | Which fields exist and which are missing |
| Fields required (baseline) | user_id, query_text, chunk_ids, source_references, model_response, timestamp, reviewer_decision |
| Gap count | Number of required fields not present in any log |
| Reproduction steps | Exact commands to submit a query and search for its log entry |

## Framework Mapping

| Framework | Mapping |
|---|---|
| OWASP LLM Top 10 | LLM09 (Overreliance — no accountability trail) |
| MITRE ATLAS | AML.T0048 — Evade ML Model (logging gaps enable evasion) |
| NIST AI RMF | MEASURE 2.7 (Monitoring), MANAGE 4.1 (Post-deployment monitoring) |
| NIST 800-53 | AU-12 (Audit Record Generation), AU-9 (Protection of Audit Information), AU-2 (Event Logging) |

## Eugene Finding

> The MedData Nexus RAG chatbot does not produce structured audit logs for user queries, retrieved chunks, or model responses. If a data exposure occurs — PHI surfaced, secrets retrieved, unauthorized document accessed — there is no forensic trail to determine what was accessed, by whom, or when. The system cannot support an incident investigation, a compliance audit, or a HITL review chain without logs. **Rank: B. Route to CISO Constant Yung and IT Security.**

## Remediation

1. Implement structured audit logging on every RAG interaction before pilot expansion. Required fields per log entry:
   - `timestamp` (ISO 8601)
   - `user_id` and `role`
   - `query_text`
   - `retrieved_chunk_ids` and source document references
   - `model_response` (full text or hash for privacy-sensitive deployments)
   - `api_path` (internal RAG vs. external API)
   - `review_decision` and `reviewer_id` for high-risk outputs
2. Store logs in a tamper-resistant, append-only store. Retain per HIPAA minimum retention requirements.
3. Define log access controls — audit logs should be readable by IT Security and CISO; not editable by anyone.

## Validation

1. Submit five queries after audit logging is implemented.
2. Query the log store for each interaction by timestamp and user ID.
3. Verify all required fields are present and populated for each entry.
4. Verify a high-risk interaction shows a reviewer decision field.
5. Confirm logs are stored in the designated tamper-resistant location.
6. Confirm a human reviewer can reconstruct the full interaction from the log entry within 60 seconds.
