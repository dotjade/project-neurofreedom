# High internal consistency does not guarantee a well-fitting tic scale

## Finding and decision

**The 2021 EMTICS study provides a within-sample counterexample to treating a high alpha as comprehensive validation.** Total tic score alpha is .87, yet the same sample gives omega .58 and a marginal two-factor fit. This does not invalidate the YGTSS, prove any particular rating is biased, or establish that omega is the true reliability. It shows why the coefficient, model, population and intended outcome must be specified.

This is an audit of historical peer-reviewed evidence, not a newly published study or treatment result. [Haas et al.](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2021.626459/full), PMID 33716826, DOI 10.3389/fpsyt.2021.626459, was published February 25, 2021. The [October 26 audit](../../ygtss_validation/2026-10-26/report.md) concerned a different, 2018 sample and cannot substitute for the present validity tests.

## Prediction and method

The bounded question tests whether the 2018 pooled-alpha finding can safely stand in for factorial, convergent and discriminant validity. The operative prediction is that these properties can diverge. Strong fit and appropriately designed external comparisons would weaken a blanket skepticism about the scale; high alpha alone would not settle the question.

We inspected the primary Methods, Results, tables and Discussion, and the linked [EMTICS protocol](https://doi.org/10.1007/s00787-018-1190-4), PMID 29982875. [Source checks](source-checks.json) and [metadata checks](metadata-checks.json) document access. The computation uses only selected published aggregates in [inputs](inputs.json). It compares the printed fit indices against the alternative cutoffs cited by the authors, with a clearly conditional rounding sensitivity check. This is **deterministic arithmetic, not a simulation, model refit or patient-data reanalysis**. There is no random seed, individual reconstruction or newly estimated interval.

## Instrument and population boundaries

This is the **original YGTSS**, not an administered validation of YGTSS-R. The study discusses the later revised anchors as proposals to compare with its findings. It uses baseline assessments from a longitudinal parent study; its psychometric analysis is not longitudinal treatment response, prediction or developmental remission research.

The analytic cohort contains 706 children aged 3–16: 624 with Tourette syndrome, 76 chronic motor and six chronic vocal tic disorders. No adult, including a persistently severely affected adult, is represented. Mean impairment is 14.58/50; that does not establish applicability at the severe end. The protocol permits ASD and other neuropsychiatric comorbidity, but excludes children unable to understand/comply with the protocol or whose parents cannot comply. Permission to enroll is not proof of representation: the psychometric report does not provide ASD counts, communication strata or subgroup-invariance tests.

Trained clinicians rated YGTSS and CGI-S; ADHD and internalizing comparators were parent questionnaires. CGI-S, CY-BOCS and SNAP-IV concern the past week, while the SDQ comparator concerns two weeks. These differences in construct, informant and window constrain interpretation. Independent blinded rating of the convergence comparator was not established. The report says interrater reliability could not be assessed. Language-specific validation was not possible; similar site averages are not proof of cross-language invariance.

## Reconcile the properties, rather than pool them

| Property | Current primary result | What it does not establish |
|---|---|---|
| Internal consistency | TTS alpha .87, omega .58; global severity alpha .88, omega .56 | No universal true reliability, test–retest agreement or group-equivalent interpretation |
| Factorial validity | Ordinal WLSMV model with motor and phonic factors; impairment allowed to load on both. RMSEA .09 [.08, .10], CFI .90, TLI .87 | High factor loadings alone do not demonstrate good overall fit |
| Local and alternative models | At least 13 error-correlation pairs identified as misspecifications; subsequent EFA did not yield a satisfactory interpretable alternative | Residual correlations do not identify a biological cause, rater mechanism or justified corrected model |
| Convergence | TTS versus clinician CGI-S Spearman correlation .65 | One related rating is not an independent gold standard, agreement test or patient-relevant functional validation |
| Discrimination | TTS correlations: OCD .27, ADHD .24, internalizing .27 | Weak correlations do not imply these conditions cause little disability or that tic severity measures total burden |
| Impairment | Factor loadings .46 motor and .24 phonic | Tic-attributed impairment must not be dismissed because it is not the same construct as symptom severity |

The authors interpret the consistency and convergence as acceptable and discrimination favorably, while retaining only marginal fit. Their omega acceptance criterion of .50 for multidimensional scales is an explicit study convention, not a universally sufficient clinical standard. Exact omega implementation and its uncertainty are not independently reconstructed here. Correlated errors are a plausible methodological explanation for alpha/omega disagreement, not a demonstrated quantified correction to the 2018 estimate.

The 2018 TTS alpha was .82 and the current alpha is .87. Comparing .82 with current omega .58 as though reliability fell over time would conflate estimators and populations. The more informative contrast is within the current sample: different reported coefficients coexist with the same marginal model fit. The different global-score alpha values across papers are also not a change estimate; construction, scaling and sample comparability are not established sufficiently for pooling.

## Actual reproducible results

[Code](analyze.py) and [results](results.json) produce:

- Arithmetic alpha-minus-omega gaps of **.29 for TTS** and **.32 for global severity**. These are not estimates of alpha bias, biological signal loss or clinical importance.
- Using the paper's lenient alternatives, the printed RMSEA and CFI meet their respective cutoffs (.10 and .90), while TLI fails .90: **two of three**. With the stricter alternatives (.06, .95, .95), **zero of three** meet them. Neither triplet meets all three under this transparent conjunction convention; the paper does not prescribe that conjunction as a diagnostic rule.
- Under hypothetical rounding to two decimals, TLI remains below .90 throughout its .865–.875 rounding interval. RMSEA remains above .06 throughout .085–.095. CFI .90 lies at its lenient boundary, so its unrounded status cannot be inferred. These rounding intervals are not confidence intervals. The reported RMSEA interval [.08, .10] is preserved separately.
- The diagnosis counts sum to 706. No missing participant's score or subgroup membership is inferred.

Thus a high alpha does not settle the fit question even under relatively permissive published criteria. Conversely, marginal fit does not license treating every YGTSS result as unusable. The supported decision is to retain the scale's useful evidence and its limitations together, and report total tic severity separately from impairment and broader patient-relevant outcomes.

## Negative findings and unresolved documentation

The EFA's failure to produce a satisfactory alternative remains negative evidence, not a successful scale redesign. The paper also provides counterevidence to automatically adopting every 2018 anchor proposal: motor frequency was skewed, whereas phonic frequency was almost symmetric. That observation is not a direct trial of revised anchors.

The reported absence of age/site/TS-subgroup differences is not a formal equivalence or invariance demonstration. Detailed subgroup outputs are not shown. Methods describe the age sensitivity subgroup as at least eight years (n=578), whereas Results use greater than eight; the discrepancy is retained rather than repaired. Results give 178/706 without past-week phonic tics and 21/706 without motor tics. The Discussion's TS-focused wording must not turn these into 178/624 or imply absence of a lifetime qualifying symptom. The abstract's OCD value appears as “27”; Table 2 explicitly supplies .27, which is the value extracted here.

No new correlation significance comparison, residual-covariance model or uncertainty estimate was computed. Pair-specific correlation denominators, missingness handling, omega variant/implementation and complete subgroup precision were not established from the inspected main text. Independent review subsequently retrieved the official supplement and checked its aggregate table: 13 rows are classified as misspecifications and two as inconclusive; rows without misspecifications are omitted by design. This supports the reported count but is not an independent model refit. Expected parameter change signs are mixed, so no claim that every residual association is positive is made. The supplement supplies no omega variant, formula or analysis code. These are prerequisites for deeper statistical replication, not reasons to request participant data in this task.

## Access, safety and next decision

Publisher HTML and official Europe PMC XML were readable; direct PMC produced a browser challenge, not proof of a broken paper link. PubMed and a bounded exact-DOI notice search revealed no correction/retraction; this is not exhaustive integrity clearance. Protocol publication was July 7, 2018, with a 2019 issue date. Some authors disclose industry and other research relationships. No source paper, participant rows, private narrative or contact details are retained. No outreach, paid compute, medical action or treatment recommendation occurred.

Ten implementation tests pass; independent source/arithmetic review is supplied separately. These are research-documentation checks, not independent clinical peer review.

Close this fixed aggregate comparison absent clarifying public methods. Next audit the specifically identified [Ho et al. parent-versus-clinician study](https://pubmed.ncbi.nlm.nih.gov/32819930/) (2020, DOI 10.1136/bmjopen-2019-034634): distinguish correlation from agreement, patients from repeated visits, and shared information from independent ratings. Verify version, timing, completeness and subgroup exclusions before interpreting interchangeability. This addresses an explicit informant gap rather than repeating the alpha audit. Pediatric proxy evidence will still not establish adult self-report or ASD/communication-group equivalence. No new personal data or contact is needed.

## Reproduce

```sh
python analyze.py
python test_analysis.py
```

Run from this directory. The saved aggregates reproduce the arithmetic; live sources and search results may change.
