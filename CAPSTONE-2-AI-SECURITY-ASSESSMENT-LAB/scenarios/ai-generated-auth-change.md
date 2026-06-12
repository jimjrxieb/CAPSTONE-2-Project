# Scenario: AI-Generated Authentication Change

## Risk

AI-generated code modifies authentication, authorization, session handling, token handling, or access-control logic without elevated review.

## Why It Matters

Authentication and authorization changes have high blast radius. AI output in these areas must be treated as untrusted until reviewed.

## Expected Control

- CODEOWNERS or review policy requires security review
- tests cover auth behavior
- CI gates run before merge
- reviewer checks for insecure defaults, bypasses, and privilege escalation
- production promotion remains human-only

## BREAK Test

Simulate an AI-assisted change that touches:

- login
- token validation
- session handling
- role checks
- authorization middleware

## Evidence To Capture

- changed files
- reviewer assignment
- test results
- security review note
- merge decision

## Finding Trigger

Create a finding if auth-sensitive AI-generated code can merge without explicit security review.

