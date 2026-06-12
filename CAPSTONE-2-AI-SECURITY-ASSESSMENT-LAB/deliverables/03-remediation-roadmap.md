# Remediation Roadmap — MedData Nexus Health Systems

> AI Security Assessment — Capstone 2
> Prepared by: jimjrxieb + Eugene (CAP2-AI-001, advisory)
> Date: 2026-06-08
> CISO: Constant Yung
> Input: `deliverables/02-client-findings-report.md`, `CBBP-PLAN/BREAK/meddata-break-validation.md`

---

## Sequencing Principle

Remediation order follows risk rank, not implementation effort.

The S-rank finding blocks all pilot expansion. It goes first regardless of complexity. B-rank pilot expansion blockers come next — all five must be resolved or risk-accepted before the pilot can expand. C-rank findings must be resolved before production. No exception.

Do not start BUILD work on a later phase while an earlier phase has an open S-rank or B-rank pilot blocker.

---

## Immediate — Before Any Pilot Expansion

**Owner: Platform Engineering Lead + CISO Constant Yung**
**Deadline: Before any user count increase or new corpus category added**

These items are not time-boxed to a sprint. They are gates. The pilot does not expand until they are closed.

### Gate 1 — Run All 10 BREAK Tests (Prerequisite)

No remediation can be validated without test execution. Execute all 10 BREAK tests from `CBBP-PLAN/BREAK/meddata-break-validation.md`. Record evidence in `evidence/` with date-stamped folders per test. This is the prerequisite for all remediation validation.

### Gate 2 — F-001: Implement ChromaDB Role-Based Access Control

Finding: F-001, S-rank, Score=20.

Implementation steps:
1. Define ChromaDB collections by sensitivity tier (Public, Internal, Confidential, Restricted).
2. Map each pilot user role to allowed collection tiers.
3. Pass user role as a query parameter on every ChromaDB request.
4. Add post-retrieval tier check: reject any chunk from an unauthorized tier before including it in the prompt.
5. Test with role × category access matrix. Every restricted-category cell for low-privilege roles must return empty.
6. CISO Constant Yung signs off on the access matrix and the BREAK test result before pilot expands.

Validation: BREAK test 4 returns PASS for all role × restricted-category combinations.

### Gate 3 — F-005: Implement Structured Audit Logging

Finding: F-005, B-rank, governance multiplier.

This gate comes second because without logging, no other remediation can be validated forensically.

Implementation steps:
1. Add audit log middleware to the RAG API. Log every interaction.
2. Required fields per entry: timestamp (ISO 8601), user_id, role, query_text, retrieved_chunk_ids, source_references, model_response, api_path, reviewer_decision (high-risk).
3. Write logs to append-only store. Set HIPAA-compliant retention policy.
4. Restrict write access to the log store. Only the platform service account writes. IT Security and CISO have read access.
5. Define log alerting for high-risk interactions flagged without a reviewer decision.

Validation: BREAK test 5 — submit five queries; all required fields present in each log entry.

---

## 30 Days — Pilot Expansion Blockers

**Owner: Platform Engineering Lead**
**Deadline: 2026-07-08**

These items block pilot expansion alongside the S-rank gate above. All five must be remediated or formally risk-accepted by CISO Constant Yung before the pilot adds users or corpus categories.

### F-002 — Input Sanitization and Prompt Injection Defense

1. Add input sanitization layer before queries reach the model. Detect and reject injection pattern signatures.
2. Enforce system prompt isolation: user query field cannot override or read system instructions.
3. Test with all three injection patterns from BREAK test 1.
4. Log rejected queries with the rejection reason.

Validation: BREAK test 1 — all three injection queries rejected at input layer; system prompt text absent from all responses.

### F-003 — Corpus Approval Workflow and Hash Verification

1. Create a signed corpus manifest. Every document in the ingest path must have a corresponding manifest entry with: filename, hash, owner, approval date, approver identity, and sensitivity tier.
2. Add hash verification step to the ingestion pipeline. Any document whose hash does not match the manifest entry is rejected.
3. Add content scan on ingest: flag documents containing adversarial instruction patterns for human review before indexing.
4. Log every ingestion decision (accepted / rejected / flagged for review).

Validation: BREAK test 2 — poisoned document placed in ingest dir; pipeline rejects it; confirmed absent from ChromaDB; no poisoned chunk retrievable.

### F-004 — Pre-Ingestion Secrets and PHI Scanning

1. Add detect-secrets and gitleaks to the ingestion pipeline. Reject any document that matches credential patterns.
2. Add PHI pattern scanner (SSN, MRN, DOB, diagnosis code patterns) to the same gate.
3. Add output filter: intercept credential and PHI patterns in the model response before delivery to the user.
4. Log every scanning decision with the matched pattern type (not the matched value).

Validation: BREAK test 3 — document with fake credential rejected at ingest; fake credential absent from all query responses.

### F-006 — HITL Enforcement

1. Define the list of output categories that require human review before distribution: vendor risk decisions, security assessment conclusions, HIPAA-adjacent outputs, legal document summaries.
2. Add a HITL gate to the RAG response workflow: high-risk outputs are flagged; a reviewer identity field and decision field are required before the output is released.
3. Build the approval record with: reviewer identity, decision, scope, timestamp, and output reference.
4. Technical gate: flagged outputs that lack an approval record cannot be forwarded or exported.

