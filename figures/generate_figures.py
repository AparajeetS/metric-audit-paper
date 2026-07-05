from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "figures" / "out"
EXP_DIR = ROOT / "experiments" / "07_jmlr_scale"

FAMILY_MAP = {
    "val_loss": "task-proximal",
    "train_loss": "task-proximal",
    "train_acc": "task-proximal",
    "metric_batch_loss": "task-proximal",
    "metric_batch_acc": "task-proximal",
    "confidence_mean": "confidence",
    "entropy_mean": "confidence",
    "margin_mean": "confidence",
    "brier": "confidence",
    "ece": "confidence",
    "logit_norm_mean": "confidence",
    "grad_norm": "gradient",
    "grad_l1": "gradient",
    "grad_linf": "gradient",
    "grad_mean_abs": "gradient",
    "per_sample_grad_norm_mean": "gradient",
    "per_sample_grad_norm_std": "gradient",
    "grad_noise_scale": "gradient",
    "fisher_trace": "fisher",
    "fisher_spectral": "fisher",
    "fisher_condition": "fisher",
    "fisher_stable_rank": "fisher",
    "fisher_entropy": "fisher",
    "fim_erank": "fisher",
    "fim_norm": "fisher",
    "sam_sharpness": "sharpness",
    "asam_sharpness": "sharpness",
    "hessian_trace_hutchinson": "sharpness",
    "hessian_top_eig_power": "sharpness",
    "feature_erank": "feature",
    "feature_erank_norm": "feature",
    "feature_norm_mean": "feature",
    "feature_cosine_mean": "feature",
    "weight_l1": "weight",
    "weight_l2": "weight",
    "weight_linf": "weight",
    "weight_rms": "weight",
    "distance_from_init_l2": "distance/update",
    "relative_distance_from_init": "distance/update",
    "update_to_weight_ratio": "distance/update",
    "random_metric": "negative-control",
}

CLASS_ORDER = [
    "survives",
    "washout",
    "sign-inversion",
    "reverse-inversion",
    "hidden-after-control",
    "weak-or-mixed",
]

CLASS_COLORS = {
    "survives": "#2f7d32",
    "washout": "#c13c37",
    "sign-inversion": "#8e24aa",
    "reverse-inversion": "#6a1b9a",
    "hidden-after-control": "#f2a03d",
    "weak-or-mixed": "#70757a",
}


def load_pooled(name: str) -> pd.DataFrame:
    df = pd.read_csv(EXP_DIR / name)
    return df[df["group"].eq("pooled")].copy()


def savefig(name: str) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUT_DIR / name
    plt.tight_layout()
    plt.savefig(path, dpi=220, bbox_inches="tight")
    plt.close()
    print(path)


def plot_raw_vs_mbe() -> None:
    df = load_pooled("jmlr_full_confirmed_680_audit_summary.csv")
    df["family"] = df["metric"].map(FAMILY_MAP).fillna("other")

    families = list(dict.fromkeys(df["family"].sort_values()))
    colors = plt.cm.tab20(np.linspace(0, 1, len(families)))
    color_map = dict(zip(families, colors))

    plt.figure(figsize=(8.2, 6.2))
    for family, group in df.groupby("family"):
        plt.scatter(
            group["raw_spearman"],
            group["mbe_partial"],
            label=family,
            s=52,
            alpha=0.82,
            edgecolor="white",
            linewidth=0.5,
            color=color_map[family],
        )
    lim = 1.0
    plt.axhline(0, color="black", linewidth=0.8, alpha=0.6)
    plt.axvline(0, color="black", linewidth=0.8, alpha=0.6)
    plt.plot([-lim, lim], [-lim, lim], color="0.55", linestyle="--", linewidth=1)
    plt.xlim(-lim, lim)
    plt.ylim(-lim, lim)
    plt.xlabel("Raw Spearman rho with final accuracy")
    plt.ylabel("MBE partial rho after controls")
    plt.title("Full 680-model audit: raw correlation vs MBE")
    plt.legend(loc="center left", bbox_to_anchor=(1.02, 0.5), frameon=False)
    savefig("raw_vs_mbe_full_680_default.png")


def plot_fim_norm_contexts() -> None:
    rows = [
        ("Image default", -0.662, -0.218),
        ("Image strict", -0.662, -0.383),
        ("Text default", -0.291, +0.014),
        ("Text strict", -0.291, +0.188),
        ("Full default", +0.225, -0.203),
        ("Full strict", +0.225, -0.300),
    ]
    labels = [r[0] for r in rows]
    raw = np.array([r[1] for r in rows])
    partial = np.array([r[2] for r in rows])
    x = np.arange(len(labels))
    width = 0.38

    plt.figure(figsize=(9.2, 4.8))
    plt.bar(x - width / 2, raw, width, label="Raw rho", color="#f58518")
    plt.bar(x + width / 2, partial, width, label="MBE partial rho", color="#4c78a8")
    plt.axhline(0, color="black", linewidth=0.8)
    plt.ylabel("Correlation with final accuracy")
    plt.title("FIM_norm changes conclusion across task and control set")
    plt.xticks(x, labels, rotation=25, ha="right")
    plt.legend(frameon=False)
    savefig("fim_norm_contexts.png")


def plot_family_heatmap() -> None:
    df = load_pooled("jmlr_full_confirmed_680_audit_summary.csv")
    df["family"] = df["metric"].map(FAMILY_MAP).fillna("other")
    table = pd.crosstab(df["family"], df["classification"])
    table = table.reindex(columns=CLASS_ORDER, fill_value=0)
    table = table.loc[table.sum(axis=1).sort_values(ascending=False).index]

    plt.figure(figsize=(8.5, 5.6))
    values = table.to_numpy()
    plt.imshow(values, aspect="auto", cmap="Blues")
    plt.colorbar(label="Metric count")
    plt.xticks(np.arange(len(table.columns)), table.columns, rotation=35, ha="right")
    plt.yticks(np.arange(len(table.index)), table.index)
    for i in range(values.shape[0]):
        for j in range(values.shape[1]):
            if values[i, j]:
                plt.text(j, i, str(values[i, j]), ha="center", va="center", color="black")
    plt.title("Metric family outcomes in full 680-model default audit")
    savefig("metric_family_class_heatmap.png")


def plot_default_vs_strict_counts() -> None:
    default = load_pooled("jmlr_full_confirmed_680_audit_summary.csv")
    strict = load_pooled("jmlr_full_confirmed_680_strict_loss_mbe_summary.csv")
    count_df = pd.DataFrame(
        {
            "Default": default["classification"].value_counts(),
            "Strict + val_loss": strict["classification"].value_counts(),
        }
    ).reindex(CLASS_ORDER).fillna(0)

    x = np.arange(len(count_df.index))
    width = 0.38
    plt.figure(figsize=(8.8, 4.8))
    plt.bar(x - width / 2, count_df["Default"], width, label="Default", color="#4c78a8")
    plt.bar(x + width / 2, count_df["Strict + val_loss"], width, label="Strict + val_loss", color="#54a24b")
    plt.xticks(x, count_df.index, rotation=30, ha="right")
    plt.ylabel("Metric count")
    plt.title("MBE class counts: full 680-model default vs strict audit")
    plt.legend(frameon=False)
    savefig("full_680_class_counts_default_vs_strict.png")


def main() -> int:
    plot_raw_vs_mbe()
    plot_fim_norm_contexts()
    plot_family_heatmap()
    plot_default_vs_strict_counts()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
