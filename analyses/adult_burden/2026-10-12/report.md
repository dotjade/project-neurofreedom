# Adult registry endpoints: severity is not an established burden surrogate

Project NeuroFreedom | 12 October 2026 | Bounded public-evidence extraction

## Actual result and decision

**Do not substitute tic severity for functional burden or quality of life, and do not start a participant-level persistent-severe-adult analysis from these publications alone.** The two reports document relevant adult measurements, but neither reports the person-level severity–burden relationship, a longitudinal joint outcome, or an applicable severe-persistence definition. This is an identification and validation gap, not a finding that severity and burden are unrelated.

The Calgary design supports a narrower future question: **repeated adult severity and independently reported burden at registration, six months and twelve months during clinical care**. It does not establish uninterrupted severity over the intervening months. Paris follow-up availability cannot be inferred from Calgary's counts. No pooled effect, participant reanalysis, treatment recommendation or cure inference is warranted.

The operational prediction and disconfirming results were recorded before opening the primary leads in [prespecified_question.md](prespecified_question.md). The prediction that published aggregates would not identify a severe-at-every-visit stratum was supported. The substantive prediction that severity explains some, but not all, burden remains **untested in these registry reports**. Lack of a published analysis does not confirm the predicted association or formally invalidate a surrogate.

## What the two reports actually establish

### Calgary treatment-description report

