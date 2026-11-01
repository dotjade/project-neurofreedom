# CANNA-TICS: direct functional evidence, without established superiority

1 November 2026. Historical peer-reviewed randomized trial plus official aggregate registry results. **Exploratory published-aggregate reanalysis, not a simulation, new trial, treatment recommendation or clinical validation.**

## Question, prediction and decision

Does CANNA-TICS identify randomized improvement in directly measured quality of life/function independently of its tic-responder result? The [local prospective plan](plan.md) was written before extraction/computation, SHA-256 `17a61c12c086c51d01507faad27ae3ab17e712a05e7315764bb4af20718cbddb`. This was not an externally registered analysis.

Prediction: tic-response findings alone cannot establish functional benefit. Disconfirming evidence would be compatible direct between-arm functional contrasts with uncertainty and multiplicity context. **The trial does provide direct contrasts, so it would be wrong to dismiss all its function claims as merely inferred from tic response.** However, all five focal confidence intervals include zero; they do not establish superiority, equivalence or absence of worthwhile benefit. The functional results are exploratory and depend on imputation. One QoL-VAS table row contains a visually verified arithmetic inconsistency.

Decision: retain the clinical signal and uncertainty together, reject established functional-superiority and no-benefit claims, and do not rank this treatment against other interventions from incompatible studies. This returns the project to direct adult clinical outcomes after completing the force-matching measurement branch.

## Sources and dates

