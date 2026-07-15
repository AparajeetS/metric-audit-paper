import numpy as np
import pandas as pd
import pytest

import mbe_eval.transport as transport
from mbe_eval.transport import leave_one_environment_out_audit


def _transport_frame(seed: int = 19, environments: int = 4, per_environment: int = 60):
    rng = np.random.default_rng(seed)
    rows = []
    for index in range(environments):
        capability = rng.normal(index * 0.25, 1.0, per_environment)
        independent_signal = rng.normal(size=per_environment)
        target = (
            0.75 * capability
            + 0.65 * independent_signal
            + index * 0.1
            + rng.normal(0, 0.15, per_environment)
        )
        rows.append(
            pd.DataFrame(
                {
                    "environment": f"env-{index}",
                    "capability": capability,
                    "benchmark_score": independent_signal
                    + rng.normal(0, 0.08, per_environment),
                    "target": target,
                }
            )
        )
    return pd.concat(rows, ignore_index=True)


def test_transport_audit_uses_each_environment_as_a_held_out_fold(monkeypatch):
    frame = _transport_frame()
    captured = {}

    def fake_cross_fitted_audit(*args, **kwargs):
        captured["args"] = args
        captured["kwargs"] = kwargs
        return {"metric": args[1], "target": args[2], "delta_mse": 0.1}

    monkeypatch.setattr(transport, "cross_fitted_audit", fake_cross_fitted_audit)
    result = leave_one_environment_out_audit(
        frame,
        "benchmark_score",
        "target",
        ["capability"],
        environment="environment",
        seed=7,
    )

    assert captured["kwargs"]["group_col"] == "environment"
    assert captured["kwargs"]["n_splits"] == 4
    assert result["audit_mode"] == "leave-one-environment-out"
    assert result["experimental"] is True
    assert result["n_environments"] == 4
    assert result["environments"] == ["env-0", "env-1", "env-2", "env-3"]


def test_transport_audit_runs_end_to_end():
    frame = _transport_frame()
    result = leave_one_environment_out_audit(
        frame,
        "benchmark_score",
        "target",
        ["capability"],
        environment="environment",
        seed=3,
    )

    assert result["group_col"] == "environment"
    assert result["independence_units"] == 4
    assert result["n_splits"] == 4
    assert result["delta_mse"] > 0
    assert result["run_residual_r"] > 0.7


def test_transport_audit_requires_three_environments():
    frame = _transport_frame(environments=2)

    with pytest.raises(ValueError, match="at least three"):
        leave_one_environment_out_audit(
            frame,
            "benchmark_score",
            "target",
            ["capability"],
            environment="environment",
        )


def test_transport_audit_rejects_environment_as_a_control():
    frame = _transport_frame()

    with pytest.raises(ValueError, match="must not also be included in controls"):
        leave_one_environment_out_audit(
            frame,
            "benchmark_score",
            "target",
            ["capability", "environment"],
            environment="environment",
        )


def test_transport_audit_rejects_sparse_or_nonnumeric_inputs():
    sparse = _transport_frame(per_environment=4)
    sparse = sparse.drop(sparse[sparse["environment"] == "env-0"].index[2:])
    with pytest.raises(ValueError, match="at least three complete rows"):
        leave_one_environment_out_audit(
            sparse,
            "benchmark_score",
            "target",
            ["capability"],
            environment="environment",
        )

    nonnumeric = _transport_frame()
    nonnumeric["benchmark_score"] = "not-a-number"
    with pytest.raises(ValueError, match="must be numeric"):
        leave_one_environment_out_audit(
            nonnumeric,
            "benchmark_score",
            "target",
            ["capability"],
            environment="environment",
        )
