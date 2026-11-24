# 24 November 2026: Which studies count injuries caused by tics?

## Daily scan

NCBI PubMed ESearch, `(Tourette[tiab] OR tic disorder[tiab] OR tic disorders[tiab]) AND (2026/11/23:2026/11/24[edat])`, returned zero indexed matches at this check. ClinicalTrials.gov API v2, condition `Tourette OR tic disorder` and `AREA[LastUpdatePostDate]RANGE[2026-11-23,2026-11-24]`, returned three existing records with a 23 November update and none with posted results:

- [NCT06576726](https://clinicaltrials.gov/study/NCT06576726): recruiting adolescent observational cohort, ages 11–17, estimated primary completion August 2029.
- [NCT01019343](https://clinicaltrials.gov/study/NCT01019343): completed broad movement-disorder interventional research record; actual primary completion August 2016. The November registry timestamp is not a new completion or outcome.
- [NCT07137442](https://clinicaltrials.gov/study/NCT07137442): recruiting observational distinction of tics and functional tics, ages 18–80, estimated primary completion August 2034.

The current records were verified individually via API v2. The version-history endpoint denied automated access, so the fields actually changed were not established. Bounded indexed bioRxiv/medRxiv and FDA/EMA/MHRA queries did not verify a relevant new preprint or material safety alert in the window. This scan is not exhaustive and 24 November is incomplete.

## Bounded question and prediction

Following the 22 November register comparison, we expected an older consecutive clinic sample to describe injury-related categories and an Australian survey to capture patient-attributed injuries outside hospital records. We tested whether either can identify the numerator and denominator for independently verified injuries attributable to tics over a fixed period in adults with measured, active severe symptoms.

## Methods and results

We extracted recruitment frame, outcome classification, source of attribution, age/severity, observation window and eligible outcome denominator from the primary sources. An unavailable field is not a negative finding.

| Source | Observed evidence | Why it cannot answer the short-term risk question |
| --- | --- | --- |
| [Baizabal-Carvallo et al.](https://link.springer.com/article/10.1007/s00415-021-10822-0), published 2021, 2022 issue | 201 consecutive people with Tourette syndrome at a tertiary center; abstract classifies 34 under broad self-injurious behavior, partitioned into 23 self-directed, 7 outward-directed and 4 tic-related. | Only the abstract was accessible. The 4 is the explicitly tic-related subgroup of that classification, not an incident-injury count. Active severe adult denominator, injury window and independent attribution are not verified. |
| [The Kids Research Institute Australia, 2025 primary survey report, p. 40](https://test.telethonkids.org.au/contentassets/8be1f70fdc6c4ffa95f2eef016f54cef/impact-for-tourettes-final---web-20250520.pdf#page=40) | 68% of adult respondents and 68% of child caregivers reported injuries they attributed to tics; commonly described injuries included pulled muscles, sprains and whiplash. | Page 40 does not give the injury-item response denominator, a fixed recall window or a severe-adult stratum. The adult percentage is respondent attribution, not adjudicated incidence. A denominator reported for a different item cannot recover its counts. |

Arithmetic reproduces the clinic classifications: 23 + 7 + 4 = 34; 34/201 = 16.92% and 4/201 = 1.99% (rounded). The survey 68% cannot be converted into a count here. The observed percentages have different selection frames and endpoints; neither their ratio nor their difference measures missed cases, misclassification or risk. This is an endpoint audit of two selected sources, not a systematic evidence-absence claim.

## Next decision

Carry both sources forward as distinct evidence: a broad clinical classification and experienced burden reported by respondents. Do not pool them or use either as a short-term adult rate. The next eligible source must identify the number of actively severe adults under observation, the same defined period for all, and new injuries with a prespecified and preferably independent attribution process. Keep care sought, received, or recorded separate from whether an injury occurred. No clinical action follows from this analysis.

## Homepage source check

On 24 November, the Australian institutional report returned HTTP 200 and p. 40 was extracted. Direct automated HTTP retrieval of the previously displayed Rizzo PMC and He and Chen PubMed pages returned 203 intermediary responses rather than verified articles. They were not classified as broken or replaced on that basis; the project retains the previous verified source records.
