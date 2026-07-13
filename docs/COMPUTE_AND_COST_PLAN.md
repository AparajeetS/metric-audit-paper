# Compute And Execution Resource Plan

Status: planning specification for MBE 2.0.

This document estimates the experimental resources required to execute the
research program. It is not a vendor quote, a claim that scientific quality is
measured by GPU-hours, or a promise to spend an entire grant allocation.

Public planning is expressed in workload units because cloud rates, regional
availability, preemption, storage, and data-transfer charges change frequently.
Provider quotes and account-specific billing information are checked at each
release gate. Actual costs, material deviations, and unused funds are reported
in the final public spend ledger.

## Resource Envelope

The minimum operational target is approximately 400 RTX 4090-equivalent
GPU-hours. The recommended envelope is approximately 650 equivalent hours when
the public-corpus gate supports proceeding to the larger holdout and
reliability program.

These estimates assume:

- public model corpora provide part of the benchmark;
- synthetic calibration and most statistics run on CPU;
- new training uses reproducible small and medium standard models;
- interrupted jobs support checkpoint and resume;
- checkpoints are curated rather than retained indiscriminately;
- expensive metric families are narrowed by mechanism if pilot runtimes exceed
  the frozen envelope.

## Minimum Workload

The v1 project showed that a large row count can be misleading when runs are
not independent or a task is invalid. New resources therefore prioritize
repeated configurations, independent environments, leakage checks, transport,
and measurement reliability.

| Work package | Minimum design | 4090-equivalent GPU-hours |
|---|---|---:|
| Public-corpus checkpoint and metric extraction | at least one substantial corpus | 60-100 |
| Corrected image factorial | 240 runs | 70-120 |
| Corrected causal-text factorial | 100 runs | 70-120 |
| Locked external holdout | reserved public environment or 80-120 new runs | 30-80 |
| Metric repeatability and batch-size checks | selected checkpoints | 25-40 |
| Pilots, failed jobs, preemption, and approved reruns | controlled reserve | 60-90 |
| **Planning range** |  | **315-550** |

The minimum corrected factorial is fixed at 340 training runs:

```text
Image: 2 datasets x 3 architectures x 8 configurations x 5 seeds = 240
Text:  1 dataset x 2 model sizes x 10 configurations x 5 seeds = 100
```

These are 68 configuration blocks with five repeated seeds, not 340 IID
observations. The pilot must demonstrate that this design resolves the frozen
minimum relevant improvement. Otherwise scale compute pauses and the design is
reassessed before additional resources are released.

## Recommended Extension

The larger envelope may support:

- 360 image runs rather than 240;
- 150-200 causal-text runs rather than 100;
- a larger locked external holdout;
- metric measurements on multiple fixed batches;
- an independent reference implementation;
- sufficient recovery capacity for preempted or failed jobs.

It does not authorize post-hoc metric searches or rerunning until a preferred
narrative appears.

## Release Gates

| Gate | Resource released | Requirement |
|---|---:|---|
| Synthetic calibration | CPU | null, proxy, and deceptive-control behavior is calibrated |
| Public-corpus comparison | 60-100 GPU-h | MBE answers a stable question not already supplied by prior methods |
| End-to-end pilot | 15-25 GPU-h | leakage, duplicate-key, recovery, schema, and runtime checks pass |
| Image factorial | 70-120 GPU-h | frozen configurations, seeds, splits, and metric cards |
| Causal-text factorial | 70-120 GPU-h | causal-mask and target computation tests pass |
| Protected holdout | 30-80 GPU-h | commit, container, hypotheses, and analysis command are timestamped |
| Final reliability checks | 20-40 GPU-h | headline conclusions survive blocked uncertainty and sensitivity checks |

No main sweep launches before synthetic calibration and the public-corpus
novelty comparison pass.

## What The Grant Compute Ceiling Covers

The public grant budget uses a ceiling for compute and storage rather than a
single raw GPU-rental estimate. The ceiling covers:

- primary image and causal-text execution;
- protected-holdout execution;
- approved failed-job recovery and uncertainty-critical reruns;
- independent duplicate execution;
- checkpoint, ledger, and public-corpus storage;
- artifact transfer, egress, and archival preparation;
- provider and regional availability variance.

The ceiling is not a spending target. Primary training may use only a fraction
of it when favorable capacity is available. Savings remain visible in the
spend ledger and do not automatically authorize additional exploratory runs.

## Procurement And Cost Governance

Before each paid gate:

1. obtain current comparable quotes from at least two suitable providers;
2. record the selected hardware, region, runtime estimate, storage, and egress;
3. set a maximum gate allocation and automatic shutdown condition;
4. verify checkpoint/resume and duplicate-run prevention;
5. reconcile completed runs, failures, and billing daily;
6. retain invoices and publish an aggregate spend entry without credentials or
   account identifiers.

Budget alarms are set at 50%, 75%, and 90% of each approved gate. The final
reserve is limited to missing factorial cells and preregistered
uncertainty-critical reruns.

## What This Program Does Not Buy

The planned envelope does not support:

- full ImageNet training across hundreds of configurations;
- pretraining modern large language models from scratch;
- exhaustive evaluation of every published metric;
- post-hoc rerunning until a preferred conclusion appears;
- CEI-R design or tuning on the protected holdout.

If large-model or ImageNet evidence becomes necessary, the project must seek a
separate resource decision or use released checkpoints. Prestige-scale compute
must not displace repeated seeds, valid controls, and independent replication.

## Bottom Line

The resource plan is designed to purchase a credible answer, not a large bill:
a calibrated protocol, a public-corpus comparison, 340 corrected repeated
training runs, a protected holdout, reliability checks, and independent
execution. Compute is released only when the preceding scientific gate earns
it.
