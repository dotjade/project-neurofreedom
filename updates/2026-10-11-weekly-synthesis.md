# Project NeuroFreedom first weekly synthesis

11 October 2026 | Work completed 8–11 October 2026

## Bottom line

The first four days produced a research framework, one executed synthetic forecasting benchmark, a numerical reporting audit, a published-aggregate attrition sensitivity analysis, structured evidence comparisons and two bounded dataset-feasibility audits. The strongest progress is knowing which claims the evidence can support and which analyses cannot yet be run. No cure, disease-modifying mechanism or validated individual predictor was discovered.

The mission covers Tourette syndrome and chronic tic disorders across all ages and severities. Persistent severe adult symptoms, pain, functional and social burden, co-occurring conditions and unmet treatment needs remain central. Developmental improvement, quiet periods and remission are subquestions; none is assumed to describe everyone's course. This is the first weekly synthesis, covering the actual 8–11 October work rather than a full seven-day research period or an exhaustive review of the field. [Current scope and protocol](https://github.com/dotjade/project-neurofreedom/blob/5d91322cfe927e28fdb7d0e1995187e0db53e0a3/RESEARCH_PROTOCOL.md).

## What was completed

- **8 October:** created the initial source-linked portfolio, 20 falsifiable hypotheses and staged research plans; extracted 15 primary-study records; executed and checked the synthetic cycle-detection benchmark.
- **9 October:** completed a dated evidence scan, five-study stress/context reconciliation, deterministic reporting check and four-study remission-endpoint comparison. Three additional primary-study records brought the structured ledger to 18. These were newly identified or indexed sources, not three new discoveries by this project.
- **10 October:** made the all-age, severe-adult-inclusive mission explicit; completed another dated scan and a five-cohort compatibility audit for a proposed within-person antecedent analysis.
- **11 October:** completed the daily scan and a six-family adult-resource audit. The bounded adult search closed without a complete design match. A September MNS follow-up supplied a feasible published-aggregate durability question for this weekly run.

