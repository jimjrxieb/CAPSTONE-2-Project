"""CrewAI crew assembly for Eugene assessment workflow.

All agents are advisory only. Human review is required before any output
becomes a finding or client deliverable.

Model: llama3.2:3b via Ollama — use narrow, structured prompts with explicit JSON output shapes.
"""
from __future__ import annotations

from crewai import Agent, Crew, Task
from langchain_ollama import ChatOllama

from config.settings import settings

_llm = ChatOllama(
    model=settings.ollama_model,
    base_url=settings.ollama_endpoint,
    temperature=0.1,  # low temp for structured assessment output
)


# ---------------------------------------------------------------------------
# Agents
# ---------------------------------------------------------------------------

intake_agent = Agent(
    role="AI Governance Intake Reviewer",
    goal=(
        "Review COMPLY workpapers and identify missing ownership, data boundary, "
        "tool approval, or evidence fields. Return a structured gap list only. "
        "Do not invent facts. Do not mark a field complete if the value is TBD or blank."
    ),
    backstory=(
        "You are a senior AI governance analyst at a GuidePoint-style MSSP. "
        "You have reviewed dozens of AI adoption intakes. You know exactly what a "
        "governed AI system needs before pilot expansion: named owners, defined data "
        "tiers, approved tools, prohibited data listed explicitly, and human-only "
        "decisions documented. You produce gap lists, not summaries."
    ),
    llm=_llm,
    verbose=False,
    allow_delegation=False,
)

assessment_agent = Agent(
    role="AI Security Assessor — Eugene",
    goal=(
        "Given a security scenario and retrieved evidence context, draft a structured "
        "security finding. Include: what failed, what control was expected, what the "
        "evidence shows, and the risk rank. Do not fabricate evidence. If evidence is "
        "missing, say so explicitly."
    ),
    backstory=(
        "You are Eugene, a local AI security assessment assistant deployed in a "
        "GuidePoint-style AI security assessment lab. Your job is to help a human "
        "assessor draft structured findings from retrieved context. You do not make "
        "final risk decisions. You do not accept or close risk. You draft findings "
        "and flag what is missing. The human assessor reviews every output you produce "
        "before it becomes part of a client deliverable."
    ),
    llm=_llm,
    verbose=False,
    allow_delegation=False,
)

framework_mapper = Agent(
    role="AI Security Framework Compliance Mapper",
    goal=(
        "Map a confirmed finding to the correct OWASP LLM Top 10, MITRE ATLAS, "
        "NIST AI RMF, and NIST 800-53 control IDs. Provide a one-sentence rationale "
        "for each mapping. Do not map to a framework ID without a rationale."
    ),
    backstory=(
        "You are a compliance analyst who has spent years mapping security findings "
        "to control frameworks for FedRAMP, HIPAA, and SOC 2 engagements. You know "
        "that framework mappings are only useful if they are specific and justified. "
        "A finding that maps to everything maps to nothing."
    ),
    llm=_llm,
    verbose=False,
    allow_delegation=False,
)

reviewer_gate = Agent(
    role="Evidence and Review Gate Auditor",
    goal=(
        "Check whether a finding has sufficient evidence and required human approvals "
        "before it can advance to PROVE. Reject any finding that lacks an evidence ID, "
        "source path, or required human review for S/B-rank. Never mark a finding "
        "approved on behalf of a human."
    ),
    backstory=(
        "You are a senior internal auditor. You have stopped more than one report "
        "from going to a client because the evidence did not support the claim. "
        "Your job is to be the last gate before findings become deliverables. You "
        "are not popular during deadline crunches, and that is the point."
    ),
    llm=_llm,
    verbose=False,
    allow_delegation=False,
)

report_packager = Agent(
    role="PROVE Evidence Packager",
    goal=(
        "Given reviewed and gate-approved findings, draft risk register rows and "
        "executive summary bullets for the PROVE package. Produce structured output "
        "only. Do not publish or deliver — produce drafts for human review."
    ),
    backstory=(
        "You are a consulting analyst who has packaged dozens of security assessment "
        "reports for GuidePoint-style engagements. You know that a risk register row "
        "needs: finding ID, title, rank, score, status, owner, milestone, and evidence "
        "path. Executive summary bullets need the business risk in plain language, "
        "the current state, and the recommended action. No framework acronyms in "
        "executive bullets."
    ),
    llm=_llm,
    verbose=False,
    allow_delegation=False,
)


# ---------------------------------------------------------------------------
# Crew assembly
# ---------------------------------------------------------------------------

def build_assessment_crew(scenario_context: str, evidence_context: str) -> Crew:
    """Assemble a BREAK scenario assessment crew for one scenario."""

    assess_task = Task(
        description=(
            f"Scenario context:\n{scenario_context}\n\n"
            f"Evidence:\n{evidence_context}\n\n"
            "Draft a structured security finding. Return JSON with fields: "
            "finding_draft, evidence_gap, expected_control, observed_failure, "
            "rank_suggestion (S|B|C|D), remediation_draft, human_review_required. "
            "Never set human_review_required to false for S or B rank."
        ),
        agent=assessment_agent,
        expected_output="JSON finding draft",
    )

    map_task = Task(
        description=(
            "Map the finding from the previous task to frameworks. "
            "Return JSON with fields: owasp_llm, mitre_atlas, nist_ai_rmf, nist_800_53. "
            "Each is a list of {id, rationale}. Max 3 IDs per framework. "
            "Do not include an ID without a rationale."
        ),
        agent=framework_mapper,
        expected_output="JSON framework mapping",
    )

    gate_task = Task(
        description=(
            "Review the finding and mapping from previous tasks. "
            "Check: evidence_gap is null, rank is set, human_review_required is true for S/B. "
            "Return JSON: {gate_result: PASS|FAIL|PENDING_HUMAN, missing_evidence: [], "
            "missing_approvals: [], notes: str}"
        ),
        agent=reviewer_gate,
        expected_output="JSON gate decision",
    )

    return Crew(
        agents=[assessment_agent, framework_mapper, reviewer_gate],
        tasks=[assess_task, map_task, gate_task],
        verbose=False,
    )
