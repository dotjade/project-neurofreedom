# Watched-treatment safety and displayed-link check - 26 October 2026

## Result and boundary

No new qualifying material watched-treatment safety notice or newly issued tic-care guideline was verified in this bounded pass. Comparison window: **25 October 2026 02:46:31 UTC to 26 October 2026 03:00:17 UTC**. This is not an absence-of-risk claim or exhaustive worldwide surveillance. Existing warnings remain relevant; no treatment change follows.

Six overlapping date-filtered queries yielded **41 displayed search cards**, not 41 independent events. Source publication dates, not crawl dates, governed eligibility. Historical labels, irrelevant pages, old guidance and secondary encyclopedias were excluded. An individual adverse-event search card was excluded without retaining its narrative. [Queries](query-ledger.json) and [18 official-source checks](source-checks.json) preserve the actual coverage.

## Official-source findings

- **FDA:** [Drug communications](https://www.fda.gov/drugs/drug-safety-and-availability/drug-safety-communications) and [device communications](https://www.fda.gov/medical-devices/medical-device-safety/safety-communications) still lead with September 15 and June 3. Six latest [CDRH news](https://www.fda.gov/medical-devices/medical-devices-news-and-events/cdrh-new-news-and-updates) headings are October 20. The latest [statement](https://www.fda.gov/drugs/drug-safety-and-availability/drug-alerts-and-statements) is the October 22 ARC annual report, not a watched-treatment action. [SrLC](https://www.accessdata.fda.gov/scripts/cder/safetylabelingchanges/) supplied a search form, not an executed label-change result set. The known [NeuroStar recall Z-0142-2027](https://www.accessdata.fda.gov/SCRIPTs/cdrh/cfdocs/cfres/res.cfm?id=222521) remains open/classified, initiated August 24 and posted October 9 in inspected fields. It is not a new event; no complete history diff was performed.
- **EMA:** The latest 25 [new-index rows](https://www.ema.europa.eu/en/news-events/whats-new) remain October 23. The search-incompleteness warning persists. The [PRAC index](https://www.ema.europa.eu/en/human-regulatory-overview/post-authorisation/pharmacovigilance-post-authorisation/signal-management/prac-recommendations-safety-signals) leads with September 28 publication. The October 23 minutes release predates this cutoff. Attachments were not re-screened.
- **MHRA:** [Drug Safety Update](https://www.gov.uk/drug-safety-update) leads with October 20; the October 15 antidepressant warning is historical. Seven [alerts-index](https://www.gov.uk/drug-device-alerts) headings were checked. That index is nonchronological and issue dates are not necessarily posting dates. Attachment coverage remains incomplete.
- **TGA and Canada:** [TGA safety updates](https://www.tga.gov.au/news/safety-updates), [alerts](https://www.tga.gov.au/safety/safety-monitoring-and-information/safety-alerts) and [PI table](https://www.tga.gov.au/product-information-safety-updates-year-table) lead with October 14, September 14 and September 29 respectively. Approval dates do not establish posting dates. Ten [Canadian recall-index](https://recalls-rappels.canada.ca/en) entries were checked, newest October 23, without a new-window watched-treatment event. Interactive recall and labeling coverage remain incomplete.
- **Guidance:** [ESSTS](https://www.essts.org/partners) describes version 2.0 in 2022 and a further update under consideration. The [AAN release](https://www.aan.com/PressRoom/Home/PressRelease/2721) is dated May 6, 2019. [AWMF TicCare](https://www.awmf.org/aktuelles/awmf-aktuell/diagnostik-und-behandlung-primaerer-tic-stoerungen-ticcare) remains an October 1 announcement of planned all-age S3 guideline development, not an issued guideline. [NICE NG127](https://www.nice.org.uk/guidance/ng127) timed out in the web reader; its current text was not inspected. The prior AWMF register-access gap remains; that register was not retried today.

Coverage is neither a complete comorbidity formulary nor worldwide pharmacovigilance. National EU, manufacturer, other-country, non-English, labeling and attachment gaps remain. No new finding is different from proof of no risk.

## Displayed links and safe optional catalog

The [daily ledger](../../../public/link-checks/2026-10-26.json) checks **18 pre-existing timeline links**, three findings and nine additional homepage research/guidance sources. All timeline targets, Ivanova's identity-matched PDF, CDC, MedlinePlus and ONLINE-TICS were retrievable. Pappert's publisher returned HTTP 403 with a bot challenge. Isaacs and all six PubMed direct requests returned HTTP 203/non-article content. The web reader resolved Isaacs and two PubMed identities; four PubMed targets remain limited. **No target was established broken.**

Pappert's [institutional primary PDF](https://www.rcpsych.ac.uk/docs/default-source/members/devolved-nations/rcpsych-in-wales/wales-cap-objective-assess-longit-outcomes.pdf?sfvrsn=d52dec25_2) returned HTTP 200 with matching title and DOI. Keep canonical attribution; today's availability is not a future guarantee.

Production `/api/public-feed` and raw GitHub exactly matched the pinned **October 25 edition**, updatedAt **2026-10-25T02:50:28Z**, with the repository-source header. This is preparation-baseline verification, **not October 26 publication**. Live homepage and script matched source; feedback remains disabled with null API origin. Static October 13 fallback and the older ONLINE-TICS next-question link were not changed. No rendered interaction was tested.

All six approved optional activities exactly match the bundled catalog. Rest/skip and stop-if-uncomfortable wording remain. Manual review found no exertion target, breath holding, tic suppression, food/allergy activity, streak, point or treatment claim. No new physical or food activity was added. Votes, comments and health-outcome collection remain disabled; reflection remains unsent page memory. Fourteen source/config safeguards and eight ledger checks pass, **22/22**, not clinical-safety or accessibility certification.

Only original summaries, source metadata and code are retained. Temporary paper bytes were deleted. No participant data, personal narratives, outreach, data request, paid compute or clinical action occurred. No feed/static source or deployment configuration was modified by this worker. Final authored-feed and new-report readback belongs to integration.

## Reproduction

Python 3, curl and pdftotext are required. Network reruns observe current availability, not this historical check. Run from this directory:

```sh
python check_links.py /path/to/repository
python check_homepage_links.py /path/to/repository
python check_supplement.py /path/to/repository
python validate.py
```

The offline validator checks the saved dated ledger. Network reruns create fresh local records; copy these scripts to a temporary directory to preserve the dated artifacts. [Validation](validation.json).
