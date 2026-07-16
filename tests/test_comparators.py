import numpy as np
import pandas as pd
import pytest

from mbe_eval.comparators import granulated_kendall, jiang_normalized_cmi


def factorial_frame(repeats: int = 2) -> pd.DataFrame:
    rows = []
    for a in range(3):
        for b in range(3):
            for repeat in range(repeats):
                rows.append(
                    {
                        "config": f"{a}-{b}",
                        "a": a,
                        "b": b,
                        "target": 2 * a + b + repeat * 0.01,
                        "metric": 2 * a + b + repeat * 0.01,
                    }
                )
    return pd.DataFrame(rows)


def test_granulated_kendall_recovers_consistent_factorial_ordering() -> None:
    score, detail = granulated_kendall(
        factorial_frame(), "metric", "target", ["a", "b"], group_col="config"
    )
    assert score == pytest.approx(1.0)
    assert (detail["finite_cells"] == 3).all()


def test_jiang_cmi_is_high_for_identical_pairwise_ordering() -> None:
    score, detail = jiang_normalized_cmi(
        factorial_frame(), "metric", "target", ["a", "b"], group_col="config"
    )
    assert score == pytest.approx(1.0)
    assert set(detail["conditioning_size"]) == {0, 1, 2}


def test_comparators_reject_inconsistent_group_hyperparameters() -> None:
    frame = factorial_frame()
    frame.loc[1, "a"] = 99
    with pytest.raises(ValueError, match="fixed hyperparameters"):
        granulated_kendall(frame, "metric", "target", ["a", "b"], group_col="config")


def test_jiang_cmi_null_is_small_in_balanced_factorial() -> None:
    frame = factorial_frame(repeats=1)
    frame["metric"] = np.tile([0.0, 1.0, 2.0], 3)
    frame["target"] = np.repeat([0.0, 1.0, 2.0], 3)
    score, _ = jiang_normalized_cmi(frame, "metric", "target", ["a", "b"])
    assert score < 0.05
