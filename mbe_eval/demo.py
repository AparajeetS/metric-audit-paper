from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from .core import audit_metrics
from .reporting import summarize_audit, write_markdown_report
from . import __version__


DEMO_METRICS = [
    "reported_gain",
    "validation_gain",
    "train_gain",
    "parameter_delta",
    "random_metric",
]

DEMO_CONTROLS = [
    "baseline_acc",
    "baseline_noise",
    "weak_baseline",
    "compute_budget",
    "suite",
    "arch",
    "regularization",
]


def make_demo_runs(n: int = 160, seed: int = 9) -> pd.DataFrame:
    """Create a small training-run ledger with weak-baseline artifacts."""

    rng = np.random.default_rng(seed)
    suite = rng.choice(["image", "text"], size=n, p=[0.60, 0.40])
    arch = rng.choice(["small_cnn", "resnet_tiny", "tiny_transformer"], size=n)
    compute_budget = rng.choice([1, 2, 4], size=n, p=[0.45, 0.35, 0.20])
    regularization = rng.choice(["low", "medium", "high"], size=n, p=[0.30, 0.50, 0.20])
    weak_baseline = rng.random(n) < 0.38

    suite_effect = np.where(suite == "image", 0.014, -0.004)
    arch_effect = np.select(
        [arch == "resnet_tiny", arch == "tiny_transformer"],
        [0.012, 0.004],
        default=-0.006,
    )
    reg_effect = np.select(
        [regularization == "medium", regularization == "high"],
        [0.010, 0.002],
        default=-0.007,
    )

    baseline_noise = np.where(
        weak_baseline,
        rng.uniform(0.035, 0.075, n),
        rng.uniform(0.006, 0.025, n),
    )
    baseline_acc = 0.70 + suite_effect + arch_effect + rng.normal(0, 0.035, n)
    baseline_acc = np.clip(baseline_acc - weak_baseline * 0.075, 0.45, 0.92)

    true_gain = (
        0.006
        + 0.008 * np.log2(compute_budget)
        + 0.70 * reg_effect
        + rng.normal(0, 0.010, n)
    )
    mechanical_recovery = weak_baseline * 0.030 + baseline_noise * 0.080
    test_gain = true_gain + mechanical_recovery + rng.normal(0, 0.008, n)

    reported_gain = weak_baseline * 0.065 + baseline_noise * 0.600 + rng.normal(0, 0.018, n)
    validation_gain = test_gain + 0.450 * true_gain + rng.normal(0, 0.008, n)
    train_gain = reported_gain + rng.normal(0, 0.012, n)
    parameter_delta = 0.006 * np.log2(compute_budget) + weak_baseline * 0.018
    parameter_delta = parameter_delta + rng.normal(0, 0.014, n)
    random_metric = rng.normal(0, 1, n)

    return pd.DataFrame(
        {
            "suite": suite,
            "arch": arch,
            "compute_budget": compute_budget,
            "regularization": regularization,
            "weak_baseline": weak_baseline.astype(int),
            "baseline_acc": baseline_acc,
            "baseline_noise": baseline_noise,
            "test_gain": test_gain,
            "reported_gain": reported_gain,
            "validation_gain": validation_gain,
            "train_gain": train_gain,
            "parameter_delta": parameter_delta,
            "random_metric": random_metric,
        }
    )


def run_demo(
    *,
    n: int = 160,
    seed: int = 9,
    bootstrap: int = 200,
    output: str | Path | None = "mbe_demo_report.md",
) -> pd.DataFrame:
    """Run a complete synthetic MBE demo and optionally write a report."""

    df = make_demo_runs(n=n, seed=seed)
    report = audit_metrics(
        df,
        metrics=DEMO_METRICS,
        target="test_gain",
        controls=DEMO_CONTROLS,
        bootstrap=bootstrap,
        seed=seed,
    )
    if output:
        write_markdown_report(
            report,
            output,
            title="MBE Demo Audit Report",
            target="test_gain",
            controls=DEMO_CONTROLS,
            notes=[
                f"Runs audited: {len(df)}",
                "Synthetic demo: replace this dataframe with your training-run ledger.",
            ],
        )
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run a CPU-only MBE demo audit.")
    parser.add_argument("--version", action="version", version=f"mbe-eval {__version__}")
    parser.add_argument("--n", type=int, default=160, help="Number of synthetic runs.")
    parser.add_argument("--seed", type=int, default=9, help="Random seed.")
    parser.add_argument("--bootstrap", type=int, default=200, help="Bootstrap resamples.")
    parser.add_argument(
        "--output",
        default="mbe_demo_report.md",
        help="Markdown report path. Use an empty string to skip writing.",
    )
    parser.add_argument("--no-output", action="store_true", help="Do not write a markdown report.")
    args = parser.parse_args(argv)

    report = run_demo(
        n=args.n,
        seed=args.seed,
        bootstrap=args.bootstrap,
        output=None if args.no_output else args.output,
    )
    print(summarize_audit(report).to_string(index=False))
    if args.output and not args.no_output:
        print(f"\nWrote {Path(args.output).resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = ["DEMO_CONTROLS", "DEMO_METRICS", "make_demo_runs", "run_demo", "main"]
