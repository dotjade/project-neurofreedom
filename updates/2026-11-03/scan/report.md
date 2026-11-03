# Bounded new-evidence scan, 3 November 2026

## Result

No new-window primary first publication, qualifying preprint, posted trial result or linked retraction was verified. One watched registry has an administrative date update. This is a bounded search, not proof that no evidence exists worldwide; regulatory safety is assessed separately.

The prior core cutoff was November 2 at 03:20:40.167517 UTC. This core scan ran November 3 from 02:40:57.513719 to 02:42:43.788281 UTC. PubMed and registry queries overlap November 1–3; preprint queries cover October 31–November 3. Calendar-day filters cannot establish exact within-day posting order. See [search-log.json](search-log.json) for exact queries, timestamps, URLs, hashes and selected metadata.

## Publications and preprints

Eight PubMed queries returned 71 ID occurrences and 67 unique records. Twenty-six overlap the previous scan; the other 41 are new to that small comparison set, not 41 new studies. Every record has an electronic or PubMed history date before November. Most new retrievals are older records with updated metadata. Nine core publication-date matches include November issue assignments for older online papers. Historical mechanistic, pediatric, comorbidity and negative findings remain evidence to retain, not new causal or clinical discoveries. Screening here establishes date eligibility, not a new full-text appraisal.

The correction screen found historical erratum citations (2007, 2023 and 2024/2025) and earlier-preprint links. Those links are not new retractions, independent replications or evidence of a new preprint version. Correction content was not reappraised; this is not exhaustive integrity clearance.

Observed bioRxiv and medRxiv pagination yielded 548 unique DOI/version records (419 and 129 respectively), with stable totals and zero title/abstract matches to the Tourette/tic lexical screen. Of these, 288 were absent from yesterday's overlapping index. Version records are not necessarily new studies. Positive and negative screen controls passed. Differently worded work, other preprint servers and indexing delays can be missed.

Supplementary web discovery found an October 28 institutional announcement for [PMID 42780243](https://pubmed.ncbi.nlm.nih.gov/42780243/). The underlying EMG/video method remains a September 20 Research Square preprint, DOI [10.21203/rs.3.rs-10832475/v1](https://doi.org/10.21203/rs.3.rs-10832475/v1), not a new November peer-reviewed publication. No participant videos, rows or dataset were opened or retained. Search crawl/access dates were not treated as publication dates. No new mechanistic or clinical claim is derived from this historical lead.

## Registry update

Four ClinicalTrials.gov queries identify one unique updated record, [NCT07137442](https://clinicaltrials.gov/study/NCT07137442), an observational neurophysiology protocol comparing tics and functional tics. Against the November 2 snapshot, its estimated start shifts November 4 to November 5, last submission October 29 to October 30 and update posting October 30 to November 2. It remains listed as RECRUITING, with estimated enrollment 75, ages 18–80 and no posted results. The posting date alone does not establish whether it appeared before or after the prior scan's exact cutoff; the snapshot change is verified. This is not evidence that recruitment began, that the proposed diagnostic method works, or that a treatment helps.

Five direct watched-record comparisons were completed. The other four selected-field snapshots are unchanged: NCT05158439, NCT06194305, NCT07093541 and NCT07905898. All five still lack posted results. The previously documented adolescent PRISM-TS enrollment inconsistency is not resolved by unchanged selected fields. Full amendment history and unselected fields were not compared.

## Limits and next decision

All 37 core API requests succeeded. Exact request provenance, selected-field differences, original screening decisions and DOI/version indexes are retained. No abstracts, unlicensed full text, case narratives or participant files are archived. WHO/national registries, other servers, non-English terminology, unindexed work and delayed notices remain coverage gaps. All ages/severities, sustained severe adult burden, pain, function and co-occurring conditions remain in scope; a null daily scan does not diminish those needs.

Continue the separately planned same-trial CANNA-TICS driving audit, preserving hierarchy, margin, analysis population, missingness and harms. Do not reopen closed marker exercises on the basis of metadata revisions. No contact, intervention, participant data or paid compute is required.

## Reproduction

Run `python scan_sources.py --out NEW_DIRECTORY --baseline baseline.json` to repeat live queries (results may change); `python build_results.py` to reproduce selected extractions; and `python validate.py` for consistency/screen controls. Baseline metadata comes from the November 2 scan at repository commit 5cc598196428261bc4c289f94cc7929af55c0bf0. Thirty-two local consistency assertions passed. No simulation or RNG is involved; these checks are not independent clinical review.
