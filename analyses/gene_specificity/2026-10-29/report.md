# Which genes have chronic-tic, OCD or combined statistical support?

29 October 2026. Published-aggregate audit of [Wang et al.](https://www.nature.com/articles/s41593-026-02419-5), DOI 10.1038/s41593-026-02419-5, PMID 42680906. This advances the previous [genetics synthesis](../../causal_synthesis/2026-10-28/genetics/report.md) from union arithmetic to an explicit 36-gene membership map. It is not new gene discovery, a patient-risk model or a treatment ranking.

## Prediction and method

**Prediction tested:** treating every union gene as individually supported at the high-confidence threshold in both disorder analyses will fail against the published gene-specific memberships. A weaker shared-liability interpretation may remain compatible with the data.

The publisher provides a standalone **Source Data Fig. 2** workbook, labelled statistical source data and gene sets, separately from mixed Supplementary Tables 1–36. The latter were not retrieved. We read the gene-only Fig2d membership columns and Fig2c combined-analysis q values, aggregate counts and category flags. Only the 36 union genes and relevant fields are retained in `inputs.json`. The original workbook is not stored in this repository. The exact source URL and SHA-256 are in `source-checks.json`.

`analyze.py` partitions named genes into four mutually exclusive membership categories and checks every retained combined classification using decimal arithmetic. High confidence requires q < 0.1. Probable requires 0.1 ≤ q < 0.3 **and** at least two de novo damaging events. The count restriction applies to probable, not high confidence. These are the paper's designations, not recalculated q values or our causal confidence scale. `gene-map.csv` preserves the source precision and flags. Six unit tests cover boundaries, the count rule and membership checks; per-row assertions check classifications against source flags.

Run:

```sh
python analyses/gene_specificity/2026-10-29/analyze.py
python -m unittest discover -s analyses/gene_specificity/2026-10-29 -p 'test_*.py'
```

Optional source re-extraction: run `extract_inputs.py /path/to/standalone-Fig2.xlsx`. Do not substitute the mixed supplementary workbook. No random seed applies. No people, variants or pedigrees were reconstructed. Figure 2 has trailing documentation rows, so not every nonempty first-column row is a gene; this extraction selects the exact Fig2d union by name rather than counting those rows.

## Actual result: named support categories

| Published high-confidence membership | Count | Genes |
|---|---:|---|
| Both separate disorder analyses | 3 | DNAH9, QRICH1, SETD1A |
| CTD analysis, not OCD analysis | 7 | ARHGAP5, CELSR3, DST, NIPBL, PKD1, ULK1, WWC1 |
| OCD analysis, not CTD analysis | 9 | ACACB, ADIPOR2, BRWD1, CCDC168, CHD8, JAK2, SCUBE1, TEP1, ZMYM2 |
| Neither separate analysis, but combined analysis | 17 | ABCD2, AKAP1, ANK3, AP1G1, BCAN, CACNA1A, CARMIL2, CEP95, COL13A1, DNAH10, ELF1, LPIN1, MSANTD4, PRRC2A, RBSN, SYNE1, TTC21B |

All genes in the first and third rows meet the combined high-confidence threshold. In the second row, CELSR3 and WWC1 instead meet the combined **probable** rule: q = 0.12751907856514899 and 0.116143064160853, respectively, each with aggregate de novo damaging count 3. All other second-row genes remain combined high confidence. All 36 retained combined labels agree with source flags.

The 17 combined-only genes are not 34 minus all 19 distinct disorder-high-confidence genes: two of those 19 are outside the combined set. There are 17 disorder-high-confidence genes inside the combined set, leaving 17 combined-only genes. This is an explicit set-membership result, not another sum of headline union counts.

**Prediction result:** the strong universal separate-disorder-support interpretation fails. Only DNAH9, QRICH1 and SETD1A meet the threshold in both separate analyses. This does not establish that the other genes lack effects in one disorder, nor that these three are uniquely shared causal genes.

## Reconcile contribution, thresholds and counterevidence

The prior synthesis noted that many genes receive some evidence from both diagnoses. That is a different question from crossing a disorder-specific multiple-testing threshold. CACNA1A illustrates the distinction: the main text places its observed contributions in OCD-only or unknown-tic cases, while the standalone membership table places it in the combined-only high-confidence category. Neither designation licenses a CTD-specific mechanism claim.

Conversely, CELSR3's CTD-only rare-variant contribution in this study does not establish biological exclusivity: the authors discuss OCD common-variant support. Adding a cohort changes ascertainment, model evidence and multiple-testing results, not just sample size. CELSR3 and WWC1 retain high-confidence status in the main text's combined trio-only analysis, but exact trio-only q values were not available in the selected standalone sheets.

Directional counterevidence is retained: ABCD2, DNAH9, DNAH10 and TEP1 have higher rare gene-disrupting event rates in singleton controls than cases. DNAH9 nevertheless passes both separate high-confidence lists; that combination is possible because evidence classes contribute differently. A passed omnibus threshold does not make each component supportive. The article's display decomposition floors some below-one Bayes factors and uses transformed contributions. We do not reinterpret that display as unrestricted inferential Bayes factors or use it to calculate evidence shares.

SLITRK5 is not retained as high confidence or probable here. The authors explain that previously supporting variant classes were excluded from current gene discovery after negative burden tests. This is not a clean independent negative replication using identical measurements. Likewise, retained prior genes are not independent replications: the source explicitly reuses earlier samples. Newly sequenced material is not automatically a held-out replication cohort.

## Uncertainty and limits

- High-confidence membership is analysis-specific. A difference between significant and nonsignificant results is not a significant CTD-versus-OCD effect difference. We did not run a diagnostic interaction or heterogeneity test.
- FDR < 0.1 is not an individual gene's 90% probability of causing a disorder. The selected q values do not provide effect-size confidence intervals or penetrance.
- Missing separate-disorder and trio-only q values prevent margin-to-threshold comparisons across those analyses. The complete gene-only Table 16/19 information would need a safely separated public artifact before extending that analysis. No mixed participant or variant supplement is needed or authorized.
- Disorder cohorts overlap through comorbidity; singleton cases are OCD-ascertained, and their analysis is European-ancestry restricted. Unknown comorbidity cannot be recoded absent. These memberships are not independent experimental populations.
- Genetic association does not identify an acute tic trigger, adult reversible target or clinical benefit. Severe persistent adults, broader function, treatment response and communication/ASD groups are not validated by this gene map.
- The previous synthesis's network counterevidence remains: PCNet convergence did not reproduce in BioGRID. The present membership audit neither resolves nor erases that result.

## Decision and next bounded question

Close this fixed membership audit. Do not label the 36-gene union a set of Tourette-specific treatment targets. Preserve the gene-level map for future safely separated aggregate replication evidence rather than repeatedly redoing union arithmetic.

Next, move to the newly encountered adult sensorimotor primary study identified in today's scan, [Reduced Sensory Attenuation Scales with Tic Severity in Tourette Syndrome](https://pubmed.ncbi.nlm.nih.gov/42947547/), PMID 42947547, DOI 10.1002/mds.70590: inspect its formal group-by-condition contrast, precision and temporal ordering before interpreting concurrent sensorimotor measures as a prospective tic trigger or compensatory mechanism. This is a distinct hypothesis-discrimination question, not a request for patient data or intervention. The integrating scan currently has abstract-level access; formal contrast estimates and model details are prerequisites, not presumed available.
