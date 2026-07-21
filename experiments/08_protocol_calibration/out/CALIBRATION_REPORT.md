# MBE Protocol Calibration

These synthetic cases have known data-generating structure. Passing means the declared audit profile matched that structure under the frozen thresholds; it does not validate MBE on real model populations.

| Scenario | Expected profile | Raw rho | Partial rho | Cross-fit residual rho | Delta MSE | Pass |
|---|---|---:|---:|---:|---:|---|
| null_metric | no-increment | -0.026 | -0.029 | -0.101 | 0.0000 | yes |
| linear_proxy | proxy-washout | 0.889 | -0.013 | -0.012 | -0.0003 | yes |
| nonlinear_proxy | nonlinear-proxy-washout | 0.942 | 0.942 | -0.115 | 0.0001 | yes |
| genuine_increment | increment-survives | 0.724 | 0.874 | 0.831 | 0.0415 | yes |
| heteroskedastic_null | conditional-null | -0.103 | -0.034 | -0.053 | -0.0001 | yes |
| clustered_null | conditional-null | 0.795 | 0.007 | 0.013 | -0.0004 | yes |
| simpson_increment | increment-after-environment-control | -0.427 | 0.804 | 0.811 | 0.0161 | yes |
| post_treatment_control | estimand-warning | 0.900 | 0.018 | 0.028 | -0.0002 | yes |

The nonlinear-proxy case is intentionally diagnostic: linear partial ranks retain a false signal, while the cross-fitted polynomial nuisance model should remove it. The post-treatment case is an estimand warning, not evidence that the original metric has no total effect.
