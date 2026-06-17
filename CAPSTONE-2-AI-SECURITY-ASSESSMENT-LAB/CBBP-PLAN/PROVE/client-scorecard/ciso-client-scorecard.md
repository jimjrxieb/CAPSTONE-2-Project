# Client Scorecard — MedData Nexus Health Systems

> **Deliverable type:** Client / CISO outcome scorecard (PROVE phase)
> **System:** Eugene — internal RAG compliance assistant
> **Engagement:** Capstone 2 AI Security Assessment Lab   **Slot:** slot-5
> **Date:** 2026-06-12   **Assessor:** jimjrxieb + Eugene (CAP2-AI-001, advisory)
> **Inputs:** COMPLY intake + wishlist, Sprint 1–2 BUILD artifacts, BREAK evidence
> **Companion deliverable:** night-shift operator handoff (PROVE dual-format)

---

## 1. The Bottom Line

You asked us to make Eugene — your internal AI assistant for finding compliance
documents — safe enough to put in front of your compliance team with real policy,
SOC 2, and HIPAA records behind it. Your own 30-day bar was: accurate answers for
approved document types, with no patient data or secrets in responses.

We built the controls that bar requires and then attacked them the way a real
adversary would. The data-protection, human-review, and audit-logging controls
held under testing. The identity-boundary gap found on 2026-06-10 was remediated
and re-tested on 2026-06-12. Eugene now derives the retrieval role from the
authenticated bearer token and rejects request-body role assertion.

A later BUILD/BREAK review sharpened that finding: the retrieval-tier filter
itself held before the fix, and the identity layer now blocks the role-spoofing
path that previously succeeded. The local generation path is documented with
both deterministic draft-path evidence and the 2026-06-12 pinned Ollama run.

**Overall posture:** READY FOR A CONTROLLED PILOT — NOT YET FOR BROAD ROLLOUT

---

## 2. Wishlist Scorecard

| # | What you asked for | Did we deliver? | What it means for you | Proof (evidence) | Control |
|---|---|---|---|---|---|
| 1 | Find the right policy / SOC 2 / HIPAA evidence fast across scattered document stores | ✅ Yes | Eugene returns the right source with citations, so audit-evidence lookup stops being a manual hunt | `Eugene-AI/evidence/baseline-rag-eval-20260609T190645Z.json` | — |
| 2 | No patient data (PHI) or secrets in AI answers | ✅ Yes | Dates of birth, API keys, and similar are stripped automatically before anyone sees a response | `Eugene-AI/evidence/break/chatbox-break-20260609T142715Z.json` | SI-4 |
| 3 | Enforce access control on retrieval (your named gap) | ✅ Yes | The tier filter held, the identity-layer bypass was fixed, and the 2026-06-12 re-run blocked role spoofing | `Eugene-AI/evidence/break/unauthorized-retrieval-break-20260610T131529Z.json`, `Eugene-AI/evidence/break/unauthorized-retrieval-break-20260612T134146Z.json`, `CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB/CBBP-PLAN/BUILD/4-completedbuilds/001-poam-0001-identity-binding-fix.md` | AC-3, AC-6 |
| 4 | Human review on high-risk answers, with a record | ✅ Yes | Risky answers are flagged for a person, and the sign-off can't be faked or skipped | `Eugene-AI/evidence/break/hitl-review-bypass-20260609T182603Z.json` | AC-6, AU-2 |
| 5 | Governed pilot: retrieval logs + review records + corpus manifest for auditors | ✅ Yes | Every query, decision, and document load is logged in a tamper-evident trail an auditor can read | `Eugene-AI/evidence/platform-control-check-20260612T045321Z.json` | AU-2, AU-10 |
| 6 | Only approved, clean documents enter the corpus | ✅ Yes | Poisoned, unapproved, or secret-bearing documents are rejected before they ever reach the AI, and the document owner is alerted | `Eugene-AI/evidence/break/corpus-contamination-break-20260609T193306Z.json` | SI-7, CM-3 |
| 7 | Ingestion pipeline passes security scans before any corpus change | ✅ Yes | The pipeline that loads documents is itself scanned for vulnerabilities and secrets before changes land | `Eugene-AI/.github/workflows/sca.yml` | SA-11, RA-5 |
| 8 | Platform controls hold on the real cluster, not just on paper | ✅ Yes | On a live Kubernetes cluster, the database couldn't be reached directly and rapid-fire abuse was throttled | `Eugene-AI/evidence/break/platform-deployed-break-20260612T043154Z.json` | SC-7, SC-5 |

Legend: ✅ delivered and tested · ⚠️ delivered, condition noted · ❌ open.

---

