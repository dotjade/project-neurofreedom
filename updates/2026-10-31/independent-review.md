# Independent review: 31 October 2026

## Outcome

The force-matching report and synthetic calculation passed this bounded independent audit. The historical study does not contain a Tourette cohort. Comparison strength, gain-baseline transport, conditional identification and null/equivalence limits are retained. The new histamine lead remains abstract-only, older than the scan window and diagnostically mixed. PRISM-TS is a planned adolescent protocol without results; 95 top-line enrollment is not 95 randomized adolescents.

## Actual checks

- Independently retrieved the primary Europe PMC author manuscript, bibliographic metadata for PMIDs 40531356 and 42956657, and the official NCT07905898 API record. No participant files or unlicensed full text were stored.
- Re-executed check_identification.py: all 30 implementation assertions passed and synthetic-results.json reproduced byte-for-byte.
- Independently computed 59 arithmetic/label assertions without importing the implementation. Exact rational calculations reproduced all six memory rows. For each of three distributions, normal raw moments were derived from the binomial expansion and Gaussian even moments, then multiplied across independent factors. Mean, variance and third central moment reproduced the saved product and calibration numbers. Additive moments, synthetic labelling and nonrandom execution were also checked.
- Read the complete model report and source-level registry extraction. Quantities and source limits are listed in [the machine-readable receipt](independent-review.json). No source discrepancy requiring correction was found.

## Reproduction of the independent arithmetic

Run from repository root: `python updates/2026-10-31/independent_math_check.py`. The standalone standard-library checker reads the saved synthetic output, independently recomputes all 59 assertions and verifies their identities against the receipt. It does not import the implementation, access the network, sample random values or write files.

For a normal variable with mean m and variance v, compute raw moment n as the sum over even j from 0 to n of C(n,j) m^(n-j) v^(j/2) (j-1)!!, with (-1)!! = 1. For independent factors X and K, the product raw moment is E[X^n]E[K^n]. Variance is raw2 minus raw1 squared; the third central moment is raw3 minus 3 raw1 raw2 plus 2 raw1 cubed. Divide the third central moment by variance^(3/2) for skewness. Use exact fractions 9/100 for indirect variance, 1/25 for factor variance, 3/2 for factor mean and indirect means 1, 2 and 3. For memory rows use I=1/2+(2/3)T and D=(3/2)I at T=1, 3/2, 2, 5/2, 3, 7/2.

## Limits

Identical-factor relabeling is a structural identification counterexample, not a tested biological alternative. No empirical model, participant-level result, posterior chain or treatment effect was re-estimated. The clinical pilot's full methods were not available in this review. The final scan, safety, daily report, STATUS, evidence and feed were subsequently reviewed. Reexecuted scan validation passed 42 checks; safety validation passed 28 checks; deployed feed schema passed. Approved activity and feedback objects remain exactly unchanged, and two primary records were appended while preserving prior records. No new-window evidence, treatment, severity-subgroup or mechanism overclaim was identified. Source acquisition was not rerun exhaustively, so this does not certify complete database coverage. EMA safety verification was separately performed by the integrating reviewer.
