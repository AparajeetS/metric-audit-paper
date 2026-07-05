from __future__ import annotations

import argparse
from pathlib import Path
import sys
from typing import Iterable

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mbe_eval.core import audit_metric, classify_effect


EXPERIMENT_DIR = ROOT / "experiments" / "07_jmlr_scale"

RAW_FILES = {
    "image_v2": EXPERIMENT_DIR / "kaggle_downloads" / "image_v2" / "jmlr_scale_image_results.csv",
    "confirm_image": EXPERIMENT_DIR / "kaggle_downloads" / "confirm_image" / "jmlr_confirm_image_results.csv",
    "text_v2": EXPERIMENT_DIR / "kaggle_downloads" / "text_v2" / "jmlr_scale_text_results.csv",
    "confirm_text": EXPERIMENT_DIR / "kaggle_downloads" / "confirm_text" / "jmlr_confirm_text_results.csv",
}

SUMMARY_FILES = {
    "image_480_default": EXPERIMENT_DIR / "jmlr_image_combined_480_audit_summary.csv",
    "image_480_strict": EXPERIMENT_DIR / "jmlr_image_combined_480_strict_loss_mbe_summary.csv",
    "text_200_default": EXPERIMENT_DIR / "jmlr_text_combined_200_audit_summary.csv",
    "text_200_strict": EXPERIMENT_DIR / "jmlr_text_combined_200_strict_loss_mbe_summary.csv",
    "full_680_default": EXPERIMENT_DIR / "jmlr_full_confirmed_680_audit_summary.csv",
    "full_680_strict": EXPERIMENT_DIR / "jmlr_full_confirmed_680_strict_loss_mbe_summary.csv",
}

DEFAULT_CONTROLS = ["lr", "wd", "dropout", "optimizer", "arch", "task", "seed"]
STRICT_CONTROLS = [*DEFAULT_CONTROLS, "val_loss"]

HEADLINE_METRICS = [
    "fim_norm",
    "val_loss",
    "fisher_trace",
    "grad_norm",
    "confidence_mean",
    "feature_norm_mean",
    "feature_erank",
    "weight_l2",
    "distance_from_init_l2",
    "update_to_weight_ratio",
    "random_metric",
]


def load_raw_pool(pool: str) -> pd.DataFrame:
    parts = {name: pd.read_csv(path) for name, path in RAW_FILES.items()}
    if pool == "image_480":
        return pd.concat([parts["image_v2"], parts["confirm_image"]], ignore_index=True, sort=False)
    if pool == "text_200":
        return pd.concat([parts["text_v2"], parts["confirm_text"]], ignore_index=True, sort=False)
    if pool == "full_680":
        return pd.concat(parts.values(), ignore_index=True, sort=False)
    raise ValueError(f"Unknown pool: {pool}")


def _safe_float(value: object) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return np.nan


def bootstrap_headlines(n_boot: int, seed: int) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    configs = [
        ("image_480_default", "image_480", DEFAULT_CONTROLS),
        ("image_480_strict", "image_480", STRICT_CONTROLS),
        ("text_200_default", "text_200", DEFAULT_CONTROLS),
        ("text_200_strict", "text_200", STRICT_CONTROLS),
        ("full_680_default", "full_680", DEFAULT_CONTROLS),
        ("full_680_strict", "full_680", STRICT_CONTROLS),
    ]
    for config_i, (label, pool, controls) in enumerate(configs):
        df = load_raw_pool(pool)
        for metric_i, metric in enumerate(HEADLINE_METRICS):
            if metric not in df.columns:
                continue
            row = audit_metric(
                df,
                metric=metric,
                target="final_acc",
                controls=controls,
                group=label,
                bootstrap=n_boot,
                seed=seed + 1000 * config_i + metric_i,
            )
            rows.append(
                {
                    "run": label,
                    "metric": metric,
                    "n": row["n"],
                    "raw_r": row["raw_r"],
                    "raw_ci_low": row.get("raw_ci_low", np.nan),
                    "raw_ci_high": row.get("raw_ci_high", np.nan),
                    "partial_r": row["partial_r"],
                    "partial_ci_low": row.get("partial_ci_low", np.nan),
                    "partial_ci_high": row.get("partial_ci_high", np.nan),
                    "delta": row["delta_partial_minus_raw"],
                    "delta_ci_low": row.get("delta_ci_low", np.nan),
                    "delta_ci_high": row.get("delta_ci_high", np.nan),
                    "classification": row["classification"],
                }
            )
    return pd.DataFrame(rows)


