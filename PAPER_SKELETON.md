# Paper Skeleton

Working title:

> Marginal Baseline Evaluation: Auditing Training Metrics Beyond Raw Correlation

This is a drafting scaffold, not final prose. Each section lists the claim, the
evidence currently available, and the remaining gap.

## Abstract

Core message:

> Training metrics are often validated by raw pooled correlation with held-out
> performance. We propose Marginal Baseline Evaluation (MBE), an audit protocol
> that tests whether a metric retains signal after controlling for ordinary
> baselines and design variables. In current Kaggle-scale experiments across
> 680 image and language-model runs, MBE preserves several stable predictors
> while exposing washout, inversion, and task-dependence in others. FIM_norm,
> our motivating case study, passes conventional validation but becomes
> task- and pooling-sensitive under MBE.

Evidence to cite:

- `SUPPORTING_EVIDENCE.md`
- `experiments/07_jmlr_scale/no_compute_outputs/NO_COMPUTE_UNCERTAINTY.md`

Remaining gap:

- locked holdout replication with frozen protocol.

## 1. Introduction

Claim:

Raw pooled correlation is insufficient for validating ML training metrics.

Motivation:

- A metric can look predictive because it tracks learning rate, architecture,
  validation loss, weak baselines, or task mix.
- Reviewers need a method that asks whether the metric adds marginal signal.

Narrative hook:

- FIM_norm looked promising under conventional tests.
- MBE later exposed that its conclusion changes across image-only, text-only,
  and pooled image+text settings.

Key figure:

- FIM_norm across image/text/full pools:
  - image default: `-0.662 -> -0.218`, survives;
  - text default: `-0.291 -> +0.014`, washout;
  - full default: `+0.225 -> -0.203`, reverse-inversion;
  - full strict: `+0.225 -> -0.300`, reverse-inversion.

## 2. Related Work

Groups to cover:

- generalization prediction metrics;
- sharpness and PAC-Bayes-adjacent measures;
- Fisher/gradient/geometry metrics;
- calibration and confidence metrics;
- conditional evaluation, partial correlation, and confounding controls;
- benchmark/reproducibility critiques of metric papers.

Positioning:

MBE is not a new scalar metric. It is an evaluation protocol for auditing
candidate metrics.

## 3. Method: Marginal Baseline Evaluation

Define:

- run ledger: one trained model per row;
- candidate metrics;
- held-out target;
- control variables;
- raw Spearman correlation;
- partial rank correlation after residualizing ranks against controls.

Default controls:

```text
lr, wd, dropout, optimizer, arch, task, seed
```

Strict controls:

```text
lr, wd, dropout, optimizer, arch, task, seed, val_loss
```

Classification thresholds:

```text
effect_threshold = 0.20
washout_threshold = 0.10
```

Classes:

- survives;
- washout;
- sign-inversion;
- reverse-inversion;
- hidden-after-control;
- weak-or-mixed.

Evidence to cite:

- `PROTOCOL_FREEZE.md`

## 4. Motivating Case Study: FIM_norm

Claim:

FIM_norm is useful because it was not obviously bad. It passed ordinary metric
validation before failing stronger audits.

Current positive evidence:

- MLP dual acid test:
  - label noise: `rho=-0.770`;
  - data capacity: `rho=-0.937`.
- CNN + BatchNorm:
  - noise: `rho=-0.956`;
  - n_train: `rho=-0.837`.
- Transformer + LayerNorm:
  - n_train: `rho=-0.951`;
  - noise: correct sign, not significant.
- Bootstrap checks often exclude zero.

Current MBE evidence:

- MLP grids:
  - FIM_norm `-0.815 -> +0.033`;
  - FIM_norm `-0.803 -> +0.056`.
- 680-model pool:
  - full default `+0.225 -> -0.203`;
  - full strict `+0.225 -> -0.300`.

Interpretation:

FIM_norm tracks a real training-state property, but the independent value of
that property is context-sensitive.

## 5. Experimental Evidence

Current confirmed pool:

