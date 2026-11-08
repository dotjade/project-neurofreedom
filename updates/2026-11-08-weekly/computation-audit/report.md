# Weekly verification of the completed H18 computation

8 November 2026. Independent implementation and interpretation audit of synthetic methods; not clinical evidence or scientific peer review.

## Decision

**The 8 November H18 package satisfies the weekly protocol requirement to complete or verify one feasible bounded analysis.** The weekly run verifies work already completed in the daily run. It must not present the same simulation as a second new research finding or initiate an expanded simulation simply to meet the cadence.

No numerical or code correction is required. H18 personalized component selection remains proposed. The analysis rejects a specific unanchored mechanism-assignment inference, not every possible personalization design and not established CBIT symptomatic benefit.

## Evidence inspected

The clean local repository was at `c9d1bae55750e460768236ced30f29f54721dbb1`. Read README, RESEARCH_PROTOCOL, current STATUS, H18 in hypotheses.md, the 7 November mechanism report, and the complete 8 November plan, provenance, simulator, results, second-calculation checks, independent review, report and reproduction receipt.

The current GitHub connector copy of `run_analysis.py` has blob `d7d5289a3ef36add0704e52c099a1d588fbf7e68`, matching the local file. All ten payload hashes in the original manifest match. All ten motivating-file SHA-256 hashes and Git blob identities were independently verified against the recorded base commit `c1faee636fe54569660c03f7bdcc977e41ce7555`. The saved plan, freeze record and result share one plan hash.

Source package: https://github.com/dotjade/project-neurofreedom/tree/c9d1bae55750e460768236ced30f29f54721dbb1/analyses/h18_identifiability/2026-11-08

Protocol: https://github.com/dotjade/project-neurofreedom/blob/c9d1bae55750e460768236ced30f29f54721dbb1/RESEARCH_PROTOCOL.md

H18 claim and falsification: https://github.com/dotjade/project-neurofreedom/blob/c9d1bae55750e460768236ced30f29f54721dbb1/hypotheses.md#h18-personalized-learning-models-improve-the-durability-and-reach-of-cbit

## Why this qualifies

- A bounded question follows the preceding source audit: can urge-generation and action-control contributions be distinguished under explicit measurement and transfer assumptions?
- The plan fixes the model, independent-unit count, repeated-observation structure, parameter grid, random seed, estimators, intervals, misspecification cases and transfer contrasts before the recorded run.
- The package preserves 14 measurement and six transfer scenarios, each with 4,000 Monte Carlo datasets. Negative, unresolved and confidently wrong results are retained.
- Code, arbitrary inputs, seed streams, dependencies, outputs and provenance are present. A documented full same-environment rerun already produced identical output bytes.
- Verification is substantive: structural equivalence, exact sampling expectations, clustering, parameter recovery, transfer and scenario accounting are tested. This weekly audit adds separate checks without expanding the experiment.
- The report ends with a stop decision and an informative next dependency: public aggregate measurement-anchor and invariance evidence. Clinical evaluation remains outside the current work.

The freeze timestamp is a local record, not an independently time-certified preregistration. Hash consistency and historical motivating-file identity are verified; this audit does not independently prove the order in which the original author wrote and ran every file.

## Independent checks performed this week

1. Re-executed the original second-calculation script in a separate scratch copy. **261/261 checks passed**, and its generated JSON was byte-identical to the archived check output. These remain the original author's checks, not 261 newly authored tests.
2. Executed the separately written `audit.py`. **352/352 audit assertions passed.** These cover payload and frozen-input provenance, exact-fraction equivalence and covariance, known-loading and transfer identification, accounting, Monte Carlo summaries, RMSE identities, interval widths, expected bias/coverage, and selected scenario reconstruction. The count is software-check accounting, not 352 independent scientific tests.
3. Reconstructed two existing scenarios using scalar Gaussian factorization without importing either original script. The same documented PRNG streams were used to verify implementation, not to claim independent random replication:
   - Weak loading 0.25, one repeat, pure generation: 302 generation labels, 28 control labels and 3,670 unresolved, exactly matching the saved 4,000 datasets.
   - Loading 1, eight repeats, hidden shift: zero generation labels, 3,783 control labels and 217 unresolved, exactly matching the saved 4,000 datasets. All selected parameter means, RMSEs and coverage counts also agree.
