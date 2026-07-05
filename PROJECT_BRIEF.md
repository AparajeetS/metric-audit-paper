# Project Brief

## Project

**Marginal Baseline Evaluation (MBE)** is a research project and Python package
for auditing machine-learning training metrics beyond raw pooled correlation.

## Problem

New training and generalization metrics are often validated by showing that they
correlate with held-out performance. That is not enough. A metric can look
useful because it tracks easier baselines, learning rate, architecture, task
mix, validation loss, or other design variables.

MBE asks a stricter question:

> Does this metric retain signal after controlling for ordinary baselines and
> experimental design variables?

## Current Evidence

Early Kaggle-scale runs are promising enough to justify further compute.

Current confirmed evidence:

- 680 trained models.
- 480 CIFAR-10 image models across CNN, ResNet, ViT, and WideResNet settings.
- 200 character-transformer language models.
- 40+ candidate metrics across Fisher/gradient, sharpness, feature, confidence,
  calibration, weight, and distance/update families.

Key finding:

- MBE is selective. It preserves several metrics while exposing washout,
  inversion, and task-dependence in others.
- FIM_norm is the motivating case study: it looked promising under conventional
  validation, survives image-only audits, washes out in text-only default
  audits, and reverses in pooled image+text audits.

No-compute uncertainty check:

- full 680 default FIM_norm: raw `+0.225 [+0.136, +0.314]`, MBE partial
  `-0.203 [-0.267, -0.117]`, reverse-inversion;
- full 680 strict FIM_norm: raw `+0.225 [+0.138, +0.296]`, MBE partial
  `-0.300 [-0.389, -0.217]`, reverse-inversion;
- random metric remains weak;
- confidence metrics can survive strong controls.

## Open-Source Outputs

- Python package: https://pypi.org/project/mbe-eval/
- GitHub repository: https://github.com/AparajeetS/metric-audit-paper
- Public Kaggle notebook: https://www.kaggle.com/code/aparajeetshadangi/audit-ml-training-metrics-with-mbe
- Evidence ledger: `SUPPORTING_EVIDENCE.md`
- Protocol freeze: `PROTOCOL_FREEZE.md`
- Reproducibility guide: `REPRODUCIBILITY.md`

## Why More Compute Is Needed

The current evidence is strong enough to define the research direction, but a
serious submission needs a locked holdout replication:

- fresh image and text runs under a frozen protocol;
- bootstrap confidence intervals for all headline metrics;
- control-set ablations;
- threshold-sensitivity analysis;
- metric-family comparisons;
- exact artifact hashes and public summaries.

The software is ready enough for users with compute to test MBE on their own
training ledgers. The bottleneck is replication scale, not package usability.

## Expected Impact

MBE can become a practical audit layer for metric papers and training-metric
benchmarks. It gives researchers a way to distinguish:

- metrics that survive baseline controls;
- metrics that wash out;
- metrics that invert under controls;
- metrics whose conclusions depend on task, architecture, or pooling.

This helps prevent overclaiming from raw correlations and makes metric
evaluation more reproducible.
