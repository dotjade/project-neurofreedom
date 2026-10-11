# Project NeuroFreedom daily public evidence scan

11 October 2026 | Search retrievals approximately 03:04–03:08 UTC

## Result

No new qualifying primary Tourette/tic study, relevant preprint, posted trial result, material registry change or in-scope regulatory safety notice was verified in this bounded daily update. The core PubMed queries returned 18 unique records, all screened in the preceding scan. Two overlapping ClinicalTrials.gov records were identical to the saved 10 October snapshots. A fully paginated bioRxiv/medRxiv title-and-abstract metadata screen found no tic-related keyword matches among 480 returned posting/version records.

Recent publicity about a wrist device required a classification safeguard: Neupulse C is described by its manufacturer as a wellness product, while Neupulse M remains in development and its regulatory pathway continues. The distinction was already announced in May. A 9 October news story is not a new clinical trial, October regulatory approval or evidence of disease modification.

No addition to the primary-study evidence file or registry-evidence file is warranted from this scan. This is a bounded negative finding, not a claim that no new research or safety event exists anywhere. It does not establish that any treatment is risk-free and does not support a clinical recommendation.

## Scope and baseline

Read the current private repository README.md, RESEARCH_PROTOCOL.md, STATUS.md, evidence.jsonl and updates/2026-10-10-evidence-scan.md before searching. The structured primary-study file contains 18 records. Baseline blob hashes were:

- README.md: `d4221c21cacd8119ff17dd9dbd32072beaf66a82`
- RESEARCH_PROTOCOL.md: `3cb049d097d68d032650700cf68d1612cbef1ec7`
- STATUS.md: `faa961c4717f0d8eaa1d8fde0f502763d2e9f472`
- evidence.jsonl: `47ccdf03793760bfd6abd3bb71113ad17d917797`
- updates/2026-10-10-evidence-scan.md: `7b9121b088095ba30d95314a4c3f62bd2a1b599c`

The primary interval begins after the previous scan, approximately 10 October 02:48 UTC. Inclusive 9–11 October date filters supply a small overlap; a nested 10–11 October PubMed entry query checks the nearer interval. Most database fields have date-only precision, and 11 October is only partly elapsed. Publication, indexing, record modification, registry posting and clinical-event dates are kept separate. A recent crawl date is not a publication date.

The scope remains Tourette syndrome and persistent tic disorders across all ages and severities, including persistent severe adult tics, pain, functional and social burden, co-occurring conditions, unmet treatment needs and durable treatment response. No age, severity, language, human-only or study-design restriction was imposed on core searches. Pediatric evidence is not substituted for adult persistence questions. No patient records, participant files or private community content were obtained, and no contact, enrolment or treatment action was taken.

## Literature findings and deduplication

All 18 unique PMIDs were already present in the preceding scan's saved official metadata. Their titles, publication/electronic dates, publication types and linked correction metadata were checked. No retrieved article had a linked CommentsCorrections notice; the date-filtered correction/retraction search returned zero. This is not a complete Crossmark, publisher-history or retraction-database audit.

The four entry-window overlap candidates remain:

