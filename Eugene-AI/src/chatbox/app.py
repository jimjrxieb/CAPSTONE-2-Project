"""Gradio chatbox UI. Calls /query. Shows source citations and review warnings."""
from __future__ import annotations

import os

import httpx

API_URL = os.getenv("EUGENE_API_URL", "http://localhost:8000/query")
HEALTH_URL = os.getenv("EUGENE_HEALTH_URL", "http://localhost:8000/health")
REVIEW_URL = os.getenv("EUGENE_REVIEW_URL", "http://localhost:8000/evidence/review-decision")
ROLE_TOKENS = {
    "vendor_risk_reviewer": os.getenv("EUGENE_VENDOR_RISK_TOKEN", os.getenv("VENDOR_RISK_TOKEN", "")),
    "compliance_analyst": os.getenv("EUGENE_COMPLIANCE_ANALYST_TOKEN", os.getenv("COMPLIANCE_ANALYST_TOKEN", "")),
    "it_security": os.getenv("EUGENE_IT_SECURITY_TOKEN", os.getenv("IT_SECURITY_TOKEN", "")),
}
ADVISORY_BANNER = (
    "Advisory output from Eugene (CAP2-AI-001, llama3.2:3b). "
    "Human review is required before any response is used as a finding or deliverable."
)
ROLE_CHOICES = ["vendor_risk_reviewer", "compliance_analyst", "it_security"]
ROLE_DEFINITIONS = {
    "vendor_risk_reviewer": "Reviews vendor-risk records and approved vendor documentation. Restricted from security, HIPAA, incident, legal, and broader compliance corpora.",
    "compliance_analyst": "Reviews policies, compliance records, vendor-risk context, legal templates, and AI governance records. Restricted from security and healthcare-privacy corpora.",
    "it_security": "Reviews all approved baseline corpus categories, including security and healthcare-privacy records. High-risk outputs still require human review.",
}
REVIEW_DECISIONS = ["approve", "reject", "escalate"]


def query_eugene(user_message: str, role: str) -> tuple[str, str, str, str]:
    """Submit a query through the controlled API path and format UI fields."""
    if not role:
        return "Select a role before submitting a query.", "", "Blocked: role required.", ""
    if role not in ROLE_CHOICES:
        return "Selected role is not allowed.", "", "Blocked: invalid role.", ""
    if not user_message or not user_message.strip():
        return "Enter a query before submitting.", "", "Blocked: query required.", ""
    token = ROLE_TOKENS.get(role, "")
    if not token:
        return "Role token is not configured for this chatbox role.", "", "Blocked: role token required.", ""

    try:
        resp = httpx.post(
            API_URL,
            json={"query": user_message.strip(), "session_id": "chatbox"},
            headers={"Authorization": f"Bearer {token}"},
            timeout=60.0,
        )
        resp.raise_for_status()
        data = resp.json()
    except httpx.HTTPStatusError as e:
        return _format_http_error(e), "", "API rejected the request.", ""
    except Exception as e:
        return f"Connection error: {e}", "", "API unavailable.", ""

    response = data.get("response", "")
    sources = data.get("sources", [])
    high_risk = data.get("high_risk", False)
    review_required = data.get("review_required", False)
    audit_id = data.get("audit_id", "")

    status = "Review required before distribution." if review_required else "Advisory draft; standard review still applies."
    if high_risk and not response.startswith("HIGH-RISK OUTPUT"):
        response = f"HIGH-RISK OUTPUT - HUMAN REVIEW REQUIRED BEFORE DISTRIBUTION\n\n{response}"

    return response, _format_sources(sources), status, audit_id


def check_api_health() -> str:
    try:
        resp = httpx.get(HEALTH_URL, timeout=5.0)
        resp.raise_for_status()
    except Exception as e:
        return f"API unavailable: {e}"
    return "API online."


