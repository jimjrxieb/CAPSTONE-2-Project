# AI Adoption Intake Questionnaire

## Purpose

Use this during COMPLY to assess whether the target client can safely pilot or scale AI usage.

## Business Outcome

- What business problem is AI supposed to solve?
- Why is AI the right tool?
- What workflow is painful today?
- What does success look like in 30, 60, and 90 days?
- What would unacceptable failure look like?

## Current AI Usage

- Which AI tools are already used?
- Which tools are approved?
- Which tools are unapproved but likely in use?
- Which teams are using AI?
- Are personal accounts used for company work?
- Are AI outputs used in production decisions?

## Data Boundary

- What data can AI see?
- What data is prohibited?
- Does the workflow include PII, PHI, secrets, contracts, source code, incident records, or regulated data?
- Is data sent to third-party vendors?
- Is data logged, retained, or used for training?
- Does RAG use sensitive internal documents?

## Tool Authority

- Can AI read files?
- Can AI write files?
- Can AI run commands?
- Can AI call APIs?
- Can AI open PRs?
- Can AI retrieve from vector databases?
- Can AI access production systems?

## Human Review

- What outputs require human review?
- What actions are human-only?
- Who approves high-risk changes?
- How is approval recorded?
- What happens if review is skipped?

## Security Controls

- Are prompts and outputs logged?
- Are AI-assisted PRs labeled?
- Are SAST/SCA/IaC/secrets scans required?
- Are dependencies reviewed?
- Are prompt injection tests run?
- Are RAG poisoning tests run?
- Are vector database boundaries tested?
- Is there an AI incident response plan?

## Evidence

- What artifacts prove the workflow is governed?
- Where are logs stored?
- Where are review notes stored?
- Where are test results stored?
- Who signs off on pilot expansion?

---

## Completed Scoped Intake: MedData Nexus

Use this answer for Capstone 2 lesson work and COMPLY validation.

| Intake Field | Answer |
|---|---|
| System name | MedData Nexus Internal GenAI/RAG Environment |
| Users | Compliance analysts, legal team, clinical administrative staff, IT security, vendor risk/compliance reviewers |
| Data classes | Internal and Confidential documents; Restricted data only with explicit authorization |
| Sensitive examples | policies, compliance evidence, SOC 2 summaries, HIPAA assessment records, vendor-risk documents, legal/BAA templates, security findings, sanitized incident records |
| Prohibited baseline data | PHI/ePHI, real patient identifiers, credentials, secrets, unreviewed vendor free text, poisoned documents, unsanitized incident reports |
| AI tools | Internal RAG chatbot; Eugene local assessment workflow; approved external API path only for approved or sanitized context |
| Highest-risk workflow | RAG retrieval and summarization over sensitive compliance, security, legal, and healthcare privacy documents where output could influence compliance, legal, vendor-risk, or security decisions |
| Top evidence request 1 | Corpus manifest showing approved, excluded, poisoned-test-only, unsafe-test-only, and sanitized files |
| Top evidence request 2 | Retrieval/access-control evidence proving users only retrieve authorized source documents and no PHI/secrets are exposed from the clean baseline |
| Top evidence request 3 | Prompt/output/audit logs showing user query, retrieved chunks, model response, API/tool path, and human review for high-risk outputs |

## Completed Finding Trigger Answer

Create a scope finding if MedData Nexus cannot prove ownership, approved AI use, data boundaries, and pilot/production evidence for the GenAI/RAG environment.

For this intake, a scope finding is triggered if:

- no business, technical, risk, or data owner is named
- PHI/Restricted data boundaries are not documented
- users are using unapproved AI tools outside the registered RAG workflow
- production or pilot use exists without logs, approval records, corpus inventory, or retrieval evidence
- human-only decisions are required by policy but not assigned or recorded
