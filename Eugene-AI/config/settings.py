"""All configuration loaded from environment."""
from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv


EUGENE_ROOT = Path(__file__).resolve().parents[1]
SLOT_ROOT = EUGENE_ROOT.parent
ROOT_ENV_PATH = SLOT_ROOT / ".env"
LOCAL_ENV_PATH = EUGENE_ROOT / ".env"

# Root .env is the shared credential/config boundary for the slot.
# Existing process environment wins so CI/Kubernetes secrets can override local files.
load_dotenv(ROOT_ENV_PATH, override=False)
load_dotenv(LOCAL_ENV_PATH, override=False)


class Settings:
    eugene_root: Path = EUGENE_ROOT
    slot_root: Path = SLOT_ROOT
    root_env_path: Path = ROOT_ENV_PATH

    # Model
    ollama_endpoint: str = os.getenv("OLLAMA_ENDPOINT", "http://localhost:11434")
    ollama_model: str = os.getenv("OLLAMA_MODEL", "llama3.2:3b")
    ollama_embed_model: str = os.getenv("OLLAMA_EMBED_MODEL", "nomic-embed-text:v1")
    eugene_mode: str = os.getenv("EUGENE_MODE", "deterministic")

    # ChromaDB
    chroma_host: str = os.getenv("CHROMA_HOST", "localhost")
    chroma_port: int = int(os.getenv("CHROMA_PORT", "8001"))
    chroma_collection: str = os.getenv("CHROMA_COLLECTION", "eugene-meddata-nexus")
    chroma_auth_token: str = os.getenv("CHROMA_AUTH_TOKEN", "")
    chroma_auth_header: str = os.getenv("CHROMA_AUTH_TOKEN_TRANSPORT_HEADER", "Authorization")
    chroma_persist_path: Path = Path(
        os.getenv("CHROMA_PERSIST_PATH", str(eugene_root / "evidence" / "chroma"))
    )

    # API
    api_host: str = os.getenv("API_HOST", "127.0.0.1")
    api_port: int = int(os.getenv("API_PORT", "8000"))
    query_rate_limit_per_minute: int = int(os.getenv("QUERY_RATE_LIMIT_PER_MINUTE", "60"))
    disable_docs: bool = os.getenv("DISABLE_DOCS", "true").lower() == "true"
    cors_origins: list[str] = os.getenv("CORS_ORIGINS", "http://localhost:7860").split(",")

    # Audit
    audit_log_path: Path = Path(os.getenv("AUDIT_LOG_PATH", str(eugene_root / "evidence" / "audit-log.jsonl")))
    review_log_path: Path = Path(os.getenv("REVIEW_LOG_PATH", str(eugene_root / "evidence" / "review-log.jsonl")))
    corpus_alert_log_path: Path = Path(
        os.getenv("CORPUS_ALERT_LOG_PATH", str(eugene_root / "evidence" / "corpus-alert-log.jsonl"))
    )
    corpus_owner_registry_path: Path = Path(
        os.getenv("CORPUS_OWNER_REGISTRY_PATH", str(eugene_root / "config" / "corpus-owners.json"))
    )
    slack_alerts_enabled: bool = os.getenv("SLACK_ALERTS_ENABLED", "false").lower() == "true"
    slack_webhook_url: str = os.getenv("SLACK_WEBHOOK_URL", "")

    # Auth
    admin_token: str = os.getenv("ADMIN_TOKEN", "")
    it_security_token: str = os.getenv("IT_SECURITY_TOKEN", "")
    compliance_analyst_token: str = os.getenv("COMPLIANCE_ANALYST_TOKEN", "")
    vendor_risk_token: str = os.getenv("VENDOR_RISK_TOKEN", "")

    # Corpus
    corpus_manifest_path: Path = Path(
        os.getenv(
            "CORPUS_MANIFEST_PATH",
            str(eugene_root.parent / "CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB" / "target-client" / "fake-data" / "corpus-manifest.md"),
        )
    )
    corpus_data_path: Path = Path(
        os.getenv(
            "CORPUS_DATA_PATH",
            str(eugene_root.parent / "CAPSTONE-2-AI-SECURITY-ASSESSMENT-LAB" / "target-client" / "fake-data"),
        )
    )
    query_top_k: int = int(os.getenv("QUERY_TOP_K", "5"))

    def validate(self) -> None:
        if not self.admin_token:
            raise EnvironmentError("ADMIN_TOKEN must be set in environment")
        if self.eugene_mode not in {"deterministic", "ollama"}:
            raise EnvironmentError("EUGENE_MODE must be deterministic or ollama")


settings = Settings()
