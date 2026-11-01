# Independent source and numerical review

1 November 2026. AI-assisted independent verification, not clinical peer review.

## Verdict

PASS for the fixed published-aggregate calculation and its stated limits. Twenty-nine independent checks pass; the ten author unit tests also pass on independent execution. `independent_check.py` does not import `analyze.py`: Wilson limits are derived by solving the score-test quadratic, risk-ratio variance from binomial non-event counts, and arm subtraction checked in integer cents. Results and input/output hashes are saved in `independent-results.json`.

The unadjusted risk difference is 0.1278409091, Newcombe-Wilson95% interval −0.0394376955 to 0.2578374467. The approximate log-Wald risk ratio is 2.40625, interval 0.7437854272 to 7.7845556673. These are different estimators from the primary center-stratified analysis, not a reconstruction or correction. Sparse placebo events limit the approximate RR interval. No clinical importance threshold or equivalence follows.

All five reported functional intervals contain zero. Four displayed arm-LSM subtractions reconcile; the VAS row differs by −6.38 points from the printed contrast, far outside the conditional ±.015 rounding envelope. This verifies reporting inconsistency only: it does not identify the correct cells or invalidate all outcomes.

## Source review

The independent extraction inspected the lawful primary DNB PDF in memory. Web screenshot failed; a separate ordinary HTTP200 fetch and local page7 render succeeded. All five focal Table3 rows and Table4 counts were visually checked; source PDF was never saved and temporary PNG deleted. Main-paper Methods2.7 establish exploratory ANCOVA, baseline imputation and LOCF. The conventional score directions are not proof of the exact trial-specific scoring implementation.

Paper primary CI[−.28,.01] and registry CI[−.2688,.0131] remain unchanged; they cannot be silently reconciled as ordinary rounding. Registry threshold titles versus descriptions are inconsistent. Ninety-eight randomized, ninety-seven treated/analyzed, and seventy-two registry completers are distinct denominators. The five functional headers do not identify observed complete-case counts. Registry adverse-event ascertainment is systematic; the section labelled non-serious includes all events, so do not add SAE totals again. No participant narratives are retained.

Before publishing, ensure inputs/report include the successful visual QA update rather than the initial screenshot-only failure. Extractor’s latest files are under `/workspace/shared/nf-weekly-nov1-review/canna/`. No source full text or QA image should be published.

## Next safe discriminating step

First inspect the publicly separated aggregate supplementary Table4 and methods for this trial. Ask whether functional estimates remain compatible across declared missing-data approaches, and whether those approaches assess informative attrition or merely offer another MAR/LOCF-based analysis. Preserve each estimator, observation count and interval. A stable estimate across assumptions does not validate those assumptions. Stop if only participant rows or contact can resolve the gap.

A subsequent direct-function candidate is the same-trial fitness-to-drive report, PMID38265476, DOI10.1089/can.2023.0114. It is not an independent replication or proof that driving is safe. Verify selected substudy denominators, comparator, baseline/timepoint and any prespecified noninferiority margin before calculating anything. Neither step returns to repeated marker validation or invents a meaningful-change threshold.

No policy denial, outreach, clinical action, participant access, paid resources, global file edits or publication performed.
