# Parent and clinician tic ratings: discrimination is not interchangeability

## Decision

**The study supports useful parent-reported discrimination in a selected pediatric clinic, not interchangeable continuous scores or proven improvement caused by practice.** Reported masking and clustered analysis are strengths. They do not remove shared-information, timing, selection and endpoint uncertainties.

This advances the October 27 informant question using [Ho et al.'s peer-reviewed study](https://pubmed.ncbi.nlm.nih.gov/32819930/), published August 20, 2020, DOI 10.1136/bmjopen-2019-034634. It is historical evidence, not a new October 2026 clinical result.

## Prediction and method

The working prediction was that agreement sufficient to replace clinician scores requires more than a favorable association or discrimination statistic and a nonsignificant mean difference. Evidence capable of changing that decision would include clearly defined score versions, paired timing, appropriate repeated-measure agreement estimates with uncertainty, and clinically justified equivalence limits.

We inspected the primary Methods, numerical Results, Table 1 and limitations through official Europe PMC XML; [metadata](metadata-checks.json) and [source checks](source-checks.json) identify retrievals. [Code](analyze.py) uses [saved published aggregates](inputs.json) to reconstruct the reported binary assessment table, check denominators and test a conditional score-additivity explanation. **This is not a simulation, patient-data reconstruction or a refit of the study's models.** There is no randomness or seed. No new confidence intervals, individual trajectories or medical decisions were generated.

## Who, what and when was compared?

| Question | Source-supported answer and boundary |
|---|---|
| Population | Regularly followed pediatric Tourette patients at one Taiwan center. Final mean age 8.8 years, SD 2.97. Newly diagnosed patients were few. No adult or chronic motor/vocal-only validation is established. |
| Selection | 594 enrolled, 3,356 parent submissions, but 1,455 paired assessments from 527 patients analyzed. Fellows sampled by convenience in the waiting room. Pairing is a selection step, not random retention. |
| Instrument | Authors translated the YGTSS into traditional Chinese, reached physician consensus and supplied a revised online parent form with introductory explanation. This wording alone does not establish identity with the 2018 YGTSS-R anchors or a cross-cultural equivalence test. Figure 1 is a partial online-form illustration, not a verified complete version comparison. |
| Timing | Parents were encouraged to complete the form the day before the visit; fellows rated at the visit. Results call evaluations simultaneous, but the limitations explicitly say they were not. We retain same-visit pairing, not verified simultaneous observation. |
| Independence | Parents and fellows were masked to each other's scores. This is not proof of independent symptom information: clinician assessment can rely on family report, and observation settings differ. No independent biological gold standard is supplied. |
| Subgroups | ASD, communication ability, detailed eligibility/exclusion criteria and severe-persistent symptom strata are not sufficiently reported to establish subgroup coverage. Missing information is not an inferred exclusion or zero count. |

A parent proxy rating is not an adult's own report. Tic-related impairment is also not a complete measure of pain, participation, quality of life or comorbidity burden. The project's severe-adult and broader chronic-tic questions therefore remain open rather than being replaced by this convenient pediatric sample.

## Preserve the positive findings and their estimands

The authors used generalized estimating equations (GEE) to account for participant clustering in repeated score-difference analyses and describe logistic GEE for discrimination. That is stronger than treating all visits as independent. The paper reports AUROC **.858 (95% CI .839–.876)**, sensitivity **79.7% (76.6–82.8)** and specificity **91.8% (89.9–93.7)** against clinician categories. These are useful discrimination findings within this selected sample. No separate held-out validation set is established.

AUROC assesses ranking across a binary reference classification, not whether two continuous scores can be substituted. The inspected report does not provide a numerical correlation coefficient, intraclass correlation, Bland–Altman limits of agreement or a prespecified equivalence margin that would establish score interchangeability. References to high correlation in prose must not become an invented numerical result. Nor would a high correlation by itself establish agreement.

The entire-score difference is reported as 4.15 points (95% CI 3.82–4.48), and combined-tic difference as 2.40 (2.22–2.58). With each repetition, the reported absolute difference decreases by .24 points (.14–.34) for the entire score and .17 (.11–.22) for combined tics. These are observational repetition associations. Follow-up selection, changing severity, familiarity, treatment and other time-varying influences are not disentangled by the coefficient. Nonsignificance after four assessments is not a demonstration of equivalence, nor a validated four-session training prescription. Per-repetition sample sizes and participant retention are needed for a stronger interpretation.

## Actual aggregate reconciliation

The [reproducible results](results.json) distinguish assessments from people:

- 527/594 = **88.72%** of enrolled patients appear in paired analysis; 67 do not. This is not an established follow-up retention rate.
- Figure 2 reports 1,522 fellow evaluations. Of these, 67 are not among the 1,455 paired assessments. This is a different entity from the coincidentally equal 67 enrolled patients outside the paired analysis.
- 1,455/3,356 = **43.36%** of parent submissions are paired; 1,901 lack a paired fellow assessment in the reported analysis. These are reports, not 1,901 missing patients.
- The clinician-reference table is:

| Parent category | Clinician moderate/severe | Clinician mild |
|---|---:|---:|
| Moderate/severe | 507 | 67 |
| Mild | 129 | 752 |

The cells total 1,455. They reproduce sensitivity 507/636 = **79.716981%** and specificity 752/819 = **91.819292%**, rounding to the published values. There are **196 discordant assessments, 13.470790%**, and 86.529210% category concordance. This is not 196 distinct people, an independent-sample accuracy estimate, or a population diagnostic rate. No cluster-naive binomial confidence intervals are added. A clinician-reference false-negative label would describe disagreement with that reference, not proof that the parent missed the patient's biological state.

### Score boundaries and additivity remain unresolved

Methods define mild as a YGTSS score below 20 and moderate/severe above 20. Exactly 20 is not assigned, and the exact score component used for this dichotomy is not made sufficiently explicit. The two reported reference counts nevertheless exhaust the 1,455 pairs. We reproduce their categories without silently changing the cutoff to at least 20, choosing the 0–50 or 0–100 endpoint, or inferring how many boundary cases existed.

Methods call the differences absolute but describe subtraction of parent scores from physician scores. Therefore no consistent direction of parent under-rating or over-rating is inferred from Table 1. Combined-tic difference 2.40 plus impairment difference 2.41 gives 4.81, not the reported entire-score 4.15. This is **not automatically an error**. If all are mean absolute differences on the same additive paired scores, the triangle inequality permits an entire-score value between |2.40−2.41| = **.01** and 2.40+2.41 = **4.81**; 4.15 lies inside. If instead these were signed means over the same observations, additivity would require a different explanation. This conditional calculation cannot decide which definition was implemented, recover individual signs, or repair a source value. It prevents an unjustified contradiction claim while identifying the exact missing prerequisite.

## Limitations and safety

Convenience selection, regular-clinic familiarity, variable fellow assessment, incomplete pairing, unclear score boundary and nonidentical observation times limit transfer. Masking of scores is retained as counterevidence against a simplistic claim that assessors simply copied each other. Conversely, neither masking nor GEE supplies unreported agreement limits or guarantees an unbiased independent reference.

The publisher route returned HTTP 403; official XML was readable. An initial full-body display incidentally included the paper's feedback quotations; no quotation, participant narrative or identifying medical data was retained in deliverables or used in the analysis. Subsequent extraction focused on aggregate methods/results. Public feedback anecdotes are not evidence of clinical efficacy. No source paper, private information, intervention, contact or paid compute is included. The source reports no specific funding and no declared competing interests; this is not independent verification of all relationships. Bounded PubMed and DOI-notice checks found no correction/retraction, not exhaustive integrity clearance.

Eleven implementation tests pass. Independent source/arithmetic review is recorded separately; this is not clinical peer review. The original GEE covariance, missingness assumptions, score coding and per-repetition precision were not re-estimated.

## Next bounded decision

Close this fixed informant audit unless public documentation resolves score identity, the boundary at 20, absolute-versus-signed handling and repeated-measure agreement uncertainty. Do not repeat generic scale audits or request participant data.

The next distinct question is the previously discovered [Wang et al. genetic-association study](https://doi.org/10.1038/s41593-026-02419-5), PMID 42680906: map which of the 36 reported risk genes are supported by chronic-tic-specific versus OCD or combined analyses, the multiple-testing thresholds and replication evidence. Test whether a transdiagnostic union can support a Tourette-specific target claim, preserving negative and nonsignificant disorder-specific evidence. Use public aggregate tables only, not individual variants or family pedigrees. Association will not be treated as a treatment target, causal mechanism or patient-specific prediction.

## Reproduce

```sh
python analyze.py
python test_analysis.py
```

Run from this directory. The saved aggregate inputs reproduce the calculations; live source content may change.
