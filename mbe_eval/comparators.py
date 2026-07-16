from __future__ import annotations

from itertools import combinations
import math
from typing import Sequence

import numpy as np
import pandas as pd
from scipy.stats import kendalltau


def kendall_rank_correlation(values: Sequence[float], target: Sequence[float]) -> float:
    """Return Kendall's tau-b, including tie correction."""
    result = kendalltau(np.asarray(values, dtype=float), np.asarray(target, dtype=float))
    return float(result.statistic)


def _configuration_frame(
    df: pd.DataFrame,
    metric: str,
    target: str,
    hyperparameters: Sequence[str],
    group_col: str | None,
) -> pd.DataFrame:
    required = [metric, target, *hyperparameters]
    if group_col:
        required.append(group_col)
    missing = [column for column in required if column not in df.columns]
    if missing:
        raise ValueError(f"missing required columns: {', '.join(missing)}")
    clean = df[required].replace([np.inf, -np.inf], np.nan).dropna().copy()
    if group_col:
        inconsistent = clean.groupby(group_col, sort=False)[list(hyperparameters)].nunique()
        if (inconsistent > 1).any(axis=None):
            raise ValueError("each configuration group must have fixed hyperparameters")
        aggregations = {metric: "mean", target: "mean"}
        aggregations.update({column: "first" for column in hyperparameters})
        clean = clean.groupby(group_col, sort=True, as_index=False).agg(aggregations)
    return clean.reset_index(drop=True)


def granulated_kendall(
    df: pd.DataFrame,
    metric: str,
    target: str,
    hyperparameters: Sequence[str],
    *,
    group_col: str | None = None,
    minimum_axis_levels: int = 2,
) -> tuple[float, pd.DataFrame]:
    """Compute Jiang et al.'s granulated Kendall coefficient.

    For each hyperparameter axis, all other hyperparameters are held fixed and
    tau-b is computed within every complete observable cell. Cell coefficients
    receive equal weight, matching the published factorial definition.
    """
    hyperparameters = list(dict.fromkeys(hyperparameters))
    if not hyperparameters:
        raise ValueError("at least one hyperparameter is required")
    frame = _configuration_frame(df, metric, target, hyperparameters, group_col)
    rows: list[dict[str, float | int | str]] = []
    for axis in hyperparameters:
        held_fixed = [column for column in hyperparameters if column != axis]
        grouped = [("all", frame)] if not held_fixed else frame.groupby(held_fixed, dropna=False)
        cell_values: list[float] = []
        eligible = 0
        for _, cell in grouped:
            if cell[axis].nunique() < minimum_axis_levels:
                continue
            eligible += 1
            value = kendall_rank_correlation(cell[metric], cell[target])
            if np.isfinite(value):
                cell_values.append(value)
        axis_value = float(np.mean(cell_values)) if cell_values else math.nan
        rows.append(
            {
                "hyperparameter": axis,
                "granulated_kendall": axis_value,
                "eligible_cells": eligible,
                "finite_cells": len(cell_values),
            }
        )
    detail = pd.DataFrame(rows)
    finite = detail["granulated_kendall"].dropna().to_numpy(dtype=float)
    overall = float(np.mean(finite)) if len(finite) else math.nan
    return overall, detail


def _conditional_information(
    metric_order: np.ndarray,
    target_order: np.ndarray,
    condition_codes: np.ndarray,
) -> tuple[float, float, int]:
    condition_codes = np.asarray(condition_codes, dtype=int)
    condition_count = int(condition_codes.max()) + 1
    categories = metric_order.astype(int) * 2 + target_order.astype(int)
    counts = np.bincount(
        condition_codes * 4 + categories,
        minlength=condition_count * 4,
    ).reshape(condition_count, 2, 2).astype(float)
    condition_totals = counts.sum(axis=(1, 2))
    metric_totals = counts.sum(axis=2)
    target_totals = counts.sum(axis=1)
    total = float(condition_totals.sum())

    mutual_information = 0.0
    for metric_value in range(2):
        for target_value in range(2):
            joint = counts[:, metric_value, target_value]
            denominator = (
                metric_totals[:, metric_value] * target_totals[:, target_value]
            )
            valid = (joint > 0) & (denominator > 0)
            mutual_information += float(
                np.sum(
                    joint[valid]
                    / total
                    * np.log(
                        joint[valid]
                        * condition_totals[valid]
                        / denominator[valid]
                    )
                )
            )

    conditional_entropy = 0.0
    for target_value in range(2):
        count = target_totals[:, target_value]
        valid = count > 0
        conditional_entropy -= float(
            np.sum(
                count[valid]
                / total
                * np.log(count[valid] / condition_totals[valid])
            )
        )
    return mutual_information, conditional_entropy, condition_count


def jiang_normalized_cmi(
    df: pd.DataFrame,
    metric: str,
    target: str,
    hyperparameters: Sequence[str],
    *,
    group_col: str | None = None,
    max_conditioning: int = 2,
) -> tuple[float, pd.DataFrame]:
    """Compute the pairwise normalized CMI criterion of Jiang et al. (2020).

    Ordered configuration pairs define binary variables indicating whether the
    first metric/target value exceeds the second. For each conditioning subset,
    U_S contains both configurations' observed values for every selected
    hyperparameter. The headline K score is the minimum normalized CMI over all
    subsets with size at most ``max_conditioning``.

    This is a descriptive plug-in estimator, not a calibrated independence test.
    """
    hyperparameters = list(dict.fromkeys(hyperparameters))
    if not hyperparameters:
        raise ValueError("at least one hyperparameter is required")
    if max_conditioning < 0:
        raise ValueError("max_conditioning must be nonnegative")
    frame = _configuration_frame(df, metric, target, hyperparameters, group_col)
    if len(frame) < 3:
        raise ValueError("Jiang CMI requires at least three configurations")

    left, right = np.where(~np.eye(len(frame), dtype=bool))
    metric_values = frame[metric].to_numpy(dtype=float)
    target_values = frame[target].to_numpy(dtype=float)
    metric_order = metric_values[left] > metric_values[right]
    target_order = target_values[left] > target_values[right]

    rows: list[dict[str, float | int | str]] = []
    maximum = min(max_conditioning, len(hyperparameters))
    for size in range(maximum + 1):
        for subset in combinations(hyperparameters, size):
            if not subset:
                codes = np.zeros(len(left), dtype=int)
            else:
                condition = pd.DataFrame(
                    {
                        f"a:{column}": frame[column].to_numpy()[left]
                        for column in subset
                    }
                    | {
                        f"b:{column}": frame[column].to_numpy()[right]
                        for column in subset
                    }
                )
                codes = pd.MultiIndex.from_frame(condition).factorize()[0]
            information, entropy, conditions = _conditional_information(
                metric_order, target_order, codes
            )
            normalized = information / entropy if entropy > 1e-15 else math.nan
            rows.append(
                {
                    "conditioning": ",".join(subset) if subset else "none",
                    "conditioning_size": size,
                    "normalized_cmi": normalized,
                    "conditional_mutual_information": information,
                    "target_conditional_entropy": entropy,
                    "conditions": conditions,
                    "ordered_pairs": len(left),
                }
            )
    detail = pd.DataFrame(rows)
    finite = detail["normalized_cmi"].dropna().to_numpy(dtype=float)
    score = float(np.min(finite)) if len(finite) else math.nan
    return score, detail


__all__ = [
    "granulated_kendall",
    "jiang_normalized_cmi",
    "kendall_rank_correlation",
]
