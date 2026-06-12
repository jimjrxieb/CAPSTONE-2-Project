# COMPLY Phase Review — Fable Enhancements

> **Reviewer:** Claude (Fable 5)
> **Date:** 2026-06-10
> **Scope:** All 14 workpapers in `CBBP-PLAN/COMPLY/` plus cross-reference verification against `deliverables/`, `scenarios/`, `templates/`, `target-architecture/`, `CBBP-PLAN/BUILD/`, `CBBP-PLAN/PROVE/`, and `target-client/fake-data/`
> **Verdict:** This is consultant-grade COMPLY work. The methodology holds together, traceability is real (F-001–F-010 verified end-to-end), and the honesty discipline — inherent risk vs. proven control, policy claim vs. enforcement — is the strongest thing in the package. The issues below are framework currency, cross-document consistency, and a few gaps a 3PAO or sharp client reviewer would catch.

---

## 1. What You Got Right

### 1.1 The architecture-mismatch discipline is the signature move
The recurring pattern — *"policy claim vs. missing enforcement"* — is applied consistently across `meddata-trust-boundaries.md` (Architecture Mismatch Log), `meddata-threat-model.md` (T-07 deep dive), and `meddata-ai-adoption-maturity.md` (Human Approval Matrix: "a policy claim, not a proven control"). This is exactly how a senior GuidePoint assessor frames findings, and it's the difference between a checklist audit and an assessment. Keep this as the house style.

### 1.2 You governed the assessor, not just the client
Eugene is registered in the client's AI inventory (CAP2-AI-001), has its own harness spec (`Cap2-Harness.md`), and its own COMPLY scope workpaper (`capstone2comply.md`). Almost nobody does this. It pre-empts the obvious client objection — "who governs *your* AI?" — and it's a differentiator worth leading with in the PROVE package.

### 1.3 Inherent-risk honesty
`meddata-ai-risk-assessment.md` explicitly frames every score as "preliminary inherent risk until BUILD/BREAK evidence confirms control behavior," and `meddata-ai-adoption-intake.md` has an "Assumptions Pending Evidence" table separating working assumptions from confirmed facts. The former external-model assumption has since been removed from Eugene scope; shadow AI remains a finding trigger. This is defensible under audit. Most assessments silently convert assumptions to facts.

### 1.4 Finding traceability is real, not decorative
Verified: F-001 through F-010 exist in `deliverables/02-client-findings-report.md` and the IDs match their usage in `meddata-ai-harness.md` (Guardrail Layer), `comply-checklist.md` (BUILD Must Produce), and `meddata-ai-engineering-crew.md` (Guardrails table). Every guardrail traces to a finding; every finding traces to a BUILD task and a BREAK test. The corpus manifest referenced everywhere actually exists at `target-client/fake-data/corpus-manifest.md`.

### 1.5 Shadow AI handled correctly
MDN-AI-002 is consistently framed as *suspected/unverified* with a defined evidence path (network logs, endpoint DLP, staff survey) — a finding trigger, not an asserted incident. The risk-assessment temptation is to write "staff are leaking data to ChatGPT"; you wrote "we cannot prove they aren't," which is the correct and defensible claim.

### 1.6 Scope separation between Eugene and coding assistants
The Scope Clarification table in `meddata-coding-assistant-intake.md` (Eugene = system under governance; Claude Code/Codex = build tools, governed by `BUILD/ai-dev-assist-harness.md`) prevents the most common confusion in AI-on-AI assessments. The two-row "Role / Tool / Governed By" table is reusable as a template.

### 1.7 The right finding is on top
T-03 / F-001 (no ChromaDB access control) as the single S-rank, with the deep-dive justification "zero attacker sophistication required — the access boundary was never built," is the correct prioritization. The threat model's "frameworks are applied after the thinking, not before it" stance is also right and reads like a real practitioner wrote it.

### 1.8 The CISO Sentence convention
Ending each workpaper with one executive-readable sentence is a strong deliverable pattern. They're all genuinely good — no filler. Worth promoting to a standard template element across all GP-CONSULTING workpapers.

---

## 2. What's Out of Date

