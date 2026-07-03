from __future__ import annotations

import pandas as pd

from .demo import run_demo
from .reporting import summarize_audit


def simulate_mbe_evaluation(seed: int = 42) -> pd.DataFrame:
    """Backward-compatible synthetic MBE demo."""

    report = run_demo(seed=seed, bootstrap=0, output=None)
    print(summarize_audit(report).to_string(index=False))
    return report


if __name__ == "__main__":
    simulate_mbe_evaluation()
