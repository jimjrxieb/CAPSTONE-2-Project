# COMPLY Phase — MedData Nexus AI Security Assessment

> **Engagement:** GP-Copilot Capstone 2
> **Client:** MedData Nexus Health Systems | CISO: Constant Yung
> **Assessor:** jimjrxieb + Eugene (CAP2-AI-001, advisory)
> **Date:** 2026-06-08
> **Status:** COMPLY COMPLETE — all workpapers filled, no open intake blockers

---

## What COMPLY Is

COMPLY answers one question before anything else is touched:

> Do we understand what this AI system is, who owns it, what data it can see, what it is allowed to do, and what evidence must exist before it is governed?

You do not harden what you have not mapped. You do not test what you have not scoped. COMPLY is the map.

---

## COMPLY Contents — Client System (MDN-AI-001)

These are the client-facing deliverables for MedData Nexus. A GuidePoint engagement produces all of these before BUILD begins.

| File | What It Is | CBBP Phase | Lesson | Status |
| --- | --- | --- | --- | --- |
| `meddata-ai-adoption-intake.md` | Full intake questionnaire — use case, owners, data, tools, governance, incident, pilot status | COMPLY | 02 | COMPLETE |
| `meddata-ai-inventory.md` | AI system registry — MDN-AI-001 (High Risk), MDN-AI-002 (unregistered, GOVERN 1.1 FAIL), CAP2-AI-001 | COMPLY | 02 | COMPLETE |
| `meddata-ai-risk-assessment.md` | Risk scored against NIST AI RMF — 1 S-rank, 9 B-rank, 6 C-rank. Post-mitigation projection: Moderate Risk | COMPLY | 02/03 | COMPLETE |
| `meddata-ai-adoption-maturity.md` | 12-dimension maturity assessment — Overall: Emerging (2/4). 6 of 12 dimensions rated Ad Hoc | COMPLY | 03 | COMPLETE |
| `meddata-trust-boundaries.md` | 6 trust boundaries mapped with controls, gaps, and fail-closed behavior | COMPLY | 04 | COMPLETE |
| `meddata-rag-corpus-intake.md` | 10 corpus intake questions answered — ownership matrix, evidence gaps, COMPLY exit criteria for RAG | COMPLY | 05 | COMPLETE |
| `meddata-coding-assistant-intake.md` | Coding assistant governance intake — 11 questions, tool authority matrix, 7 COMPLY findings | COMPLY | 06 | COMPLETE |
| `meddata-threat-model.md` | 17 threats (T-01–T-17), 3 deep-dives, full framework mapping (OWASP LLM 2025 + MITRE ATLAS + AI RMF + 800-53) | COMPLY | 07 | COMPLETE |
| `meddata-ai-harness.md` | AI harness specification for MDN-AI-001 — authority stack, data boundary, tool boundary, human approvals, guardrails, evidence layer, BUILD checklist | COMPLY | 11 | COMPLETE |
| `meddata-ai-engineering-crew.md` | AI engineering crew design for MedData Nexus — role-based AI governance for the engineering team | COMPLY | 12 | COMPLETE |
| `comply-checklist.md` | GRC-to-BUILD handoff checklist — SSP scope, AI/RAG controls, Kubernetes/CKS controls, AI-assisted engineering gates, NIST and SecAI+ concept mapping | COMPLY | 11/12 | COMPLETE |

---

## COMPLY Contents — Assessment Lab (CAP2-AI-001)

These govern Eugene and the Capstone 2 assessment workflow itself.

| File | What It Is | Status |
| --- | --- | --- |
| `Cap2-Harness.md` | Eugene harness specification — authority stack, data boundary, tool boundary, human approval gates, guardrail layer, evidence layer, BUILD checklist | COMPLETE |
| `capstone2comply.md` | Capstone 2 COMPLY scope workpaper — scoped intake for MedData Nexus, ownership requirements, data boundary table, evidence requests, COMPLY finding triggers, exit criteria | COMPLETE |

---

## What These Files Prove Together