### 2.1 OWASP LLM Top 10 — you're mixing the 2023 and 2025 lists (highest-priority fix)
The workpapers mostly use **2023 numbering**: LLM02 = Insecure Output Handling, LLM03 = Training Data Poisoning, LLM04 = Model Denial of Service, LLM06 = Sensitive Information Disclosure, LLM09 = Overreliance. But `meddata-trust-boundaries.md` Boundary 3 cites **LLM07 (System Prompt Leakage)** — that entry only exists in the **2025 (v2.0)** list. The two lists are incompatible numbering schemes, and a reviewer who knows the current list will spot the mix immediately.

Standardize on the 2025 list. Migration map for the entries you use:

| You wrote (2023) | 2025 equivalent |
|---|---|
| LLM01 Prompt Injection | LLM01 (unchanged) |
| LLM02 Insecure Output Handling | LLM05 Improper Output Handling |
| LLM03 Training Data Poisoning | LLM04 Data and Model Poisoning |
| LLM04 Model Denial of Service | LLM10 Unbounded Consumption |
| LLM06 Sensitive Information Disclosure | LLM02 Sensitive Information Disclosure |
| LLM08 Excessive Agency | LLM06 Excessive Agency |
| LLM09 Overreliance | LLM09 Misinformation (closest fit) |
| — | LLM07 System Prompt Leakage (now valid) |

**The payoff:** the 2025 list has **LLM08 — Vector and Embedding Weaknesses**, a category purpose-built for your S-rank finding. T-03/F-001 currently maps to "LLM06/LLM08" under 2023 semantics; under 2025 it maps cleanly to **LLM08: Vector and Embedding Weaknesses + LLM02: Sensitive Information Disclosure**. That's a stronger, more current citation for your most important finding. Files to update: `meddata-threat-model.md` (Framework Mapping table), `meddata-trust-boundaries.md` (all six boundary mappings), `comply-checklist.md` (AI/RAG Harness Controls), and `CBBP-PLAN/PROVE/owasp-llm-map.md`.

### 2.2 "AI 600-1 Categories" header doesn't match NIST AI 600-1
`meddata-ai-risk-assessment.md` Section 2 is titled "AI-Specific Risk Identification (AI 600-1 Categories)" but the categories used — Accuracy/Reliability, Bias/Fairness, Privacy, Robustness, Transparency, Security — are generic trustworthy-AI dimensions, not the 12 GAI risks NIST AI 600-1 actually defines (Confabulation; Data Privacy; Information Security; Value Chain and Component Integration; Harmful Bias and Homogenization; Human-AI Configuration; Information Integrity; etc.). Either retitle the section ("AI Risk Dimensions") or add a 600-1 mapping column: hallucination rows → **Confabulation**, PHI/PII rows → **Data Privacy**, injection/poisoning rows → **Information Security**, dependency rows → **Value Chain and Component Integration**. Given the Big 4 / federal audience, the real-600-1 column is worth the 20 minutes.

### 2.3 MITRE ATLAS technique IDs need a verification pass
- **AML.T0054 is LLM Jailbreak**, but it's used for the poisoning rows (T-02, T-06, T-13). Poisoning has its own techniques in current ATLAS (RAG/data poisoning was added as a distinct technique family in 2024–2025; training-data poisoning is AML.T0020).
- **T-13 (unsafe dependency)** should map to **AML.T0010 — ML Supply Chain Compromise**, which is exactly this threat. The current AML.T0054 mapping is wrong.
- ATLAS expanded significantly across 2024–2025 with GenAI/agent techniques. Re-verify every ID in `meddata-threat-model.md` Framework Mapping and `CBBP-PLAN/PROVE/mitre-atlas-map.md` against the live ATLAS matrix before this goes in a client deliverable — stale ATLAS IDs are a credibility hit with exactly the audience (federal, MITRE-literate) this capstone targets.

### 2.4 Boundary 5's OWASP mapping is wrong on its own terms
`meddata-trust-boundaries.md` Boundary 5 cites "LLM04 (Model Denial of Service — supply chain variant)." Even in the 2023 list, supply chain was its own entry (LLM05 Supply Chain Vulnerabilities); in 2025 it's **LLM03 Supply Chain**. The DoS hook was never the right one for a coding-assistant-to-repo boundary.

### 2.5 The external model is unpinned while T-12 demands pinning
T-12 (runtime drift) and the harness both require model version pinning. The local path has it (`OLLAMA_MODEL` and `OLLAMA_EMBED_MODEL`). Earlier drafts referenced an external model family without a concrete model ID; that would have required pinning and retesting before use.

