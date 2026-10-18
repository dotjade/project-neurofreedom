# Project NeuroFreedom daily public evidence scan

18 October 2026 | Core API retrievals 02:39:04–02:40:12 UTC; supplementary direct-source checks through 02:41:34 UTC, with web discovery through approximately 02:41:39. Regulator surveillance is outside this component and should be reported separately.

## Result

**No new qualifying primary tic-study result or newly posted relevant trial result was verified in this bounded scan.** One newly encountered October 16 pediatric narrative review is classified as secondary evidence. Known negative-feasibility and retraction records remain visible; their reappearance is not counted as new evidence.

- Eight PubMed queries returned 12 ID occurrences and six unique records. Only one ID was absent from the prior scan; it is a review rather than a new participant study.
- Official bioRxiv/medRxiv feeds yielded 541 distinct DOI/version pairs across 19 pages. No title/abstract matched the prespecified lexical tic/Tourette screen.
- Four ClinicalTrials.gov queries returned eight occurrences and three distinct records, all already screened. Selected date, status, design, indication, eligibility and results fields were unchanged. Two relevant records still have no results; the broad DBS return remains excluded.
- The **officially documented ISRCTN public XML API worked**, improving coverage beyond the previously inaccessible search interface. The bounded update query returned zero records. An undated positive-control query returned one requested record and reported 22 total matches, confirming a live nonempty endpoint.

These findings do not establish absence of relevant research worldwide, treatment ineffectiveness, equivalence, disease modification or a cure.

## Baseline, scope and dates

Read the current README, RESEARCH_PROTOCOL, STATUS, primary evidence ledger, October 17 report, query ledger, registry and integrity records before searching. [Repository provenance](baseline-repository-provenance.json) records fetched blob IDs; [baseline metadata](baseline-metadata.json) preserve the prior deduplication keys. The previous verified supplementary cutoff was October 17 at 03:17:08 UTC.

Search filters overlap October 16–18 inclusively, plus an October 17–18 entry-date query. October 18 was only partly elapsed. Publication, database entry, metadata revision, preprint-version posting, registry submission, registry posting and third-party synchronization are separate dates. The live databases and their indexing can change after retrieval.

No age, severity, language, human-only or study-design filter was applied to the core queries. A supplementary query explicitly included adults, severity, pain, burden, ADHD/comorbidity, treatment and adverse/negative findings. Childhood findings are not substituted for persistent severe adult evidence. No completed historical analysis was repeated.

## PubMed

ESearch used db=pubmed, retmode=json and retmax=1000. Counts were below the cap. [Search code](scan_sources.py) and [query/decision ledger](search-log.json) contain exact query strings, translated queries, date fields, request times, response hashes, IDs and screening decisions.

| Query family | Date field | Inclusive window | Returned |
|---|---|---|---:|
| Tourette OR "tic disorder" OR "tic disorders" | edat | October 16–18 | 1 |
| Same core, nearer window | edat | October 17–18 | 1 |
| Same core | pdat | October 16–18 | 2 |
| Same core | mdat | October 16–18 | 5 |
| Core plus correction/retraction terms | edat | October 16–18 | 0 |
| tics OR "chronic motor tic" OR "chronic vocal tic" OR "persistent tic" | edat | October 16–18 | 1 |
| Same synonyms | pdat | October 16–18 | 1 |
| Core plus adult/burden/comorbidity/treatment/negative terms | edat | October 16–18 | 1 |

All six records received identifier, date, publication-type and linked-notice screening. Five overlap yesterday's retrieved set; no changed linked-notice fields were found in those five. The new review's abstract was inspected to establish its design. This is not full-text review or comprehensive correction/Crossmark clearance.

### Newly encountered secondary review

