# Sensory attenuation and repeated-input gating test different contrasts

30 October 2026. Primary-source construct and estimand audit, with a bounded access result. This is not a reanalysis of participant measurements or a clinical intervention.

## Prediction and actual result

**Prediction tested:** if the new force-matching result establishes a specifically impaired action-related attenuation process, a direct-versus-indirect *group contrast* should be estimable, rather than inferred from one significant and one nonsignificant comparison. If it also establishes a predictive marker, temporally later or held-out outcomes should be evaluated.

**Actual result:** neither assertion can be verified numerically from the accessible primary abstract. We identified an associated public OSF project, but its exposed files are datasets, not a safely separate manuscript or aggregate-results table. No dataset was accessed. This is a specific access prerequisite, not a negative interaction result or evidence that the authors did not conduct one.

A useful narrower finding is established by the construct comparison: the newer study's action-related force-matching result and the older pneumatic-gating null do not estimate the same phenomenon. They cannot be pooled as positive and negative estimates of one generic sensory-filter deficit. The latter nevertheless counters an indiscriminate claim that every tactile processing measure is impaired.

## Verified source observations

[Stanco et al., PMID 42947547](https://pubmed.ncbi.nlm.nih.gov/42947547/), [DOI 10.1002/mds.70590](https://doi.org/10.1002/mds.70590), electronically dated 28 October 2026, compares 30 adults with TS and 30 controls. The abstract reports lower direct-condition force overestimation, no indirect-condition group difference, and a contemporaneous relationship with YGTSS total tic severity beyond medication load, obsessive-compulsive symptoms and urge severity. The exact score formula, fitted model, coefficients, intervals, outcome-specific n and missingness are unverified. The abstract's proposed behavioral-marker interpretation is not prospective validation.

[Isaacs et al., PMID 42810670](https://pubmed.ncbi.nlm.nih.gov/42810670/), [DOI 10.1016/j.biopsycho.2026.109408](https://doi.org/10.1016/j.biopsycho.2026.109408), electronically dated 29 September 2026, compares 28 adults with CTD and 34 controls using paired pneumatic stimuli and EEG. Its abstract reports no group difference in P50/N140/P300 gating or gating association with tactile responsivity. Smaller first-stimulus P50 responses occur in CTD and relate to responsivity. These results and the missing numerical inputs were previously audited on [12 October](../../sensory_gating/2026-10-12/report.md); that unchanged numerical task was not repeated.

Neither abstract establishes effects specifically among persistent severe or treatment-refractory adults, nor validates pediatric or ASD/communication subgroups. Unverified characteristics must not be described as excluded or absent. Sensory distress and functional burden remain meaningful even when a selected laboratory measure is null.

## Original construct and estimand comparison

| Question | Action-related force matching | Repeated pneumatic stimulation |
|---|---|---|
| Manipulation | Reproducing a target directly by finger versus indirectly through button control | First versus repeated externally delivered tactile input |
| Observed domain | Behavioral reproduction/overestimation | Electrical response amplitudes and derived gating indices |
| Required specificity contrast | Difference between the two condition-specific group effects, or a prespecified equivalent model contrast | Group difference in a defined repeated-input index or appropriate group-by-stimulus contrast |
| Clinical association | Current tic severity with reported covariate adjustment | Tactile responsivity, a different outcome |
| Alternative source of contrast | Motor execution, force calibration, task order, learning or target-memory differences | First-response generation, adaptation, baseline/index definition or recording quality |
| What cannot be inferred | A direct-condition difference alone does not isolate an internal forward-model defect | A first-stimulus amplitude difference alone does not establish defective suppression of the repeated stimulus |

The alternatives in this table are **audit questions**, not demonstrated confounds in these studies. Both paradigms involve touch but differ in active motor generation, temporal comparison and measurement scale. Standardizing both to a dimensionless effect would not create construct equivalence. Cohort overlap is unverified; summing sample sizes as independent evidence would be unjustified.

## Formal contrast and the exact missing quantities

For a hypothetical common behavioral outcome Y with identical scale in direct D and indirect I conditions, define the target contrast:

`Delta = (mean_TS,D - mean_control,D) - (mean_TS,I - mean_control,I)`.

This defines an audit estimand, **not the paper's verified fitted model**. If both conditions are observed in each person, their covariance contributes to the uncertainty of Delta. Four means and four marginal standard deviations do not alone identify its standard error. A reported model contrast and CI, or the correct covariance-aware aggregate output, could resolve it without participant rows. Effects averaged across target-force levels may require another contrast or interaction; the target levels, weights, transforms and random-effects structure remain unknown.

Distinct questions must stay distinct:

1. **Within-condition diagnosis effect:** does the direct condition differ by group?
2. **Condition specificity:** does that group effect differ from the indirect-condition group effect?
3. **Concurrent association:** does a selected behavioral measure explain additional current severity variation under the stated model?
4. **Prospective utility:** does a locked measure/model predict later outcomes in independent or appropriately held-out participants, improve on baseline severity, and remain calibrated?

A positive answer to one does not supply the others. Covariate adjustment is not randomization. Medication load can reflect prior severity or treatment selection; urge and obsessive-compulsive scores may be correlates, mediators or confounders depending on the causal question. We cannot choose their role from a variable list. Thus an adjusted association need not identify the total causal effect of changing attenuation. No patient-specific inference follows.

A complementary [synthetic contrast demonstration](model/report.md) is documented separately by the integrating daily analysis. Its invented inputs must remain separate from these studies and cannot supply their missing precision or an empirical interaction.

## Access findings and provenance

- Official PubMed XML was readable for both studies. No PMCID or linked correction notice was present in the inspected records. This is not a comprehensive correction-history audit.
- Wiley landing/full XML and the metadata-listed PDF route returned HTTP 403. The DOI/web reader was also inaccessible. These are access restrictions, not proof of a broken article.
- Europe PMC reports no archived full text for the new study. OpenAlex labels publisher access bronze and lists an OSF location. These differing metadata flags do not establish actual full-text access or a reuse license.
- The [OSF project](https://osf.io/cvsrz), independently checked through its official API, matches the title. Its flags are `registration=false` and `preprint=false`. A project created before journal publication is not thereby a preregistration. Its empty description, no wiki/children and two top-level files named as datasets did not supply standalone methods. Only listing metadata was inspected. The `.omv` files were neither downloaded nor parsed, because aggregate results could be mixed with participant rows.
- A related institutional/conference title was located, but the institutional item returned 403. The ESSTS download page explicitly states member restrictions; no linked presentation files were fetched. Neither listing is counted as independent replication or as the final article's methods.
- The older study's ScienceDirect route returned HTTP 200 with a short “Site Unavailable” page. It was not counted as paper access. The prior 12 October gate remains unresolved.

Exact routes, timestamps, source identity and bounded search terms are recorded in `source-checks.json`. No full-text paper, participant data, contact details, account request or restricted download is retained.

## Decision and next gate

**Completed:** construct reconciliation, explicit estimand map, fresh safe-source checks and a documented reason not to open mixed datasets. **Blocked:** empirical group-by-condition estimate/CI, model denominator, missingness, force-level effects and prospective-validation appraisal beyond the abstract.

The prerequisite is a lawful public manuscript or participant-free statistical output giving the contrast definition, coefficient/CI or joint covariance, analysis n, exclusion/missingness flow, medication handling and clinical-model specification. Do not request participant data, contact authors, acquire access or repeatedly probe restricted routes under this task.

Close this access pass. Retain both the positive behavioral association and the negative repeated-input finding without declaring them contradictory replications. Reopen the numerical audit only when the specific safe source becomes available.

**Next bounded question:** audit the primary modeling study [Divisive attenuation based on noisy sensorimotor predictions accounts for excess variability in self-touch](https://doi.org/10.1152/jn.00055.2025), PMID 40531356, PMCID PMC7617943. Its lawful Europe PMC manuscript XML was accessible today; title, identifiers, abstract and model-section headings were verified, not its full conclusions reanalyzed. Determine which explicit memory/noise/calibration assumptions make a direct-minus-indirect contrast identify predictive attenuation, and what aggregate patterns discriminate divisive from subtractive or nonpredictive accounts. Use published equations and nonidentifying summaries only, not its participant datasets. This is an accessible construct-identification question, not a claim that its model proves the mechanism in TS. A baseline repository search found no prior audit of this DOI/PMCID/title.