**Resolution note (2026-06-10):** Closed by scope decision, not by model pinning. Eugene/MDN-AI-001 is now local-only using Ollama; the external LLM path is out of scope and removed from active COMPLY/BUILD runtime configuration. Any future external LLM path requires a new COMPLY boundary, CISO approval, and renewed BREAK evidence.

### 2.6 Minor 800-53 misalignment
`meddata-threat-model.md` maps T-01 (prompt injection) to **SI-3** (Malicious Code Protection); `comply-checklist.md` maps the same control to **SI-10** (Information Input Validation). SI-10 is correct for input sanitization — align the threat model to it.

### 2.7 Framework coverage gaps for the target audience (optional adds)
- **ISO/IEC 42001** (AI management systems) — Big 4 audit teams increasingly map AI governance to it; one column in the PROVE crosswalks would cover it.
- **HIPAA Security Rule modernization** — HHS's proposed Security Rule update (NPRM, Dec 2024) pushes mandatory technical controls (encryption, MFA, asset inventories) that align with your findings; a one-line citation strengthens the healthcare framing.
- EU AI Act is correctly out of scope for a US healthcare client — but say so explicitly in one line in the README so the omission reads as deliberate.

---

## 3. What Can Be Improved

### 3.1 The Restricted-tier contradiction (material — fix before BUILD reads it)
Three documents disagree about what's in the corpus and how it's classified:

- `capstone2comply.md` and `meddata-rag-corpus-intake.md`: baseline corpus is **Internal/Confidential only; no Restricted-tier documents** — HIPAA assessment records and security findings are listed as part of that Internal/Confidential baseline.
- `meddata-ai-harness.md` Section 2: HIPAA assessment records, security assessment findings, and incident response records are classified **Restricted — IT Security team only**.

