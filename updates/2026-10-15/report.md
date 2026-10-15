# Project NeuroFreedom daily public evidence scan

15 October 2026 | Core API retrievals 02:58:45–03:00:45 UTC; supplementary source checks 02:57–03:02 UTC. Safety retrievals are logged separately.

## Result

One newly encountered primary study was verified: a pediatric cross-sectional allergy/tic-severity report first published **13 October**, not today. It adds an association worth checking, not evidence that allergy causes tics or that treating allergy improves tics. It provides no persistent-severe-adult estimate.

Two existing ClinicalTrials.gov records have October 14 postings, neither with results: an ecopipam expanded-access program currently marked **Temporarily not available**, and the previously recorded adult physiological study. The latter's estimated start moved from October 18 in yesterday's stored snapshot to October 19. These are registry observations, not newly demonstrated treatment effects.

Eight PubMed queries returned 15 ID occurrences and 11 unique metadata records. Twenty-four official bioRxiv/medRxiv API pages returned 684 unique DOI/version records with zero tic-keyword matches. No qualifying newly first-published October 14–15 primary paper or additional watched FDA/EMA/MHRA safety notice was verified. See the [safety report](safety/report.md) for the separate regulator check. None of these bounded negatives establishes absence of relevant evidence worldwide.

## Baseline, dates and scope

Read the current README, RESEARCH_PROTOCOL, STATUS, evidence.jsonl, October 14 report, search ledger and safety report using GitHub. Their blob identifiers and links are retained in [baseline-metadata.json](baseline-metadata.json). The initially requested root path `safety/report.md` returned 404; the linked correct path was `updates/2026-10-14/safety/report.md` and was read successfully.

Incremental comparison: October 14 API retrievals 02:46:32–02:51:03 UTC, with safety checked separately through 02:49:22 UTC. Inclusive overlap filters cover October 13–15; the nested entry-date query covers October 14–15. October 15 was only partly elapsed. Publication, PubMed/Entrez entry, metadata revision, PMC release, preprint version posting and registry posting are different dates. Search freshness labels are not evidence of source publication.

Core searches imposed no age, severity, language, human-only or design restrictions. A supplemental adult/severe/pain/burden/comorbidity/treatment/negative-findings query was included. The pediatric finding does not replace the adult-persistence priority. No closed generic cohort, MNS, gating-access, registry-endpoint or measurement-threshold analysis was repeated.

## Literature

PubMed ESearch used `db=pubmed`, `retmode=json`, `retmax=1000`; all counts were below the retrieval cap. Exact queries, translations, URLs, UTC timestamps, response hashes and screening decisions are in [search-log.json](search-log.json), with supplementary access/deduplication checks in [source-checks.json](source-checks.json). Core: `Tourette OR "tic disorder" OR "tic disorders"`. Synonyms: `tics OR "chronic motor tic" OR "chronic vocal tic" OR "persistent tic"`.

| Query | Date field | Inclusive window | Returned |
|---|---|---|---:|
| Core | edat | October 13–15 | 1 |
| Core, nearer window | edat | October 14–15 | 0 |
| Core | pdat | October 13–15 | 1 |
| Core | mdat | October 13–15 | 10 |
| Core + notice terms | edat | October 13–15 | 0 |
| Synonyms | edat | October 13–15 | 1 |
| Synonyms | pdat | October 13–15 | 1 |
| Adult/burden/treatment supplement | edat | October 13–15 | 1 |

All 11 records received date/type/identifier/linked-notice metadata screening. Four records were not in yesterday's retrieved set and their abstracts were inspected; seven overlap. This is not full-text review of all 11. No changed linked-notice field was found among overlaps; the focused correction/retraction query returned zero. This does not replace a complete publisher/Crossmark or retraction-history audit.

### Newly encountered primary evidence

