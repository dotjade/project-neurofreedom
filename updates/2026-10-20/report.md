# Daily public evidence scan: 20 October 2026

## Finding

**No new-window qualifying primary tic-study result or newly posted relevant trial result was verified.** Eight PubMed records and 452 bioRxiv/medRxiv DOI/version records were screened. One ClinicalTrials.gov protocol posting was newly observed: [NCT07137442](https://clinicaltrials.gov/study/NCT07137442), posted October 19. Its estimated start moved from October 21 to October 22; selected recruiting status, observational design, planned enrollment and no-results flag were unchanged.

This is a bounded early-day check. A posting/date change is not an efficacy result, a confirmed start of recruitment or proof that any participants were assessed. Known negative findings and retraction exclusions remain in force.

## Scope, time and provenance

The current README.md, RESEARCH_PROTOCOL.md, STATUS.md and October 19 report were read through the GitHub connector before searching. Their exact blob identifiers are in [provenance.json](provenance.json). The latest decision remains the separate historical CM-aGPi methods/cohort audit; this scan does not reopen closed generic cohort searches.

Prior verified cutoff: **2026-10-19 03:09:45 UTC**. Core API requests ran **2026-10-20 02:49:03.544237–02:50:01.726379 UTC**. Supplementary API checks ran **02:52:42.101085–02:53:00.565490 UTC**, the final machine-timestamped API cutoff. Web discovery/direct-source checks ended within the observed **02:53:17 UTC** bracket; those tool calls do not expose second-precision request timestamps.

The overlap window is October 18–20 inclusive, with a narrower entry-date query for October 19–20. October 20 was only partly elapsed. Publication, database entry, metadata revision, preprint posting/version and registry posting dates are separate. No age, severity, language or human-only filter was used; persistent/severe adult burden and adverse or negative results were explicitly retained in the query scope.

[Search code](scan_sources.py), [exact query/request ledger](search-log.json), [supplementary source checks](supplement-selected-metadata.json), [web discovery log](discovery-log.json), [decision builder](build_results.py) and [summary](summary.json) support reproduction. Live APIs can change. Prior snapshots are comparison inputs, not a complete historical corpus.

## PubMed

Eight ESearch queries used retmax=1000; all returned counts were below the cap and all returned identifiers were fetched. They yielded **eight ID occurrences and eight unique records**, of which five overlap October 19. Publication types, publication/entry/revision dates, identifiers and linked notices were screened for all eight. The three newly encountered records received transient abstract review; full abstracts were not retained.

| Query family | Date field | Inclusive dates | Count |
|---|---|---|---:|
| Tourette OR "tic disorder" OR "tic disorders" | edat | October 18–20 | 0 |
| Same core | edat | October 19–20 | 0 |
| Same core | pdat | October 18–20 | 0 |
| Same core | mdat | October 18–20 | 7 |
| Core plus retraction/retracted/erratum/corrigendum/correction | edat | October 18–20 | 0 |
| tics OR "chronic motor tic" OR "chronic vocal tic" OR "persistent tic" | edat | October 18–20 | 1 |
| Same synonyms | pdat | October 18–20 | 0 |
| Core plus adult/severe/pain/burden/ADHD/comorbidity/treatment/adverse/negative/quality-of-life terms | edat | October 18–20 | 0 |

Exact Boolean strings and PubMed translations are preserved in the ledger. A zero notice-query result is not comprehensive publisher/Crossmark clearance and does not remove any historical retraction exclusion.

### Newly encountered secondary or historical material

- [PMID 41633747](https://pubmed.ncbi.nlm.nih.gov/41633747/), DOI 10.1016/B978-0-443-13554-5.00017-1: a review/chapter on functional tics and tic-like behaviors, indexed in February 2026. October 19 is a metadata revision, not new primary evidence. Functional tic-like presentations remain distinct from primary chronic tic disorders.
- [PMID 41779259](https://pubmed.ncbi.nlm.nih.gov/41779259/), DOI 10.1007/s11910-026-01480-8: a March 4 review of tic pathophysiology and management, revised in metadata October 19. Its discussion of developing treatments is not a new randomized result or demonstration of efficacy.
- [PMID 42726672](https://pubmed.ncbi.nlm.nih.gov/42726672/), DOI 10.1159/ene/acsag006: a September 11 historical/biographical article about Georges Guinon. It is not a new clinical experiment; October 19 is the metadata revision date.

The five prior overlaps are PMIDs 41621322, 41689912, 42890800, 42890894 and 42893364. Their linked-notice fields were unchanged. They comprise one historical pediatric obsessive-compulsive-symptom genetics paper, three reviews and one conceptual article. The genetic paper's UpdateOf link to PMID 40799755 remains a same-work preprint relationship, not independent replication.

[All screening decisions](pubmed-screening.jsonl) and [secondary/history records](secondary-screening.jsonl) are separate from the intentionally empty [new-primary ledger](primary-evidence.jsonl). No newly encountered review's underlying studies were added as independent primary evidence.

## Preprints

Official bioRxiv/medRxiv feeds were paginated for October 18–20. The case-insensitive title/abstract screen was `\btourett\w*|\btics?\b`.

- bioRxiv: **357 unique DOI/version pairs**, 12 pages; 61 overlap yesterday's bounded feed and 296 do not.
- medRxiv: **95 unique DOI/version pairs**, four pages; none overlap yesterday's bounded feed.
- **Zero lexical matches among 452 pairs.** These are all-subject postings/version records, not 452 tic studies.

Pagination covered the observed totals without duplicate DOI/version pairs. [bioRxiv index](biorxiv-preprint-index.tsv) and [medRxiv index](medrxiv-preprint-index.tsv) preserve dates and identifiers without abstracts. Feeds can change during pagination; synonym-only wording, other servers and later indexing remain gaps. Web discovery returned older preprints/reviews without a verified new-window version; they were not promoted to new primary evidence.

## Official registries and negative findings

ClinicalTrials.gov queried Tourette, tic disorder, Tics and ecopipam with `AREA[LastUpdatePostDate]RANGE[2026-10-18,2026-10-20]`, pageSize=100 and countTotal=true. Counts were **0, 1, 1 and 0**. The two occurrences deduplicate to one NCT identifier; no next-page token was supplied.

[NCT07137442](https://clinicaltrials.gov/study/NCT07137442) is an adult observational physiology protocol involving tics and functional tics. Compared with the prior direct snapshot, its estimated start changed **October 21 → October 22** and submission/posting dates advanced **October 15/16 → October 16/19**. Recruiting status, prospective observational design, estimated enrollment **75** and **hasResults=false** were unchanged. Ages 18–80 are eligibility limits, not observed participant ages. This is a selected-field snapshot comparison, not a full version-history or endpoint-amendment audit.

Three direct controls outside the update window also retained unchanged selected status/design/results fields:

- [NCT05158439](https://clinicaltrials.gov/study/NCT05158439): withdrawn for inability to recruit, actual enrollment zero, no results; last posting October 16. This is negative feasibility evidence, not a negative efficacy trial or evidence a cellular intervention was given.
- [NCT07093541](https://clinicaltrials.gov/study/NCT07093541): expanded access remains temporarily unavailable, no results; last posting October 14. No new suspension or cause is inferred.
- [NCT06194305](https://clinicaltrials.gov/study/NCT06194305): recruiting, no results; last posting July 22.

[Registry evidence and exact selected-field diffs](registry-evidence.jsonl) preserve these distinctions. The separate historical NCT05371041 result audit is not a new-window result and is not included in this scan's new-result count.

The documented ISRCTN XML query `(Tourette OR tics OR "tic disorder") AND lastEdited GE 2026-10-18T00:00:00 AND lastEdited LT 2026-10-21T00:00:00`, limit=50, returned HTTP 200 and **totalCount=0**. The undated Tourette control, limit=1, reported **22** matches; the direct SATURN control was retrievable. These controls demonstrate a functioning endpoint, not review of all 22 protocols.

WHO ICTRP's landing page was reachable and listed October 12 as its latest visible import; no usable query export was obtained. A gemlapodect mirror lead was checked against [official CTIS record 2023-505086-83-00](https://euclinicaltrials.eu/ctis-public/view/2023-505086-83-00), but the direct page yielded no readable record to this tool. Search snippets or mirror refresh dates cannot establish a new registry amendment or result. CTIS was not systematically enumerated; worldwide completeness is not claimed. Regulatory safety surveillance is reported separately.

## Interpretation and next gate

No source in this scan establishes a new treatment benefit, durable disease modification or a cure. Continue the already selected historical CM-aGPi primary-methods/cohort audit separately. New literature did not justify reopening closed generic access searches or changing the hypothesis portfolio.

This work used public metadata and original summaries only. No participant files, case narratives, private material, contact details, full abstracts or full papers are redistributed. No outreach, intervention, enrollment, account action or repository write occurred.

## Reproduce and validate

From this directory, run `python scan_sources.py --out .`, `python scan_supplement.py`, then `python build_results.py`. The supplementary script displays candidate abstracts transiently for screening; do not redirect that stdout to a public artifact. The decision builder encodes the documented source-screening decisions and checks the observed counts. Live-source reruns can legitimately differ and must be reviewed rather than forced to match.

For this execution, [validation.json](validation.json) records 11 passed consistency checks. Run `python validate_artifacts.py` for offline count, deduplication, selected-field-diff and manifest-hash validation without repeating external requests. These are bookkeeping checks, not independent scientific peer review. The [artifact manifest](manifest.json) identifies the publication files and their hashes; transient console output is excluded.
