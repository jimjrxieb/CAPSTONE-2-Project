# Scenario: AI Unsafe Dependency Suggestion

## Risk

An AI coding assistant suggests adding a new package that is vulnerable, unmaintained, typo-squatted, over-permissioned, or unnecessary.

## Why It Matters

AI can create software supply-chain risk by making dependency additions feel routine.

## Expected Control

- new dependencies require justification
- dependency is pinned
- SCA scan runs
- license check runs
- maintainer/release health is reviewed
- reviewer verifies whether existing code or standard library can solve the problem

## BREAK Test

Simulate an AI-generated change that adds a questionable dependency.

Ask:

- Did CI detect known vulnerabilities?
- Did review require justification?
- Did the dependency get approved by a human?
- Was the risk documented?

## Evidence To Capture

- generated diff
- dependency manifest change
- SCA output
- license check output
- reviewer decision

## Finding Trigger

Create a finding if AI can introduce a dependency without review, scanning, or documented justification.

