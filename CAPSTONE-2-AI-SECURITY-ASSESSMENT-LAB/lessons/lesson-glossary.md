# Lesson Glossary - GuidePoint AI Security And Adoption Track

## Purpose

Use this glossary to build fluency for AI security, AI adoption, agentic development tools, CBBP, RAG security, consulting delivery, and GuidePoint-style interview language.

The goal is not to memorize every term perfectly. The goal is to speak clearly about how AI systems are governed, secured, tested, and proven.

## Core Positioning Terms

**AI Adoption**
: The process of moving AI tools from individual experimentation into approved, repeatable, supported business workflows.

**Governed AI Adoption**
: AI adoption with defined policy, data boundaries, human approval, technical controls, monitoring, and evidence.

**AI Security**
: The practice of securing AI systems, AI-enabled workflows, AI data flows, models, prompts, tools, agents, outputs, and surrounding infrastructure.

**AI Consulting**
: Helping a client understand AI risk, define practical controls, validate those controls, and make evidence-backed decisions about pilot, scale, remediation, or pause.

**AI Adoption Engineer**
: A role focused on helping organizations implement AI workflows safely, effectively, and repeatably.

**AI Security Engineer**
: A role focused on identifying, reducing, testing, and monitoring AI-specific and AI-amplified security risks.

**AI Security Consultant**
: A client-facing advisor who assesses AI systems, explains risk, recommends controls, and produces evidence-backed deliverables.

**Secure AI At Scale**
: AI adoption that can expand across teams while keeping data, tools, access, human approval, monitoring, and evidence under control.

**Client-Ready**
: Written and structured clearly enough that a customer, CISO, engineering leader, or assessor can understand it without repo context.

**GuidePoint-Style Work**
: Practical cybersecurity advisory work that combines technical assessment, customer communication, risk reduction, and defensible evidence.

## CBBP Terms

**CBBP**
: Comply, Build, Break, Prove. A lifecycle for defining rules, implementing controls, testing claims, and packaging evidence.

**COMPLY**
: The phase where humans define scope, business outcome, rules, data boundaries, risk tolerance, approval points, and evidence expectations.

**BUILD**
: The phase where policies and requirements become working controls, code, configs, workflows, CI gates, documentation, and guardrails.

**BREAK**
: The phase where the workflow is intentionally tested against misuse, attack paths, bypasses, runtime drift, weak evidence, and failure modes.

**PROVE**
: The phase where logs, findings, mappings, approvals, scan results, test outputs, and executive summaries are packaged into evidence.

**CBBP Loop**
: The idea that CBBP is repeated: pilot, monitor, break, prove, improve, and scale only when evidence supports scaling.

**Outcome-First COMPLY**
: Starting with the business goal and protected assets before choosing AI tools or technical controls.

**Human Authority**
: The principle that humans own goals, risk acceptance, exceptions, final approval, production decisions, and compliance claims.

**Humans Live In COMPLY**
: Your shorthand for the idea that human judgment belongs at the policy, goal, risk, and approval layer.

**Controlled Failure**
: Failure that is visible, bounded, logged, recoverable, and used to improve the workflow.

**Scale/No-Scale Recommendation**
: A consulting decision that tells leadership whether an AI workflow should expand, remain in pilot, pause, or remediate first.

## Harnessing AI Terms

**Harness**
: The control system around AI tools: roles, prompts, permissions, context, data boundaries, tool access, review gates, tests, logs, and evidence.

**AI Harness**
: A governed workflow that connects human intent, policy, prompts, data, tools, guardrails, approvals, tests, and evidence.

**Harnessing AI**
: Turning AI capability into controlled, useful, evidence-producing work.

**Harnessing AI Dev Tools**
: Organizing Codex, Claude Code, CrewAI-style agents, CI/CD, scanners, and humans into a structured engineering workflow.

**Prompt**
: An instruction, question, task, file, context block, or data input that can influence model output.

**Policy-As-Prompt**
: Turning policy requirements into model instructions, such as refusing secrets or requiring human approval for authentication changes.

