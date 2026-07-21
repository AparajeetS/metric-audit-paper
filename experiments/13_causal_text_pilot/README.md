# Corrected Causal-Language Pipeline Pilot

Status: timeboxed implementation pilot, not inferential evidence.

This Kaggle job performs two essential checks before the corrected text
factorial:

1. a future-token perturbation test that must leave prefix logits unchanged,
   paired with an unmasked negative control that must fail;
2. a restartable WikiText-2 run grid over small and medium causal Transformers.

The grid uses the official train, validation, and test splits, keeps model
configuration and seed identifiers separate, and stops with a wall-clock
reserve before Kaggle's session limit. Completed rows are flushed immediately.

Primary pilot outputs:

- `causal_mask_leakage_test.json`
- `mbe2_causal_text_pilot_manifest.json`
- `mbe2_causal_text_pilot.csv`

The pilot validates leakage controls, schema, metric extraction, runtime, and
failure handling. It does not support metric-family or selector claims.
