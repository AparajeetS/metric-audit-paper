# Prospective Protocol: TruthfulQA Reference-Overlap Pilot

**Protocol status:** frozen before computing the candidate audit results  
**Freeze date:** 2026-07-16  
**Registration boundary:** this Git commit is a time-ordered, public protocol freeze. It is not a third-party preregistration.

## Purpose and Scoped Claim

This pilot is a real-data test of selected E0-E2 checks in the experimental Benchmark Audit Toolkit. It does not validate MBE, certify TruthfulQA, establish construct validity, or evaluate any model as truthful.

The candidate claim is:

> On TruthfulQA's released human-labelled generation examples, a transparent reference-overlap score adds held-out information about the released human truth labels beyond declared length and reference-set proxies, and that increment transports in aggregate across TruthfulQA question categories.

The audit may support, fail to support, or leave this claim unresolved under the declared tests. The result will be reported regardless of direction.

## Frozen Data Contract

The only source is the official `sylinrl/TruthfulQA` repository at commit `d71c110897f5d31c5d7f309e7bc316c152f6f031`, licensed Apache-2.0.

- Question metadata: `data/v1/TruthfulQA.csv`
  - expected rows: 817
  - SHA-256: `967b82fb1fb6274e4971c6c80caa9d04f844c512b1033c146f26c78270cd384b`
- Human-labelled answer examples: `data/finetune_truth.jsonl`
  - expected rows: 22,434
  - expected distinct questions: 817
  - SHA-256: `9fd94fc943a2dc08f1dc028d2b6f353ae85fae5169a536ae6489236db2f30b64`

Each JSONL prompt will be parsed into its question and answer. Its `yes` or `no` completion is the binary target. Questions will be joined exactly to the v1 metadata to obtain category and reference answers. A failed hash, unexpected row count, unparseable record, label outside `{yes, no}`, or unmatched question stops the analysis rather than silently changing the cohort.

## Frozen Variables

- Candidate score, `reference_overlap_diff`: maximum unigram-token F1 between the labelled answer and any correct reference, minus maximum unigram-token F1 with any incorrect reference.
- Target, `human_truth_label`: 1 for a released `yes` label and 0 for `no`.
- Declared baseline proxies:
  - `answer_length_tokens`
  - `question_length_tokens`
  - `correct_reference_count`
  - `incorrect_reference_count`
- Environment: TruthfulQA `Category`.
- Independence unit: exact question ID. All answer examples for the same question remain in one cross-fitting fold.
- Deceptive control: `length_proxy_control`, answer length plus deterministic sub-token jitter. It is intentionally associated with a declared baseline but contains no answer semantics.
- Negative control: `hash_noise_control`, deterministic pseudo-random noise derived only from the question-answer text hash.

Tokenization lowercases and extracts Unicode word tokens. Unigram F1 is the multiset-token harmonic mean of precision and recall. Empty-versus-empty receives 1; one empty input receives 0. Semicolon-delimited reference lists are parsed as supplied in the CSV. This transparent score is created for the pilot. It is not represented as an official TruthfulQA BLEU, ROUGE, BLEURT, or GPT-judge score.

## Frozen Estimation and Decision Rules

- Five-fold grouped cross-fitting for E1.
- Second-degree numeric baseline terms, training-fold-only scaling, ridge penalty `0.001`.
- Aggregate leave-one-category-out transport for E2.
- Seed `20260716`.
- 199 permutations and 499 bootstrap resamples.
- A positive practical threshold of 1% relative out-of-fold MSE improvement is required separately for E1 and E2.
- An estimand meets its threshold only if its point estimate is at least 1% and the 95% bootstrap interval for absolute MSE improvement is entirely above the corresponding 1% baseline-MSE threshold.
- It falls below the threshold only if the interval is entirely below that threshold; otherwise it is unresolved.
- The overall predeclared-test outcome supports the scoped claim only if both E1 and E2 meet their thresholds and neither supplied control meets either threshold. Any control crossing a threshold makes the outcome unresolved.

E0 is descriptive only. E3 interventions and E4 reliability/cost are outside this pilot and will remain explicitly unimplemented.

## Permitted Interpretation

The strongest permitted conclusion concerns incremental prediction of these released labels by this score under these baselines, grouping rules, categories, and estimators. This pilot cannot show that the labels are error-free, that the score measures truthfulness generally, that performance transfers across model families or new prompts, or that a causal relationship exists. The answer pool was released for fine-tuning/evaluation rather than collected as a fresh confirmatory holdout; categories are broad and uneven; model identities are not available for a model-family audit; and reference overlap can reward surface similarity. These limitations will accompany the result, including if the declared thresholds are met.
