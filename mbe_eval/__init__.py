from .core import (
    MBEEvaluator,
    MBEReport,
    audit_metric,
    audit_metrics,
    classify_effect,
    partial_rank_corr,
    spearman_corr,
)
from .reporting import audit_report_markdown, summarize_audit, write_markdown_report

__version__ = "0.3.2"

__all__ = [
    "__version__",
    "MBEEvaluator",
    "MBEReport",
    "audit_csv",
    "audit_report_markdown",
    "audit_metric",
    "audit_metrics",
    "classify_effect",
    "make_demo_runs",
    "partial_rank_corr",
    "run_demo",
    "summarize_audit",
    "spearman_corr",
    "simulate_mbe_evaluation",
    "write_markdown_report",
]


def __getattr__(name):
    if name == "simulate_mbe_evaluation":
        from .sample_eval import simulate_mbe_evaluation

        return simulate_mbe_evaluation
    if name == "audit_csv":
        from .cli import audit_csv

        return audit_csv
    if name in {"make_demo_runs", "run_demo"}:
        from .demo import make_demo_runs, run_demo

        return {"make_demo_runs": make_demo_runs, "run_demo": run_demo}[name]
    raise AttributeError(f"module 'mbe_eval' has no attribute {name!r}")
