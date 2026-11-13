# Historical measurement comparability audit | 13 November 2026

## Question and result

Are observed tic frequency, clinician-rated severity/impairment and participant-described burden interchangeable endpoints? **Not established.** The advance is an explicit estimand/cohort reconciliation and a reproducible reporting-consistency audit, not a new treatment estimate, new discovery, simulation or patient-level reanalysis. The prospective prediction and possible disconfirmation were recorded in [plan.md](plan.md) after candidate summaries were received, before extraction. This is not a blinded preregistration.

[Evidence matrix](evidence-matrix.json) contains original source-linked aggregate extractions. Wellen and Davenport publisher full texts were inspected. Kuhn coverage is limited to the PubMed abstract and indexed primary Methods; direct full-text retrieval failed. Exact Kuhn correlation claims are excluded. No patient narratives or quotations were retained.

## Reconciliation

The three endpoints answer different questions: what an observer counts in a specific recording, how a clinician rates severity and impairment, and which problems a participant reports. Association between two clinician scores is useful counterevidence to any blanket claim that severity and burden never relate. It does not establish calibration of a brief tic count to daily-life burden. Conversely, an insignificant count-change association does not establish independence, equivalence, or absence of a clinically meaningful relationship.

The [cohort map](cohort-map.json) prevents treating two reports from the same Minnesota trial as independent replication. Individual overlap remains unknown. Registry assessments are repeated observations, not additional participants. A pooled estimate would mix incompatible endpoints, statistical estimands and dependence structures, so none was calculated.

The Wellen abstract/full-text contrast is resolved by retaining the adjusted estimate and its interval rather than repeating the broader abstract significance statement. The Davenport time-only statistic fails an elementary arithmetic consistency check: rounded coefficient and SE imply an absolute test statistic between 5.00 and 6.71, not 53.87. The check flags inconsistent reporting; it neither identifies which field is wrong nor invalidates all study results. No corrected p-value is invented.

A further estimand distinction matters: a random intercept accounts for clustering, but does not alone separate within-person change from between-person differences. Without person-mean decomposition or an equivalent identified contrast, the raw-score longitudinal coefficient should not be presented as a pure within-person effect. Observational change also does not identify a treatment effect.

## What was rejected and retained

Rejected: pooling these outcomes, counting shared-trial reports as independent replication, upgrading nonsignificance to equivalence, and treating longitudinal association as causal improvement. Retained: evidence that severity and impairment can covary, that observation context matters, and that burden requires direct measurement. No claim that a patient can or should suppress tics follows.

H18 stays closed at its previously documented boundary: none of the inspected evidence supplies a calibrated context-invariant external anchor. This comparison does not identify a latent biological mechanism. Adults, including those with persistent severe symptoms, cannot be represented by youth-heavy samples or assumed to remit. Evidence about co-occurring conditions and severe adult burden remains incomplete.

## Reproduction and limits

Run `python analyses/measurement_comparability/2026-11-13/validate.py` from the repository. Standard-library-only code reads the aggregate matrix, checks denominators and identifiers against baseline `df5cc76`, and writes [validation-results.json](validation-results.json). No random seed is needed. The baseline identifier audit found no exact PMID/DOI matches; this is an identifier coverage check, not proof that no related topic appeared previously. Source access outcomes and actual check time are in [source-ledger.json](source-ledger.json).

This is a selected three-report comparison, not a systematic review or a fresh-literature scan. The inaccessible Kuhn results limit numerical reconciliation; no exact hassle/severity coefficient is asserted. No raw data, participant re-identification, full papers, or treatment recommendations were produced.

## Next decision

Do not add another unanchored simulation. First obtain lawful accessible Kuhn results text and independently check its endpoint definition and denominator. The next informative literature-only experiment is a preregistered extraction of studies measuring observed counts and an independent burden/function endpoint on the same occasions, checking whether agreement or out-of-sample calibration exists rather than pooling correlations. New participant measurement would require clinician/institutional and ethics review, consent and approved privacy governance; it is not authorized or proposed for automatic execution here.

Primary links: [Wellen](https://link.springer.com/article/10.1007/s00787-025-02818-2), [Kuhn](https://pubmed.ncbi.nlm.nih.gov/41180850/), [Davenport](https://movementdisorders.onlinelibrary.wiley.com/doi/10.1002/mds.70342). These are historical 2025/2026 reports, newly audited here, not newly published since the preceding daily scan.
