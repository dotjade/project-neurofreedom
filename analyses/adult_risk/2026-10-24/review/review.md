# Independent review of the adult denominator and timing audit

24 October 2026

**Decision: no blocking correction.** The bounded audit is supported by the inspected primary evidence. Independent checks passed **69 of 69**. This is a documentation and arithmetic review, not clinical validation or prospective prediction.

## Evidence and reproducibility

I reviewed the prediction, report, inputs, results, analysis code, author checks, source provenance and temporal audit without changing their files. I independently opened the [official publisher article](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2026.1948693/full) and retrieved [official PMC XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=13680449&retmode=xml) into memory only. The DOI, PMID and PMCID match the requested study. The source response hash exactly matches the audit's recorded hash. The electronic publication date is 6 October 2026.

`independent_checks.py` implements the percentage check independently with exact rational arithmetic: the unrounded percentage must lie in the half-open interval from printed percent minus 0.05 to printed percent plus 0.05. It does not import or execute the author's analysis code. `checks.json` contains each result, and `source-provenance.json` records independent retrieval.

## Findings

- All eight Table 1 count/percentage pairs match the primary source. Compatible denominators are male 257, White 257, non-Hispanic 256, current medication 258, family history 232, OCD 208, ADHD 252 and life event 258. Their conditional complements relative to 258 also match. No participant identities, joint missingness patterns or regression sample sizes follow from this calculation.
- The flow counts and every reported rate reproduce correctly. Completeness and exclusions are distinct from clinical worsening. The retained-respondent denominator is not a population persistence denominator.
- Current symptoms and the 50 reused current/adult-worst scores are correctly distinguished from independent longitudinal observations. The apparent equality between 50 reused scores and the conditional OCD complement does not identify the same people.
- Methods establish recalled childhood/adult periods, lifetime OCD/ADHD assignments, medication current at survey, and an event contemporaneous with the recalled adult-worst period. The audit appropriately declines to treat lifetime OCD or current medication as verified antecedent exposures. The discussion's childhood-OCD wording does not change the methods' lifetime definition.
- Table 4 confirms the two different predictor sets and the selected coefficients and p values. The ADHD and life-event total-tic terms are nonsignificant; Table 5 positive-valence terms are nonsignificant for both outcomes. The impairment OCD p value is indeed printed and bolded as 0.050 while the footnote defines significance using a strict less-than threshold. Preserving rather than resolving that boundary is correct.
- No explicit final-model sample sizes or model-specific complete-case/imputation rule were located in the inspected main methods and tables. Leaving both model counts null is warranted. Reported R-squared values are not demonstrated held-out predictive performance. The retrospective-versus-prospective conclusion is appropriately qualified.

## Precision edit adopted

The data statement describes author-mediated availability subject to Mass General Brigham Institutional Review Board policies. The parent adopted this precision edit in the report; I verified the revised wording. It correctly avoids calling the data unrestricted public participant data or treating the statement as authorization to obtain them.

## Limits and stopping condition

PMC HTML through the web viewer returned a cache miss; the publisher HTML and official EFetch XML succeeded normally. No access restriction was bypassed. The XML contains no supplementary-material element, which does not prove that no relevant documentation exists elsewhere. This review does not authenticate an external preregistration or the prediction's historical creation order. No full paper, personal-event narratives, figures or participant data were saved; no author was contacted and no clinical model was fitted. The next substantive step for this fixed audit requires new public documentation, not reverse engineering of model n.
