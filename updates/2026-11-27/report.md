# Project NeuroFreedom daily research | 27 November 2026

## Bounded evidence scan

Checked around 02:52–02:54 UTC. PubMed ESearch: `(Tourette[Title/Abstract] OR tic disorder[Title/Abstract] OR tic disorders[Title/Abstract]) AND (2026/11/26:2026/11/27[EDAT])`. One indexed record. EDAT is a database entry date, not the journal publication date.

- [Shi and Liu, Frontiers in Genetics](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2026.2031856/full), PMID 43095713, DOI 10.3389/fgene.2026.2031856, was published 12 November and newly indexed in this scan. This is peer-reviewed exploratory research, not a human treatment study. Its whole-blood tic dataset had 28 cases and 20 controls; a separate allergy dataset had 248 cases and 209 controls, measured on a different platform. No shared gene passed the adjusted threshold in both datasets. At nominal screening, 288 genes overlapped, including 132 with opposite directions; further filtering prioritized six candidates. Those candidates do not establish a shared causal mechanism, a marker measured in people with both conditions, or an actionable test. The human immune-cell findings were inferred from expression, and the separate animal findings do not establish human benefit or risk. No estimate for persistent severe adults was presented.
- [Okun et al., NEJM Letter](https://doi.org/10.1056/NEJMc2608489), PMID 43084793, 26 November: carried forward from yesterday, not a second publication. NCBI XML still supplies no abstract, and direct publisher HTML/PDF returned 403. [NCT05371041](https://clinicaltrials.gov/study/NCT05371041) is a comparator, not a verified match. No letter sample, endpoint, outcome, or safety claim is extractable.
- ClinicalTrials.gov API v2 query: `(Tourette OR "tic disorder") AND AREA[LastUpdatePostDate]RANGE[2026-11-26,2026-11-27]`. Zero hits in this bounded check. Targeted FDA site search found no verified in-window tic-treatment safety notice. These results do not establish completeness or absence of risk.

## Bounded question: does a published measurement paper tighten the count without relying on a preprint?

**Prediction:** A published mixed-source sample of 14 distinct adults raises the lower bound for the enrollment union above 10 under the prior model, but does not add people to that union. A same-trial report of eight people does not raise the bound further.

**Methods and verified sources:** Use the two actual registry enrollments: [NCT02056873](https://clinicaltrials.gov/study/NCT02056873), 10; [NCT05371041](https://clinicaltrials.gov/study/NCT05371041), 8. Extend the [25 October accounting model](../../analyses/cohort_accounting/2026-10-25/report.md) without changing its containment assumption. [Lowor et al., published 21 March, Methods 2.1–2.2 and Table 1](https://doi.org/10.1016/j.prdoa.2026.100438) explicitly links 14 adults to both studies. The measurement comparison includes 143 video recordings and 143 EMG recordings in paired modalities, not 286 distinct people or independent visits. [Tvenstrup et al., Methods, Participants](https://journals.flvc.org/UFJUR/article/download/141687/148596) explicitly links its eight-person programming-threshold sample to NCT05371041; the bilateral analysis subset is four. Its threshold observations are not a separate trial or long-term harms denominator. No participant-level data were downloaded for this computation.

**Results:** Let k be the possible intersection of the enrolled groups. Their union has size 18 − k. The reproducible enumeration below uses public aggregate counts only; no simulation, randomness, or individual inference is involved.

```python
older, newer = 10, 8
for minimum in (0, 14, 16):
    k = [x for x in range(min(older, newer) + 1)
         if older + newer - x >= minimum]
    union = [older + newer - x for x in k]
    print(minimum, (min(k), max(k)), (min(union), max(union)))
```

| Constraint | Possible intersection | Possible union |
|---|---:|---:|
| Registry sizes alone | 0–8 | 10–18 |
| Published mixed report, without preprint | 0–4 | 14–18 |
| Prior 16-person preprint retained | 0–2 | 16–18 |

**Uncertainty and next decision:** These are conditional documentation bounds, not an estimate of actual overlap or of the people analyzed at a clinical endpoint. The two linked reports do not establish additional participants or independent treatment effects, and the model would need revision if containment fails. Retain note-level links for the measurement and programming report. Reclassify the letter only when lawful primary full text provides trial provenance, visit timing, analysis denominators, and safety reporting.

## Public journal verification

27 November bounded displayed-link pass: [Isaacs et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC10863457/) directs a direct client to a browser check but indexed full text was readable; [Pappert et al. publisher](https://www.neurology.org/doi/10.1212/01.WNL.0000086370.10186.7C) blocked the direct client, with a [primary PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/14557563/) available; [adult online behavioral study](https://link.springer.com/article/10.1186/s44247-026-00284-7) and [previous daily report](../2026-11-26/report.md) reachable. These retrieval limitations are not verified dead links. Existing optional rest card selected; catalog unchanged and feedback stays disabled. No clinical guidance, recruitment, or personal records.
