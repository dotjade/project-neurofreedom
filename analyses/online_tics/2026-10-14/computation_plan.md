# Deterministic aggregate audit, chosen after source extraction

14 October 2026, 02:47 UTC. This is an explicitly post hoc sensitivity analysis, not a trial analysis plan.

The nine focal contrasts match the question assigned before extraction: iCBIT versus online psychoeducation, across TTS, impairment and GTS-QOL, at V3, V4 and V5. Compute (1) the trial's actual primary/secondary hierarchical gate, (2) nominal interval signs, (3) Bonferroni and Holm adjustments over these nine contrasts only, and (4) sensitivity to reported three-decimal rounding and the censored p < 0.001. These procedures do not require covariance. No new confidence intervals, effect estimates or clinical-response thresholds will be calculated.

The nine-contrast family omits numerous reported tests. It is chosen for the bounded scientific question, not as a replacement for the study-wide multiplicity strategy. Retained contrasts remain exploratory. The primary endpoint retains its original standalone test; including it in the hypothetical nine-contrast calculation does not retrospectively change that test.

For each p printed to three decimals, examine the closed envelope [max(0,p−0.0005), min(1,p+0.0005)] as a conservative representation of ordinary nearest-three-decimal rounding. For p < 0.001 use the envelope [0,0.001], without treating the upper bound as the exact p. Bonferroni and Holm adjusted p-values are monotone in the component p-values, so evaluating the all-lower and all-upper vectors brackets all possible results in those envelopes. This is a reporting-precision sensitivity, not a model-uncertainty analysis.

Reconstruct noncompliant arm counts only when the randomized denominator and rounded percentage imply one integer. Check that their sum matches reported overall noncompliance. Label these as compliance classifications, never endpoint-specific loss to follow-up. Do not calculate attrition-adjusted efficacy: actual arm-by-visit outcome counts and missingness-specific outcome summaries are not supplied in the inspected main paper/registry.

Tests will cover monotonicity, independent Holm rejection thresholds, rounding envelopes, primary-gate logic, count reconstruction, CI direction and reproducible outputs. No random seed is needed for this deterministic audit.
