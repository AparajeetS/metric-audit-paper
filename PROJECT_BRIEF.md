# Project Brief

## Project

**Marginal Baseline Evaluation (MBE)** is an open research project and Python
package for stress-testing claims about machine-learning training metrics.

## Problem

New metrics are often validated with pooled correlation against held-out
performance. That can overstate value when the metric tracks learning rate,
architecture, task composition, training state, or another ordinary predictor.
It can also hide failures to transfer across environments.

MBE 2.0 asks five distinct questions:

1. Does the metric associate with the target unconditionally?
2. Does it add predictive information beyond a declared baseline?
3. Does that information transport across tasks, architectures, and datasets?
4. Does it respond correctly under interventions with known direction?
5. Is it reliable and inexpensive enough to measure consistently?

## Current State

The software is usable today. Researchers can install `mbe-eval`, run a
CPU-only demonstration, audit a CSV training ledger, inspect the implementation,
and generate a Markdown report. The current v0.3.1 release implements the MBE
v1 linear partial-rank audit.

The scientific program is earlier-stage. Existing Kaggle runs are exploratory
pilot evidence. The 680-row legacy ledger contains repeated configurations, and
the text setup lacks a causal mask and permits label leakage. Those results are
preserved as provenance and as a case study in why audit protocols themselves
need stress testing; they are not presented as confirmatory language-model
evidence.

The active MBE 2.0 program replaces a single partial-correlation verdict with
cross-fitted nonlinear baselines, separate targets, environment transport,
intervention tests, uncertainty, practical significance, and explicit positive
and negative controls.

## Open Research Outputs

- Python package: https://pypi.org/project/mbe-eval/
- GitHub: https://github.com/AparajeetS/marginal-baseline-eval
- Public notebook: https://www.kaggle.com/code/aparajeetshadangi/audit-ml-training-metrics-with-mbe
- Open research inventory: [`OPEN_RESEARCH.md`](OPEN_RESEARCH.md)
- Technical program: [`docs/MBE_2_RESEARCH_PROGRAM.md`](docs/MBE_2_RESEARCH_PROGRAM.md)
- Evidence ledger: [`SUPPORTING_EVIDENCE.md`](SUPPORTING_EVIDENCE.md)
- Reproduction guide: [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md)
- Governance: [`GOVERNANCE.md`](GOVERNANCE.md)
- MIT license: [`LICENSE`](LICENSE)

## Why Support Is Needed

The highest-value next work is methodological calibration followed by corrected
replication, not simply a larger rerun. Funding or credits would support:

- synthetic tests with known nuisance structure and oracle controls;
- reanalysis of suitable public model corpora;
- corrected image and causally masked language-model factorial experiments;
- grouped uncertainty, baseline ablations, and locked external holdouts;
- release-quality artifacts, documentation, and independent reproduction.

The minimum serious program is estimated at approximately 400 RTX
4090-equivalent GPU-hours and $300-$500 in total cloud costs. The recommended
program is approximately 650 equivalent hours with a $600-$900 cap. Compute is
released only after no-compute and pilot gates pass.

## Expected Impact

MBE is intended to become shared validation infrastructure for metric papers,
benchmark designers, and small labs. Its value is not declaring metrics
universally good or bad. It is making the evidentiary standard explicit and
reproducible: what a metric predicts, beyond which baseline, in which
environment, under which intervention, and with what uncertainty and cost.

If active maintenance stopped, the MIT-licensed implementation, package source,
protocols, artifact formats, and reproduction instructions would remain
available for independent continuation.
