# Lesson 02 - Client Intake And Scope

**Status: COMPLETE — 2026-06-08**
**Deliverable:** `CBBP-PLAN/COMPLY/meddata-ai-adoption-intake.md`

## What To Master

Good AI security work starts before testing.

The first job is to define scope:

- what system is being assessed
- what business outcome matters
- what data is involved
- who uses it
- what AI can do
- what evidence exists
- what is out of scope

## Questions I Should Ask

- What AI use case are we assessing?
- Is this an experiment, pilot, production workflow, or scaled program?
- Who are the users?
- What model or vendor is used?
- Is this SaaS AI, local AI, cloud AI, RAG, fine-tuning, or agentic automation?
- What data enters the system?
- What data leaves the system?
- Are prompts, outputs, retrieved documents, and tool calls logged?
- What compliance obligations apply?
- What is the client's biggest concern: speed, privacy, security, compliance, reliability, or cost?

## Evidence To Request

- architecture diagram
- data flow diagram
- AI inventory
- approved tool list
- acceptable use policy
- vendor review
- model/system card
- RAG corpus manifest
- access-control matrix
- logging samples
- incident response plan
- prior test results

## What I Need To Know

Scope prevents two mistakes:

- testing random things that do not matter
- making claims broader than the evidence supports

GuidePoint-style language:

> Based on the evidence reviewed, this assessment covers the defined AI workflow and should not be interpreted as a full enterprise AI program certification.

## Capstone Practice

Open:

- `templates/ai-adoption-intake-questionnaire.md`
- `templates/ai-risk-assessment.md`
- `target-client/meddata-nexus-health-systems.md`

Task:

Fill in a scoped intake for MedData Nexus:

  **System name:**
  MedData Nexus Internal GenAI/RAG Environment

  **Users:**
  Compliance analysts, legal team, clinical administrative staff, IT security, and
  vendor risk/compliance reviewers.

  **Data classes:**
  Internal and Confidential classification documents approved for baseline RAG ingestion:
  policies, compliance evidence, SOC 2 summaries, HIPAA assessment records, vendor risk
  documents, legal/BAA templates, security findings, sanitized incident records.
  PHI/ePHI, real patient identifiers, credentials, and secrets are explicitly prohibited
  from the baseline corpus. Restricted data requires explicit CISO authorization before
  inclusion.

  **AI tools:**
  Internal RAG chatbot (pilot authorization only). Eugene — assessment workflow tool,
  advisory only. External LLM API (approved path, sanitized context only) — requires
  CISO authorization for any Restricted-tier data.

  **Highest-risk workflow:**
  RAG retrieval and summarization over sensitive compliance, legal, and healthcare privacy
  documents where the output could influence a compliance decision, legal interpretation,
  or vendor risk conclusion without human review. Specific failure modes: unauthorized
  retrieval across user roles, PHI or secrets surfaced from the corpus, poisoned document
  instructions followed by the model, or AI-generated summaries distributed as authoritative
  conclusions without a recorded human approval.

  **Top three evidence requests:**
  1. Corpus manifest — which documents are approved for baseline ingestion, which are
     excluded, and which exist for adversarial testing only. Signed by named data owners
     per document category.
  2. Retrieval and access-control evidence — golden-question retrieval output proving
     users receive only authorized documents and that no PHI, secrets, or Restricted-tier
     content is returned from the clean baseline corpus.
  3. Prompt/output/audit trail — structured log showing user query, retrieved chunk IDs,
     source document references, model response, API/tool path used, and human review
     decision with reviewer identity for any high-risk output.

## Finding Trigger

Create a scope finding if:

- no owner exists 
- the data boundary is unclear
- AI tool usage is unknown
- production use exists but evidence is missing

## CISO Sentence

> The organization is using AI before it can clearly show what data the system touches, who owns the workflow, and what evidence proves the controls are operating.

