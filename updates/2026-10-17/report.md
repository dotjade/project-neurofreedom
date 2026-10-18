# Project NeuroFreedom daily public evidence scan

17 October 2026 | Core API retrievals 03:13:29–03:15:17 UTC; supplementary primary-source checks through 03:17:08 UTC. Regulator surveillance is reported separately.

## Result

- One newly encountered case report supplies a **hypothesis-generating pharmacovigilance signal**, not a causal risk estimate or a treatment result. Its earlier publication/indexing dates and later publisher-platform availability are kept separate. Only bibliographic metadata and a general design-level summary are retained; no individual case information is reproduced.
- An October 16 registry posting describes a cell-therapy study as **withdrawn for inability to recruit, with actual enrollment zero and no results**. The date the status changed is unverified. This is negative feasibility evidence, not a failed clinical-efficacy trial.
- A **historical July 2026 retraction** of a preclinical GFAP/yohimbine paper surfaced through metadata-modification searching. It is explicitly excluded from positive evidence; this is not a new October retraction.
- Eight PubMed queries returned 22 ID occurrences and 16 unique records. Official bioRxiv/medRxiv feeds returned 642 distinct DOI/version records across 22 pages, with zero lexical tic/Tourette matches. These bounded results do not establish worldwide absence of relevant work.

## Baseline, scope and dates

Read the current README, RESEARCH_PROTOCOL, STATUS, primary evidence ledger, October 16 report, baseline metadata, search log and registry ledger before searching. [Baseline metadata](baseline-metadata.json) identify the fetched repository blobs and deduplication keys. The prior core scan ended October 16 at 02:43:55 UTC, with supplementary checks through approximately 02:46:43.

Current filters cover October 15–17 inclusively, with an additional October 16–17 entry-date query. October 17 was only partly elapsed. Source publication, issue assignment, database entry, metadata revision, preprint-version posting and registry posting are distinct. An item absent from yesterday's query output can carry an earlier entry date; database timing or indexing lag is not resolved by this comparison.

No age, severity, language, human-only or study-design restriction was applied to the core queries. Adult persistence, severe symptoms, pain, social/functional burden, ADHD and other co-occurring conditions, treatment and negative findings were included in a supplementary query. Pediatric findings are not generalized to persistent severe adult symptoms. Completed historical analyses were not repeated.

## Literature

PubMed ESearch used db=pubmed, retmode=json and retmax=1000. Every count was below the cap. [Search code](scan_sources.py) and [search ledger](search-log.json) preserve exact queries, translations, dates, request UTC times, response hashes, returned IDs and decisions.

| Query | Date field | Inclusive window | Returned |
|---|---|---|---:|
| Tourette OR "tic disorder" OR "tic disorders" | edat | October 15–17 | 2 |
| Same core, nearer window | edat | October 16–17 | 0 |
| Same core | pdat | October 15–17 | 2 |
| Same core | mdat | October 15–17 | 14 |
| Core plus retraction/correction terms | edat | October 15–17 | 0 |
| tics OR "chronic motor tic" OR "chronic vocal tic" OR "persistent tic" | edat | October 15–17 | 2 |
| Same synonyms | pdat | October 15–17 | 0 |
| Core plus adult/burden/ADHD/comorbidity/treatment/negative terms | edat | October 15–17 | 2 |

All 16 records received metadata, date, type, identifier and linked-notice screening. Nine overlapped yesterday's retrieved set; seven did not. Six of the seven additional IDs had abstracts inspected for design/relevance; the retraction notice had no abstract. One of those seven, the October 13 pediatric allergy study, was already in the current primary ledger; the October 8 narrative primer is older secondary evidence. No changed linked-notice field was found among the nine overlaps. This is not full-text review of every item or comprehensive Crossmark clearance.

### Newly encountered signal-only report

