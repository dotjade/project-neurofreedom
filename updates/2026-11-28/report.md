# Project NeuroFreedom daily research | 28 November 2026

## Bounded evidence scan

Checked around 03:01–03:03 UTC. PubMed ESearch query: `(Tourette[Title/Abstract] OR tic disorder[Title/Abstract] OR tic disorders[Title/Abstract]) AND (2026/11/27:2026/11/28[EDAT])`. One indexed record; EDAT is not the publication date.

- [Tang et al., publisher correction](https://link.springer.com/article/10.1186/s13034-026-01219-w), published 26 November, PMID 43099694, corrects the June [cross-sectional pediatric study](https://doi.org/10.1186/s13034-026-01105-5), PMID 42251378. Corrected mix: 94 Tourette, 41 provisional tic disorder, 16 chronic motor tic disorder (151 total). The notice clarifies analysis software and restricted availability of pediatric data, and replaces predictive/risk wording with association terminology. Use the correction if an indexed copy retains the older wording. This is not a new cohort, longitudinal prediction, evidence of cause, or an adult estimate. This pass did not independently audit model-output supplements or seek individual data.
- ClinicalTrials.gov API v2 query: `(Tourette OR "tic disorder") AND AREA[LastUpdatePostDate]RANGE[2026-11-27,2026-11-28]`. Three hits: [NCT03764748](https://clinicaltrials.gov/study/NCT03764748), a microbiota transplant study, and [NCT07137442](https://clinicaltrials.gov/study/NCT07137442), a diagnostic neurophysiology study, were marked recruiting with no results posted. The transfusion study NCT07883252 was unrelated. Registry changes are not treatment findings or participation recommendations. Targeted FDA search found no verified in-window relevant safety notice; this search does not establish absence of risk.
- [Okun et al., journal correspondence](https://doi.org/10.1056/NEJMc2608489), PMID 43084793, 26 November, is carried forward, not a new publication. Publisher full text remained inaccessible (403). [The first author's public summary](https://parkinsonsinsights.com/dr-michael-okun-my-take/18474550225190760) reports seven of eight over a 30% improvement threshold at nine months, but does not identify the exact score component or registry ID. The small uncontrolled study does not establish comparative effectiveness or safety. The analysis below tests whether the registry numbers can corroborate a particular interpretation.

## Bounded question: can the registry establish a tic-only responder count?

**Prediction.** Numerical agreement with the author's headline does not resolve the measurement definition. Even under a favorable common-scale assumption, the posted values may identify only a range for response on motor and vocal tics without the separate impairment component.

**Inputs and method.** [NCT05371041 official results](https://clinicaltrials.gov/study/NCT05371041?tab=results) and [API](https://clinicaltrials.gov/api/v2/studies/NCT05371041), results first posted 25 September 2026. The 28 November API snapshot had SHA-256 `1c7db892f3c8caabd6b8244d061e8d6e656966360d5c9c5e531ab729e8f9dfdd`. Pair the eight sponsor-posted baseline and follow-up score rows by their within-study labels. No names or row-level scores are republished here. There was no randomized comparison, masking or control arm. The [protocol](https://cdn.clinicaltrials.gov/large-docs/41/NCT05371041/Prot_000.pdf) describes the nine-month comparison with preoperative baseline, while the registry labels the visit relative to DBS initiation; exact paper timing still needs confirmation. The protocol's eligibility, including exclusion of head-banging judged likely to damage hardware, limits generalization to all severe/high-injury cases.

**Results.** A direct calculation using the values as posted gives seven of eight strictly above a 30% numerical reduction. This is not a validated common-scale calculation: baseline is explicitly 0–100 including impairment, while follow-up is labeled 0–50 Total Tic Score and contains a value above that maximum. Eight rows with values do not validate their definitions. In a *conditional sensitivity analysis only*, assume both visits instead used the 0–100 total made by adding a 0–50 tic score and a 0–50 impairment score. A given total T allows tic scores from max(0, T−50) to min(50, T). Comparing opposite ends of those intervals gives **4–8 of eight possible tic-only responders** under that assumption, not an observed rate, confidence interval or correction. These are sharp arithmetic bounds under separability of the two components with no additional cross-person or longitudinal constraints. No mean tic-only or impairment improvement can be recovered from these inputs.

Reproduction against the named registry snapshot (run with the public JSON as the first argument; only aggregate counts printed):

```python
import json, sys
r = json.load(open(sys.argv[1]))["resultsSection"]
base = next(m for m in r["baselineCharacteristicsModule"]["measures"]
            if m["title"] == "YGTSS Score")
end = r["outcomeMeasuresModule"]["outcomeMeasures"][0]

def scores(m):
    return {row["title"]: int(row["categories"][0]["measurements"][0]["value"])
            for row in m["classes"]}

x, y = scores(base), scores(end)
assert len(x) == 8 and x.keys() == y.keys()
pairs = [(x[k], y[k]) for k in x]
assert all(50 < b <= 100 and 0 <= f <= 100 for b, f in pairs)
lo, hi = lambda t: max(0, t - 50), lambda t: min(50, t)
print(sum(10 * f < 7 * b for b, f in pairs))               # 7 raw
print(sum(10 * hi(f) < 7 * lo(b) for b, f in pairs),       # 4 forced
      sum(10 * lo(f) < 7 * hi(b) for b, f in pairs))       # 8 possible
```

**Safety, uncertainty and decision.** The registry lists serious adverse events in three of eight, other events in eight and no deaths in the posted report. The serious entries include a post-implant hospitalization for functional episodes, a scalp-incision microabscess and a prolonged postoperative stay associated with hemorrhage. The registry's adverse-event window runs from enrollment to end of follow-up (approximately two years after lead implantation), but the study remains active with non-systematic event assessment reported. Do not infer complete two-year surveillance, causal attribution to adaptive stimulation, comparative safety or population risk rates. Work/social/family and longer follow-up assessments appear in planning documents, not as posted outcomes in the analyzed results module. Matching cohort size, timing and arithmetic strengthen the NCT05371041 link but do not prove it; do not add eight people to existing cohort counts or compare directly with the older six-month motor-subscore report. Seek the article or supplement for a direct identifier, explicit denominator, scale, timing, adverse-event attribution and function. Until then keep this out of efficacy pooling and do not upgrade the headline.

## Journal verification

Three displayed evidence links checked 28 November: Isaacs PMC direct browser check but full text available via indexed retrieval; Pappert publisher returned 403 to direct retrieval but the primary [PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/14557563/) is available via indexed retrieval; Ivanova publisher returned 200. No link was classified dead. Rotated to the existing optional music-or-silence activity with silence, rest and skipping equivalent. No intervention, contact, participation, votes or data collection.
