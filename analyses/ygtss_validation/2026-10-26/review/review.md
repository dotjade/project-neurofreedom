# Independent review: YGTSS scope audit

Reviewed 26 October 2026. AI-assisted methods/source review, not clinical peer review.

## Independent checks

[PubMed](https://pubmed.ncbi.nlm.nih.gov/29653992/) confirms the identifiers and April 13 electronic versus May 8, 2018 issue dates. The [institutional primary paper](https://escholarship.org/uc/item/4bh642p5) supports the age, diagnosis, site and diagnostic-procedure partitions. Internal-consistency coefficients describe pooled original-scale performance, not newly measured interrater/test-retest agreement. The main report does not identify ASD/communication subgroup validation. Proposed revised anchors are not an empirical comparison of original and revised instruments. Absence of an ASD count must not be encoded as zero.

The interpretation is therefore appropriately narrower than a claim of equivalent measurement across groups. This is not evidence that ASD ratings are biased. Statistical similarity of selected summaries is not formal equivalence or measurement invariance, and adult inclusion alone cannot establish applicability to persistent severe adult burden.

## Numerical verification

`python independent_checks.py` executes 20 independent Decimal arithmetic and authored-output checks. All pass. Partition sums, proportions and rounded-mean differences agree. No clinical inference follows from these arithmetic checks. There is no simulation, random seed, participant reconstruction or new confidence interval.

## Access and correction limits

Extracted Table 3 signs conflict with direction labels for two items; Discussion also narrows the alpha range relative to Table 2. The former signs are not visually confirmed: screenshot retrieval failed and direct PDF download returned HTTP 429. These contested values are not inputs to the computation and cannot support correction of the paper. See [source provenance](source-provenance.json). No source full text, supplements or individual records are retained.

## Review disposition

Final report, inputs, computational output and tests reviewed. No blocking issue remains. The author removed a hardcoded qualitative validation judgment from computed results and labels the unconfirmed extracted-table discrepancy explicitly. The next question is bounded, with pediatric evidence not substituted for adult/ASD validation. Twenty independent checks and seven implementation tests passed at this review.
