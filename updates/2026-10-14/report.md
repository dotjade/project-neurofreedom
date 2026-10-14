# Project NeuroFreedom daily public evidence scan

14 October 2026 | Literature/preprint/registry API retrievals 02:46:32–02:51:03 UTC; supplementary discovery from approximately 02:46 UTC. Regulatory retrieval times are recorded separately.

## Result

One unique in-window ClinicalTrials.gov update was verified: an existing NINDS adult observational study of motor and functional tics, without posted results. An EMA Intuniv/guanfacine document update posted October 13 adds ADHD-study information and updates risk-management documentation; it is not a new tic-treatment trial or urgent safety warning. See the separate safety report for the exact regulatory dates, limitations and an older FDA device-recall item discovered during the scan.

No qualifying newly published primary tic study or tic-keyword preprint was verified in this bounded incremental search. Eight PubMed queries returned 29 ID occurrences and 27 unique metadata records. Twenty-three bioRxiv/medRxiv requests, including one empty terminal page, returned 632 unique DOI/version records with zero lexical matches. Four ClinicalTrials.gov queries returned two occurrences of the same study. These negative findings do not establish that no relevant evidence appeared elsewhere.

## Baseline and scope

Read README.md, RESEARCH_PROTOCOL.md, STATUS.md, evidence.jsonl, the October 13 scan and its ledger through GitHub before searching. Baseline blob identifiers are in [the manifest](source-manifest.json). The incremental baseline is October 13 approximately 03:17–03:24 UTC. Inclusive filters cover October 12–14; a nested entry-date query covers October 13–14. October 14 was only partly elapsed.

Publication, PubMed/Entrez entry, metadata revision, preprint posting/version, registry posting, regulator document posting and clinical-event dates remain distinct. Date-only fields cannot identify exact within-day novelty. No age, severity, language, human-only or study-design restrictions were placed on the core searches. An adult/severe/pain/burden/comorbidity/treatment/negative-findings supplement was included; pediatric evidence does not substitute for the adult question.

The exact queries, translated queries, request URLs/timestamps, metadata and screening decisions are in [the search ledger](search-log.json). This is a bounded update, not an exhaustive review.

## Peer-reviewed literature and metadata screening

PubMed ESearch used `db=pubmed`, `retmode=json`, `retmax=1000`. Every result count was below the retrieval cap. Core query: `Tourette OR "tic disorder" OR "tic disorders"`. Supplemental synonyms: `tics OR "chronic motor tic" OR "chronic vocal tic" OR "persistent tic"`.

| Query | Date field | Inclusive dates | Records |
|---|---|---|---:|
| Core | edat | October 12–14 | 1 |
| Core, nearer window | edat | October 13–14 | 0 |
| Core | pdat | October 12–14 | 0 |
| Core | mdat | October 12–14 | 26 |
| Core + correction/retraction terms | edat | October 12–14 | 0 |
| Supplemental synonyms | edat | October 12–14 | 1 |
| Supplemental synonyms | pdat | October 12–14 | 0 |
| Adult/burden/treatment supplement | edat | October 12–14 | 1 |

All 27 records received date/type/identifier/linked-notice metadata screening via EFetch. Six IDs were absent from the previous scan's set; four had abstracts that were inspected and two had none. This was not full-text review of all 27 studies.

