# Project NeuroFreedom weekly synthesis | 22 November 2026

**Decision:** Keep patient-reported function, proxy-reported function, tic severity, sleep, and medically recorded harm separate. The week's work narrowed what each can tell us. No treatment change, clinical threshold, or causal inference follows.

Scope: the seven completed daily reports from 16–22 November, with an additional aggregate-data audit below. Standing authorization for public, non-identifying science is recorded in the [13 October scope clarification](../RESEARCH_PROTOCOL.md#public-publication-scope---13-october-2026); no project visibility or homepage feed change was made for this synthesis.

## What changed this week

- **Participation:** the [16 November measurement audit](2026-11-16/report.md) found no basis in its three sources for pooling pain, sleep, or participation across age and severity. [Schug et al., PMID 43061991](https://pubmed.ncbi.nlm.nih.gov/43061991/), published online 20 November, adds pediatric clinician input: 19 occupational therapists rated relevance and 18 contributed focus-group accounts. The [21 November audit](2026-11-21/report.md) kept original COSA psychometrics indirect. Clinician relevance, child-perceived competence, and measured change in participation are different constructs. There is no verified COSA-t responsiveness or direct adult applicability in that report.
- **Sleep:** in the [17 November comparison](2026-11-17/report.md), the reported associations between impairment and sleep stayed positive across selected full and reduced models, but nominal significance depended on the model. This is compatible with a relationship and does not identify within-person prediction, timing direction, or a screening threshold.
- **Injury:** the [18 November pilot audit](2026-11-18/report.md) found that even under complete ascertainment, 0 reported serious events among 31 would leave a one-sided 95% upper bound of 9.21% in that selected pilot population. The [19–22 November audits](2026-11-22/report.md) separated reported behaviors, emergency or hospital care, and registry diagnoses. The Swedish transport association attenuated when recorded ADHD was excluded, and the Swedish cervical and transport cohorts may overlap; Taiwan TBI claims represent a separate endpoint, not replication of tic-attributed harm. Neither selected treatment participants nor longer-term registry outcomes estimate short-term adjudicated injury for adults whose tics required urgent care at screening. The week did not verify a new posted [randomized TICNET result](https://clinicaltrials.gov/study/NCT06271083) or a new qualifying safety alert in its bounded surveillance; this is not global absence.

## Reproducible audit: do similar group averages justify substituting one reporter for another?

Question and rule, set before the calculation: would the published pediatric CTIM summary identify absolute parent–child agreement on raw totals? Expect it to identify a descriptive difference between group means, but not paired agreement. Disconfirm if the paper supplies exact raw-total paired differences or the exact matched raw-total moments and compatible Pearson covariance with which to reconstruct their spread. Clinical interchangeability would additionally need an independently justified tolerance, not just correlations.

Inputs: [Cloes et al., DOI 10.1111/dmcn.13285](https://onlinelibrary.wiley.com/doi/10.1111/dmcn.13285), final paper only, Results sections on total impairment and within-family correlations. Eighty-five pediatric Tourette families (mean YGTSS total tic score 14.3/50) and 92 control families. The totals below are from the Tourette group; the paper notes blank or not-applicable items in ten families and uses per-question averages for statistical analyses. It reports within-family associations of 0.54 (tic) and 0.39 (non-tic), but we could not verify that those coefficients are Pearson correlations for the exact paired raw-total rows underlying these descriptive moments. No raw data or paired limits of agreement were available for this audit. The [mini-CTIM derivation](https://pubmed.ncbi.nlm.nih.gov/28429606/) reused the published families, so it is not an independent replication of their agreement.

| Total | Parent mean (SD) | Child mean (SD) | Parent minus child, group means | Conditional SD of paired differences, covariance unspecified |
| --- | ---: | ---: | ---: | ---: |
| Tic | 19 (21) | 18 (19) | +1 (rounding envelope 0 to 2) | 2 to 40 points (1 to 41 allowing whole-number rounding) |
| Non-tic | 26 (25) | 15 (16) | +11 (rounding envelope 10 to 12) | 9 to 41 points (8 to 42 allowing whole-number rounding) |

Method: if both SDs describe the same matched sample and same raw-total scoring, the triangle inequality for centered scores bounds SD(parent minus child) by the absolute difference and sum of the SDs. This deliberately conservative mathematical envelope is not an estimate of actual paired dispersion, a confidence interval, or a limit of agreement. The rounding extension assumes each displayed number was rounded to the nearest integer. The observed group means are not individual differences. No sampling model, participant data, random seed, or statistical test was used.

```python
rows = [('tic', 19, 18, 21, 19), ('non-tic', 26, 15, 25, 16)]
for domain, pm, cm, ps, cs in rows:
    print(domain, pm-cm, (pm-cm-1, pm-cm+1),
          (abs(ps-cs), ps+cs), (max(0, abs(ps-cs)-1), ps+cs+1))
# tic 1 (0, 2) (2, 40) (1, 41)
# non-tic 11 (10, 12) (9, 41) (8, 42)
```

Result: the non-tic group-average difference remains substantial on the numerical scale under rounding, without implying clinically important change. The small tic group-average gap does not demonstrate agreement. Parent ratings were higher on all 37 non-tic item means; for tic items the direction varied and school concerns and peer teasing ranked differently by respondent. Neither reporter is an error-free anchor for the other. Retire the shortcuts that similar group means or positive associations alone justify substitution, or that item relevance proves longitudinal responsiveness. Do not generalize this pediatric, predominantly mild-to-moderate sample to severe adults.

## Next informative safe test

Seek a published, lawful aggregate table with pair and follow-up denominators, scoring and missingness rules, and paired disagreement or repeat-change estimates. Code respondent, construct, age, severity and measurement window independently. For short-term adult harm, separately seek a prospectively tracked cohort with measured baseline severity, a fixed observation window and independently verified events with tic attribution. If the published data cannot answer either, leave the estimate missing rather than combine proxies. Any future work with individuals, new data collection or clinical thresholds would require clinical collaboration, appropriate institutional/ethics approval and privacy safeguards; none is proposed for immediate execution. No input or action is needed from the owner now.
