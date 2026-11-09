# H18 measurement anchors and transfer

Project NeuroFreedom | 9 November 2026 | Bounded historical primary-evidence audit

## Decision

**No inspected measure passes the proposed external-anchor gate. Keep H18's latent mechanism unidentified and close this fixed audit.** The six reports offer useful evidence about measurement feasibility, agreement between raters, correlations and short-term context sensitivity. They do not provide a calibrated, treatment/context-invariant measurement that separates reduced urge generation from improved action control.

This is a result of a bounded source audit, not evidence that a valid anchor cannot exist, that urges are unreal, or that behavioral therapy is ineffective. Some source access was partial. The favorable measurement findings and opposing explanations remain in the [six-source adequacy matrix](measurement-adequacy.json). No participant data, video, new experiment, model fitting or treatment recommendation is involved.

## Question and disconfirmation

The [November 8 weekly plan](https://github.com/dotjade/project-neurofreedom/blob/a68355a22f7de6e694ac4df29ad670983dd6c68f/updates/2026-11-08-weekly-synthesis.md) asked whether existing public aggregate evidence supplies a defensible external anchor for distinguishing urge-generation change from action-control change. Its prediction was that repeatability or correlation alone would be insufficient. Evidence for stable construct meaning, response thresholds/loadings and timing across a relevant manipulation or context, together with a defensible identifying restriction, would weaken that prediction and permit design preparation. Neither statistical significance nor a high reliability coefficient was the success criterion.

The audit followed the six-report ceiling and stopped after extracting the selected reports. It did not rerun the [completed simulation](https://github.com/dotjade/project-neurofreedom/blob/a68355a22f7de6e694ac4df29ad670983dd6c68f/analyses/h18_identifiability/2026-11-08/report.md). The question and decision rules preceded this run; the source selection was made during retrieval, not independently preregistered. The 90-minute cap was an upper bound, not a claim of 90 minutes of completed work.

## Actual source results

The matrix is the canonical numerical extraction. Each row includes population, construct, comparator, reliability type, uncertainty, temporal resolution, clustering, missingness, invariance, competing explanation and an explicit transfer limitation.

- [Reese et al.](https://doi.org/10.1016/j.beth.2013.09.002) support short-interval test–retest relative stability of global PUTS scores in an older-adolescent/adult trial sample. That does not establish absolute agreement or stability during therapy. This reuses the original adult-dominant CBIT cohort, rather than adding an independent treatment replication.
- [McGuire et al.](https://doi.org/10.1016/j.jpsychires.2016.09.007) provide tic-specific, past-week I-PUTS dimensions with inter-rater ICCs and uncertainty. Agreement between raters of an assessment is not repeated-session reliability, adult validation or treatment invariance.
- [Baumung et al.](https://doi.org/10.1111/jnp.12216) distinguish dimensions and expose problematic item behavior. Separate exploratory factor solutions across age groups do not establish equal thresholds/loadings, and proposed revised items are not a fully validated replacement scale.
- [Brandt et al.](https://doi.org/10.3389/fpsyt.2016.00051) link a global questionnaire to momentary urge reporting. Both depend on subjective reporting, so their correlation is not an independent calibration of latent urge generation.
- [Langelage et al.](https://doi.org/10.1038/s41598-022-19685-5) combine temporally resolved reporting with video-rated tics. Aggregate positive association coexists with heterogeneous individual associations. An observed-tic outcome is an external observation of expression, not a uniquely interpretable anchor for the mechanism that produced it.
- [Matsuda and Kano](https://doi.org/10.5765/jkacap.260010) directly compare reporting and suppression conditions. Their July 2026 paper is historical evidence newly examined here, not a November 9 publication. Its data were collected in 2012–2013. The exploratory urge/fatigue contrasts raise measurement-reactivity questions, while nonsignificant tic and mean-monitor contrasts do not establish equivalence or absence of burden. Reporting could change attention, genuine experience, motor workload or response criteria; this design does not uniquely separate them.

**Counterevidence to an overly pessimistic account:** the sources contain genuine positive reliability, convergent-validity and task-manipulation evidence. More temporally specific and tic-specific measures are feasible. The gate fails because these are insufficient identifying restrictions, not because every measurement fails or all results are null.

## What an anchor would have to establish

These are methodological requirements, not observed properties of the instruments.

1. **Define the target construct.** Urge frequency, intensity, sensory quality, awareness, perceived control and willingness to tolerate an urge are not interchangeable. A measure of conscious experience need not be a measure of latent generation. Keep global and tic-specific measures distinct.
2. **Separate precision from invariance.** Establish absolute agreement and uncertainty at the intended repeat interval under a suitable stable-condition design, rather than demanding unchanged scores during effective treatment. Then test treatment/time/context dependence of loadings and thresholds or intercepts, with an anchor not defined solely by the same tic reduction. A shared factor pattern is weaker than metric/scalar invariance; invariance within a questionnaire still does not prove biological specificity.
3. **Make temporal assumptions testable.** Prespecify whether the measure is sampled before a tic, during suppression or after a task. Quantify response latency and observation lag. A past-week summary cannot identify second-scale causal order; concurrent association cannot rule out anticipation or a common cause.
4. **Treat observation as part of the intervention context.** Reporting and operating a device may change the state under study. A no-report comparator can test some reactivity, but cannot directly observe the unreported experience. Avoid calling absence of a significant tic contrast proof of nonreactivity.
5. **Use the participant as the independent unit.** Seconds, tics and repeated sessions remain nested. Retain the covariance needed for longitudinal and cross-context contrasts. Missing audio, unusable recordings, changing tic inventories and incomplete ratings can change which construct is observed.

The exact missing prerequisite is **aggregate evidence supporting a specific measurement mapping with bounded systematic reporting change across the relevant intervention/context**, plus aggregate within-participant covariance estimates and outcome-specific denominators adequate to assess a discriminating contrast. No numerical bound for that systematic shift was established. Assigning one would merely repeat the simulation's unverified assumption.

## Transfer estimands must be separate

These are definitions for evaluating future evidence, not a registered or initiated human study. None is estimated by this audit.

**Context transfer:** for a prespecified population, intervention strategy A and comparator, define the intervention effect on an outcome in an untrained context B at a stated follow-up t. In potential-outcome notation, this is E[Y_B(t, A=1) − Y_B(t, A=0)]. Specify the context, observation instructions, medication/rescue policy, missing-outcome approach and endpoint direction in advance. A trained-context effect alone does not identify this contrast.

**Tic transfer:** define the target set before allocation, rather than selecting tics that happen to remain untreated or visible afterward. Evaluate a policy that reserves that set from direct training, preserving subsequent rescue/crossover in the chosen estimand. A total score containing trained tics cannot isolate the effect on the reserved set. Changing the inventory after improvement can create an artificial transfer signal.

**Transfer gap:** compare effects in untrained and trained contexts, Δ_B − Δ_A, with their covariance and compatible units. A ratio becomes unstable when the trained effect is small. A nonsignificant gap does not establish equivalent transfer; that would require a defensible prespecified margin and adequate precision. Even demonstrated transfer does not reveal mechanism unless the mechanisms' transfer properties are independently constrained.

**Durable functional benefit:** estimate a randomized strategy effect at a prespecified follow-up on directly measured function, alongside pain, effort, participation, co-occurring burden and harms. Do not substitute observed tic counts, response-conditioned follow-up or sustained access to training for an all-assigned, off-training or treatment-policy estimand. Persistent severe adult burden is a target applicability requirement, not established by an age-mixed or narrowly selected sample.

## Next decision and stop rule

Close the six-source anchor audit and keep H18 proposed. Do not advance to a mechanism-based allocation rule, collect personal records or run another version of the same unanchored simulation. Reopen this question only for a source that supplies the named invariance/calibration evidence, a useful aggregate correction, or a genuinely randomized transfer/strategy contrast with meaningful function and burden outcomes.

The next routine research run should continue the protocol's new-publication, registry and safety checks and act on genuinely changed prerequisites. A clinical-benefit trial can be interpretable without identifying every latent mechanism; this stop applies to the unsupported mechanism assignment, not to all behavioral-treatment research. Any later participant study would need institutional leadership, ethics/consent and data governance, none of which is initiated here.

## Coverage and verification

Repository context was checked against commit `a68355a22f7de6e694ac4df29ad670983dd6c68f`: README, research protocol, status, current evidence, November 7 mechanism audit, November 8 simulation and weekly synthesis, and public journal-source README. Sources were selected for measurement relevance rather than a date-limited effectiveness review. dot performed the AI-assisted extraction; a separate AI source/method review checked selected claims and corrections, not independent clinical peer review. Individual search-call timestamps were not retained; the ledger distinguishes two observed UTC clock checks from actual search times. [Search and access ledger](search-ledger.json) records exact queries, focal-source dispositions and failures. The six inspected primary reports are not six independent cohorts and are not an exhaustive psychometric review.

Publisher HTML was readable for Baumung and Brandt. Langelage's publisher abstract, PDF methods and indexed primary results were inspectable, but later direct retrieval failed. Initial Reese, McGuire and Matsuda extraction used indexed primary-source passages and official abstracts after direct routes failed. Their main-text sections subsequently became readable during a separate source/method review, which verified and expanded the extraction. Initial failures remain in the ledger. Langelage results/counts rely on indexed primary passages; its complete statistical methods and supplement remain unreviewed. Other unseen supplements and unverified details remain explicit. Focused DOI correction/retraction searches identified no notice in returned results; that is not comprehensive clearance.

The validation script checks the authored matrix's schema, limits, identifiers, structured numeric extraction arithmetic and inferential boundaries. Numeric accounting uses the matrix's structured fields rather than stand-alone hard-coded reference calculations. It does not compare those fields automatically against the papers or independently verify transcription. These are consistency checks, not independent source verification or clinical peer review. No repository write, source-paper republication, participant data access or clinical action was performed by this audit.
