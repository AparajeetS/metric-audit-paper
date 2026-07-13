# JMLR-Scale Metric Audit

- summary csv: `experiments\07_jmlr_scale\jmlr_holdout_image_timeboxed_audit_summary.csv`
- MBE covariates: `lr, wd, dropout, optimizer, arch, task, seed`

## pooled

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 80 | -0.240 | -0.264 | survives |
| brier | 80 | -0.752 | -0.389 | survives |
| confidence_mean | 80 | +0.727 | +0.350 | survives |
| distance_from_init_l2 | 80 | +0.411 | +0.089 | washout |
| ece | 80 | -0.760 | -0.360 | survives |
| entropy_mean | 80 | -0.730 | -0.328 | survives |
| feature_cosine_mean | 80 | +0.187 | -0.190 | weak-or-mixed |
| feature_erank | 80 | -0.374 | +0.374 | sign-inversion |
| feature_erank_norm | 80 | -0.374 | +0.374 | sign-inversion |
| feature_norm_mean | 80 | +0.613 | +0.179 | weak-or-mixed |
| fim_erank | 80 | -0.699 | -0.229 | survives |
| fim_loss_scaled_erank | 80 | +0.328 | +0.128 | weak-or-mixed |
| fim_loss_scaled_norm | 80 | +0.328 | +0.128 | weak-or-mixed |
| fim_norm | 80 | -0.699 | -0.229 | survives |
| fim_unit_erank | 80 | +0.016 | +0.123 | weak-or-mixed |
| fim_unit_norm | 80 | +0.016 | +0.123 | weak-or-mixed |
| fisher_condition | 80 | +0.672 | +0.147 | weak-or-mixed |
| fisher_entropy | 80 | -0.699 | -0.229 | survives |
| fisher_spectral | 80 | -0.583 | -0.211 | survives |
| fisher_stable_rank | 80 | -0.664 | -0.147 | weak-or-mixed |
| fisher_trace | 80 | -0.662 | -0.260 | survives |
| grad_l1 | 80 | -0.546 | -0.286 | survives |
| grad_linf | 80 | -0.583 | -0.186 | weak-or-mixed |
| grad_loss_logcorr | 80 | +0.474 | +0.103 | weak-or-mixed |
| grad_mean_abs | 80 | -0.623 | -0.241 | survives |
| grad_noise_scale | 80 | +0.289 | +0.373 | survives |
| grad_norm | 80 | -0.659 | -0.291 | survives |
| gradient_energy_entropy | 80 | -0.700 | -0.253 | survives |
| gradient_energy_gini | 80 | +0.710 | +0.276 | survives |
| hessian_top_eig_power | 60 | -0.636 | -0.482 | survives |
| hessian_trace_hutchinson | 60 | -0.661 | -0.393 | survives |
| logit_norm_mean | 80 | +0.686 | +0.119 | weak-or-mixed |
| margin_mean | 80 | +0.737 | +0.351 | survives |
| metric_batch_acc | 80 | +0.762 | +0.287 | survives |
| metric_batch_loss | 80 | -0.759 | -0.424 | survives |
| per_sample_grad_norm_mean | 80 | -0.720 | -0.330 | survives |
| per_sample_grad_norm_std | 80 | -0.564 | -0.197 | weak-or-mixed |
| random_metric | 80 | -0.092 | -0.051 | weak-or-mixed |
| relative_distance_from_init | 80 | +0.327 | +0.008 | washout |
| sam_sharpness | 80 | -0.141 | -0.153 | weak-or-mixed |
| train_acc | 80 | +0.786 | +0.491 | survives |
| train_loss | 80 | -0.805 | -0.570 | survives |
| update_to_weight_ratio | 80 | +0.326 | -0.143 | weak-or-mixed |
| val_loss | 80 | -0.822 | -0.738 | survives |
| weight_l1 | 80 | +0.300 | +0.246 | survives |
| weight_l2 | 80 | +0.262 | +0.176 | weak-or-mixed |
| weight_linf | 80 | +0.416 | +0.368 | survives |
| weight_rms | 80 | -0.045 | +0.205 | hidden-after-control |

