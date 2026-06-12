> Synthetic data for Capstone 2 testing only.
> No real patient, customer, credential, contract, or GuidePoint client data.

---

# MedData Nexus Health Systems
## IAM and Access Control Review Notes — 2026
**Document ID:** SEC-IAM-2026-001
**Review Period:** Q1 2026 (January – March)
**Report Date:** April 10, 2026
**Prepared By:** IT Security Team
**Reviewed By:** Constant Yung, CISO
**Classification:** Restricted
**Distribution:** CISO, CTO, Platform Engineering Lead — IT Security Only

---

## 1. Review Scope

This document records privileged access assignments, service account inventories, and access control gap findings for the MedData Nexus AWS environment and Kubernetes cluster as of Q1 2026. It is classified Restricted because it contains role ARNs, account identifiers, and privileged principal assignments that could assist lateral movement if disclosed to unauthorized parties.

This document must not be submitted to the Internal AI RAG Chatbot or any external AI system without CISO written authorization.

---

## 2. AWS IAM — Privileged Role Inventory

| Role Name | ARN (Fake) | Assigned Principals | Privilege Level | Last Review |
|---|---|---|---|---|
| MedData-AdminRole | `arn:aws:iam::FAKE-ACCT-001:role/MedData-AdminRole` | 2 named users (IT Security Lead, Platform Eng Lead) | Full admin — break-glass only | 2026-03-01 |
| MedData-SecurityAuditRole | `arn:aws:iam::FAKE-ACCT-001:role/MedData-SecurityAuditRole` | 4 named users (IT Security team) | Read-only across all services | 2026-03-01 |
| MedData-EKSClusterAdmin | `arn:aws:iam::FAKE-ACCT-001:role/MedData-EKSClusterAdmin` | OIDC federated (K8s cluster) | EKS cluster management | 2026-02-15 |
| MedData-RDSReadOnly | `arn:aws:iam::FAKE-ACCT-001:role/MedData-RDSReadOnly` | 6 service accounts | Read-only RDS access | 2026-03-01 |
| MedData-S3DataLake | `arn:aws:iam::FAKE-ACCT-001:role/MedData-S3DataLake` | 3 pipeline service accounts | Read/write to internal data lake buckets | 2026-01-20 |
| MedData-RAGPipelineRole | `arn:aws:iam::FAKE-ACCT-001:role/MedData-RAGPipelineRole` | ChromaDB ingest service account | S3 read for RAG source bucket only | 2026-03-15 |

**Note — AdminRole:** Break-glass access. MFA required. Usage logged to CloudTrail. Last use: 2026-02-03 (platform upgrade window). No unexplained use detected in Q1.

---

## 3. Kubernetes RBAC — Cluster Role Summary

| ClusterRole | Subjects | Namespace Scope | Risk Level |
|---|---|---|---|
| cluster-admin | 1 IAM role (EKSClusterAdmin), 1 service account (ci-deploy-sa) | Cluster-wide | High — monitored |
| view | compliance-reader service account | All namespaces | Low |
| rag-pipeline-role | rag-sa (meddata-rag namespace) | meddata-rag only | Low — scoped |
| audit-reader-role | eugene-sa (assessment namespace) | meddata-rag, audit | Low — read-only |

**Gap identified (G-IAM-001):** `ci-deploy-sa` holds cluster-admin. Remediation: scope to deploy-only ClusterRole on target namespaces. Owner: Platform Engineering Lead. Target: 2026-06-30.

---

## 4. Service Account Inventory

| Service Account | Namespace | Purpose | External Permissions | Notes |
|---|---|---|---|---|
| rag-sa | meddata-rag | RAG pipeline ingest | S3 read (MedData-RAGPipelineRole) | Reviewed — scoped correctly |
| eugene-sa | assessment | Assessment evidence runner | Audit log read | Reviewed — no write access |
| ci-deploy-sa | kube-system | CI/CD deploy | cluster-admin (see gap G-IAM-001) | Remediation scheduled |
| chroma-sa | meddata-rag | ChromaDB in-cluster access | None — cluster-local | Reviewed — no external exposure |
| compliance-reader | compliance | Compliance dashboard read | None | Reviewed — scoped correctly |

---

## 5. Privileged Account Access Review Findings

| Finding ID | Control | Description | Severity | Status |
|---|---|---|---|---|
| G-IAM-001 | AC-6 (Least Privilege) | ci-deploy-sa holds cluster-admin | Medium | Open — remediation 2026-06-30 |
| G-IAM-002 | AC-2 (Account Management) | 1 former contractor IAM user not deprovisioned within SLA | Medium | Closed 2026-03-18 — account disabled |
| G-IAM-003 | IA-5 (Authenticator Management) | MedData-AdminRole MFA policy not enforced by SCP — relies on IAM policy only | High | Open — SCP enforcement requires OU restructure, tracking in POA&M |
| G-IAM-004 | AU-9 (Protection of Audit Information) | CloudTrail log bucket lacks Object Lock — logs deletable by AdminRole | Medium | Open — Object Lock enable scheduled 2026-04-30 |

---

## 6. Access Review — AI System Service Principals

The RAG pipeline service principal (`MedData-RAGPipelineRole`) was reviewed specifically in context of the AI chatbot deployment:

- S3 bucket policy restricts to `s3:GetObject` on `meddata-rag-source-docs/*` only — no list, no write, no cross-bucket
- ChromaDB runs in-cluster with no IAM binding — accessible only within `meddata-rag` namespace
- No service principal has write access to the ChromaDB volume from outside the cluster

**Gap identified (G-IAM-005):** ChromaDB API has no authentication — any pod in the cluster can query any collection. This aligns with F-001 in the AI security assessment (no per-role access control on ChromaDB). See `CBBP-PLAN/COMPLY/meddata-trust-boundaries.md` Boundary 2.

---

## 7. Next Review

Scheduled: Q3 2026 (July).
Trigger for out-of-cycle review: any new service account created, any IAM role policy change, any new AI system onboarded to AI-INV-001.

---

*Classification: Restricted — IT Security distribution only*
*Do not submit to Internal RAG Chatbot or any external AI system*
