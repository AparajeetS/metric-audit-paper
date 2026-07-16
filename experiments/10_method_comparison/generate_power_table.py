from __future__ import annotations

import argparse
from pathlib import Path
import sys

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from mbe_eval import audit_power_diagnostic  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate per-task power diagnostics.")
    parser.add_argument("metadata_floor", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    source = pd.read_csv(args.metadata_floor)
    rows = []
    for task, group in source.groupby("task", sort=True):
        units = int(group["n"].iloc[0])
        diagnostic = audit_power_diagnostic(units)
        diagnostic.insert(0, "task", task)
        rows.append(diagnostic)
    report = pd.concat(rows, ignore_index=True)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    report.to_csv(args.output_dir / "pgdl_power_diagnostic.csv", index=False)
    lines = [
        "# PGDL Approximate Power Diagnostic",
        "",
        "These are Fisher-z approximations for a two-sided correlation test at alpha 0.05. They are planning aids, not post-hoc proof that the full joint MBE decision has this power.",
        "",
        "| Task | Independent units | Target power | Approximate minimum detectable |",
        "|---|---:|---:|---:|",
    ]
    for _, row in report.iterrows():
        lines.append(
            f"| {row['task']} | {int(row['independence_units'])} | "
            f"{row['power']:.0%} | {row['minimum_detectable_abs_correlation']:.3f} |"
        )
    (args.output_dir / "PGDL_POWER_DIAGNOSTIC.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )
    print(report.to_string(index=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
