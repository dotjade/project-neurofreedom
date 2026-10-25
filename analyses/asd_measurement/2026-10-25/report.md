# ASD, age and measured tic impairment: an estimand audit

## Decision

**The pooled adjusted association is not an adult-specific burden estimate, and the suggested reporting explanation is not a tested mechanism.** This closes the October 24 question using one previously extracted primary study, rather than counting it as a new paper.

[Aldurayhim et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC13683974/) (PMID 42902960; DOI 10.1002/mdc3.70882; published October 20, 2026) reports a lower adjusted YGTSS impairment coefficient with ASD. That result is retained. It neither establishes less lived burden nor warrants dismissing the measured association. Measurement differences, clinical differences, selection and residual confounding remain competing explanations.

## Prediction and method

The [prediction](prediction.md) specified what would overturn this conclusion: adult-stratified estimates or adequate interaction support, and an independent test of the proposed measurement explanation. Official PMC XML was inspected transiently; selected public aggregate facts, source hash and original notes were retained, not the paper. Methods, Tables 1–3, Discussion, limitations and supplement inventory were audited. The only listed supplement is an ICMJE disclosure form, not a reported adult-stratified results appendix. It was not downloaded. No participant data were accessed or requested.

[Code](analyze.py) runs deterministic aggregate arithmetic on [inputs](inputs.json). This is **not a simulation**, patient reanalysis or clinical validation. There is no random seed because there is no randomness. [Results](results.json) distinguish calculations from source claims; the [source record](source-provenance.json) provides dates and identifiers.

## Age and design coverage

The 535-person referral cohort includes ages 3–72, with mean 15.23 years, but an age range and mean do not identify the adult subgroup or its ASD composition. The report gives 49 people with ASD, including only three with support level 3. Parent registries are longitudinal, but this analysis uses first-visit observations only. Neither repeated follow-up nor a population prevalence estimate follows.

Table 3 adjusts for age at enrollment and age at tic onset alongside sex, comorbidities and medication classes. It does not report an age-by-ASD interaction or adult-stratified outcome estimate. A common pooled ASD coefficient does not supply separately estimated adult and pediatric contrasts. The enrollment-age association with impairment also cannot establish within-person worsening with age. Adult-onset, secondary and functional tic-like presentations were excluded; the sample does not establish applicability to all adult tic presentations or persistent severe adult burden.

## Comparable endpoints and counterevidence

YGTSS total tic score and separately rated impairment both range 0–50, but are different outcomes. Their global sum is not a substitute for an independent functional assessment. The study rates recent tics and tic-attributed impairment, not all disability attributable to ASD, ADHD, mood, pain, sleep or social context.

| Endpoint | Unadjusted ASD minus non-ASD mean, calculated | Reported unadjusted p | Reported adjusted ASD coefficient (95% CI) | Reported adjusted p |
|---|---:|---:|---|---:|
| Tic-related impairment | -3.06 | .111 | -4.49 (-8.46 to -0.51) | .027 |
| Total tic severity | +1.84 | .152 | -0.31 (-2.91 to 2.29) | .814 |

The impairment association is statistically detected after adjustment, while the unadjusted contrast is not. These answer different questions in potentially different analytic subsets; the numerical change is not an identified confounding effect or causal decomposition. For total tic severity both reported tests are nonsignificant. This is not an equivalence test: its adjusted interval still includes both directions. Selectively retaining the impairment p value would obscure the null severity result and exploratory context.

## Actual aggregate computation

- Impairment model: 483/535 = 90.28% of the cohort; 52 people are not in that model count.
- Severity model: 485/535 = 90.65%; 50 are not in that model count.
- Assuming both are subsets of the reported cohort, their overlap is bounded by 433–483 people. This is an arithmetic feasibility range, **not observed overlap** or identification of which people were omitted. At least two model-inclusion statuses differ because the counts differ.
- The available totals do not identify adult, ASD or support-level representation within either regression. Table 2 group headings also do not establish outcome-specific item completeness.
- Level 3 support comprises 3/49 = 6.12% of the ASD group; that arithmetic does not validate a severe-support-needs subgroup estimate.

No standard errors, new confidence intervals, individual scores, adult counts or adjusted regressions were reconstructed. Missingness causes and exact overlap remain unknown. The computations audit denominators, not treatment or disease biology.

## Measurement explanation: proposed, not demonstrated

The authors discuss possible communication, informant and symptom-attribution differences. This is a plausible explanation, not a quantified finding about measurement bias in this dataset. The inspected report does not present a language/IQ-adjusted validation model, ASD-group measurement-invariance test, independent patient-versus-proxy agreement analysis or externally validated total-function contrast. A clinician-rated scale is not automatically free of informant effects. Conversely, absence of that validation does not prove ratings are biased.

Alternative explanations remain: genuine differences in tic-attributed burden, referral selection, comorbidity and treatment patterns, residual confounding, misclassification, or combinations. Prescribing differences and medication covariates cannot establish treatment response or medication harm. No mechanism is selected from these alternatives by the reported pooled association.

## Uncertainty, access and applicability

The study is observational, exploratory and tertiary-clinic based. The public paper supplies model totals but not adult-by-ASD model membership or a direct measurement validation. Public data are restricted for ethical/privacy reasons; no request was made. Supporting disclosures were not audited. Publication and PubMed indexing dates are distinct; the paper was already extracted October 23. This report is an AI-assisted methods audit, not independent clinical peer review. No patient/family stories, interventions, recruitment, contact or paid compute were involved.

## Next decision

Close this fixed cohort audit unless public adult-stratified or measurement-validation documentation appears. Next inspect the original multicenter YGTSS revision/validation study cited by this paper (McGuire et al., 2018): does its age and comorbidity coverage validate separate impairment interpretation across ASD/communication groups, or only general tic-scale performance? Extract actual subgroup coverage, informant/reliability design and null results before extending measurement claims. This is a bounded primary-methods question, not a request for participant data or a new clinical assessment.

## Reproduction

Run `python extract_source.py` for a fresh live primary-source check, then `python analyze.py` and `python check_analysis.py` from this directory. Live source bytes may change; saved aggregate inputs permit offline calculation. Independent review and its scope are stored under `review/` after completion.
