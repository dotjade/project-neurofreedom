# 2026-11-13 bounded discovery scan

## Scope and result
Compared with the verified 2026-11-12 08:05:28 UTC scan, one newly published **secondary synthesis**, not a new primary experiment, was identified. PubMed metadata and abstracts were screened; licensed full text was not copied. Exact queries, retrieval times, response hashes and identifiers are in `scan.json`; selected registry differences are in `review.json`.

[PMID 43018909](https://pubmed.ncbi.nlm.nih.gov/43018909/), DOI [10.1007/s10578-026-02124-1](https://doi.org/10.1007/s10578-026-02124-1), electronic publication 12 November 2026: an ecopipam systematic review pooled six publications representing four trials (427 participants, predominantly pediatric). The abstract reports a YGTSS total tic score mean difference of -3.72 points versus placebo (95% CI -5.45 to -1.99), with moderate certainty according to the review authors. It does not supply enough detail to independently audit overlapping reports, pooling choices, or adult-specific estimates. Nonsignificant safety comparisons do not establish equivalence or exclude uncommon/long-term harms. This is a review of existing trials, not 427 newly studied patients or evidence of a cure. Adult and diverse-population evidence remains limited. Publisher DOI opening failed in the web tool; these statements are abstract-level, not full-text verification.

The broader PubMed query returned 23 records; the correction refinement returned zero. Six IDs overlap yesterday's scan. Most newly returned IDs represent older publications or unrelated lexical matches. PMID43014332, the November 11 OCD network meta-analysis, was already recorded yesterday and is not new tic-specific primary evidence. No qualifying newly published primary tic finding was verified in this bounded scan. Modification/indexing date is not publication date.

## Registry updates are not trial outcomes
ClinicalTrials.gov condition/date query returned three records. Directly re-read ten watched records. Selected fields were compared with yesterday's metadata, not full version histories.

* [NCT07137442](https://clinicaltrials.gov/study/NCT07137442), adult ages18-80 observational neurophysiology study: November12 posting moves estimated start from November15 to November17. Recruitment label and estimated enrollment75 remain unchanged; no posted results. An estimate is not proof that study work started.
* [NCT01019343](https://clinicaltrials.gov/study/NCT01019343), adult movement-disorder physiology study: last-update submit/post dates changed to November10/12. Other compared fields unchanged; completed status and no posted results remain.
* [NCT02119611](https://clinicaltrials.gov/study/NCT02119611) is a broad movement-disorder DBS query hit with Parkinson's disease in its returned conditions, no results. Not classified as a new Tourette outcome.
* Eight other directly watched records have unchanged compared fields. NCT05615220 still has historical posted results; do not misreport that flag as new today. The withdrawn zero-enrollment NCT05158439 remains negative feasibility information, not efficacy evidence.

## Safety pass
Targeted November2026 searches covered FDA, MHRA, EMA and TGA with relevant tic medicines (aripiprazole, guanfacine, clonidine, pimozide, haloperidol; broader FDA/EMA queries included ecopipam, FDA/TGA botulinum). Current official listing pages were opened and date context inspected. No newly dated relevant warning since the baseline was verified. This is a bounded English-language listing/search check, not a comprehensive pharmacovigilance review.

* [FDA drug safety communications](https://www.fda.gov/drugs/drug-safety-and-availability/drug-safety-communications): latest visible entry November9 concerns GLP-1 drugs, outside the target interval and not a tic-treatment finding.
* [MHRA Drug Safety Update](https://www.gov.uk/drug-safety-update): visible recent material precedes the baseline; campaign notices are not new medicine-specific signals.
* [EMA news](https://www.ema.europa.eu/en/news): visible latest entry November6 veterinary committee; October30 PRAC entry is older. Does not establish absence of all EMA communications elsewhere.
* [TGA PI month table](https://www.tga.gov.au/product-information-safety-updates-month-table): aripiprazole fall-injury/overdose-management changes dated September24, not a new November warning. Prior MHRA guanfacine labeling issue remains historical.

## Limits and decision
No treatment recommendation or patient-level inference follows. PubMed retrieval is complete for returned IDs but indexing lags and query terminology limit coverage. Search engines and official listing views can be incomplete. Preprint title/abstract lexical coverage and pagination counts are specified in scan.json; incomplete pagination must not be described as a zero-result comprehensive scan. No contacts, recruitment, patient-data collection, or interventions were performed.

Next evidence decision: retain the new review as secondary context and prioritize a lawful full-text audit of trial/report overlap and adult subgroup evidence before changing confidence in ecopipam estimates. The separate historical reanalysis addresses a different bounded question.

## Completed preprint coverage
API scan ran 03:06:19-03:09:14 UTC on November13. The November10-13 medRxiv interval completed all observed pages (219 unique DOI/version records), with no Tourette/tic lexical matches in title or abstract. bioRxiv covered 390 unique DOI/version records before the bounded time budget, with no matches in the screened portion. bioRxiv pagination was incomplete. Lexical absence is not semantic absence. Public artifacts retain bibliographic metadata, not abstracts.

Reproduce selected-field comparison with `python review.py PATH_TO_BASELINE_SCAN_JSON`; the baseline is `updates/2026-11-12/scan/scan.json` in project-neurofreedom. `scan.py` performs fresh network retrieval and thus may return later records. No random simulation or seed is involved.
