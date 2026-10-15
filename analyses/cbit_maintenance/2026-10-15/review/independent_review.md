# Independent CBIT maintenance audit

Verified 15 October 2026. Scope: aggregate arithmetic and interpretation for Wilhelm et al. 2012, DOI 10.1001/archgenpsychiatry.2011.1528, PMCID PMC3772729. No participant-level data or new clinical inference.

## Primary source verification

The [publisher full text](https://jamanetwork.com/journals/jamapsychiatry/fullarticle/1307556), especially Methods, Results and Table 4, confirms that six-month CBIT response was observed in 12 of 15 assessed acute responders. There were 24 acute responders. Follow-up status for the other nine was unknown. Both arms' responder protocols included three monthly boosters. PST nonresponders were offered CBIT; the paper states randomized comparison could not continue after week 10. The abstract gives control response as 4/63 (6.4%); Results and randomized allocation support 4/59 (6.8%). The population spanned ages 16–69.

The [PMC flow diagram](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/f10e/3772729/868c530eb647/nihms-500770-f0001.jpg), independently downloaded and visually inspected, shows randomized 63/59, Phase I completed 56/49, and analyzed 60/53. Methods requires at least one postrandomization visit for efficacy analysis. Distinguish the 113 continuous-analysis participants from the 122 CGI denominators.

PMC HTML returned a browser challenge in this independent retrieval; the publisher article was readable. No challenge was solved. The verified diagram is retained only as an audit intermediate.

## Independent arithmetic

The standard-library Python script verify_arithmetic.py enumerates every possible binary success count among missing responders. It writes independent_output.json and independent_output.tsv. All assertions passed.

- Six-month CBIT ascertainment: 15/24 = 62.5%; missing: 9/24 = 37.5%.
- Available-case response: 12/15 = 80%.
- Confirmed response across the original acute-responder denominator: 12/24 = 50%.
- Within those 24 acute responders, assigning the nine unknown outcomes all negative versus all positive gives 12/24 through 21/24, or 50%–87.5%.
- Three-month CBIT bounds: 13/24 through 22/24, or 54.1667%–91.6667%.
- PST bounds at either point: 1/4 through 3/4, or 25%–75%; available-case response 1/2 = 50%.
- The abstract denominator yields 4/63 = 6.3492%, conventionally 6.3% at one decimal, whereas 4/59 = 6.7797%, conventionally 6.8%. Preserve rather than silently fix the reported discrepancy.

These are deterministic missing-outcome bounds for a fixed finite responder cohort, not confidence intervals. The 50% lower endpoint is an observed-confirmed proportion or all-missing-negative scenario; it does not show that all nine missing participants failed. An observed 80% cannot by itself establish 80% across all 24 responders. The bounds do not account for sampling uncertainty or outcome measurement error.

## Interpretation checks

The selected follow-up population and booster protocol cannot identify all-randomized comparative six-month efficacy or off-treatment durability. Pointwise response at six months does not establish uninterrupted response, tic elimination, remission, disease modification or cure. Nine missing follow-up outcomes are distinct from the nine randomized participants omitted from continuous analysis. The article's booster schedule does not by itself verify that each participant completed every booster.

The fraction 12/63 = 19.0476% may be used only as a descriptive count of confirmed acute-and-six-month responders relative to initial CBIT allocation, with that exact label; it is not an estimate of six-month response in all randomized participants. Absence of a positive acute response does not imply absence of a later response. No adult-only conclusion is available from these aggregate counts.

## Worker artifact rerun

PASS for computation files. Read aggregate_inputs.json, aggregate_checks.py, aggregate_checks.json and computation_plan.md in the main worker directory. Ran the supplied script with output redirected to this review directory. All 37 supplied checks passed; rerun JSON exactly matched the saved JSON. A separately authored comparison script checked all extracted counts, rational proportions, bounds and enumerated scenarios against the independent extraction, plus the benchmark and NNT arithmetic: 49 checks passed. SHA-256 values establish that the four worker files were unchanged during review. See review_worker_outputs.py, worker_rerun.json, worker_rerun.log and worker_review_result.json.

The 80% sensitivity benchmark is correctly labelled hypothetical: seven missing positives give 19/24 = 79.1667%, while eight give 20/24 = 83.3333%. The source's NNT of 5 is not reproduced by the unadjusted response fractions: reciprocal risk difference = 3.1933, conventionally rounded upward to 4. The worker discloses this and does not infer an unpublished adjustment.

Final narrative and maintenance-related structured extraction checked. Two wording clarifications were recommended and verified applied: limits on extrapolation to very severe/unstable adults, and a binomial interval for returning acute responders. No numerical or central estimand defect remains in this review scope. See narrative_review.md. Other registry/bibliographic/version details are the main worker's verification scope. No worker files have been altered.
