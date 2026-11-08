# H18: what an urge measure must identify

Project NeuroFreedom | 8 November 2026 | Synthetic methods exercise, not clinical evidence

## Decision

Keep **H18 personalized component selection proposed**. This exercise identifies a measurement prerequisite, not a treatment mechanism: the two invented contributions can be separated only under explicit identifying assumptions about measurement or context transfer.

Repeated observations improve precision under a correctly specified measurement model. They do not resolve an unknown systematic reporting shift. In one prespecified sensitivity case, more precise measurements led the fitted model to choose the wrong population-level explanation confidently. A new context can test transfer, but it does not automatically identify why improvement occurred.

The next useful step is a bounded audit of measurement anchors and invariance, not a more elaborate predictor fitted to the same observations. No patient's mechanism, treatment choice, effort, function or prognosis is inferred here.

## Why this question, and what is new

The [7 November H18 audit](../../h18_mechanism/2026-11-07/report.md) separated whole-treatment benefit, global urge mediation, baseline moderation, reward manipulation and transfer. It left a specific question: could sparse global urge measurements distinguish reduced urge generation from improved action control? The current work answers that question for one deliberately simple artificial model. It does not repeat the clinical source audit, reanalyze the CBIT trials or add an empirical evidence record.

The preceding audit's Houghton and van de Griendt records motivate attention to global versus repeated urge measures. Their published effects, sample sizes and scales are **not** used to calibrate this simulation. Nothing here establishes that an actual urge measure has a particular loading or reporting bias.

The [plan](plan.md) was written and hashed before numerical execution. [Plan provenance](plan-freeze.json) records the unchanged plan and motivating repository files at commit `c1faee636fe54569660c03f7bdcc977e41ce7555`. This is a locally prespecified methods exercise, not a prospectively registered human study.

## The artificial model

Define two dimensionless population contributions:

- **g**: contribution assigned to lower urge generation.
- **c**: contribution assigned to greater action control.

Expected observed changes are:

`tic-expression reduction z = g + c`

`urge-score reduction u = lambda × g + b`

Here, lambda is how sensitively the hypothetical urge measure reflects g, and b is a systematic reporting/measurement shift. Positive values indicate reductions. These equations are assumptions, not an established account of Tourette biology. The labels do not imply that tics are voluntary, that persistence reflects insufficient effort, or that fewer observed tics means less burden.

Each simulated dataset contains **60 independent artificial units**, each with either one or eight paired-change observations. A unit-specific Gaussian deviation persists across that unit's rows; independent Gaussian measurement error is added at each repeat. The paired changes are simulated directly, not reconstructed from baseline/follow-up scores. The marginal SDs are 0.45 for unit effects and 0.80 for measurement error; their two-outcome correlations are 0.30 and 0.20 respectively. These numbers are arbitrary. There is no missingness, autocorrelation beyond the shared unit effect, ceiling/floor, treatment randomization or age/severity subgroup.

Four designs cross known loadings 0.25 and 1 with one and eight repeats. Each is tested at pure generation `(g,c)=(0.5,0)`, pure control `(0,0.5)` and equal contribution `(0.25,0.25)`. Two extra scenarios add a hidden b that cancels the true urge change. Six transfer scenarios use independent artificial units in the second context. Each scenario has **4,000 Monte Carlo datasets**, using PCG64 and master seed **20261108** with separate, recorded child streams. No personal data or observations from people enter this computation.

## 1. Structural identification comes before model fitting

Tic change alone gives one equation for two contributions. Every pair with the same sum predicts the same expected tic change. More repetitions of that equation cannot separate g and c.

If lambda is known and nonzero and b is known to be zero, the two-equation measurement matrix has rank two. Then `g=u/lambda` and `c=z-u/lambda`. Thus sparse global measurement is **not inherently structurally unidentified**: under strong measurement assumptions, even one paired contrast per independent unit supplies two distinct population means. Small sample size, error and weak sensitivity concern precision, not this algebraic rank.

If b is unknown, there are two measured means and three unknown parameters. The transformation `(g,c,b) -> (g+d,c-d,b-lambda*d)` leaves both measured means unchanged. For example, at lambda=0.25:

| Artificial world | g | c | b | Expected z | Expected u |
|---|---:|---:|---:|---:|---:|
| Lower generation with offsetting measurement shift | 0.5 | 0 | -0.125 | 0.5 | 0 |
| Higher action control without measurement shift | 0 | 0.5 | 0 | 0.5 | 0 |

