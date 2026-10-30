# Independent synthetic-methods review

30 October 2026. This is a review of an explicitly synthetic counterexample, not an analysis of the sensory-attenuation study's observations.

## Arithmetic and model

The construction is valid. For equal marginal standard errors 0.2, the variance of the contrast is 0.08(1-rho). The four chosen correlations yield positive eigenvalues for the covariance matrix. Holding marginal estimates and standard errors fixed therefore does not fix contrast uncertainty. Marginal significance decisions remain unchanged while the illustrative contrast decisions differ.

The independent script uses 60-digit mpmath normal distribution functions and a separately derived equal-variance formula, rather than importing the author's calculation. All 42 checks pass at absolute tolerance 1e-13. The nine author unit tests also pass on independent rerun. No random seed applies because nothing is sampled.

The known Gaussian sampling model makes the marginal and contrast normal formulas appropriate within this construction. Numerical evaluation still uses finite precision. The illustrative 95% intervals are pointwise, not a simultaneous family of guarantees. Crossing 0.05 is not a measure of biological or clinical importance.

## Inference boundaries

The correlation is between two estimated group differences, not raw forces or repeated trial measurements. The arbitrary estimates, errors and correlations are not fitted to the paper, do not recover its missing interaction, and cannot establish whether the authors performed that test. Other force levels, covariates and repeated-measure structure could alter the real estimand.

The example illustrates a familiar statistical principle, not a new biological finding or novel method. The next decision is to obtain the actual contrast and its uncertainty through lawful public methods or aggregate outputs, not substitute this calculation for them. No participant data, force targets, observation instructions or intervention is present.

No blocking mathematical or inference issue was found. Final hashes record the reviewed model snapshot; the source-access audit is separate.
