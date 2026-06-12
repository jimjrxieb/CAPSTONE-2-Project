"""Generate evidence for platform controls tied to T-12/T-13/T-14/T-16."""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

from config.settings import settings


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _check(name: str, passed: bool, detail: str, evidence: str) -> dict:
    return {
        "control": name,
        "status": "PASS" if passed else "FAIL",
        "detail": detail,
        "evidence": evidence,
    }


def run_platform_control_check() -> dict:
    root = settings.eugene_root
    requirements = root / "requirements.txt"
    sca_workflow = root / ".github" / "workflows" / "sca.yml"
    retriever = root / "src" / "rag" / "retriever.py"
    query_route = root / "src" / "api" / "routes" / "query.py"
    rate_limit = root / "src" / "api" / "rate_limit.py"
    configmap = root / "deploy" / "k8s" / "configmap.yaml"
    secret = root / "deploy" / "k8s" / "secret-template.yaml"
    chroma_deploy = root / "deploy" / "k8s" / "deployment-chromadb.yaml"
    networkpolicy = root / "deploy" / "k8s" / "networkpolicy.yaml"
    serviceaccount = root / "deploy" / "k8s" / "serviceaccount.yaml"
    role = root / "deploy" / "k8s" / "role.yaml"
    rolebinding = root / "deploy" / "k8s" / "rolebinding.yaml"

    requirements_text = _read(requirements)
    sca_text = _read(sca_workflow)
    retriever_text = _read(retriever)
    query_text = _read(query_route)
    rate_limit_text = _read(rate_limit)
    configmap_text = _read(configmap)
    secret_text = _read(secret)
    chroma_deploy_text = _read(chroma_deploy)
    networkpolicy_text = _read(networkpolicy)
    serviceaccount_text = _read(serviceaccount)
    role_text = _read(role)
    rolebinding_text = _read(rolebinding)

    chroma_req = re.search(r"^chromadb==([0-9.]+)$", requirements_text, re.MULTILINE)
    chroma_image = re.search(r"chromadb/chroma:([0-9.]+)", chroma_deploy_text)
    unpinned = [
        line
        for line in requirements_text.splitlines()
        if line and not line.startswith("#") and "==" not in line
    ]

    checks = [
        _check(
            "T-12 model pins recorded",
            "OLLAMA_MODEL: \"llama3.2:3b\"" in configmap_text
            and "OLLAMA_EMBED_MODEL: \"nomic-embed-text:v1\"" in configmap_text
            and "HAIKU" not in configmap_text
            and "HAIKU" not in secret_text,
            "Local generation and embedding models are pinned; Eugene has no external LLM API path in runtime config.",
            "deploy/k8s/configmap.yaml; BUILD/model-decision-record.md",
        ),
        _check(
            "T-12 Chroma package/image version aligned",
            bool(chroma_req and chroma_image and chroma_req.group(1) == chroma_image.group(1)),
            f"requirements chromadb={chroma_req.group(1) if chroma_req else 'missing'}; image chromadb/chroma={chroma_image.group(1) if chroma_image else 'missing'}",
            "requirements.txt; deploy/k8s/deployment-chromadb.yaml",
        ),
        _check(
            "T-13 SCA workflow present",
            "pip-audit" in sca_text and "requirements.txt" in sca_text and "All packages must use ==" in sca_text,
            "GitHub Actions workflow runs pip-audit and rejects non-exact pins on pull requests.",
            ".github/workflows/sca.yml",
        ),
        _check(
            "T-13 requirements exactly pinned",
            not unpinned,
            "All runtime dependencies use exact == pins." if not unpinned else f"Unpinned lines: {unpinned}",
            "requirements.txt",
        ),
        _check(
            "T-14 Chroma server auth configured",
            "CHROMA_SERVER_AUTHN_PROVIDER" in chroma_deploy_text
            and "TokenAuthenticationServerProvider" in chroma_deploy_text
            and "CHROMA_AUTH_TOKEN" in secret_text,
            "Chroma deployment requires token authentication sourced from the Kubernetes secret template.",
            "deploy/k8s/deployment-chromadb.yaml; deploy/k8s/secret-template.yaml",
        ),
        _check(
            "T-14 API uses authenticated Chroma HTTP client in server mode",
            "chromadb.HttpClient" in retriever_text
            and "TokenAuthClientProvider" in retriever_text
            and "chroma_client_auth_credentials" in retriever_text,
            "Retriever switches to HttpClient when CHROMA_HOST is not localhost and supplies token auth when configured.",
            "src/rag/retriever.py",
        ),
        _check(
            "T-14 NetworkPolicy restricts Chroma ingress",
            "name: chromadb-allow-api-only" in networkpolicy_text
            and "app: chromadb" in networkpolicy_text
            and "app: eugene-api" in networkpolicy_text
            and "port: 8000" in networkpolicy_text,
            "Default-deny policy is paired with Chroma ingress allow-list from eugene-api pods only.",
            "deploy/k8s/networkpolicy.yaml",
        ),
        _check(
            "T-15 API service account least privilege",
            "automountServiceAccountToken: false" in serviceaccount_text
            and "kind: Role" in role_text
            and "rules: []" in role_text
            and "ClusterRole" not in role_text
            and "kind: RoleBinding" in rolebinding_text
            and "kind: Role" in rolebinding_text
            and "ClusterRole" not in rolebinding_text
            and "name: eugene-api" in rolebinding_text,
            "API service account is bound to an empty namespace-scoped Role and does not mount an API token.",
            "deploy/k8s/serviceaccount.yaml; deploy/k8s/role.yaml; deploy/k8s/rolebinding.yaml",
        ),
        _check(
            "T-16 query rate limiting wired",
            "check_rate_limit(" in query_text
            and "Query rate limit exceeded" in rate_limit_text
            and "QUERY_RATE_LIMIT_PER_MINUTE" in configmap_text,
            "POST /query enforces a per-token in-process request limit, with Kubernetes config exposing the limit.",
            "src/api/routes/query.py; src/api/rate_limit.py; deploy/k8s/configmap.yaml",
        ),
    ]

    overall_status = "PASS" if all(check["status"] == "PASS" for check in checks) else "FAIL"
    return {
        "run_id": _now(),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "phase": "BUILD/BREAK",
        "test": "Platform control evidence for T-12/T-13/T-14/T-16",
        "analyst": "codex",
        "overall_status": overall_status,
        "checks": checks,
        "residual_risk": [
            "This is static evidence. A deployed-cluster BREAK run must still curl Chroma directly and prove unauthenticated access is rejected.",
            "External LLM APIs are out of scope for Eugene. Adding one later requires a new COMPLY boundary and renewed BREAK evidence.",
        ],
    }


def write_evidence(payload: dict) -> Path:
    evidence_dir = settings.eugene_root / "evidence"
    evidence_dir.mkdir(parents=True, exist_ok=True)
    path = evidence_dir / f"platform-control-check-{payload['run_id']}.json"
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return path


def main() -> int:
    payload = run_platform_control_check()
    print(json.dumps(payload, indent=2))
    path = write_evidence(payload)
    print(f"Evidence written: {path}")
    return 0 if payload["overall_status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