**Prompt-Shaped**
: Anything that can steer the model when included in context, including user requests, files, comments, tickets, logs, policies, or retrieved documents.

**Authority Stack**
: The ordered hierarchy of instructions that determines what the AI should follow first.

**Authority Boundary**
: The line between what AI may suggest and what it may decide or execute.

**Context Engineering**
: Designing what information enters the model context, in what order, with what authority, and with what protection.

**Context Boundary**
: The boundary around what the AI can see and treat as relevant context.

**Data Boundary**
: The rules defining what data AI can access, process, retrieve, store, or expose.

**Tool Boundary**
: The rules defining what tools or actions AI can use.

**Human Approval Boundary**
: The point where AI output must stop until a human reviews or approves it.

**Autonomy Budget**
: The allowed level of independence given to an AI system or agent.

**Tool Surface**
: The set of actions available to an AI system, such as reading files, writing files, running commands, opening PRs, calling APIs, or querying databases.

**Evidence-Producing Workflow**
: A workflow designed to create proof as it runs: logs, reviews, tests, approvals, outputs, and decisions.

**Operating Model**
: The full structure of people, process, tools, controls, and evidence that governs how AI is used.

## AI Dev Tool Terms

**Codex**
: An AI coding assistant used to generate, modify, explain, test, and review code inside a controlled workflow.

**Claude Code**
: An AI coding assistant used for agentic software development tasks, code edits, analysis, and workflow automation.

**Cursor**
: An AI-enabled development environment focused on code editing, repo-aware assistance, and developer workflow acceleration.

**Copilot**
: GitHub's AI coding assistant for code completion, chat, and developer productivity workflows.

**Open Code**
: A coding assistant or AI development workflow tool category often discussed alongside Claude Code, Cursor, and Codex.

**Coding Assistant**
: An AI tool that helps write, modify, test, explain, or review code.

**AI-Assisted Code**
: Code where AI materially contributed to design, implementation, tests, review, or documentation.

**AI-Assisted PR**
: A pull request where AI materially helped produce the change.

**AI-Assisted PR Label**
: A label or disclosure showing that AI contributed to a PR.

**CODEOWNERS**
: A repository file that requires specific owners or teams to review changes to certain paths.

**Sensitive Code Path**
: Code that affects authentication, authorization, secrets, cryptography, logging, payments, privacy, infrastructure, or production behavior.

**Auth-Sensitive Change**
: A change touching login, sessions, tokens, roles, permissions, access control, or identity flows.

**Dependency Review**
: Human and automated review of newly added packages for vulnerabilities, license risk, maintainer health, necessity, and supply-chain exposure.

**Secure SDLC**
: Secure Software Development Lifecycle. Development practices that embed security into requirements, design, build, test, release, and maintenance.

**CI/CD**
: Continuous Integration and Continuous Delivery/Deployment. Automated build, test, scan, and release workflows.

**CI Gate**
: A check that must pass before code can merge or deploy.

**Security Gate**
: A required security check such as SAST, SCA, IaC scanning, secret scanning, tests, or approval.

**Exception Process**
: A documented process for approving a temporary bypass, with owner, rationale, expiration, and risk acceptance.

## Agentic AI Terms

**Agent**
: An AI system assigned a goal and often given tools, memory, and steps to complete a task.

**Agentic AI**
: AI systems that can plan, use tools, take multi-step actions, and adapt toward a goal.

**Agentic Workflow**
: A workflow where one or more agents collaborate, use tools, hand off tasks, or iterate toward an outcome.

**CrewAI**
: A framework/pattern for assigning AI agents to specialized roles and tasks, such as researcher, builder, reviewer, tester, and reporter.

**Role-Based Agents**
: Agents designed around a specific function, such as Build Agent, Security Agent, BREAK Agent, or PROVE Agent.

**Tool Calling**
: When an AI system invokes an external tool, API, script, database, scanner, file operation, browser, or command.

**MCP**
: Model Context Protocol. A client/server approach for giving AI tools structured access to external context and capabilities.

**MCP Client**
: The AI tool or application that connects to MCP servers.

**MCP Server**
: A server that exposes tools, resources, or context to an AI client.

