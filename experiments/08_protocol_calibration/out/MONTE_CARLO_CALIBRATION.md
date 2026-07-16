# Repeated MBE Calibration

This is a repeated-simulation calibration of the compact polynomial-ridge MBE reference implementation. Conditional-null rows report empirical false-positive behavior; conditional-signal rows report power. The joint decision requires both a residual permutation rejection and a 95% out-of-fold Delta-MSE interval entirely above zero.

| Scenario | Signal expected | Nuisance | n | Degree | Repetitions | Legacy reject | Cross-fit reject [95% CI] | Joint decision [95% CI] | Median Delta MSE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| `clustered_null` | false | polynomial_ridge | 150 | 2 | 100 | 0.360 | 0.070 [0.034, 0.137] | 0.000 [0.000, 0.037] | -0.0009 |
| `clustered_null` | false | polynomial_ridge | 150 | 4 | 100 | 0.290 | 0.110 [0.063, 0.186] | 0.010 [0.002, 0.054] | -0.0018 |
| `clustered_null` | false | polynomial_ridge | 150 | 6 | 100 | 0.370 | 0.070 [0.034, 0.137] | 0.000 [0.000, 0.037] | -0.0043 |
| `clustered_null` | false | polynomial_ridge | 300 | 2 | 100 | 0.330 | 0.090 [0.048, 0.162] | 0.000 [0.000, 0.037] | -0.0007 |
| `clustered_null` | false | polynomial_ridge | 300 | 4 | 100 | 0.390 | 0.020 [0.006, 0.070] | 0.000 [0.000, 0.037] | -0.0010 |
| `clustered_null` | false | polynomial_ridge | 300 | 6 | 100 | 0.330 | 0.100 [0.055, 0.174] | 0.000 [0.000, 0.037] | -0.0017 |
| `clustered_null` | false | polynomial_ridge | 600 | 2 | 100 | 0.460 | 0.140 [0.085, 0.221] | 0.000 [0.000, 0.037] | -0.0003 |
| `clustered_null` | false | polynomial_ridge | 600 | 4 | 100 | 0.440 | 0.060 [0.028, 0.125] | 0.000 [0.000, 0.037] | -0.0006 |
| `clustered_null` | false | polynomial_ridge | 600 | 6 | 100 | 0.370 | 0.050 [0.022, 0.112] | 0.000 [0.000, 0.037] | -0.0006 |
| `genuine_increment` | true | polynomial_ridge | 150 | 2 | 100 | 1.000 | 1.000 [0.963, 1.000] | 1.000 [0.963, 1.000] | 0.0400 |
| `genuine_increment` | true | polynomial_ridge | 150 | 4 | 100 | 1.000 | 1.000 [0.963, 1.000] | 1.000 [0.963, 1.000] | 0.0418 |
| `genuine_increment` | true | polynomial_ridge | 150 | 6 | 100 | 1.000 | 1.000 [0.963, 1.000] | 1.000 [0.963, 1.000] | 0.0433 |
| `genuine_increment` | true | polynomial_ridge | 300 | 2 | 100 | 1.000 | 1.000 [0.963, 1.000] | 1.000 [0.963, 1.000] | 0.0413 |
| `genuine_increment` | true | polynomial_ridge | 300 | 4 | 100 | 1.000 | 1.000 [0.963, 1.000] | 1.000 [0.963, 1.000] | 0.0422 |
| `genuine_increment` | true | polynomial_ridge | 300 | 6 | 100 | 1.000 | 1.000 [0.963, 1.000] | 1.000 [0.963, 1.000] | 0.0418 |
| `genuine_increment` | true | polynomial_ridge | 600 | 2 | 100 | 1.000 | 1.000 [0.963, 1.000] | 1.000 [0.963, 1.000] | 0.0403 |
| `genuine_increment` | true | polynomial_ridge | 600 | 4 | 100 | 1.000 | 1.000 [0.963, 1.000] | 1.000 [0.963, 1.000] | 0.0412 |
| `genuine_increment` | true | polynomial_ridge | 600 | 6 | 100 | 1.000 | 1.000 [0.963, 1.000] | 1.000 [0.963, 1.000] | 0.0417 |
| `heteroskedastic_null` | false | polynomial_ridge | 150 | 2 | 100 | 0.210 | 0.140 [0.085, 0.221] | 0.040 [0.016, 0.098] | 0.0003 |
| `heteroskedastic_null` | false | polynomial_ridge | 150 | 4 | 100 | 0.190 | 0.110 [0.063, 0.186] | 0.000 [0.000, 0.037] | -0.0003 |
| `heteroskedastic_null` | false | polynomial_ridge | 150 | 6 | 100 | 0.230 | 0.060 [0.028, 0.125] | 0.000 [0.000, 0.037] | -0.0004 |
| `heteroskedastic_null` | false | polynomial_ridge | 300 | 2 | 100 | 0.350 | 0.200 [0.133, 0.289] | 0.140 [0.085, 0.221] | 0.0005 |
| `heteroskedastic_null` | false | polynomial_ridge | 300 | 4 | 100 | 0.320 | 0.060 [0.028, 0.125] | 0.000 [0.000, 0.037] | -0.0001 |
| `heteroskedastic_null` | false | polynomial_ridge | 300 | 6 | 100 | 0.320 | 0.020 [0.006, 0.070] | 0.000 [0.000, 0.037] | -0.0002 |
| `heteroskedastic_null` | false | polynomial_ridge | 600 | 2 | 100 | 0.370 | 0.130 [0.078, 0.210] | 0.110 [0.063, 0.186] | 0.0005 |
| `heteroskedastic_null` | false | polynomial_ridge | 600 | 4 | 100 | 0.490 | 0.070 [0.034, 0.137] | 0.000 [0.000, 0.037] | -0.0001 |
| `heteroskedastic_null` | false | polynomial_ridge | 600 | 6 | 100 | 0.470 | 0.040 [0.016, 0.098] | 0.000 [0.000, 0.037] | -0.0001 |
| `linear_proxy` | false | polynomial_ridge | 150 | 2 | 100 | 0.090 | 0.070 [0.034, 0.137] | 0.000 [0.000, 0.037] | -0.0002 |
| `linear_proxy` | false | polynomial_ridge | 150 | 4 | 100 | 0.050 | 0.080 [0.041, 0.150] | 0.000 [0.000, 0.037] | -0.0005 |
| `linear_proxy` | false | polynomial_ridge | 150 | 6 | 100 | 0.100 | 0.080 [0.041, 0.150] | 0.000 [0.000, 0.037] | -0.0008 |
| `linear_proxy` | false | polynomial_ridge | 300 | 2 | 100 | 0.090 | 0.060 [0.028, 0.125] | 0.000 [0.000, 0.037] | -0.0001 |
| `linear_proxy` | false | polynomial_ridge | 300 | 4 | 100 | 0.050 | 0.050 [0.022, 0.112] | 0.000 [0.000, 0.037] | -0.0003 |
| `linear_proxy` | false | polynomial_ridge | 300 | 6 | 100 | 0.040 | 0.100 [0.055, 0.174] | 0.000 [0.000, 0.037] | -0.0004 |
| `linear_proxy` | false | polynomial_ridge | 600 | 2 | 100 | 0.050 | 0.050 [0.022, 0.112] | 0.000 [0.000, 0.037] | -0.0001 |
| `linear_proxy` | false | polynomial_ridge | 600 | 4 | 100 | 0.040 | 0.060 [0.028, 0.125] | 0.000 [0.000, 0.037] | -0.0001 |
| `linear_proxy` | false | polynomial_ridge | 600 | 6 | 100 | 0.060 | 0.040 [0.016, 0.098] | 0.000 [0.000, 0.037] | -0.0002 |
| `nonlinear_proxy` | false | polynomial_ridge | 150 | 2 | 100 | 1.000 | 0.790 [0.700, 0.858] | 0.730 [0.636, 0.807] | 0.0028 |
| `nonlinear_proxy` | false | polynomial_ridge | 150 | 4 | 100 | 1.000 | 0.150 [0.093, 0.233] | 0.050 [0.022, 0.112] | 0.0002 |
| `nonlinear_proxy` | false | polynomial_ridge | 150 | 6 | 100 | 1.000 | 0.130 [0.078, 0.210] | 0.010 [0.002, 0.054] | -0.0002 |
| `nonlinear_proxy` | false | polynomial_ridge | 300 | 2 | 100 | 1.000 | 0.920 [0.850, 0.959] | 0.920 [0.850, 0.959] | 0.0026 |
| `nonlinear_proxy` | false | polynomial_ridge | 300 | 4 | 100 | 1.000 | 0.150 [0.093, 0.233] | 0.030 [0.010, 0.085] | 0.0001 |
| `nonlinear_proxy` | false | polynomial_ridge | 300 | 6 | 100 | 1.000 | 0.030 [0.010, 0.085] | 0.000 [0.000, 0.037] | -0.0001 |
| `nonlinear_proxy` | false | polynomial_ridge | 600 | 2 | 100 | 1.000 | 1.000 [0.963, 1.000] | 1.000 [0.963, 1.000] | 0.0024 |
| `nonlinear_proxy` | false | polynomial_ridge | 600 | 4 | 100 | 1.000 | 0.310 [0.228, 0.406] | 0.110 [0.063, 0.186] | 0.0001 |
| `nonlinear_proxy` | false | polynomial_ridge | 600 | 6 | 100 | 1.000 | 0.090 [0.048, 0.162] | 0.000 [0.000, 0.037] | -0.0000 |
| `null_metric` | false | polynomial_ridge | 150 | 2 | 100 | 0.060 | 0.050 [0.022, 0.112] | 0.000 [0.000, 0.037] | -0.0004 |
| `null_metric` | false | polynomial_ridge | 150 | 4 | 100 | 0.040 | 0.050 [0.022, 0.112] | 0.000 [0.000, 0.037] | -0.0007 |
| `null_metric` | false | polynomial_ridge | 150 | 6 | 100 | 0.020 | 0.040 [0.016, 0.098] | 0.000 [0.000, 0.037] | -0.0013 |
| `null_metric` | false | polynomial_ridge | 300 | 2 | 100 | 0.100 | 0.090 [0.048, 0.162] | 0.000 [0.000, 0.037] | -0.0002 |
| `null_metric` | false | polynomial_ridge | 300 | 4 | 100 | 0.100 | 0.090 [0.048, 0.162] | 0.000 [0.000, 0.037] | -0.0004 |
| `null_metric` | false | polynomial_ridge | 300 | 6 | 100 | 0.060 | 0.040 [0.016, 0.098] | 0.000 [0.000, 0.037] | -0.0005 |
| `null_metric` | false | polynomial_ridge | 600 | 2 | 100 | 0.060 | 0.040 [0.016, 0.098] | 0.000 [0.000, 0.037] | -0.0001 |
| `null_metric` | false | polynomial_ridge | 600 | 4 | 100 | 0.060 | 0.090 [0.048, 0.162] | 0.000 [0.000, 0.037] | -0.0002 |
| `null_metric` | false | polynomial_ridge | 600 | 6 | 100 | 0.060 | 0.040 [0.016, 0.098] | 0.000 [0.000, 0.037] | -0.0002 |
| `post_treatment_control` | false | polynomial_ridge | 150 | 2 | 100 | 0.080 | 0.060 [0.028, 0.125] | 0.000 [0.000, 0.037] | -0.0002 |
| `post_treatment_control` | false | polynomial_ridge | 150 | 4 | 100 | 0.090 | 0.070 [0.034, 0.137] | 0.000 [0.000, 0.037] | -0.0004 |
| `post_treatment_control` | false | polynomial_ridge | 150 | 6 | 100 | 0.100 | 0.020 [0.006, 0.070] | 0.000 [0.000, 0.037] | -0.0006 |
| `post_treatment_control` | false | polynomial_ridge | 300 | 2 | 100 | 0.040 | 0.060 [0.028, 0.125] | 0.000 [0.000, 0.037] | -0.0001 |
| `post_treatment_control` | false | polynomial_ridge | 300 | 4 | 100 | 0.040 | 0.030 [0.010, 0.085] | 0.000 [0.000, 0.037] | -0.0002 |
| `post_treatment_control` | false | polynomial_ridge | 300 | 6 | 100 | 0.070 | 0.060 [0.028, 0.125] | 0.000 [0.000, 0.037] | -0.0002 |
| `post_treatment_control` | false | polynomial_ridge | 600 | 2 | 100 | 0.060 | 0.040 [0.016, 0.098] | 0.000 [0.000, 0.037] | -0.0001 |
| `post_treatment_control` | false | polynomial_ridge | 600 | 4 | 100 | 0.050 | 0.040 [0.016, 0.098] | 0.000 [0.000, 0.037] | -0.0001 |
| `post_treatment_control` | false | polynomial_ridge | 600 | 6 | 100 | 0.110 | 0.040 [0.016, 0.098] | 0.000 [0.000, 0.037] | -0.0001 |
| `simpson_increment` | true | polynomial_ridge | 150 | 2 | 100 | 1.000 | 1.000 [0.963, 1.000] | 1.000 [0.963, 1.000] | 0.0161 |
| `simpson_increment` | true | polynomial_ridge | 150 | 4 | 100 | 1.000 | 1.000 [0.963, 1.000] | 1.000 [0.963, 1.000] | 0.0167 |
| `simpson_increment` | true | polynomial_ridge | 150 | 6 | 100 | 1.000 | 1.000 [0.963, 1.000] | 1.000 [0.963, 1.000] | 0.0172 |
| `simpson_increment` | true | polynomial_ridge | 300 | 2 | 100 | 1.000 | 1.000 [0.963, 1.000] | 1.000 [0.963, 1.000] | 0.0161 |
| `simpson_increment` | true | polynomial_ridge | 300 | 4 | 100 | 1.000 | 1.000 [0.963, 1.000] | 1.000 [0.963, 1.000] | 0.0169 |
| `simpson_increment` | true | polynomial_ridge | 300 | 6 | 100 | 1.000 | 1.000 [0.963, 1.000] | 1.000 [0.963, 1.000] | 0.0170 |
| `simpson_increment` | true | polynomial_ridge | 600 | 2 | 100 | 1.000 | 1.000 [0.963, 1.000] | 1.000 [0.963, 1.000] | 0.0160 |
| `simpson_increment` | true | polynomial_ridge | 600 | 4 | 100 | 1.000 | 1.000 [0.963, 1.000] | 1.000 [0.963, 1.000] | 0.0168 |
| `simpson_increment` | true | polynomial_ridge | 600 | 6 | 100 | 1.000 | 1.000 [0.963, 1.000] | 1.000 [0.963, 1.000] | 0.0168 |

## Reading The Table

The nominal residual-test level is 0.050. A low null rejection rate supports calibration only for the simulated nuisance structures; it does not prove conditional independence testing is universally valid. Power must be interpreted together with sample size and nuisance degree.

Across the displayed grid, conditional-null cross-fit rejection ranges from 0.020 to 1.000; conditional-signal joint detection ranges from 1.000 to 1.000.

The post-treatment scenario is a conditional null for the direct-information estimand after controlling the mediator. Its raw association is real; loss of conditional signal is not a causal verdict.

This report calibrates one reference nuisance model. Submission evidence must add alternative nuisance learners, semi-synthetic real-design tests, and held-out task-family prediction.
