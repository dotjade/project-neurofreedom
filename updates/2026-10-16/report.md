# Project NeuroFreedom daily public evidence scan

16 October 2026 | Core API retrievals 02:42:38–02:43:55 UTC; supplementary verification through approximately 02:46:43 UTC. Safety retrievals are recorded separately.

## Result

One new primary report was verified: **a qualitative interview study of 34 adults with Tourette syndrome, published 15 October**. It addresses stigma, relationships and employment. It strengthens the adult-burden evidence map, but does not measure treatment efficacy or validate a causal life-course model. Main methods, severity coverage and cohort overlap remain unverified.

One already-known adult physiology study has an October 15 registry posting without results. Its estimated start moved from October 19 to October 20 in the retrieved snapshots. The ecopipam expanded-access record remains a duplicate October 14 posting.

Eight PubMed queries returned 18 ID occurrences and 13 unique records. Twenty-one official bioRxiv/medRxiv API pages returned 601 distinct DOI/version records, with zero tic-keyword matches. No additional qualifying notice for the original FDA/EMA/MHRA tic-product watchlist was verified; FDA retrieval gaps qualify that negative. One verified MHRA antidepressant communication is retained separately as material comorbidity-care context. See the [separate safety report](safety/report.md). These bounded findings do not establish absence of relevant evidence worldwide.

## Baseline, scope and dates

Read the current README, RESEARCH_PROTOCOL, STATUS, primary ledger, October 15 report and safety report, plus the prior search and registry ledgers. [Baseline metadata](baseline-metadata.json) retain blob identifiers and compact deduplication keys rather than prior-report payloads. The attempted prior code path `updates/2026-10-15/scan.py` did not exist; this run uses its own preserved [source-search script](scan_sources.py).

The prior core scan ended October 15 at 03:00:45 UTC, with supplementary checks through approximately 03:02. Current inclusive date filters cover October 14–16, with a nested October 15–16 entry-date check. October 16 was only partly elapsed. Publication, PubMed/Entrez entry, metadata revision, PMC release, preprint-version posting and registry posting are distinct. Crossref registration is not exact first-publication timing.

No age, severity, language, human-only or design restriction was applied to the core queries. An adult/severe/pain/burden/comorbidity/treatment/negative-findings supplement was included. Persistent severe adult symptoms and functional/social burden remain central; a study of adults does not automatically represent people with sustained severe symptoms.

## Literature

PubMed ESearch used `db=pubmed`, `retmode=json`, `retmax=1000`; every observed count was below the cap. Exact queries, translations, retrieval UTC times, hashes, identifiers and decisions appear in [search-log.json](search-log.json). Core query: `Tourette OR "tic disorder" OR "tic disorders"`. Synonyms: `tics OR "chronic motor tic" OR "chronic vocal tic" OR "persistent tic"`.

| Query | Date field | Inclusive window | Returned |
|---|---|---|---:|
| Core | edat | October 14–16 | 1 |
| Core, nearer window | edat | October 15–16 | 1 |
| Core | pdat | October 14–16 | 2 |
| Core | mdat | October 14–16 | 11 |
| Core + notice terms | edat | October 14–16 | 0 |
| Synonyms | edat | October 14–16 | 1 |
| Synonyms | pdat | October 14–16 | 1 |
| Adult/burden/treatment supplement | edat | October 14–16 | 1 |

All 13 records received date/type/identifier/linked-notice screening. Nine IDs were not in yesterday's retrieved set and also received abstract review; four overlapped. No changed linked-notice field was found among overlaps. This is not full-text review of all records or complete publisher/Crossmark clearance.

### New adult qualitative evidence