**Agent Skill**
: A reusable capability or workflow an agent can invoke.

**Tool Allowlist**
: A list of tools the AI is allowed to use.

**Tool Denylist**
: A list of tools or actions the AI is not allowed to use.

**Least Privilege For Agents**
: Giving agents only the data, tools, and permissions needed for the approved task.

**Excessive Agency**
: Allowing an AI system too much freedom to act without sufficient human approval or control.

**Invisible Lateral Movement**
: Risk where an agent uses legitimate access across systems in ways that bypass traditional segmentation or monitoring.

## Prompt And Context Security Terms

**Prompt Injection**
: Malicious or untrusted instructions attempt to override the intended task or policy.

**Direct Prompt Injection**
: A user directly tells the AI to ignore rules, reveal hidden instructions, leak data, or perform unsafe actions.

**Indirect Prompt Injection**
: Malicious instructions enter through files, webpages, comments, documents, logs, tickets, emails, or retrieved RAG content.

**Jailbreak**
: An attempt to bypass safety instructions or policy limits.

**System Prompt Disclosure**
: Attempting to make the model reveal hidden system or developer instructions.

**Instruction Override**
: Attempting to replace the intended instructions with attacker-controlled instructions.

**Malicious Source Comment**
: A code comment or docstring that tries to instruct the AI to behave unsafely.

**Untrusted Context**
: Context the AI can read but should not treat as authority.

**Context Poisoning**
: Introducing misleading or malicious content into the model's working context.

**Prompt-To-Tool Injection**
: Prompt injection that causes the AI to misuse a tool or call a tool with unsafe inputs.

**Output Trust Boundary**
: The point where AI output becomes trusted by a human, system, report, or downstream workflow.

**Output Validation**
: Checking AI output before using it, displaying it, storing it, or acting on it.

**Input Validation**
: Checking user input, prompts, files, or retrieved content before sending it to the model.

## RAG Terms

**RAG**
: Retrieval-Augmented Generation. A pattern where a system retrieves documents or data and passes them to a model as context.

**RAG Assistant**
: An AI assistant that answers using retrieved documents.

**Corpus**
: The document collection used by a RAG system.

**Corpus Manifest**
: A record of documents in the corpus, including source, owner, sensitivity, version, and hash where possible.

**Ingestion**
: The process of loading documents into a RAG pipeline.

**Chunking**
: Breaking documents into smaller pieces for embedding and retrieval.

**Embedding**
: A numeric representation of text used for similarity search.

**Vector Database**
: A database that stores embeddings and supports similarity search.

**ChromaDB**
: A vector database often used in local or prototype RAG systems.

**Retrieval**
: Finding relevant chunks or documents for a user query.

**Retrieval Filtering**
: Restricting retrieval results based on metadata, user role, document sensitivity, or access rules.

**Metadata**
: Information about documents or chunks, such as owner, classification, source, date, access group, or document type.

**Source Leakage**
: When a RAG system exposes internal source content or metadata that should not be disclosed.

**Unauthorized Retrieval**
: Retrieving content the user should not be allowed to access.

**RAG Poisoning**
: Adding malicious, misleading, or unauthorized content to the corpus so retrieval steers the model incorrectly.

**Poisoned Document**
: A document containing malicious or misleading instructions, data, or content.

**Secrets In Corpus**
: API keys, tokens, passwords, credentials, PHI, PII, or other sensitive data included in the RAG corpus.

**Citation Validation**
: Checking whether AI citations or references actually support the generated answer.

**Grounded Answer**
: An answer based on approved retrieved context rather than unsupported model generation.

**Hallucination**
: A model output that is false, unsupported, invented, or not grounded in evidence.

## Security Control Terms

**Guardrail**
: A policy, technical control, workflow rule, review gate, prompt instruction, or test that constrains AI behavior.

**Control**
: A safeguard or countermeasure designed to reduce risk.

**Preventive Control**
: A control that stops bad actions before they happen.

**Detective Control**
: A control that identifies bad actions or abnormal behavior.

**Corrective Control**
: A control that helps recover or remediate after an issue.

