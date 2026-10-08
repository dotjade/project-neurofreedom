# SYNTHETIC implementation validation

Executed 8 October 2026. This verifies this code and its generated outputs, not clinical validity.

- Eleven unit/validation tests passed; see `tests.log`.
- Full run: seven scenarios × 240 independent replicate seeds × three histories = 5,040 forecast evaluations.
- Future observations are supplied only to scoring; the prediction API accepts the training history alone.
- The known clean 48-step signal is recovered and its future forecast matches to numerical precision.
- The latent-periodic and reporting-periodic constructions produce exactly identical observations.
- Plot outputs were opened and visually inspected for labeling/layout.
- No patient inputs or private source files are read by the benchmark.
- No dependencies were installed, no external service was modified, and no GitHub operation was performed by this analysis.

Reproducibility checks and any additional validation are recorded below after execution.

- Exact byte-for-byte rerun match: `replicate_results.csv`.
- Exact byte-for-byte rerun match: `summary.csv`.
- Exact byte-for-byte rerun match: `summary.json`.
- Exact byte-for-byte rerun match: `metadata.json`.
- Confirmed 5,040 replicate-level evaluation rows.
- Source SHA-256 in metadata matches final `simulate.py`.
- All summary values, including bootstrap intervals, exactly match between the intentionally observation-equivalent latent-period and reporting-period scenarios.

## Edge-case correction after independent review

A near-zero denominator previously made the fit-gain diagnostic spuriously approach one for perfectly zero, constant or linear histories. The final code explicitly assigns zero incremental gain when linear residual SSE is within a scale-aware floating-point tolerance. Three new regression tests cover those histories. This corrects the diagnostic edge case, not the noisy synthetic benchmark results. Final rerun and hash checks are recorded below.

- Final 11-test run passed after the guard fix.
- Full 5,040-evaluation rerun completed; replicate CSV and both summary files are byte-identical to the previous independent rerun.
- Final metadata source SHA-256 verified against corrected code; metadata changes only reflect the new source hash and more explicit example-plot title does not change numerical data.
