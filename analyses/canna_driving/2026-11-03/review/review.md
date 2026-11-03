# Independent review: bounded driving aggregate audit

2026-11-03. Reviewed plan, inputs, report, implementation, results and tests. Independently opened the three public primary sources below. No restricted driving full text, PDF retry, participant records or access bypass was used. Review writes are confined to this directory; main report was not edited.

## Finding

Arithmetic passes. The bounded interpretation is defensible: favorable computerized-endpoint evidence does not establish general driving safety or confirmatory noninferiority under the published conditional hierarchy. One source qualification should be added before finalization: the registry contains both a >25% primary-response analysis and a >30% analysis, whereas the published protocol specifies >30%. Both fail the superiority gate, so this qualification does not change the conclusion.

## Primary-source checks

- [PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/38265476/): identity, January 23 2024 electronic publication and October issue verified. Aggregate sample, arm sizes, baseline/final fit counts, printed percentages, transitions and reported difference/interval agree with inputs. The abstract does not supply sufficient model, imputation or analysis-set detail to resolve the arithmetic reconciliation. The authors' favorable conclusion is acknowledged in the report, without adopting it as individual advice.
- [Published protocol](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2020.575826/full): statistical-analysis section specifies >30% primary tic response, then conditional hierarchical driving noninferiority, center-stratified Mantel-Haenszel risk difference and -32 percentage-point margin. The computerized classification and five-test threshold agree with inputs. Published November 26 2020, after the registry's November 20 completion date. Publication timing alone cannot date each specification's adoption. No independent clinical justification for the margin was established by this review.
- [EU registry results](https://www.clinicaltrialsregister.eu/ctr-search/trial/2016-000564-42/results): >25% analysis, described as determined in blind review, has p=.0755; >30% analysis has p=.0633. Both exceed .05. Its >30% entry's descriptive field repeats an at-least-25% definition, so registry metadata are internally imperfect. Do not infer misconduct or reconstruct a definitive amendment history. First results date and identifiers match inputs. Although 61/64 and 26/33 appear under the non-serious heading, the registry explicitly says this section includes all serious and non-serious events. Existing all-event wording is therefore supported; adding serious counts again would be inappropriate. This resolves a preliminary reviewer concern based only on the section heading.

## Independent numerical verification

`verify.py` does not import the author's functions. It independently transcribes public aggregate numbers and uses exact rational arithmetic, then compares against results.json:

- Unique percentage-compatible denominators: 39 and 19. None lies at a rounding tie.
- Conditional transition totals: 30 and 12, each two above the reported final count.
- Crude contrast: 142/741 = 0.19163292847503374; difference from reported .17 is .021632928475033737.
- Lower confidence limit minus margin: 6/25 = .24; reported interval includes zero.
- Both public primary p values fail .05.
- Recorded plan hash matches the current file. This verifies file integrity, not independent timestamped preregistration.

All comparisons passed (`verification.json`). All ten existing implementation tests passed (`test-output.txt`). These checks are software/source checks, not a statistical refit or clinical validation.

## Interpretation and remaining limits

The report correctly labels inferred denominators as percentage-compatible, rather than observed completers, and treats transition disagreement conditionally. It does not fabricate missing outcomes. Deferring missingness bounds is justified until actual endpoint counts, transitions, imputation and population definitions are known. The CI's numerical clearance of the margin cannot restore the failed upstream gate; crossing zero is not evidence of equivalence or harm. No claim of individual driving clearance, pediatric applicability or real-world crash safety is supported or made.

Required clarification: add the two response thresholds and their p values to the report/inputs, preserving the failure-of-gate conclusion. Optional implementation improvement: `confirmatory_noninferiority_established_under_published_hierarchy` is hard-coded false. It is correct for this fixed audit but should be documented as an adjudicated finding, not presented as a general estimator that updates automatically with new inputs. `calculate` also assumes one compatible denominator per arm; acceptable here, but not general-purpose validation.

No further source retrieval is required for this bounded review. Full-methods uncertainty remains unresolved, with no permission to retry restricted paper acquisition.

## Final reconciliation

At 02:45 UTC the revised report was rechecked: it now states both primary thresholds, p values and the registry description inconsistency. The substantive reporting clarification is resolved. Inputs still contain only .0755; adding the >30% metadata would improve extraction completeness, but does not affect this audit's computation or conclusion. No blocking numerical or inferential defect remains in the revised bounded report.
