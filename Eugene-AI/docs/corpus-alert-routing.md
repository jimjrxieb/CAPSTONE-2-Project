# Corpus Alert Routing

Eugene writes corpus-integrity alerts when the ingest path detects unsigned, unapproved, poisoned, secret-bearing, or PHI-like documents.

## Owner Registry

Owner metadata lives in:

```text
Eugene-AI/config/corpus-owners.json
```

Current primary owner:

```text
RAG Corpus Owner
Team: AI Platform Governance
Slack: #rag-corpus-alerts
Email: rag-corpus-owner@meddata-nexus.fake
Backup: IT Security
```

## Local Alert Log

Default local evidence log:

```text
Eugene-AI/evidence/corpus-alert-log.jsonl
```

Each alert includes:
- alert ID
- severity
- owner and owner contact
- source path and rejection reason
- action required
- OWASP LLM tags
- NIST AI RMF tags
- MITRE ATLAS tags

## Slack Hook

Credentials and local secrets belong in the slot root `.env` file:

```text
/home/jimmie/linkops-industries/GP-copilot/GP-SECLAB/target-application/slot-5/.env
```

Use `.env.example` at the slot root as the template.

Slack delivery is disabled by default. To enable it in a real environment, set these values in the root `.env`:

```dotenv
SLACK_ALERTS_ENABLED=true
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/...
```

Do not commit webhook URLs. Use a secret manager, CI secret, or Kubernetes Secret.

## Validation

Run:

```bash
python3 -m src.evidence.corpus_alert_delivery_check
```

This writes a local alert and previews the Slack payload. It does not send a Slack message unless `SLACK_ALERTS_ENABLED=true` and `SLACK_WEBHOOK_URL` is configured.
