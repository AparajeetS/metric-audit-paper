# MBE Calibration Evidence Summary

Status: known-ground-truth and semi-synthetic evidence only. This does not validate real checkpoint metrics or unseen-task transport.

## Main Findings

- Degree-2 polynomial nuisance adjustment fails the generic proxy stress tests: joint false-decision rates span 0.000-1.000 across conditional-null cells.
- Degree-6 polynomial adjustment reduces the same conditional-null joint-decision range to 0.000-0.010 while conditional-signal power spans 1.000-1.000.
- On PGDL Tasks 1-2 real design geometry, null/proxy joint decisions span 0.000-0.070 and injected/task-specialist recovery spans 0.980-1.000.
- Opposite-sign task specialists are recovered within each task and rejected as one stable metric in the balanced pool, supporting task-specific reliability reporting.

## Nuisance Sensitivity

| Source | Nuisance | Conditional-null joint decisions | Signal joint decisions |
|---|---|---:|---:|
| Generic simulation | polynomial degree 2 | 0.000-1.000 | 1.000-1.000 |
| Generic simulation | polynomial degree 6 | 0.000-0.010 | 1.000-1.000 |
| PGDL semi-synthetic | polynomial degrees 2/4/6 | 0.000-0.070 | 0.980-1.000 |
| Generic simulation | Extra Trees | 0.020-1.000 | 1.000-1.000 |
| PGDL semi-synthetic | Extra Trees | 0.020-1.000 | 1.000-1.000 |
| PGDL semi-synthetic | polynomial degree 6 + pairwise interactions | 0.000-0.020 | 0.970-1.000 |

## Real-Data Baseline Check

The PGDL metadata floor contains 24 frozen task-by-nuisance fits. Final training loss is increment-supported in 0; 6 fits show residual dependence without interval-supported predictive improvement. This is a baseline diagnostic only and does not evaluate the checkpoint-derived metric battery.

## Shared Comparator Benchmark

Across 50 balanced-factorial repetitions, corrected interaction MBE supported known design/interaction proxies in at most 4.0% of repetitions and recovered the stable increment in 96.0%. Raw and conditional descriptive scores often remained high for proxies, confirming that the methods answer different questions rather than defining one universal ranking.

## Refit-Aware Inference

In the initial 20-repetition full-refit grid, null/proxy strict support was at most 0.0% and stable-signal recovery was 100.0%. A separate 500-repetition block-permutation null rejected 7.2%, so block-aware inference remains provisional rather than calibrated at nominal 5%.

## What This Changes

Degree 2 and the tested Extra Trees configuration are documented failure controls and cannot support primary MBE conclusions. Primary real-metric reporting must show every preregistered eligible nuisance learner, repeated cross-fitting, adjusted residual evidence, and interval-supported predictive improvement. Learner disagreement is a result, not permission to select the favorable model.

## Remaining Gates

- calibrate the implemented refit bootstrap and block permutation across broader dependence structures;
- expand the shared CMI/granulated benchmark and add a formally calibrated conditional-independence comparator;
- complete PGDL Tasks 1-2 real metric extraction;
- freeze and execute Tasks 4-5 validation and Tasks 6-9 transfer once;
- run prospective selection and independent replication.