The noise covariance is also identical by construction, so these worlds produce the **same full observed distribution**, not merely similar fits. No amount of sampling can distinguish them using these measurements under this model. This is an exact counterexample, not a claim that such a shift occurs in any real person or instrument.

An unknown loading also produces ambiguity. `(g,c,lambda)=(0.4,0.1,0.25)` and `(0.1,0.4,1)` both give `(z,u)=(0.5,0.1)` when b=0. A calibration or other identifying restriction is needed. The [structural outputs](results.json) preserve the matrices, ranks and null direction.

## 2. Repeated measurements improve precision only under the assumptions

The fitted model assumes known lambda and b=0. It uses independent-unit means, not repeated rows as separate participants. Parameter intervals use the empirical unit-mean variance and a Student t critical value with 59 degrees of freedom. Estimates are unconstrained; negative estimates are retained rather than clipped into the hypothesized positive quadrant.

For an illustrative population-level recovery diagnostic, the label is “generation-dominant” only if the 95% interval for g-c is entirely positive, “control-dominant” only if entirely negative, and otherwise unresolved. This is not a clinical classification rule or individual-level performance result.

| Known loading | Repeats per unit | Correct label under pure generation | Correct label under pure control | Unresolved under pure generation | g RMSE under pure generation |
|---:|---:|---:|---:|---:|---:|
| 0.25 | 1 | 7.55% | 7.90% | 91.75% | 0.485 |
| 0.25 | 8 | 15.78% | 15.25% | 84.08% | 0.271 |
| 1.00 | 1 | 54.15% | 53.50% | 45.85% | 0.120 |
| 1.00 | 8 | 95.08% | 95.48% | 4.93% | 0.070 |

These differences reflect the chosen sensitivity, noise and repeat structure, not actual instrument performance. Under pure generation, moving from one to eight repeats reduced g RMSE at both loadings, but repeating the weak measure often left the two contributions unresolved. Increasing loading while keeping noise fixed is a hypothetical improvement in signal sensitivity, not merely changing the units of the same measure.

The 95.08% generation-dominant rate is 3,803/4,000; its Monte Carlo Wilson 95% interval is approximately 94.36–95.70%. The 95.48% control-dominant rate is 3,819/4,000. These intervals describe finite-simulation uncertainty, not uncertainty about clinical applicability. All rates and Monte Carlo intervals are in [results.json](results.json).

Under equal contributions, a dominant label occurred in approximately 4.4–5.3% of datasets, consistent with the nominal two-sided test under the specified model. Across the correctly specified scenarios, empirical parameter-interval coverage was close to 95%, with the small fluctuations checked against exact t/noncentral-t sampling expectations. No selection of favorable scenarios was made.

### Repeated rows are not extra independent units

Eight repeats produce 480 rows, but still only 60 independent units. The intentionally wrong analysis that ignores this dependence gave only **75.88–78.03% coverage** for nominal 95% g intervals across the six correctly specified eight-repeat cases. The corresponding unit-mean analysis gave **94.83–95.35%** coverage.

Repeated observations reduce the observation-error term, while the unit-specific component remains. In this model the covariance of a unit mean is `Sigma_H + Sigma_E/R`, not `(Sigma_H + Sigma_E)/R`. This is an implementation lesson about clustering, not a recommendation to ask people to rate urges eight times.

## 3. Measurement misspecification can make the wrong answer more confident

In the prespecified sensitivity case, the true model has g=0.5 and c=0, but b=-lambda×0.5, so expected observed urge change is zero. The fitter still assumes b=0. Its expected estimate is then g=0 and c=0.5, despite the generation truth.

With lambda=1, b=-0.5 and eight repeats, it labelled the population **control-dominant in 3,783/4,000 datasets, or 94.58%**. The Monte Carlo Wilson 95% interval is approximately 93.83–95.24%. The g estimate had bias -0.499 and none of its 4,000 nominal 95% intervals covered the true g=0.5. Zero observed coverage is a finite-simulation result; the Wilson upper limit is approximately 0.096%, not proof that coverage probability is exactly zero.

The other hidden-shift case used lambda=0.25 and b=-0.125, again with eight repeats, and gave a wrong control-dominant label in 15.35% of datasets. Both shifts were deliberately scaled to cancel the urge signal completely. This compares sensitivity under proportionately scaled cancellation; it does **not** compare a fixed absolute bias across loadings or estimate the effect of increasing repeats in the hidden-shift setting. No one-repeat hidden-shift case was run. The weak-loading case was more often unresolved, but that uncertainty did not repair identification.