Validation: Attempt to distribute a high-risk output without a review record; gate blocks it. Confirm approval log captures required fields.

### F-007 — Shadow AI Audit and MDN-AI-002 Investigation

1. CISO Constant Yung initiates a shadow AI audit within 15 days.
2. Review endpoint logs for AI service traffic (OpenAI, Anthropic, Google AI, Cohere, etc.) not originating from the approved platform.
3. For any identified tool: determine what data was transmitted; assess exposure; determine if a breach notification is required.
4. Issue an acceptable use policy update. All AI tools must be registered before use.
5. Deploy endpoint DLP rules to detect AI service traffic from unapproved endpoints.

Validation: Shadow AI audit results show no unregistered AI service traffic. All tools in use appear in the approved AI inventory.

---

## 60 Days — Production Gates

**Owner: Platform Engineering Lead + security lead**
**Deadline: 2026-08-08**

These items must be resolved before production authorization. They do not block pilot continuation but must be in place before a production go-live decision.

### F-008 — CI Gate for AI-Assisted PR Disclosure

1. Create a GitHub Actions label-check workflow that fails CI if the `ai-assisted` label is absent on a PR touching sensitive paths (ingestion pipeline, RAG query handler, auth, config).
2. Update the PR template to include an AI disclosure question as a required checkbox.
3. Document which paths are classified as sensitive in CODEOWNERS or a path-sensitivity config file.

Validation: BREAK test 6 — PR without `ai-assisted` label on sensitive path fails CI. PR with label passes.

### F-009 — CODEOWNERS for Auth-Sensitive Paths

1. Create a CODEOWNERS file in the root of the repository.
2. Map auth-sensitive paths (login, token validation, role check, session management) to a named security reviewer as required approver.
3. Require auth behavior test coverage to be green before merge on these paths.
4. Document the security reviewer checklist: what the reviewer verifies, what they sign off on.

Validation: BREAK test 7 — auth-path PR with only standard reviewer is blocked by CODEOWNERS. Security reviewer approval unblocks it.

### F-010 — SCA Gate for AI-Suggested Dependencies

1. Add pip-audit to CI. Fail on any CVE above CVSS 7.0.
2. Add license check: reject packages with incompatible licenses (GPL in proprietary codebase, etc.).
3. Add pin enforcement: reject any `requirements.txt` line using range specifiers (`>=`, `~=`) without an upper bound.
4. Update PR template: require written human justification for any new dependency addition.

Validation: BREAK test 8 — unpinned package in requirements fails CI. Pinned package with justification and clean pip-audit passes.

---

## 90 Days — Operating Model Hardening

**Owner: Platform Engineering Lead + CISO Constant Yung**
**Deadline: 2026-09-08**

These items represent the operating model that makes the controls sustainable, not just present.

### Runtime Drift Prevention

1. Pin the model version in the RAG configuration. Document the pinned version in the architecture record.
2. Define a re-test requirement: any model version change triggers mandatory re-execution of BREAK tests 1–5 before the new version goes live.
3. Disable the FastAPI docs endpoint (`/docs`, `/redoc`) in production. Confirm ChromaDB is not reachable from outside the service mesh.
4. Confirm CORS headers restrict access to the approved origin list.
5. Implement and test rate limiting.

Validation: BREAK test 9 — all runtime drift checks return expected results. No docs endpoint, no exposed ChromaDB, restricted CORS, rate limit triggers, model version matches documentation.

### CI Exception Register

1. Define the exception process: what constitutes a CI gate bypass, who can approve it, how long the exception is valid.
2. Build an exception register: each entry records the bypass type, justification, approver, expiry date, and associated PR.
3. Require all CI exception approvals to flow through the register. No silent bypass path.

Validation: BREAK test 10 — bypass attempt generates a log entry and requires approval. Confirm exception register captures the full record.

### PROVE Package Completion

1. Run all 10 BREAK tests against the remediated system. Collect evidence in date-stamped folders.
2. Update `deliverables/02-client-findings-report.md` with REMEDIATED or ACCEPTED status for each finding.
3. Update `CBBP-PLAN/BREAK/meddata-break-validation.md` with actual results.
4. Generate the final PROVE package: client findings report, remediation roadmap completion record, evidence index, and CISO sign-off record.
5. CISO Constant Yung reviews and signs the production authorization decision.

---

## Remediation Sequence Summary

| Phase | Items | Deadline | Gate |
|---|---|---|---|
| Immediate — run BREAK tests | Prerequisite for all validation | No date — run now | Pilot cannot expand without |
| Immediate — S-rank | F-001 (ChromaDB RBAC) + F-005 (audit logging) | Before any pilot expansion | Hard block |
| 30 days | F-002, F-003, F-004, F-006, F-007 | 2026-07-08 | Pilot expansion blockers |
| 60 days | F-008, F-009, F-010 | 2026-08-08 | Production gates |
| 90 days | Runtime drift, exception register, PROVE package | 2026-09-08 | Operating model |
