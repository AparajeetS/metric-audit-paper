# Fantastic Robustness Measures (2023) Intake

## Study

*Fantastic Robustness Measures: The Secrets of Robust Generalization* reports
more than 1,300 adversarially trained CIFAR-10 models and a RobustBench transfer
study.

- Paper: <https://papers.nips.cc/paper_files/paper/2023/hash/98a5c0470e57d518ade4e56c6ee0b363-Abstract-Conference.html>
- Official artifact: <https://github.com/Harry24k/MAIR>
- Inspected artifact commit: `fcf0abae1c901829e192d856b6b3992a7b16d90d`
- Intake date: 2026-07-16

## Intake Result

The official repository contains adversarial training, attack, evaluation, and
model-loading code plus links to selected checkpoints. At the inspected commit,
it does not contain the paper's 1,300-model run ledger, the reported metric
matrix, or the measure-analysis implementation. Its README lists merging the
measures as future work.

An exact native-statistic reproduction or MBE reaudit would therefore require
either the authors' aggregate ledger or reconstruction of the complete training
and metric pipeline. The latter is a new GPU study, not a no-compute
reproduction. This candidate remains blocked for artifact availability and is
not counted as a failed replication.

## Unblocking Evidence

Any table with one row per model containing robust train/test performance,
training configuration, metric values, and model identifier would permit an
outcome-preserving intake. Checkpoints alone are insufficient for exact
reproduction unless the paper's metric implementations and evaluation subsets
are also frozen.
