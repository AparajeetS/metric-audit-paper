import json

import pandas as pd

from mbe_eval.claim_cli import audit_claim_csv
from mbe_eval.claim_demo import make_claim_demo, run_claim_demo


def test_claim_csv_writes_json_markdown_and_source_hash(tmp_path):
    csv_path = tmp_path / "input.csv"
    output_prefix = tmp_path / "claim"
    make_claim_demo(n_units=24).to_csv(csv_path, index=False)

    card = audit_claim_csv(
        csv_path,
        claim_id="cli-fixture",
        claim_text="A deliberately scoped synthetic claim.",
        metric="benchmark_score",
        target="external_outcome",
        baselines=["capability_proxy"],
        environment="environment",
        unit="model_id",
        n_splits=5,
        permutations=0,
        bootstrap=0,
        seed=7,
        source_url="https://example.org/dataset",
        source_version="fixture-v1",
        output_prefix=output_prefix,
    )

    parsed = json.loads((tmp_path / "claim.json").read_text(encoding="utf-8"))
    assert (tmp_path / "claim.md").exists()
    assert len(card["source"]["sha256"]) == 64
    assert parsed["source"]["url"] == "https://example.org/dataset"
    assert parsed["source"]["version"] == "fixture-v1"


def test_demo_generator_is_deterministic_and_runner_is_end_to_end(tmp_path):
    pd.testing.assert_frame_equal(make_claim_demo(24), make_claim_demo(24))

    card = run_claim_demo(
        output_dir=tmp_path / "demo",
        n_units=24,
        permutations=0,
        bootstrap=39,
        seed=20260715,
    )

    assert card["method_status"] == "experimental"
    assert (tmp_path / "demo" / "synthetic_benchmark_audit.csv").exists()
    assert (tmp_path / "demo" / "claim_card.json").exists()
    assert (tmp_path / "demo" / "claim_card.md").exists()
