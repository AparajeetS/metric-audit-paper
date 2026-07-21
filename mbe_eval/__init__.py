from .core import (
    MBEEvaluator,
    MBEInputError,
    MBEReport,
    audit_metric,
    audit_metrics,
    classify_effect,
    partial_rank_corr,
    spearman_corr,
    validate_audit_inputs,
)
from .reporting import audit_report_markdown, summarize_audit, write_markdown_report
from .crossfit import (
    classify_increment_evidence,
    classify_predictive_increment,
    cross_fitted_audit,
    refit_bootstrap_audit,
    repeated_cross_fitted_audit,
)
from .calibration import make_calibration_ledger, run_calibration, run_monte_carlo_calibration
from .reaudit import run_manifest_reaudit, run_published_reaudit, validate_study_manifest
from .robust_sign_error import robust_sign_error_environments, robust_sign_error_summary
from .checkpoint_metrics import summarize_checkpoint_pair
from .comparators import granulated_kendall, jiang_normalized_cmi, kendall_rank_correlation
from .diagnostics import abstention_reasons, audit_power_diagnostic, minimum_detectable_correlation
from .selection import (
    coverage_regret_curve,
    leave_one_task_out_global_choice,
    score_recommendations,
)
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("mbe-eval")
except PackageNotFoundError:
    __version__ = "0+unknown"

__all__ = [
    "__version__",
    "MBEEvaluator",
    "MBEReport",
    "MBEInputError",
    "audit_csv",
    "audit_claim_csv",
    "audit_benchmark_claim",
    "audit_report_markdown",
    "audit_metric",
    "audit_metrics",
    "classify_effect",
    "claim_card_json",
    "claim_card_markdown",
    "compare_benchmark_claim_specs",
    "leave_one_environment_out_audit",
    "make_claim_demo",
    "cross_fitted_audit",
    "classify_increment_evidence",
    "classify_predictive_increment",
    "repeated_cross_fitted_audit",
    "refit_bootstrap_audit",
    "make_demo_runs",
    "granulated_kendall",
    "abstention_reasons",
    "audit_power_diagnostic",
    "jiang_normalized_cmi",
    "kendall_rank_correlation",
    "minimum_detectable_correlation",
    "make_calibration_ledger",
    "partial_rank_corr",
    "run_demo",
    "run_claim_demo",
    "run_calibration",
    "run_monte_carlo_calibration",
    "run_manifest_reaudit",
    "run_published_reaudit",
    "robust_sign_error_environments",
    "robust_sign_error_summary",
    "summarize_audit",
    "spearman_corr",
    "summarize_checkpoint_pair",
    "coverage_regret_curve",
    "leave_one_task_out_global_choice",
    "score_recommendations",
    "simulate_mbe_evaluation",
    "validate_study_manifest",
    "write_markdown_report",
    "validate_audit_inputs",
]


def __getattr__(name):
    if name == "simulate_mbe_evaluation":
        from .sample_eval import simulate_mbe_evaluation

        return simulate_mbe_evaluation
    if name == "audit_csv":
        from .cli import audit_csv

        return audit_csv
    if name == "audit_claim_csv":
        from .claim_cli import audit_claim_csv

        return audit_claim_csv
    if name in {"audit_benchmark_claim", "claim_card_json", "claim_card_markdown"}:
        from .claim_card import (
            audit_benchmark_claim,
            claim_card_json,
            claim_card_markdown,
        )

        return {
            "audit_benchmark_claim": audit_benchmark_claim,
            "claim_card_json": claim_card_json,
            "claim_card_markdown": claim_card_markdown,
        }[name]
    if name == "compare_benchmark_claim_specs":
        from .contestation import compare_benchmark_claim_specs

        return compare_benchmark_claim_specs
    if name == "cross_fitted_audit":
        from .crossfit import cross_fitted_audit

        return cross_fitted_audit
    if name == "leave_one_environment_out_audit":
        from .transport import leave_one_environment_out_audit

        return leave_one_environment_out_audit
    if name in {"make_claim_demo", "run_claim_demo"}:
        from .claim_demo import make_claim_demo, run_claim_demo

        return {"make_claim_demo": make_claim_demo, "run_claim_demo": run_claim_demo}[name]
    if name in {"make_demo_runs", "run_demo"}:
        from .demo import make_demo_runs, run_demo

        return {"make_demo_runs": make_demo_runs, "run_demo": run_demo}[name]
    raise AttributeError(f"module 'mbe_eval' has no attribute {name!r}")
