# Bounded evidence and safety scan: 10 November 2026

## Result

No qualifying new-window primary publication, relevant preprint or posted trial result was verified. Two watched registries have metadata updates posted November 9, described below. No new watched-treatment official safety warning was verified in the selected sources. These findings are bounded surveillance, not proof of absence or safety. No empirical evidence record or mechanism upgrade is proposed.

README, RESEARCH_PROTOCOL, STATUS, the journal-source README, November 9 daily/scan reports and current evidence record were inspected first. The preceding core scan ended November 9 at 02:42:06 UTC; its recovered preprint pagination ended 02:43:17 UTC. Current API checks ran November 10 at **03:25:17.782452–03:27:55.287498 UTC**. Two supplemental registry checks began at 03:27:33 and 03:27:37 UTC. Web discovery and official-index inspection occurred during this November 10 run. No unrecorded per-page timestamps are invented.

## Publications

Eight PubMed date-query families over November 8–10 produced 54 ID occurrences and 49 unique records. Core/synonym entry and publication dates, modification dates, correction/retraction terms and adult/severe/function/pain/comorbidity/treatment-burden terms were included without age or language filters. Exact parameters and returned IDs are in search-log.json. The near-entry query uses the same November 8 lower bound as the core query in this run; it is redundant, not additional coverage.

The 44 pre-2026 electronic/print publications are historical metadata-modification returns, not new findings. PMID 40238019 has an April 16, 2025 electronic date and December 2026 issue date; the later issue date does not make it a new study today. The remaining five records are already screened October publications: the pediatric NLRP3 review (PMID 42996864), broad cannabis systematic review/meta-analysis (PMID 42997457), and three unrelated acronym matches (42995839, 42997792, 42997938). Secondary reviews do not become new primary tic trials. The correction/retraction entry-date query returned zero; it does not establish that all historical articles are notice-free. Screening decisions, dates, identifiers and linked-notice metadata are retained in pubmed-screening.jsonl, with no abstract or individual health narrative in the publication package.

No changed primary/aggregate input satisfying the closed H18 measurement/transfer, H15 group-mask provenance or adult CANNA-TICS missingness gates was identified by this surveillance. This is not a renewed exhaustive audit of those closed questions.

## Preprints

The bioRxiv and medRxiv APIs returned **812 distinct DOI/version records** for November 6–10: 617 bioRxiv and 195 medRxiv. Title/abstract lexical screening for Tourette or tic/tics returned zero matches. Positive and negative lexical controls passed. Only DOI/version/date indexes are retained.

Both paginations reached the observed final totals, but medRxiv's reported total changed from 194 to 195 during pagination. Its mutable index prevents claiming a fixed-snapshot exhaustive scan, even though all 195 returned keys are distinct. The complete November 9 indexes, including the prior medRxiv recovery, yield 364 bioRxiv and 121 medRxiv overlaps; 253 and 74 respective versions were not in those indexes. These 327 versions are not 327 relevant new studies. The uncorrected fields in the raw log used the earlier incomplete medRxiv baseline; summary.json explicitly supplies corrected overlap counts from the full saved TSVs. Other servers, indexing delays, absent selected words and non-English terminology remain limitations.

## Registries

Four ClinicalTrials.gov date-window queries yielded two distinct studies posted November 9. Seven watched records were compared using selected title, status, design, conditions, age and results fields. No posted results were present.

- [NCT01019343](https://clinicaltrials.gov/study/NCT01019343): last submission changed November 4 to November 6 and last posting November 5 to November 9. Other selected fields are unchanged. Completed status is a registry label, not a new result.
- [NCT07137442](https://clinicaltrials.gov/study/NCT07137442): estimated start changed November 11 to November 12. Last submission changed November 5 to November 6 and posting November 6 to November 9. This is a planned-date update, not verification that enrollment or study activity occurred.
- NCT05158439, NCT06194305, NCT06678737, NCT07093541 and NCT07905898: no selected-field change.

Two supplemental official snapshots bring the total to nine distinct registries. [NCT07839377](https://clinicaltrials.gov/study/NCT07839377) remains last posted September 24 with no results. The newly rediscovered [NCT06825520](https://clinicaltrials.gov/study/NCT06825520), on premonitory urges during habit reversal, was last posted May 28, 2025, remains a single-group unmasked pediatric plan (estimated six participants), and has no results. A third-party November 9 sync date is not an official registry update or new evidence. Estimated past completion dates and a recruiting label do not verify current recruitment. No contact, recruitment or participant access occurred.

Supplementary searches of WHO, ISRCTN, ChiCTR and UMIN/Japanese terms yielded no verified new-window result. They are not exhaustive direct database searches. Previously unresolved UMIN chronology remains unresolved; search-result ordering is not used to assign a study's recruitment status.

## Official safety

Eight regulator index pages were inspected: FDA drug/device communications, MHRA drug updates/alerts, EMA latest updates/PRAC recommendations, TGA safety updates/alerts. Targeted searches covered aripiprazole, guanfacine, clonidine, topiramate, ecopipam and pimozide. The FDA November 9 item concerns GLP-1 receptor agonists and an eye-risk labeling change, outside this watched tic-treatment scope. MHRA's newest visible drug-update/alert items were November 5. EMA's latest index had November 9 entries; no watched treatment was among the inspected entries, and PRAC signal recommendations remained first published October 26. TGA safety updates showed October 14 as the latest visible item.

The MHRA October roundup's guanfacine prolonged-release product-information correction is historical: published October 27, updated October 30. It concerns missing QT/QTc information for specified product licences, not a new November 10 class-wide signal. The search-returned aripiprazole gambling notice is December 2023. Neither is classified as a new warning. These checks are English-heavy selected-source surveillance, not worldwide pharmacovigilance, a complete label review or individual safety advice.

## Reproduction and limits

scan_sources.py reruns live metadata queries, whose results can change. build_results.py rebuilds original screening decisions, corrected overlaps and registry comparisons from saved metadata and prior indexes. No participant-level computation or random seed is involved. No API request failed during this scan. The search log deliberately excludes registry contacts/locations and result measurements. No unlicensed paper, personal medical record, intervention or paid resource is included. Continue surveillance and act on materially changed prerequisites rather than repeat closed analyses.

### Official source links checked

- https://www.fda.gov/drugs/drug-safety-and-availability/drug-safety-communications
- https://www.fda.gov/medical-devices/medical-device-safety/safety-communications
- https://www.gov.uk/drug-safety-update
- https://www.gov.uk/drug-device-alerts
- https://www.ema.europa.eu/en/news-events/whats-new
- https://www.ema.europa.eu/en/human-regulatory-overview/post-authorisation/pharmacovigilance-post-authorisation/signal-management/prac-recommendations-safety-signals
- https://www.tga.gov.au/news/safety-updates
- https://www.tga.gov.au/safety/safety-monitoring-and-information/safety-alerts
- https://www.gov.uk/drug-device-alerts/mhra-safety-roundup-october-2026

The [web query provenance](web-query-provenance.json) preserves 12 exact searches and nine direct official page checks. Individual query times were not captured; the run date is recorded without fabricated times. The TGA safety-alerts excerpt was mainly navigation, so complete latest-alert-list coverage is not claimed.
