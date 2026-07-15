import numpy as np
import pandas as pd
import pytest

from mbe_eval.crossfit import _rank_train_test, cross_fitted_audit


def _synthetic_runs(seed: int = 4, n: int = 360) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    capability = rng.normal(size=n)
    independent_signal = rng.normal(size=n)
    target = 0.9 * capability + 0.8 * independent_signal + rng.normal(0, 0.15, n)
    return pd.DataFrame(
        {
            "capability": capability,
            "target": target,
            "confounded_score": capability + rng.normal(0, 0.08, n),
            "incremental_score": independent_signal + rng.normal(0, 0.08, n),
            "model_family": [f"family-{i % 12}" for i in range(n)],
        }
    )


def test_cross_fitting_separates_confounded_and_incremental_scores():
    runs = _synthetic_runs()

    confounded = cross_fitted_audit(
        runs,
        "confounded_score",
        "target",
        ["capability"],
        seed=12,
    )
    incremental = cross_fitted_audit(
        runs,
        "incremental_score",
        "target",
        ["capability"],
        seed=12,
    )

    assert abs(confounded["run_residual_r"]) < 0.2
    assert confounded["delta_mse"] < 0.01
    assert incremental["run_residual_r"] > 0.8
    assert incremental["delta_mse"] > 0.03


def test_grouped_cross_fitting_reports_independent_groups():
    runs = _synthetic_runs()
    result = cross_fitted_audit(
        runs,
        "incremental_score",
        "target",
        ["capability"],
        group_col="model_family",
        n_splits=4,
        seed=2,
    )

    assert result["n"] == len(runs)
    assert result["independence_units"] == 12
    assert result["n_splits"] == 4
    assert result["group_col"] == "model_family"
    assert result["run_residual_r"] > 0.8


def test_cross_fitting_seeded_inference_is_reproducible():
    runs = _synthetic_runs(n=240)
    kwargs = {
        "metric": "incremental_score",
        "target": "target",
        "controls": ["capability"],
        "permutations": 39,
        "bootstrap": 40,
        "seed": 8,
    }

    first = cross_fitted_audit(runs, **kwargs)
    second = cross_fitted_audit(runs, **kwargs)

    for key in (
        "residual_r",
        "residual_p",
        "residual_ci_low",
        "residual_ci_high",
        "delta_mse_ci_low",
        "delta_mse_ci_high",
    ):
        assert first[key] == pytest.approx(second[key])


def test_cross_fitting_rejects_too_few_complete_rows():
    runs = _synthetic_runs(n=19)

    with pytest.raises(ValueError, match="at least 20 complete rows"):
        cross_fitted_audit(
            runs,
            "incremental_score",
            "target",
            ["capability"],
        )


def test_rank_transform_is_fitted_only_on_training_fold():
    train_rank, test_rank = _rank_train_test(
        pd.Series([0.0, 0.0, 2.0, 4.0]),
        pd.Series([-10.0, 0.0, 1.0, 10.0]),
    )

    assert train_rank.tolist() == pytest.approx([0.25, 0.25, 0.625, 0.875])
    assert test_rank.tolist() == pytest.approx([0.0, 0.25, 0.5, 1.0])