This does not demonstrate bias in PUTS, global urge reports or any actual treatment. It shows that, in an exact equivalent-world construction, apparently successful recovery under a correct model can fail under an unverified measurement-invariance assumption. Model precision is not evidence that the assumed causal interpretation is right.

## 4. Held-out context checks transfer, not automatically mechanism

The transfer exercise uses new independent artificial units in the second context, with eight repeats per unit in both contexts. The first-context tic mean alone predicts full transfer. The test context is not used to fit that prediction.

The second-context expected tic reduction is `z_B=t_g*g+t_c*c`. Both pure mechanisms give a first-context mean of 0.5. If both transfer coefficients equal one, they also give a second-context mean of 0.5 and remain indistinguishable. When the assumed coefficients are `(1,0.25)`, pure generation transfers at 0.5 and pure control at 0.125. Reversing the coefficients reverses that interpretation.

| Prespecified transfer coefficients (generation, control) | True contribution | Expected held-out mean | Mean held-out minus training estimate | Gap interval contains zero |
|---|---|---:|---:|---:|
| (1, 1) | Generation | 0.500 | 0.0012 | 94.73% |
| (1, 1) | Control | 0.500 | 0.0002 | 95.18% |
| (1, 0.25) | Generation | 0.500 | -0.0010 | 94.50% |
| (1, 0.25) | Control | 0.125 | -0.3745 | 3.18% |
| (0.25, 1) | Generation | 0.125 | -0.3790 | 2.50% |
| (0.25, 1) | Control | 0.500 | 0.0022 | 94.18% |

Intervals concern the difference between population means, not predictions for an individual. A gap interval containing zero does not establish equivalence or complete transfer. All six true-gap coverage rates were near 95%. The full-transfer assumption was usually contradicted when a 0.375 mean loss was built into the test context, as expected from the chosen noise level.

The known-coefficient matrix `[[1,1],[t_g,t_c]]` has rank two only if the coefficients differ. If the coefficients are unknown, two tic means generally cannot identify all four unknowns g, c, t_g and t_c. This statement is specifically about what the **two tic means** identify: equal or unknown transfer coefficients do not erase identification already supplied by a known, calibrated and invariant urge measure. A change across contexts could arise from several causes. This study does not learn biological transfer coefficients, prove which mechanism should transfer, test a treatment-allocation strategy, or establish that transfer is durable or functional benefit.

## What was verified

- Fourteen measurement and six transfer scenarios were completed, with 4,000 replications each. All scenarios are retained.
- A second calculation script, which does not import the simulator, passed **261/261** algebra, seed, accounting, bias, covariance and exact sampling-distribution checks. It compares observed rates with exact t/noncentral-t expectations where those apply. This is independent calculation, not independent authorship or scientific peer review.
- A full rerun with the same seed and environment produced byte-identical results. Both results files have SHA-256 `0bc22573642ab67d815e5e1f38ea5a59c6ef8bac33c2b1b4a4b4ae7217cf5fb8`.
- Both Python scripts compiled successfully. Python 3.12.14, NumPy 2.3.5 and SciPy 1.17.0 were used. Commands are in the [README](README.md), and all inputs are in the script and results file.

## Limits and next bounded decision

This is a linear Gaussian counterexample and a parameter-recovery check. It does not capture the biology, dynamics, bounded scales, tic-specific urges, feedback from tic suppression, changing observation behavior, correlated longitudinal errors, selection, attrition or heterogeneity of real clinical samples. It assumes a two-contribution model, fixed loadings and a known noise family; other mechanisms could explain the same observations. It estimates population means, not an individual's latent state. Even perfect parameter recovery under these equations would not establish causal mediation or a treatment benefit.

The artificial units have no age, severe-persistent-adult status, pain, effort, participation, co-occurring conditions or preferences. These omissions are applicability limits, not evidence that those outcomes are unimportant. No cure, treatment selection, sustained function or reduction in burden follows.

**Stop the fixed simulation here.** The next bounded task is to map what external anchors and invariance checks would be needed to connect global/tic-specific urge reports and independent observed-tic measures to these proposed constructs. Keep measurement sensitivity, report-shift assumptions, temporal ordering, participant clustering and context-transfer estimands explicit. Use existing public aggregate measurement evidence and distinguish feasibility from validation; do not collect videos or new symptom records. If no defensible anchor is available, retain the latent mechanism as unidentified rather than assigning a treatment component.

Clinical personalization would still require governed external validation and an equally intensive randomized strategy comparison with pain, effort, function, adverse effects and durable transfer. H18 remains proposed. No owner action, intervention, contact or paid resource is required for this synthetic result.