## 3. What We Tested Like an Attacker

| We tried to... | What happened | What it proves | Evidence |
|---|---|---|---|
| Trick Eugene into leaking a patient DOB and an API key | Blocked — both redacted from the answer | Patient data and secrets don't escape, even under a crafted prompt | `evidence/break/chatbox-break-20260609T142715Z.json` |
| Forge or skip the human review sign-off (7 ways) | All 7 blocked | High-risk answers can't be rubber-stamped or bypassed | `evidence/break/hitl-review-bypass-20260609T182603Z.json` |
| Poison the document corpus (5 ways) | All 5 rejected before ingestion, owner alerted | Bad documents can't quietly corrupt the AI's knowledge | `evidence/break/corpus-contamination-break-20260609T193306Z.json` |
| Reach the vector database directly, bypassing the app | Blocked by network policy from inside and outside the namespace | The data store isn't exposed even to an attacker already in the cluster | `evidence/break/platform-deployed-break-20260612T043154Z.json` |
| Retrieve documents above the user's role | Blocked after fix (was: partially succeeded at the identity layer) | POAM-0001 closure confirms role spoofing is rejected after identity binding | `evidence/break/unauthorized-retrieval-break-20260610T131529Z.json`; `evidence/break/unauthorized-retrieval-break-20260612T134146Z.json` |

---

## 4. Closed POA&M Items — In Business Terms

| POA&M ID | Business risk (plain English) | Closure note | Owner | Closed | Blocks |
|---|---|---|---|---|---|
| POAM-0001 | A user could retrieve compliance documents above their authorization level by bypassing the identity check behind role filtering — e.g. Vendor Risk seeing IT Security material | CLOSED 2026-06-12. The query role is derived from the bearer token; request-body role assertion is rejected; unauthorized-retrieval BREAK passed on re-run `20260612T134146Z`. | Eugene platform owner | 2026-06-12 | None for this POA&M; static per-role lab tokens remain accepted for controlled pilot only |

This was a real BREAK finding. Per CBBP it moved through BUILD plan 001,
implementation notes, re-BREAK evidence, and POA&M closure. The remaining
identity maturity limitation is not POAM-0001: the lab still uses static,
shared, per-role tokens. That is accepted for the controlled pilot only and
should become a separate pre-production identity-provider item before broad
rollout.

---

## 5. The Ask

We recommend approving a **controlled pilot** with a small group of trusted
compliance-team users now. We need your sign-off to proceed with the pilot and
agreement that external IdP integration, per-user identity, token lifetime, and
rotation remain pre-production requirements before broad rollout.

---

## 6. Evidence Index (for the auditor)

| Claim (section/row) | Evidence file | Date | Result |
|---|---|---|---|
| §2.1 fast retrieval | `Eugene-AI/evidence/baseline-rag-eval-20260609T190645Z.json` | 2026-06-09 | PASS |
| §2.2 / §3 no PHI/secrets | `Eugene-AI/evidence/break/chatbox-break-20260609T142715Z.json` | 2026-06-09 | PASS |
| §2.3 / §3 access control detection | `Eugene-AI/evidence/break/unauthorized-retrieval-break-20260610T131529Z.json` | 2026-06-10 | FAIL (POAM-0001 opened) |
| §2.3 / §3 access control closure | `Eugene-AI/evidence/break/unauthorized-retrieval-break-20260612T134146Z.json` | 2026-06-12 | PASS (POAM-0001 closed) |
| §2.4 / §3 HITL | `Eugene-AI/evidence/break/hitl-review-bypass-20260609T182603Z.json` | 2026-06-09 | PASS |
| §2.5 audit trail | `Eugene-AI/evidence/platform-control-check-20260612T045321Z.json` | 2026-06-12 | PASS |
| §2.6 / §3 corpus integrity | `Eugene-AI/evidence/break/corpus-contamination-break-20260609T193306Z.json` | 2026-06-09 | PASS |
| §2.7 pipeline scans | `Eugene-AI/.github/workflows/sca.yml` | 2026-06-10 | PASS |
| §2.8 / §3 deployed platform | `Eugene-AI/evidence/break/platform-deployed-break-20260612T043154Z.json` | 2026-06-12 | PASS |
| live generation (Ollama) | `Eugene-AI/evidence/eugene-helpfulness-eval-ollama-20260612T044252Z.json` | 2026-06-12 | PASS |

---

*Generated in the PROVE phase. Every plain-English claim above is backed by the
raw evidence in Section 6. POAM-0001 is closed in `risk-register.md` and the
slot-5 POA&M registry. Companion night-shift operator handoff: see
`CBBP-PLAN/PROVE/` (pending).*
