# Scenario: AI Runtime Drift

## Risk

The documented AI security control does not match the deployed runtime behavior.

## Why It Matters

Policies and architecture diagrams do not secure the system by themselves. Runtime must match the claim.

## Expected Control

- config is versioned
- deployment values match documented controls
- runtime checks validate exposed endpoints, CORS, logging, rate limits, and data boundaries
- drift creates a finding or POA&M item

## BREAK Test

Compare written claims against live behavior.

Examples:

- docs endpoints claimed disabled but return HTTP 200
- CORS policy claims one variable but runtime uses another
- vector DB claimed internal but exposed through route or service
- rate limit claimed but not enforced

## Evidence To Capture

- documented claim
- runtime command/output
- timestamp
- affected control
- remediation path

## Finding Trigger

Create a finding if runtime contradicts the documented security story.

