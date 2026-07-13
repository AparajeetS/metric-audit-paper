# JMLR-Scale Metric Audit

- summary csv: `experiments\07_jmlr_scale\jmlr_holdout_text_audit_summary.csv`
- MBE covariates: `lr, wd, dropout, optimizer, arch, task, seed`

## pooled

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 100 | -0.829 | -0.339 | survives |
| brier | 100 | -0.433 | -0.056 | washout |
| confidence_mean | 100 | +0.550 | +0.256 | survives |
| distance_from_init_l2 | 100 | +0.774 | +0.041 | washout |
| ece | 100 | -0.457 | -0.122 | weak-or-mixed |
| entropy_mean | 100 | -0.541 | -0.183 | weak-or-mixed |
| feature_cosine_mean | 100 | +0.708 | +0.388 | survives |
| feature_erank | 100 | -0.630 | -0.299 | survives |
| feature_erank_norm | 100 | -0.630 | -0.299 | survives |
| feature_norm_mean | 100 | +0.340 | -0.275 | reverse-inversion |
| fim_erank | 100 | -0.534 | -0.224 | survives |
| fim_loss_scaled_erank | 100 | +0.092 | +0.217 | hidden-after-control |
| fim_loss_scaled_norm | 100 | +0.092 | +0.217 | hidden-after-control |
| fim_norm | 100 | -0.534 | -0.224 | survives |
| fim_unit_erank | 100 | +0.374 | +0.070 | washout |
| fim_unit_norm | 100 | +0.374 | +0.070 | washout |
| fisher_condition | 100 | +0.643 | +0.282 | survives |
| fisher_entropy | 100 | -0.534 | -0.224 | survives |
| fisher_spectral | 100 | -0.822 | -0.293 | survives |
| fisher_stable_rank | 100 | -0.350 | -0.247 | survives |
| fisher_trace | 100 | -0.837 | -0.387 | survives |
| grad_l1 | 100 | -0.830 | -0.329 | survives |
| grad_linf | 100 | -0.025 | +0.128 | weak-or-mixed |
| grad_loss_logcorr | 100 | +0.652 | +0.035 | washout |
| grad_mean_abs | 100 | -0.830 | -0.329 | survives |
| grad_noise_scale | 100 | -0.497 | -0.336 | survives |
| grad_norm | 100 | -0.827 | -0.328 | survives |
| gradient_energy_entropy | 100 | -0.496 | -0.186 | weak-or-mixed |
| gradient_energy_gini | 100 | +0.465 | +0.184 | weak-or-mixed |
| logit_norm_mean | 100 | +0.754 | -0.108 | weak-or-mixed |
| margin_mean | 100 | +0.570 | +0.258 | survives |
| metric_batch_acc | 100 | +0.330 | -0.043 | washout |
| metric_batch_loss | 100 | -0.429 | -0.071 | washout |
| per_sample_grad_norm_mean | 100 | -0.828 | -0.422 | survives |
| per_sample_grad_norm_std | 100 | -0.639 | -0.030 | washout |
| random_metric | 100 | +0.072 | +0.051 | weak-or-mixed |
| relative_distance_from_init | 100 | +0.774 | +0.045 | washout |
| sam_sharpness | 100 | -0.820 | -0.275 | survives |
| train_acc | 100 | +0.387 | +0.015 | washout |
| train_loss | 100 | -0.447 | -0.116 | weak-or-mixed |
| update_to_weight_ratio | 100 | +0.775 | +0.047 | washout |
| val_loss | 100 | -0.930 | -0.830 | survives |
| weight_l1 | 100 | +0.738 | +0.159 | weak-or-mixed |
| weight_l2 | 100 | +0.757 | +0.070 | washout |
| weight_linf | 100 | +0.092 | -0.058 | weak-or-mixed |
| weight_rms | 100 | +0.757 | +0.070 | washout |

