# The Marginal Baseline Eval (MBE)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Welcome to the **Marginal Baseline Eval (MBE)** repository! 

This repository provides the formal implementation of the MBE protocol — a strict, 4-stage validation methodology designed to rigorously audit representation metrics in deep neural networks. 

It was originally built during a massive case study that mathematically falsified the Gradient Effective Rank (FIM_norm) metric.

## Why Do We Need MBE?

The AI safety and interpretability communities frequently propose internal structural metrics (e.g., representation geometry, effective rank, gradient coherence) to predict generalization or track model health. 

However, many of these metrics are secretly **Loss Proxies**. Because early validation loss trivially predicts final test accuracy, any metric that mathematically correlates with the *magnitude* of the loss will automatically correlate with generalization. Such a metric provides **zero independent structural insight**.

The MBE protocol catches these false positive metrics using a rigorous **partial-correlation baseline control**.

## Installation

You can install the framework directly from PyPI:

```bash
pip install mbe-eval
```

Or, if you want to run the PyTorch demos, clone the repository:

```bash
git clone https://github.com/AparajeetS/metric-audit-paper-code.git
cd metric-audit-paper-code
pip install -r requirements.txt
```

## The MBE API

MBE is a fully importable Python framework powered by `pandas` and `pingouin`. You can integrate it directly into your own model evaluation pipelines.

```python
from mbe_eval import MBEEvaluator

# Pass your experimental arrays (numpy arrays)
evaluator = MBEEvaluator(metric_name="My Cool Metric", baseline_name="Epoch 20 Val Loss")
report = evaluator.evaluate(metric_vals, baseline_vals, target_vals)
```
This automatically prints a beautiful `rich` diagnostics table to the console and generates a high-resolution `seaborn` graphical report in the `mbe_reports/` directory.

## Real PyTorch Demos

We provide two end-to-end PyTorch scripts in the `examples/` directory that actually train neural networks and run the evaluation live.

**1. The Acid Test (Stage 1)**
Shows how a metric can successfully track capacity and noise, giving false assurance.
```bash
python examples/01_run_acid_test.py
```

**2. The Heterogeneous Grid (Stage 4)**
The killer demo. Trains 20 models with randomized hyperparameters, computes the Gradient Effective Rank, and runs the final MBE Partial Correlation control to prove the metric is a disguised loss proxy.
```bash
python examples/02_run_heterogeneous_grid.py
```

## Repository Structure

```
metric-audit-paper-code/
├── mbe_eval/               # The core MBE evaluation API
│   ├── __init__.py
│   ├── core.py             # MBEEvaluator class
│   ├── utils.py            # PyTorch FIM_norm extraction
│   └── sample_eval.py      # Basic synthetic simulation
├── examples/               # Real end-to-end PyTorch demos
│   ├── 01_run_acid_test.py
│   └── 02_run_heterogeneous_grid.py
├── experiments/            # All 12 original paper experiment scripts
├── metric_audit/           # Core FIM_norm computation library
├── docs/
│   └── RESULTS.md          # Raw numerical results for the paper
├── PAPER.md                # Full technical writeup
├── requirements.txt
├── LICENSE
└── README.md
```

## Citation

If you use the Marginal Baseline Eval in your own representation evaluation, please cite the accompanying manuscript:

```
Shadangi, A. (2026). Does It Beat the Baseline? A Comprehensive Negative Result 
on Gradient Effective Rank as a Generalization Predictor. arXiv preprint.
```