This matters more than any other inconsistency because the role→tier mapping is the implementation spec for **F-001, the S-rank finding**. BUILD will implement whichever table it reads first. Pick one classification scheme, declare a single source of truth (the harness Section 2 table is the better candidate — it's the most granular), and make the other two documents reference it instead of restating it.

### 3.2 The numbers don't reconcile across documents
- **13** threats (T-01–T-13) · **12** scenario files in `scenarios/` · "all **12** BREAK scenarios" (`meddata-ai-risk-assessment.md`) · "All **10** tests in meddata-break-validation.md" (`Cap2-Harness.md`) · **10** BREAK tests listed in the harness sketch.
- README claims "**10** findings in client-findings-report.md" (verified correct) — but the intake documents 7 finding triggers, the inventory has 5 MDN-GOVERN-00x findings, and nothing maps MDN-GOVERN-00x → F-00x.

None of these are wrong individually — they're different lenses — but a 3PAO will ask you to reconcile them. Fix with one **traceability matrix** (new file or a section in the README): `T-ID → F-ID → MDN-GOVERN-ID → scenario file → BREAK test # → PROVE evidence artifact`. One table kills every "why do these counts differ?" question permanently, and it's the artifact a Big 4 workpaper reviewer would build anyway.

### 3.3 Hold Eugene to the standard you hold the client to
`meddata-ai-inventory.md` says CAP2-AI-001 "**HITL Enforced: Yes**" — but `Cap2-Harness.md` says every guardrail is "enforced by workflow convention." That is *precisely* the "policy claim vs. missing enforcement" mismatch you flag the client for in six places. Two options: downgrade the inventory cell to "Procedural — enforced by convention, not technical gate," or add one technical artifact (e.g., a required `reviewer_signoff` field in the evidence JSON schema that the PROVE packager rejects as incomplete if absent). The second option is a half-day of work and turns a self-consistency wobble into a demo: "we found this class of gap in our own tool and closed it."

### 3.4 Missing threats worth adding to the model
- **T-14: Vector store infrastructure exposure.** Default ChromaDB ships with **no authentication at all** — anyone with network reach to the Chroma port can read every collection. This is distinct from T-03 (role-based retrieval through the app); it's the path *around* the app. Maps to LLM08:2025, SC-7, IA-2. Given the S-rank finding lives in ChromaDB, the network/infra exposure of the same component is a conspicuous absence.
- **T-15: Embedding-layer attacks** — embedding inversion (reconstructing document text from stored vectors) and cross-collection leakage. This is the other half of LLM08:2025 and the reason "delete the document" doesn't mean "the data is gone" in a vector DB.
- **T-16: Unbounded consumption.** Rate limiting appears as a guardrail in the harness with no threat driving it — a control without a threat breaks your own traceability rule. Add the threat (local resource exhaustion / availability degradation), map to LLM10:2025, SC-5.
- **User overreliance** exists as a C-rank risk row ("user cannot distinguish AI summary from authoritative document") but never enters the threat model. For a system whose output influences compliance and legal decisions, a one-row T-entry (maps to LLM09:2025, Human-AI Configuration in 600-1) closes the loop.

### 3.5 Anchor the L×I scale
The 1–5 likelihood and impact scales have no anchor definitions, so two assessors will score the same risk differently — the first thing a 3PAO probes on a scored register. Add a six-line table to `meddata-ai-risk-assessment.md` (or the template): L1 = requires nation-state capability … L5 = happens through normal authorized use; I1 = cosmetic … I5 = regulated-data exposure / reportable incident. T-03's "zero attacker sophistication" deep-dive already *is* an L-anchor argument — formalize it.

### 3.6 Adopt the GP-Copilot audit trail standard in workpaper headers
Workpapers carry date and assessor but not the platform's audit-run fields (`run_id`, `analyst` with version, `evidence_file`). Adding three header lines (e.g., `run_id: 20260608T112437Z`, `analyst: jimjrxieb + eugene:v0.1`, `evidence_file:` path to the ingest/baseline JSON) makes COMPLY artifacts match the 3PAO presentation map in CLAUDE.md and lets the PROVE package index them mechanically. The ingestion evidence already has timestamps — the linkage is the missing piece.

### 3.7 Path hygiene for RAG/tooling consumption
Cross-references use inconsistent bases: `BUILD/ai-dev-assist-harness.md` (actually `../BUILD/` from this folder), `templates/...` and `lessons/...` (lab-root relative), `target-architecture/trust-boundaries.md` (lab-root). All targets exist (verified), but the inconsistency breaks mechanical link-checking and RAG ingestion of these docs into JADE's corpus. Standardize on lab-root-relative paths with a one-line convention note in the README.

### 3.8 Small fixes
- `meddata-ai-adoption-maturity.md` rates "AI-assisted development controls" **Ad Hoc** while its evidence cell says the dimension is "not applicable to current scope." Rate it on the ingestion-pipeline evidence (which the gap text already describes) or mark it N/A — not both.
- README Exit Gate says "10 findings in client-findings-report.md" under the criterion "scope findings created" — accurate, but cite the F-ID range (F-001–F-010) so the claim is checkable without opening the file.
- `capstone2comply.md` data boundary table allowed Internal-tier data to an external API "with approved external AI tool" while the external model path was still an unevidenced assumption per the intake. This is now closed by removing the external LLM path from Eugene scope.

---

## Priority Order

| # | Action | Why first | Effort |
|---|---|---|---|
| 1 | Reconcile Restricted-tier classification (3.1) | Feeds the S-rank fix; BUILD implements whichever table it reads | 1 hr |
| 2 | Migrate OWASP LLM mappings to 2025 list (2.1, 2.4) | Visible currency error; strengthens the S-rank citation via LLM08:2025 | 2 hrs |
| 3 | Build the traceability matrix (3.2) | Kills every count-reconciliation question; 3PAO-ready artifact | 2 hrs |
| 4 | Verify/fix ATLAS IDs (2.3) and SI-3→SI-10 (2.6) | Wrong IDs in client deliverables | 1 hr |
| 5 | Fix Eugene HITL claim (3.3) | Self-consistency; turns a wobble into a selling point | 0.5–4 hrs |
| 6 | Add T-14/T-15/T-16 (3.4) + remove external LLM path from Eugene scope (2.5) | Closes the real coverage gaps before BREAK planning finalizes | 2 hrs |
| 7 | 600-1 mapping column (2.2), L×I anchors (3.5), header standard (3.6), path hygiene (3.7), small fixes (3.8) | Polish; do before PROVE package closes | 3 hrs |

**Bottom line:** The methodology and honesty discipline are the hard parts, and they're done right. Everything above is correctable in roughly two working days, and items 1–4 are the ones a skeptical reviewer would find first.
