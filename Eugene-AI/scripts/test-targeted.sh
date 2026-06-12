#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

export PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
export PYTHONDONTWRITEBYTECODE=1

if [ "$#" -eq 0 ]; then
  set -- tests/test_chatbox.py tests/test_review_workflow.py tests/test_hitl_review_break_runner.py tests/test_baseline_eval_runner.py tests/test_pipeline_manifest.py tests/test_query_response.py tests/test_query_auth.py tests/test_audit_logger.py tests/test_corpus_contamination_break_runner.py tests/test_corpus_alerts.py tests/test_sanitizer.py tests/test_settings_env.py tests/test_crewai_dry_run.py
fi

timeout --preserve-status 20s pytest -q --tb=short -x "$@"