Pringsheim and Martino, first published 7 December 2024, analyzed 95 adults enrolled January 2021–April 2024: 81 Tourette syndrome (TS), 13 persistent motor and one persistent vocal tic disorder; ages 18–73. Registration/six/twelve-month collection includes YGTSS tic inventory, severity and impairment, GTS quality of life, psychiatric conditions and treatment. The instrument version, psychiatric severity scales and GTS-QOL implementation details are unspecified. Follow-up assessments were completed by 63 and 55 adults at analysis; the eligible-at-each-visit denominator, joint completion and item-level missingness are not reported. [Methods and Results](https://movementdisorders.onlinelibrary.wiley.com/doi/10.1002/mdc3.14296).

Baseline YGTSS total tic severity was 21.3 (95% CI 19.7–22.8); impairment 21.2 (19.0–23.3). Thirty-two participants received botulinum toxin sometime during enrollment; eleven also used oral medication. Table 1's never-minus-ever-treated differences were 3.9 severity points (0.7–7.1) and 1.3 impairment points (−3.3–5.9). These are different endpoints, not a severity–impairment correlation. GTS-QOL results and longitudinal severity/burden changes are absent. Systematic adverse-effect collection was absent. [Table 1 and treatment description](https://movementdisorders.onlinelibrary.wiley.com/doi/10.1002/mdc3.14296).

### Expanded Calgary/Paris phenomenology report

Nilles and colleagues, 23 July 2025, analyzed first assessments in 227 adults with childhood-onset primary tics: 210 TS, 16 persistent motor, one persistent vocal disorder. Recruitment began in 2021 during clinical care; the cutoff date and age range are not specified. Mean age was 31.2 years. Functional/mixed functional, provisional, secondary and adult-onset presentations were excluded. The YGTSS revised version assesses the previous week. Total tic severity was 20.4 and impairment 21.3. No severe threshold, repeated endpoint results, QoL scores or severity–QoL model is reported. [Methods, Results and Tables 1–2](https://onlinelibrary.wiley.com/doi/pdf/10.1111/ene.70252).

Comorbidity denominators are 218 overall, 78 women and 140 men, versus 227/82/145 for the sample. The antipsychotic row prints 95 overall but 33 women and 66 men; these sum to 99. This unresolved discrepancy appears in indexed PMC text and publisher PDF text. Nationality counts (108 Canadian, 119 French) must not silently become verified site-specific follow-up counts. [Table 1, PDF page 3](https://onlinelibrary.wiley.com/doi/pdf/10.1111/ene.70252).

The reports belong to the same registry family. Overlap of the earlier Calgary participants with the expanded sample is plausible but not enumerated. Treat the reports as potentially overlapping; neither sum 95+227 into an independent sample nor subtract them to infer newly recruited participants.

## Instrument crosswalk and construct limits

The [structured extraction](extraction.json) distinguishes a named collection instrument, its published scale definition and verified use at a particular registry/site/visit.

- **YGTSS total tic severity:** separate motor and phonic scores, each 0–25, summed to 0–50. Number, frequency, intensity, complexity and interference contribute. The revised registry report explicitly uses a past-week inventory. This is clinician-rated retrospective assessment, not a dense independent video record.
- **YGTSS impairment:** distinct 0–50 score, in ten-point steps, covering tic-related impacts on social/family life, schoolwork and self-esteem. It is neither a complete general-function measure nor a fully independent reporter/method when obtained within the same clinical assessment.
- **YGTSS global severity:** total tic score plus impairment, 0–100. Correlating this composite with impairment contains a built-in shared component. It cannot validate tic severity alone as a burden proxy. [Primary scale/benchmark methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC7867408/).
- **GTS-QOL:** the original adult patient-reported instrument has 27 items and psychological, physical, obsessional and cognitive subscales. Its validation supports measuring a broader construct than motor/vocal severity. [Original development study](https://pubmed.ncbi.nlm.nih.gov/18955683/). Published scale descriptions specify a four-week recall, 0–4 item ratings and normalized 0–100 subscale scores, higher indicating worse QoL. [French adaptation study](https://pmc.ncbi.nlm.nih.gov/articles/PMC7755204/). Those standard definitions do not establish which version, language, scoring algorithm, missing-item rule or domains were actually used at either registry site.
- **Psychiatric burden:** the expanded report verifies DSM-5 diagnoses through clinical examination or psychiatric consultation. Diagnosis presence is not symptom severity. Specific repeated symptom instruments and their recall windows remain unverified.
- **Pain, employment/participation, fatigue/sleep and treatment burden:** no separate repeated endpoint definitions are established here. Do not infer their absence from the underlying registry, or assume a total QoL score identifies each domain.

The past-week YGTSS and standard four-week GTS-QOL windows differ. A nominal six-month visit is an assessment time, not evidence that a scale integrates the preceding six months.

## Evidence, counterevidence and what remains untested

The decision to retain separate endpoints has both conceptual and empirical safeguards:

1. A clinician can assess substantial tic-specific severity while a patient reports burdens arising from several domains. Distinct instruments are available; dropping the direct burden measurement would discard information before interchangeability has been demonstrated.
2. Calgary's treatment-group severity and impairment contrasts are not identical. However, one interval excluding zero and the other including zero does **not** demonstrate that their effects differ. The comparison is nonrandomized; the ever-treated group was older, treatment may predate registration, and classification uses treatment sometime during enrollment. It is neither a causal treatment effect nor an appropriate prospective baseline predictor without time-order verification. Never receiving botulinum toxin does not mean untreated.
3. The expanded report's nonsignificant sex comparisons do not establish equivalence, predictive accuracy or within-person concordance. Its introductory claim about psychiatric effects on QoL cites other research; it is not an adjusted finding from these 227 adults.
4. Counterweight: tic severity includes interference, and external scale research shows severity/impairment relate to clinician-rated illness. Thus a useful relationship is plausible. Yet the primary benchmark study found only fair categorical agreement with clinician severity and used a mixed-age sample, not a validation of adult registry QoL substitution. [Benchmark study](https://pmc.ncbi.nlm.nih.gov/articles/PMC7867408/).

Neither registry report supplies severity–QoL correlations, adjusted coefficients, longitudinal change correlations, classification sensitivity/specificity for high burden, or individual discordance tables. No comparable aggregate association effect is available to combine. Marginal means and confidence intervals cannot recover these missing relationships.

## Severe persistence: a precise candidate, not an identified result

An appropriate **candidate descriptive estimand**, conditional on resolving thresholds and data availability, is:

> Among baseline adults with childhood-onset primary tic disorder who meet a diagnosis-appropriate severity threshold at registration, what proportion also meets that threshold at the six- and twelve-month assessments during observed clinical care, and what are their separately measured impairment and QoL distributions at each visit?

Its mathematical structure is P(T6 ≥ τd and T12 ≥ τd | T0 ≥ τd, baseline age ≥18, diagnosis d), accompanied by the separate joint distributions of impairment and QoL. This is persistence **at three observed visits**. It is not uninterrupted twelve-month severity, lifelong adult persistence, untreated natural history or a causal treatment effect. A fully operational severe estimand is not yet specified because τd and visit windows require justification.

A single borrowed TS total-score cutoff is unsafe across diagnoses: motor-only or phonic-only tic severity can occupy only one 0–25 component. A total-score cutoff above 25 would structurally exclude every such person, regardless of disability. Their burden must remain visible.

The external benchmark paper does not solve this automatically. Its Table 3 prints overlapping marked/severe total-score categories at 43, has few model-classified severe cases, and reports fair classification agreement. It is inappropriate to install that boundary as a universal severe-adult registry rule without further validation. A category label must not replace the patient's functional experience. [Table 3 and limitations](https://pmc.ncbi.nlm.nih.gov/articles/PMC7867408/).

Maintain a parallel all-adult analysis of continuous severity, impairment and QoL. It must retain people with sustained severe burden, minimal within-person variability, or substantial functional limitation despite lower total tic scores; eligibility must never depend on having a quiet-to-peak transition.

## Executed aggregate checks

The small [audit script](aggregate_checks.py) and [actual output](aggregate_checks.json) use only published counts:

- 63/95 = 66.32% and 55/95 = 57.89% had completed the respective follow-ups at analysis. These are completion fractions against enrollment, **not established retention rates among everyone due for follow-up**.
- If both completion groups are subsets of the same 95 adults, between 23 and 55 adults completed both follow-ups. The exact intersection is unavailable. These set bounds do not establish complete YGTSS/GTS-QOL records.
- 227−218 = 9 adults lack a comorbidity-table denominator contribution; 33+66−95 = 4 exposes the antipsychotic-row inconsistency. Neither arithmetic result identifies the underlying cause or the correct replacement count.

The script includes checks of partition counts, exact rational bounds, all feasible visit-overlap counts and boundary cases. No unreported covariance, response rate, severe count or pooled effect was manufactured.

## Next narrow decision and prerequisites

**Go:** retain a multidomain endpoint specification and the candidate observed-visit estimand as a research-design artifact. The endpoint verification requested by the current plan is complete with explicit limitations.

**No-go:** participant modeling, causal comparisons, a numeric severe-persistence estimate, or a severity-only burden endpoint. Do not repeat the closed generic cohort search. Reopen registry feasibility only when a public protocol/data dictionary/new report or a separately authorized custodian response supplies the missing fields.

The next feasible public-evidence task is narrowly defined: examine adult GTS-QOL/YGTSS validation and longitudinal concordance evidence to choose a patient-relevant burden endpoint and assess defensible diagnosis-specific severity definitions. It should stop with an explicit no-go if published validation cannot support a threshold or substitution; it is not another search for a convenient cohort.

Before any participant analysis, require:

1. A current site-specific protocol/data dictionary proving exact instruments, language/version, item scoring, recall periods, assessment/rater procedures and available visits. Verify Paris's schedule independently.
2. Linkable adults, age/onset/diagnostic definitions, recruitment and cutoff dates, exact visit dates/tolerances, a full eligibility/attendance flow and outcome-specific missingness. Establish the earlier/expanded report overlap.
3. An agreed, justified severity definition appropriate to TS and single-modality disorders, distinct burden definitions and adequate numbers in each stratum. Avoid thresholds chosen after inspecting outcomes.
4. Treatment histories with start/stop dates, dose, adherence, therapy/device exposure and relevant injection timing; distinguish baseline, newly initiated and ongoing treatments. Resolve the printed medication discrepancy before using aggregate treatment counts.
5. Repeated psychiatric symptom measures and confounder timing; baseline and follow-up impairment/QoL item/domain availability; specific pain/participation endpoints if those are the target.
6. A prespecified descriptive target population and missing-data plan separating not-yet-due assessments, refusals, losses, death and item nonresponse. Use sensitivity analyses; do not label complete-case results the baseline cohort's trajectory.
7. Appropriate institutional/ethics review, consent-compatible secondary use, lawful custodian permission/data-use agreement and a secure approved environment. Both reports offer restricted author-request data, not public participant records or this project's access approval.

No custodian was contacted, no participant file was obtained, and no clinical action was undertaken.

## Provenance and limitations

This is a targeted two-report endpoint audit, not a systematic review or independent clinical peer review. Supporting scale sources clarify constructs and threshold uncertainty, not extra registry replications. Public source retrieval ran on 12 October 2026; methods/tables were read in publisher HTML/PDF text and indexed primary-source text. Direct PMC opens for the two leads returned browser checks; alternate official publisher routes supplied the substantive reports. Publisher-PDF screenshots failed with cache errors; no visual-page verification is claimed. Supplement captions concern tic phenomenology, and the separate DOCX was not retrieved; no negative assertion about uninspected supplement contents is made. No correction/retraction notice was identified in inspected views and exact-title checks, but comprehensive clearance was not performed.

Searches/access attempts and repository blob versions are retained in [provenance.json](provenance.json). Only original summaries, structured facts and reproducible arithmetic are included. No source full text or participant information is redistributed.
