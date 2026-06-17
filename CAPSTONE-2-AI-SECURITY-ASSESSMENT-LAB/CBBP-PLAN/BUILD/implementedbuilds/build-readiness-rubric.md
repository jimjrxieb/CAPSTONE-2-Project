# BUILD Readiness Rubric

Use this rubric to decide whether the BUILD phase is ready to hand to BREAK and PROVE.

Scoring:

- 0 = not present
- 1 = notes only
- 2 = drafted but not reviewable
- 3 = reviewable plan
- 4 = implemented with local evidence
- 5 = implemented, tested, and traceable through PROVE

## 1. COMPLY Receiver Quality

| Item | Score | Evidence |
| --- | ---: | --- |
| COMPLY findings are translated into BUILD tickets | 4 | `comply-to-build-handoff.md` |
| Client wishlist and gaps are visible in the build plan | 4 | `comply-to-build-handoff.md`, `../COMPLY/README.md` |
| Each build item has a source finding, threat, or harness requirement | 4 | `../COMPLY/traceability-matrix.md` |
| BUILD scope avoids inventing new client assumptions | 4 | `comply-to-build-handoff.md` |
| Remaining phase-2 items are named honestly | 4 | `sprint1-status.md`, `../../STATUS.md` |

Target: 4+ average.

## 2. AI Dev-Tool Authorization

| Item | Score | Evidence |
| --- | ---: | --- |
| Codex and Claude Code are explicitly allowed or disallowed before build work starts | 4 | `ai-dev-assist-harness.md` |
| Allowed context and prohibited context are documented | 5 | `ai-dev-assist-harness.md` |
| Local socket, network, and destructive-command boundaries are documented | 4 | `ai-dev-assist-harness.md` |
| Human approval is required for sensitive build actions | 4 | `ai-dev-assist-harness.md` |
| AI assistance remains advisory, not ownership or risk acceptance | 5 | `ai-dev-assist-harness.md` |

Target: 4+ average.

## 3. Build Plan Quality

| Item | Score | Evidence |
| --- | ---: | --- |
| Build work is broken into sprint-sized loops | 4 | `comply-to-build-handoff.md`, `sprint1-status.md` |
| Each sprint has clear acceptance criteria | 4 | `comply-to-build-handoff.md` |
| The plan names files, modules, workflows, or policies to build | 4 | `comply-to-build-handoff.md`, `eugene-build-harness.md` |
| Rollback or limitation language exists where risk is high | 3 | `cks-platform-build-plan.md`, `ai-dev-assist-harness.md` |
| The plan distinguishes local capstone proof from production maturity | 4 | `sprint1-status.md`, `../../STATUS.md` |

Target: 4+ average.

## 4. Human Review And Approval

| Item | Score | Evidence |
| --- | ---: | --- |
| Build scope is human-reviewed before implementation | 3 | `comply-to-build-handoff.md`, `ai-dev-assist-harness.md` |
| Security-sensitive changes require CODEOWNERS or equivalent review | 4 | `eugene-build-harness.md`, `../../../Eugene-AI/CODEOWNERS` |
| AI-assisted changes have a disclosure or label gate | 4 | `eugene-build-harness.md`, `../../../Eugene-AI/.github/workflows/ai-assist-label-check.yml` |
| Dependency and platform changes require scan evidence | 4 | `cks-platform-build-plan.md`, `../../../Eugene-AI/.github/workflows/sca.yml` |
| Exceptions must move to PROVE as evidence, not disappear | 4 | `ai-dev-assist-harness.md`, `../PROVE/ai-dev-tool-boundary-evidence.md` |

Target: 4+ average.

## 5. BUILD To BREAK Handoff

| Item | Score | Evidence |
| --- | ---: | --- |
| Each build control has an intended BREAK scenario | 4 | `comply-to-build-handoff.md`, `../COMPLY/traceability-matrix.md` |
| BREAK runners or test steps exist for core controls | 4 | `../BREAK/meddata-break-validation.md`, `sprint1-status.md` |
| Expected pass/fail behavior is documented | 4 | `../BREAK/meddata-break-validation.md` |
| Phase-2 BREAK gaps are clearly named | 4 | `sprint1-status.md`, `../../STATUS.md` |
| BREAK can test without guessing what BUILD meant | 4 | `comply-to-build-handoff.md` |

Target: 4+ average.

## 6. BUILD To PROVE Handoff

| Item | Score | Evidence |
| --- | ---: | --- |
| Evidence paths are named for implemented controls | 4 | `sprint1-status.md`, `../PROVE/loop*-*.md` |
| PROVE receives both pass evidence and limitation notes | 4 | `../PROVE/meddata-prove-package.md` |
| Client deliverables can cite BUILD/BREAK evidence | 4 | `../../deliverables/02-client-findings-report.md` |
| Runtime or platform evidence gaps are not overclaimed | 4 | `sprint1-status.md`, `../../STATUS.md` |
| The build can be explained as a repeatable method, not a one-off script pile | 4 | `README.md` |

Target: 4+ average.

## BUILD Pass Criteria

BUILD is ready for public capstone review when:

- every BUILD lane has a COMPLY source
- Codex / Claude Code boundaries are explicit
- sprint loops have acceptance criteria
- human review gates are visible
- BREAK knows how to test each claim
- PROVE knows what evidence closes each claim
- phase-2 limitations are named instead of hidden

Current assessment: BUILD is complete for the local capstone review boundary.
Future work such as remote CI history, external identity integration, expanded
workflow automation, or cloud deployment requires a new approved BUILD item and
COMPLY traceability.
