# Synthetic causal-control demonstration: stopping an event does not locate its unique origin

**SYNTHETIC MATHEMATICAL EXERCISE. No patients, fitted biology or clinical effect estimates.** This is not a Tourette mechanism discovery. It checks an inference rule used when interpreting mechanistic treatments.

## Prediction, method and actual result

The [pre-computation plan](plan.md) predicted that three different stipulated input architectures could share event rates and responses to a downstream gate. [Code](analyze.py) enumerates eight binary input/gate states for each scenario. The [inputs](inputs.json) are arbitrary, fixed before execution; [results](results.json) contain all 30 scenario outputs plus five joint-input cases. No random numbers or seed are used.

| Artificial architecture | Baseline event probability, context A | Halve downstream gate | Selectively block X | Selectively block Z |
|---|---:|---:|---:|---:|
| One input X | .100000 | .050000 | 0 | .100000 |
| Parallel X OR Z | .100000 | .050000 | .052786 | .052786 |
| Coincident X AND Z | .100000 | .050000 | 0 | 0 |

Context B scales baseline to .16 and downstream-controlled probability to .08 in all three. Blocking both inputs gives zero in all three. These are constructed probabilities, not measured tic rates, treatment effects or forecasts.

**Two separate inference failures are demonstrated:**

1. Equal baseline/contextual rates and equal downstream symptom reduction do not identify the upstream architecture.
2. Even complete event abolition under an ideally selective X block does not distinguish X as the sole trigger from X as one necessary member of a two-input mechanism. A common necessary bottleneck can be clinically useful without being the unique original cause.

This does **not** establish full observational equivalence. X/Z marginal probabilities deliberately differ across architectures; sufficiently valid input measurements could distinguish them without intervention. Only the listed event probabilities and downstream-control contrasts match. All inputs and gates are independent in the first construction; real feedback and compensation are absent. A named X must refer to a common, independently measured operational target before the intervention comparison has scientific meaning.

## Selectivity and timing implications

In the separately defined ordinary-action channel, a shared gate passes an independent demand with probability .4. Halving that gate reduces ordinary-action probability from .20 to .10 in context A. Selective X/Z blocks leave it .20 in this construction. This is a reason to measure preserved function, not evidence that any actual treatment works through general motor suppression. A real intervention could selectively control tics, alter ordinary action differently, or have other harms.

A separate Fréchet check fixes both input marginals at .25. Their joint probability can range from 0 to .25; with gate .5, coincidence-driven event probability consequently ranges from 0 to .125 despite identical marginal input activity. The five evaluated joint values satisfy nonnegative four-cell probabilities and identical marginals. This establishes a mathematical limitation of marginal measurements, not that human tics are produced by synchrony. It is a separate construction, not a continuation of the .20-drive calibration above.

## Uncertainty, reproducibility and decision

Ten implementation tests pass. Independent closed-form checks are stored under [review](review/). These validate code/logic only. The deliberate calibration, Boolean rules, arbitrary probabilities, instantaneous ideal blocks and assumed normal-action channel prevent biological generalization. There are no clinical confidence intervals, power calculations, newly identified biomarkers or patient predictions.

The practical research decision is to distinguish **root liability**, **event-generating input**, **permissive state**, and **controllable output**. A useful mechanistic comparison needs independent target engagement, timing, specificity and functional outcomes. Complete symptom control would be valuable even before unique origins are known, but it would not by itself prove causal repair or durability after control ends. No real intervention or new data collection was performed or authorized by this exercise.

Reproduce with `python analyze.py`, `python test_analysis.py`, and the independent review script from the documented directories.
