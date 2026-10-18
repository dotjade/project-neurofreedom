# Post-extraction computation plan

15 October 2026. The scientific prediction preceded source retrieval; these formulas were specified after count extraction and before execution. This is not a trial preregistration or an independent clinical analysis.

For each arm and follow-up visit let A be the number of acute responders, O those assessed, and R those still CGI-I positive. Missing count M=A−O. Calculate ascertainment O/A, available-case response R/O, and documented response R/A. Enumerate integer m=0,…,M hypothetical positive outcomes among missing acute responders. Full acute-responder proportions are (R+m)/A, with deterministic bounds R/A to (R+M)/A. No missing-at-random assumption is imposed. These are finite-cohort identification bounds, not confidence intervals, and do not estimate a randomized treatment effect after response-based selection/crossover.

Show R divided by original randomized N only as the documented fraction who were acute responders and later observed positive, explicitly not the all-randomized follow-up response rate. For six-month CBIT, test how many missing positives are needed to reach the quoted available-case benchmark of 80%; it is an arithmetic sensitivity target, not a clinical threshold.

Check the acute randomized CGI response risk difference and its reciprocal only to diagnose the source's printed NNT inconsistency. Do not use it as medical advice or an alternative prespecified efficacy model. Show raw exact arithmetic alongside the reported source value.

Use Python standard library with rational arithmetic, no stochastic computation, and reproducible sorted JSON. Check counts, bound endpoints/widths, monotonic sensitivity scenarios, hand-derived expected fractions, invalid inputs and agreement between direct and enumerated bounds. Report passed tests and preserve input/code hashes. Do not calculate joint response, survival, off-treatment efficacy, missing mean tic/impairment values, or longitudinal covariance.
