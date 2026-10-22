# Daily public evidence scan: 22 October 2026

## Finding and decision

**No new qualifying primary tic-study outcome or newly posted relevant trial result was verified since the previous cutoff in this bounded scan.** The four PubMed candidates are all historical repository overlaps. Two known retraction records resurfaced because of metadata revision; they are not a newly issued retraction. One watched registry again moved an estimated start date, without results.

This does not alter today's separately scoped audit of Okun et al. 2024, PMID 38499664, DOI 10.1038/s41598-024-57071-5, NCT02056873. Keep the distinction between blinded stimulation-state comparisons, longitudinal tic changes and functional outcomes. This scan neither repeats that analysis nor reopens the closed generic adult-cohort search. No clinical action or treatment recommendation follows from a zero new-result count.

## Scope and dates

The current README, research protocol, STATUS, public journal source README, October 21 scan and relevant evidence were read first at repository commit `c9314ae695c3b5624f5049a3d819fef922ebe14b`. [Provenance and hashes](provenance.json) identify the exact source snapshot.

- Prior strict cutoff: **2026-10-21 02:57:34.629924 UTC**.
- Current core API requests: **2026-10-22 02:58:39.764722 to 03:00:44.969432 UTC**.
- Official supplementary registry checks: **02:59:05.882179 to 02:59:12.802907 UTC**.
- Inclusive overlap queries: **October 20 to 22**, plus a narrower October 21 to 22 entry-date query. October 22 was only partly elapsed. The [web discovery ledger](discovery-log.json) gives its separate query brackets and access limits.

No age, severity, language or human-only filter was applied. Persistent severe adult symptoms, pain, functional burden, co-occurring conditions, unmet treatment needs and negative findings remain in scope alongside pediatric studies. Developmental improvement and remission are not assumed for everyone. Publication, database entry, metadata revision, registry posting and preprint-version dates are different events. A future planned start/completion or a search-engine crawl date is not evidence that a trial ran or reported results.

## PubMed: four historical records, no new outcome

Eight exact ESearch queries yielded **four ID occurrences and four unique records**. All were retrieved through EFetch for date/type/linked-notice screening; two overlap October 21 and two overlap the October 17 to 18 integrity records. All counts were below `retmax=1000`.

| Query | Field | Inclusive interval | Count |
|---|---|---|---:|
| Tourette OR "tic disorder" OR "tic disorders" | edat | October 20 to 22 | 0 |
| Same core | edat | October 21 to 22 | 0 |
| Same core | pdat | October 20 to 22 | 0 |
| Same core | mdat | October 20 to 22 | 4 |
| Core plus retraction/retracted/erratum/corrigendum/correction | edat | October 20 to 22 | 0 |
| tics OR "chronic motor tic" OR "chronic vocal tic" OR "persistent tic" | edat | October 20 to 22 | 0 |
| Same synonyms | pdat | October 20 to 22 | 0 |
| Core plus adult/severe/pain/burden/ADHD/comorbidity/treatment/adverse/negative/quality-of-life terms | edat | October 20 to 22 | 0 |

[Exact strings, translations and counts](search-log.json), [timestamped request metadata](request-log.json) and [all screening decisions](pubmed-screening.jsonl) are retained. The new-primary-outcome ledger, [primary-evidence.jsonl](primary-evidence.jsonl), is intentionally empty.

