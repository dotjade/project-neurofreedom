# Independent design and inference review

Reviewed the local frozen plan/configuration and analysis/output structure on 2026-10-19. No plan, configuration, analysis source, or results were edited. This is an original methods audit, not a clinical validation. The separate numerical reviewer is responsible for full replicate-by-replicate regeneration.

## Verdict

The construction and the reported interpretation are coherent with the frozen plan. Independent centered-moment calculations verify the exact finite-population algebra to floating-point precision. The local preregistration SHA-256 matches the configuration: `80d1305ea39d32c8f8a5be7576f9a79b66cc4fdd87ebf06d8a9fda2997527c17`. This audit does not independently attest the public commit timestamp or the chronology of source execution.

## Algebra

Stratum antithetic pairing gives E[U]=E[V]=E[XU]=E[XV]=0 and E[X²]=1. Writing q=E[UV], A=B+1 and C=B−X. Therefore tic mean is 2; pain means are A=1 and B=C=0; covariances are A=B=0.16+0.04q and C=−0.24+0.04q. Cross-moments are A=2+cov(A), B=cov(B), C=cov(C). For this fixed population q=−0.005373600673953618, giving covariances 0.15978505597304182, 0.15978505597304182, and −0.24021494402695812. The C−B covariance/cross-moment difference is −0.4; A−B covariance is zero and pain-mean difference is 1. C's residual numerical mean near −5e−17 is floating-point zero.

## Observation claims and limitations

- These are descriptive changes in 400 artificial units, with no treatment assignment or causal identification. Prefer “constructed pain improvement” or “additive shift” to unqualified “benefit.” N=400 and 200 replicates are fixed demonstration settings, not clinical sample-size or power findings.
- All tic records are the same by construction. This demonstrates a stipulated ambiguity, not an empirical finding that tic improvement fails to predict pain outcomes in patients.
- B and C also have different marginal pain variances. Joint covariance is informative here, but this experiment does not establish that pairing is uniquely necessary to distinguish these particular worlds.
- Independent zero-mean cross-domain error preserves expected raw moments; correlated/domain-dependent errors, clipping, selective domain observation, estimated propensity errors, and MNAR missingness have not been tested. Both visits and both domains share one observation indicator in the specified design.
- Known-probability HT raw means and cross-moments are unbiased under independent Bernoulli selection and positivity. “No diagnostic flags” in 200 replicates is a limited implementation diagnostic, not proof of unbiasedness, identification, or model validity. MCSE concerns repeatability of this simulation, not patient uncertainty.
- HT plug-in covariance is not generally unbiased. Its exact expected bias here is −sum_i[((1−p_i)/p_i) T_i P_i]/N². Independent arithmetic gives MAR biases A=−0.010099048073397038, B=−0.0025990480733970394, C=+0.003900951926602961. These are supplementary analytic checks, not an added preregistered endpoint. They explain why covariance bias must remain separate from raw-moment diagnostics.
- Unweighted MAR summaries are distorted relative to full-population targets: the reported mean pain changes are A=0.8161780438242593, B=−0.1838219561757407, C=0.27266986248870234. Preserve this adverse selection finding rather than presenting only the weighted output.
- The strongest negative control must remain prominent: under support loss, the observed A and C records are exactly equal for every retained unit and every matched replicate, while their full-population mean pain changes differ by 1. Reported observed mean pain improvement is 0.5984956635129703 in both. Known X and N do not restore missing-stratum outcomes. HT recovery is unavailable; identifying full-population outcomes would require assumptions beyond the observed data. The simulator knows the truth, but an observer does not recover it from this design.
- The support-loss summaries' “bias” is their difference from full-population truth, not error around their selected-stratum descriptive estimand. The negative-control selected-stratum true pain mean is 0.6 for A and C, and −0.4 for B.

## Artifacts

`review_design.py` independently reads the input CSV and output JSON, verifies the plan hash and exact algebra, uses centered covariance rather than the analysis source's raw-moment subtraction, and computes the supplemental analytic covariance bias. It never imports or mutates analysis source. Numerical output is saved in `design_checks.json`.

## Portable layout and rerun

Publish these three review files under `analyses/paired_outcomes/2026-10-19/design_review/`. From that directory run `python review_design.py`; the default source is its parent analysis directory. For the original sibling workspace layout run `python day19_design_review/review_design.py --source day19_design` from the workspace root. Outputs are always written beside the checker.
