# 23 November 2026: Can a small blood-marker study establish diagnostic accuracy?

## Scan and source verification
PubMed ESearch (Tourette, tic disorder or tic disorders in title/abstract, entry dates 22–23 November) returned one match. [He et al.](https://doi.org/10.1177/11772719261505231), PMID [43067834](https://pubmed.ncbi.nlm.nih.gov/43067834/), was published electronically on 3 November and entered PubMed on 22 November, per NCBI PubMed XML. It was not in the evidence ledger. Full text was read via NCBI PMC EFetch (PMC13788251) after the ordinary PMC page was access-limited. ClinicalTrials.gov API v2 (conditions Tourette or tic disorder; last update posted 22–23 November) returned zero. One apparent November index hit, NCT05705999, actually had a registry last-update-posted date of 18 July 2025. Bounded indexed bioRxiv, medRxiv, FDA, EMA and MHRA checks revealed no verified new relevant preprint or safety alert. This is not exhaustive and the current day is incomplete.

## Bounded question and prediction
We expected high apparent case-control accuracy to be reproducible from reported denominators for the combined marker, but not sufficient for a clinic-ready test. We checked the paper's operating-point arithmetic and compared the direction of the miR-429 finding with its cited earlier primary study.

## Methods and results
The single-center cross-sectional study compared 60 children ages 3–14 with tic disorders (20 in each of three reported subtypes) with 20 healthy controls. It reported lower miR-429 and higher miR-189 in cases. Different tic subtypes were not significantly separated by either marker. At the combined operating point, reported 59/60 case detections and 20/20 correct controls yield 79/80, or 98.75% apparent accuracy. Nominal Wilson 95% binomial intervals are 91.14–99.71% for 59/60 sensitivity and 83.89–100% for 20/20 specificity. Those intervals quantify sample-size uncertainty only, not bias from selecting or evaluating thresholds in this sample; they are not external-validation intervals.

At the miR-189-only operating point, the abstract, Results text and Figure 4 caption all give 100% sensitivity and 93.3% specificity. No integer true-negative count out of 20 yields 93.3%; one control changes a raw rate by five percentage points. The paper did not supply an alternative denominator or enough information to resolve this check. Do not reverse the labels or substitute an inferred confusion matrix. Combined sensitivity as reported, 98.3%, is also lower than the reported 100% for miR-189 alone, despite wording that sensitivity improved versus the single markers. This is a reporting inconsistency, not evidence that the underlying association is false.

[Rizzo et al. (2015)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4513635/) also reported lower serum miR-429 in Tourette syndrome. They reported 95% sensitivity and 42% specificity in their separate assay cohort of 52 Tourette cases and 15 unaffected controls; compare these as published estimates, not interchangeable thresholds. He et al. reported 95% sensitivity and specificity for miR-429 in their mixed tic-disorder sample. Agreement on direction is not replication of specificity. Population, comparator, assay and operating-point differences prevent pooling.

Reproduce the interval calculation with only the published aggregate counts (no individual data or random seed):

```python
from math import sqrt
z = 1.959963984540054
for k, n in [(59, 60), (20, 20)]:
    p = k/n
    d = 1 + z*z/n
    c = (p + z*z/(2*n))/d
    h = z*sqrt((p*(1-p) + z*z/(4*n))/n)/d
    print(k, n, round(100*(c-h), 2), round(100*(c+h), 2))
print(any(round(100*k/20, 1) == 93.3 for k in range(21)))
```

## Next decision and limitations
Treat this as a pediatric candidate association, not a validated diagnostic or severity test. Healthy controls do not represent children referred for diagnostic uncertainty. There was no demonstrated external validation, no longitudinal evidence, and no prospective evidence of clinical usefulness. The study also reports no hemolysis monitoring because the samples had been exhausted. Seek an independently assessed cohort of consecutive referrals, including relevant clinical comparators, with thresholds fixed in advance, complete denominators and assay quality controls before revisiting diagnostic accuracy. Do not infer adult performance, causation, a treatment target or patient-specific meaning. The separate severe-adult injury endpoint question remains open.

## Homepage source check
On 23 November the adult priorities PMC full text and the online ERP publisher article were accessible in the web retrieval. The Pappert publisher denied automated access (403); the matching PubMed record was independently identified through official XML even though the browser endpoint was access-limited. This does not show that the publisher link is broken for readers.