- [PMID 39947542](https://pubmed.ncbi.nlm.nih.gov/39947542/), DOI 10.1016/j.ijbiomac.2025.140956, remains explicitly retracted. The February 2025 preclinical paper is excluded from positive mechanism or efficacy evidence.
- Its [notice, PMID 42527169](https://pubmed.ncbi.nlm.nih.gov/42527169/), DOI 10.1016/j.ijbiomac.2026.153656, was electronically published July 29, 2026; October is its issue date. Compared with the October 18 snapshot, the duplicate ErratumIn/ErratumFor cross-links are no longer returned, and the notice type now includes Journal Article rather than Published Erratum. RetractionIn/RetractionOf and Retraction Notice remain. This is a metadata change, not a new retraction or reinstatement. The reason for retraction was not independently verified. [Exact differences](integrity-recheck.json). Retraction does not by itself falsify the biological mechanism.
- [PMID 41220182](https://pubmed.ncbi.nlm.nih.gov/41220182/), DOI 10.1002/brb3.71041, is the November 2025 rat-model study already screened yesterday. October 20 is a metadata-revision date, not a new experiment. No human efficacy inference is made.
- [PMID 41794658](https://pubmed.ncbi.nlm.nih.gov/41794658/), DOI 10.1186/s12888-026-07932-2, is a March 2026 scoping review of functional-tic comorbidity, also screened yesterday. It is secondary evidence and does not supply a new independent chronic-tic cohort.

The retracted paper's abstract was transiently available during retrieval and was not retained or used as positive evidence; no notice abstract was returned. The two yesterday-overlap abstracts were not re-extracted. Linked PubMed notices are not an exhaustive publisher/Crossmark review.

## Preprints and supplementary discovery

The official bioRxiv/medRxiv feeds were fully paginated for October 20 to 22 as observed, without request errors or changing reported totals:

| Server | DOI/version pairs | Pages | In prior bounded feed | Not in prior bounded feed |
|---|---:|---:|---:|---:|
| bioRxiv | 453 | 16 | 201 | 252 |
| medRxiv | 186 | 7 | 71 | 115 |

The case-insensitive title/abstract expression `\btourett\w*|\btics?\b` matched **one of 639 pairs**. DOI **10.64898/2026.06.25.734531**, version 2 dated October 21, is prostate-cancer metabolic modeling. Its abbreviation TICs means thermodynamically infeasible cycles, not movement or vocal tics. It was excluded after transient abstract review. These are 639 all-subject posting/version records, not 639 tic studies. [bioRxiv identifiers](biorxiv-preprint-index.tsv), [medRxiv identifiers](medrxiv-preprint-index.tsv).

Six supplementary search queries returned 36 displayed cards across two combined batches, not complete engine hit counts or unique studies. They surfaced older primary papers, reviews, preprints and protocols, with no verified since-cutoff tic outcome. Automatically returned community/recruitment material was excluded without retaining identifiable content or treating it as scientific evidence. The [ledger](discovery-log.json) records primary/official links, classifications and access limits. An official publisher search card described an October 15 correction to a prior review, but direct retrieval was access-limited; it is neither a new-window correction nor independently reverified full text. Other preprint servers and synonym-only abstracts remain coverage gaps.

## Official registries and preserved negative evidence

ClinicalTrials.gov used **server-side selected-field projection** excluding result measurements, contacts, officials and locations. Tourette, tic disorder, Tics and ecopipam queries with `AREA[LastUpdatePostDate]RANGE[2026-10-20,2026-10-22]` returned **0, 1, 1 and 0**, deduplicating to **NCT07137442**, with no next page token. Four direct controls were also retrieved. [Current selected fields and differences](registry-evidence.jsonl).

- [NCT07137442](https://clinicaltrials.gov/study/NCT07137442): estimated start October 25 to **October 26**; posting October 20 to **October 21**; submission October 19 to **October 20**. Recruiting status, observational design, planned enrollment 75, eligibility ages 18 to 80 and absence of results persist. Eligibility is not an observed age distribution. This is not a verified recruitment event, efficacy outcome or full amendment-history audit.
- [NCT05158439](https://clinicaltrials.gov/study/NCT05158439): withdrawn for inability to recruit, actual enrollment zero and no results. Preserve negative feasibility, not negative efficacy or evidence of cell administration.
- [NCT07093541](https://clinicaltrials.gov/study/NCT07093541): expanded access remains temporarily unavailable without results. No new suspension or cause is inferred.
- [NCT06194305](https://clinicaltrials.gov/study/NCT06194305): pediatric CBIT study remains recruiting without results. Selected status/design/results fields are unchanged.

The ISRCTN XML query for tic terms with `lastEdited GE 2026-10-20T00:00:00 AND lastEdited LT 2026-10-23T00:00:00` returned HTTP 200 and **totalCount=0**. An undated Tourette control returned **totalCount=22**, but only one control record was requested; this is not a review of all 22. WHO ICTRP's landing page was reachable and still listed October 12 as its latest visible import; no usable query export was obtained. The official CTIS gemlapodect URL returned an HTML application shell, not an interpreted trial record. [Supplementary source log](supplement-selected-metadata.json). Worldwide registries were not exhaustively enumerated.

## Limits, safety and reproducibility

The separate [safety pass](safety/report.md) records regulator coverage and its own limits. This scan makes no claim that absence of a verified notice means absence of risk. Index lag, partial-day coverage, limited search vocabulary, unavailable full methods and non-enumerated registries constrain the negative finding. No participant rows, raw physiological signals, private narratives, contacts, full abstracts or full papers are publication artifacts. No data-access request, outreach, recruitment, paid compute or medical intervention occurred.

To repeat the live scan, use a checkout of the cited base commit:

```sh
python prepare_baseline.py --repo /path/to/base-checkout --out /tmp/neurofreedom-baseline.json
python scan_sources.py --baseline /tmp/neurofreedom-baseline.json --out /tmp/neurofreedom-live-scan
python scan_supplement.py
python build_results.py --raw /tmp/neurofreedom-live-scan/search-log.json --repo /path/to/base-checkout --out /tmp/neurofreedom-reviewed-scan
```

Live results may change. `build_results.py` encodes today's reviewed decisions and intentionally requires review if new IDs appear. `scan_supplement.py` writes beside its script, so copy it into a temporary run directory when reproducing rather than overwriting this dated snapshot. `python validate_artifacts.py --repo /path/to/base-checkout` checks the saved counts, identifier deduplication, overlap, metadata deltas, projection boundary and artifact hashes without external requests. These are documentation checks, not clinical hypothesis tests or independent peer review. Prior baseline bodies are not duplicated in this update.
