# H18 synthetic measurement-identifiability test

Research date: 8 November 2026. Written before the numerical experiment; this is a local methods plan, not a registered human study. No clinical data, outcome reconstruction, treatment, contact or personal classification is involved.

## Question and predictions

Can lower urge generation and higher action control be distinguished from sparse global urge/tic changes? When do repeated observations and a new context help, and when do they leave the distinction unidentified?

Predictions made before execution:

1. Tic change alone identifies only a sum of two latent contributions. A calibrated, invariant urge measure with nonzero sensitivity supplies a second identifying equation. Sparse measurement is not by itself proof of structural nonidentifiability.
2. Repeated measurements reduce random measurement error, but cannot fix an unknown systematic reporting shift. A weak known urge loading makes parameter estimation imprecise even when the algebraic model is identifiable.
3. Treating repeated rows as independent will make confidence intervals too narrow. Participant-mean analysis will retain nominal coverage under the specified Gaussian model.
4. An unmodeled reporting shift that cancels genuine urge change can be mistaken for action control. More precise measurement can make that wrong interpretation more confident.
5. Training-context tic improvement will not guarantee transfer. A contrast in transfer identifies the two contributions only if unequal mechanism-specific transfer coefficients are known; equal or unknown coefficients do not supply the missing distinction.

## Fixed model and arbitrary inputs

All values are dimensionless inventions for a methods exercise. They are not PUTS/YGTSS points, clinically calibrated effects, trial sample-size advice or empirical reliability estimates.

Let g denote a population-average contribution from reduced urge generation and c a contribution from increased action control. The expected paired changes are z = g + c (positive tic-expression reduction) and u = lambda*g + b (positive urge-score reduction). b is a systematic reporting/measurement change. No claim is made that this is the true biological model. The main fitted model assumes known lambda and b=0.

For synthetic independent unit i and repeated paired contrast r, X_ir = (z,u) + H_i + E_ir. H_i is a mean-zero Gaussian unit-specific effect with marginal SDs (0.45,0.45) and correlation 0.30. E_ir is an independent mean-zero Gaussian observation error with marginal SDs (0.80,0.80) and correlation 0.20. Unit effects persist across that unit's repeated rows. There are N=60 independent units per dataset, no missing rows, no temporal trend and R=1 or 8 paired contrasts per unit. Pre/post raw observations are not simulated; their contrast is the observation. This is not a randomized treatment comparison or a causal mediation model.

Use NumPy PCG64 via SeedSequence: master seed 20261108. Fixed scenario order creates independent child streams. Run 4,000 Monte Carlo datasets per scenario. Primary scenarios cross lambda in (0.25,1.0), R in (1,8), and (g,c) in ((0.5,0),(0,0.5),(0.25,0.25)), with b=0. Additional sensitivity scenarios use the pure generation truth with R=8, both lambda values, and b=-lambda*0.5 while fitting b=0.

## Analyses fixed before fitting

1. Derive and numerically verify measurement Jacobian ranks, null directions, and an exact observational-equivalence construction. Include unknown b, zero loading, unknown loading and context-transfer conditions. Do not use a simulation's ability to select an assumed model as proof that it is identified in reality.
2. Estimate g as mean(u)/lambda and c as mean(z)-g. Analyze independent unit means, not repeated rows as independent units. Use the empirical covariance of 60 unit means divided by 60, transformed by the fixed linear estimator, and two-sided Student t 95% intervals with 59 degrees of freedom. Save bias, RMSE, interval width, coverage and coverage Monte Carlo uncertainty. Compare g intervals with an explicitly incorrect row-independent variance estimate.
3. A descriptive label is generation-dominant if the 95% interval for g-c is wholly positive, control-dominant if wholly negative, and unresolved otherwise. Report the three label frequencies for every truth, without individual-level claims or a clinical decision threshold. With equal contributions, any dominant label is a false positive under this model. These labels are an illustrative population-parameter recovery diagnostic, not treatment recommendations.
4. For context transfer, independently generate training and held-out samples of 60 units, eight repeats each. Do not use held-out context outcomes in fitting the training mean. Consider fixed transfer pairs (t_g,t_c)=(1,1),(1,0.25),(0.25,1), for both pure truths. Held-out context means are z_B=t_g*g+t_c*c; use the same random-effect and measurement covariance. The full-transfer prediction is the estimated training mean z_A. Report test-minus-training mean, bias relative to the true transfer gap, and the frequency that a 95% interval for that gap contains zero. The interval uses an independent-sample Welch standard error/degrees of freedom. It is an interval for a population mean gap, not an individual prediction interval. Compute the known-coefficient transfer matrix rank separately, and show why unknown coefficients remain nonidentifying.

## Verification and decision

Save configuration, plan hash, environment, code, aggregate outputs, a readable report and reproducibility tests. Preserve all scenarios, including failures and misspecification. Re-run outputs with the same seed, verify exact output bytes, independently verify linear algebra and expected sampling variances, and check empirical coverage against Monte Carlo uncertainty without treating every arbitrary tolerance as a scientific validation.

Stop this toy-model exercise after the fixed scenarios. Keep H18 proposed. If the anticipated structural ambiguity is confirmed, the next useful step is to specify which measurement-invariance/anchor assumptions and explicit transfer estimands existing measures could support; do not add a more elaborate predictor to the same unidentified observations. Clinical personalization would still require governed independent validation and a randomized strategy comparison with function, pain, effort, adverse effects and durable transfer. Persistent severe adult burden is not represented by these artificial units and cannot be inferred from them.
