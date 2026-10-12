# Independent review of the 12 October evidence audit

12 October 2026, completed approximately 02:57 UTC

## Verdict

No material arithmetic or interpretation error identified in the reviewed adult-endpoint report, structured extraction, calculation script or CBIT–TMS extraction. Their main limits are justified: the adult reports do not identify severe persistence or validate severity as a burden surrogate; the linked preprint and trial record do not establish added clinical efficacy for persistent severe adult illness. The small safety-label clarification below was subsequently applied and verified.

## Arithmetic and adult report checks

- Read the complete adult report, extraction and prospective question; reran `aggregate_checks.py`: **47 checks passed**, reproducing its JSON output. The script is aggregate arithmetic, not a statistical reanalysis. Its normal run rewrites only its generated `aggregate_checks.json`; no substantive worker artifact was edited.
- Independently derived the sharp intersection bounds: max(0, 63 + 55 − 95) = **23**, and min(63, 55) = **55**. Both endpoints are feasible. At 23, the both/six-only/twelve-only/neither cells are 23/40/32/0; at 55 they are 55/8/0/32. Neither case establishes endpoint completeness or severity.
- **63/95 = 66.3158%** and **55/95 = 57.8947%** are fractions of enrollees with assessments completed at analysis. Eligible/due denominators are absent, so retention and permanent loss cannot be inferred. No severe prevalence, covariance, transition count or treatment effect was manufactured.
- Publisher methods/results verify the 95-person Calgary denominator, 63/55 completions, 0/6/12-month schedule, named severity/impairment/QoL collection and absence of systematic treatment adverse-effect collection. Table 1 supplies nonrandomized treatment-group contrasts, not severity–burden correlations. [Calgary primary report](https://movementdisorders.onlinelibrary.wiley.com/doi/10.1002/mdc3.14296)
- Publisher PDF text verifies the expanded sample of 227, first-assessment design, revised YGTSS past-week assessment, psychiatric denominators 218/78/140 and the printed antipsychotic inconsistency 95 versus 33 + 66 = 99. The nine-person denominator difference does not explain its cause. Nationality is not a longitudinal site flow. [Expanded primary report, Methods and Tables 1–2](https://onlinelibrary.wiley.com/doi/pdf/10.1111/ene.70252)
- Primary benchmark Table 3 really prints total-score ranges 28–43 and 43–46, with only fair classification agreement. The caution against adopting that boundary wholesale is appropriate. Single-modality disorders have a structural total-score ceiling of 25 under the stated scoring. [Benchmark study](https://pmc.ncbi.nlm.nih.gov/articles/PMC7867408/)
- Confirmed the original GTS-QOL's 27 items/four domains from its development abstract and four-week recall/0–4 scoring from indexed primary French-adaptation text. The French validation identifies six factors, reinforcing the report's warning to verify actual language/version rather than assume cross-site domain equivalence. [Original validation](https://pubmed.ncbi.nlm.nih.gov/18955683/), [French validation](https://pmc.ncbi.nlm.nih.gov/articles/PMC7755204/)

## Linked TMS trial checks

- Independently inspected the saved official aggregate registry JSON and ran **25 additional assertions** on outcome values, SDs, denominators, absent analysis rows, participant flow and adverse-event totals. Started 17/16/17, completed 17/15/16; neural-outcome denominators 15/13/17; adverse-event risk denominators 17/15/16. All match the extraction. [NCT04578912](https://clinicaltrials.gov/study/NCT04578912)
- The 46/22/18 outcome values are event counts. Summing the non-serious event categories independently produces the same counts. This agreement does not identify affected sessions, treatment-related affected participants or the basis of abstract session percentages. The ≥80%-session completion outcome is 48/50 = 96%; it is not 96% completion of every scheduled assessment.
- Verified the single unlabeled tic-suppression category and missing comparison analyses, despite five described intervals. Verified neural units labeled eta squared while descriptions promise Cohen's d. With these ambiguities, refusing to reconstruct a clinical contrast is justified.
- **Suggested precision edit:** the registry explicitly labels the non-serious event rows `NON_SYSTEMATIC_ASSESSMENT`; that field is not supplied for the zero-serious-event totals. Say “zero serious events were recorded over four months; non-serious events were labeled non-systematically assessed,” rather than attaching that assessment label directly to the serious-event result.
- **Resolved:** verified that the parent revised the extraction's serious-AE row to state: “As recorded over four months; small sample limits inference. Non-serious AE rows separately label assessment non-systematic.” This resolves the suggestion without changing any counts.
- Independently opened the 2023 protocol. Its phase-1 primary measure is task activation; connectivity is the secondary neural measure. Safety/feasibility are progression gates and clinical comparisons are exploratory. Planned phase-1 enrollment is 60. The extraction accurately distinguishes this hierarchy from the current registry and abstract; amendment history is needed before asserting outcome switching. [Published protocol, Objectives, Outcomes and Sample size](https://link.springer.com/article/10.1186/s13063-023-07455-1)
- Saved official medRxiv DOI metadata and PubMed XML agree on DOI **10.64898/2026.09.29.26364036**, preprint identity, 1 October posting, NCT04578912, age range, 50-person design and abstract session percentages. The abstract contains no clinical between-arm estimate with a confidence interval. Metadata reports version 1, CC BY and no published successor. This is a metadata/abstract check, not a full-preprint peer review. [Preprint DOI](https://doi.org/10.64898/2026.09.29.26364036), [PubMed record](https://pubmed.ncbi.nlm.nih.gov/42856611/)

## Scope and limitations

Read primary publisher HTML/PDF text through web tools; did not download or store papers, supplements or participant information. Direct new-preprint PubMed/API opens failed, so that portion was independently parsed from existing official metadata/abstract captures, with identity additionally confirmed in the publisher's indexed listing. No fresh registry API retrieval, historical-version audit, image-level PDF review, full-preprint review or comprehensive correction/retraction check was completed. The prospective-question file's asserted timing was read, not independently authenticated.

Reviewed adult report SHA-256: `ebf829fc61aaab3bbebb794d84f38a3967d98d6635f321957a0d533199c2be2b`.

Initially reviewed TMS extraction SHA-256: `fb002aad04009cdaa01a1d7d689abb32ad51b6aab3c647c7be91951593038aea`.

Corrected TMS extraction SHA-256, verified approximately 02:59 UTC: `2bd9355e7919baa06b186fe5bffdae50c4842ab1c99292e3d2d23ffd8e95b856`.

Registry JSON SHA-256: `24b49a5a5bec8d4d1a6899b387aa2235941448d7a96a7aac9276c9eb5723eae7`.

## Reproducibility addendum

At approximately 03:00 UTC, saved and reran the [25-assertion registry audit](registry_checks.py), with [minimal aggregate inputs](registry_inputs.json) and [actual output](registry_checks_output.json). The rerun passed all 25 assertions. The [README](README.md) explains the check breakdown and input provenance; its projection script can reproduce these selected fields from the permitted registry capture or separately refresh official API data into memory. No full source registry was duplicated in the review bundle. The original run was inline; the saved code preserves the same 25 fact assertions and adds an outcome-order guard.

No external write, outreach, participant analysis or clinical action was performed.
