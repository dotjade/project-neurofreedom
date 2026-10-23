# Independent review of the NCT02056873 historical audit

Reviewed 23 October 2026 for the parent research agent. This review is limited to the historical-registration audit and its reproducibility materials; it does not review the separate literature scan or persistence survey.

## Decision

The historical audit is supportable for publication after the calendar-clock correction already applied by the parent. The central claims are appropriately bounded: dated public registration wording changed, but the evidence does not establish decision dates, reasons, selective reporting, or a paper error. No clinical effect estimate or responder count should be derived from this documentation exercise.

The original opening described six months of continuous stimulation. The registered clock is six months post-surgery, not six months of delivered exposure. The parent replaced this with “at six months post-surgery during continuous DBS”; the corrected report passed the independent check.

Optional wording precision: describe version 24 as the last record before results were posted rather than simply the last pre-results version. The index lists results-submission events under version 24; neither label establishes when investigators knew any result.

## What was independently verified

- A separate ordinary cloud-browser tab rendered the official historical pages without authentication or security changes. I re-extracted only Study Status, Study Design, the first protocol-side Outcome Measures section, and Document Section for versions 1, 7, 8, 13, 23, 24 and 25. All 28 section texts and all seven version URLs exactly match the submitted extracts.
- The independently retrieved 25-row history index exactly matches the saved index, with contiguous version numbers. Its exact protocol-side Outcome Measures change label occurs only at version 25. This is not a full-text comparison of all 25 records.
- Versions 1, 7, 8, 13, 23 and 24 contain the same four declared primary outcome definitions. Version 25 contains one, including 40% total-tic wording and a postoperative six-month clock. The earliest inspected outcome definitions contain no numeric 40% threshold. This absence is limited to those definitions; it is not evidence of absence throughout every contemporaneous research document.
- The version 7 to 8 masking-label boundary is directly supported. Enrollment and the later sequential, two-arm, nonrandomized design metadata agree with the report. These are registry descriptions, not independently reconstructed treatment histories.
- Submission, qualifying QC submission, posting, document date and upload are distinguished correctly. In particular, 3 February 2014 is first submission, 4 February is QC-qualified submission, and 6 February is first posting as displayed. Current results milestones are 18 October 2023, 30 August 2024 and 5 September 2024 respectively. The displayed protocol date is 23 September 2019 and upload is 10 October 2023 at 12:40. A 2019 document date does not establish public availability in 2019.

Sources: [first historical version](https://clinicaltrials.gov/study/NCT02056873?tab=history&a=1#version-content-panel), [masking boundary version](https://clinicaltrials.gov/study/NCT02056873?tab=history&a=8#version-content-panel), [version 24](https://clinicaltrials.gov/study/NCT02056873?tab=history&a=24#version-content-panel), and [version 25](https://clinicaltrials.gov/study/NCT02056873?tab=history&a=25#version-content-panel). The live evidence file contains all seven exact URLs and retrieval times.

## Protocol cross-check

The official 64-page protocol has the recorded 2019 date and matches the submitted SHA-256. Its text supports the audit’s threshold contrasts: total-tic criteria on pages 7, 16 and 32–33; motor-only wording on page 10 and later analysis pages; differing strict and inclusive 40% criteria. Responsive schedules differ across pages 9, 40 and 45. Blinded video ratings and separate mode-testing days remain described on pages 24, 32–33 and 38, so an overall open-label registry label cannot establish that every assessment was unmasked. Page 35 also permits delayed primary assessment if optimization is incomplete. These are within-document differences, not a dated amendment sequence. The evidence supports neither a 2024 invention claim nor a claim that every clause was adopted in 2019. [Official protocol and SAP](https://cdn.clinicaltrials.gov/large-docs/73/NCT02056873/Prot_SAP_000.pdf).

## Reproducibility and limits

The supplied checker was run on a separate copy, leaving the original inputs and outputs unchanged. All 38 checks passed, and its output reproduces the submitted checks.json byte-for-byte. A second review script adds 36 passing checks, including exact live-versus-saved section comparisons, exact index-label matching, milestone sequences, postoperative clock wording and the protocol hash check.

The checker tests saved documentation structure and selected strings. Its prohibited-row sentinel checks are useful safeguards, not a formal proof that every possible form of patient data is absent or that no undesired section was ever seen during original collection. Manual inspection of the retained sections found no participant observation rows; my live extraction avoided the later results Outcome Measures section. Enrollment counts and the protocol’s planned sample-size criteria are metadata, not participant-level reconstruction. No efficacy reanalysis or simulation was performed.

The prediction text explicitly denies preregistration. I reviewed that text but did not independently establish the timing of its composition relative to the original extraction; the report should continue to treat it as a recorded, non-preregistered prediction rather than a prospective study registration.

Access limits: the web reader could not open the historical route, while the ordinary browser successfully rendered it. The web reader supplied protocol text; attempted web PDF screenshots failed with cache misses. The PDF bytes were downloaded in memory solely for hash and page-count checking, with no PDF or full extracted text written to disk. Protocol review is therefore text-based, not a completed rendered-page inspection. No investigator contact, login, participant record access, or full-paper retention occurred. No global search for every possible amendment archive was performed, so lack of a displayed earlier protocol must not be presented as proof that none exists anywhere.

## Review files

- `live-metadata-check.json`: independent live metadata and history-index evidence.
- `protocol-hash-check.json`: independent official-PDF hash and page-count check only.
- `checker_copy/checks.json`: retained output from an isolated rerun; duplicate metadata inputs are not republished.
- `independent_checks.py` and `independent-checks.json`: review checks and recorded input hashes.

No original audit file was modified by this reviewer, and nothing was published by the reviewer. Integration adapted the review script to its repository-relative path and reran it against the final report, whose minor wording/scan-link changes are documented there. The bounded next step is to retain the stated uncertainty and close the historical audit unless new lawful public dated amendment evidence becomes available; repeatedly rereading the same documents will not resolve the missing sequence.
