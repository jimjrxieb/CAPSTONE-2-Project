# AI Adoption At Scale - CBBP Track

## Purpose

This track extends Capstone 2 from a RAG security assessment into a broader AI adoption assessment.

The goal is to prove that I can assess whether a client can scale AI securely, not just whether one chatbot works.

## Consulting Frame

The client question:

> Can we safely scale AI tools across engineering, security, compliance, and business teams?

The CBBP answer:

- COMPLY defines the outcome, data boundary, human authority, and scale criteria.
- BUILD implements the approved workflow and controls.
- BREAK tests whether those controls survive misuse, bypass pressure, and runtime drift.
- PROVE packages the evidence into a scale/no-scale recommendation.

## AI Adoption Maturity Curve

| Stage | AI Usage | Security Maturity | Assessment Focus |
|---|---|---|---|
| Ad Hoc | Unsanctioned public tools and personal accounts | No policy, no visibility | shadow AI discovery |
| Emerging | Department pilots | Basic controls, limited monitoring | approved use and data boundaries |
| Scaling | Cross-functional AI workflows | Defined governance and monitoring | control validation and resilience |
| Mature | AI embedded across the organization | AI lifecycle controls and risk-driven decisions | continuous improvement |

## Capstone 2 Scenario

MedData Nexus wants to use AI in three ways:

1. Internal RAG assistant over compliance, security, healthcare, and vendor documents.
2. AI coding assistants for engineers working on internal applications.
3. AI-assisted security and compliance workflows for analysts.

The assessment must determine:

- what AI is being used
- what data AI can access
- what actions AI can take
- where human approval is required
- what technical controls exist
- how controls are tested
- what evidence supports broader adoption

## COMPLY Deliverables

- AI adoption intake questionnaire
- AI usage inventory
- data classification and AI use matrix
- human decision matrix
- maturity rating
- initial risk register

## BUILD Deliverables

- AI dev assist harness for Codex and Claude Code
- repeatable RAG pipeline build plan
- Eugene assessment API/chatbox build
- approved AI workflow design
- coding assistant guardrail model
- RAG/vector database boundary model
- review gate and CI control model
- logging and evidence design

## BREAK Deliverables

- prompt injection tests
- RAG poisoning tests
- sensitive data misuse test
- AI-assisted PR label bypass test
- auth-sensitive generated code review test
- unsafe dependency suggestion test
- runtime drift test
- human approval bypass test

## PROVE Deliverables

- AI adoption evidence package
- findings report
- executive scale/no-scale recommendation
- 30/60/90-day remediation roadmap

## Interview Language

> Capstone 2 is not only a RAG attack lab. I expanded it into a governed AI adoption assessment. The RAG system is the technical target, but the consulting value is the operating model: identify the adoption stage, define human authority, build controls, break the workflow, and prove whether the client is ready to scale.
