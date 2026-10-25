# Prespecified weekly report-to-cohort accounting question

Recorded 2026-10-25 before constructing/executing the weekly cohort graph.

Question: Can adding the five selected DBS report-role counts from this week's linked sources be interpreted as independent people or independent clinical replications?

Prediction: explicit nesting and mixed-trial membership will invalidate addition; graph-based bounds will expose the difference without identifying people. A source establishing independent recruitment for each report, or an unlinked third cohort in the mixed report, would disconfirm the two-family coding. Do not force a bound if the mixed report's membership/count is not verified.

Fixed reports: Cagle2022 (four embedded-device participants), Okun2024 (ten enrolled), Lowor2025 (five physiology contributors), NCT05371041 results (eight enrolled), and Lowor2026 preprint (sixteen people from the two named trials). Counts have different roles and are not clinical outcome denominators. The naive sum is a deliberately invalid comparator, not an estimator.

Method: verify the reported trial links; enumerate integer allocations of the mixed report between two enrollment universes of 10 and 8 under a separately labelled disjoint-cohort assumption. Without disjointness, only set-cardinality bounds conditional on the sixteen distinct people being a subset of the union are permissible. No identities, individual rows, outcomes, pooled efficacy or safety rates will be accessed/reconstructed. Missing participant membership remains missing.

Primary result: report count, trial-family count, naive total, union bounds, and conditional mixed-report allocations. Sensitivity: omit preprint; relax disjointness. This is deterministic set arithmetic with no RNG/seed, not a patient simulation. Numerical bounds are conditional on sourced membership; they are not confidence intervals or evidence of treatment benefit. No publication-count confidence score.
