# Shared Method Comparison

This benchmark uses known-truth balanced factorial ledgers. Scores answer different questions; CMI and rank coefficients are descriptive and are not thresholded as hypothesis tests.

| Scenario | True stable increment | Raw rho | Partial rho | Granulated tau | Jiang CMI | Additive MBE support | Interaction MBE support |
|---|---:|---:|---:|---:|---:|---:|---:|
| independent_null | false | -0.004 | -0.007 | -0.025 | 0.006 | 0.000 | 0.040 |
| design_proxy | false | 0.977 | 0.622 | 0.778 | 0.418 | 0.680 | 0.040 |
| interaction_proxy | false | 0.759 | 0.385 | 0.432 | 0.158 | 0.880 | 0.020 |
| genuine_increment | true | 0.587 | 0.795 | 0.556 | 0.129 | 0.920 | 0.960 |
| axis_specialist_proxy | false | 0.831 | -0.004 | 0.333 | 0.028 | 0.000 | 0.000 |
| sign_flip_increment | false | -0.081 | -0.085 | -0.074 | 0.006 | 0.020 | 0.100 |

The source-faithful robust sign-error statistic is compared with MBE on the Dziugaite et al. public ledger rather than relabeled for this synthetic design. See `../09_published_metric_reaudit/studies/dziugaite2020/out/SOURCE_REPRODUCTION.md`.