- 480 CIFAR-10 image models;
- 200 character-transformer language models;
- 40+ candidate metrics.

Primary tables:

- full 680 default;
- full 680 strict + `val_loss`;
- image-only default/strict;
- text-only default/strict;
- metric-family summary.

No-compute uncertainty:

- bootstrap resamples: 200;
- unit: row/model run;
- target: `final_acc`.

Headline CI examples:

| Run | Metric | Raw rho, 95% CI | MBE partial rho, 95% CI | Class |
|---|---|---:|---:|---|
| full 680 default | FIM_norm | `+0.225 [+0.136, +0.314]` | `-0.203 [-0.267, -0.117]` | reverse-inversion |
| full 680 strict | FIM_norm | `+0.225 [+0.138, +0.296]` | `-0.300 [-0.389, -0.217]` | reverse-inversion |
| full 680 default | random_metric | `-0.035 [-0.112, +0.033]` | `-0.062 [-0.131, +0.018]` | weak-or-mixed |
| full 680 strict | confidence_mean | `+0.833 [+0.807, +0.850]` | `+0.536 [+0.464, +0.586]` | survives |

Default-threshold class counts:

| Run | Survives | Washout | Reverse inv. | Hidden | Weak/mixed |
|---|---:|---:|---:|---:|---:|
| image 480 default | 21 | 3 | 0 | 1 | 16 |
| image 480 strict | 29 | 1 | 0 | 4 | 4 |
| text 200 default | 15 | 12 | 1 | 1 | 10 |
| text 200 strict | 15 | 7 | 1 | 0 | 15 |
| full 680 default | 19 | 7 | 1 | 2 | 12 |
| full 680 strict | 26 | 4 | 1 | 3 | 6 |

Interpretation:

MBE is selective. It preserves many metrics while flagging fragile ones.

## 6. Metric-Family Findings

Use `METRIC_TAXONOMY.md`.

Likely findings:

- task-proximal and confidence/calibration metrics are generally stable;
- Fisher/gradient magnitude metrics often survive;
- feature geometry, weight norms, and distance/update proxies are fragile;
- sharpness metrics are mixed and sensitive to control set;
- FIM_norm is task- and pooling-sensitive.

Figure:

- family-by-class heatmap.

## 7. Ablations And Sensitivity

No-compute sensitivity already done:

- thresholds:
  - `effect_threshold in {0.15, 0.20, 0.25}`;
  - `washout_threshold in {0.05, 0.10, 0.15}`.

Remaining:

- control-set ablations:
  - no controls;
  - hyperparameters only;
  - hyperparameters + architecture/task;
  - strict + validation loss.

## 8. Limitations

Must say plainly:

- Current large evidence is not yet a locked holdout replication.
- Bootstrap is row-level, not block-level.
- Current tasks are CIFAR-10 and character-level LM only.
- Some metric implementations are approximate and metric-batch based.
- MBE detects conditional association, not causality.

## 9. Reproducibility

Point to:

- `REPRODUCIBILITY.md`;
- `experiments/07_jmlr_scale/ARTIFACTS.md`;
- `experiments/07_jmlr_scale/no_compute_uncertainty.py`;
- `experiments/07_jmlr_scale/no_compute_outputs/`.

Package:

```bash
pip install mbe-eval
mbe-eval-demo --bootstrap 200
```

CSV audit:

```bash
mbe-eval-audit --csv runs.csv --metrics fim_norm,val_loss --target final_acc --controls lr,wd,arch,seed
```

## 10. Conclusion

Conclusion claim:

MBE turns metric validation from "does this correlate with performance?" into
"does this metric retain signal beyond ordinary baselines?" The current
evidence shows that this distinction matters: several metrics survive, several
wash out, and FIM_norm changes conclusion depending on task and pooling.

## Immediate Writing Tasks

1. Turn Section 3 into polished method prose.
2. Create one FIM_norm figure from the current tables.
3. Create one metric-family heatmap.
4. Write the limitations section early to keep the paper honest.
5. Draft a locked-replication subsection before running any new compute.
