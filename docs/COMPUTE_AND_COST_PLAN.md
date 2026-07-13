# Compute And Cloud Cost Plan

Status: planning estimate for MBE 2.0, priced on 2026-07-12.

This budget estimates the minimum new compute needed for a serious empirical
submission. It is not a claim that JMLR has a GPU-hour requirement. Reviewers
care about experimental design, independence, uncertainty, and relevance, not
the dollar value of the hardware bill.

## Executive Estimate

The minimum credible plan is approximately:

```text
400 RTX 4090-equivalent GPU-hours
$300-$500 all-in cloud budget
```

The recommended plan, with a larger external holdout and enough contingency to
avoid underpowered or incomplete tables, is:

```text
650 RTX 4090-equivalent GPU-hours
$600-$900 all-in cloud budget
```

These numbers assume:

- public model corpora provide a substantial part of the benchmark;
- synthetic calibration and most statistics run on CPU;
- training uses small standard models rather than ImageNet-scale foundation
  models;
- spot/community GPUs are checkpointed and automatically resumed;
- checkpoints are curated rather than retained indiscriminately;
- no stipend, salary, or personal-time cost is included.

An all-on-demand hyperscaler execution should budget approximately
`$1,200-$2,500`, depending on VM shape, region, failures, and storage.

## Why 400 GPU-Hours Is The Minimum

The v1 project already demonstrates that a large row count can be misleading
when runs are not independent or the task is invalid. The minimum budget is
therefore allocated to repeated configurations, independent environments, and
metric reliability rather than simply maximizing model count.

| Work package | Minimum design | 4090-equivalent GPU-hours |
|---|---|---:|
| Public-corpus checkpoint/metric extraction | at least one substantial corpus | 60-100 |
| Corrected image factorial | 240 runs | 70-100 |
| Corrected causal text factorial | 100 runs | 70-100 |
| Locked external holdout | 80-120 runs or reserved public environment | 30-60 |
| Metric repeatability and batch-size checks | selected checkpoints | 25-40 |
| Pilots, failed jobs, preemption, reruns | approximately 20-25% reserve | 60-90 |
| **Planning total** |  | **315-490** |

The project should reserve 400 hours as the minimum operational target. If the
pilot benchmarks indicate that Hessian/Fisher extraction is slower than
expected, the metric list should be narrowed by mechanism before increasing the
budget.

## Recommended 650-Hour Plan

The recommended plan supports:

- 360 image runs rather than 240;
- 150-200 causal text runs rather than 100;
- a larger locked holdout;
- metric measurements on multiple fixed batches;
- reference-implementation validation;
- sufficient failure and preemption reserve.

It does not fund ImageNet training, large language-model pretraining, or broad
foundation-model fine-tuning. Those would be extensions, not minimum evidence.

## Current Reference Prices

Prices are dynamic and must be checked again immediately before purchase.

### RTX 4090 rental

RunPod currently advertises RTX 4090 access from `$0.34/hour` on its model page,
while the page headline shows `$0.69/hour` for currently offered capacity:

https://www.runpod.io/gpu-models/rtx-4090

Vast.ai lists real-time 4090 offers around `$0.35/hour` at the time of this
estimate, with a much wider availability-dependent range:

https://vast.ai/

For budgeting, use `$0.69/hour` rather than assuming the lowest advertised
community offer will always be available.

### Google Cloud L4

Google lists current spot GPU prices in `us-central1` of approximately:

- L4: `$0.2231/GPU-hour`;
- T4: `$0.14/GPU-hour`;
- A100 40 GB: `$1.1472/GPU-hour`;
- A100 80 GB: `$1.5712/GPU-hour`.

Source:

https://cloud.google.com/spot-vms/pricing

The GPU-only on-demand L4 price is approximately `$0.5600/hour` before the
required VM CPU, memory, disk, and network charges:

https://cloud.google.com/products/compute/gpus-pricing

Google notes that spot prices are dynamic and can change as frequently as every
30 days. The final cost must use the pricing calculator and selected region.

## Raw Compute Cost Scenarios