## suite=image

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 80 | -0.240 | -0.264 | survives |
| brier | 80 | -0.752 | -0.389 | survives |
| confidence_mean | 80 | +0.727 | +0.350 | survives |
| distance_from_init_l2 | 80 | +0.411 | +0.089 | washout |
| ece | 80 | -0.760 | -0.360 | survives |
| entropy_mean | 80 | -0.730 | -0.328 | survives |
| feature_cosine_mean | 80 | +0.187 | -0.190 | weak-or-mixed |
| feature_erank | 80 | -0.374 | +0.374 | sign-inversion |
| feature_erank_norm | 80 | -0.374 | +0.374 | sign-inversion |
| feature_norm_mean | 80 | +0.613 | +0.179 | weak-or-mixed |
| fim_erank | 80 | -0.699 | -0.229 | survives |
| fim_loss_scaled_erank | 80 | +0.328 | +0.128 | weak-or-mixed |
| fim_loss_scaled_norm | 80 | +0.328 | +0.128 | weak-or-mixed |
| fim_norm | 80 | -0.699 | -0.229 | survives |
| fim_unit_erank | 80 | +0.016 | +0.123 | weak-or-mixed |
| fim_unit_norm | 80 | +0.016 | +0.123 | weak-or-mixed |
| fisher_condition | 80 | +0.672 | +0.147 | weak-or-mixed |
| fisher_entropy | 80 | -0.699 | -0.229 | survives |
| fisher_spectral | 80 | -0.583 | -0.211 | survives |
| fisher_stable_rank | 80 | -0.664 | -0.147 | weak-or-mixed |
| fisher_trace | 80 | -0.662 | -0.260 | survives |
| grad_l1 | 80 | -0.546 | -0.286 | survives |
| grad_linf | 80 | -0.583 | -0.186 | weak-or-mixed |
| grad_loss_logcorr | 80 | +0.474 | +0.103 | weak-or-mixed |
| grad_mean_abs | 80 | -0.623 | -0.241 | survives |
| grad_noise_scale | 80 | +0.289 | +0.373 | survives |
| grad_norm | 80 | -0.659 | -0.291 | survives |
| gradient_energy_entropy | 80 | -0.700 | -0.253 | survives |
| gradient_energy_gini | 80 | +0.710 | +0.276 | survives |
| hessian_top_eig_power | 60 | -0.636 | -0.482 | survives |
| hessian_trace_hutchinson | 60 | -0.661 | -0.393 | survives |
| logit_norm_mean | 80 | +0.686 | +0.119 | weak-or-mixed |
| margin_mean | 80 | +0.737 | +0.351 | survives |
| metric_batch_acc | 80 | +0.762 | +0.287 | survives |
| metric_batch_loss | 80 | -0.759 | -0.424 | survives |
| per_sample_grad_norm_mean | 80 | -0.720 | -0.330 | survives |
| per_sample_grad_norm_std | 80 | -0.564 | -0.197 | weak-or-mixed |
| random_metric | 80 | -0.092 | -0.051 | weak-or-mixed |
| relative_distance_from_init | 80 | +0.327 | +0.008 | washout |
| sam_sharpness | 80 | -0.141 | -0.153 | weak-or-mixed |
| train_acc | 80 | +0.786 | +0.491 | survives |
| train_loss | 80 | -0.805 | -0.570 | survives |
| update_to_weight_ratio | 80 | +0.326 | -0.143 | weak-or-mixed |
| val_loss | 80 | -0.822 | -0.738 | survives |
| weight_l1 | 80 | +0.300 | +0.246 | survives |
| weight_l2 | 80 | +0.262 | +0.176 | weak-or-mixed |
| weight_linf | 80 | +0.416 | +0.368 | survives |
| weight_rms | 80 | -0.045 | +0.205 | hidden-after-control |

