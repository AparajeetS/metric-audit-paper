from __future__ import annotations

import math
from typing import Sequence

import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype


def _ridge_fit(x: np.ndarray, y: np.ndarray, alpha: float) -> np.ndarray:
    penalty = np.eye(x.shape[1], dtype=float) * alpha
    penalty[0, 0] = 0.0
    return np.linalg.pinv(x.T @ x + penalty) @ x.T @ y


def _numeric_block(
    train: pd.Series,
    test: pd.Series,
    degree: int,
) -> tuple[list[np.ndarray], list[np.ndarray]]:
    train_values = train.to_numpy(dtype=float)
    test_values = test.to_numpy(dtype=float)
    mean = float(np.mean(train_values))
    scale = float(np.std(train_values))
    if not np.isfinite(scale) or scale < 1e-12:
        scale = 1.0
    train_z = np.clip((train_values - mean) / scale, -8.0, 8.0)
    test_z = np.clip((test_values - mean) / scale, -8.0, 8.0)
    return (
        [np.power(train_z, power) for power in range(1, degree + 1)],
        [np.power(test_z, power) for power in range(1, degree + 1)],
    )


def _design_train_test(
    train: pd.DataFrame,
    test: pd.DataFrame,
    controls: Sequence[str],
    degree: int,
) -> tuple[np.ndarray, np.ndarray]:
    train_blocks: list[np.ndarray] = [np.ones(len(train), dtype=float)]
    test_blocks: list[np.ndarray] = [np.ones(len(test), dtype=float)]

    for control in controls:
        if is_numeric_dtype(train[control]):
            train_numeric, test_numeric = _numeric_block(
                train[control].astype(float),
                test[control].astype(float),
                degree,
            )
            train_blocks.extend(train_numeric)
            test_blocks.extend(test_numeric)
            continue

        train_values = train[control].astype(str)
        test_values = test[control].astype(str)
        levels = sorted(train_values.unique().tolist())
        for level in levels[1:]:
            train_blocks.append((train_values == level).to_numpy(dtype=float))
            test_blocks.append((test_values == level).to_numpy(dtype=float))

    return np.column_stack(train_blocks), np.column_stack(test_blocks)


def _rank_train_test(
    train: pd.Series,
    test: pd.Series,
) -> tuple[np.ndarray, np.ndarray]:
    """Map train and test values through the training-fold empirical CDF.

    Ties receive their mid-distribution value. Test values that were not seen in
    training receive their insertion percentile. Keeping the transform inside
    each fold prevents held-out outcomes or scores from influencing their own
    representation.
    """

    train_values = train.to_numpy(dtype=float)
    test_values = test.to_numpy(dtype=float)
    sorted_train = np.sort(train_values)
    denominator = float(len(sorted_train))

    def transform(values: np.ndarray) -> np.ndarray:
        left = np.searchsorted(sorted_train, values, side="left")
        right = np.searchsorted(sorted_train, values, side="right")
        return (left + right).astype(float) / (2.0 * denominator)

    return transform(train_values), transform(test_values)


def _fold_ids(
    df: pd.DataFrame,
    n_splits: int,
    seed: int,
    group_col: str | None,
) -> np.ndarray:
    rng = np.random.default_rng(seed)
    folds = np.empty(len(df), dtype=int)

    if group_col:
        groups = df[group_col].astype(str).to_numpy()
        unique_groups = np.unique(groups)
        if len(unique_groups) < 2:
            raise ValueError(f"group column {group_col!r} must contain at least two groups")
        rng.shuffle(unique_groups)
        split_count = min(n_splits, len(unique_groups))
        mapping = {group: i % split_count for i, group in enumerate(unique_groups)}
        return np.asarray([mapping[group] for group in groups], dtype=int)

    order = rng.permutation(len(df))
    split_count = min(n_splits, len(df))
    folds[order] = np.arange(len(df)) % split_count
    return folds


def _rank_correlation(a: np.ndarray, b: np.ndarray) -> float:
    a_rank = pd.Series(a).rank(method="average").to_numpy(dtype=float)
    b_rank = pd.Series(b).rank(method="average").to_numpy(dtype=float)
    if np.std(a_rank) <= 0 or np.std(b_rank) <= 0:
        return math.nan
    return float(np.corrcoef(a_rank, b_rank)[0, 1])


