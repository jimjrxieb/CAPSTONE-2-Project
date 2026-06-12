from pathlib import Path

import pytest

from src.rag.document_store import (
    ManifestViolationError,
    check_manifest,
    load_baseline_manifest_records,
    load_manifest_entries,
    validate_baseline_manifest_contract,
)


def test_load_manifest_entries_excludes_golden_questions(tmp_path):
    manifest = tmp_path / "corpus-manifest.md"
    manifest.write_text(
        "| Category | File |\n"
        "|---|---|\n"
        "| Policies | `source-documents/policies/ai-usage-policy-v2.md` |\n"
        "| Eval | `expected-retrieval/golden-questions.md` |\n"
        "| Variant | `policy-with-injection-payload.md` |\n",
        encoding="utf-8",
    )
    assert load_manifest_entries(manifest) == {"source-documents/policies/ai-usage-policy-v2.md"}


def test_check_manifest_rejects_unapproved_file(tmp_path):
    corpus_root = tmp_path / "fake-data"
    path = corpus_root / "unapproved.md"
    path.parent.mkdir(parents=True)
    path.write_text("unapproved", encoding="utf-8")

    with pytest.raises(ManifestViolationError):
        check_manifest(path, corpus_root=corpus_root, manifest_entries=set())


def test_baseline_manifest_contract_requires_owner_approval_and_classification(tmp_path):
    manifest = tmp_path / "corpus-manifest.md"
    manifest.write_text(
        "## Baseline Corpus\n\n"
        "| Category | File | Classification | Owner | Approved By | Approval Date | Purpose |\n"
        "|---|---|---|---|---|---|---|\n"
        "| Policies | `source-documents/policies/ai-usage-policy-v2.md` | Internal |  | CISO | 2026-01-01 | Policy lookup |\n"
        "\n## Excluded From Clean Baseline\n",
        encoding="utf-8",
    )

    findings = validate_baseline_manifest_contract(manifest)
    assert findings == [
        {
            "source_path": "source-documents/policies/ai-usage-policy-v2.md",
            "reason": "MISSING_MANIFEST_METADATA",
            "missing_fields": ["owner"],
        }
    ]


def test_baseline_manifest_records_parse_clean_contract(tmp_path):
    manifest = tmp_path / "corpus-manifest.md"
    manifest.write_text(
        "## Baseline Corpus\n\n"
        "| Category | File | Classification | Owner | Approved By | Approval Date | Purpose |\n"
        "|---|---|---|---|---|---|---|\n"
        "| Policies | `source-documents/policies/ai-usage-policy-v2.md` | Internal | AI Governance | CISO | 2026-01-01 | Policy lookup |\n"
        "\n## Excluded From Clean Baseline\n",
        encoding="utf-8",
    )

    assert validate_baseline_manifest_contract(manifest) == []
    records = load_baseline_manifest_records(manifest)
    assert records[0].owner == "AI Governance"
    assert records[0].approved_by == "CISO"


def test_baseline_manifest_contract_detects_unapproved_file_on_disk(tmp_path):
    corpus_root = tmp_path / "fake-data"
    approved = corpus_root / "source-documents" / "policies" / "ai-usage-policy-v2.md"
    rogue = corpus_root / "source-documents" / "security" / "rogue.md"
    approved.parent.mkdir(parents=True)
    rogue.parent.mkdir(parents=True)
    approved.write_text("approved", encoding="utf-8")
    rogue.write_text("rogue", encoding="utf-8")
    manifest = corpus_root / "corpus-manifest.md"
    manifest.write_text(
        "## Baseline Corpus\n\n"
        "| Category | File | Classification | Owner | Approved By | Approval Date | Purpose |\n"
        "|---|---|---|---|---|---|---|\n"
        "| Policies | `source-documents/policies/ai-usage-policy-v2.md` | Internal | AI Governance | CISO | 2026-01-01 | Policy lookup |\n"
        "\n## Excluded From Clean Baseline\n",
        encoding="utf-8",
    )

    findings = validate_baseline_manifest_contract(manifest, corpus_root=corpus_root)
    assert findings == [
        {"source_path": "source-documents/security/rogue.md", "reason": "UNAPPROVED_FILE_ON_DISK"}
    ]
