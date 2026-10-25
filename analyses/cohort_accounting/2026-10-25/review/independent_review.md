# Independent review of conditional DBS cohort accounting

25 October 2026, approximately 03:40–03:42 UTC. This review concerns set arithmetic and source-to-assumption handling, not clinical peer review or treatment-effect validation.

## Finding

The fixed input/output arithmetic is correct under its explicitly stated containment assumptions. Five heterogeneous report-role counts sum arithmetically to 43, but this is not an eligible-person total or a duplication-rate denominator. The five records name two trial families, not five independent clinical replications.

An independently written integer Venn-cell enumeration, rather than the parent script's overlap-loop formula, finds seven feasible aggregate configurations given enrollment sizes 10 and 8 and a 16-person mixed report contained in their union. The union can be 16, 17 or 18; intersection can be 0, 1 or 2. With disjointness imposed, the union is 18 and the mixed report can allocate (older,newer) as (8,8), (9,7) or (10,6). Without the mixed-report constraint or disjointness, union size can be any integer 10–18. Thirteen independent assertions passed, including incompatible-count and zero/small-set controls. These are conditional mathematical constraints, not observed membership, clinical sample sizes, confidence intervals or estimates of treatment benefit.

The original 12 tests also passed when rerun by this reviewer. No patient identities, individual rows or outcomes were required or reconstructed.

## Source/assumption review

- [Lowor 2026 primary preprint Methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC13596655/): independently retrieved indexed primary-source text reports sixteen people recruited as part of two related studies, and explicitly names NCT02056873 and NCT05371041. This supports the mixed-family linkage; it does not enumerate each person's trial membership or prove consistency with every later enrollment universe. Preprint status remains preliminary.
- [Cagle 2022 primary report](https://pmc.ncbi.nlm.nih.gov/articles/PMC9468946/): indexed primary-source text independently confirms four analyzed embedded-device participants and NCT02056873, distinct from six screened/consented. The four are not an additional cohort merely because a separate publication exists.
- Official ClinicalTrials.gov API was fetched using only `NCTId,EnrollmentCount,EnrollmentType,EligibilityCriteria` projection for [NCT02056873](https://clinicaltrials.gov/api/v2/studies/NCT02056873?format=json&fields=NCTId,EnrollmentCount,EnrollmentType,EligibilityCriteria) and [NCT05371041](https://clinicaltrials.gov/api/v2/studies/NCT05371041?format=json&fields=NCTId,EnrollmentCount,EnrollmentType,EligibilityCriteria). Live selected metadata confirmed actual enrollment 10 and 8. The newer trial excludes prior neurosurgical intervention including DBS and explanted DBS systems. No outcome/result measurements, contacts or individual rows were requested.
- The earlier public October 20 and October 22 source audits support Lowor's five-person physiology subset within a six-implant publication and Okun's ten enrolled cohort. This review did not freshly reproduce Lowor's full main-methods extraction or inspect participant tables; it does not claim independent confirmation of every membership edge.

**Necessary interpretation qualification:** registry identifiers and current enrollment counts are not an audited individual census. All report-containment bounds are conditional on accurate distinct-person counts and nesting in the named enrollment universes. Eligibility supports a disjointness scenario only if implemented and if the enrollment-universe correspondence holds; it is not identity verification. Without accepting containment, no informative unique-person census is established here. Do not compute a percentage of duplicate participants or pool endpoint denominators from these figures.

## Implementation correction

The reviewed parent code bound `a,b` to dictionary value order while labelling them older/newer. That yields correct results for the fixed serialized inputs, but reordering cohort keys could swap allocation labels. Recommended correction: use explicit NCT identifiers and add a key-order invariance test. This is an implementation robustness issue, not a change to the current scientific arithmetic. Publication should confirm the correction or explicitly restrict the function to the fixed ordering.

## Limits

The five sources are selected from this week's DBS trail, not an exhaustive DBS literature census. No clinical efficacy, safety rate, uncertainty interval or general adult applicability follows from family bookkeeping. Sources contribute different estimands and observations even when recruitment overlaps. This review did not rerun original clinical/physiology analyses, seek private data or contact investigators. Source bodies were used transiently; only original commentary and the independent aggregate checker/output are retained.

## Correction verification, 2026-10-25 03:44 UTC

Re-read the corrected implementation: cohort sizes are now bound explicitly to `NCT02056873` and `NCT05371041`. The added `test_cohort_key_order` reverses the input key order and confirms unchanged full results. Reran the complete implementation suite: all 13 tests passed. Independently recalculated from the fixed JSON inputs and confirmed exact equality with the saved `results.json`; the scientific outputs are unchanged. The previously noted implementation issue is closed.

A focused overclaim scan of the weekly synthesis found the cohort-accounting conclusions appropriately conditional, explicitly not an observed unique-person census, duplication rate or clinical effect denominator. This focused check is not independent revalidation of every daily evidence extraction summarized in the weekly report.