Müller-Vahl et al., [primary article](https://doi.org/10.1016/j.psychres.2023.115135), PMID [36878177](https://pubmed.ncbi.nlm.nih.gov/36878177/), was first online **February 28, 2023**, with a May 2023 issue date. A lawful [German National Library copy](https://d-nb.info/1334360707/34) was inspected transiently. The [EU Clinical Trials Register results](https://www.clinicaltrialsregister.eu/ctr-search/trial/2016-000564-42/results), EudraCT **2016-000564-42**, cross-reference **NCT03087201** and show first/current results publication **December 31, 2023**. Neither source is newly published in November 2026. The registry reports final analysis November 15, 2021 and trial end November 20, 2020; those are different dates.

[Source log](source-log.json), [selected original aggregate extraction](inputs.json), [code](analyze.py), [results](results.json), [tests](test_analysis.py) and independent review preserve provenance. The primary PDF was read in memory; a temporary page render confirmed focal Table 3 cells and Table 4 counts and was deleted. No full paper, source screenshot, participant file or clinical narrative is retained.

## Population and estimand

This double-blind randomized placebo comparison directly includes adults with TS or chronic motor tics. Of 98 randomized people, one untreated participant was excluded: the treated analysis set contains 64 nabiximols and 33 placebo participants. Thus it is not an all-randomized 98-person analysis. Registry completion counts are 48/64 and 24/33, not endpoint-specific observed functional denominators.

The paper reports 58/64 and 31/33 with TS, six and two with chronic motor tics, and no chronic vocal-only participants. Mean ages are 37.4 and 34.9; baseline total-tic means are 28.6 and 29.3. Eligibility required at least moderate illness and tic-score thresholds, but does not establish a separately analyzed persistent-severe-adult group. Exclusions include pervasive developmental disorders, schizophrenia history, comorbidity requiring primary treatment and substance-use disorder, limiting transport to people with these unmet needs. Registry age categories cover 18–64, not older adults or children.

Treatment lasts 13 weeks including four titration weeks and nine stable-dose weeks. Functional ANCOVA compares end-of-treatment change, adjusting for baseline, treatment and pooled center (Hannover versus others). The paper describes baseline mean imputation and last observation carried forward for missing follow-up. Row-specific observed counts and complete sensitivity results are not established. The arm headers 64/33 must not be reinterpreted as 97 complete observed questionnaires.

## Direct functional comparisons

Contrasts are reported nabiximols minus placebo. The table preserves published estimates, not reconstructed model results.

| Endpoint | Reported contrast | Reported 95% CI | p |
|---|---:|---|---:|
| GTS-QoL normalized | −4.13 | −8.65 to 0.39 | .07 |
| GTS-QoL VAS | +5.55 | −0.69 to 11.80 | .08 |
| YGTSS tic-attributed impairment | −4.12 | −8.45 to 0.22 | .06 |
| SF-12 physical | +0.69 | −2.24 to 3.63 | .64 |
| SF-12 mental | +2.12 | −1.39 to 5.64 | .23 |

Lower QoL burden and tic-attributed impairment conventionally indicate improvement; life-satisfaction VAS and SF-12 conventionally favor higher values. Exact trial-specific reverse coding/normalization was not verified, so no new standardized effect or clinical threshold is assigned. These scales measure different constructs. Tic impairment is not all participation, pain or comorbidity-related burden, and marginal improvements do not identify the same people improving jointly.

The authors describe p<.1 as a substantial trend. That exploratory convention does not turn .06–.08 into confirmatory superiority. Fitness to drive, rather than these five outcomes, was the key secondary endpoint; no confirmatory multiplicity control for the focal function claims was established. No post hoc threshold, pooled scale effect, or absence-of-benefit declaration is imposed here.

### Executed consistency test

Four of five focal arm least-squares mean differences equal their reported contrast. The QoL-VAS arm entries −3.19 and −2.36 subtract to **−0.83**, not the printed **+5.55**, which the prose also repeats. The discrepancy is **6.38 points**. It exceeds a conditional ±0.015 numerical envelope if each of the three displayed quantities was rounded independently to the nearest .01. This envelope is not a confidence interval.

Independent visual inspection confirms the printed cells; this is not merely PDF text extraction. It does not establish which value, coding description or row is wrong. The reported +5.55 and CI are retained as reported, not endorsed as reconciled. A corrected aggregate table or explicit model/scoring explanation is the exact prerequisite. The separate global-YGTSS interval discrepancy noted in extraction is not silently repaired or used as a focal outcome.

## Primary tic response: signal with uncertainty

The primary responder threshold was changed from 30% to 25% at blinded review, according to the paper. The exact review date and full amendment/SAP sequence were not verified. Do not infer either a fully unchanged original endpoint or outcome-driven misconduct. Registry title says >25%, while its description says at least 25%; its 30% entry repeats a 25% description. These conflicts remain visible.

There were **14/64 responders (21.875%)** versus **3/33 (9.091%)**. Missing primary outcomes were counted as nonresponse. The published center-stratified Mantel-Haenszel superiority analysis did not establish superiority: paper p=.07 and placebo-minus-nabiximols difference −.13 [−.28,.01]; registry p=.0755, difference −.1278 [−.2688,.0131]. Preserve both intervals: their lower endpoints are not simply the same value rounded to two decimals. No preferred corrected interval is invented.

Our separately specified **unadjusted** calculation reverses direction to nabiximols minus placebo:

- Risk difference **+12.784 percentage points**, hybrid Wilson/Newcombe 95% interval **−3.944 to +25.784 percentage points**.
- Risk ratio **2.406**, approximate log-Wald 95% interval **0.744 to 7.785**.

This uses the [Newcombe independent-proportions method](https://pubmed.ncbi.nlm.nih.gov/9595617/) without continuity correction. It does not reconstruct the stratified model, adjust center effects, or supply a functional effect. Small event counts make the risk-ratio interval particularly imprecise. Different methods legitimately produce different intervals; this calculation is not a correction of the authors' analysis. All these estimates remain null-compatible, and none proves equivalence or zero efficacy.

## Harms and missingness remain separate outcomes

The paper reports at least one adverse event in **61/64 (95.31%)** versus **26/33 (78.79%)**, while **315 versus 116** are numbers of events, not people. Potentially related adverse events affected 58 versus 21 people. Registry adverse-event discontinuation counts are five versus one; one person per arm had a serious adverse event. These are short-trial descriptive aggregates, not individual risk predictions or proof of equal safety.

Registry ascertainment is systematic from first administration through last follow-up. Its nominal non-serious-event section explicitly includes all events, including serious ones; do not add serious counts again. Registry noncompletion is 25/97, whereas the paper's discussion gives dropout 19.4%; definitions are not reconciled. Completion, dropout, adverse-event discontinuation and endpoint-specific missingness must not be conflated. No individual event narratives were copied.

The paper discloses DFG support and detailed industry/material/consultancy relationships. The bounded exact-DOI integrity search found no notice; this is not comprehensive correction/retraction clearance or conflict-free certification.

## Uncertainty and next decision

The study supplies a direct adult randomized functional test, which is stronger than inferring function from tic-score change. But short duration, imputation, unverified endpoint-specific missingness, exploratory multiplicity, scoring/reporting ambiguity, exclusions and lack of a verified meaningful-change anchor limit its interpretation. There is no treatment-free durability, disease-modification, cure or severe-adult subgroup claim. No cannabinoid use or treatment change is recommended.

Next perform a bounded public documentation audit of this trial's protocol, dated amendments/SAP and lawful aggregate sensitivity outputs: do functional conclusions remain compatible under documented missingness analyses, and are score direction and endpoint timing fixed before unblinding? In advance, disconfirm concern if the public documents supply prespecified endpoints, explicit score coding, endpoint-specific observed counts, corrected VAS output and compatible between-arm sensitivity intervals. If these are absent, record exactly which are missing and close the branch rather than infer unpublished outcomes, contact authors or open participant datasets. This documentation task is not a misconduct investigation, new trial or permission to collect data.

## Reproduce and verification

From repository root:

```sh
python analyses/canna_function/2026-11-01/analyze.py
python -m unittest discover -s analyses/canna_function/2026-11-01 -p 'test_*.py' -v
python updates/2026-11-01-weekly/verify_daily.py
```

Python standard library, no RNG/seed, participant data or paid compute. Ten implementation tests cover boundary cases, group exchange, arithmetic, null compatibility and determinism. The separate daily verification is explicitly a reproduction of an earlier aggregate result, not a second new result. Twenty-nine independent source/numeric checks pass in [the review](review/review.md); checks are not clinical peer review. Publisher access was blocked while the lawful institutional primary copy and official registry were readable; supplement access and detailed sensitivity analyses remain unverified.
