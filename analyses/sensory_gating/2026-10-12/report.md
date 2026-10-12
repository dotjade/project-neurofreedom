# Adult pneumatic somatosensory gating methods and precision audit

12 October 2026 | Project NeuroFreedom | Bounded follow-up to the 9 October extraction

## Decision

Keep the adult pneumatic-gating result as **counterevidence to a generalized gating-deficit account in this paradigm, with precision unresolved**. Do not label the groups equivalent, infer that every relevant deficit is absent, or recast the first-stimulus P50 finding as a demonstrated gating deficit. No study effect, confidence interval, equivalence result, or effect-size bound could be calculated from the accessible quantities.

This pass adds a specific analysis-access decision. The abstract names **gating differences and regression marginal effects**; a conventional P50 ratio analysis must not be silently substituted. A public publisher PDF is discoverable and publisher-deposited metadata lists a CC BY 4.0 version-of-record license. Nevertheless, the actual paper and its tables were not retrievable through the tested routes. The limitation is verified retrieval failure, **not a verified paywall or proof that no lawful full text exists**.

## Prediction and falsification check

[The analysis plan](preanalysis.md) was written before new source retrieval and calculation, after the prior abstract result was known. The strong hypothesis predicts reduced attenuation of repeated tactile input in CTD and a relationship between poorer gating and tactile responsivity. The reported nulls fail to supply that predicted positive evidence. Decisive rejection of a quantitatively meaningful deficit would require adequate uncertainty estimates against an independently justified margin. Neither is available here. This was not preregistration or a blinded prediction of the paper's findings.

## Verified study finding

