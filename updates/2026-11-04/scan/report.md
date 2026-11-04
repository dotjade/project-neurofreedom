# Bounded new-evidence scan, 4 November 2026

## Result

No qualifying new-window primary first publication, preprint, posted trial result or linked retraction was verified. One watched registry has an administrative date update. This is a bounded search, not evidence that no relevant work exists worldwide; regulatory safety is assessed separately.

The prior core cutoff was November 3 at 02:42:43.788281 UTC. This scan ran November 4 from 02:36:31.704588 to 02:40:05.116250 UTC, including recovery of one transient API failure. PubMed and registry queries overlap November 2–4; preprint queries cover November 1–4. Calendar-day filters cannot establish exact within-day posting order. Exact queries, source URLs, timestamps and response hashes are in [search-log.json](search-log.json).

## Publications and preprints

Eight PubMed queries yielded 62 ID occurrences and 62 unique records. Forty-two overlap the prior scan and 20 are absent from that comparison set, not 20 new studies. Sixty came from the core modification-date query; two came from broader tic entry-date terms. Every retained record has an electronic or historical PubMed date before November. Date eligibility was checked without turning recent indexing or issue assignment into a new publication. Historical negative, mechanistic, pediatric and comorbidity findings are not discarded or reclassified as discoveries.

The two newly indexed case-report titles, [PMID 42972472](https://pubmed.ncbi.nlm.nih.gov/42972472/) and [PMID 42973455](https://pubmed.ncbi.nlm.nih.gov/42973455/), carry September 29 and October 19 electronic dates respectively. They are case reports, not comparative evidence for treatment efficacy or a new November clinical result. Individual narratives were not extracted or retained. Correction links in other retrieved records point to historical errata or earlier preprint versions, not newly verified retractions. This is not exhaustive research-integrity clearance.

The bioRxiv and medRxiv APIs yielded 921 unique DOI/version records: 732 and 189 respectively. Title/abstract lexical screening found no Tourette/tic match. Five hundred fifty version records were absent from the previous overlapping index; they are not necessarily 550 separate new studies. Both observed paginations completed with stable reported totals. One medRxiv request at cursor 60 returned HTTP 503; a single bounded recovery resumed that page successfully, preserved the failed request and completed the remaining pages. Positive and negative lexical controls passed. Other servers, differently worded work and indexing delays remain gaps.

Supplementary web discovery returned historical papers, registry mirrors and event pages. [PMID 42412229](https://pubmed.ncbi.nlm.nih.gov/42412229/) has a July 7 electronic publication date despite a November issue assignment. Mirror synchronization/crawl dates were not treated as registry changes. Official registry web pages for two historical leads exposed only shells; the core official API update-window scan, not those shells, supplies registry verification. No community posts or participant files were used. See [discovery-log.json](discovery-log.json).

## Registry update

Four ClinicalTrials.gov update-window queries identified one unique record, [NCT07137442](https://clinicaltrials.gov/study/NCT07137442), an observational protocol comparing tics and functional tics. Against the November 3 snapshot, estimated start shifts November 5 to November 8, last submission October 30 to November 2, and update posting November 2 to November 3. It remains listed as RECRUITING, with estimated enrollment 75, ages 18–80 and no posted results. The posting date alone cannot establish whether it appeared before or after yesterday's exact cutoff; the selected-field snapshot change is verified. This is not evidence that recruitment actually began, that a diagnostic method is valid or that a treatment helps.

Five direct watched-record comparisons were completed. The other four selected-field snapshots are unchanged: NCT05158439, NCT06194305, NCT07093541 and NCT07905898. All five lack posted results. The previously documented adolescent PRISM-TS enrollment discrepancy is not resolved by unchanged selected fields. Unselected fields and complete amendment histories were not compared.

## Coverage and next decision

Fifty of 51 API requests succeeded; the sole transient failure was recovered and both preprint paginations completed. No abstracts, unlicensed full text, individual case narratives or participant files are archived. The archive contains selected public bibliographic/protocol metadata and original screening decisions. WHO and national registries, other preprint servers, non-English terminology, unindexed work and delayed notices remain limitations. A null daily scan does not diminish persistent severe adult burden, pain, functional limitations, co-occurring conditions or unmet treatment needs across ages and chronic tic disorder categories.

Continue the planned H15 group-only network-map/code/license feasibility gate. Do not reopen completed sensory/gene or CANNA-TICS audits because of metadata revisions. No researcher contact, intervention, personal data or paid compute is needed.

## Reproduction

Run `python scan_sources.py --out NEW_DIRECTORY --baseline baseline.json` for live queries, whose results can change. `resume_preprints.py` documents the single recovery of the observed medRxiv HTTP503; it performs no work when pagination is already complete. Run `python build_results.py` and `python validate.py` to reproduce selected extractions and 32 local consistency/screen-control assertions. Baseline metadata comes from the November 3 scan at commit c0a9b5b10049b0714e432386d73c1933a6058c93. No simulation or RNG is involved. These are computational checks, not independent clinical validation.
