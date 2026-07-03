from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd


DEFAULT_COLUMNS = [
    "metric",
    "n",
    "raw_r",
    "partial_r",
    "delta_partial_minus_raw",
    "classification",
]


def summarize_audit(report: pd.DataFrame, columns: Iterable[str] | None = None) -> pd.DataFrame:
    """Return a compact, sorted view of an MBE audit dataframe."""

    if report.empty:
        return pd.DataFrame(columns=list(columns or DEFAULT_COLUMNS))
    selected = [c for c in (columns or DEFAULT_COLUMNS) if c in report.columns]
    summary = report[selected].copy()
    if "partial_r" in summary.columns:
        summary = summary.sort_values("partial_r", key=lambda s: s.abs(), ascending=False)
    return summary.reset_index(drop=True)


def _fmt(value: object) -> str:
    if isinstance(value, float):
        return f"{value:+.3f}" if abs(value) < 10 else f"{value:.3f}"
    return str(value)


def audit_report_markdown(
    report: pd.DataFrame,
    *,
    title: str = "MBE Audit Report",
    target: str | None = None,
    controls: Iterable[str] | None = None,
    notes: Iterable[str] | None = None,
) -> str:
    """Render a compact markdown report from `audit_metrics` output."""

    lines = [f"# {title}", ""]
    if target:
        lines.append(f"- Target: `{target}`")
    if controls:
        lines.append(f"- Controls: {', '.join(f'`{c}`' for c in controls)}")
    if notes:
        for note in notes:
            lines.append(f"- {note}")
    if len(lines) > 2:
        lines.append("")

    summary = summarize_audit(report)
    if summary.empty:
        lines.extend(["No audit rows were available.", ""])
        return "\n".join(lines)

    lines.extend(
        [
            "| Metric | n | Raw rho | MBE partial rho | Delta | Class |",
            "|---|---:|---:|---:|---:|---|",
        ]
    )
    for _, row in summary.iterrows():
        lines.append(
            "| `{metric}` | {n} | {raw} | {partial} | {delta} | {classification} |".format(
                metric=row.get("metric", ""),
                n=row.get("n", ""),
                raw=_fmt(row.get("raw_r", "")),
                partial=_fmt(row.get("partial_r", "")),
                delta=_fmt(row.get("delta_partial_minus_raw", "")),
                classification=row.get("classification", ""),
            )
        )

    counts = report["classification"].value_counts().to_dict() if "classification" in report else {}
    if counts:
        counts_text = ", ".join(f"{label}: {count}" for label, count in sorted(counts.items()))
        lines.extend(["", f"Class counts: {counts_text}."])

    return "\n".join(lines) + "\n"


def write_markdown_report(report: pd.DataFrame, path: str | Path, **kwargs) -> Path:
    """Write `audit_report_markdown` output and return the resolved path."""

    output = Path(path)
    output.write_text(audit_report_markdown(report, **kwargs), encoding="utf-8")
    return output


__all__ = ["audit_report_markdown", "summarize_audit", "write_markdown_report"]
