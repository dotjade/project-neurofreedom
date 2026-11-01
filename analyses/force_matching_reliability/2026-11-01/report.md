# Force-matching stability is not repeat-session reliability

1 November 2026. Historical peer-reviewed aggregate-methods audit and **executed arithmetic of published group means**, not a simulation, participant reanalysis, new treatment finding or Tourette biomarker validation.

## Question, prediction and decision

Does published evidence establish that the indirect baseline stays interpretable as familiarity changes, and that the attenuation measure is reliable between sessions? The prediction was that clinical between-person interpretation needs both an understood baseline and reproducible measurements, not just a convincing average laboratory effect.

**Result:** the retrieved methodological study supports small changes in mean error when fewer within-session repetitions are used, but it does not establish retest reliability or a condition-specific absence of learning. A previously uncomputed comparison of its published aggregates shows that changing the extraction window from 2–2.5 to 2.5–3 seconds reduces the equal-force direct-minus-slider contrast by **0.12 N, about 13.45%**. This is a descriptive device-specific sensitivity, not a new significance test. It reconciles apparently stable direct measurements with a changing indirect baseline.

Close this aggregate audit. The required same-task repeat-session coefficient and its uncertainty were not verified in the bounded search. Do not replace them with split-half coefficients, other force-sense tasks, or the inaccessible adult TS paper. Stop this branch pending lawful participant-free aggregate methods/results; do not obtain participant rows or contact researchers. Broader clinical prioritization should return to the existing portfolio rather than generate another synthetic force-matching demonstration.

## Sources and methods

