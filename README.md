# The Marginal Baseline Eval (MBE)

Welcome to the **Marginal Baseline Eval (MBE)** repository! 

This repository provides the formal implementation of the MBE protocol—a strict, 4-stage validation methodology designed to rigorously audit representation metrics in deep neural networks. 

It was originally built during a massive case study that mathematically falsified the Gradient Effective Rank ($\text{FIM}_{norm}$) metric.

## Why Do We Need MBE?
The AI safety and interpretability communities frequently propose internal structural metrics (e.g., representation geometry, effective rank, gradient coherence) to predict generalization or track model health. 

However, many of these metrics are secretly **Loss Proxies**. Because early validation loss trivially predicts final test accuracy, any metric that mathematically correlates with the *magnitude* of the loss will automatically correlate with generalization. Such a metric provides **zero independent structural insight**.

The MBE protocol is designed to catch these false positive metrics using a rigorous partial-correlation baseline control.

## Quickstart: The Sample Eval
We provide a plug-and-play python script that simulates exactly how MBE detects a disguised loss proxy. 

To run the sample test on a dummy metric:

```bash
cd mbe_eval
python sample_eval.py
```

### What happens in `sample_eval.py`?
1. It simulates 30 heterogeneous training runs with varying hyperparameters.
2. It generates a "Proposed Metric" that is secretly just a noisy copy of the early validation loss.
3. **Stage 1 (Absolute Correlation):** It checks if the metric predicts final generalization. It will **PASS**, yielding a massive $p$-value and appearing to be a breakthrough discovery.
4. **Stage 2 (MBE Control):** It runs the partial-correlation control against the trivial baseline (early validation loss). It will instantly **FAIL**, revealing the metric offers zero marginal signal.

## The Full 12-Test Falsification (Case Study)
If you wish to explore the original case study that proved why MBE is necessary—the complete falsification of the Gradient Effective Rank metric ($\text{FIM}_{norm}$) across MLPs, CNNs, and Transformers—all scripts are preserved in the `experiments/` directory.

See `PAPER.md` for the full technical writeup of the math, the origin story, and the mechanistic autopsy.

## Citation
If you use the Marginal Baseline Eval in your own representation evaluation, please cite the accompanying manuscript.
