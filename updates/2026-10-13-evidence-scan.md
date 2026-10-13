# Project NeuroFreedom daily public evidence scan

13 October 2026 | Retrievals approximately 03:17–03:24 UTC

## Result

No new qualifying peer-reviewed primary tic study, relevant preprint, ClinicalTrials.gov update/result, or material FDA/EMA/MHRA target-therapy safety notice was verified in this bounded incremental check. This scan proposes no addition to the primary-study, preprint or registry evidence files. It does not establish that no relevant finding appeared anywhere.

Eight PubMed searches yielded 100 ID occurrences and 98 unique records. The only newly indexed candidate not in yesterday's set was an unrelated breast-imaging study using “TICs” for time-intensity curves. The October 1 CBIT–TMS preprint was a known overlap. Twenty fully paginated bioRxiv/medRxiv API pages yielded 563 posting/version records with zero tic-keyword matches. Four ClinicalTrials.gov queries each returned zero studies.

New official notices did exist: EMA displayed 15 entries dated October 12 and MHRA had an October 12 Pedmarqsi recall, but no watched tic-therapy safety notice was identified. The distinction between newly available website content and relevant new evidence is preserved.

## Baseline, dates and scope

Before searching, read README.md, RESEARCH_PROTOCOL.md, STATUS.md, evidence.jsonl, [yesterday's scan](2026-10-12-evidence-scan.md) and its search ledger. Exact baseline blob identifiers, request timestamps, queries, result IDs, exclusions and access limits are in the [machine-readable ledger](2026-10-13-search-log.json).

The incremental baseline is October 12 approximately 02:51 UTC. Inclusive database filters cover October 11–13, with a nested October 12–13 entry-date query. October 13 was only partly elapsed. Publication, electronic posting, PubMed/Entrez entry, metadata revision, registry posting and clinical-event dates are distinct. Date-only fields cannot determine exact within-day novelty; fresh crawl timestamps were not treated as scientific publication dates.

Core searches used no age, severity, language, human-only or study-design restriction. They cover TS and persistent tic disorders across ages, with severe persistent adult illness, pain, social/functional burden, comorbidity, treatment and negative findings explicitly represented in a supplemental query. A pediatric result would not substitute for the adult question. No closed generic adult-cohort search, unchanged MNS calculation, gating full-text access hunt or unresolved preprint synthesis was repeated.

## Peer-reviewed literature and metadata screening

PubMed ESearch endpoint: `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi`; `db=pubmed`, `retmode=json`, `retmax=1000`. Each count was below the retrieval cap. All 98 returned records received date/type/linked-notice metadata screening through EFetch; the new entry candidate's abstract was inspected for eligibility. This was not full-text review of 98 papers.

| Query family | Date field | Inclusive dates | Returned |
|---|---|---|---:|
| Core | edat | October 11–13 | 1 |
| Core | edat | October 12–13 | 0 |
| Core | pdat | October 11–13 | 0 |
| Core | mdat | October 11–13 | 96 |
| Notice | edat | October 11–13 | 0 |
| Supplemental synonyms | edat | October 11–13 | 2 |
| Supplemental synonyms | pdat | October 11–13 | 0 |
| Adult/burden/treatment | edat | October 11–13 | 1 |

- Core: `Tourette OR "tic disorder" OR "tic disorders"`
- Supplemental synonyms: `tics OR "chronic motor tic" OR "chronic vocal tic" OR "persistent tic"`
- Notice: core in parentheses AND `(retraction OR retracted OR erratum OR corrigendum OR correction)`
- Adult/burden/treatment: core in parentheses AND `(adult OR severe OR pain OR burden OR comorbid* OR treatment OR adverse OR negative OR quality of life)`

[PMID 42861218](https://pubmed.ncbi.nlm.nih.gov/42861218/), DOI 10.21037/qims-2026-0790, concerns breast MRI and was excluded as an acronym false positive. It was electronically published September 4, assigned an October 1 issue date and entered PubMed October 12 at 05:32, with Entrez history at 04:24; XML history timestamps carry no explicit timezone. It is not tic-disorder evidence or a newly first-published October 12 study.

Eighty-five records overlap yesterday's 201-record metadata set. Of 13 newly encountered IDs, 12 are older publications returned by the modification query; their titles, dates, types and exclusion decisions are retained. Metadata modification is not new research. Supplementary web discovery again returned the October 8 Nature primer/PrimeView, older ecopipam results and institutional trial publicity. Reviews, educational materials, old primary studies and irrelevant matches were not counted as in-window primary evidence.

Sixteen records carried linked notices. Normalized linked-notice fields were unchanged among overlapping records. The two additional linked-source families were a [2018 erratum](https://pubmed.ncbi.nlm.nih.gov/29524074/) and a [2024 editorial](https://pubmed.ncbi.nlm.nih.gov/39159415/), not new corrections or clinical safety signals. The focused new-entry notice query returned zero. This is not a complete publisher/Crossmark/retraction-history audit.

## Preprints

[PMID 42856611](https://pubmed.ncbi.nlm.nih.gov/42856611/), DOI 10.64898/2026.09.29.26364036, remains the October 1 preprint already examined on October 12. Its generic Journal Article metadata does not override the Preprint classification. No renewed clinical-effect calculation or unavailable full-text search was attempted.

The official interval API `https://api.biorxiv.org/details/{server}/2026-10-11/2026-10-13/{cursor}` was separately paginated and screened with case-insensitive `\btourett\w*|\btics?\b` over titles and abstracts:

- bioRxiv: 15 pages, cursors 0–420 by 30; 421 unique DOI/version pairs; terminal page one record; reported total 421 and new-paper count 345 throughout.
- medRxiv: five pages, cursors 0–120 by 30; 142 unique DOI/version pairs; terminal page 22 records; reported total 142 and new-paper count 111 throughout.
- Zero lexical matches in either feed. Counts are posting/version records, not tic studies. Metadata for deduplication is preserved; full papers are not stored.

Stable totals during this retrieval do not make the feeds a permanently frozen census. Other servers, metadata without these terms and later postings remain outside coverage.

## Trial registries

Official ClinicalTrials.gov API queries used `filter.advanced=AREA[LastUpdatePostDate]RANGE[2026-10-11,2026-10-13]`, `pageSize=100`, `format=json`, `countTotal=true`, with `query.cond=Tourette`, `query.cond=tic disorder`, `query.cond=Tics` and `query.term=ecopipam`. Every response reported totalCount 0 and no next-page token. No in-window posting/result was verified; no trial-status claim was inferred from an expected completion date.

WHO ICTRP's direct query was inaccessible. Domain-limited discovery across ISRCTN, legacy EU/CTIS and ReBEC did not verify an in-window update, but these systems were not comprehensively exported. No worldwide registry-negative claim or historical field-diff completion is made.

## Regulatory safety

The [safety report](2026-10-13-safety.md) and [exact search ledger](2026-10-13-safety-search-log.json) record 14 queries and 10 successfully opened unique official sources. FDA's latest visible drug/device communications remained September 15/June 3. EMA had 15 October 12 entries; none identified a watched therapy notice, and main CHMP-agenda keyword checks were negative. The agenda annex remained inaccessible. MHRA Drug Safety Update still topped at September 2; its October 12 Pedmarqsi recall was unrelated.

Therapies covered: ecopipam; aripiprazole, risperidone, pimozide, haloperidol; clonidine, guanfacine; valbenazine, deutetrabenazine, tetrabenazine; median-nerve stimulation/Neupulse, rTMS and DBS. This is bounded public-notice surveillance, not every label revision, all regulators or spontaneous-event signal analysis. Existing risks are not negated by a negative daily scan.

## Research consequence

The scan does not change a clinical claim or justify an intervention. Continue the already specified adult GTS-QOL/YGTSS validation and longitudinal-concordance question as a separate bounded analysis; retain pain, impairment, quality of life and participation as distinct outcomes. No patient files, individual/family information, outreach, enrollment, purchase, paid compute or medical intervention was involved.
