# Tic-treatment safety and displayed-link review — 17 October 2026

## Result

No additional qualifying FDA, EMA or MHRA safety notice was verified for the watched tic therapies or material ADHD/OCD medication-care context in this bounded early-day review. This does not establish that no adverse effects, unindexed notices or unsearched label changes exist.

The known October 15 MHRA antidepressant communication, October 13 EMA Intuniv document update and October 9 FDA NeuroStar recall remain prior-seen records. A new posting date, document or footer does not by itself demonstrate a new risk.

Two specific FDA access gaps from October 16 were resolved: both Medline recall records identify surgical convenience kits outside the named watched tic devices. Broader FDA coverage remains incomplete.

## Scope, timing and method

- Baseline documents were read from the repository default branch before searching: README, protocol, status, public-journal README, current feed, October 16 safety report and link ledger. File identities are in [repository-provenance.json](repository-provenance.json).
- Requested prior cutoff: approximately October 16, 02:46 UTC. The prior report additionally records contextual-notice verification at approximately 02:51 UTC; that MHRA item is already known.
- Publication-date overlap: October 15–17. Actual research retrievals: approximately October 17, 03:13:28–03:17:12 UTC.
- Sixteen unique search queries were submitted. The first four-query batch was repeated once to retain a complete URL inventory. Four retained result sets contain 70 cards, including duplicates and irrelevant/history/resource pages; that is not a count of unique events or exhaustive surveillance. [Exact queries and screening](search-log.json).
- Twenty-one distinct official-source paths were attempted, including a failed initial SrLC path later corrected and an inaccessible filtered recall listing. [Source checks](source-checks.json).
- Core watch: ecopipam; aripiprazole, risperidone, pimozide, haloperidol; clonidine, guanfacine; valbenazine, deutetrabenazine, tetrabenazine; median-nerve stimulation/Neupulse, rTMS and DBS.
- Supplementary queries covered topiramate, botulinum toxin and tiapride, plus ADHD/OCD terms and methylphenidate, atomoxetine, lisdexamfetamine, fluvoxamine, sertraline and antidepressants. This was a bounded expansion, not complete surveillance of every comorbidity treatment.
- Regulator sources supplied the evidence. No media/news report was used as primary safety evidence. Search freshness labels, approval records and device listings were not treated as new safety notices.

## Official-source findings

### FDA

