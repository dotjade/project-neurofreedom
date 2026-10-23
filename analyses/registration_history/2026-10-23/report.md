# A registry's current endpoint is not its complete history

Project NeuroFreedom | 23 October 2026 | Historical registration/protocol audit, not a new clinical result

## Decision

The official history of **NCT02056873** establishes dated changes in the public registration. It does **not** establish when each analysis decision was made, why the wording changed, selective reporting, or an error in the paper. Do not repair responder counts or compute a new efficacy estimate from these documents.

The earliest record lists four primary outcomes, including a responsive-versus-continuous YGTSS comparison through 24 months. The latest record lists one primary outcome, a count reaching 40% total-tic reduction at six months post-surgery during continuous DBS. This 2024 registry wording is not evidence that all those details were present in the 2014 registration. Conversely, the public protocol dated September 2019 already contains 40% criteria, so it would also be wrong to say the threshold was invented in 2024.

## Today's distinct new-evidence scan

The [daily scan](../../../updates/2026-10-23/report.md) added two newly indexed, earlier-published observational reports about adult persistence and ASD-related tic measurement. Those positive discovery results are separate from this historical audit; neither study establishes treatment efficacy or individual prognosis. No new relevant trial result was verified.

## Prediction and method

[Prediction](prediction.md) was recorded before detailed version extraction, after orienting to the prior audit. It anticipated that dated documents would distinguish some definitions but not resolve their rationale. This was not preregistered. Consistent outcome definitions and clocks across versions would weaken the change prediction; unavailable history would be an access limit, not evidence of bias.

Read the required repository documents and October 22 audit at commit `7d609957041a0a3be47fab331bf74dd838998927`. Inspected all 25 rows of the official history index, then seven selected versions: 1, 7, 8, 13, 23, 24 and 25. Selection covers the first record, the masking-change boundary, enrollment/design-change entries and the last-before-posted-results/current entries. The history index identifies Outcome Measures changes only in version 25 after the initial record. This is an index-guided audit, not full-text comparison of every intermediate version.

Browser extraction was restricted to protocol-side outcome definitions, design, status and document metadata. Version 25 has two identically named Outcome Measures headings. An initial selector also returned its aggregate results summary; the selector was narrowed to the first heading, and that extra results section was not retained or used. No individual measurement row, case narrative, participant reconstruction or efficacy reanalysis was performed. The current protocol/SAP was read in memory; no PDF or unlicensed paper is retained.

## Dated registration findings

| Official version | Submitted date | Posted date shown in version | Finding |
|---|---|---|---|
| 1 | 4 February 2014, QC-qualified submission | 6 February 2014, marked estimated | Four primary outcomes: continuous total-tic reduction at six months; physiology/gamma association through 24 months; responsive-versus-continuous YGTSS comparison through 24 months; continuous total-tic reduction at 24 months. No numeric 40% response threshold in these outcome definitions. Single group, one arm, double masking of participant/outcome assessor, planned enrollment 10. |
| 7 | 5 June 2015 | 8 June 2015, estimated | Same outcome definitions and double-mask label. |
| 8 | 25 November 2015 | 26 November 2015, estimated | Masking label changes to open label. Same outcome definitions, one group, planned enrollment 10. |
| 13 | 9 November 2017 | 14 November 2017, actual | Planned enrollment becomes 20. Same outcome definitions; open label. |
| 23 | 21 December 2021 | 22 December 2021, actual | Enrollment now 10 actual. Same four outcome definitions. |
| 24 | 13 June 2023 | 15 June 2023, actual | Last record before results were posted; same four primary outcome definitions. No protocol document displayed in this version's document section. |
| 25 | 30 August 2024 | 5 September 2024, actual | One primary outcome: number with 40% reduction in total YGTSS tics with continuous DBS, baseline to six months after surgery. Total tic scale explicitly 0-50. Sequential assignment, two arms, nonrandomized, open label; enrollment 10 actual. Protocol/SAP and consent document metadata appear. |

