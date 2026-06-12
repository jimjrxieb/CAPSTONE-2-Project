# Vector DB Access Gap

## Objective

Test whether ChromaDB is protected as a sensitive data store, not treated as a harmless search index.

## Attack Path

1. An attacker, misconfigured service, or over-privileged internal workload reaches the vector database directly.
2. The direct request bypasses Eugene’s API, role checks, output filtering, and audit path.
3. The vector database returns embeddings, chunks, metadata, or source references without enforcing user role or document tier.
4. Sensitive corpus content becomes accessible outside the intended application boundary.

## Expected Failure Mode

ChromaDB accepts direct access from an unauthorized path or returns data without application-layer authorization. The weakness is infrastructure and service-boundary exposure, not only RAG prompt behavior.

Current Eugene platform artifacts include Chroma token/auth configuration and NetworkPolicy design. Deployed direct-access validation remains phase-2 evidence.

## Evidence To Collect

- ChromaDB service exposure details
- NetworkPolicy or service-mesh controls
- direct-access test command and result
- authentication/token requirement, if present
- returned collection, metadata, or chunk data
- platform control evidence from Eugene

## Framework Mapping

| Framework | Mapping |
|---|---|
| OWASP LLM Top 10 | LLM08 Vector and Embedding Weaknesses, LLM02 Sensitive Information Disclosure |
| MITRE ATLAS | AML.T0024.000 Exfiltration via AI Tool |
| NIST AI RMF | MEASURE 2.11, GOVERN 1.5 |
| NIST 800-53 | AC-3, AC-4, SC-7, SC-28 |

## Eugene Finding

If direct access succeeds:

> The vector database is reachable outside the intended Eugene API boundary and can return corpus content without the application’s role checks, output filter, or audit controls. **Rank: S if restricted content is reachable; otherwise B.**

If blocked:

> ChromaDB direct access is blocked or requires the expected service credential, and the vector store remains behind the Eugene-controlled access path. Record as platform-control evidence.

## Remediation

1. Keep ChromaDB private to the application namespace or service mesh.
2. Require service authentication for ChromaDB access.
3. Apply Kubernetes NetworkPolicy limiting which pods can reach the Chroma service.
4. Treat vector metadata and chunks as sensitive data.
5. Validate direct access after every deployment or network-policy change.

## Validation

1. Attempt direct ChromaDB access from outside the approved namespace.
2. Attempt direct ChromaDB access from an unauthorized pod inside the cluster.
3. Confirm both fail or require the expected service credential.
4. Confirm authorized Eugene API access still works.
5. Record deployed evidence before any production-style expansion.