## arch=cnn

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 20 | -0.256 | -0.358 | survives |
| brier | 20 | -0.445 | -0.575 | survives |
| confidence_mean | 20 | +0.229 | +0.094 | washout |
| distance_from_init_l2 | 20 | +0.244 | -0.179 | weak-or-mixed |
| ece | 20 | -0.502 | -0.495 | survives |
| entropy_mean | 20 | -0.114 | +0.117 | weak-or-mixed |
| feature_cosine_mean | 20 | +0.183 | -0.273 | hidden-after-control |
| feature_erank | 20 | +0.629 | +0.662 | survives |
| feature_erank_norm | 20 | +0.629 | +0.662 | survives |
| feature_norm_mean | 20 | -0.349 | -0.317 | survives |
| fim_erank | 20 | -0.349 | -0.249 | survives |
| fim_loss_scaled_erank | 20 | +0.441 | +0.318 | survives |
| fim_loss_scaled_norm | 20 | +0.441 | +0.318 | survives |
| fim_norm | 20 | -0.349 | -0.249 | survives |
| fim_unit_erank | 20 | +0.197 | +0.028 | weak-or-mixed |
| fim_unit_norm | 20 | +0.197 | +0.028 | weak-or-mixed |
| fisher_condition | 20 | +0.023 | -0.124 | weak-or-mixed |
| fisher_entropy | 20 | -0.349 | -0.249 | survives |
| fisher_spectral | 20 | -0.483 | -0.455 | survives |
| fisher_stable_rank | 20 | -0.323 | -0.138 | weak-or-mixed |
| fisher_trace | 20 | -0.523 | -0.466 | survives |
| grad_l1 | 20 | -0.394 | -0.658 | survives |
| grad_linf | 20 | -0.672 | -0.605 | survives |
| grad_loss_logcorr | 20 | +0.382 | +0.106 | weak-or-mixed |
| grad_mean_abs | 20 | -0.394 | -0.658 | survives |
| grad_noise_scale | 20 | +0.520 | +0.634 | survives |
| grad_norm | 20 | -0.576 | -0.721 | survives |
| gradient_energy_entropy | 20 | -0.474 | -0.393 | survives |
| gradient_energy_gini | 20 | +0.469 | +0.392 | survives |
| hessian_top_eig_power | 20 | -0.380 | +0.155 | weak-or-mixed |
| hessian_trace_hutchinson | 20 | -0.281 | +0.226 | sign-inversion |
| logit_norm_mean | 20 | -0.078 | -0.411 | hidden-after-control |
| margin_mean | 20 | +0.248 | +0.179 | weak-or-mixed |
| metric_batch_acc | 20 | +0.382 | +0.635 | survives |
| metric_batch_loss | 20 | -0.477 | -0.563 | survives |
| per_sample_grad_norm_mean | 20 | -0.603 | -0.441 | survives |
| per_sample_grad_norm_std | 20 | -0.433 | -0.508 | survives |
| random_metric | 20 | +0.039 | +0.076 | weak-or-mixed |
| relative_distance_from_init | 20 | +0.244 | -0.179 | weak-or-mixed |
| sam_sharpness | 20 | -0.498 | -0.353 | survives |
| train_acc | 20 | +0.911 | +0.887 | survives |
| train_loss | 20 | -0.943 | -0.925 | survives |
| update_to_weight_ratio | 20 | +0.048 | -0.584 | hidden-after-control |
| val_loss | 20 | -0.820 | -0.918 | survives |
| weight_l1 | 20 | +0.444 | +0.363 | survives |
| weight_l2 | 20 | +0.405 | +0.319 | survives |
| weight_linf | 20 | +0.406 | +0.275 | survives |
| weight_rms | 20 | +0.405 | +0.319 | survives |

## arch=resnet

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 20 | -0.426 | -0.304 | survives |
| brier | 20 | -0.495 | -0.193 | weak-or-mixed |
| confidence_mean | 20 | +0.528 | +0.345 | survives |
| distance_from_init_l2 | 20 | +0.856 | +0.124 | weak-or-mixed |
| ece | 20 | -0.559 | -0.181 | weak-or-mixed |
| entropy_mean | 20 | -0.543 | -0.309 | survives |
| feature_cosine_mean | 20 | +0.096 | -0.005 | weak-or-mixed |
| feature_erank | 20 | +0.370 | -0.099 | washout |
| feature_erank_norm | 20 | +0.370 | -0.099 | washout |
| feature_norm_mean | 20 | +0.495 | +0.644 | survives |
| fim_erank | 20 | -0.534 | +0.143 | weak-or-mixed |
| fim_loss_scaled_erank | 20 | +0.707 | -0.045 | washout |
| fim_loss_scaled_norm | 20 | +0.707 | -0.045 | washout |
| fim_norm | 20 | -0.534 | +0.143 | weak-or-mixed |
| fim_unit_erank | 20 | +0.638 | -0.076 | washout |
| fim_unit_norm | 20 | +0.638 | -0.076 | washout |
| fisher_condition | 20 | +0.597 | -0.285 | reverse-inversion |
| fisher_entropy | 20 | -0.534 | +0.143 | weak-or-mixed |
| fisher_spectral | 20 | -0.586 | -0.271 | survives |
| fisher_stable_rank | 20 | -0.358 | +0.082 | washout |
| fisher_trace | 20 | -0.678 | -0.326 | survives |
| grad_l1 | 20 | -0.696 | -0.329 | survives |
| grad_linf | 20 | -0.496 | -0.256 | survives |
| grad_loss_logcorr | 20 | +0.147 | +0.224 | hidden-after-control |
| grad_mean_abs | 20 | -0.696 | -0.329 | survives |
| grad_noise_scale | 20 | +0.370 | +0.318 | survives |
| grad_norm | 20 | -0.648 | -0.291 | survives |
| gradient_energy_entropy | 20 | -0.556 | +0.116 | weak-or-mixed |
| gradient_energy_gini | 20 | +0.585 | -0.086 | washout |
| hessian_top_eig_power | 20 | -0.689 | -0.460 | survives |
| hessian_trace_hutchinson | 20 | -0.750 | -0.477 | survives |
| logit_norm_mean | 20 | +0.844 | +0.243 | survives |
| margin_mean | 20 | +0.513 | +0.300 | survives |
| metric_batch_acc | 20 | +0.490 | -0.162 | weak-or-mixed |
| metric_batch_loss | 20 | -0.529 | -0.252 | survives |
| per_sample_grad_norm_mean | 20 | -0.692 | -0.265 | survives |
| per_sample_grad_norm_std | 20 | -0.568 | -0.208 | survives |
| random_metric | 20 | +0.065 | -0.381 | hidden-after-control |
| relative_distance_from_init | 20 | +0.856 | +0.124 | weak-or-mixed |
| sam_sharpness | 20 | -0.582 | -0.104 | weak-or-mixed |
| train_acc | 20 | +0.499 | +0.515 | survives |
| train_loss | 20 | -0.540 | -0.536 | survives |
| update_to_weight_ratio | 20 | +0.841 | +0.142 | weak-or-mixed |
| val_loss | 20 | -0.405 | -0.716 | survives |
| weight_l1 | 20 | +0.759 | +0.025 | washout |
| weight_l2 | 20 | +0.753 | -0.124 | weak-or-mixed |
| weight_linf | 20 | +0.794 | +0.240 | survives |
| weight_rms | 20 | +0.753 | -0.124 | weak-or-mixed |

