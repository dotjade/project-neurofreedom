# Daily public evidence scan: 19 October 2026

## Finding

**No new-window qualifying primary tic-study result or newly posted relevant registry result was verified in this bounded scan.** Twelve PubMed records were screened; 11 were absent from yesterday's bounded result set, but this does not make them 11 new studies. Newly encountered material includes older primary papers, secondary reviews, a hypothesis/theory article and unrelated lexical matches.

A historical 2025 mechanistic paper involving six implanted TS participants is retained as a follow-up lead, separately from the intentionally empty new-primary ledger. It does not establish clinical benefit or a cure. Current findings do not warrant changing treatment claims.

## Scope, provenance and dates

Prior verified cutoff: October 18 at 02:41:39 UTC. Core API requests ran October 19 at 03:07:21–03:08:06 UTC; selected candidate checks ended at 03:09:45 UTC. Searches overlap October 17–19 inclusive; October 19 was only partly elapsed. Date filters concern publication, database entry, metadata revision, preprint posting/version or registry posting, according to the source. They are not interchangeable.

The current RESEARCH_PROTOCOL.md, main evidence.jsonl, October 18 report, search ledger and supporting scan/build code were read via the GitHub connector. Repository tree at retrieval: `00f5e25592b3ab2a15f5485053358ea9356d97a5`. Baseline files preserve the exact prior identifiers and comparison metadata. [Search code](scan_sources.py), [search/decision ledger](artifact_parts/manifest.json), [candidate verification](candidate-verification.json) and [summary](summary.json) preserve requests, times, counts, hashes and decisions. Live APIs may change; these are observed responses, not a frozen database census.

No age, severity, language or human-only filter was applied. Adult persistence, severe symptoms, pain, burden, co-occurring conditions, negative findings and adverse outcomes were explicitly included in supplementary searching. Pediatric and selected implanted-cohort findings are not extrapolated to the whole adult population.

## PubMed

Eight ESearch queries used retmax=1000; all counts were below the cap. They yielded **21 ID occurrences and 12 unique records**. All received publication-type/date/identifier and linked-notice screening. Selected non-case abstracts were read transiently; abstracts and full papers are not retained.

| Query | Date field | Inclusive dates | Count |
|---|---|---|---:|
| Tourette OR "tic disorder" OR "tic disorders" | edat | October 17–19 | 3 |
| Same core | edat | October 18–19 | 0 |
| Same core | pdat | October 17–19 | 0 |
| Same core | mdat | October 17–19 | 9 |
| Core plus retraction/retracted/erratum/corrigendum/correction | edat | October 17–19 | 0 |
| tics OR "chronic motor tic" OR "chronic vocal tic" OR "persistent tic" | edat | October 17–19 | 6 |
| Same synonyms | pdat | October 17–19 | 0 |
| Core plus adult/severe/pain/burden/ADHD/comorbidity/treatment/adverse/negative/quality-of-life terms | edat | October 17–19 | 3 |

The ledger supplies exact Boolean strings and PubMed translations, rather than only these abbreviations. One record overlaps yesterday: PMID 42888480, the previously screened October 16 pediatric abdominal-tic narrative review. Its linked-notice fields remained unchanged. No linked correction/retraction was found for the newly screened records, but this is not comprehensive Crossmark or publisher clearance.

### Secondary and conceptual material

