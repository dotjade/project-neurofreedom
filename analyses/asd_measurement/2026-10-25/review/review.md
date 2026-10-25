# Independent review: ASD age and impairment audit

Checked 25 October 2026 against a fresh official PMC XML response for PMID 42902960, DOI 10.1002/mdc3.70882. The response hash and access time are in `source-provenance.json`. No article body, individual data or supplement document was retained.

## Results

- 34 independent checks passed: identifiers; all selected table cells; independently parsed means, coefficients, confidence intervals and p values; model counts; sample coverage; subset-overlap bounds; support-level arithmetic; supplement inventory; rerun and byte comparison.
- All 30 parent checks also passed in a disposable copy, without modifying parent outputs.
- Methods/Discussion review supports the scope distinction: a pooled age-adjusted cross-sectional coefficient is not an adult-specific estimate, a longitudinal trajectory, a causal treatment estimate or a direct test of communication-related measurement bias.
- The measured adjusted impairment association and null severity finding are both retained. Nonsignificance is not described as equivalence, and possible reporting differences are not asserted as proven bias.
- The visible supplement inventory contains a disclosure statement, not adult-stratified outcomes. No additional research data were accessed or requested.

## Wording correction verified

The original overlap paragraph said the feasibility interval was not evidence that “different people were necessarily omitted.” Given reported model sizes 483 and 485 within the same cohort, the omitted sets cannot be identical. Suggested replacement: “not observed overlap or identification of which people were omitted; at least two model-inclusion statuses differ because the counts differ.” The parent applied the correction and it was read back successfully at 02:48 UTC. This does not change the 433–483 overlap range or main conclusion. No blocking correction remains.

## Limits

This is an independent AI-assisted source/arithmetic check, not clinical peer review or participant-data verification. The source is the official public main paper plus supplement inventory; no private data or undisclosed analyses were inspected. Absence of an adult-specific or measurement-validation result is restricted to the inspected report, not the entire literature. Arithmetic checks do not validate clinical measurement, causality or generalizability.

## Reproduction

`python independent_checks.py` rechecks live source facts and runs the parent checks in a temporary directory. It supports both the original sibling `day25_asd` layout and the integrated `review/` subdirectory layout. Live XML bytes may change; compare the new hash rather than assuming a fixed source snapshot.