## arch=vit

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 20 | -0.435 | -0.212 | survives |
| brier | 20 | -0.565 | -0.552 | survives |
| confidence_mean | 20 | +0.529 | +0.464 | survives |
| distance_from_init_l2 | 20 | +0.618 | +0.135 | weak-or-mixed |
| ece | 20 | -0.523 | -0.404 | survives |
| entropy_mean | 20 | -0.574 | -0.537 | survives |
| feature_cosine_mean | 20 | +0.167 | -0.064 | weak-or-mixed |
| feature_erank | 20 | -0.012 | +0.410 | hidden-after-control |
| feature_erank_norm | 20 | -0.012 | +0.410 | hidden-after-control |
| feature_norm_mean | 20 | +0.129 | +0.480 | hidden-after-control |
| fim_erank | 20 | -0.379 | -0.321 | survives |
| fim_loss_scaled_erank | 20 | +0.077 | +0.007 | weak-or-mixed |
| fim_loss_scaled_norm | 20 | +0.077 | +0.007 | weak-or-mixed |
| fim_norm | 20 | -0.379 | -0.321 | survives |
| fim_unit_erank | 20 | +0.347 | +0.502 | survives |
| fim_unit_norm | 20 | +0.347 | +0.502 | survives |
| fisher_condition | 20 | +0.328 | +0.198 | weak-or-mixed |
| fisher_entropy | 20 | -0.379 | -0.321 | survives |
| fisher_spectral | 20 | -0.356 | +0.023 | washout |
| fisher_stable_rank | 20 | -0.212 | -0.214 | survives |
| fisher_trace | 20 | -0.495 | -0.076 | washout |
| grad_l1 | 20 | -0.523 | -0.156 | weak-or-mixed |
| grad_linf | 20 | -0.466 | -0.307 | survives |
| grad_loss_logcorr | 20 | +0.550 | +0.391 | survives |
| grad_mean_abs | 20 | -0.523 | -0.156 | weak-or-mixed |
| grad_noise_scale | 20 | +0.171 | -0.073 | weak-or-mixed |
| grad_norm | 20 | -0.499 | -0.120 | weak-or-mixed |
| gradient_energy_entropy | 20 | -0.465 | -0.413 | survives |
| gradient_energy_gini | 20 | +0.490 | +0.456 | survives |
| logit_norm_mean | 20 | +0.472 | +0.361 | survives |
| margin_mean | 20 | +0.567 | +0.473 | survives |
| metric_batch_acc | 20 | +0.550 | +0.316 | survives |
| metric_batch_loss | 20 | -0.529 | -0.533 | survives |
| per_sample_grad_norm_mean | 20 | -0.656 | -0.363 | survives |
| per_sample_grad_norm_std | 20 | -0.329 | +0.127 | weak-or-mixed |
| random_metric | 20 | -0.277 | -0.130 | weak-or-mixed |
| relative_distance_from_init | 20 | +0.618 | +0.135 | weak-or-mixed |
| sam_sharpness | 20 | -0.486 | -0.184 | weak-or-mixed |
| train_acc | 20 | +0.545 | +0.507 | survives |
| train_loss | 20 | -0.511 | -0.494 | survives |
| update_to_weight_ratio | 20 | +0.591 | +0.027 | washout |
| val_loss | 20 | -0.263 | -0.301 | survives |
| weight_l1 | 20 | +0.567 | +0.237 | survives |
| weight_l2 | 20 | +0.546 | +0.195 | weak-or-mixed |
| weight_linf | 20 | +0.555 | +0.282 | survives |
| weight_rms | 20 | +0.546 | +0.195 | weak-or-mixed |

