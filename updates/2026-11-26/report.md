# Project NeuroFreedom daily research | 26 November 2026

## Evidence scan

Bounded check at about 03:24 UTC. The previous verified report was on 25 November. NCBI PubMed ESearch query: (Tourette[Title/Abstract] OR tic disorder[Title/Abstract] OR tic disorders[Title/Abstract]) AND (2026/11/25:2026/11/26[EDAT]). Two records returned; publication dates are separate from indexing dates. Checked their NCBI XML.

- [Okun et al., PMID 43084793](https://pubmed.ncbi.nlm.nih.gov/43084793/), [DOI](https://doi.org/10.1056/NEJMc2608489), is a NEJM Letter dated 26 November on dual-target adaptive deep-brain stimulation. The NCBI record and Crossref metadata identify it but provide no abstract; publisher HTML and PDF returned HTTP 403 to direct retrieval. This could contain original observations. Sample, comparison, outcomes, overlap with previous reports and harms are not verified. Do not infer a trial result from its title. A lawfully accessible version of record or author manuscript is the prerequisite to extraction.
- [PMID 43078479](https://pubmed.ncbi.nlm.nih.gov/43078479/), [DOI](https://doi.org/10.1055/a-3012-7282), electronic publication 24 November: preclinical network modelling and a rat model of tic-like behavior. Abstract-only assessment. Findings are not human efficacy, dose, safety, or a basis to use the studied product.
- ClinicalTrials.gov v2 query: (Tourette OR "tic disorder") AND AREA[LastUpdatePostDate]RANGE[2026-11-25,2026-11-26]. Two hits: previously reviewed [NCT07137442](https://clinicaltrials.gov/study/NCT07137442), listed recruiting, update posted 25 November and no posted results; and NCT06654427 (obstetric care toolkit, unrelated). No new qualifying posted result in this bounded search.
- Targeted FDA web search for Tourette/ecopipam safety in this window found no in-window notice. This is not a comprehensive safety finding. PubMed dates, registry query coverage, publisher restrictions, and non-indexed evidence limit the scan.

## Bounded question: can work status capture opportunities someone did not pursue?

**Prediction:** A workforce status item and an opportunity restriction item measure different things. A combined missing and non-applicable category also prevents reconstruction of an eligible response rate.

**Methods:** Compare [Malli and Forrester-Jones, Table 5](https://d-nb.info/1252374968/34#page=10) with the [2025 Australian Impact for Tourette’s survey, figures 27 and 29](https://www.thekids.org.au/contentassets/8be1f70fdc6c4ffa95f2eef016f54cef/impact-for-tourettes-final---web-20250520.pdf#page=61). Extract count labels and denominators before comparing constructs. Deterministically vary eligibility and outcome among the UK table's unclassified entries; this is sensitivity arithmetic, not a new clinical observation.

**Source reconciliation:** The UK work-avoidance row shows 104 stopping themselves from applying, 43 reporting no difference, and 52 combined not applicable or missing, for 199 entries. The published 52.3% uses the full table denominator. The 53.8% in the narrative and repeated in a later review belongs to the close-relationship row (107/199); the work item is separate from reported discrimination when finding a job. The recruitment prose states 232 completed, 43 excluded and 199 included; 232 minus 43 is 189. The work row is internally consistent at 199, but the flow cannot be reconciled without clarification. No count is silently corrected.

**Sensitivity result:** Assuming the 104 and 43 are correctly classified among eligible respondents, let n of the 52 unclassified entries be eligible and y of those endorse the work item. Across all integers 0 <= y <= n <= 52, the hypothetical eligible rate (104+y)/(147+n) ranges from 104/199 (52.3%) to 156/199 (78.4%). Both extremes treat all 52 as eligible but assign opposite answers. The 104/147 (70.7%) value applies to the recorded noncombined responses, not necessarily all eligible people. The bounds only refer to the table frame under these assumptions, not sampling uncertainty, hidden response behavior, or a population rate.

```python
from fractions import Fraction
values = [Fraction(104+y, 147+n) for n in range(53) for y in range(n+1)]
assert len(values) == 1431
assert (min(values), max(values)) == (Fraction(104, 199), Fraction(156, 199))
```

The Australian survey reports 71% working for wages, self-employed or seeking work combined (56%, 13%, 2%), and separately 52% describing moderate to extreme impact on opportunities. Those are different measures and their joint denominator and overlap were not verified. The UK item concerns not applying in the context of anticipated discrimination; the Australian item is broader perceived restriction. Similar percentages are not replication. Neither survey identifies a rate for adults with prospectively confirmed severe active tics.

**Next decision:** Keep current work or school status, relevant opportunities considered but not pursued, and effort or difficulty after participation separate. Specify a recall window and an opportunity gate. Distinguish no relevant opportunity, deferred, chose not to pursue, and not offered or denied, then retain missing or declined separately. Require item-specific denominators and paired outcome counts before estimating overlap. No survey launch, new participant data, individual prognosis or treatment action.

## Journal maintenance

26 November: Isaacs full text accessible through PMC indexed retrieval; Neurology publisher returned 403 and matching [Pappert PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/14557563/) was accessible; Ivanova canonical publisher full text accessible. No broken link established. Kept all six optional approved activity choices unchanged and selected the existing small mark or silly sentence. No new activity or feedback collection.
