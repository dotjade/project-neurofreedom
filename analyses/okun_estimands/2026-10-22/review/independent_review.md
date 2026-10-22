# Independent clinical/function estimand review

Checked 22 October 2026. Repository basis: c9314ae695c3b5624f5049a3d819fef922ebe14b. This is an AI-assisted source and inference review, not independent clinical peer review. No participant rows were saved, reconstructed, counted or analyzed.

## Independently verified source facts

[Okun 2024](https://www.nature.com/articles/s41598-024-57071-5), DOI 10.1038/s41598-024-57071-5, appeared on 18 March 2024. Relevant locations: Clinical programming; Results of chronic responsive DBS; Secondary behavioral and mood outcomes; Quality of life outcomes; Safety; Tables 3 and 6.

- Primary-outcome-period MRVRST stimulation-mode order was randomized; psychiatrist and participant were masked. The paper explicitly distinguishes prior-weeks YGTSS from this immediate comparison.
- Table 3 labels its percentage summaries as responder outcomes. Those percentages are not an all-enrolled effect estimate.
- MOS-36 compares baseline with six months. Several domains have reported improvements above ten points, but multiplicity-adjusted tests are nonsignificant. Table 6 displays individual rows, not an aggregate mean/SD/CI summary. The caption does not specify the correction procedure.
- Main-text behavioral/mood comparisons are nonsignificant. Safety includes infection-related explant/reimplant and separate lead repositioning.
- Response wording alternates between points and percent; device capability does not imply sustained responsive exposure. The exact MOS version and item recall window are not documented in the inspected methods.

[Earlier Cagle 2022](https://jamanetwork.com/journals/jamaneurology/articlepdf/2795845/jamaneurology_cagle_2022_br_220005_1664471661.47084.pdf), DOI 10.1001/jamaneurol.2022.2741, describes four analyzed participants from six recruited, excluding the first two for unavailable embedded technology. It identifies NCT02056873, matching Okun's program, and uses a 40% YGTSS primary response threshold. Its closed-versus-open comparison is nonsignificant; the abstract does not establish equivalence. This is linked-cohort evidence, not an independent replication.

The [2019-09-23 protocol/SAP](https://cdn.clinicaltrials.gov/large-docs/73/NCT02056873/Prot_SAP_000.pdf), printed pages 32, 35 and 38, plans three separate mode-testing days, mode setting one hour before recording, and 30-day stability of final parameters. These are planned methods; the article's shorter account does not prove identical implementation for every participant. Avoid describing this as a verified same-day crossover.

A fresh [projected registry retrieval](https://clinicaltrials.gov/study/NCT02056873?tab=results) at 03:01:00 UTC independently confirmed eight responsive-period starters, five completers and three noncompleters. The systematically assessed safety window is three years. Serious events affected 4/10 in the continuous-labelled group and 0/5 in the responsive-labelled group; other events affected 10/10 and 0/5 respectively. These are selected sequential exposure groups, not independent randomized arms. The [saved narrow check](registry-independent-check.json) contains only public group-level metadata.

## Reviewer's inference and required guardrails

1. Randomized ordering of immediate stimulation states is not randomization to six months of treatment. A longitudinal preoperative contrast includes time, surgery, programming, treatment history and selection. Do not combine the estimands or use the immediate contrast as a functional-outcome control.
2. Nonsignificance does not prove no functional benefit, clinical equivalence or absence of harm. Preserve the direction reported by authors without converting it into a demonstrated functional effect.
3. Do not infer a common functional denominator from ten enrolled, eight chronic-capable devices, four selected responders, or visible individual rows. An aggregate denominator and paired estimator must be supplied by a lawful group-level source, not reconstructed here.
4. Do not calculate a change-score interval from marginal summaries without the necessary paired covariance or an explicitly justified alternative. Do not equate a ten-point descriptive change with an established clinically important threshold for this cohort.
5. Do not infer an instrument's exact version/recall window from its short name. Likewise do not carry washout or assessment timings from the earlier cohort into later participants without documentation.
6. Reoperations defeat an unqualified 'no safety issues' summary. An adverse-event count, affected-person count and exposure-adjusted risk are different quantities. Preserve the report's timing limits.

## Access and boundary notes

Okun publisher HTML and PDF were retrievable. Cagle overlap/methods were verified from indexed primary-text excerpts; complete direct Cagle publisher-PDF retrieval is not claimed. A final direct JAMA PDF web-reader open at 03:07 UTC returned a cache miss. PMC direct opens showed a browser-check page; these are access limitations, not evidence the papers are absent. Table-format inspection exposed individual rows in the tool display; those rows were not retained in files or used to derive any result. Only source structure, aggregate statements and study-level methods inform this review.

## Decision

The three outcomes do not support one interchangeable treatment estimand. Stop a functional efficacy calculation unless a genuine compatible aggregate contrast, denominator, scoring/window definition and uncertainty become available. This is a documentation/estimand conclusion, not a finding that DBS cannot benefit anyone. Severe refractory adults remain the relevant sampled population; pediatric and broad-population extrapolation is unsupported.

## Draft review

The [audit report](../report.md) was read in full at 03:03 UTC and the final source-access/instrument wording was checked at 03:08 UTC. No substantive inference error was identified. The protocol p18 independently supports the Modified Rush five-category 0-20 total; exact YGTSS revision remains unverified. All 25 offline documentation/boundary checks passed in an independent rerun at 03:08:10 UTC. The [dated review record](draft-review.json) identifies its exact SHA-256 and the scope/limits of this check. Any later claim-changing edits require another check.