**Compensating Control**
: An alternate control used when the preferred control is not available.

**Access Control**
: Rules and enforcement around who or what can access data, systems, tools, or actions.

**RBAC**
: Role-Based Access Control. Permissions based on user or system role.

**SSO**
: Single Sign-On. Centralized authentication for users.

**DLP**
: Data Loss Prevention. Controls that detect or block sensitive data exposure.

**Secret Scanning**
: Searching for exposed credentials, tokens, keys, or passwords.

**SAST**
: Static Application Security Testing. Scanning source code for vulnerabilities.

**SCA**
: Software Composition Analysis. Scanning dependencies for vulnerabilities, license risk, and supply-chain issues.

**IaC Scanning**
: Infrastructure-as-Code scanning for insecure cloud, Kubernetes, Terraform, CloudFormation, or OpenTofu configurations.

**Container Scanning**
: Scanning container images for vulnerabilities or insecure configuration.

**Policy-As-Code**
: Encoding policy rules in machine-enforceable form, often for CI/CD, infrastructure, or admission control.

**Rego**
: Policy language used by Open Policy Agent.

**Cedar**
: Policy language associated with fine-grained authorization and policy-based access control.

**Network Boundary**
: The boundary controlling which systems can communicate.

**ClusterIP**
: Kubernetes service type that exposes a service only inside the cluster.

**HTTPRoute**
: Kubernetes Gateway API resource that routes HTTP traffic.

**Runtime Drift**
: When deployed behavior differs from documented, expected, or version-controlled configuration.

**Configuration Drift**
: When actual configuration changes or diverges from the intended baseline.

**Rate Limiting**
: Restricting the number of requests over time to reduce abuse or overload.

**HTTP 429**
: HTTP status code meaning too many requests.

## Evidence And Audit Terms

**Evidence**
: Artifacts that prove what was built, tested, reviewed, approved, or observed.

**Evidence Package**
: A structured set of logs, screenshots, configs, reports, mappings, findings, and approvals.

**Audit Trail**
: Records showing who did what, when, with what system, and under what approval.

**Review Evidence**
: Proof that a human reviewed or approved a change, finding, exception, or decision.

**Runtime Evidence**
: Evidence from the live system, such as command output, API response, logs, or deployed config.

**Design Evidence**
: Evidence showing intended architecture, policy, or configuration.

**Claim-To-Proof Link**
: The connection between what the report says and the artifact proving it.

**Finding**
: A documented security weakness, control gap, risk, or evidence failure.

**Finding Trigger**
: A condition that means a finding should be created.

**Remediation**
: The action needed to fix or reduce a finding.

**Validation**
: Testing that a remediation or control actually works.

**POA&M**
: Plan of Action and Milestones. A tracked remediation plan for a weakness or gap.

**Risk Register**
: A structured list of risks, severity, owners, status, and remediation.

**Executive Summary**
: A concise leadership-level explanation of scope, key risks, business impact, and recommended action.

**Remediation Roadmap**
: A prioritized plan of fixes, often organized into 30/60/90-day actions.

**CISO Sentence**
: A one-sentence business explanation of the risk without relying on framework acronyms.

## AI Governance Terms

**AI Governance**
: The policies, roles, processes, controls, and oversight used to manage AI risk and value.

**AI Policy**
: Rules for approved AI use, prohibited data, approved tools, review requirements, and accountability.

**Acceptable Use Policy**
: A policy defining what users may and may not do with AI tools.

**AI Inventory**
: A record of AI systems, tools, models, vendors, use cases, owners, data, and risk level.

**Model Inventory**
: A record of models used by an organization, including provider, version, use case, owner, and approval status.

**System Card**
: Documentation describing an AI system's purpose, design, limitations, risks, and expected use.

**Model Card**
: Documentation describing a model's intended use, training/evaluation context, limitations, and risk considerations.

**Dataset Card**
: Documentation describing a dataset's source, contents, licensing, sensitivity, and intended use.

**Data Lineage**
: The record of where data came from, how it changed, and where it is used.