[Lin et al., DOI 10.1007/s00431-026-07510-4](https://link.springer.com/article/10.1007/s00431-026-07510-4), [PMID 42867549](https://pubmed.ncbi.nlm.nih.gov/42867549/), studies 136 children aged 4–13: 76 with tic disorders alone and 60 with associated allergic disease. Its composite allergy index is associated with a 2.66-point higher YGTSS total-tic score per one-standard-deviation increase (p<.001). The abstract also reports greater functional impairment in the allergy group, without an effect estimate or interval.

Publisher metadata and PubMed agree on online publication October 13; the publisher assigns a November issue. PubMed history gives October 13 at 23:36 and Entrez October 13 at 17:11, without an explicit timezone. Yesterday's ledger returned no October 13–14 core entry-date records. Thus this is newly encountered in the actual query returns, **not proven to have first appeared after yesterday's scan**; indexing/query-membership latency cannot be resolved from these records.

The accessible publisher overview corroborates the abstract and says only complete YGTSS/allergy records were analyzed, without imputation. Full methods/tables were not available in this pass; a linked supplement was identified but not inspected. Confidence intervals, adjustment variables, exact index formula, recruitment flow, medication handling and potential cohort overlap remain unresolved. Cross-sectional associations do not identify temporal order or causal effects. Do not reconstruct precision from the threshold p value, infer allergy-treatment benefit, or generalize to adults. The study belongs in the primary-study ledger with its access and applicability limits; the [structured extraction](primary-evidence.jsonl) preserves those distinctions.

### Other newly returned records

- PMID [42867542](https://pubmed.ncbi.nlm.nih.gov/42867542/), DOI 10.1007/s00431-026-07466-5: October 13 rapid review of functional cough and proposed phenotypes. It is secondary evidence, not a new primary tic trial; direct pediatric evidence is described as limited. Excluded from primary additions.
- PMID [38945036](https://pubmed.ncbi.nlm.nih.gov/38945036/), DOI 10.1016/j.pediatrneurol.2024.05.001: pediatric sleep report first online May 7, 2024. Its October 13, 2026 PMC-release and October 14 metadata-revision fields do not make it new research.
- PMID [40169089](https://pubmed.ncbi.nlm.nih.gov/40169089/), DOI 10.1016/j.neubiorev.2025.106130: review first online March 30, 2025; October 14 metadata revision, not a new primary study.

Default-branch GitHub searches for PMID 42867549, DOI suffix 07510-4 and “Allergic load” each returned zero. The complete current primary ledger and previous scan were also checked. Search-index absence is not an exhaustive repository-history audit; no independent-cohort claim is made.

## Preprints

Official API interval: `https://api.biorxiv.org/details/{server}/2026-10-13/2026-10-15/{cursor}`. Case-insensitive title/abstract screen: `\btourett\w*|\btics?\b`.

- bioRxiv: 17 pages, 498 distinct DOI/version pairs; final cursor 480 returned 18. Stable reported total 498, new-paper count 384. There were 226 overlaps with yesterday's retrieved set and 272 pairs not in that set.
- medRxiv: 7 pages, 186 distinct DOI/version pairs; final cursor 180 returned 6. Stable reported total 186, new-paper count 150. There were 93 overlaps and 93 pairs not in yesterday's set.
- Zero lexical matches across 684 pairs. These are all-subject posting/version records, not 684 tic studies. The observed responses were fully paginated; live feeds are not a frozen census. Other servers, later postings and relevant titles/abstracts without these words remain outside coverage.

## Registry updates

ClinicalTrials.gov API used `AREA[LastUpdatePostDate]RANGE[2026-10-13,2026-10-15]`, page size 100 and total-count requests. Condition searches Tourette, tic disorder and Tics, plus a term search ecopipam, returned 1, 2, 2 and 1 records respectively. Six occurrences deduplicate to two studies; no next-page token was returned. Details are in [registry-evidence.jsonl](registry-evidence.jsonl).

### NCT07093541: current expanded-access availability

[The Emalex ecopipam expanded-access record](https://clinicaltrials.gov/study/NCT07093541) was first posted July 30, 2025; this update was submitted October 8 and posted October 14, 2026. Current status is `TEMPORARILY_NOT_AVAILABLE`; status-verified month remains March 2026. **Do not describe this as an October 14 closure or suspension:** historical changed fields were not recovered, so the timing or reason for that status is unverified.

The registered age range is 6–50. Its open-label program is intended for people unable to use approved/D2-antagonist treatments because of failure, tolerability, safety or access problems, with safety and patient-reported outcomes including quality of life. It has no comparator, posted results or enrollment count in the inspected design module. Medical, psychiatric and medication exclusions and the age ceiling limit applicability. The record is not evidence of approval, availability to a particular person, efficacy, or a new safety signal. No enrollment or contact was attempted.

### NCT07137442: observed snapshot change

[The NINDS adult physiological study](https://clinicaltrials.gov/study/NCT07137442) remains Recruiting, with 75 planned adults aged 18–80 and no results. Update submitted October 13 and posted October 14. The current estimated start is October 19; yesterday's original extraction recorded October 18. This is a verified difference between retrieved snapshots, not a complete field-history audit. The two-day primary EEG measure, future estimated start and ongoing recruitment are distinct from a treatment outcome or confirmation that testing has begun. The previously noted healthy-volunteer flag/narrative discrepancy remains.

Registry history pages were sparse or inaccessible to the web extractor. WHO ICTRP was inaccessible. Domain-limited ISRCTN, CTIS/legacy EU and ReBEC searches provided discovery only, not a complete export or worldwide history comparison. The already-audited ReBEC RBR-10rvhk97 record reappeared with July registration/approval dates and was not counted as a new October result.

## Research consequence and limits

Keep the new pediatric association separate from the adult CBIT-maintenance investigation. A possible next source-verification step is the allergy paper's public supplement/methods, conditional on lawful access, to establish adjustment, composite construction, precision and cohort selection before any causal discussion. It is not a reason to initiate allergy testing, elimination diets, medication changes or a home experiment.

No participant data, individual/family narratives, outreach, data-access request, account action, trial enrollment, treatment, purchase, paid computation or public collection occurred. Only original summaries, bibliographic/protocol metadata, source links and reproducible search code are retained. Scientific full text, copied abstracts, raw HTML/XML and contact details are not redistributed. No claim of cure or disease modification follows.
