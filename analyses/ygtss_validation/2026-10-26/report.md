# What the 2018 YGTSS study validates, and what it does not

## Decision

**The original multicenter study supports pooled tic-scale internal consistency, not ASD/communication-group measurement equivalence.** The October 25 plan is advanced by an instrument-version, population and reliability audit, not a new treatment finding. Neither proof of unbiased measurement nor proof of measurement bias follows. This preserves the measured ASD association in the prior cohort while keeping its proposed reporting mechanism unvalidated.

## Prediction and method

Before extraction, the operative prediction was that a broad reliability claim would not by itself establish comparable interpretation between ASD/communication groups. Counterevidence capable of changing that decision would be documented subgroup representation plus an appropriate invariance, differential-item, external-criterion or independent informant-agreement analysis. Merely including adults or common comorbidities would not meet that test.

We inspected [McGuire et al.'s primary paper](https://escholarship.org/uc/item/4bh642p5), Methods, Results, Tables 1–3 and Discussion, and checked its [PubMed record](https://pubmed.ncbi.nlm.nih.gov/29653992/) and [publisher metadata](https://www.neurology.org/doi/10.1212/WNL.0000000000005474). PMID 29653992, PMCID PMC5952973 and DOI 10.1212/WNL.0000000000005474 identify a peer-reviewed article published online April 13, 2018, in the May 8 issue. It is historical evidence, not an October 2026 discovery.

[Inputs](inputs.json), [code](analyze.py), [results](results.json) and [tests](test_analysis.py) record selected published aggregates and deterministic arithmetic. **This is not a simulation or participant-data reanalysis.** No seed is needed. We did not estimate new reliability coefficients, individual scores, confidence intervals, causal effects or biological mechanisms.

## Population, informant and instrument map

| Audit question | Verified coverage and interpretation |
|---|---|
| Population | Seven US specialty clinics; 617 people, ages 5–69: 516 youth and 101 adults. Diagnoses: 552 Tourette, 46 chronic motor, five chronic vocal and 14 transient tic disorders. This is not an adult-only or persistent-severe-adult validation. |
| Comorbidity | Current ADHD, OCD, anxiety and depression are described. ASD counts, language/IQ strata and their analytic representation are not reported in the inspected main article. Unreported is not zero, and no universal ASD exclusion is inferred. |
| Ascertainment | Methods specify 410 structured interviews and 207 best-estimate diagnoses. Thus the abstract's general interview description must not be read as 617 structured interviews. |
| Informants | Participants and parents of youth took part in clinician-administered diagnostic assessment. The same or another trained clinician rated YGTSS; supervision varied by source protocol. Separate child, parent and clinician agreement estimates were not supplied. The diagnostic informant description does not identify each informant's weight in the final tic rating. |
| Endpoints | Recent 7–10-day motor/phonic dimensions combine into total tic score; tic-attributed impairment is separate. Both total tic and impairment scales span 0–50, but equal ranges do not make them interchangeable or exhaustive measures of lived burden. |
| Instrument version | Existing YGTSS data informed expert-consensus anchor/checklist revisions. Recommendation of YGTSS-R is not an independent prospective test of the revised form or a head-to-head demonstration of improved precision. |

## Reliability is not one property

The measured pooled alpha values are motor .80, phonic .87 and total tic .82. The total-tic-plus-impairment entry is .67. Alpha concerns item-score covariance, not whether two informants agree, scores remain stable, ratings mean the same across groups, or an outcome captures everything important to patients. The article explicitly says interrater and test–retest reliability across sites/raters were not examined, despite rater training. Earlier reliability figures cited in its Introduction belong to earlier studies, not new results in these 617 people.

A lower combined alpha does not prove impairment is invalid, nor justify deleting it. It reinforces the need to state the intended construct rather than treating symptom intensity and functional impact as a single interchangeable outcome. No ASD-group validation test satisfying the prediction's counterevidence criterion was identified in this report. That is a bounded documentation result, not a field-wide claim that no such evidence exists.

## Actual arithmetic and negative evidence

The five partition checks reconcile age groups, diagnoses, sites and diagnostic assessment counts. Adults comprise **16.369530%**; chronic motor/vocal diagnoses together **8.265802%**; structured interviews **66.450567%**. These are sample composition, not population prevalence, model completeness or evidence of validity in small subgroups.

From Table 1 rounded means, adult minus youth differences are motor **+0.95**, phonic **-1.97**, total tic **-1.02** and impairment **+1.77** points. Table 1 marks motor and phonic differences significant, but not total tic or impairment. The latter nulls are not equivalence tests. Opposite motor/phonic directions show why a similar sum cannot establish identical component behavior. These are cross-sectional group contrasts, not developmental trajectories, remission, or within-person change.

The authors combined age groups after descriptive comparisons. Similar means are compatible with different measurement relations and do not establish invariance. Comorbidity and sex differences also remain; pooled coefficients must not silently become adult-specific or ASD-specific coefficients.

### Source inconsistencies retained, not repaired

Table 2 and the abstract give motor alpha .80, while Discussion gives a narrower .82–.87 range. We retain the explicit table values. In PDF text extraction, Table 3 shows negative signs for motor complexity (-.21) and phonic intensity (-.30), alongside positive-direction labels. PDF screenshots failed, so these are **text-extraction discrepancies pending visual confirmation**, not conclusively identified printing errors. We do not correct signs, reconstruct distributions or use those cells in computation. Distribution skew alone would not establish informant bias even if every sign were confirmed.

## Uncertainty, access and limits

Specialty referral and source-trial selection constrain generalization. An adult age range does not establish sustained severe symptoms, and the small chronic-vocal subgroup cannot validate all single-modality presentations. Tic-related impairment is not a substitute for pain, participation, quality of life or all comorbidity-related burden. The study does not measure treatment response or show that reported lower impairment in another cohort is true lower total disability.

Main-paper text was available from the lawful UC repository and indexed primary-source extracts. Direct PMC access produced a browser challenge; Europe PMC XML returned HTTP 500. Supplement documents and original source-trial exclusion criteria were not audited. No full-text paper, case narrative, participant data, private story or contact details are retained in deliverables. Bounded DOI notice search and PubMed EFetch found no linked correction/retraction; this is not exhaustive integrity clearance. Author disclosures include research funding, royalties and industry relationships, not an absence-of-conflict certification.

Seven implementation tests passed, including the five partition checks and output reproduction; these are software checks, not independent clinical peer review. Independent review is recorded separately. An initial command used the wrong working directory and failed to find inputs; the corrected repository-local run passed. No outreach, data request, paid compute or medical action occurred.

## Next bounded decision

Close this fixed 2018 audit unless new subgroup or revised-form validation documentation appears. Next inspect the independent [2021 EMTICS psychometric study, PMID 33716826](https://pubmed.ncbi.nlm.nih.gov/33716826/) (DOI 10.3389/fpsyt.2021.626459): reconcile its factorial/convergent/discriminant tests and negative fit findings with the 2018 pooled-alpha claim, keeping total tic and impairment distinct. Verify instrument version and pediatric eligibility before extrapolating to adults or ASD/communication groups. Do not repeat adult cohort searches or obtain participant data. The required prerequisite for a direct subgroup conclusion remains public subgroup-specific validation with defined informants, constructs and uncertainty.

## Reproduce

From this directory:

```sh
python analyze.py
python test_analysis.py
```

Results are deterministic from the saved selected aggregates. Source retrieval can change and is not part of an offline clinical validation.
