# Safety and displayed-link pass - 27 October 2026

## Result and coverage

**No new qualifying material watched-treatment risk or issued tic-care guideline was verified** between the prior cutoff, 26 October 03:00:17 UTC, and this pass ending 27 October 03:16:57 UTC. New official documents did appear; they are not all new safety findings. This is bounded surveillance, not proof of no risk or advice to change care.

Six overlapping date-filtered searches returned 27 displayed cards, not unique events. Old studies, labels, guidance, unrelated records and directories were excluded from new findings. An individual adverse-event card was excluded without retaining its narrative. [Queries](query-ledger.json) and [20 official-source checks](source-checks.json) distinguish dates, document types and access limits.

## What changed at official sources

The [EMA new index](https://www.ema.europa.eu/en/news-events/whats-new) has 25 rows dated October 26, including new PRAC documents. Its search-incompleteness banner persists.

- The [five-page adopted recommendations](https://www.ema.europa.eu/en/documents/prac-recommendation/prac-recommendations-signals-adopted-28-september-1-october-2026-prac-meeting_en.pdf), EMA/PRAC/206892/2026, and [two-page wording](https://www.ema.europa.eu/en/documents/prac-recommendation/new-product-information-wording-extracts-prac-recommendations-signals-adopted-28-september-1-october-2026-prac_en.pdf), EMA/PRAC/206903/2026, were read in full. The official index confirms October 26 publication, distinct from adoption at the September 28 to October 1 meeting. The labeling action concerns binimetinib/encorafenib neutropenia; the other listed substances fall outside the defined watch. These are new documents, but no new watched-treatment risk was identified.
- The [October 26 to 29 agenda](https://www.ema.europa.eu/en/documents/agenda/agenda-prac-meeting-26-29-october-2026_en.pdf), EMA/PRAC/227255/2026, is not an adopted decision. A reproducible 23-term screen found six substring occurrences. They represent two agenda items repeated in contents/body, with tetrabenazine also matching inside deutetrabenazine, not six events. Page 25 lists deutetrabenazine PSUSA/00011177/202603 for adoption; page 20 lists a methylphenidate formulation/strength extension and updated risk-management plan for adoption. Neither passage supplies a new adverse-risk conclusion. [Screen metadata](prac-agenda-check.json). The cumulative signal list was not diffed.
- [MHRA Drug Safety Update](https://www.gov.uk/drug-safety-update) added an October 26 MedSafetyWeek/Yellow Card reporting campaign, not a new watched-treatment warning. Its October 15 antidepressant warning remains historical. The [alerts index](https://www.gov.uk/drug-device-alerts) added an October 26 clopidogrel-liquid recall outside this watch. Six leading headings were screened; the index is nonchronological and issue date need not equal posting date.
- Ten [Health Canada entries](https://recalls-rappels.canada.ca/en) were screened. New October 26 to 27 entries concern other products, including a glucose app, stent and analyzer, not the watched therapies.

## Other checks and limitations

[FDA drug](https://www.fda.gov/drugs/drug-safety-and-availability/drug-safety-communications) and [device](https://www.fda.gov/medical-devices/medical-device-safety/safety-communications) communication indexes still lead with September 15 and June 3. Six leading [CDRH news](https://www.fda.gov/medical-devices/medical-devices-news-and-events/cdrh-new-news-and-updates) headings are October 20; the [latest statement](https://www.fda.gov/drugs/drug-safety-and-availability/drug-alerts-and-statements) is the October 22 ARC annual report. [SrLC](https://www.accessdata.fda.gov/scripts/cder/safetylabelingchanges/) remains a retrieved form, not an executed label-change result set. The historical NeuroStar recall was not separately rechecked today.

[TGA updates](https://www.tga.gov.au/news/safety-updates), [alerts](https://www.tga.gov.au/safety/safety-monitoring-and-information/safety-alerts) and [PI table](https://www.tga.gov.au/product-information-safety-updates-year-table) still lead with October 14, September 14 and September 29. Label approval dates do not establish posting dates. [ESSTS](https://www.essts.org/partners) describes 2022 guidelines and a further update under consideration; [AAN](https://www.aan.com/PressRoom/Home/PressRelease/2721) remains a May 2019 release. [AWMF TicCare](https://www.awmf.org/aktuelles/awmf-aktuell/diagnostik-und-behandlung-primaerer-tic-stoerungen-ticcare) describes planned all-age guideline development, not an issued guideline. [NICE NG127](https://www.nice.org.uk/guidance/ng127) returned 403; current text was not inspected, and the target is not established broken.

Other attachments, full national labeling/recall databases, manufacturer notices, non-English coverage and the AWMF register remain incomplete. The watch is not an exhaustive comorbidity formulary or worldwide surveillance. Existing warnings remain important even without a new qualifying finding.

## Homepage links and activity safety

The [daily ledger](../../../public/link-checks/2026-10-27.json) covers 19 pre-existing timeline targets, three findings and nine additional displayed research/guidance links. All timeline targets, Ivanova's identity-matched PDF, CDC, MedlinePlus and ONLINE-TICS were retrieved. Pappert's publisher returned a 403 bot challenge; the [institutional primary PDF](https://www.rcpsych.ac.uk/docs/default-source/members/devolved-nations/rcpsych-in-wales/wales-cap-objective-assess-longit-outcomes.pdf?sfvrsn=d52dec25_2) was retrieved with matching identity. Isaacs and six PubMed direct routes returned HTTP 203/non-article bodies. The web reader resolved Isaacs and PMID 25044024; five PubMed reader routes remained limited. No target was established broken. Preserve canonical attribution and distinguish client-specific access from outages.

Production `/api/public-feed` and anonymous raw GitHub matched the pinned **October 26 edition**, updatedAt **2026-10-26T03:04:05Z**, with repository-source header. This is a preparation baseline, **not October 27 publication verification**. Homepage/script matched source and live feedback remains disabled with null API origin. Static fallback and old next-question link were unchanged. No rendered/mobile/keyboard/narration QA is claimed.

All six approved activities remain unchanged. Manual review retained optional rest/skip and stop-if-uncomfortable language, without exertion targets, breath holding, tic suppression, food/allergy activities, streaks, points or treatment claims. Voting, comments and health-outcome collection remain disabled; reflection remains unsent page memory. **22/22 checks pass**, not clinical-safety or accessibility certification.

No patient data, personal narrative, source-document copy, contact, clinical action or paid compute was retained or performed. Temporary paper bytes were deleted. Feed/static source and deployment settings were not edited. Integration owns final publication readback.

## Reproduce

Python 3, curl and pdftotext are required. Copy scripts to a temporary directory for fresh network checks without replacing the historical ledgers:

```sh
python check_links.py /path/to/repository
python check_homepage_links.py /path/to/repository
python check_supplement.py /path/to/repository
python check_prac_agenda.py
```

`python validate.py` performs offline dated-ledger checks. New network runs describe current access, not historical access. [Validation](validation.json).
