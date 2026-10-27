# Independent EMTICS psychometric audit review

Reviewed 27 October 2026. AI-assisted source/methods review, not independent clinical peer review.

## Source reconciliation

The [primary publisher article](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2021.626459/full) supports the reported pediatric baseline sample, original instrument, coefficient values, fit indices and convergence/discrimination estimates. The earlier 2018 pooled alpha and this paper's omega are not interchangeable longitudinal observations. The within-sample coefficient difference also cannot quantify measurement bias without a compatible identified estimand.

Marginal fit, residual correlations, the unsuccessful alternative-factor exploration and missing interrater evidence must remain alongside favorable associations. The paper reports training, not measured interrater reliability. Neither clinical similarity nor low correlations with other symptom measures establish invariance across age, language or ASD groups. Impairment and symptom severity should not be equated with all lived burden.

## Independent computation

`python independent_checks.py` passes 28 independent arithmetic, cutoff and authored-output checks. The alternative thresholds come from the paper's Methods. Requiring all three is the project's declared sensitivity convention, not a universal clinical rule. Classification at CFI .90 is sensitive to unreported rounding precision; the TLI shortfall remains under the stated rounding scenario. These calculations neither refit the model nor validate a clinical cutoff. No seed applies.

## Clarifications preserved

Counts without recent phonic tics use all 706 participants, not the TS-only denominator. The age-subgroup wording differs between Methods and Results. The final audit must not silently repair either ambiguity. An allowed diagnosis in the parent protocol is not evidence of actual representation in this analysis.

## Supplement and unresolved implementation

The official [EuropePMC supplement route](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7949908/supplementaryFiles) yielded a one-page model-diagnostic table, inspected in text and rendered form. It contains 13 misspecification and two inconclusive decisions; no-misspecification rows are omitted. This is not a complete covariance matrix. Neither the table nor the inspected main methods identifies the exact omega variant/formula/code. Reported coefficients are retained without declaring either the true reliability. No source PDF or image is retained in the repository.

## Final disposition

Final report, evidence record, source checks, inputs, code and outputs reviewed. No blocking issue remains. The author incorporated the supplement check, distinguishes unknown omega implementation from the published coefficients, and preserves the rounding caveat. Twenty-eight independent checks and ten implementation tests pass. Hashes identify the reviewed versions.
