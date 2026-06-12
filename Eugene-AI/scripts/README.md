# Eugene Test Runners

Use capped test runners during local mini CBBP loops. Raw `pytest tests -q` should be reserved for explicit checkpoint validation.

## Targeted Loop Check

```bash
scripts/test-targeted.sh
```

Default coverage:
- chatbox client controls
- HITL review workflow
- HITL bypass runner

You can pass specific tests:

```bash
scripts/test-targeted.sh tests/test_sanitizer.py tests/test_output_filter.py
```

## Full Capped Check

```bash
scripts/test-full-capped.sh
```

This runs the full test suite with:
- pytest plugin autoload disabled
- bytecode writes disabled
- fail-fast enabled
- 45-second timeout cap

## Why

The local lab has pytest plugins and UI imports that can hold event-loop resources open when a test hangs. These wrappers keep checks bounded and reduce CPU spikes during iterative BUILD/BREAK work.
