# Prespecified local methods exercise, not clinical data

30 October 2026. Written before this computation, not a registered study.

Question: do separate direct/indirect condition significance labels identify a group-by-condition contrast when the covariance of the two estimated group differences is missing?

Prediction: fixed condition differences and standard errors can yield the same marginal tests but different contrast tests under admissible covariance values. This tests a rule of inference, not whether the new sensory-attenuation paper performed the correct analysis.

Method: construct bivariate Gaussian estimates with known covariance. Fix arbitrary direct/indirect differences at 0.6/0.2 and both marginal standard errors at 0.2. Vary correlation among -0.5, 0, 0.5 and 0.9. Compute the difference of differences, its standard error, two-sided normal p value and 95% interval. Verify covariance positive definiteness. Treat 0.05 as an illustrative statistical threshold, not clinical importance. No sample, force unit, participant, paper parameter, intervention or random seed is used. No model is fitted.

Limitation: real force-matching tasks may require force-level, repeated-measure, missingness and adjusted-model structure absent from this construction. It neither supplies the paper's interaction nor proves no interaction exists. If the source supplies the fitted interaction and uncertainty, this demonstration is subordinate to that estimate.
