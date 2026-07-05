# No-Compute Uncertainty And Sensitivity

This report uses only saved Kaggle result CSVs. No model training is run.

- Bootstrap resamples per metric/run: `200`
- Bootstrap unit: row/model run
- Target: `final_acc`
- Default controls: `lr, wd, dropout, optimizer, arch, task, seed`
- Strict controls: default controls plus `val_loss`

## Headline Bootstrap CIs

| Run | Metric | n | Raw rho, 95% CI | MBE partial rho, 95% CI | Delta, 95% CI | Class |
|---|---|---:|---:|---:|---:|---|
| image_480_default | `fim_norm` | 480 | -0.662 [-0.707, -0.599] | -0.218 [-0.295, -0.115] | +0.444 [+0.351, +0.557] | survives |
| image_480_default | `val_loss` | 480 | -0.822 [-0.845, -0.794] | -0.730 [-0.774, -0.671] | +0.091 [+0.052, +0.143] | survives |
| image_480_default | `fisher_trace` | 480 | -0.475 [-0.548, -0.401] | -0.180 [-0.310, -0.038] | +0.295 [+0.198, +0.419] | weak-or-mixed |
| image_480_default | `grad_norm` | 480 | -0.476 [-0.549, -0.381] | -0.200 [-0.325, -0.093] | +0.275 [+0.169, +0.398] | survives |
| image_480_default | `confidence_mean` | 480 | +0.720 [+0.674, +0.760] | +0.315 [+0.214, +0.422] | -0.405 [-0.506, -0.303] | survives |
| image_480_default | `feature_norm_mean` | 480 | +0.539 [+0.475, +0.598] | +0.254 [+0.090, +0.381] | -0.285 [-0.440, -0.144] | survives |
| image_480_default | `feature_erank` | 480 | -0.424 [-0.488, -0.344] | +0.199 [+0.101, +0.285] | +0.623 [+0.494, +0.717] | weak-or-mixed |
| image_480_default | `weight_l2` | 480 | +0.128 [+0.036, +0.226] | +0.122 [-0.007, +0.265] | -0.006 [-0.169, +0.131] | weak-or-mixed |
| image_480_default | `distance_from_init_l2` | 480 | +0.438 [+0.352, +0.507] | +0.148 [+0.063, +0.253] | -0.290 [-0.409, -0.173] | weak-or-mixed |
| image_480_default | `update_to_weight_ratio` | 480 | +0.404 [+0.316, +0.468] | +0.020 [-0.096, +0.151] | -0.384 [-0.492, -0.245] | washout |
| image_480_default | `random_metric` | 480 | -0.013 [-0.090, +0.078] | -0.070 [-0.155, +0.009] | -0.057 [-0.175, +0.030] | weak-or-mixed |
| image_480_strict | `fim_norm` | 480 | -0.662 [-0.709, -0.608] | -0.383 [-0.460, -0.278] | +0.279 [+0.178, +0.399] | survives |
| image_480_strict | `val_loss` | 480 | -0.822 [-0.849, -0.793] | -0.730 [-0.781, -0.655] | +0.091 [+0.048, +0.162] | survives |
| image_480_strict | `fisher_trace` | 480 | -0.475 [-0.536, -0.410] | -0.359 [-0.445, -0.247] | +0.116 [+0.012, +0.235] | survives |
| image_480_strict | `grad_norm` | 480 | -0.476 [-0.545, -0.403] | -0.350 [-0.449, -0.234] | +0.126 [+0.021, +0.237] | survives |
| image_480_strict | `confidence_mean` | 480 | +0.720 [+0.676, +0.769] | +0.503 [+0.417, +0.586] | -0.217 [-0.323, -0.126] | survives |
| image_480_strict | `feature_norm_mean` | 480 | +0.539 [+0.473, +0.592] | +0.348 [+0.214, +0.452] | -0.191 [-0.329, -0.079] | survives |
| image_480_strict | `feature_erank` | 480 | -0.424 [-0.499, -0.344] | +0.228 [+0.113, +0.342] | +0.652 [+0.511, +0.762] | sign-inversion |
| image_480_strict | `weight_l2` | 480 | +0.128 [+0.041, +0.227] | +0.215 [+0.090, +0.322] | +0.088 [-0.052, +0.208] | hidden-after-control |
| image_480_strict | `distance_from_init_l2` | 480 | +0.438 [+0.349, +0.504] | +0.325 [+0.221, +0.417] | -0.113 [-0.248, +0.014] | survives |
| image_480_strict | `update_to_weight_ratio` | 480 | +0.404 [+0.327, +0.479] | +0.185 [+0.077, +0.316] | -0.220 [-0.332, -0.085] | weak-or-mixed |
| image_480_strict | `random_metric` | 480 | -0.013 [-0.092, +0.071] | -0.016 [-0.114, +0.079] | -0.002 [-0.106, +0.102] | weak-or-mixed |
| text_200_default | `fim_norm` | 200 | -0.291 [-0.439, -0.120] | +0.014 [-0.142, +0.173] | +0.305 [+0.148, +0.453] | washout |
| text_200_default | `val_loss` | 200 | -0.930 [-0.954, -0.890] | -0.861 [-0.898, -0.796] | +0.069 [+0.042, +0.109] | survives |
| text_200_default | `fisher_trace` | 200 | -0.818 [-0.853, -0.757] | -0.424 [-0.519, -0.293] | +0.395 [+0.317, +0.495] | survives |
| text_200_default | `grad_norm` | 200 | -0.818 [-0.860, -0.759] | -0.430 [-0.541, -0.285] | +0.388 [+0.297, +0.498] | survives |
| text_200_default | `confidence_mean` | 200 | +0.308 [+0.181, +0.462] | +0.076 [-0.093, +0.230] | -0.231 [-0.392, -0.079] | washout |
| text_200_default | `feature_norm_mean` | 200 | +0.325 [+0.188, +0.431] | -0.240 [-0.385, -0.077] | -0.565 [-0.689, -0.434] | reverse-inversion |
| text_200_default | `feature_erank` | 200 | -0.734 [-0.796, -0.652] | -0.471 [-0.563, -0.353] | +0.263 [+0.183, +0.351] | survives |
| text_200_default | `weight_l2` | 200 | +0.708 [+0.647, +0.757] | +0.023 [-0.081, +0.110] | -0.685 [-0.761, -0.612] | washout |
| text_200_default | `distance_from_init_l2` | 200 | +0.752 [+0.695, +0.798] | +0.198 [+0.045, +0.314] | -0.553 [-0.697, -0.442] | weak-or-mixed |
| text_200_default | `update_to_weight_ratio` | 200 | +0.752 [+0.692, +0.798] | +0.176 [+0.048, +0.301] | -0.575 [-0.695, -0.451] | weak-or-mixed |
| text_200_default | `random_metric` | 200 | +0.068 [-0.059, +0.208] | +0.009 [-0.120, +0.148] | -0.059 [-0.182, +0.055] | weak-or-mixed |
| text_200_strict | `fim_norm` | 200 | -0.291 [-0.424, -0.139] | +0.188 [+0.046, +0.300] | +0.479 [+0.310, +0.655] | weak-or-mixed |
| text_200_strict | `val_loss` | 200 | -0.930 [-0.953, -0.895] | -0.861 [-0.905, -0.796] | +0.069 [+0.042, +0.111] | survives |
| text_200_strict | `fisher_trace` | 200 | -0.818 [-0.855, -0.765] | -0.295 [-0.410, -0.155] | +0.524 [+0.429, +0.637] | survives |
| text_200_strict | `grad_norm` | 200 | -0.818 [-0.855, -0.754] | -0.325 [-0.425, -0.171] | +0.493 [+0.400, +0.622] | survives |
| text_200_strict | `confidence_mean` | 200 | +0.308 [+0.150, +0.455] | -0.049 [-0.205, +0.132] | -0.357 [-0.514, -0.147] | washout |
| text_200_strict | `feature_norm_mean` | 200 | +0.325 [+0.221, +0.424] | -0.152 [-0.294, +0.008] | -0.477 [-0.643, -0.293] | weak-or-mixed |
| text_200_strict | `feature_erank` | 200 | -0.734 [-0.797, -0.660] | -0.312 [-0.448, -0.173] | +0.422 [+0.299, +0.544] | survives |
| text_200_strict | `weight_l2` | 200 | +0.708 [+0.647, +0.759] | +0.131 [+0.040, +0.209] | -0.577 [-0.661, -0.486] | weak-or-mixed |
| text_200_strict | `distance_from_init_l2` | 200 | +0.752 [+0.695, +0.800] | +0.254 [+0.122, +0.349] | -0.498 [-0.612, -0.415] | survives |
| text_200_strict | `update_to_weight_ratio` | 200 | +0.752 [+0.689, +0.798] | +0.235 [+0.102, +0.335] | -0.517 [-0.632, -0.422] | survives |
| text_200_strict | `random_metric` | 200 | +0.068 [-0.081, +0.218] | -0.042 [-0.179, +0.087] | -0.110 [-0.256, +0.053] | weak-or-mixed |
| full_680_default | `fim_norm` | 680 | +0.225 [+0.136, +0.314] | -0.203 [-0.267, -0.117] | -0.428 [-0.539, -0.320] | reverse-inversion |
| full_680_default | `val_loss` | 680 | -0.935 [-0.945, -0.920] | -0.698 [-0.735, -0.624] | +0.238 [+0.200, +0.310] | survives |
| full_680_default | `fisher_trace` | 680 | -0.809 [-0.842, -0.773] | -0.211 [-0.320, -0.103] | +0.598 [+0.492, +0.707] | survives |
| full_680_default | `grad_norm` | 680 | -0.809 [-0.837, -0.773] | -0.227 [-0.329, -0.086] | +0.582 [+0.483, +0.701] | survives |
| full_680_default | `confidence_mean` | 680 | +0.833 [+0.813, +0.852] | +0.339 [+0.259, +0.418] | -0.494 [-0.588, -0.411] | survives |
| full_680_default | `feature_norm_mean` | 680 | -0.425 [-0.500, -0.346] | +0.071 [-0.048, +0.190] | +0.496 [+0.349, +0.612] | washout |
| full_680_default | `feature_erank` | 680 | -0.538 [-0.605, -0.469] | +0.097 [-0.014, +0.183] | +0.635 [+0.515, +0.733] | washout |
| full_680_default | `weight_l2` | 680 | +0.685 [+0.625, +0.740] | +0.093 [-0.012, +0.199] | -0.592 [-0.726, -0.453] | washout |
| full_680_default | `distance_from_init_l2` | 680 | +0.672 [+0.617, +0.723] | +0.014 [-0.072, +0.120] | -0.658 [-0.765, -0.544] | washout |
| full_680_default | `update_to_weight_ratio` | 680 | +0.241 [+0.168, +0.316] | +0.066 [-0.037, +0.180] | -0.175 [-0.284, -0.049] | washout |
| full_680_default | `random_metric` | 680 | -0.035 [-0.112, +0.033] | -0.062 [-0.131, +0.018] | -0.027 [-0.120, +0.073] | weak-or-mixed |
| full_680_strict | `fim_norm` | 680 | +0.225 [+0.138, +0.296] | -0.300 [-0.389, -0.217] | -0.525 [-0.621, -0.421] | reverse-inversion |
| full_680_strict | `val_loss` | 680 | -0.935 [-0.947, -0.921] | -0.698 [-0.742, -0.647] | +0.238 [+0.198, +0.286] | survives |
| full_680_strict | `fisher_trace` | 680 | -0.809 [-0.841, -0.768] | -0.390 [-0.482, -0.275] | +0.419 [+0.330, +0.522] | survives |
| full_680_strict | `grad_norm` | 680 | -0.809 [-0.843, -0.765] | -0.376 [-0.470, -0.261] | +0.433 [+0.347, +0.528] | survives |
| full_680_strict | `confidence_mean` | 680 | +0.833 [+0.807, +0.850] | +0.536 [+0.464, +0.586] | -0.297 [-0.369, -0.238] | survives |
| full_680_strict | `feature_norm_mean` | 680 | -0.425 [-0.498, -0.352] | +0.069 [-0.055, +0.185] | +0.494 [+0.379, +0.597] | washout |
| full_680_strict | `feature_erank` | 680 | -0.538 [-0.603, -0.476] | +0.108 [-0.007, +0.202] | +0.646 [+0.535, +0.748] | weak-or-mixed |
| full_680_strict | `weight_l2` | 680 | +0.685 [+0.612, +0.737] | +0.185 [+0.108, +0.277] | -0.501 [-0.596, -0.385] | weak-or-mixed |
| full_680_strict | `distance_from_init_l2` | 680 | +0.672 [+0.611, +0.725] | +0.284 [+0.184, +0.378] | -0.388 [-0.475, -0.294] | survives |
| full_680_strict | `update_to_weight_ratio` | 680 | +0.241 [+0.182, +0.309] | +0.253 [+0.155, +0.351] | +0.012 [-0.088, +0.140] | survives |
| full_680_strict | `random_metric` | 680 | -0.035 [-0.118, +0.032] | -0.044 [-0.115, +0.031] | -0.010 [-0.101, +0.080] | weak-or-mixed |

## Default-Threshold Class Counts

The default threshold is `effect_threshold=0.20`, `washout_threshold=0.10`.

| Run | Survives | Washout | Sign inv. | Reverse inv. | Hidden | Weak/mixed |
|---|---:|---:|---:|---:|---:|---:|
| image_480_default | 21 | 3 | 0 | 0 | 1 | 16 |
| image_480_strict | 29 | 1 | 2 | 0 | 4 | 4 |
| text_200_default | 15 | 12 | 0 | 1 | 1 | 10 |
| text_200_strict | 15 | 7 | 0 | 1 | 0 | 15 |
| full_680_default | 19 | 7 | 0 | 1 | 2 | 12 |
| full_680_strict | 26 | 4 | 0 | 1 | 3 | 6 |

## Sensitivity Read

- The current headline story should be read as threshold-sensitive until a locked replication is run.
- The key qualitative question is whether fragile families remain fragile across nearby thresholds.
- Inversions are reported separately from washout because they indicate sign reversal, not just collapse.
