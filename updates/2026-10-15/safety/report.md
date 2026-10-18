# Tic-treatment safety scan — 15 October 2026

## Result

No additional qualifying new watched FDA, EMA or MHRA safety notice was verified in this bounded scan. This is a search result, not evidence that no adverse effects or unlisted notices exist.

The known EMA Intuniv document update dated 13 October and FDA NeuroStar recall posted 9 October were rechecked and excluded from the new count. Their already-recorded safety context remains in the [14 October report](https://github.com/dotjade/project-neurofreedom/blob/main/updates/2026-10-14/safety/report.md).

- Incremental cutoff: 14 October 2026, 02:49:22 UTC, the prior safety scan's retrieval end
- Deliberate publication-date overlap: 13–15 October 2026
- Actual web retrieval interval: approximately 15 October, 02:57–02:59 UTC
- Searches: 17 exact queries in six batches; 65 returned result cards screened
- Direct checks: 14 official source URLs attempted; 12 gave usable current pages, one returned stale/inconsistent listing content, and one date-filtered database URL was inaccessible
- New qualifying notices: 0
- Known notices retained for deduplication: 2

## Scope and dates

Drugs: ecopipam; aripiprazole, risperidone, pimozide, haloperidol; clonidine, guanfacine; valbenazine, deutetrabenazine, tetrabenazine. Devices: median nerve stimulation/Neupulse, rTMS and deep brain stimulation.

Publication dates, regulatory event dates, document dates and page-footer revisions were kept separate. Most sources do not supply an exact within-day publication time, so overlap is used rather than assigning unsupported UTC timing.

## Regulator checks

### FDA

The [drug communications index](https://www.fda.gov/drugs/drug-safety-and-availability/drug-safety-communications) still has 15 September as its newest visible dated notice. The [device communications index](https://www.fda.gov/medical-devices/medical-device-safety/safety-communications) still leads with 3 June.

The [drug news page](https://www.fda.gov/drugs/news-events-human-drugs/whats-new-related-drugs) now has an unrelated bladder-cancer indication dated 14 October. The [recall/public-alert index](https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts) has three 14 October rows: an argatroban particulate recall and two sesame-allergen food entries. All are outside the watchlist.

[NeuroStar recall Z-0142-2027](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRES/res.cfm?id=222521) still shows 24 August firm initiation and 9 October FDA posting. Core extracted fields remain consistent with the baseline: Class II, open/classified, out-of-spec HP coil cables, 179 units. Its current footer says 13 October rather than the prior 12 October footer; no event-level substantive change is evidenced. This is not counted as a new notice. No patient-injury mechanism or count is inferred.

### EMA

The [What's New index](https://www.ema.europa.eu/en/news-events/whats-new) displayed 35 rows dated 14 October and 26 dated 13 October, with no 15 October row. No named watchlist medicine appeared among the 14 October rows. The 13 October Intuniv row is already catalogued.

The [Intuniv page](https://www.ema.europa.eu/en/medicines/human/EPAR/intuniv) still dates the inspected product-information, RMP and procedural-history updates to 13 October, and identifies procedure VR/0000334464 dated 3 September. This check verifies metadata, not a new label analysis.

The [PRAC signal index](https://www.ema.europa.eu/en/human-regulatory-overview/post-authorisation/pharmacovigilance-post-authorisation/signal-management/prac-recommendations-safety-signals) still leads with the August–September meeting recommendations published 28 September. One ambiguously titled new 14 October document was inspected and excluded: it concerned management-board administration.

### MHRA

The [Drug Safety Update index](https://www.gov.uk/drug-safety-update) still leads with 2 September. The [drug/device alerts index](https://www.gov.uk/drug-device-alerts) still leads with unrelated CRRT/echinocandin advice issued 13 October. The [October field-safety list](https://www.gov.uk/drug-device-alerts/field-safety-notices-for-october-2026), published 9 October, still contains the unrelated Nova StatStrip ketone-strip entry.

## Coverage and limits

This is an incremental public-notice scan, not exhaustive regulatory surveillance. Search filters returned historical material and some irrelevant government sources; actual official dates controlled classification. Returned-card counts are not unique-event counts or database totals. Search batches did not identify which query produced each card.

FDA's press-release recall list is incomplete by design. A date-filtered device database URL was inaccessible, and a different database listing returned stale September content despite October search snippets; neither supports a no-recall conclusion. Individual active ingredients were not exhaustively enumerated in FDA safety-labeling databases, and current labels were not compared byte by byte. National EU notices, private manufacturer communications and raw adverse-event cases were not systematically searched. Indexing delays can conceal recent notices.

No treatment recommendation, outreach, participant collection, repository commit or external state change was made. Only original summaries, metadata and links were saved; no full-text sources or identifiable participant data are included.

Files:
- [Exact search queries and screening log](search-log.json)
- [Official source checks and retrieval limitations](source-checks.json)
- [Known-notice deduplication records](regulatory-evidence.jsonl)
