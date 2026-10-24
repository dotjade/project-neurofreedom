# Adult tic-risk claims: denominators and timing audit

24 October 2026 | Published aggregate analysis, not a simulation or patient model

## Actual result and decision

**Kaylor et al. supports retrospective associations in selected adult respondents, not an established prospective individual-risk model.** The audit verifies recruitment and completeness stages, exposes why 258 cannot automatically be used as every model denominator, and distinguishes recalled childhood severity from lifetime comorbidity and current medication. The two final model counts and their explicit missing-data rules were not located. No participant reconstruction, model fitting, treatment-effect estimate or individual prognosis was attempted.

Source: [Kaylor et al., primary paper](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2026.1948693/full), DOI 10.3389/fpsyt.2026.1948693, PMID 42903303, published October 6, 2026. This advances yesterday's extraction with a focused documentation audit and reproducible aggregate arithmetic. It is not a newly published study today.

## Prediction, method and actual calculation

The [pre-calculation prediction](prediction.md) expected complete recruitment counts but insufficient model-denominator and exposure-order information. Publisher methods/tables/discussion and official PMC XML were inspected. [Source provenance](source-provenance.json) records actual retrieval and response hash; no full paper, participant plots or personal-event narrative is stored. [Inputs](inputs.json), [code](analyze.py), [outputs](results.json) and [temporal audit](temporal-audit.json) separate printed facts from conditional arithmetic.

The paper reports 758 invited, 334 responding, 292 with complete childhood/adult tic items, and 258 retained after consistency/exclusion rules. Arithmetic gives response 44.06%, completeness among respondents 87.43%, retention after that gate 88.36%, and final sample/invited 34.04%. Differences are 424 nonrespondents, 42 respondents outside the completeness gate and 34 subsequent exclusions. They are distinct stages, not a clinical deterioration rate.

Table 1 explicitly excludes missing/unknown values. Its counts and one-decimal percentages are compatible with different denominators. Under the stated nearest-0.1-point rounding assumption, enumerating integer denominators no greater than 258 yields:

| Field | Printed count / percent | Rounding-compatible denominator | Conditional missing/unknown relative to 258 |
|---|---:|---:|---:|
| OCD | 124 / 59.6% | 208 | 50 |
| ADHD | 67 / 26.6% | 252 | 6 |
| Family history | 155 / 66.8% | 232 | 26 |
| Male / White | 144 / 56.0%; 240 / 93.4% | 257 each | 1 each |
| Non-Hispanic | 252 / 98.4% | 256 | 2 |
| Current medication / life event | 72 / 27.9%; 153 / 59.3% | 258 each | 0 each |

These are **conditional rounding-compatible totals, not author-confirmed denominators or regression sample sizes**. They depend on correctly printed counts/percentages and the rounding assumption. Joint overlap, outcome completeness and any imputation are unknown. The study's 50 reused current-as-adult-worst scores happen to equal the conditional OCD missing count; there is no basis for identifying them as the same people. Model n was deliberately left null, not reverse-engineered from rounded t, p or R-squared statistics.

The 247/258 current-tic fraction (95.74%) describes selected retained respondents, not population persistence. The 50/258 reused-score fraction is 19.38%, not independent longitudinal validation. No random seed applies to this deterministic calculation.

## Timing and counterevidence

- Childhood-worst and adult-worst periods have age-based ordering, but both are recalled at one survey. That does not reproduce a prospectively observed childhood baseline.
- Methods assign lifetime OCD; discussion calls it childhood OCD. Onset before the adult-worst outcome is not established for the modeled variable.
- Medication is current at survey, whereas the outcome is recalled adult-worst impairment. Treatment seeking/confounding and reverse temporal ordering remain plausible. The positive coefficient is not evidence medication causes harm or should be stopped.
- Life events are recalled as contemporaneous with the worst period, not demonstrated antecedent triggers. No personal narratives were copied.
- Counterweight: the childhood-score association persists in both reported multivariable models, and the paper directly documents adults with continuing symptoms. These findings deserve retention rather than dismissal. They do not remove selection, recall, adapted self-report or temporal limitations.

The total-tic and impairment models use different selected predictor sets. Their reported R-squared values (0.32 and 0.28) are not verified held-out performance. ADHD and life-event terms in the total-tic model are nonsignificant (p=.82 and .098); positive life-event valence is nonsignificant in both separately modeled outcomes. The impairment OCD p value is printed .050 despite bolding/significance wording. It is preserved as printed; rounding cannot resolve the unrounded threshold. Nonsignificance does not prove no association.

## Uncertainty, limits and next decision

This is a targeted methods audit, not clinical peer review or a systematic review. No public model-specific n, explicit missing-data rule or prospective external validation was located in inspected main-text methods/tables. This does not prove none exists elsewhere. PMC XML has no supplementary-material element; author-mediated access is subject to Mass General Brigham IRB policies, not unrestricted public participant data or authorization to obtain them. Demographic concentration and original diagnostic exclusions limit applicability, including to ASD/intellectual disability and the broader chronic-tic population. Worst-ever and current symptom outcomes must not be conflated with enduring severe functional burden.

**Close this fixed audit unless new public documentation supplies model-specific counts, missingness handling and exposure timing.** No risk score, pooled effect or patient-data analysis follows. Next examine the newly indexed Aldurayhim ASD/tic study's age structure and adjusted-versus-unadjusted impairment evidence: can its mixed-age estimates support an adult-specific burden conclusion, and is a measurement explanation tested or only proposed? Audit published aggregate age/comorbidity/model coverage, preserve the null severity result and stop at absent adult-stratified data. Do not repeat the earlier adult registry surrogate audit, reconstruct participants or infer less lived burden from a lower measured score.
