# 20 November 2026 | Counting injury, reported burden and urgent care separately

## Bounded evidence scan

On 20 November UTC, PubMed ESearch found zero records for `(Tourette[Title/Abstract] OR "tic disorder"[Title/Abstract] OR "tic disorders"[Title/Abstract]) AND ("2026/11/19"[Date - Publication] : "2026/11/20"[Date - Publication])`. ClinicalTrials.gov API v2 returned totalCount 0 for condition `Tourette OR chronic tic disorder` and `AREA[LastUpdatePostDate]RANGE[11/19/2026, 11/20/2026]`. The [randomized TICNET record](https://clinicaltrials.gov/study/NCT06271083) still had no posted results and its last posted update was 21 February 2024. Supplementary indexed searches for current studies, preprints and safety signals did not verify a qualifying result. These are bounded checks subject to indexing lag, search matching and incomplete worldwide coverage; they do not rule out new results or safety events.

## Question, prediction and method

The [November 19 report](../2026-11-19/report.md) found no short-term injury estimate for adults excluded from TICNET because they needed urgent care. Would two historical clinical studies move us closer to that estimate, or mainly show how endpoint choice changes what gets counted? Prediction: they help specify the endpoint but cannot estimate that prospective risk. Read primary reports, extract denominator, window, attribution and severity, and compare the within-study counts without pooling or annualizing them.

| Source | What was counted | Main boundary |
| --- | --- | --- |
| [Cheung et al., 2007](https://pubmed.ncbi.nlm.nih.gov/17566119/) | 17 of 333 specialty-clinic patients (5.11%) met a historical composite of at least two emergency visits or at least one hospitalization for Tourette symptoms or associated behavioral conditions. | The three years describe the clinic evaluation period, not common individual follow-up. Encounters included injury and other reasons. The primary abstract does not provide an injury-only numerator. |
| [Szejko et al., 2019](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2019.00638/full) | With a one-week lookback, 55 of 165 (33.33%) reported self-injurious behavior, including 34 of 100 younger participants and 21 of 65 adults (32.31%). The definition included behaviors without visible injury. | One-time ambulatory interview, not later events or an urgent-risk cohort. Attribution to tics versus other behavior was not reliably separated. |

Arithmetic is reproducible as `100 * numerator / denominator`, rounded to two decimals. The study percentages do not have comparable denominators, endpoints or observation windows; their difference is not an estimate of missed cases or health-care access. In Szejko et al., the adult groups' unadjusted YGTSS medians were 71 and 44.5, but the authors did not report a statistically significant adjusted predictor of current behavior in adults. This does not establish no association. The YGTSS intensity component used by the study partly incorporates self-injury, and the score and reported behavior referred to the same week. The contrast may therefore partly reflect measurement overlap. The published aggregates cannot isolate how much.

## Decision and next useful input

Keep urgent-care encounters, concrete injury, encounter reason, and attribution certainty as separate extraction fields. Permit mixed or uncertain attribution. To test prediction, look for a baseline measure that does not mechanically encode the injury outcome, independently ascertained events after baseline, known follow-up completeness, and inclusion of the urgent-risk group. These historical reports add a measurement constraint, not a validated predictor or an estimate for TICNET-excluded adults. No personal risk or treatment inference follows.

## Journal and link maintenance

On 20 November UTC, the three most recent dated report targets checked via anonymous raw GitHub returned HTTP 200. The Frontiers primary paper returned 200. The Wiley primary publisher returned 403 to the link checker; this is access-limited, not evidence of a broken link, and the public primary abstract is linked above. The pre-publication live feed returned HTTP 200 with repository provenance and 24 entries. Featured activity: Notice one comfortable thing, using existing optional copy with permission to skip. The activity catalog and disabled shared feedback are unchanged. No new intervention or rendered visual acceptance is claimed.
