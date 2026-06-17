# CKS Platform Build Plan — MDN-AI-001

> **Source:** `COMPLY/comply-checklist.md` Kubernetes / CKS Platform Controls  
> **Purpose:** Define the local capstone platform hardening artifacts BUILD must create for reviewable CKS-style evidence.

**Status:** COMPLETE — local capstone platform build scope closed
**Approved by:** J · build-approver (senior CISSP/CISO) · 2026-06-12
**Approval scope:** Local/dev platform artifacts, static policy checks, and lab evidence only.

---

## Platform Scope

The local Eugene build can run without Kubernetes, but the capstone includes a
reviewable Kubernetes-style platform package so a reviewer can inspect the
intended workload, network, policy, and supply-chain controls. Live cloud
deployment is outside this BUILD.

Target artifact path:

```text
Eugene-AI/
  Dockerfile
  deploy/
    k8s/
      namespace.yaml
      configmap.yaml
      secret-template.yaml
      deployment-api.yaml
      deployment-chromadb.yaml
      service-api.yaml
      service-chromadb.yaml
      networkpolicy.yaml
    policies/
      disallow-privileged.yaml
      require-resource-limits.yaml
      disallow-latest-tag.yaml
      require-non-root.yaml
```

---

## Required Controls

| Control | Artifact | Acceptance Criteria |
|---|---|---|
| Non-root workload | `Dockerfile`, `deployment-api.yaml` | App runs as non-root UID; privilege escalation disabled |
| Read-only app posture | `deployment-api.yaml` | Root filesystem read-only where feasible; writable volume only for evidence/logs |
| Resource limits | `deployment-*.yaml` | CPU and memory requests/limits set for API and ChromaDB |
| Namespace isolation | `namespace.yaml` | RAG workload isolated from other workloads |
| Kubernetes RBAC | service account + role files | API and ingest jobs use least-privilege service accounts |
| NetworkPolicy | `networkpolicy.yaml` | Default deny; allow only API/chatbox/retriever paths needed |
| Secret template | `secret-template.yaml` | Placeholder only; no real token values committed |
| ConfigMap | `configmap.yaml` | Non-secret model, Chroma, CORS, and audit settings |
| Admission policy | `deploy/policies/*.yaml` | OPA/Kyverno rejects privileged pods, missing limits, latest tags, root user |
| Image scanning | CI workflow | Image scan fails on high/critical findings unless exception is recorded |
| Audit logging | API plus K8s audit requirement | App audit JSONL plus K8s namespace event retention are documented |

---

## CKS Checklist

| CKS Area | BUILD Check |
|---|---|
| Cluster setup and hardening | Namespace isolation, admission policies, audit log requirement |
| System hardening | Non-root containers, dropped capabilities, read-only filesystem |
| Minimize microservice vulnerabilities | NetworkPolicy and resource limits |
| Supply chain security | Image scan, SBOM, exact dependency pins, no latest tags |
| Monitoring, logging, runtime security | App audit logs and Kubernetes event-retention requirement |

---

## Completion Note

This build is complete for the local capstone. It does not claim a production
cloud deployment, managed identity integration, or runtime security operations.
Those are separate adoption decisions outside this BUILD boundary.
