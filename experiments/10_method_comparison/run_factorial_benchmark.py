from __future__ import annotations

import argparse
from pathlib import Path
import sys

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from mbe_eval import (  # noqa: E402
    audit_metric,
    cross_fitted_audit,
    granulated_kendall,
    jiang_normalized_cmi,
    kendall_rank_correlation,
)


SCENARIOS = {
    "independent_null": (False, False),
    "design_proxy": (False, False),
    "interaction_proxy": (False, False),
    "genuine_increment": (True, True),
    "axis_specialist_proxy": (False, False),
    "sign_flip_increment": (False, True),
}


def make_factorial_case(
    scenario: str,
    *,
    repeats: int,
    seed: int,
) -> pd.DataFrame:
    if scenario not in SCENARIOS:
        raise ValueError(f"unknown scenario: {scenario}")
    rng = np.random.default_rng(seed)
    rows = []
    for hp_a in range(3):
        for hp_b in range(3):
            for hp_c in range(3):
                latent = rng.normal()
                base = 0.7 * hp_a + 0.5 * (hp_b - 1) ** 2 + 0.45 * hp_a * hp_c
                for repeat in range(repeats):
                    target_noise = rng.normal(0, 0.30)
                    metric_noise = rng.normal(0, 0.20)
                    if scenario == "independent_null":
                        metric = rng.normal()
                        target = base + target_noise
                    elif scenario == "design_proxy":
                        metric = base + metric_noise
                        target = base + target_noise
                    elif scenario == "interaction_proxy":
                        metric = hp_a * hp_c + metric_noise
                        target = base + target_noise
                    elif scenario == "genuine_increment":
                        metric = latent + metric_noise
                        target = base + 0.9 * latent + target_noise
                    elif scenario == "axis_specialist_proxy":
                        metric = hp_a + metric_noise
                        target = base + target_noise
                    else:
                        metric = latent + metric_noise
                        target = base + (hp_c - 1) * latent + target_noise
                    rows.append(
                        {
                            "scenario": scenario,
                            "config_id": f"a{hp_a}-b{hp_b}-c{hp_c}",
                            "repeat": repeat,
                            "hp_a": hp_a,
                            "hp_b": hp_b,
                            "hp_c": hp_c,
                            "metric": metric,
                            "target": target,
                        }
                    )
    return pd.DataFrame(rows)


def evaluate_case(
    frame: pd.DataFrame,
    *,
    permutations: int,
    bootstrap: int,
    seed: int,
) -> dict[str, float | int | str | bool]:
    controls = ["hp_a", "hp_b", "hp_c"]
    config = frame.groupby("config_id", as_index=False).agg(
        metric=("metric", "mean"),
        target=("target", "mean"),
        hp_a=("hp_a", "first"),
        hp_b=("hp_b", "first"),
        hp_c=("hp_c", "first"),
    )
    granulated, granulated_detail = granulated_kendall(
        frame, "metric", "target", controls, group_col="config_id"
    )
    cmi, cmi_detail = jiang_normalized_cmi(
        frame,
        "metric",
        "target",
        controls,
        group_col="config_id",
        max_conditioning=2,
    )
    partial = audit_metric(frame, "metric", "target", controls)
    additive = cross_fitted_audit(
        frame,
        "metric",
        "target",
        controls,
        group_col="config_id",
        degree=6,
        nuisance_model="polynomial_ridge",
        permutations=permutations,
        bootstrap=bootstrap,
        seed=seed,
    )
    interactions = cross_fitted_audit(
        frame,
        "metric",
        "target",
        controls,
        group_col="config_id",
        degree=6,
        nuisance_model="polynomial_ridge_interactions",
        permutations=permutations,
        bootstrap=bootstrap,
        seed=seed,
    )
    return {
        "scenario": str(frame["scenario"].iloc[0]),
        "expected_stable_increment": SCENARIOS[str(frame["scenario"].iloc[0])][0],
        "contains_conditional_increment": SCENARIOS[str(frame["scenario"].iloc[0])][1],
        "configurations": len(config),
        "raw_spearman": float(spearmanr(config["metric"], config["target"]).statistic),
        "raw_kendall": kendall_rank_correlation(config["metric"], config["target"]),
        "partial_spearman": float(partial["partial_r"]),
        "granulated_kendall": granulated,
        "granulated_min_axis": float(granulated_detail["granulated_kendall"].min()),
        "jiang_cmi": cmi,
        "jiang_cmi_min_conditioning": str(
            cmi_detail.loc[cmi_detail["normalized_cmi"].idxmin(), "conditioning"]
        ),
        "mbe_additive_residual_r": additive["residual_r"],
        "mbe_additive_p": additive["residual_p"],
        "mbe_additive_delta": additive["delta_mse"],
        "mbe_additive_delta_ci_low": additive["delta_mse_ci_low"],
        "mbe_additive_class": additive["increment_classification"],
        "mbe_interaction_residual_r": interactions["residual_r"],
        "mbe_interaction_p": interactions["residual_p"],
        "mbe_interaction_delta": interactions["delta_mse"],
        "mbe_interaction_delta_ci_low": interactions["delta_mse_ci_low"],
        "mbe_interaction_class": interactions["increment_classification"],
    }


