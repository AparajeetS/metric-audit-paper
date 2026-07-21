# PGDL Semi-Synthetic Calibration

This experiment preserves the real Tasks 1-2 sample sizes and hyperparameter geometry while injecting metrics whose role is known by construction. It uses no protected PGDL metric outputs.

| Scope | Case | Expected signal | Nuisance | Degree | n | Repetitions | Joint decision [95% CI] | Sign correct | Median residual rho | Median Delta MSE |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| balanced_pool | `opposite_sign_task_specialists` | heterogeneous | polynomial_ridge_interactions | 6 | 108 | 100 | 0.040 [0.016, 0.098] | 1.000 | -0.017 | 0.0592 |
| task1 | `injected_increment` | True | polynomial_ridge_interactions | 6 | 96 | 100 | 1.000 [0.963, 1.000] | 1.000 | 0.830 | 0.0328 |
| task1 | `real_design_proxy` | False | polynomial_ridge_interactions | 6 | 96 | 100 | 0.020 [0.006, 0.070] | 1.000 | 0.202 | -0.0031 |
| task1 | `real_structure_null` | False | polynomial_ridge_interactions | 6 | 96 | 100 | 0.000 [0.000, 0.037] | 1.000 | 0.031 | -0.0011 |
| task1 | `task_specialist` | True | polynomial_ridge_interactions | 6 | 96 | 100 | 1.000 [0.963, 1.000] | 1.000 | 0.905 | 0.0776 |
| task2 | `injected_increment` | True | polynomial_ridge_interactions | 6 | 54 | 100 | 0.970 [0.915, 0.990] | 1.000 | 0.843 | 0.0348 |
| task2 | `real_design_proxy` | False | polynomial_ridge_interactions | 6 | 54 | 100 | 0.000 [0.000, 0.037] | 1.000 | 0.189 | -0.0053 |
| task2 | `real_structure_null` | False | polynomial_ridge_interactions | 6 | 54 | 100 | 0.010 [0.002, 0.054] | 1.000 | 0.012 | -0.0009 |
| task2 | `task_specialist` | True | polynomial_ridge_interactions | 6 | 54 | 100 | 1.000 [0.963, 1.000] | 1.000 | -0.902 | 0.0795 |

The joint decision requires a residual permutation p-value at or below 0.050 and a 95% out-of-fold Delta-MSE interval entirely above zero. The balanced pooled specialist case deliberately combines opposite task-specific directions; it is a heterogeneity diagnostic, not a conditional-null false-positive test.

These results validate behavior on the observed design distribution, not on unseen checkpoint metrics. They cannot substitute for Tasks 4-5 validation or Tasks 6-9 protected transfer.