Isaacs and colleagues studied 28 adults with CTD and 34 neurotypical adults with paired pneumatic stimulation and dense-array EEG. The abstract reports no group difference in P50, N140 or P300 gating indices and no gating–responsivity association. CTD showed a smaller first-stimulus P50; within CTD, smaller S1 P50 related to greater tactile responsivity. No other component-amplitude group difference was reported. This is a single-assessment comparison, not a treatment or trajectory experiment. [Primary abstract](https://pubmed.ncbi.nlm.nih.gov/42810670/); [DOI](https://doi.org/10.1016/j.biopsycho.2026.109408).

## What the pattern does and does not test

1. **Response generation and repeated-input attenuation are distinct outcomes.** An S1 amplitude contrast cannot establish that S2 suppression is impaired. A response to the first stimulus may be relevant to early sensory processing without identifying the mechanism of later attenuation.
2. **Index definitions matter.** Difference scores and regression marginal effects can address different conditional questions. Polarity, subtraction order, baseline handling, transformations, and model adjustment need verification, particularly across positive and negative ERP components. We cannot infer the direction or size of a reported index from its name.
3. **A zero group mean contrast would not prove zero subgroup effects.** Adult diagnosis alone does not establish applicability to people with continuously severe tics, pain, refractory treatment histories, or substantial functional burden. These characteristics are unverified, rather than known absent or excluded.
4. **The nulls do not refute reported sensory distress.** Self-reported responsivity and a laboratory attenuation measure are different constructs. Failure of one proposed physiological explanation does not invalidate the experience.
5. **The S1 association is a narrower candidate, not a replacement established mechanism.** Cross-sectional association cannot identify causal direction or show that changing S1 P50 would improve tics or function. Multiplicity, reliability, covariate sensitivity and replication remain prerequisites. Statistical significance of one outcome and nonsignificance of another also do not establish that their effects differ.
6. **Do not generalize modalities or interventions.** Pneumatic tactile stimulation does not by itself settle auditory gating, electrical median-nerve responses, every inter-stimulus timing, or treatment efficacy. No completed MNS calculation or generic adult-resource search was repeated.

## Exact missing prerequisites

The [structured extraction](extraction.json) marks unverified fields explicitly. The immediate requirement is usable methods and statistical output, not new participant records.

| Intended inference | Minimum quantities or definitions still needed |
|---|---|
| Between-group difference-score estimate and interval | Exact index and polarity; group mean index, SD or SE, and outcome-specific analysis n; test/model and confidence level. A directly reported contrast with SE/CI and its inferential specification could suffice instead. |
| Reconstruct a difference-score variance from S1/S2 summaries | Both component variances **and their within-person covariance/correlation**, or the SD of the paired difference itself. Separate S1/S2 SDs alone are insufficient. |
| Interval for a regression marginal effect | Exact estimand, covariates, coefficient/contrast estimate, SE or CI, reference/averaging scheme, degrees of freedom or asymptotic method, and any robust/clustered variance procedure. Joint contrasts require the appropriate covariance matrix. |
| Tactile-responsivity association | Named scale, scoring direction, model, actual association estimate, analysis n, uncertainty, and adjustment/multiplicity specification. A partial or regression association must not be treated as an unadjusted Pearson correlation. |
| Equivalence or exclusion of a meaningful deficit | Above information plus a defensible independent smallest relevant effect/margin and the matching equivalence/one-sided inference. The margin must not be reverse-engineered from nonsignificance. |
| Severe-persistent adult applicability | Recruitment and diagnostic criteria; TS versus other CTD composition; ages and duration; severity/impairment distribution; pain/function measures; treatment refractoriness, if measured. |
| Confounding, selection and signal-quality appraisal | Comorbidity diagnoses and symptom scales; medications, doses/timing/stability and any adjustment; relevant exclusion criteria; handedness/stimulation site and timing/intensity; EEG reference/filters, trial rejection, tic artifact handling, retained trials, component windows/electrodes and reliability; missingness and multiplicity/preregistration. |

For illustration of the missing quantity only, if the actual score were D = S1 − S2, Var(D) = Var(S1) + Var(S2) − 2Cov(S1,S2). This is an algebraic requirement, not a claim that the paper used this sign or a calculation of its variance. For an unadjusted independent-group contrast, a Welch standard error could use sqrt(sD,CTD²/nCTD + sD,control²/ncontrol); the observed SDs and endpoint-specific n are not available. None were imputed.

The reported group counts alone do not identify a study confidence interval. We did not assume an observed effect of zero, infer an exact p-value from a verbal null, import another paper's SD/covariance, or present a sample-size-only power calculation as this study's precision.

## Access, provenance and correction check

- Baseline read: repository README, protocol, status, the original gating evidence record, 9 October scan and 11 October weekly synthesis. Their priorities close the unchanged MNS and generic adult-cohort work and select this question.
- Current official PubMed XML was retrieved successfully. Its electronic-publication date is 29 September 2026; its metadata revision is 8 October. A revision date is not evidence of a new study or a scientific correction. Crossref associates the article with volume 211 and the November 2026 issue, which does not replace the September online-publication date.
- No linked CommentsCorrections entry appeared in the retrieved PubMed XML. The inspected Crossref record had no update-to item and an empty relation object. This is a limited metadata check, not a completed publisher/Crossmark or retraction-database audit.
- ScienceDirect's landing page and public PDF, the Crossref-linked Elsevier API and the linking-hub route failed to supply the paper. The **dot cloud browser** independently displayed “Site Unavailable” for both publisher page and PDF. No user computer was used. A successful HTTP status returning an error page was not counted as successful paper access.
- PubMed's PMC link query returned no linked PMC record. OpenAlex reported no repository full-text location, and its only paper PDF location was the publisher URL. Targeted institutional/author/preprint searches found no usable copy. Europe PMC API attempts returned 503 and cannot support a negative availability claim.
- Crossref's publisher-deposited record includes a CC BY 4.0 version-of-record license starting 29 September; PubMed retains an all-rights-reserved copyright string. We recorded the discrepancy without adjudicating reuse permissions or saving the paper. No full-text paper, participant file, contact list, or personal medical data is in this deliverable.

[PubMed XML source](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=42810670&retmode=xml), [publisher-deposited Crossref metadata](https://api.crossref.org/works/10.1016%2Fj.biopsycho.2026.109408), [publisher PDF location](https://www.sciencedirect.com/science/article/pii/S0301051126002218/pdf), [OpenAlex discovery metadata](https://api.openalex.org/works/https://doi.org/10.1016/j.biopsycho.2026.109408).

## Executed work and next gate

Executed: bounded retrieval, original structured extraction, hypothesis reconciliation, and the standard-library metadata audit [check_source_metadata.py](check_source_metadata.py). Actual selected-metadata output and retrieval/identity validation are in [source_metadata.json](source_metadata.json) and [source_check.log](source_check.log). This code is **not** an effect-size reanalysis or a clinical result. No statistical uncertainty computation was executed because the required inputs were unavailable.

**Stop this access pass.** Reopen the numerical question when a working lawful full-methods/table source is available. First extract the existing contrasts and uncertainty, then decide whether a reproducible aggregate analysis is justified. Any author contact, institutional access arrangement, participant-data application or clinical experiment requires its own authorization and governance. In the meantime the portfolio should retain the null result and the narrower S1 signal with the precise limitations above; it should not promote either into equivalence, a treatment target or a cure claim.

This report is an evidence-access and methods audit by an assistant, not independent clinical peer review or an exhaustive systematic search.