def summarize(ledger: pd.DataFrame) -> pd.DataFrame:
    numeric = [
        "raw_spearman",
        "raw_kendall",
        "partial_spearman",
        "granulated_kendall",
        "granulated_min_axis",
        "jiang_cmi",
        "mbe_additive_delta",
        "mbe_interaction_delta",
    ]
    rows = []
    for scenario, group in ledger.groupby("scenario", sort=False):
        row: dict[str, float | int | str | bool] = {
            "scenario": scenario,
            "expected_stable_increment": bool(group["expected_stable_increment"].iloc[0]),
            "contains_conditional_increment": bool(group["contains_conditional_increment"].iloc[0]),
            "repetitions": len(group),
            "mbe_additive_support_rate": float(
                (group["mbe_additive_class"] == "increment-supported").mean()
            ),
            "mbe_interaction_support_rate": float(
                (group["mbe_interaction_class"] == "increment-supported").mean()
            ),
        }
        for column in numeric:
            row[f"{column}_median"] = float(group[column].median())
            row[f"{column}_q05"] = float(group[column].quantile(0.05))
            row[f"{column}_q95"] = float(group[column].quantile(0.95))
        rows.append(row)
    return pd.DataFrame(rows)


def write_report(summary: pd.DataFrame, path: Path) -> None:
    lines = [
        "# Shared Method Comparison",
        "",
        "This benchmark uses known-truth balanced factorial ledgers. Scores answer different questions; CMI and rank coefficients are descriptive and are not thresholded as hypothesis tests.",
        "",
        "| Scenario | True stable increment | Raw rho | Partial rho | Granulated tau | Jiang CMI | Additive MBE support | Interaction MBE support |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for _, row in summary.iterrows():
        lines.append(
            f"| {row['scenario']} | {str(bool(row['expected_stable_increment'])).lower()} | "
            f"{row['raw_spearman_median']:.3f} | {row['partial_spearman_median']:.3f} | "
            f"{row['granulated_kendall_median']:.3f} | {row['jiang_cmi_median']:.3f} | "
            f"{row['mbe_additive_support_rate']:.3f} | {row['mbe_interaction_support_rate']:.3f} |"
        )
    lines.extend(
        [
            "",
            "The source-faithful robust sign-error statistic is compared with MBE on the Dziugaite et al. public ledger rather than relabeled for this synthetic design. See `../09_published_metric_reaudit/studies/dziugaite2020/out/SOURCE_REPRODUCTION.md`.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare metric-evaluation methods on one factorial grid.")
    parser.add_argument("--repetitions", type=int, default=50)
    parser.add_argument("--seeds-per-config", type=int, default=5)
    parser.add_argument("--permutations", type=int, default=199)
    parser.add_argument("--bootstrap", type=int, default=199)
    parser.add_argument("--seed", type=int, default=2026)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).parent / "out")
    args = parser.parse_args()
    rows = []
    for repetition in range(args.repetitions):
        for scenario_index, scenario in enumerate(SCENARIOS):
            case_seed = args.seed + repetition * 10_007 + scenario_index * 1_009
            frame = make_factorial_case(scenario, repeats=args.seeds_per_config, seed=case_seed)
            rows.append(
                {
                    "repetition": repetition,
                    "seed": case_seed,
                    **evaluate_case(
                        frame,
                        permutations=args.permutations,
                        bootstrap=args.bootstrap,
                        seed=case_seed,
                    ),
                }
            )
    ledger = pd.DataFrame(rows)
    summary = summarize(ledger)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    ledger.to_csv(args.output_dir / "factorial_method_ledger.csv", index=False)
    summary.to_csv(args.output_dir / "factorial_method_summary.csv", index=False)
    write_report(summary, args.output_dir / "FACTORIAL_METHOD_COMPARISON.md")
    print(summary.to_string(index=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