def _permutation_p_value(
    values: np.ndarray,
    target: np.ndarray,
    observed: float,
    permutations: int,
    rng: np.random.Generator,
    groups: np.ndarray | None,
) -> float:
    """Vectorized two-sided rank-permutation test.

    Permuting values does not change their global ranks, so ranking once is
    exactly equivalent to calling Spearman correlation after every shuffle.
    Group permutations are generated as one matrix to avoid a Python loop over
    groups for every replicate.
    """

    value_rank = pd.Series(values).rank(method="average").to_numpy(dtype=float)
    target_rank = pd.Series(target).rank(method="average").to_numpy(dtype=float)
    value_centered = value_rank - np.mean(value_rank)
    target_centered = target_rank - np.mean(target_rank)
    denominator = float(
        np.sqrt(np.sum(np.square(value_centered)) * np.sum(np.square(target_centered)))
    )
    if denominator <= 0 or not np.isfinite(observed):
        return math.nan

    permuted = np.empty((permutations, len(values)), dtype=float)
    if groups is None:
        order = np.argsort(rng.random((permutations, len(values))), axis=1)
        permuted[:] = value_rank[order]
    else:
        for group in np.unique(groups):
            idx = np.flatnonzero(groups == group)
            order = np.argsort(rng.random((permutations, len(idx))), axis=1)
            permuted[:, idx] = value_rank[idx][order]

    permuted_r = (permuted @ target_centered) / denominator
    exceedances = int(np.count_nonzero(np.abs(permuted_r) >= abs(observed)))
    return float((exceedances + 1) / (permutations + 1))


