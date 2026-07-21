from __future__ import annotations

from numbers import Integral, Real
from typing import Sequence

import numpy as np
import pandas as pd
from pandas.api.types import is_bool_dtype, is_numeric_dtype

from .crossfit import cross_fitted_audit


def _require_column_name(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a non-empty column name")
    return value


def _require_non_negative_integer(value: object, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, Integral) or value < 0:
        raise ValueError(f"{label} must be a non-negative integer")
    return int(value)


def leave_one_environment_out_audit(
    df: pd.DataFrame,
    metric: str,
    target: str,
    controls: Sequence[str],
    *,
    environment: str,
    degree: int = 2,
    ridge: float = 1e-3,
    numeric_control_transform: str = "rank",
    permutations: int = 0,
    bootstrap: int = 0,
    seed: int = 0,
) -> dict[str, object]:
    """Run an experimental leave-one-environment-out MBE diagnostic.

    Each environment is held out as one cross-fitting fold. Models for the
    declared baseline and the metric-augmented baseline are therefore fitted
    only on other environments. The returned statistics describe transport in
    this dataset; they do not validate MBE or certify the benchmark construct.
    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")

    metric = _require_column_name(metric, "metric")
    target = _require_column_name(target, "target")
    environment = _require_column_name(environment, "environment")
    if len({metric, target, environment}) != 3:
        raise ValueError("metric, target, and environment must be distinct columns")

    if isinstance(controls, (str, bytes)) or not isinstance(controls, Sequence):
        raise TypeError("controls must be a sequence of column names")
    control_list = list(controls)
    if any(not isinstance(control, str) or not control.strip() for control in control_list):
        raise ValueError("controls must contain only non-empty column names")
    if len(set(control_list)) != len(control_list):
        raise ValueError("controls must not contain duplicate columns")
    if environment in control_list:
        raise ValueError("environment must not also be included in controls")
    if metric in control_list or target in control_list:
        raise ValueError("controls must not include the metric or target")

    required = [metric, target, *control_list, environment]
    missing = [column for column in required if column not in df.columns]
    if missing:
        raise ValueError(f"missing required columns: {', '.join(missing)}")

    for column, label in ((metric, "metric"), (target, "target")):
        if not is_numeric_dtype(df[column]) or is_bool_dtype(df[column]):
            raise ValueError(f"{label} column {column!r} must be numeric")

    if isinstance(degree, bool) or not isinstance(degree, Integral) or degree < 1:
        raise ValueError("degree must be a positive integer")
    if isinstance(ridge, bool) or not isinstance(ridge, Real):
        raise ValueError("ridge must be a finite non-negative number")
    ridge = float(ridge)
    if not np.isfinite(ridge) or ridge < 0:
        raise ValueError("ridge must be a finite non-negative number")
    if numeric_control_transform not in {"rank", "zscore"}:
        raise ValueError("numeric_control_transform must be 'rank' or 'zscore'")
    permutations = _require_non_negative_integer(permutations, "permutations")
    bootstrap = _require_non_negative_integer(bootstrap, "bootstrap")
    if isinstance(seed, bool) or not isinstance(seed, Integral):
        raise ValueError("seed must be an integer")

    clean = df[required].replace([np.inf, -np.inf], np.nan).dropna()
    environment_values = clean[environment].astype(str)
    environments = sorted(environment_values.unique().tolist())
    if len(environments) < 3:
        raise ValueError(
            "leave-one-environment-out audit requires at least three complete-case "
            "environments"
        )

    counts = environment_values.value_counts()
    sparse = sorted(counts[counts < 3].index.tolist())
    if sparse:
        raise ValueError(
            "each environment requires at least three complete rows; too few in: "
            + ", ".join(sparse)
        )

    result: dict[str, object] = dict(
        cross_fitted_audit(
            df,
            metric,
            target,
            control_list,
            group_col=environment,
            n_splits=len(environments),
            degree=int(degree),
            ridge=ridge,
            numeric_control_transform=numeric_control_transform,
            permutations=permutations,
            bootstrap=bootstrap,
            seed=int(seed),
        )
    )
    result.update(
        {
            "audit_mode": "leave-one-environment-out",
            "experimental": True,
            "environment_col": environment,
            "n_environments": len(environments),
            "environments": environments,
        }
    )
    return result


__all__ = ["leave_one_environment_out_audit"]
