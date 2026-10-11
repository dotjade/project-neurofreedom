# Bounded analysis specification

Recorded 2026-10-11T04:06:30Z, after reading published aggregates and before executing any analysis code. This is a prospective execution specification for this computation, not a preregistered clinical study or a prediction made blind to the source data.

## Question
Do the published motor-score aggregates identify a decrease in the full 41-person follow-up-analysis cohort mean at three months when the unobserved scores can take any value on the verified 0–25 motor scale? Four weeks is a contextual comparison under the same method.

## Disconfirming result
The claim that the direction of full-cohort improvement is robust to unrestricted missing outcomes is weakened/disconfirmed if a scale-admissible missing-outcome scenario yields zero or positive mean change. This tests robustness/identification, not absence of benefit or treatment efficacy.

## Estimands and rules
Let N=41; n be the number with follow-up; m=N-n; Y_R their reported follow-up mean; B_R their own reported baseline mean; B the full-cohort baseline mean; Y_M the hypothetical missing follow-up mean. Negative change means lower severity. Full-cohort mean follow-up is (n*Y_R+m*Y_M)/N; change subtracts B. Returnee paired mean change is Y_R-B_R, never Y_R-B. Bounds use Y_M in [0,25]. Tipping point solves full-cohort change=0. No-change-missing assumes missing mean follow-up equals their implied baseline (N*B-n*B_R)/m. Additional descriptive scenarios vary missing mean change from its own baseline by 0,1,2,3 points, and compare same-as-observed change and same-as-observed outcome. Scenarios outside scale bounds are labeled infeasible, not clipped.

The source is internally inconsistent: full baseline 18.62 differs from the baseline reconstructed from n=36 mean18.83 and n=5 mean19.0. Main computations will explicitly be conditional on printed B=18.62. A separate hypothetical branch will use the pooled baseline from printed subgroup means; it is not a corrected datum. Printed decimal means are rounded aggregates. Report deterministic rounding envelopes using +/-0.005 for two-decimal means and +/-0.05 for the one-decimal early-dropout mean; these are not confidence intervals. Maintain source and analysis distinctions.

No invented covariance, confidence intervals, responder counts, participant-level reconstructions, clinical recommendations, or extrapolation to a severe-adult stratum. No pooled motor+phonic result. Report the missing prerequisites for exact empirical inference. No additional endpoint will be substituted if this task is infeasible.

## Reproducibility and stopping
Use Python standard library only. Preserve inputs, source locators, code, exact deterministic outputs, run metadata and tests. Finish after the bounded calculations, edge/invariance tests and independent arithmetic check pass, or report the precise missing prerequisite. No paid compute or GitHub writes.
