# SYNTHETIC methods result: separate condition tests do not identify their contrast

30 October 2026. No paper estimates, participants, biological observations or treatment effects are represented below.

## Prediction and method

We predicted that identical direct- and indirect-condition marginal estimates can coexist with different decisions for their formal contrast when the covariance is unspecified. The [plan](plan.md) was written before execution but is not a registered study. [Inputs](inputs.json), [code](analyze.py), [results](results.json) and [tests](test_analysis.py) are included.

In an artificial bivariate Gaussian estimator model, set the two group differences to 0.6 and 0.2 arbitrary units, each with standard error 0.2. These numbers are analyst-chosen, not extracted from the force-matching paper. Correlation refers to the **two estimated group differences**, not raw trials or an assumed clinical within-person correlation. Four admissible covariance matrices are evaluated; positive determinants ensure positive definiteness. Such matrices can also be formed by adding two independent group-mean covariance matrices, each half the stipulated total.

The contrast is 0.6 minus 0.2 = 0.4. Its variance is SE(direct)^2 + SE(indirect)^2 minus twice their covariance. We use known-covariance normal tests and 95% intervals, not sample-estimated t tests or a fitted mixed model. The 0.05 decision threshold is illustrative statistical convention, not a clinically meaningful boundary. Analytic formulas are evaluated numerically with floating-point arithmetic; no random seed is required. Intervals are pointwise, not simultaneous.

## Actual synthetic result

The marginal normal z statistics remain 3 and 1, with two-sided p values approximately .00270 and .31731 in every scenario. Yet the contrast uncertainty and test change:

| Correlation of difference estimates | Contrast SE | Contrast z | Two-sided p | Below .05? |
|---|---:|---:|---:|---|
| -.5 | .34641 | 1.15470 | .24821 | No |
| 0 | .28284 | 1.41421 | .15730 | No |
| .5 | .20000 | 2.00000 | .04550 | Yes |
| .9 | .08944 | 4.47214 | .00000774 | Yes |

The identical marginal outcomes therefore do not identify the formal contrast's precision or statistical decision. The covariance is a missing input, not a nuisance that can safely be set to zero. This does not establish whether an interaction exists in the real study, nor imply that its authors failed to test one. It shows why the accessible abstract's separate condition statements cannot substitute for the actual contrast and uncertainty.

## Limits and next decision

Nine implementation tests pass, including covariance validity, fixed marginals, differing decisions, interval consistency and a zero-contrast control. Independent checks are recorded under [review](review/). These checks validate this mathematical illustration only.

A real force-matching design may include several force levels, repeated trials, unequal variances, missing measurements, covariate adjustment and model-specific degrees of freedom. None is represented here. No arbitrary values were tuned to reproduce the paper, and the Gaussian model is not a biological model. Nonsignificance is not equivalence; significance is not causation or clinical usefulness.

For the actual study, a lawful report of the fitted group-by-condition contrast with standard error or interval, model specification and effective sample counts would suffice for a primary audit. Alternatively, suitable aggregate condition estimates and their covariance could support a clearly specified reconstruction, if the model warrants it. Participant-level data, contact or new experimentation are neither required nor authorized here. Until those inputs are accessible, retain the paper's adult association and indirect-condition null without inventing its interaction.
