# MNS follow-up: what attrition permits and prevents us from concluding

Project NeuroFreedom | Executed aggregate sensitivity analysis | 11 October 2026

## Finding

**The sign of the three-month full-cohort mean change is not identified under unrestricted scale-bounded missing outcomes.** Conditional on the printed baseline mean of 18.62, the possible change spans approximately **−13.01 to +2.84 motor-score points**. This establishes sensitivity to unobserved outcomes; it does not show that those outcomes actually deteriorated, or that the intervention had no benefit.

An average worsening of approximately **1.96 points among the 26 missing participants**, relative to their own baseline average, would offset the 15 returnees' reported average improvement of 3.40 points. This change-based threshold depends on the printed paired-returnee means and counts, not on the disputed full-cohort baseline. The threshold is hypothetical, not a clinical cutoff or a responder proportion.

**Source inconsistency matters:** the full-cohort baseline cannot be reconciled with the printed baseline subgroup means by ordinary displayed-value rounding. All baseline-dependent results therefore remain explicitly conditional, and an alternate branch is a sensitivity scenario rather than a correction.

## Question and disconfirming result

Before calculation, the analysis specification asked whether the direction of full-41 motor-score improvement remained identified if every missing follow-up outcome could lie anywhere on the valid scale. An admissible scenario producing zero or positive change would disconfirm robustness to unrestricted attrition. The source aggregates were already known when this computational specification was written; this was not a blinded hypothesis prediction or a registered trial analysis.

The disconfirming criterion was met at three months, but not at four weeks. The scope of this conclusion is mean-change identification, not efficacy, disease modification, cure, or the project's severe-adult antecedent question.

## Verified inputs and source location