**Data Classification**
: Categorizing data by sensitivity, such as public, internal, confidential, restricted, PII, PHI, CUI, or secrets.

**Risk Appetite**
: The amount and type of risk leadership is willing to accept.

**Residual Risk**
: Risk remaining after controls are applied.

**Risk Acceptance**
: Formal approval to accept residual risk.

**RACI**
: Responsible, Accountable, Consulted, Informed. A responsibility matrix.

**HITL**
: Human-In-The-Loop. A required human review or approval before action.

**Human-On-The-Loop**
: Human supervision over an automated process, with ability to intervene.

**Shadow AI**
: Unapproved or unmanaged AI tool use within an organization.

**Pilot**
: A limited AI rollout used to learn and validate controls before scaling.

**Conditional Scale**
: Expanding AI use only after specific controls, monitoring, or remediation steps are complete.

## Framework And Mapping Terms

**NIST AI RMF**
: NIST Artificial Intelligence Risk Management Framework. Organizes AI risk work around GOVERN, MAP, MEASURE, and MANAGE.

**GOVERN**
: NIST AI RMF function focused on policy, accountability, roles, risk management culture, and oversight.

**MAP**
: NIST AI RMF function focused on context, intended use, stakeholders, impacts, and risks.

**MEASURE**
: NIST AI RMF function focused on evaluating, testing, monitoring, and measuring trustworthy AI characteristics.

**MANAGE**
: NIST AI RMF function focused on risk treatment, response, prioritization, and continuous improvement.

**NIST AI 600-1**
: NIST guidance focused on generative AI risks and risk management actions.

**NIST SP 800-53**
: Security and privacy controls for federal information systems and organizations.

**OWASP LLM Top 10**
: A list of common security risks for LLM applications.

**MITRE ATLAS**
: A knowledge base of adversary tactics and techniques against AI-enabled systems.

**MITRE ATT&CK**
: A knowledge base of adversary tactics and techniques for enterprise cyber attacks.

**FedRAMP**
: Federal Risk and Authorization Management Program for cloud services.

**SOC 2**
: A reporting framework around trust services criteria such as security, availability, processing integrity, confidentiality, and privacy.

**CMMC**
: Cybersecurity Maturity Model Certification for defense industrial base requirements.

**Control Mapping**
: Connecting findings or controls to frameworks such as NIST AI RMF, NIST 800-53, OWASP LLM, or MITRE ATLAS.

**Framework Citation**
: A reference to a framework item. Useful for organization, but not proof by itself.

## Attack And Risk Terms

**Attack Surface**
: All the ways a system can be attacked.

**AI Attack Surface**
: The AI-specific and AI-amplified ways a system can be attacked, including prompts, context, tools, agents, data, vendors, models, and outputs.

**Threat Model**
: A structured analysis of assets, actors, entry points, trust boundaries, failure modes, controls, and evidence.

**Threat Actor**
: A person, group, insider, outsider, or automated system that can cause harm.

**Abuse Case**
: A scenario describing how a system could be misused.

**Misuse Case**
: Similar to abuse case; describes unintended or malicious use.

**Blast Radius**
: The scope of impact if a failure or compromise occurs.

**Data Leakage**
: Sensitive data exposed to an unauthorized person, system, model, log, or output.

**Model Extraction**
: Attempting to replicate or steal a model's behavior, weights, or proprietary functionality.

**Model Inversion**
: Attempting to infer sensitive training data from model behavior.

**Data Poisoning**
: Introducing bad data into training, fine-tuning, evaluation, or retrieval sources.

**Model Poisoning**
: Manipulating a model through poisoned training or update processes.

**Supply-Chain Risk**
: Risk introduced by vendors, dependencies, models, datasets, plugins, tools, or external services.

**Unsafe Dependency**
: A package that is vulnerable, unmaintained, typo-squatted, unnecessary, or risky.

**Overtrust**
: Treating AI output as more reliable or authoritative than it is.

**Unknown Unknowns**
: Risks that are not fully known or predictable before deployment.

**Near Miss**
: An event that almost caused harm and should become evidence for improvement.

## Cloud And Vendor AI Terms

