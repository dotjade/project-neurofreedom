# Independent daily research review: 1 November 2026

## Scientific review

An independent reviewer inspected the primary manuscript XML for [PMID 36002628](https://doi.org/10.3758/s13428-022-01954-w), including methods, Tables 1, 2, 4 and 5 and the reliability/learning paragraphs. The manuscript's August 24, 2022 online date is distinct from the 2023 issue year. The 138-person, single-session design and mean age 24.51 years do not validate a Tourette-specific or persistent-severe-adult biomarker.

The reported .94 direct and .86 slider coefficients are Spearman-Brown-corrected split-half estimates, not test-retest or direct-minus-slider reliability. No coefficient confidence intervals were recovered. A pooled sequence of 64 trials with counterbalanced 32-trial condition blocks is not a condition-specific indirect-learning estimate. Stable average performance, individual rank reliability and repeat-session agreement remain separate claims.

Independently transcribed Table 4 values reproduce the equal-force direct-minus-slider estimates: 0.8925 N at 2–2.5 seconds and 0.7725 N at 2.5–3 seconds. Their difference is -0.1200 N, comprising a -0.025 N direct change minus a +0.095 N slider change. This is descriptive arithmetic on rounded published aggregates, not a new significance test or a simulation. Without within-person covariance, no contrast-change confidence interval is recoverable. A within-trial extraction-window effect is not evidence of across-trial learning.

The separate Table 2 and main-text summaries do not exactly match Table 4; they must not be silently substituted or pooled. The source's slope comparison to a mean error is not adopted as an equivalence margin because the units and intended comparison differ.

## Adjacent retest source

The reviewer separately inspected [PMID 38212469](https://doi.org/10.1038/s41598-024-51644-0), including the live PMC report and original XML. It tests a different contralateral pinch-force construct in 30 healthy young adults across one week, with a two-way mixed, absolute-agreement, single-measurement ICC. Its reported variable-error results are weaker than absolute/constant-error results. It cannot substitute for direct/slider attenuation retest validation.

Conditional on Table 1 spreads being SDs from the same paired observations and units, as its methods appear to state, five printed triples violate the necessary bound |SD1 − SD2| ≤ SDdifference ≤ SD1 + SD2, even allowing rounding at .01. This is a reporting ambiguity, not a determination of its cause. No participant data were inspected and no corrected coefficient, SEM or change threshold is inferred. The adjacent study is excluded from numerical attenuation calibration independently of this concern because its task and construct differ.

## Independent computation

Run `python independent_check.py`. The script records the manually inspected aggregate inputs, uses decimal arithmetic for the main contrasts, and checks conditional SD consistency. All 54 assertions passed, including the scan-screen, final-count and feed checks below. [Machine-readable results](independent-check-results.json) preserve outputs and limitations. No random sampling, seed, participant data or paid compute is involved. Passing these checks validates the stated arithmetic, not the articles' underlying data or clinical interpretation.

## Preprint screening controls

The reviewer parsed the actual Python AST literal and saved JSON screening expressions for October 31 and November 1, rather than judging escaped display strings. The October 31 script exactly matches commit de5f1e43230840aa430f66b5c06443df128deff1. All six expressions match the positive controls “Tourette syndrome” and “chronic motor tics” and reject “statistics”. No historical regex defect or erratum was established. Controls verify this lexical filter only, not complete retrieval or indexing coverage. Eight additional independent metadata checks reconcile the final 17 unique PubMed records, 898 preprint DOI/version records, 48 successful core requests and five unchanged selected registry comparisons. These checks are against saved logs, not a separate exhaustive rerun of the searches.

## Safety source

The official [Singapore HSA notice](https://www.hsa.gov.sg/announcements/recall-of-tetrabenazine-25mg-112-s-sun-italy/) was independently inspected. Its announcement is dated November 1; the recall date is October 27. It concerns one batch, DNG1035A, of Tetrabenazine 25mg 112’s Sun-Italy, a Class 2 retail-level precautionary recall for black spots. This is a batch-specific quality notice, not a new drug-wide, class-wide or Tourette-specific safety effect. Instructions address supplying institutions. No treatment change is proposed and no patient exposure is inferred. Exact within-day publication time is unavailable.

## Older scan records

The reviewer independently opened the official PubMed records for [PMID 42664664](https://pubmed.ncbi.nlm.nih.gov/42664664/) and [PMID 42617303](https://pubmed.ncbi.nlm.nih.gov/42617303/). Their August electronic dates precede their November issue dates. The first is an observational protective-care sample, not a Tourette-selected medication comparison; the second is a secondary review, not new primary participants. The daily report correctly avoids inventing a Tourette subgroup denominator, treatment effect, or Tourette-specific withdrawal estimate from review-wide results. Both remain abstract-limited extractions.

## Public-feed integration

Eleven independent feed checks pass: the six activity objects and disabled feedback configuration exactly match the pinned prior edition; rest-or-leave is an existing selection; research/activity/entry dates are November 1; updatedAt is not future-dated; the timeline remains within 24 entries with the preceding 23 preserved; no em dash is introduced; and no new clinical result is claimed alongside the narrow one-batch regulatory summary. The report and STATUS preserve clinical-scope and uncertainty limits. This is source review, not proof of deployment.

## Review limits

This review did not access participant datasets, re-estimate reliability from raw data, validate a clinical biomarker, exhaustively search all correction notices, or perform rendered/mobile/narration tests. PubMed/PMC access differed across routes; a browser challenge is not a broken citation. Final source publication and live feed verification belong in the separate publication receipt.
