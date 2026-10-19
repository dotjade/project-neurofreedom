# Paired outcomes: what direct pain measurement can and cannot identify

19 October 2026 | Executed synthetic methods test | Arbitrary units, no participant data

## Decision

Direct paired pain measurement distinguishes some stipulated worlds that tic-only records cannot distinguish. It does not overcome lack of observations in an entire subgroup. This is a mathematical counterexample and a reproducible observation-model check, not evidence of a treatment benefit, patient-level decision accuracy or biological mechanism.

The frozen [plan](preregistration.md) and [configuration](config.json) were committed and read back before execution at [0a46777](https://github.com/dotjade/project-neurofreedom/commit/0a4677711ad6da4f7122a194cefa49b5ede3f097), confirmed at 03:09:20 UTC. Execution began after 03:09:32 UTC. The plan was drafted locally at 03:07:06 UTC, then clarified before publication to acknowledge marginal variance as another discriminator and distinguish worker publication scope. Published plan/configuration bytes were not changed afterward. This is public pre-analysis specification for a synthetic exercise, not registration of a clinical study.

## Fixed construction and estimands

Four hundred artificial units have balanced X=-1 and X=+1 strata. All three worlds share identical tic improvements and baseline scores. Pain improvement is additive in A, zero on average in B, and cancels across strata in C. The complete noiseless means are tic=2 in every world and pain A=1, B=0, C=0. Positive change means baseline minus follow-up. These are finite-population descriptive changes without treatment assignment or a causal contrast.

Because tic observations are literally identical across worlds, tic-only nonidentifiability is exact by construction, not something established by simulation accuracy. Paired pain measurements add separately observed information. B and C share a mean but differ in covariance with tic change; they also differ in marginal pain variance, so covariance is not the only possible discriminator.

The joint covariance targets, computed with population divisor N, are A=B=0.15978506 and C=-0.24021494. Their raw cross-moments are A=2.15978506, B=0.15978506 and C=-0.24021494. The finite-population U/V cross-product is retained rather than silently replaced by its expectation.

N=400 and 200 observation replicates are arbitrary computational settings for a small fixed test. They are not a clinical sample-size recommendation, adequate-power claim or calibrated measurement design. All effect magnitudes, scales, probability settings and noise amplitudes are analyst-chosen, not fitted clinical quantities.

## Actual output

Independent zero-mean errors, uniform between -0.25 and +0.25 per visit and domain, were added before computing observed changes. Complete-observation design results averaged over the 200 replicates were:

| World | Pain mean | Monte Carlo SE | Tic–pain covariance | Monte Carlo SE |
|---|---:|---:|---:|---:|
| A | 0.999361 | 0.000672 | 0.160343 | 0.000469 |
| B | -0.000639 | 0.000672 | 0.160343 | 0.000469 |
| C | -0.000639 | 0.000672 | -0.240511 | 0.000596 |

These Monte Carlo SEs describe uncertainty in simulation averages over repeated observation noise/masks for one fixed artificial population. They are not patient confidence intervals, standard errors of clinical effects or probabilities of correct decisions. Matched random numbers across worlds deliberately reduce variability in scenario contrasts; they do not reproduce separate real trials.

Under observed-X missingness, observation probability is 0.8 in X=-1 and 0.3 in X=+1. Naive complete-case pain means become 0.816178, -0.183822 and 0.272670 for A, B and C. This selection can create apparent positive average change in C despite zero full-population mean. Horvitz–Thompson estimates using the exact known simulation probabilities average 0.996565 (MCSE 0.005833), -0.001133 (0.002072) and -0.000019 (0.002795). Such recovery depends on correct probabilities, positivity and the stated error model. Neither knowing these probabilities nor the error assumptions is guaranteed in a future study.

Complete, MCAR and MAR raw-moment diagnostics produced zero flags under the prespecified |mean error|>4 MCSE criterion. This is a programming/observation-model diagnostic, not an inferential clinical threshold or proof of unbiasedness. Unbiased raw moment targets follow from the specified probability model. The covariance formed by subtracting the product of two estimated weighted means is not promised unbiased. Its MAR estimation errors were -0.006805, -0.002950 and +0.005490 for A, B and C; these are retained rather than hidden behind raw-moment recovery. Independent post-run arithmetic gives expected finite-sample covariance biases of approximately -0.01010, -0.00260 and +0.00390 under MAR; differences between realized and expected biases also contain Monte Carlo variation. Full results include all MCAR and weighted covariance results.

## Preserved failure: measurement cannot repair unsupported strata

In the support-loss design only X=-1 is observed, so A and C produce exactly identical observed tic and pain data, including identical errors, in every replicate. Their selected-subpopulation mean pain improvement averages 0.598496 in both, although full-population means differ by 1. No full-population weighted estimate is calculated because the other stratum has zero observation probability. The selected covariance is approximately zero in both worlds and does not reveal their different full-population covariances. Output fields labelled bias compare against the full-population target throughout: under support loss this is a selection/target gap, not bias relative to the selected-subpopulation estimand.

This is an exact observational-equivalence negative control, not merely a wide attrition interval or agreement between response labels. It shows why direct pain measurement is informative but insufficient without an observation design that covers the target population or additional justified assumptions.

## Verification, reproducibility and limits

[Source](run_analysis.py), [synthetic inputs](synthetic_inputs.csv), [replicate output](artifact_parts/manifest.json), [summary results](results.json), [tests](test_analysis.py), [execution log](execution.log) and [test log](tests.log) are preserved. Python standard library only. Run from this directory:

    python run_analysis.py
    python -m unittest test_analysis.py -v

Eighteen implementation tests passed, including exact tic identity, complete-data algebra, separate centered covariance arithmetic, full score/error envelopes, missingness support, complete-case versus weighted identity when fully observed, exact support-loss observational equivalence and deterministic reruns. The [independent numerical review](review/independent_review.md) separately regenerated all 2,400 rows and all 84 summary entries, with maximum numerical difference 1.03e-15; fresh-directory execution reproduced the three generated artifacts byte for byte and passed the 18 original tests. The separate [inference review](design_review/design_review.md) confirmed the estimand and analytic covariance-bias distinctions. Computational verification is not clinical peer review or validation of the chosen assumptions.

The code generates 400 artificial population rows and 2,400 observation-summary rows. Synthetic unit labels are simulation indices and are not people or participant identifiers. The joint observation mask requires both outcomes at both visits to be observed together. Separate item missingness, error correlations, nonlinear reporting bias, unmeasured selection, scale validation, recall mismatch, temporal generalization and treatment assignment are outside this model. Pairing alone does not remove those problems. The implementation does not define estimates for an empty observed set; no frozen replicate is empty, and general reuse would require explicit handling of that edge case. No clinical rates, meaningful-change cutoffs, persistent-severe-adult effects, durability, disease modification or cure conclusions follow.

## Next bounded decision

Close this fixed synthetic test. Before another simulation, specify a defensible paired measurement/observation model: exact pain-interference construct and recall window; compatibility with separately measured tic change; availability of joint outcomes and subgroup coverage; and what supports error/missingness assumptions. The lawful-primary-source gate for the Marras focal-tic pain endpoint remains separate and unresolved. Do not substitute a model assumption for missing primary methods or initiate participant collection. A human study would require appropriate investigator, validated measurements, governance and separate authorization.

## Public artifact packaging

Large generated or source-metadata artifacts are stored in lossless text parts because oversized connector writes stalled. Run `python restore_artifacts.py` in this directory before the original commands. The [manifest](artifact_parts/manifest.json) records original SHA-256 values, byte lengths and ordered parts. This is storage-only packaging after execution, not an analytical deviation; frozen plan/configuration and results are unchanged. Original files are reconstructed byte for byte.
