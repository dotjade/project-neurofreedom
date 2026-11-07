# Bounded evidence and safety scan: 7 November 2026

## Result

One newly published peer-reviewed **measurement study** was verified: [Wu et al., JMIR AI, November 6](https://ai.jmir.org/2026/1/e98782), DOI 10.2196/98782, PMID 42993949. This is **not its first public disclosure**: the publisher reports an earlier preprint dated April 19. No qualifying new preprint, posted result among the screened registries, or new official watched-treatment warning was verified. This bounded scan is not an exhaustive global absence claim.

The reference repository main commit was `fbe540dd2552c07526418b407b1383be0a06a91b`. README, RESEARCH_PROTOCOL, STATUS, journal-source README and the prior scan were read through the GitHub connector. [Baseline verification](baseline-verification.json) records source hashes. The previous core cutoff was November 6 at 02:55:38.829914 UTC, supplemented by book metadata at 02:55:43.665529 UTC. Today's API work ran **03:06:22.790215–03:10:53.550409 UTC**. Later publisher and safety checks are separately timestamped where available.

## New paper: useful measurement evidence, unresolved reporting limits

[Wu and colleagues](https://ai.jmir.org/2026/1/e98782) studied 168 children aged 4–15 across three Chinese tertiary hospitals: 83 with active motor tics and 85 selected healthy controls. They selected 559 clips from standardized ward video monitoring and report participant-disjoint training and testing. The test denominator is **55 clips, not 55 independently sampled patients**. Reported accuracy was 49/55 (89.1%, 95% CI 77.8–95.9%); recall was 25/25 positive clips (100%, 95% CI 86.3–100%); specificity was 80.0% (95% CI 61.4–92.3%).

The [structured extraction](new-evidence.jsonl) separates those results from limitations: unknown preanalytic exclusion count, selected healthy controls, discarded poor-quality/occluded recordings, incompletely described participant counts and validation allocation, and no independent held-out-center or home test. The system does not include audio or measure the full functional-interference domain. Neither clinical benefit, treatment selection, severe-adult applicability nor a biological mechanism follows from clip discrimination. A patient-wise split helps prevent identity leakage but does not itself prove external generalizability.

A small [reproducible arithmetic check](reported-arithmetic.json), using only published aggregates, flags a reporting inconsistency. The three baseline accuracies (74.1%, 75.9%, 79.6%) cannot arise from an integer count of correct predictions out of the stated common n=55 at one-decimal rounding. They are compatible with 40/54, 41/54 and 43/54. This **does not prove n=54 was used**. The missing numerator/denominator or method needs clarification before comparative performance is promoted. No predictions, missing clip, repaired table or corrected P value were invented. The paper's P=.004 is a DeLong **AUC** comparison, not a tested accuracy difference. The Qwen accuracy 49/55 is arithmetically compatible with its stated denominator.

The final publisher HTML is lawfully accessible under CC BY 4.0 and was inspected transiently. The earlier preprint page was inaccessible through the web reader, so no version-by-version novelty audit was completed. PubMed metadata shows no linked correction/retraction; that is not comprehensive clearance. No participant video, image, case narrative or private data were acquired. The source supplies no public model weights or full processing pipeline for independent reproduction. This scan did not train or reproduce the model.

This new record is adjacent to existing repository video-method records PMID 42908833 and PMID 42964513, but it is not pooled with them: validation populations, labels, sampling units and endpoints differ, and cross-study participant overlap is not established.

## Publications and corrections

Eight PubMed query families returned **33 ID occurrences and 22 unique IDs**, all accounted for, including one book chapter. Queries cover entry, publication and modification dates, correction/retraction terms, chronic/persistent tic synonyms, and adult/severe/pain/co-occurring/treatment burden. Calendar overlap is November 5–7; the nearer entry-date query is November 6–7. No language or age filter was imposed. Exact queries, IDs, date fields, retrieval timestamps and response hashes are in [search-log.json](search-log.json).

After including the previous book supplement, four IDs were absent from the prior complete returned set. Only PMID 42993949 is a new-window journal primary paper. PMID 41503301 is a historical narrative review; PMID 41881176 is a March 2026 adult tract-imaging study with null clinical correlations, not a new November publication; PMID 42990710 uses a cognitive-test TICS acronym, not tic disorders. The older stress TICS-9 record, surgical process study and body-dysmorphic methods paper are also excluded. [Screening decisions](pubmed-screening.jsonl) preserve all 22 IDs rather than dropping inconvenient or non-journal results.

The raw query log's five “new-to-prior” IDs compare only with the prior core parser output. The curated summary correctly uses the prior **complete** scan, including PMID 23556151's separately verified book supplement, and therefore reports four. This is an accounting distinction, not newly discovered book evidence.

No linked new retraction/correction was found in returned metadata. A targeted search did not resolve the prior undated Nature primer correction lead. No absence or new-window correction claim is made for that unresolved source.

## Preprints

bioRxiv and medRxiv APIs supplied **1,084 unique DOI/version records** over November 4–7: 854 and 230 respectively. Both paginations reached their stable observed totals after one bounded resume of two transient HTTP 503 failures. Title/abstract screening with `\btourett\w*|\btics?\b` found no match. Positive and negative lexical controls pass. **409 version records** were absent from the prior overlapping index; these are not 409 new studies or relevant tic papers.

Only DOI/version/date indexes and relevant metadata are retained, not the screened abstract corpus. Other servers, work without the selected terms, non-English terminology and delayed indexing remain gaps. Supplemental searches included arXiv and JMIR preprints; the newly published journal paper's older JMIR preprint is not a new preprint result.

## Trial registries

Four date-window ClinicalTrials.gov queries and five direct watches yielded **six unique selected-field snapshots**; all six still report `hasResults=false`. Results and contacts were not harvested. The [registry ledger](registry-evidence.jsonl) distinguishes current selected fields from proof of recruitment or efficacy.

- [NCT07137442](https://clinicaltrials.gov/study/NCT07137442): estimated start November 10→11, last update submission November 4→5, posting November 5→6. It still lists RECRUITING, estimated enrollment 75, ages 18–80. These are administrative metadata changes, not demonstrated enrollment, diagnostic performance or benefit.
- NCT01019343, NCT05158439, NCT06194305, NCT07093541 and NCT07905898 have no change in the selected fields compared with November 6. Unchanged metadata does not resolve earlier enrollment discrepancies or establish actual activity.

A supplemental query included WHO/UMIN/ISRCTN/ChiCTR and a Japanese tic term, but it was not an exhaustive direct registry search. The previous UMIN000063483 detail/status chronology remains unresolved. No new recruitment claim is made.

## Official safety review

Six dated search queries and **13 official index/referral/page checks** are recorded in [safety-query-log.json](safety-query-log.json) and [safety-review.json](safety-review.json). A direct EMA index check screened 90 date-stamped headings. Its sole named-watch match was the already historical November 3 Sycrest/asenapine update, not a new-window warning; linked attachments were not exhaustively inspected.

No qualifying new watched-treatment official warning or newly issued tic guideline was verified since the previous safety cutoff (November 6 at 02:54:20 UTC). The HSA tetrabenazine batch recall and EMA Deanxit combination review remain historical; the latter explicitly excludes flupentixol alone. TicCare remains a guideline registration. A search-surfaced Swiss aripiprazole recall is dated April 1, not November. Fresh search-card dates for the TGA product-information page were resolved to its official September 29 update date, with the located methylphenidate item dated July 22. Crawl recency is not event recency.

This is English-heavy surveillance of selected regulators, not complete worldwide pharmacovigilance, every label/attachment, or proof of safety. Individual adverse-event reports were not extracted or retained. No treatment change is proposed.

## Reproduction, limits and next decision

The core made **57 requests: 55 successful responses and two transient failures**, each subsequently recovered at the same API cursor. Live reruns can change. Run `python scan_sources.py --out NEW_DIRECTORY --baseline baseline.json`; `resume_preprints.py` documents this run's bounded failed-cursor continuation. `build_results.py` reconstructs classifications from the captured log; `check_reported_arithmetic.py` reproduces the integer check; `validate.py` verifies bookkeeping and consistency, not clinical validity. No random seed or simulation is involved.

Retain the new study as preliminary pediatric measurement evidence with the denominator issue visible. Require clarified aggregate reporting and independent clinically realistic validation before promoting diagnostic or monitoring claims. Do not collect videos or contact authors as part of this scan. Continue the separately assigned H18 mechanism/generalization audit; this publication does not alter its causal-evidence standard. Persistent severe adult symptoms, pain, function, co-occurring needs and all-age chronic tic evidence remain central. No intervention, outreach, enrollment or paid resource was used, and no repository files were edited during scan preparation.
