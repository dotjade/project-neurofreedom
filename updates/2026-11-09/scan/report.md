# Bounded evidence and safety scan: 9 November 2026

## Result

No qualifying new-window primary publication, preprint, posted trial result or official watched-treatment safety warning was verified. This is a bounded early-day surveillance result, not proof that none exists or that treatments are safe. No new primary evidence record is proposed for `evidence.jsonl`.

The current source reference was [a68355a22f7de6e694ac4df29ad670983dd6c68f](https://github.com/dotjade/project-neurofreedom/commit/a68355a22f7de6e694ac4df29ad670983dd6c68f). README, RESEARCH_PROTOCOL, STATUS, journal-source README, evidence and the November 8 scan were read first through the GitHub connector. Eight source-blob hashes were recomputed successfully in [baseline verification](baseline-verification.json).

The previous core cutoff was **November 8, 03:07:59.615070 UTC**. Today's core API work ran **November 9, 02:38:48.088705–02:42:06.319868 UTC**. A failed medRxiv page was recovered, and pagination finished at **02:43:17.961556 UTC**. Two directed metadata checks have separate timestamps. [Search log](search-log.json), [request log](request-log.json), [recovery ledger](preprint-recovery.json) and [summary](summary.json) preserve exact queries, source hashes and accounting. These are source checks, not a systematic review or a new clinical analysis.

## Literature: publication, indexing and overlap

Eight PubMed query families returned **40 ID occurrences and 35 unique records**. Entry, publication and modification dates were queried over November 7–9, with a nearer November 8–9 entry-date query. Core Tourette/tic terms, chronic/persistent synonyms, correction/retraction terms, and adult, severe, pain, function, comorbidity and treatment-burden terms were included. There were no age or language filters. Calendar-day filters do not establish exact within-day first-publication time.

All 35 records have [screening decisions](pubmed-screening.jsonl):

- Twenty-nine are historical 2002–2018 papers returned by the modification-date query. A database modification is not a new scientific finding. One has an erratum citation dated December 2007; another has an old commentary link. Neither was treated as a new correction.
- [PMID 42995077](https://pubmed.ncbi.nlm.nih.gov/42995077/), the *Trends in Cognitive Sciences* editorial, is prior-screened acronym overlap.
- [PMID 42996864](https://pubmed.ncbi.nlm.nih.gov/42996864/) is a pediatric NLRP3 review electronically published October 23, not new primary evidence. Its [publisher abstract](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2026.1968624/abstract) explicitly distinguishes human neuroimmune associations from animal/non-tic mechanisms and says disease-specific causal and intervention validation is lacking. The attempted full-text URL resolved to an abstract page, not a full-methods extraction.
- [PMID 42997457](https://pubmed.ncbi.nlm.nih.gov/42997457/), [DOI 10.1016/j.eclinm.2026.104299](https://doi.org/10.1016/j.eclinm.2026.104299), is a broad medical-cannabis systematic review/meta-analysis electronically published October 29. The official XML abstract was inspected. It retains limited psychiatric evidence, uncontrolled Tourette reports and heterogeneous safety data; these cannot be promoted to a new tic trial, a formulation-independent treatment effect or an individual's risk estimate. The DOI web-reader route was inaccessible.
- A prostate-cancer preprint and two ultrasound time-intensity-curve papers are unrelated acronym matches, not tic studies.

Thirty-four records were absent from the previous scan's query set, but this is **not** 34 new papers or 34 new repository findings. Dynamic indexing and date-query differences are retained. The dedicated correction/retraction entry-date query returned zero; that does not clear every paper or establish worldwide absence of notices. The known retracted historical review flagged on November 8 remains excluded from substantive support.

### Directed sensory-paper check

The separately requested check of [Stanco et al., PMID 42947547](https://pubmed.ncbi.nlm.nih.gov/42947547/) is **historical and already recorded**, not a new-window finding. It was first published October 28 and audited on October 29–30. The official metadata response hash is identical to the one recorded in the October 30 audit; no linked notice is present. This makes **36 distinct PubMed IDs inspected**, including the directed lookup, not 36 new studies.

Its 30-adult-TS/30-control force-matching association does not establish a causal mechanism, prospective prediction or treatment efficacy. Direct-condition significance and indirect-condition nonsignificance are not a formal interaction. The [Wiley landing page](https://movementdisorders.onlinelibrary.wiley.com/doi/10.1002/mds.70590) now exposes explicit aggregate supplement descriptions for S1–S4, but the exact DOCX download returned HTTP 403. No numerical table, individual dataset or new precision estimate was obtained. Keep the [existing fixed audit](https://github.com/dotjade/project-neurofreedom/blob/main/analyses/sensory_contrast/2026-10-30/report.md) closed pending lawful aggregate methods/tables. Details: [incidental check](incidental-sensory-check.json) and [official metadata](supplement-pubmed.json).

## Preprints

The bioRxiv/medRxiv APIs yielded **485 unique DOI/version records** over November 6–9: **364 bioRxiv and 121 medRxiv**. Title/abstract screening with `\btourett\w*|\btics?\b` found no match. Positive and negative lexical controls passed. Both paginations completed against stable observed totals. A medRxiv cursor-60 request returned HTTP 503; one bounded retry succeeded and only the remaining pages were requested. The initial failure and successful recovery remain in the record.

Thirty-five versions were absent from the previous overlapping index: six bioRxiv and 29 medRxiv. They are not 35 new relevant studies. The [bioRxiv](biorxiv-preprint-index.tsv) and [medRxiv](medrxiv-preprint-index.tsv) indexes retain DOI, version and date only. Supplemental searches covered arXiv/JMIR and returned the already screened JMIR measurement-paper lead, without establishing a new relevant version. Other servers, non-English terms, abstracts lacking selected words, delayed indexing and mutable API pagination remain limitations. A lexical null is not proof of complete absence.

## Clinical-trial registries

Four date-window ClinicalTrials.gov queries returned zero postings over November 7–9. Seven direct watched records had **no selected-field change and no posted results** versus the November 8 core/supplemental snapshots: NCT01019343, NCT05158439, NCT06194305, NCT06678737, NCT07093541, NCT07137442 and NCT07905898. See [registry comparisons](registry-evidence.jsonl). This is selected-field comparison, not an exhaustive version-history audit. A registry status label or planned date does not verify current enrollment, activity, efficacy or safety.

A supplementary [UCSF lead](https://clinicaltrials.ucsf.edu/trial/NCT07839377) was reconciled with the [official registry](https://clinicaltrials.gov/study/NCT07839377). The official [projected snapshot](supplement-registry.json) reports first/last posting September 24, 2026, estimated 40 participants ages 15–35, randomized unmasked parallel assignment and `hasResults=false`. The institutional page's September 18 update reflects an earlier date than public registry posting. This is a historical study lead, not a new result, validated target or confirmed currently active recruitment. It is the **eighth distinct registry inspected**.

The API projection excludes contacts, officials, locations and result measurements. Supplemental web searches included WHO/UMIN/ISRCTN/ChiCTR and a Japanese tic query, but are not exhaustive direct searches of those registries. Prior unresolved UMIN chronology is not cleared. No contact, recruitment, enrollment or participant-file access occurred.

## Official safety and guidance

Four targeted safety query families, eight official regulator index pages and an Intuniv product page were inspected. Exact queries and decisions appear in [safety-query-log.json](safety-query-log.json) and [safety-review.json](safety-review.json). The prior safety-summary time was November 8 at 03:09:42.279875 UTC. Web checks were performed during this November 9 run; no unrecorded per-page timestamps are invented.

No qualifying new watched-treatment official warning or newly issued tic guideline was verified. The [FDA drug](https://www.fda.gov/drugs/drug-safety-and-availability/drug-safety-communications) and [device](https://www.fda.gov/medical-devices/medical-device-safety/safety-communications) indexes exposed no new relevant event. The newest visible [MHRA safety](https://www.gov.uk/drug-safety-update) and [alert](https://www.gov.uk/drug-device-alerts) items were November 5. The [EMA current index](https://www.ema.europa.eu/en/news-events/whats-new) showed November 6 entries and [PRAC recommendations](https://www.ema.europa.eu/en/human-regulatory-overview/post-authorisation/pharmacovigilance-post-authorisation/signal-management/prac-recommendations-safety-signals) remained first published October 26. The [TGA safety-update](https://www.tga.gov.au/news/safety-updates) and [alert](https://www.tga.gov.au/safety/safety-monitoring-and-information/safety-alerts) indexes yielded no new relevant event.

Recently crawled Intuniv information refers to an October 27 product-information update, not a new November 9 warning. Old shortages, product listings and broad guidance returned by search are not new class-wide hazard findings. This is English-heavy selected-source surveillance, not worldwide pharmacovigilance or a complete label review. No individual adverse-event narrative or risk estimate was retained. Prior inaccessible correction/catalogue leads were not cleared, and unchanged searches were not repeated.

## Reproduction and next decision

`scan_sources.py` performs the live queries; results and dates may change. `recover_preprints.py` documents the bounded continuation needed for this run. `build_results.py` rebuilds classifications, indexes and comparisons from saved metadata. `validate.py` checks accounting and consistency, not clinical validity or search completeness. No random seed or participant computation is involved.

Continue the separately assigned public aggregate measurement-anchor/invariance audit. This scan gives no basis to upgrade a mechanism, treatment, diagnostic system or personalized rule. Keep persistent severe adult function, pain, effort, participation and co-occurring burden central alongside all-age tic evidence. No personal records, intervention, outreach, paid resource or repository write was part of this scan preparation.