[Chen et al., PMID 42875858](https://pubmed.ncbi.nlm.nih.gov/42875858/), [DOI 10.1097/ANS.0000000000000710](https://doi.org/10.1097/ANS.0000000000000710), is an original qualitative study based on interviews with 34 adults. Participants described stigma shaping identity, relationships and work, alongside coping, concealment and withdrawal. These themes are relevant to research on adult participation and social burden, independently of tic-score change.

The publisher labels it Original Article, Publish Ahead of Print, October 15. PubMed and Crossref corroborate that date. Crossref creation was October 15 at 04:01:16 UTC; PubMed history reports 07:18 and Entrez 00:41 without explicit timezones. These are different metadata events, and do not resolve the exact first-publication time. The report was absent from the prior query set and current primary ledger; three default-branch PMID/DOI/title searches returned no match.

Only the abstract and public publisher overview were inspected. Recruitment, geography, age distribution, severe/persistent symptoms, comorbidity coverage, interview/coding procedures, reflexivity, saturation, negative cases, funding and overlapping cohorts require verification. A life-course interpretation does not establish prospective longitudinal follow-up. The sample cannot supply population prevalence or intervention-effect estimates; proposed support approaches were not tested here. [Structured extraction](primary-evidence.jsonl) retains these limits without personal narratives or participant details.

### Exclusions and metadata-only returns

- [PMID 42875818](https://pubmed.ncbi.nlm.nih.gov/42875818/), DOI 10.1111/jgs.70797, is an October 14 cognitive-aging cohort. Here TICS means Telephone Interview for Cognitive Status, not tic disorders; excluded as an acronym collision.
- [PMID 42808868](https://pubmed.ncbi.nlm.nih.gov/42808868/), DOI 10.3238/arztebl.m2026.0156, is an adult-OCD narrative review. PubMed labels electronic/issue date October 16 but entry September 29. It is secondary evidence, and first public availability is not resolved from these fields.
- Six other newly returned IDs are older publications: functional-tic diagnostic review (38940477, June 28, 2024); adult video classification (38973244, July 7, 2024); child/adult symptom networks (39054607, July 25, 2024); adolescent HRV/QoL (40215249, April 11, 2025); unrelated sarcopenia (40759914, August 4, 2025); and a conceptual consciousness article (41151214, October 27, 2025). Their recent modification dates do not make them new studies.

No completed generic cohort, MNS, gating-access, endpoint-threshold or attrition analysis was repeated. Older relevant adult evidence is preserved in screening metadata without relabelling it an incremental discovery.

## Preprints

Official endpoint: `https://api.biorxiv.org/details/{server}/2026-10-14/2026-10-16/{cursor}`. Case-insensitive title/abstract screen: `\btourett\w*|\btics?\b`.

- bioRxiv: 15 pages; 443 distinct DOI/version pairs; final cursor 420 returned 23. Reported total remained 443, with new-paper count 348. There were 216 pairs overlapping yesterday's set and 227 not in it.
- medRxiv: 6 pages; 158 pairs; final cursor 150 returned 8. Reported total remained 158, with new-paper count 128. There were 83 overlaps and 75 pairs not in yesterday's set.
- Zero lexical matches across 601 pairs. These are all-subject postings/versions, not 601 tic papers. Observed pages were fully enumerated; live feeds are not a frozen census, and relevant work without the chosen words or on other servers can be missed.

## Official registries

ClinicalTrials.gov used `AREA[LastUpdatePostDate]RANGE[2026-10-14,2026-10-16]`, page size 100 and total-count requests. Condition searches Tourette, tic disorder and Tics, plus the ecopipam term query, returned 1, 2, 2 and 1 records. Six occurrences deduplicate to two records; no next-page tokens were returned. See [registry evidence](registry-evidence.jsonl) and [selected prior fields](prior-registry-selected-fields.json).

- [NCT07137442](https://clinicaltrials.gov/study/NCT07137442): existing adult observational physiology study, Recruiting, planned N=75 aged 18–80, no results. Update submitted October 14 and posted October 15. Estimated start changed from October 19 to October 20; other compared status fields were unchanged. The registered two-day EEG endpoint is not a treatment outcome, and recruitment plus a future estimate does not establish that testing has begun. This is a selected-field comparison, not a complete history audit.
- [NCT07093541](https://clinicaltrials.gov/study/NCT07093541): ecopipam expanded-access record retains its October 14 posting, current `TEMPORARILY_NOT_AVAILABLE` status and no results. No selected status/date field changed. The timing or reason for unavailability remains unresolved; no new closure or safety suspension is inferred.

WHO ICTRP's landing page was readable today and lists October 12 as the latest import for several major contributing registries, before this incremental window. No usable search export was obtained. ISRCTN search was inaccessible; CTIS returned a page shell without results. Domain-limited discovery and the previously audited ReBEC RBR-10rvhk97 record did not establish a new posting; its registration/last-approval date remains July 21. This is incomplete worldwide registry coverage.

## Consequence and limits

The new qualitative study is a directly relevant adult-burden source, separate from the historical randomized functioning analysis. A bounded next source check would establish recruitment, severe/comorbid representation, analytic rigor and cohort overlap through lawful methods/supplement access. Its model should remain provisional until that check; no treatment or participant-study proposal follows automatically.

[Supplementary source checks](source-checks.json) document web-extractor failures, successful official API/publisher retrievals, deduplication and search noise. The verified October 15 MHRA antidepressant communication concerns clearer information about established risks. The safety report preserves its relevance to comorbidity care separately from the original tic-product watchlist. Safety coverage is incomplete, particularly for FDA recall listings.

No participant data, individual/family stories, contact details, outreach, account action, trial enrollment, medical intervention, purchase, paid computation or repository commit occurred. Only original summaries, bibliographic/protocol metadata, links and reproducible search code are retained. No abstracts, full papers or raw source HTML/XML are redistributed. No cure or disease-modification claim follows.