| Scenario | Hours | Rate assumption | Raw GPU cost |
|---|---:|---:|---:|
| Lowest opportunistic 4090 | 400 | $0.34/h | $136 |
| Conservative rented 4090 | 400 | $0.69/h | $276 |
| Lowest opportunistic 4090 | 650 | $0.34/h | $221 |
| Conservative rented 4090 | 650 | $0.69/h | $449 |
| GCP spot L4, GPU component only | 400 | $0.2231/h | $89 |
| GCP spot L4, GPU component only | 650 | $0.2231/h | $145 |
| GCP on-demand L4, GPU component only | 400 | $0.5600/h | $224 |
| GCP on-demand L4, GPU component only | 650 | $0.5600/h | $364 |

The GCP rows exclude VM host, disk, and network charges and are therefore not
all-in prices.

## Non-GPU Project Costs

Minimum reserve:

| Item | Minimum | Recommended | Notes |
|---|---:|---:|---|
| Persistent storage and snapshots | $30 | $75 | curated checkpoints and raw ledgers |
| Egress and artifact transfer | $20 | $75 | depends strongly on public-corpus size |
| CPU analysis and orchestration | $20 | $60 | most statistics should run locally |
| Failed/preempted-job overhead | included in hours | included in hours | 20-25% GPU reserve |
| Archival DOI/repository | $0 | $0 | use free public archival services where possible |
| **Non-GPU reserve** | **$70** | **$210** | excluding labor |

Because public checkpoint corpora can be large, storage and egress must be
measured during M3 before committing to the full download.

## Recommended Purchase Decision

### Minimum viable serious evidence

Approve a hard cap of `$500` only after Gates M0-M4 pass.

This supports roughly 400 4090-equivalent hours plus modest storage and egress.
It is sufficient if:

- public corpora are usable;
- the primary metric battery is limited to mechanism-distinct metrics;
- the external holdout can partly reuse a reserved public environment;
- pilots confirm the runtime model.

### Safer JMLR-targeted evidence

Approve `$900` after the public-corpus benchmark demonstrates novelty.

This provides enough room for approximately 650 equivalent hours, larger seed
blocks, a stronger holdout, and failed-run recovery without altering the
protocol to fit a depleted budget.

### Google Cloud credits

`$300` in Google Cloud credits can plausibly cover the GPU component of the
minimum plan on spot L4 capacity, and may cover most of the total minimum plan
if jobs are efficient and data transfer is small. It should not be treated as
guaranteed coverage because:

- spot capacity can be unavailable or preempted;
- the VM host and storage are billed separately;
- metric extraction may be memory- or runtime-dominated;
- prices and quotas vary by region.

## Compute Governance

No expensive job launches without:

1. a frozen manifest and unique configuration IDs;
2. an estimated per-run runtime from the pilot;
3. a maximum spend and automatic shutdown condition;
4. checkpoint/resume support;
5. a completed-run ledger that prevents accidental duplication;
6. failure rows retained for audit;
7. daily cost and completion reconciliation.

Budget alarms should be set at 50%, 75%, and 90% of the approved cap. The final
10% is reserved for missing cells and reviewer-critical reruns, not exploratory
metric design.

## What This Budget Does Not Buy

The minimum plan does not support:

- full ImageNet training across hundreds of configurations;
- pretraining modern language models from scratch;
- exhaustive evaluation of every published metric;
- post-hoc rerunning until a preferred narrative appears;
- CEI-R hyperparameter searches on the locked holdout.

If reviewers later require ImageNet or large-model evidence, seek separate
credits or use released checkpoints. Do not consume the core replication budget
on one prestige-scale experiment at the expense of repeated seeds and valid
controls.

## Bottom Line

The lowest defensible cash target is approximately `$300-$500`, not because
that amount impresses a reviewer, but because it funds a valid minimum design:
public-corpus comparison, 340 new repeated training runs, a protected holdout,
and measurement-reliability checks.

The recommended cap is `$900`. Beyond that, additional money should only be
spent after MBE 2.0 demonstrates clear novelty over existing conditional and
robust metric-evaluation methods.
