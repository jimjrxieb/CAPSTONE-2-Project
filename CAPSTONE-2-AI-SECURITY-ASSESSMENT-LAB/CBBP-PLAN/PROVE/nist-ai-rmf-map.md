# NIST AI RMF Mapping

| Scenario | AI RMF Function/Subcategory | Why It Applies | Evidence | Remediation |
|---|---|---|---|---|
| Direct prompt injection | MEASURE 2.11; MANAGE 2.4 | Prompt-injection resistance must be measured and managed before pilot expansion. | `Eugene-AI/evidence/break/chatbox-break-20260609T142715Z.json`; `Eugene-AI/evidence/eugene-helpfulness-eval-ollama-20260612T044252Z.json`; `Eugene-AI/evidence/crewai/dry-run-rag-direct-prompt-injection.json` | Keep sanitizer/output-filter tests in BREAK and require human review before findings become final. |
| Unauthorized retrieval / access boundary | GOVERN 1.5; MAP 5.1; MEASURE 2.11 | Role-bound retrieval and vector DB isolation are core accountability and security measurement claims. | `Eugene-AI/evidence/break/unauthorized-retrieval-break-20260610T131529Z.json`; `Eugene-AI/evidence/break/platform-deployed-break-20260612T043154Z.json` | Bind identity to role server-side, maintain NetworkPolicy, and rerun unauthorized retrieval BREAK before expansion. |
| Runtime and model pinning | MAP 3.5; MANAGE 4.1 | Model/runtime changes can invalidate prior assessment evidence. | `Eugene-AI/evidence/platform-control-check-20260611T194349Z.json`; `Eugene-AI/evidence/eugene-helpfulness-eval-ollama-20260612T044252Z.json` | Pin generation and embedding model tags/digests and rerun evals after changes. |
