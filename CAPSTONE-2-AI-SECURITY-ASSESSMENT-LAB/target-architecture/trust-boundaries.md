# Trust Boundaries — MedData Nexus Internal RAG System

> Last updated: 2026-06-08
> Full security analysis: `CBBP-PLAN/COMPLY/meddata-trust-boundaries.md`
> Scope: baseline target architecture. See `../CBBP-PLAN/BUILD/sprint1-status.md` for implemented Eugene controls and evidence.

## Boundary Map

```
[User] ──(auth + input sanitization)──> [RAG App]
           untrusted input enters here

[RAG App] ──(role-gated query)──> [ChromaDB Vector DB]
           sensitive documents retrieved here

[RAG App] ──(prompt construction + system prompt isolation)──> [LLM / Eugene Model]
           system instructions + retrieved chunks assembled here

[LLM Model] ──(output filter + source attribution)──> [RAG App] ──> [User]
           sensitive content can leak here

[AI Tool] ──(PR label + scan gate + human review)──> [Repo / Production]
           code or config changes exit here

[Human Reviewer] ──(recorded approval)──> [Production Action / Risk Acceptance]
           authority boundary — no approval record = no action
```

## Boundary Status Summary

| Boundary | Accepts Untrusted Input | Exposes Sensitive Data | Requires Human Approval | Logged | Current Status |
|---|---|---|---|---|---|
| User → RAG App | Yes | No (query only) | No | Yes in Eugene evidence | Token-bound role enforcement implemented in Eugene |
| RAG App → Vector DB | No | Yes | No | Yes in Eugene evidence | Role-filtered retrieval implemented; live direct-DB proof remains hardening |
| RAG App → Model | No | Yes (via chunks) | No | Partial | Sprint 1 uses deterministic draft path; live generation needs separate evidence |
| Model Output → User | No | Yes (response) | Yes (high-risk) | Yes in Eugene evidence | Output filter and HITL flags implemented; human final judgment remains required |
| AI Tool → Repo | No | No (code only) | Yes | Workflow evidence | CODEOWNERS, AI-assisted PR labeling, and SCA workflow exist |
| Human Approval → Production Action | No | No | Yes — always | Review evidence | HITL review route/evidence exists; production-grade approver integration is future work |