def submit_review(
    audit_id: str,
    reviewer_id: str,
    decision: str,
    rationale: str,
    token: str,
) -> str:
    if not audit_id or not audit_id.strip():
        return "Review blocked: audit ID required."
    if not reviewer_id or not reviewer_id.strip():
        return "Review blocked: reviewer ID required."
    if decision not in REVIEW_DECISIONS:
        return "Review blocked: decision must be approve, reject, or escalate."
    if not rationale or len(rationale.strip()) < 12:
        return "Review blocked: rationale must be at least 12 characters."
    if not token or not token.strip():
        return "Review blocked: IT Security token required."

    try:
        resp = httpx.post(
            REVIEW_URL,
            json={
                "audit_id": audit_id.strip(),
                "reviewer_id": reviewer_id.strip(),
                "decision": decision,
                "rationale": rationale.strip(),
            },
            headers={"Authorization": f"Bearer {token.strip()}"},
            timeout=30.0,
        )
        resp.raise_for_status()
        data = resp.json()
    except httpx.HTTPStatusError as e:
        return _format_http_error(e)
    except Exception as e:
        return f"Review unavailable: {e}"

    review = data.get("review", {})
    return (
        "Review recorded: "
        f"{review.get('decision', decision)} by {review.get('reviewer_id', reviewer_id)} "
        f"for {review.get('audit_id', audit_id)}."
    )


def build_demo():
    import gradio as gr

    with gr.Blocks(title="Eugene - AI Security Assessment Assistant") as demo:
        gr.Markdown(f"# Eugene Assessment Assistant\n\n{ADVISORY_BANNER}")

        with gr.Row():
            role_selector = gr.Dropdown(
                choices=ROLE_CHOICES,
                label="Role",
                value=None,
                allow_custom_value=False,
            )
            health_output = gr.Textbox(label="API Status", value=check_api_health, interactive=False)

        role_definition = gr.Textbox(label="Role Boundary", interactive=False)
        query_input = gr.Textbox(label="Query", placeholder="Ask about the MedData Nexus corpus...", lines=3)

        with gr.Row():
            submit_btn = gr.Button("Submit", variant="primary")
            clear_btn = gr.Button("Clear")

        with gr.Row():
            response_output = gr.Textbox(label="Eugene Response", lines=12, show_copy_button=True)
            sources_output = gr.Markdown(label="Sources")

        with gr.Row():
            status_output = gr.Textbox(label="Review Status", interactive=False)
            audit_output = gr.Textbox(label="Audit ID", interactive=False)

        with gr.Row():
            reviewer_input = gr.Textbox(label="Reviewer ID", placeholder="e.g., sec-reviewer-1")
            decision_input = gr.Dropdown(
                choices=REVIEW_DECISIONS,
                label="Decision",
                value=None,
                allow_custom_value=False,
            )
            token_input = gr.Textbox(label="IT Security Token", type="password")
        rationale_input = gr.Textbox(label="Review Rationale", lines=2)
        review_btn = gr.Button("Record Review")
        review_output = gr.Textbox(label="Review Record Status", interactive=False)

        submit_btn.click(
            fn=query_eugene,
            inputs=[query_input, role_selector],
            outputs=[response_output, sources_output, status_output, audit_output],
        )
        role_selector.change(
            fn=get_role_definition,
            inputs=[role_selector],
            outputs=[role_definition],
        )
        review_btn.click(
            fn=submit_review,
            inputs=[audit_output, reviewer_input, decision_input, rationale_input, token_input],
            outputs=[review_output],
        )
        clear_btn.click(
            fn=lambda: ("", "", "", "", "", "", "", ""),
            inputs=[],
            outputs=[
                query_input,
                response_output,
                sources_output,
                status_output,
                audit_output,
                rationale_input,
                review_output,
                token_input,
            ],
        )
    return demo


def get_role_definition(role: str) -> str:
    if not role:
        return "Select a role to see the retrieval boundary."
    return ROLE_DEFINITIONS.get(role, "Role boundary unavailable.")


def _format_sources(sources: list[dict]) -> str:
    if not sources:
        return "No source chunks returned within the selected role boundary."
    lines = ["**Sources retrieved:**"]
    for source in sources:
        doc_name = source.get("doc_name", "unknown")
        classification = source.get("classification", "unknown")
        chunk_id = source.get("chunk_id", "unknown")
        lines.append(f"- `{doc_name}` | `{classification}` | `{chunk_id}`")
    return "\n".join(lines)


def _format_http_error(error: httpx.HTTPStatusError) -> str:
    try:
        detail = error.response.json().get("detail", error.response.text)
    except Exception:
        detail = error.response.text
    return f"Error {error.response.status_code}: {detail}"


if __name__ == "__main__":
    demo = build_demo()
    server_name = os.getenv("GRADIO_SERVER_NAME", "127.0.0.1")
    server_port = int(os.getenv("GRADIO_SERVER_PORT", "7860"))
    demo.launch(server_name=server_name, server_port=server_port, share=False)
