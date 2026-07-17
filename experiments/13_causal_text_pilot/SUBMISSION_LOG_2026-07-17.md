# Kaggle Submission Log: Corrected Causal Text Pilot

- Submitted: 2026-07-17 (Asia/Calcutta)
- Kaggle version 1: completed with zero valid training rows because Kaggle's
  preinstalled PyTorch wheel had no compatible CUDA kernel image for the P100.
  The failure artifacts are retained and are not evidence.
- Kaggle version 2: pins the previously validated PyTorch 2.4.1 CUDA 11.8 wheel
  and adds a fail-fast GPU matrix-multiplication preflight.
- Version 2 status after the dependency/preflight window: `RUNNING`
- Submitted script SHA256:
  `f2c08ff480b2ccc0a91c04b4375d07f9c6d35a07b8589b72cfacda15636c8313`
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
