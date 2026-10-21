# Daily public evidence scan: 21 October 2026

## Finding

**No new qualifying primary tic-study outcome, newly posted relevant trial result or additional watched-treatment regulator warning was verified since the previous cutoff.** This is not an unqualified “no new primary evidence” claim: the overlapping search newly encountered one adjacent primary MRI-methods paper, which has no Tourette cohort and predates the strict cutoff. A historical rat study and a functional-tic review also surfaced through metadata revision.

One newly observed registry posting is substantive only as a protocol-date update: [NCT07137442](https://clinicaltrials.gov/study/NCT07137442) now estimates its start on October 25 rather than October 22. Recruiting status, observational design, planned enrollment of 75 and absence of results are unchanged. A planned date is not a verified recruitment event or treatment outcome.

## Scope, dates and provenance

The current README, research protocol, status and October 20 report and source logs were read before searching. Repository source commit: `81feefe52fa1a401b01fd51ee8950a5e4de4a9ae`; hashes are in [provenance.json](provenance.json).

- Prior main scan: API cutoff **2026-10-20 02:53:00.565490 UTC**, final web-check bracket **02:53:17 UTC**. The latter is the strict comparison cutoff here.
- Current core API requests: **2026-10-21 02:50:26.582445–02:51:07.315339 UTC**. Supplementary registry checks ended **02:51:14.112838 UTC**. Feed recovery ended **02:55:27.270525 UTC**; the final publisher-date check ended **02:57:34.629924 UTC**, the main scan's final machine-timestamped cutoff.
- Search overlap: **October 19–21 inclusive**, with an additional October 20–21 entry-date query. October 21 was only partly elapsed. Safety has its own documented interval, ending **02:52:58.744651 UTC**.

No age, severity, language or human-only restriction was applied. Persistent severe adult symptoms, pain, functional burden, co-occurring conditions, unmet treatment needs and negative findings remain explicitly in scope alongside children. Database entry, publication, metadata revision, preprint version and registry posting dates are not interchangeable. Later or future-dated index material cannot establish evidence available by this cutoff; expected completion dates never count as results.

## PubMed and adjacent primary evidence

Eight ESearch queries returned **11 ID occurrences, eight unique records and five overlaps** with yesterday's bounded scan. All IDs were fetched; counts were below `retmax=1000`. All eight received metadata/type/date/notice screening, and the three newly encountered IDs received transient abstract review.

| Query family | Date field | Inclusive dates | Count |
|---|---|---|---:|
| Tourette OR “tic disorder” OR “tic disorders” | edat | October 19–21 | 1 |
| Same core | edat | October 20–21 | 0 |
| Same core | pdat | October 19–21 | 1 |
| Same core | mdat | October 19–21 | 8 |
| Core plus retraction/retracted/erratum/corrigendum/correction | edat | October 19–21 | 0 |
| tics OR “chronic motor tic” OR “chronic vocal tic” OR “persistent tic” | edat | October 19–21 | 0 |
| Same synonyms | pdat | October 19–21 | 0 |
| Core plus adult/severe/pain/burden/ADHD/comorbidity/treatment/adverse/negative/quality-of-life terms | edat | October 19–21 | 1 |

Exact strings, translations, timestamps and source-response hashes are in [search-log.json](search-log.json). [PubMed screening](pubmed-screening.jsonl) records every decision. The [new qualifying primary tic-outcome ledger](primary-evidence.jsonl) is intentionally empty; that does not erase the adjacent or historical primary work below.

### Newly encountered imaging-methods lead, not a tic-treatment result

[PMID 42896917 / DOI 10.3174/ajnr.A9681](https://pubmed.ncbi.nlm.nih.gov/42896917/) compares centromedian-nucleus MRI visualization across separate cohorts: QSM in 24 people with cavernous malformations, white-matter-null imaging in 16 with epilepsy, and MP2RAGE in 24 healthy people. No Tourette cohort is described. The abstract reports better lateral contrast with QSM but lower overall signal-to-noise. Independent cohort differences confound sequence comparisons; this does not establish targeting accuracy, tic prediction or clinical benefit.

PubMed/Crossref list October 19; PubMed's entry history is October 19 at 20:54, with no time zone specified. The [publisher DOI route](https://doi.org/10.3174/ajnr.A9681) resolves to an October 15 URL and exposes October 15 publication metadata alongside an October 19 DC.Date. The date discrepancy remains unresolved; both precede the strict cutoff. Its absence from yesterday's results does not prove why indexing differed. Retain as **newly encountered adjacent technical primary evidence**, not a newly published since-cutoff result. Full methods were not audited. [Extraction](adjacent-evidence.jsonl), [selected checks](selected-candidate-checks.json) and [date check](publisher-date-check.json).

### Other newly encountered records

- [PMID 41220182](https://pubmed.ncbi.nlm.nih.gov/41220182/), DOI 10.1002/brb3.71041, is a November 2025 IDPN rat-model study of jujuboside A/tiapride and striatal transmitter/behavior measures. October 20 is metadata revision, not a new experiment. Animal stereotypy does not establish human tic efficacy or justify treatment. [Historical preclinical record](historical-preclinical.jsonl).
- [PMID 41794658](https://pubmed.ncbi.nlm.nih.gov/41794658/), DOI 10.1186/s12888-026-07932-2, is a March 2026 functional-tic comorbidity scoping review, revised in metadata October 20. It is secondary evidence; its underlying studies were not added as independent new cohorts. Functional tic-like presentations remain distinct from primary chronic tic disorders.

Five overlaps are PMIDs 41633747, 41779259, 42726672, 42890800 and 42890894. Their linked-notice fields were unchanged. No linked PubMed notice or Crossref update relation was returned for the adjacent imaging paper, but this is not comprehensive publisher/Crossmark clearance. Historical retraction exclusions remain in force; a zero new notice count cannot rehabilitate a retracted finding.

## Preprints and discovery checks

Official bioRxiv/medRxiv date feeds were fully paginated for October 19–21 as observed:

| Server | DOI/version pairs | Pages | Overlap with prior scan | Not in prior bounded feed |
|---|---:|---:|---:|---:|
| bioRxiv | 486 | 17 | 254 | 232 |
| medRxiv | 166 | 6 | 95 | 71 |

The case-insensitive title/abstract expression `\btourett\w*|\btics?\b` matched **zero of 652 pairs**. These are all-subject postings/version records, not 652 tic studies. Totals stayed at 486 and 166; no duplicate DOI/version pair was recorded. [Indexes](biorxiv-preprint-index.tsv) and [medRxiv index](medrxiv-preprint-index.tsv) retain identifiers/dates without abstracts.

The first workers stopped before feed requests because prior publication logs stored their version indexes separately. Restoring the baseline from prior TSVs resolved that schema error. The subsequent pass timed out at cursor 60 on each server; a logged resume with a 60-second timeout completed all remaining pages without further errors. [Initial feed pass](preprint-search-log.json), [completed resume](preprint-resume-log.json). These failures were recovered, not silently counted as zero matches or complete coverage.

Six supplementary web queries returned 30 displayed cards in two batches; these are not complete engine hit counts. Historical trials, protocols, reviews, unrelated disorders and imaging leads were excluded from new-outcome counts. Search crawl labels did not establish new publication or preprint versions. [Discovery ledger](discovery-log.json). Other preprint servers and synonym-only abstracts remain gaps.

## Official registries and preserved negative evidence

ClinicalTrials.gov queries for Tourette, tic disorder, Tics and ecopipam with `AREA[LastUpdatePostDate]RANGE[2026-10-19,2026-10-21]` returned **0, 1, 1 and 0**. The two occurrences deduplicate to **NCT07137442**, with no further page token. Its posting changed October 19→20, submission October 16→19 and estimated start October 22→25. Direct recheck corroborated the selected fields. Eligibility is ages 18–80, not an observed sample-age distribution. This is not a complete version-history or endpoint-amendment audit.

Three direct controls outside the update window retained unchanged selected status/design/results fields:

- [NCT05158439](https://clinicaltrials.gov/study/NCT05158439): withdrawn for inability to recruit, actual enrollment zero, no results. Negative feasibility is not negative efficacy or evidence of cellular administration.
- [NCT07093541](https://clinicaltrials.gov/study/NCT07093541): expanded access temporarily unavailable, no results. No new suspension or reason is inferred.
- [NCT06194305](https://clinicaltrials.gov/study/NCT06194305): recruiting pediatric CBIT study, no results.

[Registry records and exact selected-field differences](registry-evidence.jsonl) preserve these distinctions. The historical NCT05371041 aggregate crosswalk is a separate task, not a new-window result in this count.

ISRCTN's XML query `(Tourette OR tics OR "tic disorder") AND lastEdited GE 2026-10-19T00:00:00 AND lastEdited LT 2026-10-22T00:00:00`, limit 50, returned HTTP 200 and **totalCount=0**. The undated Tourette control reported **22**, and the direct SATURN control was retrievable; this does not mean all 22 protocols were reviewed. [Supplementary source log](supplement-selected-metadata.json).

WHO ICTRP's landing page was reachable and still listed October 12 as its latest visible import, but no usable query export was obtained. The official [CTIS gemlapodect record](https://euclinicaltrials.eu/ctis-public/view/2023-505086-83-00) returned its application shell without an interpreted trial record. Neither CTIS nor worldwide registries were exhaustively enumerated.

## Safety and decision

The [separate safety pass](safety/report.md) screened 56 search cards from 16 exact queries and checked 18 official source paths across FDA, EMA, MHRA, TGA and Health Canada. No additional qualifying watched-treatment notice was verified. FDA filtered-recall/labeling access, unresolved MHRA attachments, TGA posting lag and incomplete Canadian/global coverage remain explicit. Absence of a verified notice is not absence of harm.

No finding changes the selected next step: continue the separately scoped, aggregate-only NCT05371041 protocol/SAP/results crosswalk. The imaging lead does not justify reopening generic cohort searches or claiming a new therapy, disease modification or cure.

Only public metadata and original summaries were retained. No individual rows, personal narratives, contact fields, full abstracts or full papers were saved or redistributed. No outreach, participant collection, intervention or repository mutation occurred in this scan.

## Reproduce and validate

`scan_sources.py`, `scan_supplement.py`, `resume_preprints.py` and the selected-source check scripts record live requests; rerun results can change. `build_results.py` rebuilds original decisions from saved metadata. `python validate_artifacts.py` checks saved counts, deduplication, date bounds, selected-field differences and the explicit publication [manifest](manifest.json) without external requests. Baseline inputs are comparison snapshots, not an exhaustive historical corpus. Transient source bodies and `__pycache__` are excluded from publication.
