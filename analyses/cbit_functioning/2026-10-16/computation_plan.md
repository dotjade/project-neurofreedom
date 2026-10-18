# Bounded aggregate computation

Specified after source extraction, before executing the computation, 16 October 2026.

## Purpose

Check how much support the printed exploratory functional tests provide without treating their p-values as confirmatory or recovering unavailable patient-level information.

1. Count nominal p < .05 functional tests in each distinct estimand: randomized acute contrast (Table 1), postrandomization responder association (Table 2), and selected CBIT responder/completer time effect (Table 3).
2. Apply Holm and Bonferroni sensitivities separately to the 12, 12 and 11 tested functional rows. Parental role has no follow-up test and is excluded from the Table 3 family, not assigned a p-value. These restricted families are chosen after seeing the report. They do not adjust the complete study's testing, restore confirmation, or address selection bias. Validity of Bonferroni/Holm as a mathematical correction does not depend on endpoint independence.
3. Calculate arithmetic change contrasts from rounded displayed means for descriptive orientation only. These are not reconstructed model estimates, confidence intervals, treatment-effect heterogeneity tests or meaningful-change thresholds. Lower scores mean less disability or poorer adjustment resolved, not tic absence.
4. Audit reported flow counts and denominator conflicts. Do not recompute the completed October 15 maintenance sensitivity.

No standard error of a within-person change or difference-in-changes is inferred from marginal standard errors; their covariance is unavailable. No F-distribution calculation is attempted without the reported degrees of freedom. No unreported outcome denominator is reverse-engineered from rounded F/partial eta-squared values. No individual outcomes, adult-only estimate or joint-response analysis is manufactured.

The computation is deterministic, uses Python's standard-library Decimal arithmetic, and needs no random seed or external packages. A synthetic implementation test of the correction routines is an implementation check, not a biological simulation.