[PMID 42888480](https://pubmed.ncbi.nlm.nih.gov/42888480/), [DOI 10.1111/jpc.70627](https://doi.org/10.1111/jpc.70627), concerns abdominal tics in children/adolescents and a proposed differential-diagnosis framework. PubMed explicitly classifies it as a review; the abstract describes a narrative synthesis. It does not contribute a new cohort, controlled treatment estimate or demonstrated diagnostic accuracy.

PubMed and Crossref give electronic publication October 16. PubMed records entry October 17 at 05:33 and Entrez entry at 00:14, without timezone labels. Crossref creation is October 17 at 03:55:38 UTC and deposit at 03:55:46. These metadata dates must not replace the reported electronic-publication date. The web extractor could not open PubMed; the official EFetch response succeeded. Full text was not assessed. See [secondary screening](secondary-screening.jsonl), which is deliberately separate from the empty new-primary ledger.

### Other decisions and negative evidence

- PMID 42867549: the October 13 pediatric allergy association study is already in the main evidence ledger. Its October 16 revision is not a new study.
- PMID 42808868: adult OCD secondary review already screened; October 16 publication metadata coexist with September 29 database entry. It is not primary tic evidence.
- PMID 40229987: older occlusal-device case reports, already screened; metadata modification creates no new controlled result. No individual case details were retained.
- [Affected PMID 39947542](https://pubmed.ncbi.nlm.nih.gov/39947542/) and [notice PMID 42527169](https://pubmed.ncbi.nlm.nih.gov/42527169/): the historical GFAP/yohimbine preclinical paper remains explicitly retracted. The notice's electronic date is July 29, despite its October issue. Retain exclusion from positive mechanistic/efficacy evidence. No new retraction reason or status change was verified, and the retraction alone does not disprove the mechanism. [Integrity recheck](integrity-recheck.jsonl).

## Preprints

Official endpoint: https://api.biorxiv.org/details/{server}/2026-10-16/2026-10-18/{cursor}. Case-insensitive title/abstract screen: `\btourett\w*|\btics?\b`.

- bioRxiv: 16 pages, 473 unique DOI/version pairs; last cursor 450 returned 23. Reported total stayed 473. There were 344 exact overlaps with yesterday and 129 pairs absent from that scan.
- medRxiv: three pages, 68 unique pairs; last cursor 60 returned eight. Reported total stayed 68. There were 59 overlaps and nine pairs absent from yesterday.
- Zero lexical matches across 541 pairs. These are all-subject preprint postings/versions, not 541 tic studies. Observed pagination was complete. This is a live, bounded lexical screen, not a frozen census; other servers and records lacking these words may be missed. Secondary search returned older preprint leads, without a verified in-window version warranting inclusion.

## Official trial registries

### ClinicalTrials.gov

The filter was `AREA[LastUpdatePostDate]RANGE[2026-10-16,2026-10-18]`, pageSize=100, countTotal=true. Tourette, tic disorder, Tics and ecopipam queries returned 2, 3, 3 and 0 records, respectively. No next-page token was present. [Structured registry rechecks](registry-evidence.jsonl) preserve what was compared; this is not a full protocol-history audit.

- [NCT05158439](https://clinicaltrials.gov/study/NCT05158439): still Withdrawn, actual enrollment zero, reason inability to recruit, without results. Submission October 13 and posting October 16 are unchanged. The actual date of withdrawal remains unresolved. Preserve this as negative feasibility/status evidence, not a negative efficacy trial or proof that cell therapy was administered.
- [NCT07137442](https://clinicaltrials.gov/study/NCT07137442): observational adult physiology protocol remains Recruiting, planned N=75, ages 18–80, estimated start October 21, last posting October 16, without results. Planned dates and measures are not observed outcomes.
- [NCT02119611](https://clinicaltrials.gov/study/NCT02119611): unchanged broad DBS record remains outside the relevant set; current indication fields do not establish a Tourette cohort.
- [NCT07093541](https://clinicaltrials.gov/study/NCT07093541), directly rechecked outside the date filter: expanded-access ecopipam status remains Temporarily Not Available, last posting October 14, no results. Selected fields and response hash match the prior supplementary retrieval. No new suspension, cause or safety event is inferred.
- [NCT06194305](https://clinicaltrials.gov/study/NCT06194305): a discovery mirror displayed an October 17 synchronization date, but the official record's last posting is July 22, with no results. It is excluded from new-window updates. The mirror date is not registry posting or publication.

### ISRCTN coverage improvement

The ordinary search page was inaccessible and a direct record page redirected to a JavaScript/cookie holding page. Its linked [FAQ](https://www.isrctn.com/page/faqs) points to public API documentation. The documented endpoint succeeded without credentials:

`https://www.isrctn.com/api/query/format/default`

Exact query: `(Tourette OR tics OR "tic disorder") AND lastEdited GE 2026-10-16T00:00:00 AND lastEdited LT 2026-10-19T00:00:00`; limit=50. The XML response was HTTP 200 and reported totalCount=0. An undated `Tourette` query with limit=1 reported totalCount=22 and returned one record. This control was an endpoint check, not a review of all 22 studies. A direct SATURN record metadata check also succeeded; no new-window result was promoted.

[Supplementary retrievals](supplement-selected-metadata.json), [positive control](isrctn-control.json), [retrieval code](scan_supplement.py) and [control code](check_isrctn.py) preserve the usable route for future scans. A zero count applies only to this query and live response.

### Remaining coverage limits

WHO ICTRP's web extractor timed out, but ordinary HTTP retrieved the landing page. Its latest listed import date was October 12, before this overlap window; no usable query export was obtained. CTIS returned a page shell without an enumerated result set. Domain-limited web discovery did not verify another qualifying in-window registry update. No worldwide registry-completeness claim is made.

## Deliverables and boundary

[Summary](summary.json), [discovery/access ledger](source-checks.json) and [validation](validation.json) accompany the records. [Build script](build_results.py) applies the dated original screening decisions; retrieval code operates against live sources and outputs may change.

No primary-study addition is warranted today. The empty [primary-evidence.jsonl](primary-evidence.jsonl) is intentional; do not duplicate the historical studies or recast a narrative review as a new trial. Do not remove existing negative findings.

Only original summaries, bibliographic/protocol metadata, identifiers, request hashes and code are retained. No abstracts, full papers, raw source HTML/XML, individual case narratives, private community content or family data are redistributed. No outreach, intervention, account action, participant collection, payment or GitHub write occurred during this scan.