The [drug-communications index](https://www.fda.gov/drugs/drug-safety-and-availability/drug-safety-communications) still leads with September 15, and the [device-communications index](https://www.fda.gov/medical-devices/medical-device-safety/safety-communications) with June 3. The [CDRH index](https://www.fda.gov/medical-devices/medical-devices-news-and-events/cdrh-new-news-and-updates) leads with October 15 items unrelated to a watched-device safety change.

Freshness improved for two previously limited indexes:
- The [drug-news page](https://www.fda.gov/drugs/news-events-human-drugs/whats-new-related-drugs) now shows an October 16 eye-drop approval and an October 15 hidden-ingredient notice. Direct review identified the latter as a sexual-enhancement product, outside scope.
- The [recall public-notice index](https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts) now shows October 16 and 15 food recalls. FDA explicitly warns that this index does not contain every recall.

[NeuroStar Z-0142-2027](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRES/res.cfm?id=222521) retains August 24 initiation and October 9 posting, open/classified status and an HP-coil cable-specification issue. Its footer advanced from October 14 to 15; no new substantive event was established from that footer.

Yesterday's unresolved cards now read successfully:
- [Medline Z-0174-2027, record 222811](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRES/res.cfm?id=222811): laparoscopy/transplant and catheter-laboratory convenience kits. Initiated September 2; posted October 15.
- [Medline Z-0189-2027, record 223070](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRES/res.cfm?id=223070): foot/ankle convenience kit classified as a pneumatic tourniquet. Initiated September 11; posted October 15.

Both are excluded from the watched-device count after product identification. These narrow gaps can be closed without claiming complete FDA coverage.

The October 15–17 filtered device-recall listing remains inaccessible through the web tool. The verified [SrLC database search form](https://www.accessdata.fda.gov/scripts/cder/safetylabelingchanges/) is readable, but no in-window result set or ingredient-by-ingredient enumeration was executed. A failed guessed overview path was corrected; it is not evidence that SrLC itself is unavailable.

### EMA

The [What's New index](https://www.ema.europa.eu/en/news-events/whats-new) now contains 38 October 16 rows and 17 October 15 rows; none names a watched medicine. Updated generic safety-signal timetables are process documents, not newly established product risks.

[Intuniv](https://www.ema.europa.eu/en/medicines/human/EPAR/intuniv) retains October 13 product-information/risk-management metadata and procedure VR/0000334464 dated September 3. No new label-text comparison was performed. The [PRAC signal index](https://www.ema.europa.eu/en/human-regulatory-overview/post-authorisation/pharmacovigilance-post-authorisation/signal-management/prac-recommendations-safety-signals) still leads with recommendations published September 28.

### MHRA

The [October 15 antidepressant communication](https://www.gov.uk/drug-safety-update/antidepressants-new-safety-measures-for-all-patients-to-improve-communication-of-the-risk-of-suicidal-thoughts-and-behaviours-and-persistent-sexual-dysfunction) remains the latest displayed Drug Safety Update. It concerns communication of established risks, with patient-information warning/card measures; the supporting leaflet remains planned for 2027. It is retained as known comorbidity-care context, not a new risk discovery, Tourette treatment result or personal medication instruction.

The [alerts index](https://www.gov.uk/drug-device-alerts) is not strictly chronological but showed no newly qualifying October 16–17 notice; its latest visible issuance was October 13 for unrelated CRRT advice. The [October field-safety list](https://www.gov.uk/drug-device-alerts/field-safety-notices-for-october-2026) retains October 9 and the unrelated ketone-strip item.

## Displayed links and live baseline

[link-ledger.json](link-ledger.json) records ordinary anonymous HTTP GETs, redirects, status, target/content checks and actual timestamps, approximately 03:14:20–03:14:43 UTC.

- All 9 displayed repository timeline links returned HTTP 200 and rendered the expected repository path/article.
- Isaacs 2024 returned HTTP 200 with matching title, DOI and PMCID.
- Ivanova 2026 returned HTTP 200 with PDF magic bytes; temporary text extraction matched the author and DOI.
- Pappert 2003 returned HTTP 403 with a browser-challenge page. The target article was not read through this route; the link is access-limited, not established broken.
- Confirmed broken links: 0. Recommended replacements: 0.
- Production /api/public-feed and raw GitHub both returned HTTP 200 and exactly matched the repository October 16 JSON. Production reported X-Journal-Source: repository, updatedAt 2026-10-16T02:53:02Z and lastResearchDate 2026-10-16.

This verifies the existing baseline only. It is not an October 17 publication claim, a new deployment or rendered-page accessibility testing.

## Approved activity catalog

The existing six ideas and voluntary rest/skip alternatives are intact. The baseline still features notice-one-thing with activityEditionDate October 16. No new activity, treatment claim or mandatory progression was introduced. This is a content/governance review, not an individualized clinical safety assessment. Feedback/voting remains disabled, with sampleSize 0 and empty aggregates/trend.

## Limits and next decision

Retain overlap in future scans. Do not repeatedly flag the two resolved Medline records as unknown. Continue to distinguish FDA source freshness from complete recall/label coverage. No byte-for-byte label comparison, exhaustive national EU/manufacturer search or individual adverse-event analysis was performed. Search cards and page indexes can lag publication; precise within-day publication times were generally unavailable.

No medication change, clinician outreach, participant collection, transaction, repository commit or feed edit was made. Only original summaries, source metadata/links and verification artifacts were retained. A separately encountered literature case report is not counted as a regulator notice or causal safety finding.

Supporting records: [regulatory evidence](regulatory-evidence.jsonl), [source checks](source-checks.json), [search log](search-log.json), [link ledger](link-ledger.json).

