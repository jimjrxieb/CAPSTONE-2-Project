# Deploy Runbook — Falco + Local SIEM Alert Backend (Sprint A · A-T1)

> The deploy-agent runbook that satisfies Sprint A's **A-T1**. Stands up the
> alert backend the BREAK "watch" half depends on, so scenarios A-T2…A-T7 can
> capture *alert-fired* evidence, not just *control-held*.
>
> **Owner:** deploy agent (`dev-environment-agent`) — NOT the pentest agent.
> **Phase rule:** deploying detective infrastructure (Falco, Loki, Grafana) is
> **half-A** — agent-runnable, not blocked by the attack-tool hook. The same
> mechanics as any `helm install`. Attacks come later, in A-T2…A-T7.
> **Authored:** 2026-06-16. Local-lab only; no external endpoints.

---

## Alert Backend — Three Layers

`detection-validation` treats these as ground truth over the app's own pass claim.

| Layer | What it captures | Scenarios that rely on it | Already exists? |
|---|---|---|---|
| **Eugene audit log** (`evidence/audit-log.jsonl`, hash-chained) | app-level rejects/redactions/denies | 1, 2, 3, 4, 5, 7, 8 | ✅ yes |
| **Falco** (modern-eBPF, custom rules) | runtime/network anomalies at the cluster | **6** (direct Chroma access), **4** (cross-role/namespace, optional) | ❌ net-new |
| **Local SIEM** = Falcosidekick → Loki + Grafana, **and** a JSONL evidence file | one analyst pane for Falco + forwarded audit events | all (the "watch" pane) | ❌ net-new |

Honest scoping: only **scenario 6** strictly needs a Falco *network* rule. Scenario
4's cross-role detection is primarily the Eugene audit entry; Falco is a secondary
signal. Scenarios 1, 2, 3, 5, 7, 8 are app-level — their alert is the audit entry,
*forwarded into the SIEM pane* so the SOC sees app + runtime in one place.

---

## Prerequisites

1. Tools on the host: `kind` (or `k3d`), `kubectl`, `helm`, and a container runtime. WSL2 is the target.
2. Eugene deployed first, per the Sprint 2 sequence (`sprint2-plan.md` T3):
   `namespace → configmap → secret (from `secret-template.yaml`, throwaway values) → chromadb → api → services → networkpolicy → role/rolebinding → deploy/policies/`.
3. Resource budget: Falco DaemonSet + Falcosidekick + single-binary Loki + Grafana ≈ 1–2 GB RAM. If the box can't spare it, take the A-T1 blocker path (below) rather than thrashing.

Manifests/values this runbook produces live under a new `Eugene-AI/deploy/alert-backend/` dir (the deploy agent creates them on execution): `falco-values.yaml`, `falco-rules-eugene.yaml`, `loki-values.yaml`, `grafana-datasource.yaml`, `promtail-audit.yaml`.

---

## Step 1 — Cluster + Eugene up

```bash
kind create cluster --name eugene-break
kubectl apply -f Eugene-AI/deploy/k8s/namespace.yaml
kubectl apply -f Eugene-AI/deploy/k8s/configmap.yaml
# secret from template with throwaway values — never real creds
kubectl apply -f Eugene-AI/deploy/k8s/secret-template.yaml
kubectl apply -f Eugene-AI/deploy/k8s/deployment-chromadb.yaml \
              -f Eugene-AI/deploy/k8s/service-chromadb.yaml
kubectl apply -f Eugene-AI/deploy/k8s/serviceaccount.yaml \
              -f Eugene-AI/deploy/k8s/role.yaml \
              -f Eugene-AI/deploy/k8s/rolebinding.yaml
kubectl apply -f Eugene-AI/deploy/k8s/deployment-api.yaml \
              -f Eugene-AI/deploy/k8s/service-api.yaml
kubectl apply -f Eugene-AI/deploy/k8s/networkpolicy.yaml
kubectl -n eugene-ai wait --for=condition=ready pod --all --timeout=180s
```

Apply `deploy/policies/` only if Kyverno/OPA is installed; otherwise record "policies validated statically only" in the evidence — do not silently skip.

## Step 2 — Falco (modern eBPF) + Falcosidekick

On kind/WSL2 the kernel-module driver usually won't build. Use the **modern eBPF**
probe — this is the load-bearing setting.

```bash
helm repo add falcosecurity https://falcosecurity.github.io/charts && helm repo update
helm install falco falcosecurity/falco \
  --namespace falco --create-namespace \
  --set driver.kind=modern_ebpf \
  --set falcosidekick.enabled=true \
  --set falcosidekick.config.loki.hostport=http://loki.siem.svc:3100 \
  --set falcosidekick.config.loki.tenant=eugene \
  -f Eugene-AI/deploy/alert-backend/falco-values.yaml
```

`falco-values.yaml` also enables a **file output** so every alert is written to a
JSONL evidence file (the evidence-of-record, independent of Grafana):
Falcosidekick `config.fileoutput` → a mounted path the runbook copies to
`Eugene-AI/evidence/break/falco-alerts-<run-id>.jsonl` at teardown.

## Step 3 — Custom Falco rules (scenario-mapped)

