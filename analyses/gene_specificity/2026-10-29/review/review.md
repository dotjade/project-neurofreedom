# Independent aggregate-source and methods review

29 October 2026. Scope: named membership classification, threshold implementation, source-to-input fidelity and inference boundaries. No clinical or genetic prediction is made.

## Source inspection

I independently read the [primary article](https://www.nature.com/articles/s41593-026-02419-5) and parsed the separate Source Data Figure 2 workbook using openpyxl, independently of the author's XML extractor. Only gene-aggregate sheets Fig2c and Fig2d were read. The mixed supplementary workbook was not accessed. The source SHA-256 is archived in `source-checks.json`; the original workbook remains outside the repository.

The independent script confirms the 12, 10 and 34 published set sizes, 36-gene union and disjoint 3/7/9/17 partition. It verifies every retained row's memberships, numerical q, damaging-event count and flags against the source. The two genes outside the combined high-confidence set pass the probable rule. There are 18,111 numeric-q rows, not 18,170 genes: trailing documentation must be excluded. Across those rows, 88 fall in the probable q band but only 20 also satisfy its count criterion. All published combined flags match the rules.

## Executed checks

- `python review/independent_source_checks.py /path/to/standalone-Fig2.xlsx`: 50 independent checks passed. Requires openpyxl. No random seed applies.
- Author unittest suite: six tests passed on independent rerun.
- The review uses independent set operations and numeric source parsing, not the author's output as an oracle.

## Interpretation and limitations

No blocking issue found. The report separates threshold membership from contribution, biological exclusivity and independently replicated effects. It does not treat unequal significance as a significant diagnostic contrast. Counterevidence, reused cohorts and unavailable separate-disorder q values remain explicit. It does not translate the gene map into an adult mechanism, individual risk or therapy.

The named mapping is a useful extension of yesterday's union arithmetic, not new gene discovery. Numerical agreement cannot remove ascertainment, comorbidity, model or ancestry limits. Independent access used the same publisher workbook, so this is an independent extraction and methods audit, not an independent biological replication.

The author added an exact SHA-256 guard to the optional extractor before fixed-sheet parsing, resolving the reproducibility recommendation. The evidence amendment and validation record are consistent with the verified analysis. Final file hashes accompany this review; later changes require renewed review.
