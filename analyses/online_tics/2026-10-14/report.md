# ONLINE-TICS: later exploratory benefit does not rescue the failed primary endpoint

Project NeuroFreedom | 14 October 2026 | One adult randomized trial, protocol and registration

## Decision

Retain a **time-specific, exploratory adult benefit signal**, with tic severity, impairment and disease-specific quality of life separate. Do not promote this trial to confirmatory primary success, established non-inferiority to face-to-face CBIT, increasing efficacy over time, or benefit that persists after access/practice stops.

The primary contrast missed its prespecified criterion. Later estimates are encouraging but do not change that decision. Several clinically relevant contrasts are inconclusive, inconsistent, or point away from benefit. This is a research interpretation, not a treatment recommendation.

The [prediction and disconfirming conditions](prespecified_question.md) were recorded before retrieving new trial sources. The result supports the predicted need for time/outcome-specific interpretation; it does not establish individual tic–QoL concordance or discordance. This bounded analysis is closed at the published aggregates.

## Endpoint hierarchy and observed contrasts

The [2016 protocol](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2016.00119/full) and [official registration](https://clinicaltrials.gov/study/NCT02605902) identify YGTSS-TTS at one week after treatment as primary. The protocol permits confirmatory face-to-face non-inferiority only after primary superiority succeeds. The main paper explicitly acknowledges exploratory testing after that gate fails. Its three-point non-inferiority margin is a between-treatment design margin, not a QoL threshold or proof that the treatments are equivalent.

All numbers below are **published adjusted between-group change contrasts, iCBIT minus online psychoeducation**, with pointwise 95% intervals. Lower is favorable for these three measures. V3 is one week, V4 three months and V5 six months after the end of the regular treatment course. [Primary paper, Tables 3–4](https://publications.rwth-aachen.de/record/889351/files/889351.pdf).

| Outcome | V3: estimate [95% CI]; p | V4: estimate [95% CI]; p | V5: estimate [95% CI]; p |
|---|---|---|---|
| YGTSS-TTS | −1.28 [−2.58, 0.01]; .053 | −2.25 [−3.75, −0.75]; .003 | −2.71 [−4.27, −1.16]; <.001 |
| YGTSS impairment | −3.43 [−6.29, −0.56]; .019 | −2.80 [−6.10, 0.51]; .097 | −5.13 [−8.72, −1.54]; .005 |
| GTS-QOL | −1.67 [−4.67, 1.32]; .272 | −5.28 [−8.69, −1.88]; .002 | −4.60 [−8.21, −0.99]; .013 |

Only the V3 TTS cell is the primary endpoint. The other cells are secondary/exploratory, even when their visit coincides with the primary visit. An interval crossing zero does not prove no effect or equivalence. Conversely, an interval excluding zero does not establish a patient-important magnitude without a defensible anchor.

At V3, the iCBIT–face-to-face TTS estimate is +0.98 [−1.01, 2.96], just 0.04 below the three-point upper-limit margin. That arithmetic condition is met, but the confirmatory gate is closed. The displayed p=.333 tests an ordinary between-group contrast; it is not the non-inferiority p-value. The face-to-face arm has 24 participants at one site and was not powered for non-inferiority. Its comparison with control is also inconclusive at V3, which limits demonstrated assay sensitivity within this trial. Nonsignificance between active treatments is not equivalence.

The later TTS point estimates become more favorable. A formal **increase in treatment effect over time** is not established by their numerical order or separate p-values: the needed contrast covariance is absent, and Figure 1 describes separately expanded repeated-measures models. Nor can the different impairment/QoL significance patterns show that endpoint effects differ. They have different scales and no supplied joint contrast covariance.

## Executed aggregate computation

The [post-extraction computation plan](computation_plan.md), [inputs](aggregate_inputs.json), [standard-library Python code](aggregate_checks.py), [actual output](aggregate_checks.json) and [run log](execution_log.txt) preserve a deterministic, reproducible audit. This is not participant-data reanalysis.

1. The original primary gate fails; confirmatory non-inferiority therefore remains unavailable.
2. Six of the nine focal contrasts are nominally favorable with intervals excluding zero.
3. In an explicitly **post hoc, restricted nine-contrast sensitivity**, both Holm and Bonferroni retain four: TTS at V4/V5, impairment at V5, and GTS-QOL at V4. Holm adjusted values using the printed p-values are .021, <.009, .030 and .016 respectively; the computation uses .001 only as a conservative bound for the censored V5 TTS p<.001. Impairment V3 and GTS-QOL V5 no longer pass (.076 and .065).
4. The same decisions hold throughout conservative envelopes for three-decimal p-value rounding and p<.001 censoring. There are 33 passing checks, including separate step-down Holm decisions, monotonicity, edge cases and compliance arithmetic. Independent numerical review reproduced the focal inputs, adjusted results and all 33 checks.

**This sensitivity is neither the trial's prespecified multiplicity procedure nor a comprehensive correction for every reported analysis.** Its family was chosen to match the three-outcome/three-time question, not to confer confirmation on selected results. Numerous other endpoints and comparisons remain outside it. No adjusted effect-size confidence intervals were fabricated. Restricted robustness cannot repair the failed original gate, nonrandom missingness or reporting inconsistencies.

## Missingness, adherence and exposure

The randomized allocation is 67 iCBIT, 70 control and 24 face-to-face. The paper reports 108/161 compliant through V3, with 53 classified noncompliant: 42 had missing clinic visits and 11 insufficient sessions; nine further participants dropped out during follow-up. The published arm percentages uniquely reconstruct noncompliant counts of 27, 16 and 10, which sum to 53. These are **derived compliance classifications, not endpoint-specific observed sample sizes**. They cannot establish that exactly 119 were assessed at V3 or that the primary model used only 108 participants. [Paper, Methods 2.4 and Results 3](https://publications.rwth-aachen.de/record/889351/files/889351.pdf).

The mixed model assumes missing at random. LOCF and per-protocol sensitivity analyses are described as consistent with the primary result, without numeric sensitivity estimates in the inspected main text. Neither MAR assertion nor LOCF is a demonstrated bound against informative missingness. Arm-by-visit outcome counts, missingness-specific outcomes and joint covariance are not available here, so no attrition-adjusted efficacy, tipping-point estimate or joint responder count is justified.

Follow-up occurs while iCBIT access remains available; face-to-face participants could receive boosters. The defensible target is sustained benefit **under continued access to a learned intervention**, not proven persistence after all intervention exposure ends. Greater self-responsibility or ongoing practice is an explanatory hypothesis, not a tested mediator.

## Negative and inconsistent evidence retained

- Vocal-tic contrasts include zero at all three visits; motor contrasts are nominally favorable. This does not establish a motor–vocal treatment-effect difference.
- Video-rated tics favor iCBIT at V4, but not V3 or V5. The CGI-I responder model did not converge. Reported tic-responder contrasts use a threshold changed from 30% to 25% at a reported blinded review meeting; they cannot substitute for the primary continuous endpoint or a QoL response definition.
- GTS-QOL-VAS is distinct from the disease-specific total. Its V3 contrast is −7.32 [−12.02, −2.62], p=.002. Under standard higher-is-better life-satisfaction scoring, this points **away from iCBIT benefit**. The direction is explicitly documented in [Gerasch 2016, QoL methods](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2016.00416/full); trial-specific reverse coding was not verified, so that qualification must stay attached. The V4 interval includes zero and V5 sits at the printed p=.050/CI-zero boundary. Do not relabel these as uniform QoL improvement.
- Premonitory urges at V3 also point unfavorably: +1.46 [0.32, 2.59], p=.012. Later intervals include zero. Comorbidity outcomes do not show consistent benefit at every visit.
- Table 4 and narrative ATQ values disagree, changing V5's nominal significance. Table 3 gives impairment V5 upper CI −1.54, whereas prose prints +1.54. The focal calculation uses the table and retains the conflict. It cannot determine the corrected underlying analysis.
- Investigators attributed none of 128 reported incidents to treatment. That event count is not a count of affected participants; open-question ascertainment and sample size cannot establish absence of rare harms. This is separate from unfavorable patient-reported contrasts.

[Structured extraction](extraction.json) retains numeric details, source locations, funding/conflicts, eligibility and additional discrepancies. The registry/protocol use strict inclusion inequalities where the paper describes minimum scores; the protocol describes eight sessions over ten weeks while the paper describes eight weeks. Use relative visit timing rather than silently choosing a calendar week. The protocol abstract's other trial identifier is corrected only by reference to its own body and the official ONLINE-TICS record.

## Next bounded scientific decision

Close this trial-level extraction and the attempted joint-response/MNAR computation. Do not repeat it without corrected results, endpoint-specific missingness or covariance. No contact or participant-level access is authorized or needed for the next step.

The next useful question is **whether the adult behavioral-treatment benchmark supports maintenance beyond the acute response population and continued boosters**. Audit the original [Wilhelm et al. 2012 face-to-face CBIT randomized trial](https://pmc.ncbi.nlm.nih.gov/articles/PMC3772729/)'s primary and follow-up denominators, response-conditioned follow-up, booster exposure and separately measured impairment. It is an adult-dominant trial that includes ages 16–17; preserve that limitation and stop any adult-only estimate if a ≥18 subgroup is unavailable. This is a defined design/estimand comparison, not a pooled efficacy comparison, new severe-adult cohort search, or pediatric substitution. Do not assume GTS-QOL was collected or infer off-treatment durability from a responder-only follow-up.

## Provenance and scope

Read the current README, research protocol, status and 13 October burden-validation report through the GitHub connector first; source blob IDs and retrieval/search logs are in [provenance.json](provenance.json). The question was selected by the preceding day's explicit plan. This is one targeted trial audit, not a systematic review or an independent clinical validation.

The main PDF and protocol were readable. Main-paper screenshots failed; no visual verification is claimed. The live registry API was retrieved on 14 October 2026: status completed, actual enrollment 161, last posted update 27 May 2020, no posted aggregate results. It is supporting registration evidence, not new 2026 trial evidence. No correction/retraction was identified in limited searches; publisher access failure prevents comprehensive clearance. Exact German GTS-QOL translation/scoring and native-domain effects were not verified. No source full-text copies, patient records, family data, clinical action, outreach or paid resources were saved or used. No GitHub write was made by this analysis task.