| Claim | File(s) That Support It |
| --- | --- |
| We know what AI systems are in use | `meddata-ai-inventory.md` |
| We know who owns the system and who can accept risk | `meddata-ai-adoption-intake.md`, `capstone2comply.md` |
| We have measured AI adoption maturity honestly | `meddata-ai-adoption-maturity.md` |
| We have mapped the architecture and trust boundaries | `meddata-trust-boundaries.md` |
| We know what data is in the corpus and who approved it | `meddata-rag-corpus-intake.md` |
| We know how coding assistants are governed | `meddata-coding-assistant-intake.md` |
| We have risk-scored the system against NIST AI RMF | `meddata-ai-risk-assessment.md` |
| We have threat-modeled how the system could fail | `meddata-threat-model.md` |
| We have defined the harness the client needs to build | `meddata-ai-harness.md` |
| We have designed the AI engineering governance model | `meddata-ai-engineering-crew.md` |
| We have a concise GRC-to-DevSecOps handoff checklist | `comply-checklist.md` |
| We have governed our own assessment tool (Eugene) | `Cap2-Harness.md`, `capstone2comply.md` |

---

## COMPLY Exit Gate Status

Per `capstone2comply.md` exit criteria — status as of 2026-06-08:

| Criterion | Status |
| --- | --- |
| System name and use case defined | SATISFIED |
| Business, technical, risk, and data owners named | PARTIAL — named roles; individuals not confirmed by client |
| Users and roles scoped | SATISFIED |
| Approved AI tools listed | SATISFIED |
| Prohibited data is explicit | SATISFIED |
| Human-only decisions documented | SATISFIED |
| Top evidence requests mapped to artifacts | SATISFIED — all gaps documented as findings |
| Scope findings created for missing governance facts | SATISFIED — 10 findings in client-findings-report.md |

**COMPLY is complete.** Outstanding items are findings tracked in `deliverables/02-client-findings-report.md` — they move to BUILD/BREAK/PROVE, not back to COMPLY.

---

## Framework Coverage

| Framework | Where It's Applied |
| --- | --- |
| NIST AI RMF (GOVERN, MAP, MEASURE, MANAGE) | `meddata-ai-risk-assessment.md`, `meddata-threat-model.md`, `meddata-ai-harness.md` |
| NIST 800-53 Rev 5 (AC, AU, CA, CM, IA, SA, SC, SI, SR) | `meddata-trust-boundaries.md`, `meddata-threat-model.md`, `deliverables/02-client-findings-report.md` |
| OWASP LLM Top 10 | `meddata-threat-model.md`, `deliverables/02-client-findings-report.md` |
| MITRE ATLAS | `meddata-threat-model.md`, `deliverables/02-client-findings-report.md` |
| HIPAA (data boundary, audit logging, PHI controls) | `meddata-rag-corpus-intake.md`, `meddata-ai-harness.md`, `meddata-ai-adoption-intake.md` |

---

## Handoff to BUILD and BREAK

COMPLY is input to BUILD and BREAK. Nothing in COMPLY authorizes pilot expansion or production use.

- **BUILD reads:** `meddata-ai-harness.md` (Section 6 Implementation Checklist) to know what to implement
- **BUILD also reads:** `comply-checklist.md` to translate GRC scope into DevSecOps work items, including Kubernetes/CKS-style platform controls
- **BREAK reads:** `meddata-threat-model.md` (all 17 threats) and `meddata-ai-harness.md` (Section 5 Guardrail Layer) to know what to test
- **PROVE reads:** `deliverables/02-client-findings-report.md` to know what was found and what is open

The S-rank finding (F-001 — no ChromaDB access control) is a hard block on pilot expansion regardless of BUILD progress. See `CBBP-PLAN/PROVE/meddata-prove-package.md`.

## Traceability

COMPLY threat, finding, governance, BUILD, BREAK, and PROVE references are reconciled in `CBBP-PLAN/COMPLY/traceability-matrix.md`. That matrix explains why threat counts, finding counts, and evidence counts differ across workpapers and is the handoff reference for BUILD.