- [PMID 42850293](https://pubmed.ncbi.nlm.nih.gov/42850293/), DOI 10.1038/s41572-026-00742-6: review, published 8 October, PubMed-history date 9 October. Secondary synthesis, not an independent primary sample.
- [PMID 42850245](https://pubmed.ncbi.nlm.nih.gov/42850245/), DOI 10.1038/s41572-026-00748-0: companion PrimeView, published 8 October, PubMed-history date 9 October. No independent efficacy evidence.
- [PMID 42850218](https://pubmed.ncbi.nlm.nih.gov/42850218/), DOI 10.1080/0964704X.2026.2734029: biography and historical translation, published 8 October, PubMed-history date 9 October. It discusses historical haloperidol treatment rather than a new treatment experiment.
- [PMID 42852027](https://pubmed.ncbi.nlm.nih.gov/42852027/), DOI 10.3389/fpsyt.2026.1920653: somatic-cough case report published 24 September, indexed 9 October. Tic disorder was excluded; do not generalize the report to tic treatment.

All four had already been screened on 10 October. The three 8 October publications have Entrez-history dates on 8 October and PubMed-history dates on 9 October; neither should be called first published on 9 October. No novel full-text extraction was needed for this update.

The remaining 14 unique IDs were modification-window overlaps: 42845759, 41961094, 41888346, 41557034, 41288886, 41152527, 41079641, 40965605, 40540000, 39679818, 39175366, 38619754, 38269641 and 31980733. These include older relevant primary studies and irrelevant all-field matches. Their prior dates and screening status exclude them from new-in-interval counts. Metadata revision alone cannot establish a new result. The supplemental tic-synonym searches added no unique PMID.

## Official trial registry findings

The three ClinicalTrials.gov searches produced five returns and two unique NCT IDs. Both have last-update-posted dates of 9 October and no posted results. Whole-record JSON comparison with the complete 10 October official API snapshots found no field differences, including in derived metadata.

- [NCT01043549](https://clinicaltrials.gov/study/NCT01043549), adult posterior-parietal rTMS: unchanged historical termination for lack of efficacy; actual enrollment five; completion September 2012. The recent registry posting is not a new trial failure in October 2026. The existing negative-evidence record should be retained without a duplicate.
- [NCT07137442](https://clinicaltrials.gov/study/NCT07137442), adult tic/functional-tic physiology: unchanged recruiting label, estimated start 14 October 2026, estimated enrollment 75, ages 18–80 and no results. Its medication/comorbidity exclusions still limit applicability to many people with severe treated adult illness. An estimated date or recruiting label is not proof that enrollment has begun or that a biomarker works.

The ecopipam term query found zero updated records in the overlap. This says nothing about older trial results. No historical API was retried after the preceding scan's access restriction; the current comparison is between two lawfully saved current-record snapshots, not a full registry-history reconstruction.

WHO ICTRP's Tourette query again did not return usable content via the web tool. Targeted ISRCTN, legacy EU-register and CTIS-domain discovery did not verify a new in-window record, but these sources were not comprehensively date-filtered or exported. Global registry coverage remains incomplete.

## Preprints

Official [bioRxiv/medRxiv API documentation](https://api.biorxiv.org/) was checked before using the date-range endpoint. All pages for 9–11 October were retrieved:

- bioRxiv: 15 pages, 425 posting/version records, 425 unique DOI/version pairs. API `count_new_papers` was 327.
- medRxiv: two pages, 55 posting/version records, 55 unique DOI/version pairs. API `count_new_papers` was 33.

Across all 480 records, a case-insensitive title-plus-abstract filter `\btourett\w*|\btics?\b` returned zero candidates. This was an automated lexical screen of the entire returned metadata set, not manual full-text review of 480 papers. Counts include versions and are not counts of relevant tic studies. No age/category/design restriction was used. This closes yesterday's specific preprint-feed limitation for these two servers and this date range, but not for other preprint servers or papers lacking those terms in searchable metadata. A preprint would remain unreviewed evidence even if relevant.

## Publicity safeguard for the wrist device

A 9 October University-of-Nottingham-attributed news story about the wrist device surfaced during broad discovery. It is publicity, not a primary experiment or official approval record. No personal testimonials or identifying clinical anecdotes were extracted or retained in this report.

The manufacturer's [6 May 2026 release announcement](https://neupulse.co/blogs/news/introducing-our-early-access-wellness-release) already explained its wellness-first approach while medical-device regulatory work continued. Its [current science page](https://neupulse.co/pages/science) describes Neupulse C as intended for general wellbeing and Neupulse M as still in development. The science page links the already-recorded 2023 randomized trial, DOI 10.1111/jnp.12313 / PMID 37133932. Thus the recent story does not establish a new first launch, independent new efficacy evidence, product equivalence to the research prototype, medical approval, lasting benefit after stimulation, or a cure. Manufacturer statements establish the company's current description, not an independent safety or efficacy judgment.

## Regulatory safety

The official FDA, EMA and MHRA check ran 03:05–03:06 UTC. No new in-scope notice was identified for ecopipam; aripiprazole, risperidone, pimozide or haloperidol; clonidine or guanfacine; valbenazine, deutetrabenazine or tetrabenazine; median nerve stimulation/Neupulse, rTMS or DBS.

Checked the [FDA Drug Safety Communications](https://www.fda.gov/drugs/drug-safety-and-availability/drug-safety-communications), [device communications](https://www.fda.gov/medical-devices/medical-device-safety/safety-communications), [drug recalls](https://www.fda.gov/drugs/drug-safety-and-availability/drug-recalls), [device safety index](https://www.fda.gov/medical-devices/medical-device-safety), [device recalls and early alerts](https://www.fda.gov/medical-devices/medical-device-safety/medical-device-recalls-and-early-alerts), [EMA What's New](https://www.ema.europa.eu/en/news-events/whats-new), [PRAC highlights](https://www.ema.europa.eu/en/news/meeting-highlights-pharmacovigilance-risk-assessment-committee-prac-28-september-1-october), [MHRA alerts](https://www.gov.uk/drug-device-alerts), [October field safety notices](https://www.gov.uk/drug-device-alerts/field-safety-notices-for-october-2026) and [Drug Safety Update](https://www.gov.uk/drug-safety-update).

EMA's 43 visible rows dated 9 October were screened; no 10–11 October row was visible. FDA's 11 listed device communications had no new-window entry. The latest FDA drug/device communications remained 15 September/3 June; MHRA Drug Safety Update still ended 2 September. The 9 October overlap notices concern Brevital injection, Philips diagnostic ultrasound, Ocrevus and StatStrip ketone strips, already noted and outside the specified scope. FDA's full device-recall index worked today, resolving yesterday's page-access limitation.

This is public-announcement surveillance, not a full label-version comparison, all enforcement records, FAERS/MAUDE signal analysis, all national authorities or all manufacturers. Same-day changes, indexing delay and unpublished signals remain possible. Existing non-new risks remain clinically relevant; none is negated by this scan.

## Reproducible database ledger

### PubMed

ESearch endpoint: `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi`. All calls used `db=pubmed`, `retmode=json`, `retmax=1000`, default start zero. Returned counts were below the cap. All 18 unique IDs were fetched by EFetch XML at 03:06:01 UTC; the two supplemental IDs were also fetched at 03:07:52.

Core query exactly: `Tourette OR "tic disorder" OR "tic disorders"`.

| Retrieval start UTC | Date field | Inclusive range | Count |
|---|---|---|---:|
| 03:05:31 | edat | 2026/10/09–2026/10/11 | 4 |
| 03:05:38 | edat | 2026/10/10–2026/10/11 | 0 |
| 03:05:44 | pdat | 2026/10/09–2026/10/11 | 0 |
| 03:05:50 | mdat | 2026/10/09–2026/10/11 | 15 |
| 03:05:55 | edat, notice query below | 2026/10/09–2026/10/11 | 0 |
| 03:07:40 | edat, supplemental query below | 2026/10/09–2026/10/11 | 2 |
| 03:07:46 | pdat, supplemental query below | 2026/10/09–2026/10/11 | 0 |

Notice query exactly: `(Tourette OR "tic disorder" OR "tic disorders") AND (retraction OR retracted OR erratum OR corrigendum OR correction)`.

Supplemental query exactly: `tics OR "chronic motor tic" OR "chronic vocal tic" OR "persistent tic"`.

The two supplemental entry hits were 42850293 and 42850218, both duplicates. Across all seven calls: 21 returned ID occurrences, 18 unique PMIDs, zero new-to-baseline IDs and zero new qualifying studies. No unrecognized-phrase warnings were returned. The core modification query's 15 IDs comprise the 14 modification-only IDs listed above plus 42852027. [Reproducible core entry-date query](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=Tourette%20OR%20%22tic%20disorder%22%20OR%20%22tic%20disorders%22&datetype=edat&mindate=2026%2F10%2F09&maxdate=2026%2F10%2F11&retmode=json&retmax=1000).

### ClinicalTrials.gov

API v2 endpoint: `https://clinicaltrials.gov/api/v2/studies`. Each call used `filter.advanced=AREA[LastUpdatePostDate]RANGE[2026-10-09,2026-10-11]`, `pageSize=100`, `format=json`, `countTotal=true`.

- 03:06:07: `query.cond=Tourette`, totalCount 1.
- 03:06:13: `query.cond=tic disorder`, totalCount 2.
- 03:06:19: `query.cond=Tics`, totalCount 2.
- 03:06:24: `query.term=ecopipam`, totalCount 0.

Five returns, two unique NCTs; no next-page token on any response. [Reproducible Tourette registry query](https://clinicaltrials.gov/api/v2/studies?query.cond=Tourette&filter.advanced=AREA%5BLastUpdatePostDate%5DRANGE%5B2026-10-09%2C2026-10-11%5D&pageSize=100&format=json&countTotal=true).

### Preprint API

- `https://api.biorxiv.org/details/biorxiv/2026-10-09/2026-10-11/{cursor}`: cursors 0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420; retrieval starts 03:06:27 through 03:07:58 UTC.
- `https://api.biorxiv.org/details/medrxiv/2026-10-09/2026-10-11/{cursor}`: cursors 0 and 30; retrieval starts 03:08:04 and 03:08:10 UTC.

Every response reported status `ok`, category `all`, and interval `2026-10-09:2026-10-11`. Terminal pages returned five and 25 records respectively, meeting their stated total counts. DOI/version deduplication found no repeated pair within either returned set.

## Supplementary web discovery ledger

Exact queries below ran approximately 03:05–03:07 UTC. Search-engine exhaustive counts were unavailable; these are not added to database totals. Date/domain operators produced old or irrelevant hits, so dates were inspected rather than assumed.

1. `Tourette "October 10, 2026" OR "October 11, 2026"`
2. `Tourette tic disorder after:2026-10-08`, domain `pubmed.ncbi.nlm.nih.gov`
3. `Tourette "tic disorder" after:2026-10-08`, domains `medrxiv.org`, `biorxiv.org`
4. `"Tourette" after:2026-10-08`, domains `isrctn.com`, `clinicaltrialsregister.eu`, `euclinicaltrials.eu`
5. `"Tourette" "October 2026" adult severe trial treatment`
6. `site.nottingham.ac.uk "New wrist stimulation device" "2026"`
7. `site.neupulse.co.uk "Neupulse C" "medical"`
8. `"New wrist stimulation device brings relief" "nottingham"`
9. `site.nottingham.ac.uk/news Neupulse October 2026`
10. `site.nottingham.ac.uk "Neupulse C"`

No primary in-window study was verified through these supplementary searches. Older ecopipam conference/press material, the review already screened on 10 October, and the previously recorded MNS trial were not promoted as new. The Nottingham-hosted original news page was not located; the product distinction above relies on the verified manufacturer pages. WHO direct query attempted at 03:07 UTC: `https://trialsearch.who.int/?query=Tourette`; tool reported it inaccessible.

## Consequence for the research program

Keep the all-age/severity research priorities and current evidentiary claims unchanged. Continue the separate bounded adult longitudinal/data-feasibility work selected in STATUS.md; this scan supplies no basis to substitute a pediatric sample, promote a cure hypothesis or assume durable disease modification. Keep publications, registry metadata, product publicity and clinical-event dates distinct. No urgent clinical alert follows from this scan.


## Appendix Exact regulatory discovery queries


All searches used the web tool. Literal query strings are reproduced below. Date operators and recency settings returned old documents and irrelevant hits, so search-result timestamps were not treated as publication evidence. Broad grouped searches also produced noisy results, so simpler domain-filtered searches supplemented them. No exhaustive search-engine result count is asserted.

### 03:05:22–03:05:24

1. `site:fda.gov (ecopipam OR aripiprazole OR risperidone OR pimozide OR haloperidol OR clonidine OR guanfacine OR valbenazine OR deutetrabenazine OR tetrabenazine) (safety OR recall OR warning) after:2026-10-08 before:2026-10-12`
2. `site:ema.europa.eu (ecopipam OR aripiprazole OR risperidone OR pimozide OR haloperidol OR clonidine OR guanfacine OR valbenazine OR deutetrabenazine OR tetrabenazine) after:2026-10-08 before:2026-10-12`
3. `site:gov.uk (ecopipam OR aripiprazole OR risperidone OR pimozide OR haloperidol OR clonidine OR guanfacine OR valbenazine OR deutetrabenazine OR tetrabenazine) (safety OR recall OR warning) after:2026-10-08 before:2026-10-12`

### 03:05:45–03:05:47

4. `(site:fda.gov OR site:gov.uk OR site:ema.europa.eu) (Tourette OR Neupulse OR "median nerve stimulation" OR rTMS OR "transcranial magnetic stimulation" OR "deep brain stimulation") (safety OR recall OR warning) after:2026-10-08 before:2026-10-12`
5. `(site:fda.gov OR site:gov.uk OR site:ema.europa.eu) ecopipam "October 2026"`
6. `(site:fda.gov OR site:gov.uk OR site:ema.europa.eu) (aripiprazole OR risperidone OR pimozide OR haloperidol) "October 2026"`
7. `(site:fda.gov OR site:gov.uk OR site:ema.europa.eu) (clonidine OR guanfacine OR valbenazine OR deutetrabenazine OR tetrabenazine) "October 2026"`

### 03:05:53–03:05:55

8. `ecopipam safety October 2026` — domains: fda.gov, ema.europa.eu, gov.uk.
9. `Neupulse recall safety` — domains: fda.gov, gov.uk; recency: 7 days.
10. `"deep brain stimulation" recall` — domains: fda.gov, gov.uk; recency: 7 days.
11. `"transcranial magnetic stimulation" safety recall` — domains: fda.gov, gov.uk; recency: 7 days.

### 03:06:03–03:06:05

12. `aripiprazole risperidone safety after:2026-10-08 before:2026-10-12` — domains: fda.gov, ema.europa.eu, gov.uk.
13. `pimozide haloperidol safety after:2026-10-08 before:2026-10-12` — domains: fda.gov, ema.europa.eu, gov.uk.
14. `clonidine guanfacine safety after:2026-10-08 before:2026-10-12` — domains: fda.gov, ema.europa.eu, gov.uk.
15. `valbenazine deutetrabenazine tetrabenazine safety after:2026-10-08 before:2026-10-12` — domains: fda.gov, ema.europa.eu, gov.uk.

### 03:06:14–03:06:16

16. `"median nerve" safety after:2026-10-08 before:2026-10-12` — domains: fda.gov, gov.uk.
17. `"ecopipam" safety` — domains: fda.gov, ema.europa.eu, gov.uk; recency: 7 days.
18. `"Neupulse" safety` — domains: fda.gov, gov.uk; recency: 7 days.
19. `"PRAC" "October 2026" safety` — domain: ema.europa.eu; recency: 7 days.

