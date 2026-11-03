# CANNA-TICS driving: favorable signal, unresolved analysis sets

3 November 2026. **Historical published-aggregate audit, not a simulation, independent trial, participant-data reanalysis or driving clearance.**

## Question and prospective prediction

The [local plan](plan.md) preceded full-methods retrieval attempts and computation; SHA-256 is recorded in [inputs](inputs.json). It was not externally preregistered. We asked whether the same-trial driving report establishes confirmatory noninferiority or general road safety. The prediction was that the upstream test hierarchy and endpoint/population limits prevent that stronger inference. An independently valid confirmatory hierarchy, justified margin, compatible analysis sets and direct road-safety ascertainment would weaken that concern.

## Primary sources and extraction

The peer-reviewed [driving report](https://doi.org/10.1089/can.2023.0114), PMID [38265476](https://pubmed.ncbi.nlm.nih.gov/38265476/), first appeared January 23, 2024; its issue is October 2024. The accessible abstract describes 64 adults at two sites (43 active, 21 placebo), assessed by computerized binary fitness at baseline and week 13, after nine stable-treatment weeks. It reports a favorable difference of 0.17, 95% CI -0.08 to 0.43. This is a same-trial substudy, not replication. Full text redirects to restricted access; actual model, imputation and population details remain unverified. [Source log](source-log.json) records the bounded access and integrity checks.

The [2020 protocol](https://doi.org/10.3389/fpsyt.2020.575826) specifies center-stratified Mantel-Haenszel estimation, a -32 percentage-point noninferiority margin and testing only after primary tic superiority. Its computerized criterion classifies a person unfit if any of five test percentile ranks is below 16. These are planned tests, not observed road crashes. The margin's clinical justification was not established in this bounded audit. Publication after trial completion does not independently establish when each provision was fixed.

The official [EU results](https://www.clinicaltrialsregister.eu/ctr-search/trial/2016-000564-42/results), first published December 31, 2023, identify NCT03087201/EudraCT 2016-000564-42. The blind-review-defined 25% primary test p=.0755 did not pass the superiority gate. The originally planned 30% analysis also failed (p=.0633); its registry description repeats 25%, a retained metadata inconsistency. Whole-trial adverse-event counts are 61/64 active versus 26/33 placebo, not driving-substudy counts or accident rates. The registry's adverse-event section includes serious events, so those must not be added again. Neither these historical results nor this audit is new clinical evidence today.

## Executed reconciliation

[Code](analyze.py) and [results](results.json) reproduce the following without RNG or participant records:

- Under nearest-0.1-percent rounding, 28 reported fit participants at 71.8% uniquely imply denominator 39 among integers up to 43. Likewise, 10 at 52.6% imply 19 among integers up to 21. These are **percentage-compatible denominators**, not verified observed-completer counts.
- If the baseline and transition counts described exactly the same complete population, active final fit would be 24 - 2 + 8 = 30, and placebo 14 - 4 + 2 = 12. These differ from the reported final 28 and 10. Different analysis populations or missingness handling could explain this; an error is not established.
- The crude fraction contrast 28/39 - 10/19 equals 0.19163, not the reported 0.17. This is not a reconstructed adjusted estimator or a correction of the paper.
- The reported lower limit -0.08 is 24 percentage points above the planned -0.32 margin, but its interval includes zero. Numerical clearance of that margin does not reopen the failed upstream confirmatory gate. Nor does it establish superiority, equivalence, zero impairment or an acceptable risk for an individual.

This narrows rather than erases the favorable signal: the reported estimate favors active treatment, while the accessible documents do not support the stronger confirmatory/general-safety conclusion. The author's favorable interpretation is retained as counterevidence to a blanket harm claim, not adopted as individual advice.

The planned missingness bounds were **not executed**. Treating four and two as verified missing outcomes would silently assume the very analysis-set definitions under audit. Exact prerequisites are a lawful participant-free methods/table source giving observed endpoint counts, paired transitions, imputation, ITT/per-protocol definitions and corresponding intervals. No missing outcomes or corrected table were invented.

## Applicability, uncertainty and next decision

A short selected adult computerized assessment does not establish long-term road safety, an absence of sedation, benefits in children or older adults, or results for separately identified persistent-severe adults and excluded comorbidities. Pain, work participation and other functional burdens remain distinct. This is not a treatment change, cure claim or recommendation to drive/use cannabinoids.

Ten implementation tests pass. Independent checks are recorded in [review](review/review.md); software/source verification is not clinical validation. No source PDF, participant file or individual narrative is published.

Close the fixed driving abstract/hierarchy audit until the specified lawful aggregate methods become available. Do not repeat restricted full-text attempts or infer missing outcomes. Next follow the monthly portfolio's conditional H15 gate: inventory publicly licensed group-only network maps, code, input provenance and reuse conditions before any computation. Stop if only participant-level or controlled-access materials exist. No author contact, data application, intervention, owner action or paid compute is needed for that inventory; clinical validation would require independent cohorts, institutional governance and ethics review.

## Reproduce

From repository root:

```sh
python analyses/canna_driving/2026-11-03/analyze.py
python -m unittest discover -s analyses/canna_driving/2026-11-03 -p 'test_*.py' -v
```
