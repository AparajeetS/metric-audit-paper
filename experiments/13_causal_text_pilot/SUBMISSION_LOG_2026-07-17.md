# Kaggle Submission Log: Corrected Causal Text Pilot

- Submitted: 2026-07-17 (Asia/Calcutta)
- Kaggle version 1: completed with zero valid training rows because Kaggle's
  preinstalled PyTorch wheel had no compatible CUDA kernel image for the P100.
  The failure artifacts are retained and are not evidence.
- Kaggle version 2: completed with zero valid training rows. The CUDA wheel and
  causal leakage preflight passed, but the first training cell failed with a
  device-side assertion. WikiText contains the literal `<unk>` token; the
  vocabulary list inserted it twice and dictionary conversion then left the
  largest token ID one past the embedding boundary. The failure artifacts are
  retained under `experiments/13_causal_text_pilot_runs/v2` and are not
  evidence.
- Kaggle version 3: excludes `<unk>` from the sorted vocabulary before adding
  its reserved ID and asserts that every encoded split stays within vocabulary
  bounds. The exact downloaded data pass with vocabulary size 33,278 and
  maximum token ID 33,277. This repair does not alter the frozen run grid,
  targets, or metric definitions.
- Version 3 submitted: 2026-07-17 (Asia/Calcutta)
- Version 3 status after startup: `RUNNING`
- Version 3 submitted script SHA256:
  `42b274585d1d08182a4a487edb8ca53b749e346e67ee9ee85e86b71778d29d2f`
- GPU slots used: 1
- Wall-clock limit: 7.5 hours with a 20-minute launch reserve and 15-minute in-run reserve
- Kernel: <https://www.kaggle.com/code/aparajeetshadangi/mbe-2-causal-text-pipeline-pilot>

## Frozen Scope

The run performs two essential pipeline tests:

1. a causal-mask future-token perturbation test with an unmasked negative
   control;
2. a restartable WikiText-2 pilot over small and medium causal Transformers,
   four frozen optimizer/regularization configurations, and three seeds.

There are 24 planned cells. Each completed row is flushed immediately. The job
is an implementation and runtime pilot, not inferential or confirmatory metric
evidence.

## Expected Outputs

- `causal_mask_leakage_test.json`
- `mbe2_causal_text_pilot_manifest.json`
- `mbe2_causal_text_pilot.csv`