4. The new script compiled successfully. The inspected checkout remained clean. No repository edits, visibility changes, personal data, new model scenarios or full 20-scenario rerun were performed by this audit.

Original `results.json` SHA-256: `0bc22573642ab67d815e5e1f38ea5a59c6ef8bac33c2b1b4a4b4ae7217cf5fb8`.

Environment: Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0. Exact reproduction is environment-specific.

## Scientific interpretation and disconfirming criterion

The invented observation model is `z=g+c`, `u=lambda*g+b`. With known nonzero loading and known zero shift, the two population contributions are algebraically identifiable. Sparse measurements alone do not prove structural nonidentifiability. Repeated observations improve precision but leave the independent-unit component of variance intact.

With an unknown reporting shift, `(g,c,b)` and `(g+d,c-d,b-lambda*d)` have the same expected observations. In this model their noise distributions are also identical. Exact rational arithmetic confirms the counterexample. This is the decisive failure of the proposed two-observation mechanism assignment when no identifying anchor is available. More precise estimation of the same observations cannot resolve that ambiguity.

The prespecified hidden-shift case shows the consequence: the fitted population label is confidently wrong in 3,783/4,000 datasets (94.575%). This does not establish that any clinical instrument has that shift. The two hidden-shift cases both use eight repeats and proportional cancellation; they do not estimate a one-versus-eight-repeat effect under hidden bias or compare a fixed absolute shift across sensitivities.

The clinical H18 falsification rule requires either no clinically worthwhile out-of-sample incremental benefit over equally intensive care, or parameters that cannot distinguish competing mechanisms. This computation addresses only the parameter-distinguishability prerequisite under one toy model. It supplies no trial of allocation, no clinical benefit threshold and no patient-level mechanism. Reject that unanchored operationalization; do not call H18 clinically falsified or validated.

Transfer has a separate identifying condition. Two tic means identify the two contributions only when unequal mechanism-specific transfer coefficients are known. Unknown coefficients do not supply that information, but also do not undo identification already supplied by a valid urge measure. Independent held-out artificial units test a population transfer gap, not transfer within the same person. An interval containing zero is not equivalence or proof of complete transfer.

## Limits and next decision

All effects, loadings, correlations and variances are artificial. There is no clinically calibrated scale, missingness, bounded outcome, real temporal dynamics, causal mediation identification, treatment randomization, age/severity group, pain, effort, function or co-occurring-condition outcome. Persistent severe adult applicability is not established. No cure, treatment choice, instrument defect or individual latent state follows.

**Stop the fixed simulation.** Next inspect existing public aggregate evidence for independently anchored urge/observed-tic measurement, invariance across time/context, global versus tic-specific timing, and explicit transfer estimands. Reopen simulation only if a new defensible anchor or a materially different preregistered question justifies it. Without an anchor, retain the mechanism as unidentified. Prospective personalization still requires authorized clinical governance, external validation and an equally intensive randomized strategy comparison measuring durable function, pain, effort and harms. No owner action is needed for this verification.

## Reproduce this audit

From a clean repository checkout with the documented dependencies, invoke the audit script with the repository root and an output path outside the checkout:

```sh
python /path/to/audit.py /path/to/project-neurofreedom --output /tmp/h18-weekly-audit-results.json
python -m py_compile /path/to/audit.py
```

The supplied `audit-results.json` is the actual output on the inspected commit. On a later clean commit, the recorded execution commit will differ; the source hashes, algebra, selected counts and substantive checks should remain unchanged if the original package is unchanged. The script deliberately checks cleanliness and does not repair or modify source files.

To repeat the original second calculation without writing into the repository, copy `independent_checks.py`, `results.json`, `plan.md` and `plan-freeze.json` from the original package to a temporary directory, run the copied script there, and compare its `independent-check-results.json` with the original. A full simulator rerun is already documented in the original package and is not necessary to repeat this bounded weekly verification.
