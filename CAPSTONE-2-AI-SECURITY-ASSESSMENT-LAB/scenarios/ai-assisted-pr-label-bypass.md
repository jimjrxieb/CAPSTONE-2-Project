# Scenario: AI-Assisted PR Label Bypass

## Risk

A developer uses an AI coding assistant for a material change but does not label the PR as AI-assisted.

## Why It Matters

Without disclosure, the organization cannot prove which changes were AI-assisted, whether extra review occurred, or whether AI-generated output entered production.

## Expected Control

- PR template asks whether AI materially contributed.
- `ai-assisted` label or equivalent disclosure is required.
- CI or review policy flags missing disclosure.
- Security-sensitive changes require human review.

## BREAK Test

Submit or simulate a PR where:

- the change is AI-assisted
- the PR has no AI-assisted label
- the change touches a meaningful code path

## Evidence To Capture

- PR screenshot or exported metadata
- CI result
- review comment
- policy link
- pass/fail decision

## Finding Trigger

Create a finding if the workflow allows material AI-assisted code to merge without disclosure or review evidence.

