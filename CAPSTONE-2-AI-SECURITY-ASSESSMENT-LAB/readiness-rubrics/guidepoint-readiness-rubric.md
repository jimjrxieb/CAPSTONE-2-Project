# GuidePoint Readiness Rubric

Use this rubric to decide whether Capstone 2 is job-ready.

Scoring:

- 0 = not started
- 1 = notes only
- 2 = working draft
- 3 = demo-ready
- 4 = interview-ready
- 5 = client-ready

## 1. AI Security Architecture

| Item | Score | Evidence |
|---|---:|---|
| Architecture overview explains the RAG chatbot and Eugene assessment flow | 0 | `target-architecture/architecture-overview.md` |
| Data flow shows documents, embeddings, retrieval, model call, output, and logs | 0 | `target-architecture/data-flow.md` |
| Trust boundaries are clearly identified | 0 | `target-architecture/trust-boundaries.md` |
| Sensitive data paths are documented | 0 | `target-architecture/data-flow.md` |
| Human approval points are documented | 0 | `target-architecture/trust-boundaries.md` |

Target: 4+ average.

## 2. RAG Security Assessment

| Item | Score | Evidence |
|---|---:|---|
| RAG ingestion risks are documented | 0 | `scenarios/` |
| Vector DB access-control risks are documented | 0 | `scenarios/rag-vector-db-access-gap.md` |
| Retrieval filtering and metadata risks are documented | 0 | `target-architecture/data-flow.md` |
| Source leakage test exists | 0 | `scenarios/rag-source-leakage.md` |
| Unauthorized retrieval test exists | 0 | `scenarios/rag-unauthorized-retrieval.md` |

Target: 4+ average.

## 3. AI Red Team Scenarios

| Scenario | Score | Required Output |
|---|---:|---|
| Direct prompt injection | 0 | finding + mapping + remediation |
| Poisoned RAG document | 0 | finding + mapping + remediation |
| Source leakage | 0 | finding + mapping + remediation |
| Unauthorized retrieval | 0 | finding + mapping + remediation |
| Secrets in corpus | 0 | finding + mapping + remediation |
| Vector DB access gap | 0 | finding + mapping + remediation |
| Missing output filtering | 0 | finding + mapping + remediation |
| Missing audit logging | 0 | finding + mapping + remediation |

Target: all scenarios 3+, at least four scenarios 4+.

## 4. Framework Mapping

| Item | Score | Evidence |
|---|---:|---|
| OWASP LLM Top 10 mapping exists | 0 | `CBBP-PLAN/PROVE/owasp-llm-map.md` |
| MITRE ATLAS mapping exists | 0 | `CBBP-PLAN/PROVE/mitre-atlas-map.md` |
| NIST AI RMF mapping exists | 0 | `CBBP-PLAN/PROVE/nist-ai-rmf-map.md` |
| NIST 800-53 mapping exists | 0 | `CBBP-PLAN/PROVE/nist-800-53-map.md` |
| Each finding has at least one framework citation | 0 | `deliverables/02-client-findings-report.md` |

Target: 4+ average.

## 5. Eugene Model Usage

| Item | Score | Evidence |
|---|---:|---|
| Eugene model is used as the assessment brain | 0 | API output / evidence |
| Model version is recorded | 0 | `evidence/` |
| Prompt/system instructions are documented | 0 | `evidence/` |
| Inference outputs are captured | 0 | `evidence/` |
| Limitations and HITL needs are documented | 0 | `STATUS.md` |

Target: 4+ average.

## 6. CrewAI And n8n

| Item | Score | Evidence |
|---|---:|---|
| CrewAI workflow plan exists | 0 | `workflows/crewai/README.md` |
| CrewAI roles are defined | 0 | `workflows/crewai/README.md` |
| n8n workflow plan exists | 0 | `workflows/n8n/README.md` |
| n8n intake/approval flow is documented | 0 | `workflows/n8n/README.md` |
| Security controls for workflow credentials/logging are documented | 0 | `workflows/n8n/README.md` |

Target: 3+ first, then 4+.

## 7. Client Deliverables

| Deliverable | Score | Evidence |
|---|---:|---|
| Risk register | 0 | `CBBP-PLAN/PROVE/risk-register.md` |
| Findings report | 0 | `deliverables/02-client-findings-report.md` |
| Executive summary | 0 | `deliverables/01-executive-summary.md` |
| Remediation roadmap | 0 | `deliverables/03-remediation-roadmap.md` |
| Evidence folder has repeatable outputs | 0 | `evidence/` |

Target: all 4+ before calling the capstone interview-ready.

## 8. Interview Readiness

Practice until these answers are clean:

- What did you build?
- Why did you use Eugene?
- What is the AI attack surface?
- How did you threat model the RAG system?
- What did prompt injection prove?
- What did poisoned retrieval prove?
- How did you map findings to OWASP LLM and MITRE ATLAS?
- How did you map findings to NIST AI RMF and NIST 800-53?
- What would you tell a CISO?
- What would you fix first?

Then practice the first completed scenario until the business explanation, technical evidence, and remediation answer are clear without notes.

The first interview-ready slice must defend:

- why Eugene was used despite model limitations
- why a self-built RAG attack transfers to client assessment work
- what the finding means in one CISO-ready sentence
- what evidence proves the finding happened
- what remediation and validation would close the issue

## Pass Criteria

Capstone 2 is GuidePoint-ready when:

- Architecture score average is 4+.
- RAG security score average is 4+.
- All eight scenarios have findings and remediation.
- All four framework maps exist.
- Eugene model usage is evidenced.
- Client findings report is readable without repo context.
- Executive summary is under one page and business-focused.
- Remediation roadmap has 30/60/90-day actions.
- At least one scenario passes the Constant pressure test at 4+ before expanding to all eight.
- You can explain the project in two minutes without notes.

## Two-Minute Capstone Pitch

> Capstone 2 is my applied AI security assessment lab. I built Eugene as the dedicated assessment assistant for a repeatable RAG security workflow over synthetic healthcare SaaS documents. I tested AI-specific risks like prompt injection, poisoned retrieval, source leakage, unauthorized retrieval, secrets in the corpus, missing output filtering, vector DB access gaps, and missing audit logging. Then I mapped the findings to OWASP LLM Top 10, MITRE ATLAS, NIST AI RMF, and NIST 800-53. The output is a client-style findings report, risk register, remediation roadmap, and executive summary. The point is to show I can build, assess, break, govern, and explain GenAI systems.