- [PMID 42890800](https://pubmed.ncbi.nlm.nih.gov/42890800/), [publisher](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2026.1948442/full): October 2 **hypothesis/theory** article about classification of coprophenomena. PubMed's generic Journal Article label must not be mistaken for a primary validation study. Its proposed diagnostic reframing has not been validated here. Coprolalia alone must not be used to infer functional etiology.
- [PMID 42890894](https://pubmed.ncbi.nlm.nih.gov/42890894/), [publisher](https://www.frontiersin.org/journals/child-and-adolescent-psychiatry/articles/10.3389/frcha.2026.1936806/full): October 2 **systematic review** of functional tic-like behaviors. Its 39 included reports are not 39 new independent cohorts. The review explicitly recognizes repeated reports from shared repositories; retrospective evidence limits causal and treatment inferences. FTLB evidence is kept distinct from chronic primary tic disorders.
- [PMID 42893364](https://pubmed.ncbi.nlm.nih.gov/42893364/): **pediatric PANDAS narrative review**, electronically published May 30 and entered into PubMed in October. It supplies no new chronic-tic immune-treatment trial or severe-adult efficacy estimate.
- PMID 41689912: older systematic review of gambling cognition; secondary, outside the new-publication window. PMID 42888480 remains yesterday's pediatric narrative-review record.

[Secondary screening records](secondary-screening.jsonl) are separate from primary evidence and from preprints. No review's pooled underlying cohort is re-added as original data.

### Historical primary lead and other exclusions

[PMID 40977255](https://pubmed.ncbi.nlm.nih.gov/40977255/), [DOI 10.1002/mds.70043](https://doi.org/10.1002/mds.70043), was electronically published September 22, 2025. Its October 17, 2026 metadata revision triggered retrieval. The abstract describes six participants with severe treatment-resistant TS, bilateral CM/aGPi leads and recordings across nine monthly visits without stimulation during recording. Tic-state low-frequency activity/coherence differences are within-person associations, not a randomized treatment effect, causal proof or clinically validated biomarker.

Age distribution, full eligibility, raw-data availability and overlap with other DBS publications were not verified. Nine visits are repeated measurements, not nine cohorts. Exact-PMID GitHub search and the main evidence ledger did not locate the paper, but search absence is not proof of a unique cohort. [Historical lead](historical-leads.jsonl) defines a source/age/trial-ID/cohort verification gate; it is deliberately not promoted to the main primary-evidence ledger.

PMID 41621322 is an older pediatric obsessive-compulsive-symptom genetic study. Its linked UpdateOf preprint PMID 40799755 represents the same work and must not count as independent replication. It does not establish a tic-specific treatment target. PMIDs 10382139 and 11518480 are historical executive-function comparisons from 1999/2001; the latter reports no working-memory group differences, but neither is a new tic-treatment result. PMID 11055462 is a historical letter/comment classified with case reports; no case detail was retained. PMIDs 42889367 and 42889785 are unrelated sepsis/nanocatalyst lexical returns.

## Preprints

Official bioRxiv/medRxiv date feeds were paginated for October 17–19. The prespecified case-insensitive title/abstract screen was `\btourett\w*|\btics?\b`.

- bioRxiv: 125 unique DOI/version pairs across five pages; 26 overlap yesterday, 99 do not.
- medRxiv: nine pairs on one page; all nine overlap yesterday.
- **Zero lexical matches among 134 pairs.** These are all-subject postings, not 134 tic studies. Pagination was complete for the observed totals.

Web discovery returned an October 1 TMS/CBIT preprint and a July beta-burst preprint, not a verified in-window new version. Preprints remain unreviewed evidence; no clinical recommendation follows from them. Other servers, synonym-only abstracts and later indexing remain coverage gaps.

## Official registries and negative evidence

ClinicalTrials.gov queried Tourette, tic disorder, Tics and ecopipam with `AREA[LastUpdatePostDate]RANGE[2026-10-17,2026-10-19]`, pageSize=100 and countTotal=true. Each query returned zero; none supplied a next-page token. This is a bounded update search, not a census of all TS trials.

Direct checks outside the window deliberately retained known negative/status evidence and checked discovery leads:

- [NCT05158439](https://clinicaltrials.gov/study/NCT05158439): Withdrawn, actual enrollment zero, inability to recruit, no results; last posting October 16. Negative feasibility evidence, not a negative efficacy trial or proof a cellular intervention was administered.
- [NCT07137442](https://clinicaltrials.gov/study/NCT07137442): Recruiting observational physiology protocol, last posting October 16, no results. Planned measures/dates are not observed outcomes.
- [NCT07093541](https://clinicaltrials.gov/study/NCT07093541): expanded-access status remains Temporarily Not Available, last posting October 14, no results. Selected status/design/results fields are unchanged from yesterday; no new suspension or cause is inferred.
- [NCT06194305](https://clinicaltrials.gov/study/NCT06194305): Recruiting, last posting July 22, no results; selected fields unchanged.
- [NCT07839377](https://clinicaltrials.gov/study/NCT07839377), [NCT07854665](https://clinicaltrials.gov/study/NCT07854665) and [NCT06825520](https://clinicaltrials.gov/study/NCT06825520): discovery leads have official last-post dates September 24, 2026; October 2, 2026; and May 28, 2025, respectively, with no results. They are excluded from new-window updates. Institutional/mirror crawl or synchronization dates do not establish new trial evidence.

The documented ISRCTN XML API query `(Tourette OR tics OR "tic disorder") AND lastEdited GE 2026-10-17T00:00:00 AND lastEdited LT 2026-10-20T00:00:00`, limit=50, returned HTTP 200 and totalCount=0. The undated Tourette positive control, limit=1, again reported 22 matches. This establishes a functioning endpoint, not review of all 22 protocols. The direct SATURN control was also retrieved. See [supplement](supplement-selected-metadata.json) and [control](isrctn-control.json).

WHO ICTRP's landing page was reachable; its latest listed import was October 12. No usable query export was obtained. CTIS was not independently enumerated today. No global-registry completeness is claimed. Regulatory surveillance is a separate component.

## Interpretation and next gate

The empty [new-primary ledger](primary-evidence.jsonl) is intentional. Existing negative findings and retraction exclusions remain in force; a zero retraction-query result does not clear historical retracted work. No study demonstrated disease modification or a cure in this run.

Next useful literature step: verify the historical recording paper's accessible source, age and cohort links before deciding whether it adds a nonduplicated mechanism test. Do not launch a generic data-access search or infer data availability from an abstract. Independent bounded analysis work is reported separately.

This scan retained original summaries, public bibliographic/protocol metadata and code only. No source abstract/full text, patient-level records, case narratives, contacts or private material are redistributed. No outreach, intervention, enrollment, account action or repository write occurred.

## Public artifact packaging

Large generated or source-metadata artifacts are stored in lossless text parts because oversized connector writes stalled. Run `python restore_artifacts.py` in this directory before the original commands. The [manifest](artifact_parts/manifest.json) records original SHA-256 values, byte lengths and ordered parts. This is storage-only packaging after execution, not an analytical deviation; frozen plan/configuration and results are unchanged. Original files are reconstructed byte for byte.