The main primary source is McNaughton et al., [Methodological considerations for the force-matching task](https://doi.org/10.3758/s13428-022-01954-w), [PMID 36002628](https://pubmed.ncbi.nlm.nih.gov/36002628/), [PMCID PMC10556179](https://pmc.ncbi.nlm.nih.gov/articles/PMC10556179/). Online publication was **24 August 2022**, with 2023 volume/issue publication. This is historical evidence newly audited, not a new-window discovery. Lawful CC BY 4.0 manuscript XML was inspected through [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10556179/fullTextXML). Only original summaries and selected aggregate numerical inputs are saved here; no full paper or participant dataset is published.

We inspected sample, design, Tables 2–5, split-half results and learning analysis, distinguishing three time scales: milliseconds within a trial, sequential trials within a session, and sessions separated by days. Searches and exclusions are in [source-log.json](source-log.json). The adjacent retest source was Li and Li, [DOI 10.1038/s41598-024-51644-0](https://doi.org/10.1038/s41598-024-51644-0), PMID 38212469, published January 11, 2024. It was inspected to test endpoint comparability, not pooled as attenuation validation. No dataset linked by either article was opened.

### Population, order and calibration

The main study has **138 right-handed participants**, mean age **24.51 years (SD 8.71)** and 95 women. It is one experimental session, not a TS cohort or a developmental comparison. Four target forces (1, 1.5, 2 and 2.5 N) occur eight times in each condition, giving 64 trials. Target order is randomized; direct and slider conditions occupy separate 32-trial blocks with condition order counterbalanced. A one-minute pause follows every 16 trials. The right finger receives the force and the left finger either presses the lever or moves the potentiometer.

The authors attribute possible slider timing lag to the device mapping, including a fourth-degree polynomial linearization. That is a proposed apparatus explanation, not independently established biology. The linked 2021 device publication ([PMID 34027595](https://pubmed.ncbi.nlm.nih.gov/34027595/), DOI 10.3758/s13428-021-01605-6, online May 23, 2021) was checked for bibliographic context, not independently replicated or treated as new calibration data. The main paper warns that numerical error estimates are device-specific and contains a smaller previously reported sample; those reports are not independent replication.

## Which reliability was actually measured?

The main paper reports Spearman–Brown-corrected **split-half** reliability for each condition's mean error, separately. No confidence intervals for these coefficients were found in the inspected manuscript.

| Repetitions per force/condition | Direct | Slider |
| --- | ---: | ---: |
| 2 | 0.88 | 0.74 |
| 4 | 0.91 | 0.81 |
| 6 | 0.92 | 0.84 |
| 8 | 0.94 | 0.86 |

Reducing repetitions preserves roughly similar group means while the coefficients fall, especially for the slider. Our equally weighted reconstruction from rounded Table 2 means is 0.755 N for two repetitions versus 0.7625 N for eight. A nonsignificant difference in means is not proof of equivalent measurement precision. Further, the first two, four and six repetitions are nested subsets of the same eight, not independent sessions.

Neither condition coefficient is the reliability of the **direct-minus-slider difference**, a condition ratio, or the latent factor in the October 31 model. Difference-score reliability depends on component/error covariance. No separate-day session was included, so these values do not estimate retest agreement, temporal stability, standard error of a change score, or clinically meaningful change.

The Li and Li study instead tests **contralateral pinch-force proprioception** in 30 healthy young adults (mean age 20.4, SD 2.7), twice one week apart. It reports two-way mixed-effects, absolute-agreement, single-measurement ICCs. Its normalized constant-error ICCs are reported as 0.76–0.85 and variable-error ICCs as −0.25 to 0.05. These concern active bilateral pinch matching at percentages of maximum force, not the direct versus slider self-touch contrast. Different normalization, target construction and response processes preclude pooling or using these as attenuation retest coefficients. Published table dispersion entries also warrant caution. If the session and difference dispersions are SDs for the same paired sample, as the methods indicate, some fail the necessary paired-SD bound. For example, NAE at 10% has session SDs 0.69 and 0.21, requiring a difference SD between 0.48 and 0.90, but the table prints 0.22. This is an unresolved reporting ambiguity, not a diagnosis of the underlying data or a corrected estimate. We do not reconstruct or validate its ICCs. The useful finding is the construct mismatch and metric dependence, not a transferable numerical reliability value.

## Within-session learning: preserve the null, narrow the claim

The main paper finds little overall trend: the average individual slope over 64 trials is **0.0004 N/trial (SD 0.02)**. The authors report 95% of individual slopes between −0.05 and 0.05 and negligible correlations with the measured psychological scores. These results count against a large common monotonic change over the particular session; they should not be discarded to favor a learning story.

However, the reported slope combines both counterbalanced condition blocks. A near-zero average of whole-session slopes does not identify the slope within the slider condition or isolate a condition-by-trial interaction. Order-related shifts can cancel across counterbalanced sequences, and nonlinear early familiarization may evade a global straight line. This is a limitation of the available estimand, **not evidence that concealed learning occurred**. The authors compare per-trial slopes with a force-error magnitude; without an explicit time span, those quantities have different units. We therefore do not adopt the stated 10% comparison as an equivalence margin. There was no prespecified equivalence test establishing negligible learning at the relevant condition level.

## Executed aggregate sensitivity analysis

Run `python audit_aggregates.py`. [Inputs](aggregate-inputs.json) transcribe only group means from Tables 2 and 4 and reported split-half coefficients. [Outputs](aggregate-results.json) record calculations and **23 passing assertions**. Python standard library only; deterministic arithmetic, no random seed or paid compute.

For every force, subtract slider mean error from direct mean error, then average equally across the four equally represented force levels. Since both errors subtract the same physical target, this difference also equals direct minus slider matched force. This is not a fitted attenuation parameter or an average individual ratio.

| Window after go | Mean direct error, N | Mean slider error, N | Direct minus slider, N |
| --- | ---: | ---: | ---: |
| 2.0–2.5 s | 0.4875 | −0.4050 | 0.8925 |
| 2.5–3.0 s | 0.4625 | −0.3100 | 0.7725 |

The contrast change is **−0.1200 N (−13.45% relative to the earlier window)**, decomposed into −0.025 N direct change minus +0.095 N slider change. The per-force contrast changes are −0.06, −0.12, −0.15 and −0.15 N. Thus the direct plateau does not imply the contrast is invariant to extraction timing. Table 5 reports no significant direct comparison between these last windows, but slider comparisons are significant at each target (p=.003 or <.001). We do not treat those separate p values as a formal interaction test.

Published inputs are rounded to 0.01 N. If each is conventionally rounded within 0.005 N, worst-case numerical uncertainty in the difference of contrasts is 0.02 N, not a sampling confidence interval. The direction survives that rounding bound. A sampling CI or formal paired contrast requires cross-condition and cross-window covariance (or a directly reported contrast with precision); these are not supplied. No patient data are needed or requested: a lawful participant-free statistical summary would suffice.

The main narrative gives overall direct error 0.47 N, slider error −0.27 N and their difference 0.76 N. The first two rounded values subtract to 0.74 N, not 0.76. Table 2 eight-repetition means instead imply 0.7625 N; Table 4 final-window means imply 0.7725 N. We preserve these distinct reported summaries and do not silently reconcile them. The focused window contrast uses Table 4 consistently and does not rely on the discrepant narrative total. The earliest direct 1.5-N Table 4 entry also does not track the simple monotonic prose; it is retained as printed but is outside the focused last-two-window comparison.

## Uncertainty, scope and exact prerequisite

This single-device historical study tests largely young adults. It does not establish indirect baseline adaptation after prolonged practice, stability across days, or transport to children, older adults, severe persistent adult tics, pain, comorbidity or treatment response. Stable measurement would still not prove mechanism, prospective prediction or functional benefit. No causal claim about a patient's biology follows.

The bounded search did not verify a same-paradigm repeat-session direct/slider attenuation reliability coefficient with uncertainty. This is **not proof that no such study exists**. Exact prerequisites are a lawful aggregate report of repeat-session design and interval, population/age, apparatus/calibration, order and familiarization, exact endpoint, ICC model or other coefficient with CI, and absolute agreement/change-error estimates. Condition-specific trial trends with uncertainty are separately needed to test the indirect-learning prediction. The adult TS contrast retains its previous participant-free methods/results prerequisite. Do not re-open mixed datasets, collect data, contact researchers or recommend an intervention.
