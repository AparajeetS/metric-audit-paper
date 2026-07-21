from __future__ import annotations

import argparse
from pathlib import Path
import sys

import numpy as np
import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from mbe_eval import cross_fitted_audit, make_calibration_ledger, refit_bootstrap_audit  # noqa: E402


EXPECTED = {
    "null_metric": False,
    "nonlinear_proxy": False,
    "clustered_null": False,
    "genuine_increment": True,
}


def run_refit_grid(
    *,
    repetitions: int,
    n: int,
    refit_draws: int,
    permutations: int,
    seed: int,
) -> pd.DataFrame:
    rows = []
    for repetition in range(repetitions):
        ledger = make_calibration_ledger(n=n, seed=seed + repetition * 10_007)
        for scenario_index, (scenario, expected) in enumerate(EXPECTED.items()):
            frame = ledger.loc[ledger["scenario"] == scenario].copy()
            result = refit_bootstrap_audit(
                frame,
                "metric",
                "target",
                ["baseline"],
                group_col="config_id",
                degree=6,
                nuisance_model="polynomial_ridge",
                refit_bootstrap=refit_draws,
                permutations=permutations,
                seed=seed + repetition * 10_007 + scenario_index * 1_009,
            )
            rows.append(
                {
                    "repetition": repetition,
                    "scenario": scenario,
                    "expected_increment": expected,
                    "residual_p": result["residual_p"],
                    "delta_mse": result["delta_mse"],
                    "refit_delta_mse_ci_low": result["refit_delta_mse_ci_low"],
                    "refit_delta_mse_ci_high": result["refit_delta_mse_ci_high"],
                    "refit_classification": result["refit_increment_classification"],
                }
            )
    return pd.DataFrame(rows)


def run_block_grid(*, repetitions: int, permutations: int, seed: int) -> pd.DataFrame:
    rows = []
    for repetition in range(repetitions):
        rng = np.random.default_rng(seed + repetition * 10_007)
        block = np.repeat(np.arange(4), 50)
        baseline = rng.normal(size=len(block))
        block_metric = np.array([-2.0, -0.5, 0.7, 2.2])[block]
        block_target = np.array([-1.7, -0.3, 0.9, 2.0])[block]
        frame = pd.DataFrame(
            {
                "block": block,
                "baseline": baseline,
                "metric": block_metric + rng.normal(size=len(block)),
                "target": block_target + baseline + rng.normal(size=len(block)),
            }
        )
        result = cross_fitted_audit(
            frame,
            "metric",
            "target",
            ["baseline", "block"],
            permutation_block_col="block",
            degree=4,
            permutations=permutations,
            bootstrap=0,
            seed=seed + repetition * 10_007,
        )
        rows.append(
            {
                "repetition": repetition,
                "residual_r": result["residual_r"],
                "block_permutation_p": result["residual_p"],
                "rejected": result["residual_p"] <= 0.05,
            }
        )
    return pd.DataFrame(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description="Calibrate refit and block-aware inference paths.")
    parser.add_argument("--repetitions", type=int, default=20)
    parser.add_argument("--n", type=int, default=150)
    parser.add_argument("--refit-draws", type=int, default=39)
    parser.add_argument("--permutations", type=int, default=99)
    parser.add_argument("--block-repetitions", type=int, default=100)
    parser.add_argument("--seed", type=int, default=20260716)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    refit = run_refit_grid(
        repetitions=args.repetitions,
        n=args.n,
        refit_draws=args.refit_draws,
        permutations=args.permutations,
        seed=args.seed,
    )
    block = run_block_grid(
        repetitions=args.block_repetitions,
        permutations=args.permutations,
        seed=args.seed + 9_000_001,
    )
    summary = (
        refit.assign(
            supported=refit["refit_classification"].eq("increment-supported")
        )
        .groupby(["scenario", "expected_increment"], as_index=False)
        .agg(
            repetitions=("supported", "size"),
            support_rate=("supported", "mean"),
            median_delta_mse=("delta_mse", "median"),
            median_refit_ci_low=("refit_delta_mse_ci_low", "median"),
        )
    )
    args.output_dir.mkdir(parents=True, exist_ok=True)
    refit.to_csv(args.output_dir / "refit_calibration_ledger.csv", index=False)
    block.to_csv(args.output_dir / "block_permutation_ledger.csv", index=False)
    summary.to_csv(args.output_dir / "refit_calibration_summary.csv", index=False)
    block_rate = float(block["rejected"].mean())
    lines = [
        "# Refit And Block-Aware Inference Calibration",
        "",
        f"The full refit bootstrap uses {args.refit_draws} configuration resamples in each of {args.repetitions} repetitions per scenario. The block-permutation null uses {args.block_repetitions} repetitions and rejects in {block_rate:.1%}.",
        "",
        "| Scenario | Expected increment | Strict refit support rate | Median Delta MSE | Median refit lower CI |",
        "|---|---:|---:|---:|---:|",
    ]
    for _, row in summary.iterrows():
        lines.append(
            f"| {row['scenario']} | {str(bool(row['expected_increment'])).lower()} | "
            f"{row['support_rate']:.3f} | {row['median_delta_mse']:.4f} | "
            f"{row['median_refit_ci_low']:.4f} |"
        )
    lines.extend(
        [
            "",
            "This is an initial finite calibration, not a general coverage guarantee. More dependence structures and bootstrap sizes remain required.",
            "",
        ]
    )
    (args.output_dir / "REFIT_INFERENCE_CALIBRATION.md").write_text(
        "\n".join(lines), encoding="utf-8"
    )
    print(summary.to_string(index=False))
    print(f"block_permutation_reject_rate={block_rate:.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
