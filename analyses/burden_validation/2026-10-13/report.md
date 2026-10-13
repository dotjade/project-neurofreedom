# Adult burden endpoints: retain direct patient report; do not install a universal severe cutoff

Project NeuroFreedom | 13 October 2026 | Bounded six-report validation and longitudinal test

## Decision

Use a **version- and language-specific GTS-QOL patient report as the principal candidate disease-specific burden measure**, with its native domain profile preserved. Keep clinician-rated YGTSS total tic severity, its motor/phonic components, and impairment separate. Do not replace direct burden measurement with a tic score, label a tic-response cutoff a severe-state definition, or interpret a global YGTSS score containing impairment as independent burden validation.

This closes the current endpoint-substitution/universal-threshold question at the evidence available in this bounded pass. It does not claim no suitable evidence could exist elsewhere. The six reports support separate constructs and repeated measurement, but do not supply an externally validated adult, diagnosis-specific severe-persistence rule, an adult anchor-based GTS-QOL meaningful-change threshold, or treatment-effect surrogacy. Missing validation is not proof of zero association.

The [prediction and disconfirming results](prespecified_question.md) were recorded before retrieving the new primary sources. Positive but incomplete adult cross-sectional association was observed. The predicted absence of sufficient substitution/threshold validation was sustained within this set. A stronger claim that longitudinal tic and QoL changes are unrelated remains untested: paired change covariance/correlations are not supplied.

## What the six primary reports contribute

Numerical detail, source locations, populations and access limits are in [extraction.json](extraction.json).