`falco-rules-eugene.yaml`, loaded via the chart's `customRules`:

- **`Unexpected Connection to Chroma` (scenario 6):** fire on an inbound/outbound
  connection to the ChromaDB service port (`chromadb:8001`) from any container
  whose pod label is **not** `app=eugene-api`. This is the *detection* of the
  A-T6 attempt; the
  NetworkPolicy is the *block*. Both must show: block + this alert.
- **`Cross-Namespace Access to Eugene` (scenario 4, secondary):** fire on a
  connection into the `eugene-ai` namespace from an unexpected namespace/SA. Flagged
  as secondary — A-T4's primary proof is the Eugene audit deny entry.

Keep rules narrow (priority `WARNING`+, output includes pod, ns, sa, fd.sip/sport)
so they're legible in Grafana and don't drown in noise.

## Step 4 — Loki + Grafana (the SIEM pane)

```bash
helm repo add grafana https://grafana.github.io/helm-charts && helm repo update
helm install loki grafana/loki -n siem --create-namespace \
  -f Eugene-AI/deploy/alert-backend/loki-values.yaml          # single-binary mode
helm install grafana grafana/grafana -n siem \
  --set-file datasources."datasources\.yaml"=Eugene-AI/deploy/alert-backend/grafana-datasource.yaml
kubectl -n siem wait --for=condition=ready pod --all --timeout=180s
```

`grafana-datasource.yaml` points Grafana at `http://loki.siem.svc:3100`. Pre-load a
dashboard panel: "Eugene BREAK alerts" filtered on the custom-rule names above.

## Step 5 — Forward Eugene audit events into the pane (so app + runtime are one view)

Deploy `promtail-audit.yaml` (a small Promtail) tailing the Eugene API pod's
`audit-log.jsonl` into Loki under label `source=eugene-audit`. Now the SOC pane
shows app-level rejects (scenarios 1,2,3,5,7,8) next to Falco runtime alerts
(6, 4). Optional but it's what makes "the SIEM" a single pane rather than two silos.

---

## Acceptance (A-T1 done when ALL pass)

```bash
helm list -A | grep -E "falco|loki|grafana"                      # three releases present
kubectl -n falco get pod -l app.kubernetes.io/name=falco         # Falco + sidekick Running
kubectl -n siem  get pod                                         # loki + grafana Running
test -f Eugene-AI/evidence/audit-log.jsonl                       # Eugene audit writing
```

Then a **benign end-to-end smoke test** of the watch path — prove an event flows
all the way through before any real scenario runs:

```bash
# trip the Chroma rule benignly: exec a throwaway pod and curl the chroma port
kubectl run probe --image=curlimages/curl -n eugene-ai --restart=Never -- \
  curl -s --max-time 3 http://chromadb.eugene-ai.svc:8001/api/v1/heartbeat || true
# expect: NetworkPolicy blocks it AND the Falco rule fires
```

Smoke test passes when the probe event appears in **both** Loki (visible in Grafana)
and the `falco-alerts-<run-id>.jsonl` evidence file. Delete the probe pod after.

Write one evidence file: `Eugene-AI/evidence/break/alert-backend-deploy-<run-id>.json`
recording cluster type, Falco driver/version, Falcosidekick outputs, Loki/Grafana
versions, the smoke-test result (block + alert-fired in both sinks), and overall_status.

**A-T1 ends with the environment LEFT RUNNING.** Do not tear down — A-T2…A-T7 run
against this live cluster and alert backend. Teardown is the final step of Sprint A
(see below).

## Blocker path (machine can't host it)

If Falco's eBPF probe won't load or RAM is insufficient: stop, write the blocker
into A-T1 and the `alert-backend-deploy` evidence (`overall_status: BLOCKED`,
exact failure), and set A-T2…A-T7 run notes to **"control-held only, alert backend
unavailable."** Do not fake alert-fired evidence. This is the honest degraded
result rule 7 of Sprint A's Ground Rules already calls for.

## Teardown — end of Sprint A, NOT after A-T1

**A-T1 leaves the environment running.** A-T2…A-T7 run against this live cluster
and its alert backend; tearing down after A-T1 would force a redeploy and risk
drift between the deploy proof and the pentest runs. Teardown is the **final step
of Sprint A**, after A-T7's verdict is recorded.

```bash
# copy the falco JSONL out of the pod first, then:
helm uninstall grafana loki -n siem; helm uninstall falco -n falco
kind delete cluster --name eugene-break
```

Leave no cluster running once Sprint A is complete. The evidence JSONs persist
under `Eugene-AI/evidence/`.

---

## Guardrails

- **No git.** J reviews and commits.
- **half-A, agent-runnable.** Deploying Falco/Loki/Grafana is detective-infra
  deployment — run it directly. The attack-tool hook applies only in A-T2…A-T7,
  and only if a scenario reaches for external offensive tooling (none do).
- **Throwaway secrets only** in the cluster — never real creds/PHI.
- **Local-lab only.** Loki/Grafana bind in-cluster; no external ingress.
- **Evidence naming:** `<name>-<ISO-run-id>.json|jsonl` under `Eugene-AI/evidence/break/`.
