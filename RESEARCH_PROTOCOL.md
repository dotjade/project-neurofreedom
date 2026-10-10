# Project NeuroFreedom research protocol

Version 0.1 | 8 October 2026

## Purpose and boundaries

Build a traceable research program toward safe, durable disease modification and ultimately a validated cure for Tourette syndrome. This initial research portfolio is a targeted evidence map, not an exhaustive systematic review, a clinical protocol, a proven treatment, or evidence that a cure has been discovered. Current evidence cannot promise a cure or a date for one.

The repository contains public scientific evidence, original summaries, explicit hypotheses and reproducible research plans only. It must not contain individual medical records, symptom diaries, names or identifiers of children, family histories, videos, genetic data, credentials or private community posts. Do not upload patient information even to a private repository. Repository privacy does not replace consent, clinical governance or data protection.

Use primary research to test claims. Treat guidance as guidance, observational associations as associations, and animal/cell findings as preclinical. Social posts can identify unanswered questions, burden and usability problems; they cannot establish efficacy or causation. No outreach, enrolment, data-access application, account creation beyond the requested repository, purchases or medical intervention is included in a literature-research authorization.

## Scope clarification — 10 October 2026

Cover Tourette syndrome and chronic tic disorders globally across ages and severities. Persistent severe adult symptoms, pain, social and functional burden, co-occurring conditions, unmet treatment needs and durable treatment response are central research priorities. Do not frame the mission around one trajectory or assume quiet periods, developmental improvement or remission for everyone. Preserve waxing/waning and remission research as subquestions while deliberately seeking adult persistence and negative-treatment evidence. Label pediatric-to-adult extrapolation and cohort exclusions explicitly. A transition-only design must not erase people with sustained severe burden.

## Core definitions

- Symptom response: a prespecified clinically meaningful improvement on validated measures during a stated period.
- Functional benefit: improvement in comfort, participation, sleep, school/work or quality of life, even if tics remain.
- Remission: a stated symptom threshold maintained over a stated interval, with ascertainment method and treatment status disclosed. Self-report and blinded observation are separate measures.
- Durable benefit: improvement persists at repeated follow-up; this alone does not prove alteration of underlying disease biology.
- Disease modification: evidence that an intervention changes the underlying course beyond natural history, measurement effects and transient suppression.
- Cure: a high evidentiary standard for lasting resolution without unacceptable harm or continuing tic-suppressing treatment; an operational research definition must be agreed by patients and clinical experts before testing. No existing intervention in this portfolio is labelled a cure.

## Search and updating method

For each search, record date/time, database, exact query, date limits, filters, results screened, inclusions, exclusion reasons and coverage limits. Suggested starting sources: PubMed, ClinicalTrials.gov, WHO ICTRP, relevant primary journals, official guidelines and investigator/consortium pages. Confirm trial status in the registry before describing recruitment. Search evidence through the actual run date; never infer a future trial result from an expected completion date.

Starting query families:

1. (Tourette OR tic disorder) AND (longitudinal OR remission OR persistence OR natural history)
2. (Tourette OR tic disorder) AND (sleep OR polysomnography OR REM OR arousal)
3. (Tourette OR tic disorder) AND (randomized OR sham OR placebo OR controlled trial)
4. (Tourette OR tic disorder) AND (genome OR exome OR interneuron OR striatum OR dopamine OR histamine OR GABA OR acetylcholine)
5. (Tourette OR tic disorder) AND (connectivity OR EEG OR biomarker OR prediction OR machine learning)
6. (Tourette OR tic disorder) AND (adverse event OR withdrawal OR negative trial OR replication)

Deduplicate by DOI/PMID/NCT identifier, then title and cohort. Distinguish multiple reports of one trial or overlapping cohort. Record full-text availability. Abstract-only evidence is labelled as such. Save source URLs and original paraphrased extraction, not unlicensed copies of papers. Store licensed full text only after checking reuse rights. Search negative findings and contradictory results deliberately.

PRISMA 2020 provides a reporting framework for a future systematic review. This first pass does not claim PRISMA-compliant completion. Source: https://www.prisma-statement.org/prisma-2020-statement

## Evidence record schema

Each record should carry: stable ID; title; authors/year; source URL; DOI/PMID/NCT; study type; population/age; sample and analysis counts; comparator; intervention/exposure; prespecified outcomes; follow-up; numeric results and uncertainty if available; adverse events; attrition; risk-of-bias concerns; conflicts/funding; applicability; related cohort IDs; claim supported; claim not supported; full-text/abstract status; extraction date; reviewer; correction/retraction check; next verification task.

For body-of-evidence judgements assess risk of bias, inconsistency, indirectness, imprecision and publication bias. Do not relabel an informal confidence score as a formal GRADE assessment. Mechanistic plausibility and clinical efficacy require separate judgements. Source: https://www.gradeworkinggroup.org/docs/Criteria_for_using_GRADE_2016-04-05.pdf

## Hypothesis lifecycle

A hypothesis starts as proposed. Specify predicted direction, population, measurable outcome, confounders, negative controls, data access and a result that would weaken or falsify it. Record analysis code/version when actually executed. Promote only after independent evidence or replication; retain rejected hypotheses and why they failed. Do not treat twenty generated hypotheses as twenty discoveries, or label a hypothesis novel without a dedicated prior-art search.

For computational work, split data by participant, family and site as appropriate; avoid repeated measurements leaking across train/test sets. Separate feature selection from final held-out evaluation. Report calibration, uncertainty, missingness, subgroup performance and domain shift. Compare with simple baselines. Retrospective predictive accuracy is not proof of treatment benefit.

## Operating cycle

The four research schedules were enabled on 8 October 2026 after user approval. See STATUS.md for start dates and flexible timing. Setup success is not evidence that a future run has already executed.

- Daily: search new publications, trial updates and consequential safety findings; then advance one bounded question through counterevidence review, structured extraction, reanalysis or a small reproducible synthetic/permitted-public-data computation. Log the prediction, method, actual finding, uncertainty and next decision. If blocked, identify the missing prerequisite. Do not invent a result or repeatedly redo completed work.
- Weekly: synthesize new evidence and complete or verify one feasible bounded analysis, preserving code, inputs, random seeds, outputs, negative results and independent checks. Propose the next informative experiment with its clinical/ethics/data-access dependencies. Report what was tested, learned, rejected and what help is needed, rather than merely listing new papers.
- Monthly: reassess the hypothesis portfolio, failed predictions, computational progress, feasible collaboration routes and resources needed.
- Quarterly: revisit strategy, target pathways and adjacent-field developments; produce a versioned progress report including negative findings and unmet dependencies.

A run must report inability to access a required source or update the repository rather than pretending work was saved. Never claim uninterrupted research between runs. Separate literature updates from clinician decisions and patient observations.

## Initial analysis priority (historical; broadened scope above applies)

Operationalize remission before searching for a switch. Extract how longitudinal studies defined tic absence, how long it lasted, who rated it, whether observers were blinded, medication status and quality-of-life change. Determine whether plausible mechanistic signals predict trajectory after adjusting for age, baseline severity, ascertainment and attrition. This is tractable evidence work that can proceed without collecting any new patient data.

## Active discovery execution update on 8 October 2026

The daily and weekly schedules were successfully updated to require hypothesis testing or feasible analyses, not collection alone. Existing schedules remain unchanged. Research runs use available compute; no paid resources, external-agent connections, public release or clinical intervention are authorized by this execution plan. Synthetic methods tests must be labelled explicitly and cannot establish an individual biological mechanism. An open collaboration project remains a proposal pending a reviewed publication scope and appropriate governance.
