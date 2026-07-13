# Grant Execution Plan

This document maps a proposed $25,000 public-goods grant to a falsifiable MBE
2.0 validation program. It is a plan, not completed evidence.

## Project Lead And Execution Evidence

Aparajeet Shadangi is the project creator and current maintainer. Existing
execution evidence includes:

- an MIT-licensed Python package with two command-line tools;
- CI coverage across supported Python versions;
- a public Kaggle walkthrough and reproducibility documentation;
- a preserved 680-row exploratory evidence ledger across 40+ metric columns;
- public disclosure of repeated configurations, text-label leakage, and claims
  that must be retested rather than hidden;
- a frozen MBE 2.0 research program, milestone gates, and compute model.

The project currently has one primary technical lead. An eligible external
replicator will be selected before the protected holdout is opened under the
[independent replication protocol](docs/INDEPENDENT_REPLICATION_PROTOCOL.md).

## What Is New

MBE does not claim that hyperparameter conditioning or partial correlation is
new. The proposed contribution is a calibrated audit system that jointly tests
five distinct metric claims: association, incremental utility, transport,
intervention consistency, and measurement reliability. It combines a baseline
information ladder, cross-fitted nonlinear nuisance adjustment, deliberately
deceptive controls, configuration-blocked uncertainty, environment holdouts,
and scoped claim cards. Novelty remains a gate: if comparison with prior
conditional and robust evaluation methods shows no meaningful distinction, the
project publishes the benchmark and narrows or withdraws the method claim.

## Minimum 340-Run Matrix

The number 340 is the sum of two frozen minimum factorial designs, not an
undifferentiated run-count target.

| Domain | Design | Runs |
|---|---|---:|
| Image | 2 datasets x 3 architectures x 8 configurations x 5 seeds | 240 |
| Causal language modeling | 1 dataset x 2 model sizes x 10 configurations x 5 seeds | 100 |
| **Total** | 68 configuration blocks with 5 repeated seeds each | **340** |

Image candidates are CIFAR-10 and CIFAR-100 with ResNet-18,
WideResNet-28-2, and ViT-Tiny or an equivalently reproducible transformer. The
text design uses an explicitly tested causal mask and a public language-model
dataset such as WikiText-2. Final choices, splits, thresholds, and exclusion
rules are frozen before the scale gate.

Five seeds per configuration permit configuration-blocked uncertainty and
matched intervention comparisons. They are not presented as an a priori power
guarantee. The corrected pilot estimates variance and runtime; if the minimum
relevant improvement cannot be resolved by this matrix, scale compute pauses
and the design is revised before funds are released.

## Protected Holdout

The protected environment is selected and frozen before analysis of the main
factorials is unblinded. It must differ by dataset or task family and cannot be
used for metric design, nuisance-model selection, thresholds, or exclusions.
Before access, the project timestamps the repository commit, container digest,
metric cards, baseline ladder, hypotheses, and one primary analysis command.
The frozen result is retained regardless of direction.

## Proposed Budget

| Budget line | Ceiling | Release condition |
|---|---:|---|
| Research engineering and execution | $12,000 | Paid against frozen-protocol, implementation, analysis, documentation, and release milestones |
| Cloud compute and storage | $5,000 | Gated ceiling for primary runs, protected holdout, approved reruns, independent execution, storage, artifact transfer, archival preparation, and provider variance |
| Independent replication and audit | $5,000 | Released under the published independence and conflict rules |
| Open benchmark and archival release | $2,000 | Dataset packaging, checksums, metadata, persistent hosting, and citable archive |
| Contingency | $1,000 | Failed jobs or approved variance; unused balance remains visible |
| **Total** | **$25,000** | Final public spend ledger and artifact manifest |

These are ceilings, not spending targets. Compute is released only after the
synthetic calibration, public-corpus comparison, and corrected pilot pass their
gates. Unused funds and material reallocations are reported publicly.

## Public Deliverables

- corrected MBE 2.0 package and command-line tools;
- synthetic calibration suite and deceptive controls;
- 340-run image/text benchmark ledger with metric cards and hashes;
- timestamped protected-holdout result;
- independent replication report and discrepancy log;
- one-command reproduction bundle;
- public benchmark archive and paper, including a negative result if earned;
- final compute and spend ledger.