The dated scans did not verify a newly first-published qualifying primary tic study or newly posted trial result in their narrow update windows. That negative result is limited by timing, source coverage and access. The 11 October search was already completed before this synthesis and was not repeated. Search counts overlap across days and must not be added as independent studies. [Execution record](https://github.com/dotjade/project-neurofreedom/blob/5d91322cfe927e28fdb7d0e1995187e0db53e0a3/STATUS.md), [9 October scan](https://github.com/dotjade/project-neurofreedom/blob/5d91322cfe927e28fdb7d0e1995187e0db53e0a3/updates/2026-10-09-evidence-scan.md), [10 October scan](https://github.com/dotjade/project-neurofreedom/blob/5d91322cfe927e28fdb7d0e1995187e0db53e0a3/updates/2026-10-10-evidence-scan.md), [11 October scan](https://github.com/dotjade/project-neurofreedom/blob/5d91322cfe927e28fdb7d0e1995187e0db53e0a3/updates/2026-10-11-evidence-scan.md).

## What was tested and learned

### A repeating fit is not enough to establish a biological cycle

The synthetic benchmark used seven scenarios, 240 matched replicate trajectories per scenario and three history lengths, producing 5,040 history/forecast evaluations. These are generated numbers, not patients or 5,040 independent subjects. Eleven implementation tests passed; independent checks reproduced numerical outputs and corrected a zero/constant/linear-history diagnostic edge case.

Under the specified simulator, 76.7% of short, autocorrelated but nonperiodic histories met an illustrative apparent-cycle flag. Their harmonic forecasts nevertheless had 92.3% higher average future error than the past-selected nonperiodic baseline. Conversely, a stable injected rhythm was forecastable under favorable assumptions. A drifting rhythm could defeat the fixed-period model. Most importantly, a latent oscillator and periodic reporting bias were constructed to produce exactly the same observations and forecasts.

**Decision:** require untouched future observations, suitable nonperiodic comparators and independent measurement channels before advancing a cycle claim. Successful forecasting cannot by itself identify a biological oscillator; failure of one fixed-period model cannot reject every oscillatory mechanism. The percentages above are simulator results, not clinical false-positive rates or advice about observation frequency. [Executed benchmark and limitations](https://github.com/dotjade/project-neurofreedom/blob/5d91322cfe927e28fdb7d0e1995187e0db53e0a3/analyses/cycle_detection/README.md), [validation record](https://github.com/dotjade/project-neurofreedom/blob/5d91322cfe927e28fdb7d0e1995187e0db53e0a3/analyses/cycle_detection/VALIDATION.md).

### Stress effects depend on the outcome and timescale being estimated

The five-study comparison did not support a universal rule that higher stress immediately produces more visible tics. A pediatric longitudinal cohort reported a modest preceding-stress association with later severity, while immediate laboratory counts showed null, inverse or suppression-context-dependent patterns. An adult weekly-report study found a same-week association but no overall one-week-lag association.

These studies change population, exposure, task, informant and outcome as well as timescale. They do not demonstrate a biological effect reversing sign over time. Immediate visible frequency and later rated burden are different quantities. Delayed stress effects, context-dependent expression, reporting bias and common causes remain competing explanations.

The deterministic audit found that the printed Buse 2016 interaction statistic F(2,54)=3.1 implies p approximately .05315, inconsistent with its printed p<.044. A second calculation confirmed the discrepancy. This does not identify which printed value is wrong or reproduce the participant-level analysis.

**Decision:** retire only the universal immediate stress-to-more-tics claim. Keep narrower delayed and context-specific hypotheses, with independent outcome measurement and forward prediction required before promotion. The actual adult antecedent analysis remains unexecuted. [Study comparison and audit](https://github.com/dotjade/project-neurofreedom/blob/5d91322cfe927e28fdb7d0e1995187e0db53e0a3/analyses/stress_context/README.md); primary anchors: [Lin 2007](https://pmc.ncbi.nlm.nih.gov/articles/PMC3073143/), [Buse 2016](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2016.00084/full), [Hoekstra 2004](https://www.psychiatrist.com/jcp/association-small-life-events-self-reports-tic-severity/).

### Remission proportions cannot be combined without defining the endpoint

The four-study extraction found direct within-cohort disagreement between self-reported absence, routine examination and more sensitive observation. Low impairment can coexist with observable tics. Conversely, one observed tic does not establish continuous disability or erase a person's meaningful improvement.

Ascertainment explains part of the apparent contradiction, but not every cross-cohort difference. Recruitment, age, developmental window, treatment and missing participants also differ. No common repeatedly confirmed, medication-free remission endpoint was recoverable, so no pooled remission rate was calculated.

**Decision:** keep tic presence, severity, pain, impairment, participation and quality of life separate. Groth's original journal denominator still needs verification; the thesis reconstruction may count repeated assessments rather than unique people. Burd's operational definition remains abstract-limited. The expanded New Tics cohort overlaps the earlier sample and is not independent replication. Its broader endpoint extraction remains pending. [Four-study harmonization and primary links](https://github.com/dotjade/project-neurofreedom/blob/5d91322cfe927e28fdb7d0e1995187e0db53e0a3/analyses/remission/2026-10-09-harmonization.md).

### Sleep does not establish a universal off switch

Primary overnight studies observed tics during sleep, including across sleep stages. This contradicts universal cessation, while leaving state-dependent modulation, arousal and sleep-related burden as useful research questions. A sleep–tic association does not identify causal direction, and less movement is not automatically recovery of normal voluntary function.

**Decision:** retain a narrower sleep-state mechanism question; do not build a cure claim on the assumption that sleep eliminates tics. No new sleep experiment was performed this week. [Cohrs adult polysomnography study](https://pubmed.ncbi.nlm.nih.gov/11160467/), [Glaze overnight study](https://pubmed.ncbi.nlm.nih.gov/6573576/), [foundation synthesis](https://github.com/dotjade/project-neurofreedom/blob/5d91322cfe927e28fdb7d0e1995187e0db53e0a3/foundation.md).

### The proposed adult antecedent analysis is not yet executable

The 10 October audit assessed five cohort families; the 11 October extension assessed six additional resource families. None demonstrated the full combination of appropriately timed exposures, independent observed outcomes at days/weeks resolution, adequate linked lag windows, treatment/missingness histories, a characterized severe-persistent adult subgroup and a lawful route to the necessary records.

The closest resources answer different questions:

- **Nottingham home MNS:** repeated independently coded tic videos, but treatment-focused and without documented repeated non-treatment antecedents or a defined persistent-severe-adult stratum.
- **UF responsive DBS:** directly relevant severe adult disease and physiological measurements, but treatment-responsive programming, stimulation state and mismatched windows complicate natural-history inference.
- **Calgary/Paris adult registries:** useful leads for adult burden and treatment course at their documented longer timescales, not a substitute for unobserved daily dynamics.

**Decision:** close the bounded generic cohort search. Reopen only for a new release/protocol or a separately authorized, specific custodian clarification. This is a negative feasibility finding for a defined design, not evidence that antecedents do not exist. No participant files were obtained or analyzed. Public file listings, an author-request statement and a controlled-access archive each fall short of granted usable access. Pediatric data must not replace the adult target. [Five-cohort audit](https://github.com/dotjade/project-neurofreedom/blob/5d91322cfe927e28fdb7d0e1995187e0db53e0a3/analyses/data_feasibility/2026-10-10-audit.md), [six-family adult audit](https://github.com/dotjade/project-neurofreedom/blob/5d91322cfe927e28fdb7d0e1995187e0db53e0a3/analyses/data_feasibility/2026-10-11-adult-audit.md).

## Treatment durability and this weekly computation

The September 2026 MNS follow-up comes from the earlier randomized trial; it is not independent replication or a new October publication. Its active-arm motor-tic analysis reports 41 participants at baseline, 36 after four weeks and 15 at three months. Three-month retention for this analysis is therefore 15/41, about 36.6%.

The reported returnee improvement is worth assessing, but there is no contemporaneous sham comparison at that follow-up. Missing outcomes, selection, natural fluctuation and treatment history remain alternative explanations. These denominators do not establish a responder count, and a motor-tic endpoint is not total tic burden or function. [MNS follow-up](https://pubmed.ncbi.nlm.nih.gov/42704310/), [original controlled trial](https://pmc.ncbi.nlm.nih.gov/articles/PMC10947020/).

### Executed aggregate sensitivity analysis

The prespecified computational question was whether the sign of the full-41 mean motor-score change survives every possible missing follow-up mean on the 0–25 scale. An admissible missing-outcome scenario erasing improvement would disconfirm that strong robustness claim. This was specified before calculation, after the source aggregates were known; it was not a preregistered clinical study.

At three months, 15 returnees had mean motor score 15.33 versus their own baseline 18.73, a mean improvement of 3.40 points. An average worsening of **51/26 = 1.9615 points among the 26 missing participants** would offset that improvement in the full-41 mean. This is a hypothetical aggregate threshold, not evidence that missing participants actually worsened. No responder count can be inferred.

Conditional on the printed overall baseline 18.62, full-cohort three-month change is bounded by **−13.0115 to +2.8422 points** when missing outcomes range across the scale. The sign is therefore not identified. Four-week bounds, with 36 observed, remain negative: **−4.3517 to −1.3029**. Neither before/after result establishes causality without the appropriate control comparison.

A source inconsistency was preserved: the printed baseline means for 36 returnees and five early dropouts combine to 18.8507, not the printed full-41 value 18.62; ordinary rounding cannot reconcile them. An explicitly hypothetical alternative-baseline branch preserves both qualitative conclusions. The change-based 1.9615 threshold depends on the paired returnee means and counts, not the disputed full baseline. Rounding sensitivity also preserves the conclusions. These are identification bounds and scenarios, not confidence intervals or fabricated participant trajectories.

The deterministic exact-fraction implementation archived its source inputs, source locators, code and actual outputs. Nineteen unit tests and 56 separate Decimal checks passed; a separate reviewer reproduced outputs byte-for-byte and passed 275 additional exact-arithmetic, rounding and provenance checks. This is computational verification, not independent clinical peer review. [Analysis and limitations](https://github.com/dotjade/project-neurofreedom/blob/main/analyses/mns_attrition/report.md), [reproduction instructions](https://github.com/dotjade/project-neurofreedom/blob/main/analyses/mns_attrition/README.md).

**Decision:** reject only the stronger inference that full-cohort three-month improvement is robust regardless of missing outcomes. Preserve the reported returnee improvement and the possibility of benefit. Do not infer no efficacy, durable disease modification, a cure or applicability to a severe-adult subgroup from this calculation.


The wider treatment portfolio retains the same distinction: symptomatic benefit during treatment can be real without proving lasting alteration of disease. Ecopipam's responder-enriched randomized-withdrawal evidence does not establish off-treatment disease modification; its small adult subgroup cannot settle persistent-severe-adult effectiveness. MNS rhythm specificity is challenged by benefit during both rhythmic and arrhythmic stimulation in a separate crossover trial, without refuting all possible stimulation effects. [Ecopipam phase 3](https://pubmed.ncbi.nlm.nih.gov/42189524/), [MNS crossover](https://pubmed.ncbi.nlm.nih.gov/37048598/).

## Which hypotheses changed status

- **Contradicted as universal statements:** sleep eliminates all tics; immediate stress consistently increases visible tic counts.
- **Not supported by the methods test:** a strong repeating fit alone identifies a biological cycle; a forecast gain alone identifies its mechanism. The synthetic result does not reject all biological cycles.
- **Supported only in part:** ascertainment and endpoint differences help explain apparent remission disagreement. They do not explain every cohort difference or yield a single pooled remission rate.
- **Weakened in a specified paradigm:** a general somatosensory-gating-deficit account. A 28-adult tic-disorder versus 34-control EEG study reported no group differences in its gating indices. Full precision and methods remain unverified; nonsignificance is not equivalence, and this does not retire every gating pathway or the MNS mechanism question. [Primary abstract](https://pubmed.ncbi.nlm.nih.gov/42810670/).
- **Feasibility prediction failed within the audited scope:** finding a fully documented, accessible adult days/weeks independent-outcome dataset. The biological antecedent prediction remains untested.
- **Still proposed:** the portfolio's 20 causal/therapeutic hypotheses, including adult reversibility of genetically anchored circuit changes, mechanism-specific stimulation and durable behavioral/pharmacological synergy. No hypothesis becomes a discovery merely by appearing in the portfolio. [Hypothesis definitions and falsification rules](https://github.com/dotjade/project-neurofreedom/blob/5d91322cfe927e28fdb7d0e1995187e0db53e0a3/hypotheses.md).

Two reporting safeguards also mattered. A recent adult rTMS registry posting described a five-person study completed in 2012 and terminated for lack of efficacy; it was not a newly failed 2026 trial. Wrist-device wellness-product publicity was not classified as medical-device approval or a new treatment result. Neither observation supports a broad claim that all rTMS or all peripheral stimulation fails. [Dated registry interpretation](https://github.com/dotjade/project-neurofreedom/blob/5d91322cfe927e28fdb7d0e1995187e0db53e0a3/updates/2026-10-10-evidence-scan.md), [product classification check](https://github.com/dotjade/project-neurofreedom/blob/5d91322cfe927e28fdb7d0e1995187e0db53e0a3/updates/2026-10-11-evidence-scan.md).

## Next informative work

### Public evidence work that can proceed without new participant data

The aggregate durability calculation above is complete. Use its limitations to specify a clear durability endpoint for future study planning. Keep continued-treatment response, benefit after a time-limited intervention, function and harms separate. Where published quantities are missing, preserve the uncertainty rather than fitting an apparently precise model.

In parallel, complete the already identified adult gating methods/precision check if lawful full text is available. Keep the original Groth denominator and expanded New Tics endpoint extraction as bounded developmental questions; they do not replace the adult priority. Do not repeatedly run the completed cycle benchmark or reopen the closed generic adult dataset search without a new reason.

### A focused existing-data route for sustained adult burden

The next adult real-data decision should be a specific modality-and-permission check for an existing adult registry, with the scientific target deliberately limited to its native follow-up intervals. Calgary's published registration, six-month and twelve-month assessments offer a concrete lead for persistence, impairment, quality of life and treatment course. Pain and participation should be included only if their actual measures are confirmed; they must not be inferred from a tic score. [Calgary report and access statement](https://pmc.ncbi.nlm.nih.gov/articles/PMC11952939/), [expanded Calgary/Paris report](https://pmc.ncbi.nlm.nih.gov/articles/PMC12284832/).

A prespecified analysis could ask how repeated burden and function change among adults with documented sustained severity, while reporting treatment changes and missingness explicitly. It must retain people with continuously severe symptoms rather than requiring quiet-to-peak transitions. This would be observational trajectory research, not proof of a causal antecedent or a treatment effect. No such data access or analysis has yet occurred.

The go/no-go gate is narrow: confirm linked repeated adult records, severity/persistence definitions, actual outcome fields, treatment and missingness information, sufficient follow-up, consent-compatible reuse and secure institutional handling. If those requirements are absent, stop that proposed analysis. Do not interpolate sparse visits into fictitious daily observations.

### Institutional experiment to plan only after those gates

For the durability question, an informative future trial would retain a concurrent credible control through prespecified follow-up, verify masking and treatment exposure, and assess observed tics alongside pain, function, quality of life and harms. Severe persistent adults need an explicit inclusion/analysis plan, without requiring a prior quiet phase. Missing-outcome sensitivity should be planned before results are seen. Any treatment-free assessment or treatment change would require specialist clinical judgment and formal oversight; this is not a home experiment or a suggestion to stop treatment.

## Human help and remaining limits

**No immediate family contribution, personal health data, device purchase or home experiment is needed for the public-evidence work.**

If the project elects to pursue the existing adult records, the essential next help is an authorized institutional investigator and data custodian: confirmation of the exact retained fields and reuse terms, an appropriate secure environment, and any required ethics/data-use review. A defined contact or application would require separate approval before it is made. No clinician outreach, collaboration, access request, recruitment or clinical intervention has been arranged.

This synthesis preserves the scope of the dated work. Some primary extractions remain abstract-only or supplement-limited; correction/retraction and worldwide registry coverage are incomplete. No formal systematic-review completeness, independent clinical peer review or uninterrupted research between runs is claimed. Synthetic validation, published-aggregate arithmetic, metadata feasibility and patient-level clinical evidence remain distinct.

Repository baseline read for this synthesis: [commit 5d91322cfe927e28fdb7d0e1995187e0db53e0a3](https://github.com/dotjade/project-neurofreedom/commit/5d91322cfe927e28fdb7d0e1995187e0db53e0a3), committed 11 October 2026 at 03:15:49 UTC. The weekly aggregate analysis has its own execution metadata, hashed inputs/code, outputs and verification logs in analyses/mns_attrition. No participant records were used.