Sources: [history index](https://clinicaltrials.gov/study/NCT02056873?tab=history), [first version](https://clinicaltrials.gov/study/NCT02056873?tab=history&a=1#version-content-panel), [last record before posted results](https://clinicaltrials.gov/study/NCT02056873?tab=history&a=24#version-content-panel), [current historical version](https://clinicaltrials.gov/study/NCT02056873?tab=history&a=25#version-content-panel). Saved extracts include exact version URLs, observed text and retrieval timestamps.

The first submission date was **3 February 2014**, while the first QC-qualified version is **4 February**. Do not conflate submission, QC or posting. Version 25 gives results first submitted **18 October 2023**, first meeting QC **30 August 2024**, and first posted **5 September 2024**. These are reporting milestones, not dates of clinical benefit. The current actual primary completion is **25 August 2021**, study completion **24 August 2023**; earlier version 24 had an estimated June 2023 completion. No conclusion about the reasons for timing changes follows.

## Protocol counterevidence and unresolved amendments

The sole displayed protocol/SAP is dated **23 September 2019**, uploaded **10 October 2023 at 12:40**. Its 64-page text supplies important counterevidence to overinterpreting the 2024 registration edit:

- Pages 7 and 16 describe a greater-than-40% total motor/phonic tic reduction; pages 32-33 again use total motor/phonic tic score at six months.
- Page 10 instead uses greater-than-40% motor-subscale reduction, with six of ten meeting the study effectiveness criterion. Pages 41-44 mix total-tic and motor-only wording, and greater-than versus at-least-40% criteria. These are inconsistencies within one dated document, not a demonstrated sequence of amendments.
- Responsive stimulation is already a study aim in the initial registration, so it is not newly introduced by the 2024 paper. In the 2019 protocol, page 9 describes up to four one-week chronic responsive tests after month 6 and before month 36; page 40 instead describes month-long periods, plus or minus 14 days, between months 6 and 36; page 45 refers to month-long tests after month 3. We cannot collapse those clocks into one verified actual exposure period.
- The 2015 open-label registry change does not prove that every later assessment was unblinded. The 2019 protocol still describes blinded video assessments and separate mode-testing days. Overall chronic treatment allocation and masking of a particular outcome are different design properties.

[Official protocol/SAP](https://cdn.clinicaltrials.gov/large-docs/73/NCT02056873/Prot_SAP_000.pdf). It is publicly hosted despite historical confidentiality text in its footer; no document copy is republished. No dated earlier protocol or amendment log was established in the displayed registry documents. A document's stated 2019 version date and 2023 upload do not prove when every clause was adopted or approved. Thus **first incorporation of motor-only criteria and exact responsive timing remains unresolved**. The October 22 paper/functional analysis is not repeated or numerically repaired.

## Actual result and uncertainty

The prediction was partly supported: public endpoint/design changes can be dated and the 2019 document predates the latest registered 40% endpoint. It was not possible to identify a clean, internally consistent amendment sequence. The missing prerequisite is a lawful public dated earlier protocol/amendment trail or aggregate methods clarification, not individual patient records or investigator contact.

This is selected severe-adult surgical-trial documentation, not an estimate for all Tourette/chronic tic disorders, children, untreated psychiatric comorbidity or every adult trajectory. Persistence, functional burden and unmet needs remain central; neither remission nor treatment success is assumed. No new clinical effect, causal mechanism, durable disease modification or cure is established. Registry absence of a formerly listed endpoint is not proof that no data were collected or reported elsewhere.

Access: the web reader could not open the history route, but the ordinary cloud browser rendered it successfully without authentication or security changes. The initial shell-only HTTP page is not the rendered historical record. Saved metadata supports an offline deterministic comparison; it is not an independently validated clinical dataset. No simulation was run and no random seed applies.

## Next decision

Close this historical audit unless new public dated amendment documentation appears. Do not repeatedly reopen the same missing-history question. Next audit the newly indexed adult persistence survey by Kaylor and colleagues (PMID 42903303, DOI 10.3389/fpsyt.2026.1948693): distinguish retrospective associations from prospective prediction, map invitation/response/analysis denominators and persistence definitions, and test how selection and recall limit claims about severe adult outcomes. Use published aggregates only; do not reconstruct individual data or infer a patient's prognosis.

## Reproduction

Run `python check_history.py` in this directory. It checks saved version identity, the seven inspected metadata extracts, unchanged early outcome definitions, latest outcome count/threshold, date distinctions, selection scope and prohibited-row exclusions. `browser-extraction.js` records the read-only DOM extraction logic for the observed official pages; a current supported browser session is required to repeat live retrieval. Outputs are documentation checks, not statistical tests of clinical efficacy.

## Independent check

A [separate source review](review/history-review.md) re-extracted all seven selected versions and the 25-entry history index, matching all retained section texts. It confirmed the official protocol hash and corrected a calendar/exposure-clock phrase before publication. The original checker reproduced 38/38 checks; 36 independent checks passed. These are source/documentation checks, not clinical peer review or efficacy replication. The final integration adds a scan cross-link and clarifies that version 24 precedes posted results, not necessarily all knowledge of results.
