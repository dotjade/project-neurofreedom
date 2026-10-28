# Independent parent-versus-clinician audit review

Reviewed 28 October 2026. AI-assisted source and arithmetic review, not clinical peer review.

## Primary-source checks

The [primary article](https://doi.org/10.1136/bmjopen-2019-034634) was inspected through official Europe PMC XML, excluding the feedback subsection. Figures 1 and 2 were independently retrieved and visually inspected. The former is a partial translated form illustration, not complete version verification; the latter provides the fellow-evaluation denominator. See [provenance](source-provenance.json). No participant narrative, individual plot point, source paper or image is retained.

Assessment counts must remain distinct from people. Masking the other rater's score does not prove informational independence. The reported timing descriptions conflict; they cannot establish simultaneous observations. AUC concerns category discrimination, not interchangeable continuous scores. No numerical ICC was identified in inspected methods/results. Nonsignificance after repeated assessments is not equivalence or a randomized learning effect.

## Independent arithmetic

`python independent_checks.py` passes 29 checks, including the author's output. The reconstructed aggregate categories sum correctly. The 196 discordances are assessments, not 196 patients. No independent-observation confidence intervals, clustering corrections, new sensitivity tests or individual score reconstruction were attempted.

Under the explicitly conditional absolute-difference interpretation, the reverse and ordinary triangle inequalities support bounds of .01 to 4.81 for the mean absolute total difference. The reported 4.15 is compatible. Under a signed same-pair interpretation, additivity would instead apply. Thus the audit appropriately preserves an estimand ambiguity rather than alleging a numerical error.

## Limits and disposition

The score's equality-at-20 rule and precise classification variant remain unresolved. A translated pediatric clinical workflow cannot establish adult, severe-adult or ASD/communication-group equivalence. Full-score limits of agreement and outcome-specific uncertainty remain prerequisites for stronger interchangeability claims, not invitations to collect participant data.

Final report, evidence record and analysis reviewed. No substantive blocking issue remains. All 29 independent checks and 11 implementation tests pass. The exact reviewed file hashes accompany this review. Minor evidence-record spacing corrections were applied before the final hash freeze.