[Jackson et al., published 7 September 2026](https://bpspsychub.onlinelibrary.wiley.com/doi/10.1111/jnp.70080), DOI 10.1111/jnp.70080; [PMID 42704310](https://pubmed.ncbi.nlm.nih.gov/42704310/).

The outcome is the YGTSS-R **motor** score, 0–25; total tic severity is 0–50. The indexed primary-publisher full text supplied the following aggregates:

| Assessment | Observed n | Follow-up mean | Baseline mean for those same returnees |
|---|---:|---:|---:|
| Four weeks | 36 | 16.25 | 18.83 |
| Three months | 15 | 15.33 | 18.73 |

The baseline analysis cohort is 41, with printed mean 18.62. Five early dropouts have a separately printed baseline mean of 19.0. Exact locators: **Methods → Outcome measures** for scale bounds; **Results → Analyses: Motor tic severity (YGTSS-R), first paragraph** for the full cohort/four-week/subgroup means and **second paragraph** for the three-month count and paired means. Figure 1a was not digitized.

These are the 2026 extension's denominators. The [2023 trial](https://pmc.ncbi.nlm.nih.gov/articles/PMC10947020/) initially allocated 45 per arm, 135 overall, and admitted ages 12 upward. Its counts are not substituted here. The extension analyzes the same trial and provides no contemporaneous sham comparison for this follow-up analysis.

Direct DOI/publisher opens failed; substantive indexed primary-source methods/results were retrievable, with the motor paragraph obtained again through a targeted query. The month-three aggregate identity, 15.33 − 18.73 = −3.40, agrees with the reported paired change. Original text was not copied into the deliverable. No relevant correction or retraction notice emerged from the bounded exact-DOI searches; this is not comprehensive clearance.

## Estimands and assumptions

Let N=41, n denote observed follow-up count, m=N−n, Y_R the observed follow-up mean, B_R those returnees' own baseline mean, B the original cohort baseline mean, and Y_M a hypothetical missing follow-up mean. Lower scores indicate less motor severity.

- Returnee paired mean change: Y_R − B_R.
- Hypothetical full-cohort follow-up mean: (n × Y_R + m × Y_M) / N.
- Hypothetical full-cohort change: that mean minus B.
- Scale bounds: evaluate Y_M=0 and Y_M=25.
- Null tipping outcome: Y_M* = (N × B − n × Y_R) / m.
- Implied missing-group baseline, conditional on consistent partitions: B_M = (N × B − n × B_R) / m.
- Null tipping missing-group change: Y_M*−B_M = −n × (Y_R−B_R) / m.

These are deterministic aggregate identities; no missing-at-random assumption is needed for the scale bounds. They assume the printed counts refer to nested subsets of the same baseline cohort, as the motor-results narrative states. The source means are rounded and internally inconsistent, so the calculations do not reconstruct exact empirical data. Fraction arithmetic prevents avoidable computational rounding; it cannot repair source uncertainty.

The unpaired comparison 15.33 − 18.62 = −3.29 is not the returnees' −3.40 paired change. A mean reduction cannot be turned into a number of responders. Neither marginal standard deviations nor an assumed covariance are used to construct confidence intervals or significance tests.

## Actual outputs

### Main branch: conditional on printed full-41 baseline 18.62

| Timepoint | Retention | Returnee paired change | Full-cohort change bounds | Missing follow-up mean needed for zero change |
|---|---:|---:|---:|---:|
| Four weeks | 36/41 (87.8%) | −2.58 | [−4.3517, −1.3029] | 35.6840, outside 0–25 |
| Three months | 15/41 (36.6%) | −3.40 | [−13.0115, +2.8422] | 20.5181, within 0–25 |

There are 26/41 missing outcomes at three months (63.4%). The full-cohort three-month follow-up mean itself ranges from 5.6085 to 21.4622 under these scale-only scenarios. The large interval reflects missing outcomes, not a sampling confidence interval. Extremes illustrate identification limits; they are not forecasts of what happened.

At four weeks, even placing all five missing outcomes at the maximum score does not erase the direction of the full-cohort pre/post change under the chosen aggregates. This is neither a treatment-control contrast nor proof that the four-week effect is causal.

### Three-month scenarios relative to the missing group's own baseline

The baseline printed for all 41 and the month-three returnee baseline imply a missing-group baseline mean of 18.5565. This is an algebraic implication, not an observed or independently verified statistic.

| Hypothetical mean change among the 26 missing | Full-41 mean change |
|---|---:|
| Same −3.40 change as returnees | −3.4000 |
| No average change | −1.2439 |
| +1 point worsening | −0.6098 |
| +1.9615 points worsening | 0 |
| +2 points worsening | +0.0244 |
| +3 points worsening | +0.6585 |

Each listed scenario is scale-admissible at the mean level in both baseline branches. None is claimed to describe actual missing participants. A mean-level deterioration does not imply that every missing person worsened, nor that anyone met a clinical response threshold. No individual trajectories were fabricated.

The transparent aggregate calculation is 15 × 3.40 = 51 score-points of observed improvement; 51/26 = 1.9615 points of missing-group mean worsening balances it. Assuming no average change in missing participants leaves 51/41 = 1.2439 points of full-cohort improvement. Assuming +2 points yields (26 × 2 − 51)/41 = +1/41 = +0.0244. The same identities apply under either full-baseline branch because the full baseline cancels.

### Inconsistent baseline and alternate sensitivity branch

The printed subgroup means imply (36 × 18.83 + 5 × 19.0)/41 = **18.8507**, differing from 18.62 by 0.2307. Conversely, using 18.62 and the 36-returnee baseline implies an early-dropout baseline mean of 17.108, not the printed 19.0. This cannot identify which value or denominator is wrong.

Treating each two-decimal mean as lying within ±0.005 and the one-decimal dropout mean within ±0.05 gives a printed full-baseline rounding interval [18.615, 18.625] and a subgroup-derived interval [18.8402, 18.8612]. They do not overlap. This demonstrates that ordinary rounding alone cannot explain the inconsistency under the stated partition.

**If**, as a separate hypothetical branch, the full baseline were the pooled 18.8507, four-week bounds would be [−4.5824, −1.5337] and three-month bounds [−13.2422, +2.6115]. The missing follow-up mean needed for zero three-month change would be 20.8819. Both qualitative conclusions persist. This branch is not asserted to be the correct empirical baseline.

Conservative rounding envelopes also preserve both conclusions. In the printed-baseline branch, the three-month change envelope becomes [−13.0183, +2.8490] and the null missing-outcome threshold lies between 20.5073 and 20.5288. The missing-group mean-change threshold lies between 1.9558 and 1.9673 in both branches. The envelopes use interval extremes and do not claim joint attainability of every combination, particularly where pooled baseline shares a component. They are not confidence intervals.

## Interpretation, missing prerequisites and next decision

The analysis rejects only the stronger claim that the direction of three-month full-cohort improvement follows from these observed aggregates regardless of missing outcomes. It preserves the narrower reported finding among assessed returnees. It does not establish that attrition caused the observed improvement, that missing people actually worsened, or that treatment had no lasting effect.

Completer significance cannot resolve the unobserved outcomes. Similar observed baseline averages cannot establish that dropout was unrelated to unobserved follow-up severity. A selected-returnee comparison and a single-arm mixed model also cannot supply the missing contemporaneous control contrast. Natural fluctuation, expectancy, regression to the mean, treatment changes and selection remain alternative explanations that this aggregate computation cannot separate.

Further empirical precision requires a verified, internally consistent baseline partition and follow-up sums, exact analysis populations, and missingness reasons. Responder inference requires a prespecified threshold and actual paired response information. Causal durability requires an appropriately controlled follow-up design with retention and treatment histories addressed. Any participant-level access or clarification outreach has a separate authorization and governance gate; none occurred here.

**Next informative research decision:** retain MNS as a symptom/durability research lead while requiring controlled, retention-aware follow-up before promoting disease-course claims. Prioritize published correction/clarification or new aggregate follow-up when available. Do not keep recomputing these unchanged inputs. This task does not justify substituting this mixed-age treatment sample for a severe-persistent-adult cohort or inferring an individual's biology. Pain, participation, function and sustained adult burden remain distinct priorities.

## Reproducibility and checks

- `ANALYSIS_SPEC.md`: pre-execution question, disconfirming result and bounded plan.
- `inputs.json`: source locators, exact printed inputs, access limits, search strings and repository blob SHAs.
- `analyze.py`: deterministic Python 3 standard-library computation with exact fractions.
- `results.json`: actual computed outputs, including exact fractions and decimal renderings.
- `scenarios.csv`: flat scenario outputs; infeasible tipping scenarios are explicitly flagged.
- `execution.log` and `run_metadata.json`: actual run output, UTC execution time and SHA-256 provenance.
- `test_analysis.py` / `tests.log`: 19 passing tests covering edge cases, identities, rounding, feasibility and output reproducibility.
- `check_arithmetic.py` / `arithmetic_check.log`: 56 passing checks using a separate Decimal implementation that does not import the main analysis. This second implementation is an arithmetic check by the same analyst, not independent scientific peer review.

No randomness, paid compute, personal medical data, participant-level files, GitHub mutation, clinical recommendation or external contact was used. Numeric display precision exceeds the scientific precision of the source and is shown only for reproducibility.
