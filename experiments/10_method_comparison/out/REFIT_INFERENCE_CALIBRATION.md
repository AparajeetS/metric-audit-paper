# Refit And Block-Aware Inference Calibration

The full refit bootstrap uses 39 configuration resamples in each of 20 repetitions per scenario. The block-permutation null uses 500 repetitions and rejects in 7.2%.

| Scenario | Expected increment | Strict refit support rate | Median Delta MSE | Median refit lower CI |
|---|---:|---:|---:|---:|
| clustered_null | false | 0.000 | -0.0036 | -0.0151 |
| genuine_increment | true | 1.000 | 0.0404 | 0.0301 |
| nonlinear_proxy | false | 0.000 | -0.0002 | -0.0006 |
| null_metric | false | 0.000 | -0.0011 | -0.0022 |

This is an initial finite calibration, not a general coverage guarantee. More dependence structures and bootstrap sizes remain required.
