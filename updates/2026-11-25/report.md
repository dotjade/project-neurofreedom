# Project NeuroFreedom daily research note | 25 November 2026

## Bounded new-evidence scan

- **PubMed:** NCBI ESearch (Tourette, “tic disorder”, or “tic disorders”; November 24 to 25 by entry date) returned two indexed records. NCBI XML labels both Review: [PMID 43076924, an ecopipam review](https://pubmed.ncbi.nlm.nih.gov/43076924/) and [PMID 43075416, a pediatric neuroimmune framework review](https://pubmed.ncbi.nlm.nih.gov/43075416/). The first has no abstract in the retrieved record and its full text was not verified. The second abstract explicitly distinguishes hypotheses and observations from demonstrated developmental mechanisms. Neither is a new primary study result. The search date window overlaps yesterday's scan deliberately, because records can enter later that day.
- **ClinicalTrials.gov:** the v2 API returned two records with updates posted November 24, no further page and no posted results. [NCT07905898](https://clinicaltrials.gov/study/NCT07905898) is a previously registered adolescent resilience intervention, not yet recruiting, with feasibility as the primary outcome and estimated primary completion March 2031. [NCT07137442](https://clinicaltrials.gov/study/NCT07137442) is the existing NIH observational neurophysiology study listed as recruiting, with estimated primary completion August 2034. Its beta-power outcome over two days is not longitudinal injury follow-up. This pass verified current fields, not what changed in each revision.
- **Other coverage:** targeted searches of indexed preprints and regulator pages did not verify a new tic-specific primary result or material safety notice in the window. This is a bounded check, not a comprehensive negative safety conclusion. Existing sources below are used for design, not counted as new publications.

## Bounded question: can participation stand in for feeling engaged?

**Prediction:** An item asking whether a person can take part while managing tics will miss some burden captured by asking how present or engaged they feel. These are narrower constructs than quality of life and should not substitute for a tic count or a physical injury outcome.

**Methods:** Contrast two separate interview items in [Barber et al., 2024, PMID 38557310](https://pmc.ncbi.nlm.nih.gov/articles/PMC11179959/) with first-person qualitative themes from [Phoenix-Kane et al., 2025](https://doi.org/10.1080/18387357.2025.2584410). Check whether the published aggregate margins alone determine joint endorsement. All inputs below are public group percentages; there are no individual records.

**Observed reports:** Barber's selected follow-up interviewed 72 people aged 16 to 30 about 11 years after a pediatric trial. On one item, 87.3% reported that they could manage tics and participate, 9.9% could do one or the other, and 2.8% neither. On the separate presence item, 45.2% reported less presence, 27.4% more, and 27.4% neither. Neither original treatment group nor responder status detectably predicted either of these item responses in the reported analyses. Strategies were not limited to the original intervention, and absence of a detectable group difference is not evidence of equivalence. Phoenix-Kane gathered 13 interviews and one written response from UK adults aged 18 to 59 who self-reported that they had been diagnosed in adulthood; nine reported childhood onset. Accounts illustrated effort and exhaustion despite appearing to manage tics. First-person accounts are distinct from examples about other people. The studies were not prospective measures of actual activity completion or verified injuries.

**Aggregate inference, not an observed cross-tab:** Under ordinary decimal rounding of unweighted integer counts with an item denominator at most 72, the only compatible category counts are 62/71, 7/71, 2/71 and 28/62, 17/62, 17/62, respectively. If both item margins were unweighted as assumed and drawn from the same 72 interviewees, the count that endorsed both participation and less presence could range from 18 to 28: the lower bound is 62 + 28 - 72 and the upper bound is the smaller endorsement count. The published results do not identify the exact count, who overlapped, or a paired response rate. This arithmetic does not estimate true unreported responses; nonresponse remains unknown.

Reproduce with Python 3 (deterministic, no seed required):

```python
from fractions import Fraction

def matches(percent_tenths):
    rows = []
    for n in range(1, 73):
        counts = [int(Fraction(p*n, 1000) + Fraction(1, 2))
                  for p in percent_tenths]
        if sum(counts) == n and all(
            p - Fraction(1, 2) <= Fraction(1000*k, n) < p + Fraction(1, 2)
            for k, p in zip(counts, percent_tenths)
        ):
            rows.append((n, *counts))
    return rows

assert matches([873, 99, 28]) == [(71, 62, 7, 2)]
assert matches([452, 274, 274]) == [(62, 28, 17, 17)]
assert (max(0, 62 + 28 - 72), min(62, 28)) == (18, 28)
```

**Limitations and next decision:** The interview cohorts were selected, neither gives a representative estimate for adults with severe active tics, and the numbers above do not measure injury, treatment harm or effectiveness. Use the distinction as a design check: keep participation and the effort of staying engaged separate for the same short recall window. Distinguish no difficulty, activity not attempted, strategy not used, and missing response. In a future authorized design review, require item denominators and a paired cross-tab to quantify overlap. Keep visible tic observations, pain, sleep disruption and independently ascertained injury separate. No survey, recruitment, patient data or treatment action.

## Public link check

November 25: Isaacs PMC full text was accessible through indexed retrieval despite a direct HTTP 203 intermediary; the Pappert publisher returned 403 to direct requests and matching PMID 14557563 was verified in NCBI XML; Ivanova's canonical publisher full text returned HTTP 200. No link was classified as broken. Reviewed the existing optional activity catalog; no activity was added, and feedback remains off.