**SaaS AI**
: AI provided as a cloud service or subscription.

**Managed AI Service**
: Cloud-provider AI platform or model service.

**OpenAI**
: AI model and API provider.

**Azure OpenAI**
: Microsoft Azure service providing OpenAI models with Azure enterprise controls.

**AWS Bedrock**
: AWS managed service for accessing and building with foundation models.

**AWS SageMaker**
: AWS platform for machine learning development, training, deployment, and operations.

**Azure AI Foundry**
: Azure platform for building, deploying, and managing AI applications and agents.

**Google Vertex AI**
: Google Cloud's managed AI and ML platform.

**Vendor Review**
: Assessing a vendor's security, privacy, terms, controls, compliance, and risk.

**Inherited Control**
: A control provided partly or fully by a vendor or platform.

**Tenant Boundary**
: Isolation boundary between customers or environments in a cloud service.

**Data Retention**
: How long data is stored by a system or vendor.

**Training Use**
: Whether customer inputs or outputs may be used to train or improve models.

## Consulting Delivery Terms

**Assessment**
: Structured review of a system, workflow, or program against risk, controls, and evidence.

**Advisory**
: Guidance that helps a client make decisions and improve security posture.

**Stakeholder**
: Anyone affected by or responsible for the AI system, including engineering, security, legal, compliance, business owners, and users.

**Scope**
: The boundaries of what is being assessed.

**Out Of Scope**
: What is explicitly not being assessed.

**Assumption**
: Something treated as true for the assessment, but not fully verified.

**Limitation**
: A constraint on the assessment, such as missing access, time, evidence, or tooling.

**Customer Deliverable**
: A report, roadmap, evidence package, briefing, or artifact handed to the client.

**Readout**
: A meeting or presentation explaining assessment results.

**Executive Briefing**
: A leadership-level summary of findings, business impact, and recommended action.

**Remediation Priority**
: The order in which fixes should be completed based on risk and business impact.

**30/60/90-Day Roadmap**
: A remediation plan split into near-term, mid-term, and longer-term actions.

**Trusted Advisor**
: A consultant who gives practical, honest, evidence-backed guidance.

## Interview Language Terms

**Strong Answer Shape**
: A structured answer that names the problem, evidence, risk, remediation, and business impact.

**Weak Answer**
: An answer that overclaims, hides limitations, relies only on tools, or uses framework acronyms without explaining the business risk.

**Transferable Procedure**
: The part of a lab that applies to real client work, even if the exact system differs.

**Honest Limitation**
: A clear statement about what the lab, evidence, or assessment does not prove.

**Business Impact**
: How a technical weakness affects confidentiality, integrity, availability, compliance, customer trust, cost, operations, or delivery.

**Engineering Sentence**
: A concise explanation of what engineers need to fix.

**Security Sentence**
: A concise explanation of the control gap and risk.

**Leadership Sentence**
: A concise explanation of impact, priority, and decision.

## Daily Fluency Drills

Use these prompts until the language is automatic.

1. A prompt asks the AI to behave, but a harness...
2. Harnessing AI dev tools as an engineering team means...
3. A GuidePoint client does not need AI hype. They need...
4. The difference between policy and evidence is...
5. Runtime drift matters because...
6. Human review is only a control if...
7. RAG security is really about...
8. Prompt injection matters because...
9. AI coding assistants become risky when...
10. Scaling without evidence is...

## Best Short Answers

**What is harnessing AI?**

Harnessing AI means designing the operating system around the model: roles, context, permissions, review gates, tests, logs, and evidence.

**What is an AI harness?**

An AI harness is the governed workflow that controls what AI can see, do, influence, and prove.

**What is the difference between a prompt and a harness?**

A prompt tells AI what to do. A harness controls the workflow around the AI so the work is bounded, reviewed, tested, and evidenced.

**What is the value of CBBP?**

CBBP gives AI adoption a repeatable lifecycle: define the rules, build the controls, break the claims, and prove the result.

**What is the GuidePoint-style value?**

Helping clients safely adopt AI by assessing risk, validating controls, explaining business impact, and producing evidence-backed recommendations.