[Traverso, Mittaine and Bagheri, PMID 42881067](https://pubmed.ncbi.nlm.nih.gov/42881067/), [DOI 10.1016/j.therap.2026.08.002](https://doi.org/10.1016/j.therap.2026.08.002), is a case report concerning a possible tic adverse-event association with sublingual allergen immunotherapy. It can generate a question for pharmacovigilance; it cannot establish incidence, a class-wide risk, general causality or tic-treatment benefit. It is not a regulator warning or an instruction to change treatment.

PubMed reports electronic publication September 23, with PubMed entry October 15 at 23:31 and Entrez entry at 22:05; those database timestamps do not specify timezones. Crossref creation was September 23 at 04:17:58 UTC and deposit revision October 15 at 20:35:12 UTC. The [EM-consulte publisher listing](https://www.em-consulte.com/medecine/revue/THERAP/souspresse/therapies) reports corrected-proof online availability October 16. The exact first public availability remains unresolved; the October 16 platform date must not replace the earlier metadata.

The PubMed abstract was read only for source assessment. ScienceDirect returned a Site Unavailable page despite HTTP 200; the EM-consulte article endpoint returned HTTP 403, while its public listing was accessible. No full-text methods or independent causality adjudication was verified. The [structured record](primary-evidence.jsonl) deliberately omits case demographics, narrative, timeline, images and individual medical details. DOI/PMID searches and the current primary ledger did not identify a duplicate; case-level overlap was not investigated.

### Historical integrity finding

[PMID 39947542](https://pubmed.ncbi.nlm.nih.gov/39947542/), DOI 10.1016/j.ijbiomac.2025.140956, is marked Retracted Publication and linked to [notice PMID 42527169](https://pubmed.ncbi.nlm.nih.gov/42527169/), DOI 10.1016/j.ijbiomac.2026.153656. The notice's electronic date is July 29, 2026; its current issue is October. Recent metadata modification does not make the retraction new.

The affected preclinical study is excluded from positive mechanism or efficacy evidence. Retraction does not itself prove the proposed mechanism false. The notice text and reason were not verified because publisher retrieval was unavailable. Crossref also contains differently sourced update metadata: a Retraction Watch retraction entry dated July 29 and a publisher erratum entry dated October 1. PubMed's retraction designation is explicit. See the separate [integrity record](integrity-evidence.jsonl).

No matching record appears in the fetched primary ledger. Default-branch GitHub connector searches for both PMIDs and GFAP returned no matches. These scoped checks did not find a project claim requiring correction; they are not a complete byte-for-byte repository/history audit.

### Other screening decisions

The October 15 adult qualitative study and October 13 pediatric allergy study are duplicates. The adult-OCD review with an October 16 electronic/issue date was already screened yesterday and is secondary evidence. The October 8 Tourette primer is also secondary and outside the publication window. Older occlusal-device case reports, laryngeal-dystonia research, video classification, symptom networks, HRV/QoL, functional-tic review, sarcopenia and Parkinson-DBS records do not become new studies through modification dates. The cognitive-aging TICS return is an acronym collision. Decisions and original dates remain in the ledger.

## Preprints

Official endpoint: https://api.biorxiv.org/details/{server}/2026-10-15/2026-10-17/{cursor}. The case-insensitive title/abstract screen was `\btourett\w*|\btics?\b`.

- bioRxiv: 17 pages, 508 distinct DOI/version pairs, final cursor 480 returning 28; reported total stayed 508. Of these, 141 exact pairs overlapped yesterday's retrieved set and 367 did not.
- medRxiv: 5 pages, 134 distinct pairs, final cursor 120 returning 14; total stayed 134. There were 75 exact overlaps and 59 pairs absent from yesterday's set.
- Zero lexical matches among 642 pairs. These are all-subject postings/versions, not 642 tic studies. Observed pagination was complete, but live feeds are not a frozen census, date/version metadata can change, and work without the selected words or on other servers can be missed.

## Official registries

ClinicalTrials.gov used AREA[LastUpdatePostDate]RANGE[2026-10-15,2026-10-17], pageSize=100 and countTotal=true. Tourette, tic disorder, Tics and ecopipam queries returned 2, 3, 3 and 0 records. Eight occurrences deduplicated to three records; no next-page tokens were returned. Two are relevant; the broad DBS record is excluded. [Registry evidence](registry-evidence.jsonl) is separate from primary-study evidence.

- [NCT05158439](https://clinicaltrials.gov/study/NCT05158439): current phase 1, single-group, open-label mesenchymal-cell protocol is Withdrawn, enrollment 0 ACTUAL, reason inability to recruit, no results. The update was submitted October 13 and posted October 16; first posting was December 15, 2021. No previous official snapshot was obtained, so the date of withdrawal is unresolved. The registry describes a patient-funded protocol and four-year safety monitoring. Neither activity nor safety/efficacy is demonstrated. Numeric age bounds are absent; generic child/adult/older-adult flags establish no actual representation.
- [NCT07137442](https://clinicaltrials.gov/study/NCT07137442): existing adult observational physiology study remains Recruiting, planned N=75, ages 18–80, without results. Its October 16 posting moves estimated start from October 20 to October 21; submission moved October 14 to 15. Other compared status/date fields were unchanged. Two-day EEG measures are not treatment outcomes; selected-field comparison is not a complete history audit.
- [NCT02119611](https://clinicaltrials.gov/study/NCT02119611): excluded after official description/eligibility inspection. Its current DBS cohort concerns Parkinson disease, dystonia or essential tremor, not a verified Tourette cohort. Broad search retrieval alone is insufficient for inclusion.
- [NCT07093541](https://clinicaltrials.gov/study/NCT07093541): directly rechecked outside the current date filter. The October 14 ecopipam expanded-access posting, temporary-unavailability status and absence of results remain unchanged in selected fields. No new suspension, cause or safety event is inferred.

WHO ICTRP's landing page remained readable, listing October 12 as the latest import for multiple major registries, before this overlap window. No usable search export was obtained. ISRCTN search was inaccessible and CTIS returned a page shell without results. Bounded domain-limited discovery did not verify another new posting. Worldwide registry coverage is incomplete.

## Consequence and limits

Retain the case report only as a weak, general pharmacovigilance signal, the withdrawn protocol as feasibility/status evidence and the retracted paper as an explicit integrity exclusion. None supports a cure, disease modification, general risk estimate or change in clinical care. No newly first-published controlled tic-treatment result was verified in this bounded interval.

[Supplementary checks](source-checks.json) record the exact discovery queries, known access limits and date conflicts. [Supplementary retrieval code](scan_supplement.py) reproduces the selected-field reads; live outputs can change. Regulator surveillance is reported separately.

No participant information, case narrative, abstracts, full papers or raw source HTML/XML are redistributed. No outreach, account action, trial enrollment, medical intervention, purchase, paid compute or repository commit occurred during this scan.
