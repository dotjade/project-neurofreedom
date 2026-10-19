# Independent arithmetic and identification review

Reviewed 2026-10-19. This is a computational and estimand review of a synthetic construction, not clinical validation, an empirical study, or external peer review.

## Verdict

**Pass for the frozen synthetic specification; no arithmetic or reproducibility defect found.** A separately written checker, without importing `run_analysis.py`, regenerated the population, visit-level observations and every one of the 2,400 replicate rows. All 84 summary entries and diagnostic flags were independently recomputed. Maximum numerical difference was 1.03e-15 against a 2e-12 tolerance. All 157,936 assertion checks passed; this count includes repeated per-record assertions, not 157,936 independent scientific tests. The 18 original unit tests passed in a fresh temporary directory. Fresh execution reproduced all three generated artifacts byte for byte, and repeating the independent checker reproduced its log byte for byte.

The frozen preregistration, configuration and source-provenance hashes match `preexecution.sha256`. The parent reports publication commit `0a4677711ad6da4f7122a194cefa49b5ede3f097`, confirmed at 03:09:20 UTC, and execution after 03:09:32 UTC. This review verifies the supplied file hashes but does not independently attest the remote commit timestamp or the complete pre-execution history. It made no changes to frozen or main artifacts and no GitHub writes.

## Confirmed results

- Population size 400, equal X strata, antithetic within-stratum U/V means zero, and fixed seeds match the plan.
- Tic records and observation indicators are matched across A/B/C. Complete population tic mean is 2 in every world. Pain means are 1, 0, and 0 (C's residual is floating-point roundoff).
- Population covariance is 0.159785055973 for A/B and -0.240214944027 for C. The exact stipulated C-minus-B difference is -0.4; A-minus-B is zero. The independent checker uses centered products for covariance, separately from the source's raw-moment identity.
- Baseline and follow-up scores, including every realized error, stay within [0,10]. Realized extrema are 2.15309939858 and 6.04678253077. No clipping was needed.
- Observed counts range 215–268 for MCAR and 197–244 for MAR; complete always has 400. Support loss always selects exactly the 200 X=-1 units.
- Support-loss A and C have identical full observed paired records, not merely equal summary statistics. Their full-population pain means still differ by 1. Unsupported full-population HT estimates are correctly unavailable. This is a valid negative control for identification from these observations without extra extrapolation restrictions.
- There are zero preregistered raw-moment diagnostic flags. This confirms the recorded run has no flagged departure; it does not establish unbiasedness empirically or validate the imposed measurement/missingness assumptions.

## Estimands and interpretation limits

Under positive known inclusion probabilities, independent zero-mean cross-domain errors give E[R*T/p]=T, E[R*P/p]=P and E[R*T*P/p]=T*P for each fixed unit. Dividing their sums by known N therefore targets full-population raw moments. Complete-case MAR summaries instead represent an X-selected mixture; their departures from full-population truth are expected. MCAR complete-case raw moments have the expected finite-population target conditional on a nonempty observed sample. The implementation is undefined for an empty selected sample, but none of the frozen runs is empty; the probability under p=0.6 is 0.4^400. This edge case does not invalidate this fixed run.

HT plug-in covariance is not unbiased merely because its three component raw moments are. Under this specific independent Bernoulli observation/error model its exact bias is

`-sum_i [(1-p_i)/p_i * T_i * P_i] / N^2`.

The theoretical biases for (A, B, C) are:

- Complete: (0, 0, 0)
- MCAR: (-0.003599642, -0.000266308, +0.000400358)
- MAR: (-0.010099048, -0.002599048, +0.003900952)

Reported Monte Carlo covariance errors should be interpreted against these targets, rather than called evidence of an invalid raw-moment estimator. No modification to the frozen estimator is warranted for this review.

For support loss, `bias` fields are calculated against the full-population truth even though complete-case estimates describe the observed X=-1 subpopulation. In prose, call these differences **selection/target gaps**, not errors for the selected-subpopulation mean or covariance. No full-population recovery is available without added information or structural assumptions about the unobserved stratum.

The run demonstrates algebraic discrimination of deliberately chosen worlds. B and C also differ in marginal pain variance; covariance is not the unique possible discriminator. With shared errors, A-minus-B pain change is exactly 1 for every observed pair, so the toy contrast is particularly favorable. It does not quantify power, diagnostic performance, causal treatment effects, clinical meaningfulness, patient prevalence, or durability. Independence, known propensities, complete-domain pairing, and zero-mean error are imposed conditions. Correlated errors, outcome-dependent nonresponse, unknown propensities, and unpaired visits are outside this run; no extra scenarios were added after seeing results.

## Reproduction

Run `python review/independent_checks.py` from any directory. See `independent_checks.log` for hashes and detailed numerical checks, `independent_checks_repeat.log` for the repeated log, and `reproducibility.log` for fresh-directory byte matching and the original test-suite result. The checker requires only Python's standard library.
