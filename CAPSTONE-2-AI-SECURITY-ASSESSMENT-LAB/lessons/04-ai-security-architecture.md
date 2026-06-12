# Lesson 04 - AI Security Architecture

**Status: COMPLETE — 2026-06-08**
**Deliverable:** `CBBP-PLAN/COMPLY/meddata-trust-boundaries.md`
**Architecture updated:** `target-architecture/trust-boundaries.md`, `target-architecture/data-flow.md`

## What To Master

AI architecture review is trust-boundary review.

The model is only one part. The real system includes:

- users
- prompts
- system instructions
- retrieved documents
- embeddings
- vector database
- APIs
- tools/plugins
- logs
- vendors
- reviewers
- downstream actions

## Questions I Should Ask

- Where does untrusted input enter?
- Where is sensitive data stored?
- Where are prompts constructed?
- Where does retrieval happen?
- What system instructions are used?
- What tools can the AI call?
- What identity does the AI or agent use?
- What output is trusted by humans or systems?
- What is logged?
- What is not logged?
- Where can the system fail closed?

## Evidence To Request

- architecture diagram
- data flow
- trust boundary map
- prompt construction code
- system prompt/version history
- API route list
- service exposure
- RBAC config
- network policy
- logging configuration

## What I Need To Know

GuidePoint-style review looks for mismatches:

- diagram says internal, runtime exposes it
- policy says review required, PR shows no review
- model refuses direct prompt, but tool action leaks data
- RAG corpus says approved, but ingestion has no owner

## Capstone Practice

Open:

- `target-architecture/architecture-overview.md`
- `target-architecture/data-flow.md`
- `target-architecture/trust-boundaries.md`

Task:

Add or verify these trust boundaries:

- user to RAG app
- RAG app to vector database
- RAG app to model
- model output to user
- AI coding assistant to repo
- human approval to production action

## Finding Trigger

Create a finding if:

- sensitive data crosses an undocumented boundary
- AI has unclear tool authority
- logs cannot reconstruct AI actions
- runtime exposure contradicts the architecture

## CISO Sentence

> The AI workflow crosses sensitive trust boundaries without enough evidence that access, logging, and human approval are consistently enforced.

