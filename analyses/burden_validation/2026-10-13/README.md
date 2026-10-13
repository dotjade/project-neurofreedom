# Adult burden validation and response-label concordance

13 October 2026. Read [report.md](report.md), the [question specified before extraction](prespecified_question.md) and [source extraction](extraction.json).

## Reproduce the aggregate calculation

From this directory, run `python aggregate_checks.py` using Python 3 and its standard library. No network, paid compute, participant records or random seed is required. The calculation is deterministic and uses [aggregate_inputs.json](aggregate_inputs.json), whose source locations identify published counts. The command overwrites `aggregate_checks.json`; preserve the dated output before changing inputs or code. The archived run passed 26 checks and its output reproduced byte-for-byte.

The calculation reconstructs agreement of two response classifications in a pooled mixed-age trial sample. It does not estimate adult quality-of-life surrogacy, a severe-state cutoff or a causal treatment contrast. Pointwise Wilson intervals omit threshold-selection optimism and trial/site clustering. See the report for all restrictions.

`build_extraction.py` regenerates the original structured literature extraction using its encoded source facts and `benchmarks_review.json`; it is an authoring aid, not automated scientific validation. `provenance.json` records searches and access limits. `manifest.json` records artifact SHA-256 hashes, excluding itself.
