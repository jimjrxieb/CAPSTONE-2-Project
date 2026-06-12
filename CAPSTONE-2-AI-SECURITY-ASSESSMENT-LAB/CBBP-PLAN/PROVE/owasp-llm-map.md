# OWASP LLM Top 10 Mapping

This project standardizes on the OWASP Top 10 for LLM Applications 2025 list.

| Scenario | OWASP LLM 2025 Category | Why It Applies | Evidence | Remediation |
|---|---|---|---|---|
| Direct prompt injection | LLM01 Prompt Injection | User text attempts to override or reveal system instructions | `loop1-chatbox-rag-prove.md`; `Eugene-AI/evidence/break/chatbox-break-20260609T142715Z.json`; `Eugene-AI/evidence/eugene-helpfulness-eval-ollama-20260612T044252Z.json` | Input sanitizer, prompt isolation, rejection logging |
| Unauthorized role retrieval from ChromaDB | LLM08 Vector and Embedding Weaknesses; LLM02 Sensitive Information Disclosure | Vector retrieval can return chunks above the user's authorization tier | `Eugene-AI/evidence/break/unauthorized-retrieval-break-20260610T131529Z.json`; `Eugene-AI/evidence/break/platform-deployed-break-20260612T043154Z.json` | Role-filtered retrieval and post-retrieval tier checks |
| Poisoned document ingestion | LLM04 Data and Model Poisoning; LLM01 Prompt Injection | Corpus document contains adversarial instructions or unapproved data | `loop3-rag-corpus-prove.md`; corpus contamination BREAK evidence | Manifest gate, injection scan, owner alert |
| Secrets or PHI in corpus/output | LLM02 Sensitive Information Disclosure; LLM05 Improper Output Handling | Sensitive data could be indexed or reflected without filtering | Corpus contamination BREAK evidence; output filter tests | Secret/PHI scanner, output filter, HITL flag |
| Excessive tool authority | LLM06 Excessive Agency | AI tooling could touch paths or actions outside approved scope | AI dev tool boundary evidence | Deny-by-default tool authority and approval log |
| User overreliance on AI summary | LLM09 Misinformation | Users may treat advisory summaries as authoritative decisions | Helpfulness eval; HITL evidence | AI-generated label, citations, human review record |
| Resource or cost exhaustion | LLM10 Unbounded Consumption | High-volume requests can consume local compute or degrade API availability | `Eugene-AI/evidence/platform-control-check-20260612T045321Z.json`; `Eugene-AI/evidence/break/platform-deployed-break-20260612T043154Z.json` | Rate limits, timeouts, CPU/memory limits |
| AI-suggested dependencies | LLM03 Supply Chain | AI suggestions can introduce vulnerable or malicious dependencies | SCA workflow and exact-pin evidence in `Eugene-AI/evidence/platform-control-check-*.json`; live PR/CI bypass simulation pending | Exact pins, SCA scan, dependency review |