1. **Original development:** patient-derived items and separate development/evaluation samples support the disease-specific instrument. Reliability is reported as high. The abstract’s 0.5–0.7 correlations are between subscales, not evidence of YGTSS–QoL concordance. Full original methods were inaccessible in the inspected lawful routes; exact age eligibility and retest details remain unverified. [Cavanna 2008](https://pubmed.ncbi.nlm.nih.gov/18955683/).
2. **French adaptation:** the original four-domain arrangement was not reproduced. Six domains and altered item groupings were obtained in a sample including ages 16–17. Stable-status retest estimates do not validate detection of improvement. Uncertainty is substantial: for example, social-domain ICC was 0.71, 95% CI 0.47–0.86. YGTSS was not the convergence instrument. [Jalenques 2020, Tables 6–7](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0243912).
3. **Severity classification:** mixed-age YGTSS benchmarks show fair categorical agreement, rather than interchangeable classification. The printed marked/severe boundary overlaps at 43. No single-modality exclusion is reported, but there is no diagnosis-specific calibration. Inclusion of some motor-only/vocal-only diagnoses does not validate their classification. [McGuire primary manuscript](https://escholarship.org/content/qt8f61z3r0/qt8f61z3r0.pdf).
4. **Meaningful tic response:** a 25% TTS reduction is supported against a clinician improvement anchor in pooled behavioral-trial participants. That is a change criterion, not an adult severe-state cutoff or a GTS-QOL responder definition. Even the trial commonly called “adult” included ages 16–17. [Jeon 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3999642/).
5. **Longitudinal counterweight:** an adult, self-selected aripiprazole cohort had a significant tic-score change and nonsignificant QoL change. This prevents assuming demonstrated QoL benefit from the tic result, but **does not establish that the effects differ**, QoL equivalence, or a causal drug effect. Follow-up cross-sectional correlations are not change correlations. [Gerasch 2016, Tables 2–3](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2016.00416/full).
6. **Longitudinal positive evidence:** a small adult TICNET cohort reported improvement in both measures over follow-up and included motor-only cases. It remains uncontrolled and unmasked, excludes urgent dangerous tics, and cannot establish within-person concordance from parallel group trajectories. Published standardized-effect intervals are wide; retain them rather than treating significance in a different model as a precision substitute. [Ivanova 2026, Table 3](https://link.springer.com/content/pdf/10.1186/s44247-026-00284-7.pdf).

The McGuire and Jeon analyses share parent CBIT trial families; their exact person overlap is unavailable. They are not independent replications. The positive and negative longitudinal studies were retained deliberately, rather than selecting only co-improving examples. None is untreated adult natural history.

## Keep six different measurement claims separate

- **Cross-sectional correlation:** between-person association at an assessment. It can be useful even when scores disagree for individuals; it does not estimate within-person change.
- **Test–retest reliability:** reproducibility among sufficiently stable respondents. Excluding people who changed is sensible for that aim, but cannot test responsiveness in those excluded people.
- **Responsiveness:** ability to detect relevant change over time. A change in a treatment cohort is suggestive, but its magnitude depends on true change, sampling, measurement error, expectations and treatment context.
- **Meaningful change:** needs an appropriate patient/clinical anchor and interpretation in the target population. Statistical significance, an effect size or reliable-change index alone is not a patient-important threshold. A tic-scale threshold cannot simply be transferred to QoL.
- **Treatment-effect surrogacy:** requires evidence that treatment effects on one endpoint predict the effects on the patient-relevant outcome across relevant interventions/settings. Neither correlation nor two declining group means is sufficient.
- **Severity classification:** a present-state distinction. Neither response nor trial inclusion criteria establish “severe”; repeating a weak classifier does not validate persistent-severe status.

These are methodological distinctions used to interpret the source results, not six claims that this project has newly validated.

## Executed aggregate test: how often do response labels disagree?

A justified small computation was possible for Jeon’s published aggregate overlaps, without patient records. With CGI-I response as the reference and ≥25% TTS reduction as the index, the table is TP=63, FP=25, FN=9 and TN=135. The [script](aggregate_checks.py), [inputs](aggregate_inputs.json), and [actual results](aggregate_checks.json) reconstruct:

- Agreement: 198/232 = **85.34%**; discordance: 34/232 = **14.66%** (pointwise Wilson 95% CI 10.68–19.78%)
- Sensitivity: **87.50%** (77.92–93.28%); specificity: **84.38%** (77.95–89.19%)
- Among tic-threshold responders, **71.59%** (61.42–79.96%) also met CGI-I response
- Cohen’s κ = **0.67736**, consistent with the printed 0.68; the paper’s integer sensitivity is 87%, while exact overlaps yield 87.5%

Thus the classifications show substantial agreement but are not identical even against a clinician anchor. These are mixed-age, in-sample response metrics, **not adult QoL-surrogate performance**. The intervals are conditional on the selected threshold, use binomial Wilson calculations, and do not account for threshold-selection optimism or site/trial clustering. Armwise predictive values in the output condition on postrandomization response and must not be interpreted as randomized treatment-effect contrasts.

Twenty-six checks pass. The initial verification exposed a mistaken hand-entered kappa expectation and floating-point endpoint equality; both were corrected before the successful run. No unreported covariance, adult subgroup table or QoL responder count was manufactured. McGuire’s category margins cannot identify exact severe sensitivity, so no full contingency table was reconstructed.

## Practical endpoint specification and stopping rule

For the future registry design, the defensible specification is:

1. Analyze continuous patient-reported GTS-QOL and its **actual language/version’s native domains** over the verified visits. Validation is strongest for TS; use in motor-only/vocal-only disorders still needs explicit applicability review. Inclusion in a mixed-diagnosis treatment study is not diagnosis-specific instrument validation. A total may be reported only with a verified scoring algorithm and prespecified interpretation; do not average French six-domain and English four-domain scores as though they were identical. Cross-language comparison/pooling requires measurement-equivalence evidence or an explicit sensitivity strategy.
2. Analyze YGTSS-TTS, motor, phonic and impairment in parallel. A total-score cutoff above the single-modality maximum cannot define severe motor-only/vocal-only disease. Do not solve that problem by arbitrarily doubling a modality score or borrowing an enrollment threshold.
3. Keep adults with high burden and little tic variability in the study. Record diagnosis and currently active tic modalities separately. Use diagnosis-stratified descriptive distributions until a defensible state-classification rule exists.
4. Preserve the four-week GTS-QOL versus past-week YGTSS recall distinction. Six-monthly visits do not establish uninterrupted interval severity. Patient-relevant pain, participation/work, sleep and treatment harms need separately verified endpoints if they are scientific targets; a QoL total alone does not identify those domains.
5. Do not label patients QoL responders using an invented MCID. To test change concordance, require paired same-person scores, visit/recall alignment, outcome-specific missingness, and an appropriate change model. A formal comparison of endpoint effects needs their joint covariance, not comparison of two p values.

**Close this measurement pass now.** Reopen universal classification or surrogacy only for a materially new validation source or an authorized study with the necessary measurements. No participant analysis or access request is justified merely because public aggregates exist.

The next concrete research task should move to **one adult randomized treatment study**, rather than another measurement audit: [Haas et al., ONLINE-TICS](https://www.mdpi.com/2077-0383/11/1/250), which has accessible tic, impairment and GTS-QOL contrasts. Test the time-specific treatment-benefit claim using its primary endpoint and patient-relevant outcomes, preserve multiplicity/attrition and null findings, and stop if published joint quantities cannot support a discordance calculation. This is a verified source lead, not a seventh study analyzed here or a treatment recommendation.

## Provenance and limitations

Read the current README, protocol, status and 12 October adult endpoint report/extraction before beginning. Searches/access attempts and screened leads are logged in [provenance.json](provenance.json). Retrieval ran on 13 October 2026. This targeted selection is not a systematic review, a meta-analysis, a comprehensive MCID search or independent clinical validation. Direct PMC opens often returned browser checks; publisher HTML/PDF and indexed primary text supplied alternatives. Ivanova PDF screenshots failed, so visual-page verification is not claimed. No correction/retraction was identified in inspected source pages and limited identifier searches; this is not comprehensive clearance. Funding/conflict extraction is incomplete for the older scale/benchmark sources and is explicitly marked.

Only original summaries, aggregate facts and reproducible code are saved. No source full text, participant records, family information, outreach, intervention or paid resources were used.