## arch=wide_resnet

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 20 | -0.361 | -0.475 | survives |
| brier | 20 | +0.041 | -0.348 | hidden-after-control |
| confidence_mean | 20 | +0.093 | +0.462 | hidden-after-control |
| distance_from_init_l2 | 20 | +0.577 | +0.165 | weak-or-mixed |
| ece | 20 | -0.071 | -0.472 | hidden-after-control |
| entropy_mean | 20 | -0.262 | -0.622 | survives |
| feature_cosine_mean | 20 | +0.071 | -0.272 | hidden-after-control |
| feature_erank | 20 | +0.254 | -0.148 | weak-or-mixed |
| feature_erank_norm | 20 | +0.254 | -0.148 | weak-or-mixed |
| feature_norm_mean | 20 | +0.077 | +0.248 | hidden-after-control |
| fim_erank | 20 | -0.454 | -0.227 | survives |
| fim_loss_scaled_erank | 20 | +0.158 | +0.176 | weak-or-mixed |
| fim_loss_scaled_norm | 20 | +0.158 | +0.176 | weak-or-mixed |
| fim_norm | 20 | -0.454 | -0.227 | survives |
| fim_unit_erank | 20 | +0.356 | +0.145 | weak-or-mixed |
| fim_unit_norm | 20 | +0.356 | +0.145 | weak-or-mixed |
| fisher_condition | 20 | +0.474 | +0.288 | survives |
| fisher_entropy | 20 | -0.454 | -0.227 | survives |
| fisher_spectral | 20 | -0.358 | -0.531 | survives |
| fisher_stable_rank | 20 | -0.388 | -0.235 | survives |
| fisher_trace | 20 | -0.427 | -0.583 | survives |
| grad_l1 | 20 | -0.420 | -0.596 | survives |
| grad_linf | 20 | -0.066 | -0.310 | hidden-after-control |
| grad_loss_logcorr | 20 | +0.020 | -0.041 | weak-or-mixed |
| grad_mean_abs | 20 | -0.420 | -0.596 | survives |
| grad_noise_scale | 20 | +0.230 | +0.520 | survives |
| grad_norm | 20 | -0.414 | -0.566 | survives |
| gradient_energy_entropy | 20 | -0.436 | -0.192 | weak-or-mixed |
| gradient_energy_gini | 20 | +0.495 | +0.260 | survives |
| hessian_top_eig_power | 20 | -0.636 | -0.723 | survives |
| hessian_trace_hutchinson | 20 | -0.495 | -0.534 | survives |
| logit_norm_mean | 20 | +0.534 | +0.590 | survives |
| margin_mean | 20 | +0.074 | +0.476 | hidden-after-control |
| metric_batch_acc | 20 | +0.049 | +0.276 | hidden-after-control |
| metric_batch_loss | 20 | -0.047 | -0.452 | hidden-after-control |
| per_sample_grad_norm_mean | 20 | -0.493 | -0.644 | survives |
| per_sample_grad_norm_std | 20 | -0.414 | -0.540 | survives |
| random_metric | 20 | +0.168 | +0.264 | hidden-after-control |
| relative_distance_from_init | 20 | +0.577 | +0.165 | weak-or-mixed |
| sam_sharpness | 20 | -0.532 | -0.320 | survives |
| train_acc | 20 | -0.050 | +0.653 | hidden-after-control |
| train_loss | 20 | -0.185 | -0.680 | hidden-after-control |
| update_to_weight_ratio | 20 | +0.553 | +0.012 | washout |
| val_loss | 20 | -0.499 | -0.794 | survives |
| weight_l1 | 20 | +0.516 | +0.551 | survives |
| weight_l2 | 20 | +0.444 | +0.676 | survives |
| weight_linf | 20 | +0.374 | +0.445 | survives |
| weight_rms | 20 | +0.444 | +0.676 | survives |
