# PGDL Metadata Baseline Floor

This table measures final training loss beyond each task's declared hyperparameters. It contains no checkpoint-derived metric results and does not open the protected holdout metric evaluation.

| Task | Split | Nuisance | Degree | n | Hyperparameter MSE | + train-loss MSE | Delta MSE [95% CI] | Residual rho [95% CI] | Evidence |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| task1 | development | polynomial_ridge | 4 | 96 | 0.0128 | 0.0124 | 0.0004 [-0.0010, 0.0021] | 0.020 [-0.155, 0.215] | no-supported-increment |
| task1 | development | polynomial_ridge | 6 | 96 | 0.0157 | 0.0155 | 0.0001 [-0.0016, 0.0021] | 0.068 [-0.096, 0.254] | no-supported-increment |
| task1 | development | polynomial_ridge_interactions | 6 | 96 | 0.0072 | 0.0081 | -0.0009 [-0.0023, 0.0001] | 0.246 [0.062, 0.433] | residual-dependence-only |
| task2 | development | polynomial_ridge | 4 | 54 | 0.0074 | 0.0080 | -0.0006 [-0.0019, 0.0005] | 0.143 [-0.142, 0.399] | no-supported-increment |
| task2 | development | polynomial_ridge | 6 | 54 | 0.0073 | 0.0084 | -0.0011 [-0.0024, 0.0003] | 0.138 [-0.136, 0.396] | no-supported-increment |
| task2 | development | polynomial_ridge_interactions | 6 | 54 | 0.0042 | 0.0048 | -0.0006 [-0.0013, 0.0001] | 0.109 [-0.175, 0.368] | no-supported-increment |
| task4 | validation | polynomial_ridge | 4 | 96 | 0.0185 | 0.0194 | -0.0009 [-0.0036, 0.0014] | 0.105 [-0.116, 0.287] | no-supported-increment |
| task4 | validation | polynomial_ridge | 6 | 96 | 0.0200 | 0.0205 | -0.0005 [-0.0038, 0.0027] | 0.134 [-0.069, 0.312] | no-supported-increment |
| task4 | validation | polynomial_ridge_interactions | 6 | 96 | 0.0170 | 0.0141 | 0.0029 [-0.0009, 0.0067] | 0.057 [-0.154, 0.271] | no-supported-increment |
| task5 | validation | polynomial_ridge | 4 | 64 | 0.0812 | 0.0839 | -0.0027 [-0.0161, 0.0107] | 0.079 [-0.141, 0.301] | no-supported-increment |
| task5 | validation | polynomial_ridge | 6 | 64 | 0.0731 | 0.0713 | 0.0018 [-0.0121, 0.0130] | 0.056 [-0.181, 0.286] | no-supported-increment |
| task5 | validation | polynomial_ridge_interactions | 6 | 64 | 0.0634 | 0.0772 | -0.0137 [-0.0361, 0.0095] | 0.195 [-0.038, 0.443] | no-supported-increment |
| task6 | holdout | polynomial_ridge | 4 | 96 | 0.0122 | 0.0122 | 0.0000 [-0.0017, 0.0017] | -0.110 [-0.292, 0.067] | no-supported-increment |
| task6 | holdout | polynomial_ridge | 6 | 96 | 0.0146 | 0.0138 | 0.0008 [-0.0015, 0.0035] | -0.164 [-0.338, -0.001] | no-supported-increment |
| task6 | holdout | polynomial_ridge_interactions | 6 | 96 | 0.0055 | 0.0061 | -0.0005 [-0.0016, 0.0004] | -0.121 [-0.310, 0.071] | no-supported-increment |
| task7 | holdout | polynomial_ridge | 4 | 48 | 0.0463 | 0.0471 | -0.0009 [-0.0079, 0.0058] | 0.294 [0.010, 0.513] | residual-dependence-only |
| task7 | holdout | polynomial_ridge | 6 | 48 | 0.0511 | 0.0498 | 0.0013 [-0.0078, 0.0107] | 0.435 [0.176, 0.639] | residual-dependence-only |
| task7 | holdout | polynomial_ridge_interactions | 6 | 48 | 0.0461 | 0.0695 | -0.0234 [-0.0504, 0.0012] | 0.504 [0.306, 0.686] | residual-dependence-only |
| task8 | holdout | polynomial_ridge | 4 | 64 | 0.0464 | 0.0474 | -0.0010 [-0.0076, 0.0053] | 0.223 [-0.010, 0.479] | no-supported-increment |
| task8 | holdout | polynomial_ridge | 6 | 64 | 0.0391 | 0.0393 | -0.0001 [-0.0077, 0.0074] | 0.241 [0.011, 0.489] | residual-dependence-only |
| task8 | holdout | polynomial_ridge_interactions | 6 | 64 | 0.0492 | 0.0573 | -0.0081 [-0.0245, 0.0067] | 0.387 [0.166, 0.598] | residual-dependence-only |
| task9 | holdout | polynomial_ridge | 4 | 32 | 0.0157 | 0.0203 | -0.0046 [-0.0112, 0.0010] | 0.194 [-0.151, 0.600] | no-supported-increment |
| task9 | holdout | polynomial_ridge | 6 | 32 | 0.0144 | 0.0163 | -0.0020 [-0.0061, 0.0026] | 0.166 [-0.148, 0.507] | no-supported-increment |
| task9 | holdout | polynomial_ridge_interactions | 6 | 32 | 0.0144 | 0.0210 | -0.0065 [-0.0160, 0.0023] | 0.087 [-0.229, 0.404] | no-supported-increment |

Training accuracy is not tested as a candidate because it is part of the accuracy-gap target. Hyperparameter MSE is an out-of-fold rank-target error, so it is a benchmark floor rather than an estimate in original accuracy units.