def cross_fitted_audit(
    df: pd.DataFrame,
    metric: str,
    target: str,
    controls: Sequence[str],
    *,
    group_col: str | None = None,
    n_splits: int = 5,
    degree: int = 2,
    ridge: float = 1e-3,
    permutations: int = 0,
    bootstrap: int = 0,
    seed: int = 0,
) -> dict[str, float | int | str]:
    """Estimate incremental metric signal with grouped cross-fitting.

    Numeric controls are expanded into a frozen polynomial basis within each
    training fold. Categorical controls are one-hot encoded from training-fold
    levels. The function reports out-of-fold residual dependence and the change
    in target mean-squared error from adding the metric to the baseline model.

    This is a compact reference implementation for protocol calibration. It is
    not a causal estimator and does not select the control set for the user.
    """

    if n_splits < 2:
        raise ValueError("n_splits must be at least 2")
    if degree < 1:
        raise ValueError("degree must be at least 1")

    controls = list(dict.fromkeys(c for c in controls if c not in {metric, target}))
    required = [metric, target, *controls]
    if group_col:
        required.append(group_col)
    missing = [column for column in required if column not in df.columns]
    if missing:
        raise ValueError(f"missing required columns: {', '.join(missing)}")

    clean = (
        df[required]
        .replace([np.inf, -np.inf], np.nan)
        .dropna()
        .reset_index(drop=True)
    )
    if len(clean) < max(20, n_splits * 3):
        raise ValueError("cross-fitted audit requires at least 20 complete rows")

    fold_ids = _fold_ids(clean, n_splits, seed, group_col)
    target_rank = np.full(len(clean), np.nan, dtype=float)
    metric_rank = np.full(len(clean), np.nan, dtype=float)
    target_pred = np.full(len(clean), np.nan, dtype=float)
    metric_pred = np.full(len(clean), np.nan, dtype=float)
    augmented_pred = np.full(len(clean), np.nan, dtype=float)

    for fold in np.unique(fold_ids):
        test_idx = np.flatnonzero(fold_ids == fold)
        train_idx = np.flatnonzero(fold_ids != fold)
        train = clean.iloc[train_idx]
        test = clean.iloc[test_idx]
        target_train_rank, target_test_rank = _rank_train_test(
            train[target], test[target]
        )
        metric_train_rank, metric_test_rank = _rank_train_test(
            train[metric], test[metric]
        )
        target_rank[test_idx] = target_test_rank
        metric_rank[test_idx] = metric_test_rank
        x_train, x_test = _design_train_test(train, test, controls, degree)
        metric_train_blocks, metric_test_blocks = _numeric_block(
            pd.Series(metric_train_rank),
            pd.Series(metric_test_rank),
            degree,
        )
        x_aug_train = np.column_stack([x_train, *metric_train_blocks])
        x_aug_test = np.column_stack([x_test, *metric_test_blocks])

        target_beta = _ridge_fit(x_train, target_train_rank, ridge)
        metric_beta = _ridge_fit(x_train, metric_train_rank, ridge)
        augmented_beta = _ridge_fit(x_aug_train, target_train_rank, ridge)
        target_pred[test_idx] = x_test @ target_beta
        metric_pred[test_idx] = x_test @ metric_beta
        augmented_pred[test_idx] = x_aug_test @ augmented_beta

    target_residual = target_rank - target_pred
    metric_residual = metric_rank - metric_pred
    run_residual_r = _rank_correlation(metric_residual, target_residual)
    baseline_squared_error = np.square(target_rank - target_pred)
    augmented_squared_error = np.square(target_rank - augmented_pred)

    inference_metric = metric_residual
    inference_target = target_residual
    if group_col:
        cluster = pd.DataFrame(
            {
                "group": clean[group_col].astype(str).to_numpy(),
                "metric_residual": metric_residual,
                "target_residual": target_residual,
                "baseline_squared_error": baseline_squared_error,
                "augmented_squared_error": augmented_squared_error,
            }
        ).groupby("group", sort=True).mean()
        inference_metric = cluster["metric_residual"].to_numpy(dtype=float)
        inference_target = cluster["target_residual"].to_numpy(dtype=float)
        inference_baseline_error = cluster["baseline_squared_error"].to_numpy(dtype=float)
        inference_augmented_error = cluster["augmented_squared_error"].to_numpy(dtype=float)
    else:
        inference_baseline_error = baseline_squared_error
        inference_augmented_error = augmented_squared_error

    residual_r = _rank_correlation(inference_metric, inference_target)
    baseline_mse = float(np.mean(inference_baseline_error))
    augmented_mse = float(np.mean(inference_augmented_error))

    permutation_p = math.nan
    if permutations > 0:
        rng = np.random.default_rng(seed + 1_000_003)
        permutation_p = _permutation_p_value(
            inference_metric,
            inference_target,
            residual_r,
            permutations,
            rng,
            None,
        )

    residual_ci_low = math.nan
    residual_ci_high = math.nan
    delta_mse_ci_low = math.nan
    delta_mse_ci_high = math.nan
    if bootstrap > 0:
        rng = np.random.default_rng(seed + 2_000_003)
        unit_count = len(inference_metric)
        draws = rng.integers(0, unit_count, size=(bootstrap, unit_count))
        metric_rank = pd.Series(inference_metric).rank(method="average").to_numpy(dtype=float)
        target_rank = pd.Series(inference_target).rank(method="average").to_numpy(dtype=float)
        sampled_metric = metric_rank[draws]
        sampled_target = target_rank[draws]
        sampled_metric -= sampled_metric.mean(axis=1, keepdims=True)
        sampled_target -= sampled_target.mean(axis=1, keepdims=True)
        numerators = np.sum(sampled_metric * sampled_target, axis=1)
        denominators = np.sqrt(
            np.sum(np.square(sampled_metric), axis=1)
            * np.sum(np.square(sampled_target), axis=1)
        )
        bootstrap_r = np.divide(
            numerators,
            denominators,
            out=np.full(bootstrap, np.nan, dtype=float),
            where=denominators > 0,
        )
        bootstrap_delta = np.mean(
            inference_baseline_error[draws] - inference_augmented_error[draws],
            axis=1,
        )
        residual_ci_low, residual_ci_high = np.nanquantile(bootstrap_r, [0.025, 0.975])
        delta_mse_ci_low, delta_mse_ci_high = np.nanquantile(
            bootstrap_delta, [0.025, 0.975]
        )

    return {
        "metric": metric,
        "target": target,
        "controls": ",".join(controls),
        "group_col": group_col or "",
        "n": len(clean),
        "independence_units": len(inference_metric),
        "n_splits": int(len(np.unique(fold_ids))),
        "polynomial_degree": degree,
        "run_residual_r": run_residual_r,
        "residual_r": residual_r,
        "residual_p": permutation_p,
        "residual_ci_low": float(residual_ci_low),
        "residual_ci_high": float(residual_ci_high),
        "baseline_mse": baseline_mse,
        "augmented_mse": augmented_mse,
        "delta_mse": baseline_mse - augmented_mse,
        "delta_mse_ci_low": float(delta_mse_ci_low),
        "delta_mse_ci_high": float(delta_mse_ci_high),
        "relative_mse_improvement": (baseline_mse - augmented_mse) / baseline_mse
        if baseline_mse > 0
        else math.nan,
    }


__all__ = ["cross_fitted_audit"]
