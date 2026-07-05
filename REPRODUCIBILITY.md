# Reproducibility

This page explains what can be reproduced locally from saved artifacts and what
requires fresh GPU compute.

## Local Setup

```bash
git clone https://github.com/AparajeetS/metric-audit-paper.git
cd metric-audit-paper
python -m venv .venv
.venv\Scripts\activate
pip install -e ".[dev]"
```

Run package tests:

```bash
python -m pytest -q
```

Run the CPU-only package demo:

```bash
mbe-eval-demo --bootstrap 200
```

This writes `mbe_demo_report.md` and does not require GPU compute.

## Regenerate MBE Tables From Saved CSVs

The current paper-scale summaries are generated from saved Kaggle CSV outputs:

```bash
python experiments/07_jmlr_scale/analyze_jmlr_scale.py
```

Expected headline outputs include:

- `experiments/07_jmlr_scale/jmlr_image_combined_480_audit_summary.md`
- `experiments/07_jmlr_scale/jmlr_image_combined_480_strict_loss_mbe_summary.md`
- `experiments/07_jmlr_scale/jmlr_text_combined_200_audit_summary.md`
- `experiments/07_jmlr_scale/jmlr_text_combined_200_strict_loss_mbe_summary.md`
- `experiments/07_jmlr_scale/jmlr_full_confirmed_680_audit_summary.md`
- `experiments/07_jmlr_scale/jmlr_full_confirmed_680_strict_loss_mbe_summary.md`

The key raw result artifacts and SHA256 hashes are listed in
`experiments/07_jmlr_scale/ARTIFACTS.md`.

## CPU-Only Uncertainty And Threshold Sensitivity

Bootstrap confidence intervals and threshold-sensitivity counts can be
regenerated from saved CSVs without GPU compute:

```bash
python experiments/07_jmlr_scale/no_compute_uncertainty.py --bootstrap 200
```

Expected outputs:

- `experiments/07_jmlr_scale/no_compute_outputs/headline_bootstrap_ci.csv`
- `experiments/07_jmlr_scale/no_compute_outputs/threshold_sensitivity.csv`
- `experiments/07_jmlr_scale/no_compute_outputs/NO_COMPUTE_UNCERTAINTY.md`

## Public Notebook

The public Kaggle walkthrough is:

https://www.kaggle.com/code/aparajeetshadangi/audit-ml-training-metrics-with-mbe

Its source is tracked at:

```text
kaggle/mbe_metric_audit/how_to_audit_ml_training_metrics_mbe.ipynb
```

Push a new notebook version with:

```bash
python -m kaggle kernels push -p kaggle\mbe_metric_audit
```

## GPU-Required Training Runs

The package and saved-analysis scripts do not require GPU. Fresh model-training
replications do.

Current large-scale training scripts live in:

```text
experiments/07_jmlr_scale/
```

Representative Kaggle push commands:

```bash
python -m kaggle kernels push -p experiments\07_jmlr_scale
```

Or use the helper scripts:

```powershell
.\experiments\07_jmlr_scale\push_image.ps1
.\experiments\07_jmlr_scale\push_text.ps1
```

The current confirmed pool used:

- 480 image models: CNN, ResNet, ViT, WideResNet on CIFAR-10.
- 200 text models: character-transformer language models.
- Default MBE controls: `lr`, `wd`, `dropout`, `optimizer`, `arch`, `task`, `seed`.
- Strict MBE controls: default controls plus `val_loss`.

## Evidence Files

Use these files when checking the research claims:

- `SUPPORTING_EVIDENCE.md`: run-by-run interpretation and washout lists.
- `RUN_PROGRESS_LOG_2026-06-28.md`: run ledger for the current large-scale pass.
- `experiments/07_jmlr_scale/ARTIFACTS.md`: artifact hashes and raw CSV references.
- `experiments/06_independent_audit/artifact_audit_report.md`: independent audit of older artifacts.

## Compute Gap

The repository is intentionally usable without fresh compute. The current gap is
not software accessibility; it is replication scale. The next grant-funded or
GPU-credit-funded step should be:

1. freeze the MBE protocol;
2. launch a locked holdout replication;
3. bootstrap headline correlations;
4. run control-set ablations;
5. publish updated CSVs, hashes, and summaries.