def threshold_sensitivity() -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for label, path in SUMMARY_FILES.items():
        df = pd.read_csv(path)
        pooled = df[df["group"].eq("pooled")].copy()
        for effect in [0.15, 0.20, 0.25]:
            for washout in [0.05, 0.10, 0.15]:
                classes = [
                    classify_effect(
                        _safe_float(row["raw_spearman"]),
                        _safe_float(row["mbe_partial"]),
                        effect_threshold=effect,
                        washout_threshold=washout,
                    )
                    for _, row in pooled.iterrows()
                ]
                counts = pd.Series(classes).value_counts().to_dict()
                rows.append(
                    {
                        "run": label,
                        "effect_threshold": effect,
                        "washout_threshold": washout,
                        "survives": counts.get("survives", 0),
                        "washout": counts.get("washout", 0),
                        "sign_inversion": counts.get("sign-inversion", 0),
                        "reverse_inversion": counts.get("reverse-inversion", 0),
                        "hidden_after_control": counts.get("hidden-after-control", 0),
                        "weak_or_mixed": counts.get("weak-or-mixed", 0),
                        "insufficient_data": counts.get("insufficient-data", 0),
                    }
                )
    return pd.DataFrame(rows)


def _fmt_ci(row: pd.Series, value_col: str, low_col: str, high_col: str) -> str:
    value = _safe_float(row[value_col])
    low = _safe_float(row[low_col])
    high = _safe_float(row[high_col])
    if np.isnan(low) or np.isnan(high):
        return f"{value:+.3f}"
    return f"{value:+.3f} [{low:+.3f}, {high:+.3f}]"


def write_markdown(boot: pd.DataFrame, sens: pd.DataFrame, out_path: Path, n_boot: int) -> None:
    lines = [
        "# No-Compute Uncertainty And Sensitivity",
        "",
        "This report uses only saved Kaggle result CSVs. No model training is run.",
        "",
        f"- Bootstrap resamples per metric/run: `{n_boot}`",
        "- Bootstrap unit: row/model run",
        "- Target: `final_acc`",
        "- Default controls: `lr, wd, dropout, optimizer, arch, task, seed`",
        "- Strict controls: default controls plus `val_loss`",
        "",
        "## Headline Bootstrap CIs",
        "",
        "| Run | Metric | n | Raw rho, 95% CI | MBE partial rho, 95% CI | Delta, 95% CI | Class |",
        "|---|---|---:|---:|---:|---:|---|",
    ]
    for _, row in boot.iterrows():
        lines.append(
            "| {run} | `{metric}` | {n} | {raw} | {partial} | {delta} | {cls} |".format(
                run=row["run"],
                metric=row["metric"],
                n=int(row["n"]),
                raw=_fmt_ci(row, "raw_r", "raw_ci_low", "raw_ci_high"),
                partial=_fmt_ci(row, "partial_r", "partial_ci_low", "partial_ci_high"),
                delta=_fmt_ci(row, "delta", "delta_ci_low", "delta_ci_high"),
                cls=row["classification"],
            )
        )

    lines.extend(
        [
            "",
            "## Default-Threshold Class Counts",
            "",
            "The default threshold is `effect_threshold=0.20`, `washout_threshold=0.10`.",
            "",
            "| Run | Survives | Washout | Sign inv. | Reverse inv. | Hidden | Weak/mixed |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    default = sens[(sens["effect_threshold"] == 0.20) & (sens["washout_threshold"] == 0.10)]
    for _, row in default.iterrows():
        lines.append(
            f"| {row['run']} | {row['survives']} | {row['washout']} | "
            f"{row['sign_inversion']} | {row['reverse_inversion']} | "
            f"{row['hidden_after_control']} | {row['weak_or_mixed']} |"
        )

    lines.extend(
        [
            "",
            "## Sensitivity Read",
            "",
            "- The current headline story should be read as threshold-sensitive until a locked replication is run.",
            "- The key qualitative question is whether fragile families remain fragile across nearby thresholds.",
            "- Inversions are reported separately from washout because they indicate sign reversal, not just collapse.",
            "",
        ]
    )
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="CPU-only uncertainty analysis from saved large-scale CSVs.")
    parser.add_argument("--bootstrap", type=int, default=200, help="Bootstrap resamples per metric/run.")
    parser.add_argument("--seed", type=int, default=20260705, help="Bootstrap seed.")
    parser.add_argument(
        "--out-dir",
        default=str(EXPERIMENT_DIR / "no_compute_outputs"),
        help="Output directory for CSV/markdown reports.",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    boot = bootstrap_headlines(args.bootstrap, args.seed)
    sens = threshold_sensitivity()
    boot.to_csv(out_dir / "headline_bootstrap_ci.csv", index=False)
    sens.to_csv(out_dir / "threshold_sensitivity.csv", index=False)
    write_markdown(boot, sens, out_dir / "NO_COMPUTE_UNCERTAINTY.md", args.bootstrap)
    print(f"Wrote {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
