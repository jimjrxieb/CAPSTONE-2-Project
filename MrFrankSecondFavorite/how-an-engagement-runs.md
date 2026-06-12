# How an AI Security Engagement Runs

One page. How a consulting process maps to a repeatable, evidence-first delivery method.

---

## The map

A solid engagement usually runs through four stages. This framework gives each stage a clear job, an owner, and a deliverable — so the engagement produces evidence, not just notes.

```
  Engagement              This framework         The client gets
  ──────────────          ──────────────         ───────────────

  1. DISCOVERY     ───►    COMPLY                 Scope + gap analysis
     "Understand the              "What should be         (where you are vs.
      current system"              true? Where are         where you need to be)
                                   we today?"

  2. STRATEGY      ───►    COMPLY → BUILD         Roadmap
     "Craft a tailored            "Decide what to          (prioritized fixes,
      roadmap"                     build, in what           with owners + dates)
                                   order"

  3. IMPLEMENTATION───►    BUILD                  Working controls
     "Execute with                "Make it true,           (IaC, policy, CI gates,
      precision"                   by design"               hardening — built + documented)

  4. OPTIMIZATION  ───►    BREAK → PROVE          Proof it works + report
     "Continuous                  "Prove it stays          (validation results,
      monitoring &                 true, then show          evidence package,
      refinement"                  stakeholders"            exec summary, roadmap)
```

---

## The one idea that makes it different

Most consulting goes **Discovery → Strategy → Implementation → Report.** It reports on what was *built*.

This framework inserts a validation step before the report:

> **A control can be fully compliant and still ineffective until it has been validated.**

So before the client gets a report, the controls get *tested* — prompt-injection attempts against the AI feature, a check that the NetworkPolicy actually blocks traffic, a verification that the CI gate actually fails a bad PR. The report then says "tested and working," not "configured and assumed."

That's the difference between a deliverable a client trusts and one they file away.

---

## What each stage produces (the deliverables)

| Stage | Deliverable | Audience |
|---|---|---|
| Discovery | Intake summary + gap analysis | Client lead — "here's where you stand" |
| Strategy | Prioritized remediation roadmap | Client lead — "here's the plan, in order, with dates" |
| Implementation | Built controls + implementation notes | Client engineers — "here's what changed and why" |
| Optimization (validate) | Validation findings | Engineers — "here's what passed, what didn't" |
| Optimization (report) | 1-page exec summary + evidence package + POA&M | Founder / CISO / auditor — "here's the risk, the proof, and the open items" |

The exec summary is always **one page, risk-first, business framing** — what a founder or CISO actually reads. The detailed evidence sits behind it for engineers and auditors.

---

## Why this capstone matters

The boring, repeatable parts of an engagement — the intake questions, the gap analysis structure, the build checklist, the validation checklist, the report template — came out of the Eugene capstone. That matters because the framework was not invented in a vacuum. It was built while actually scoping, building, testing, and documenting an AI/RAG security lab.

Start with **[capstone-as-engagement.md](capstone-as-engagement.md)** for the real run-through.
