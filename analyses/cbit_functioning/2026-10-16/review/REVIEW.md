# Independent audit: McGuire functioning analysis

Audit date: 16 October 2026. Source: [NIH author manuscript, Tables 1–3 and Figure 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC7190082/), PMID 31451122, DOI 10.1017/S0033291719002150. The full text was independently retrieved through the official PMC HTTP endpoint. The original manuscript and image are not included in this deliverable.

## Verdict

The bounded interpretation and numerical results pass independent review. These findings constrain functional claims; they do not establish equivalence, a general lack of benefit, or an individual treatment recommendation.

- All 12 randomized acute functional comparisons have printed p values above .05, ranging from .13 to .70.
- The two nominal Table 2 positives compare response groups pooled across treatment arms. They are postrandomization associations, not randomized effects or evidence that tic reduction caused functional improvement.
- Follow-up analysis selects CBIT responders who returned; responders were offered/planned to receive booster sessions; actual attendance was not established. It cannot establish controlled or off-treatment durability.
- SDS total has omnibus p=.03. Its posttreatment cell alone carries the baseline-difference marker; the six-month cell does not. Work disability carries that marker at both visits. A six-month SDS total pairwise p is not supplied.
- The figure and prose disagree on PST follow-up count. The screening flow also fails arithmetic. Neither discrepancy has been silently repaired.

## Independent numerical checks

A separate HTML-table parser extracted printed functioning numbers without copying the main extraction. After suppressing the single-participant follow-up row, all 363 numerical cells checked against the main input agree. A separate Decimal implementation reproduces all 144 checked corrections, displayed-mean contrasts, change calculations, and pairwise markers in the main output. No discrepancies were found.

Restricted families contain 12, 12, and 11 tests respectively, with 0, 2, and 2 nominal p<.05 results. None survives Holm or Bonferroni correction within its family. The two responder associations each become .24. Follow-up SDS total becomes .33 with either procedure; work becomes .40 with Holm and .44 with Bonferroni. These are original post-hoc sensitivity calculations over restricted families, not the authors' study-wide adjusted results. They do not remove selection bias or establish confirmatory evidence. Ordinary rounding of printed hundredth p values cannot change the absence of corrected positives under these families.

The implementation uses synthetic routine checks, not simulated clinical data. The main implementation and tests were reviewed and rerun without modifying their files; all 13 tests passed after the final privacy revision. The final main inputs and outputs were also checked to confirm that single-participant scores and changes are absent.

## Limits retained

Marginal standard errors do not supply within-person covariance. No standard error of change, treatment-effect confidence interval, F-test degrees of freedom, outcome-specific sample size, adult-only estimate, equivalence margin, clinically meaningful threshold, or individual outcome was reconstructed. Arithmetic contrasts of rounded adjusted means are descriptive checks, not replacements for the reported model estimates. Nonsignificance and nonsignificant baseline-completer comparisons do not establish absence of selection or missing-data bias.

## Privacy and reproducibility

The follow-up parental-role row has only one complete participant. Its numerical scores and changes are absent from the reviewer inputs, code, and outputs; only n=1 and untested metadata remain. Other parenthood-related results are not assigned an unreported denominator. No private data, full-paper copy, or figure is included.

- `extract_independent.py`: optional independent extraction from already retrieved primary HTML; automatically suppresses the single-participant row.
- `independent_inputs.json`: sanitized published aggregate extraction and provenance.
- `audit_independent.py`: offline independent audit. Run with Python 3; no external package needed. It reads the adjacent main files only for cross-checks.
- `independent_audit_output.json`: reproducible audit results.
- `main_test_rerun.txt`: test-run evidence.

No repository changes or commit were made by this reviewer.