- [PMID 42860839](https://pubmed.ncbi.nlm.nih.gov/42860839/), DOI 10.1002/mdc3.70862, is a cervical-dystonia rTMS pilot. It is not a tic-disorder study; the Tourette term appears in an author funding disclosure. It was first published online October 11, with PubMed history October 12 at 05:32 and Entrez history at 02:53. XML timestamps carry no explicit timezone. Although newly returned compared with yesterday's query set, it is not proven to have first entered or changed query membership after the baseline.
- Five other newly encountered IDs were older publications returned by the modification query: PMID 10382139 (1999 executive-function report), 11055462 (2000 comment), 40708347 (youth sensory dysregulation, first online July 24, 2025), 41908734 and 42343079 (2026 Parkinson-disease DBS reports). Metadata revision does not make them new research. Their complete date/type/identifier screening is retained.
- [PMID 42861218](https://pubmed.ncbi.nlm.nih.gov/42861218/) remains the prior-screened breast-MRI acronym false positive. It is not tic-disorder evidence.

Twenty-one metadata records overlap yesterday. Five records have linked notices; normalized fields were unchanged among overlapping records. The newly encountered linked family involves a 1999 study and 2000 comment, not an in-window correction. The focused notice query returned zero. This does not replace a complete publisher/Crossmark/retraction-history audit.

Supplementary discovery returned the already known October 8 Nature primer, older ecopipam results, historical reviews, educational pages and irrelevant matches. Search crawl dates and literal date-filter hits were not treated as first publication dates.

## Preprints

Official interval API: `https://api.biorxiv.org/details/{server}/2026-10-12/2026-10-14/{cursor}`. Titles and abstracts were screened using case-insensitive `\btourett\w*|\btics?\b`.

- bioRxiv: 480 unique DOI/version records, 16 nonempty pages plus an empty terminal page at cursor 480. All nonempty pages reported total 480 and new-paper count 389. Of these DOI/version pairs, 236 overlap yesterday and 244 were not in that set.
- medRxiv: 152 unique DOI/version records across six pages; final cursor 150 contained two records. Reported total 152 and new-paper count 112 were stable. Fifty-eight pairs overlap yesterday and 94 were not in that set.
- Zero lexical matches. Counts refer to posting/version records across all subjects, not tic studies. The known October 1 CBIT–TMS preprint was outside this posting-date interval; no repeated unavailable-full-text search or clinical-effect reconstruction was attempted.

The full observed interval was paginated, but feeds are live and are not a frozen census. Other servers, titles/abstracts lacking these words and later postings are outside coverage.

## Trial registry update

ClinicalTrials.gov API used `AREA[LastUpdatePostDate]RANGE[2026-10-12,2026-10-14]`, `pageSize=100`, `format=json`, `countTotal=true` with condition queries Tourette, tic disorder, Tics, and a term query ecopipam. Counts were 0, 1, 1 and 0; no next-page token was returned. The two occurrences deduplicate to [NCT07137442](https://clinicaltrials.gov/study/NCT07137442).

This NINDS study compares neurophysiology in adults aged 18–80 with motor tics, functional tics and healthy controls. Enrollment is planned at 75, up to 25 per group. Its registered primary outcome is pre-tic vertex EEG beta power over two days. First posted August 22, 2025; current update submitted October 12 and posted October 13, 2026. No results are posted. Current status is Recruiting, while start remains estimated October 18, 2026. Recruitment status does not establish that physiological testing has begun.

The healthy-volunteer flag is false despite a healthy-control arm and narrative. The record also has ambiguous vocal-tic-only exclusion wording. Medication timing, psychiatric and low-urge eligibility criteria restrict applicability to some high-burden treated adults. The short physiological assessment is not a sustained-severity cohort or treatment-benefit comparison. No diagnostic biomarker validation, efficacy or disease-modification claim follows. See [the original registry evidence record](registry-evidence.jsonl).

The official NIH search-indexed protocol corroborates the adult study and recruitment description; the registry's legacy NIH link redirected to a generic index. The ClinicalTrials.gov historical view was inaccessible. The posting date is verified, but exact changed fields compared with the prior version are not. Do not call it newly opened recruitment or a newly launched study.

An apparent October 13 synchronization of NCT06270251 on a third-party site was checked against the official API: its actual last update was March 19, 2026. It was excluded from the in-window count. WHO ICTRP was inaccessible; domain-limited ISRCTN, EU/CTIS, legacy EU and ReBEC discovery was not a complete registry export. No worldwide registry-negative conclusion is made.

## Regulatory safety and research consequence

See [the safety report](safety/report.md) and its ledger and [regulatory evidence records](safety/regulatory-evidence.jsonl) for official sources, document-version dates and separate classification of new postings versus older newly discovered notices. The guanfacine update requires preserving the limits of long-term neurocognitive inference and adverse-event discontinuation information; it does not establish tic benefit, a new tic indication, or absence of known risks.

The scan does not add a newly published primary or preprint efficacy record to evidence.jsonl. It adds a separate registry-update summary and regulatory evidence rather than conflating protocols, ADHD findings and tic-trial results. The planned adult ONLINE-TICS analysis remains separate. No completed MNS, gating-access, generic cohort, registry-endpoint or measurement-threshold work was repeated. No participant or family files, outreach, enrollment, purchase, intervention, paid compute or full scientific paper storage was involved.