## suite=text

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 100 | -0.829 | -0.339 | survives |
| brier | 100 | -0.433 | -0.056 | washout |
| confidence_mean | 100 | +0.550 | +0.256 | survives |
| distance_from_init_l2 | 100 | +0.774 | +0.041 | washout |
| ece | 100 | -0.457 | -0.122 | weak-or-mixed |
| entropy_mean | 100 | -0.541 | -0.183 | weak-or-mixed |
| feature_cosine_mean | 100 | +0.708 | +0.388 | survives |
| feature_erank | 100 | -0.630 | -0.299 | survives |
| feature_erank_norm | 100 | -0.630 | -0.299 | survives |
| feature_norm_mean | 100 | +0.340 | -0.275 | reverse-inversion |
| fim_erank | 100 | -0.534 | -0.224 | survives |
| fim_loss_scaled_erank | 100 | +0.092 | +0.217 | hidden-after-control |
| fim_loss_scaled_norm | 100 | +0.092 | +0.217 | hidden-after-control |
| fim_norm | 100 | -0.534 | -0.224 | survives |
| fim_unit_erank | 100 | +0.374 | +0.070 | washout |
| fim_unit_norm | 100 | +0.374 | +0.070 | washout |
| fisher_condition | 100 | +0.643 | +0.282 | survives |
| fisher_entropy | 100 | -0.534 | -0.224 | survives |
| fisher_spectral | 100 | -0.822 | -0.293 | survives |
| fisher_stable_rank | 100 | -0.350 | -0.247 | survives |
| fisher_trace | 100 | -0.837 | -0.387 | survives |
| grad_l1 | 100 | -0.830 | -0.329 | survives |
| grad_linf | 100 | -0.025 | +0.128 | weak-or-mixed |
| grad_loss_logcorr | 100 | +0.652 | +0.035 | washout |
| grad_mean_abs | 100 | -0.830 | -0.329 | survives |
| grad_noise_scale | 100 | -0.497 | -0.336 | survives |
| grad_norm | 100 | -0.827 | -0.328 | survives |
| gradient_energy_entropy | 100 | -0.496 | -0.186 | weak-or-mixed |
| gradient_energy_gini | 100 | +0.465 | +0.184 | weak-or-mixed |
| logit_norm_mean | 100 | +0.754 | -0.108 | weak-or-mixed |
| margin_mean | 100 | +0.570 | +0.258 | survives |
| metric_batch_acc | 100 | +0.330 | -0.043 | washout |
| metric_batch_loss | 100 | -0.429 | -0.071 | washout |
| per_sample_grad_norm_mean | 100 | -0.828 | -0.422 | survives |
| per_sample_grad_norm_std | 100 | -0.639 | -0.030 | washout |
| random_metric | 100 | +0.072 | +0.051 | weak-or-mixed |
| relative_distance_from_init | 100 | +0.774 | +0.045 | washout |
| sam_sharpness | 100 | -0.820 | -0.275 | survives |
| train_acc | 100 | +0.387 | +0.015 | washout |
| train_loss | 100 | -0.447 | -0.116 | weak-or-mixed |
| update_to_weight_ratio | 100 | +0.775 | +0.047 | washout |
| val_loss | 100 | -0.930 | -0.830 | survives |
| weight_l1 | 100 | +0.738 | +0.159 | weak-or-mixed |
| weight_l2 | 100 | +0.757 | +0.070 | washout |
| weight_linf | 100 | +0.092 | -0.058 | weak-or-mixed |
| weight_rms | 100 | +0.757 | +0.070 | washout |

## arch=char_transformer

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 100 | -0.829 | -0.339 | survives |
| brier | 100 | -0.433 | -0.056 | washout |
| confidence_mean | 100 | +0.550 | +0.256 | survives |
| distance_from_init_l2 | 100 | +0.774 | +0.041 | washout |
| ece | 100 | -0.457 | -0.122 | weak-or-mixed |
| entropy_mean | 100 | -0.541 | -0.183 | weak-or-mixed |
| feature_cosine_mean | 100 | +0.708 | +0.388 | survives |
| feature_erank | 100 | -0.630 | -0.299 | survives |
| feature_erank_norm | 100 | -0.630 | -0.299 | survives |
| feature_norm_mean | 100 | +0.340 | -0.275 | reverse-inversion |
| fim_erank | 100 | -0.534 | -0.224 | survives |
| fim_loss_scaled_erank | 100 | +0.092 | +0.217 | hidden-after-control |
| fim_loss_scaled_norm | 100 | +0.092 | +0.217 | hidden-after-control |
| fim_norm | 100 | -0.534 | -0.224 | survives |
| fim_unit_erank | 100 | +0.374 | +0.070 | washout |
| fim_unit_norm | 100 | +0.374 | +0.070 | washout |
| fisher_condition | 100 | +0.643 | +0.282 | survives |
| fisher_entropy | 100 | -0.534 | -0.224 | survives |
| fisher_spectral | 100 | -0.822 | -0.293 | survives |
| fisher_stable_rank | 100 | -0.350 | -0.247 | survives |
| fisher_trace | 100 | -0.837 | -0.387 | survives |
| grad_l1 | 100 | -0.830 | -0.329 | survives |
| grad_linf | 100 | -0.025 | +0.128 | weak-or-mixed |
| grad_loss_logcorr | 100 | +0.652 | +0.035 | washout |
| grad_mean_abs | 100 | -0.830 | -0.329 | survives |
| grad_noise_scale | 100 | -0.497 | -0.336 | survives |
| grad_norm | 100 | -0.827 | -0.328 | survives |
| gradient_energy_entropy | 100 | -0.496 | -0.186 | weak-or-mixed |
| gradient_energy_gini | 100 | +0.465 | +0.184 | weak-or-mixed |
| logit_norm_mean | 100 | +0.754 | -0.108 | weak-or-mixed |
| margin_mean | 100 | +0.570 | +0.258 | survives |
| metric_batch_acc | 100 | +0.330 | -0.043 | washout |
| metric_batch_loss | 100 | -0.429 | -0.071 | washout |
| per_sample_grad_norm_mean | 100 | -0.828 | -0.422 | survives |
| per_sample_grad_norm_std | 100 | -0.639 | -0.030 | washout |
| random_metric | 100 | +0.072 | +0.051 | weak-or-mixed |
| relative_distance_from_init | 100 | +0.774 | +0.045 | washout |
| sam_sharpness | 100 | -0.820 | -0.275 | survives |
| train_acc | 100 | +0.387 | +0.015 | washout |
| train_loss | 100 | -0.447 | -0.116 | weak-or-mixed |
| update_to_weight_ratio | 100 | +0.775 | +0.047 | washout |
| val_loss | 100 | -0.930 | -0.830 | survives |
| weight_l1 | 100 | +0.738 | +0.159 | weak-or-mixed |
| weight_l2 | 100 | +0.757 | +0.070 | washout |
| weight_linf | 100 | +0.092 | -0.058 | weak-or-mixed |
| weight_rms | 100 | +0.757 | +0.070 | washout |
