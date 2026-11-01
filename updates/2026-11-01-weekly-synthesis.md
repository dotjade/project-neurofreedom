# Project NeuroFreedom weekly synthesis

1 November 2026 | Fourth weekly synthesis | Work reviewed: October 26 to November 1

Prepared against public repository baseline `3bba0b5cdffed63f1df8e635ca0077bdafe88a84`. This is a synthesis of the verified daily work, the October 28 requested causal investigation and a new bounded historical trial audit. It is not another global scan or the separately scheduled monthly portfolio review. Scope remains Tourette and chronic tic disorders across ages and severities, including persistent severe adult symptoms, pain, participation, co-occurring conditions and unmet treatment needs. Developmental improvement is not assumed for everyone.

## What the week actually changed

### Measurement claims now have sharper boundaries

The original 2018 YGTSS study included 101 adults among 617 participants, but its pooled total-tic alpha .82 does not supply adult-specific, ASD/communication-group, interrater or retest validation. The independent pediatric EMTICS study reports alpha .87 alongside omega .58 and marginal factorial fit. These are different coefficients and models, not evidence that reliability deteriorated over time. The negative factor diagnostics coexist with useful convergence; neither universal validity nor wholesale scale rejection is warranted. Tic-attributed impairment remains distinct from total tic severity and broader lived burden. [2018 audit](../analyses/ygtss_validation/2026-10-26/report.md), [EMTICS audit](../analyses/emtics_validation/2026-10-27/report.md).

Ho's parent/clinician comparison has useful discrimination and appropriate clustering, but 1,455 paired assessments belong to 527 people. Its 196 disagreements are assessments, not distinct patients. Masking of scores is a strength, not proof of independent symptom information. Decreasing differences with repeated visits do not establish causal practice effects, a four-visit prescription or interchangeable continuous scores. Pediatric proxy results do not validate adult self-report. [Informant audit](../analyses/informant_agreement/2026-10-28/report.md).

### Biological leads remain leads, not targets or forecasts

Wang's September genetics paper was newly retrieved, not newly published this week. The 36-gene union partitions into 3 meeting both diagnosis-specific high-confidence thresholds, 7 CTD-not-OCD, 9 OCD-not-CTD and 17 combined-only. These are threshold memberships, not evidence of biological exclusivity or 36 treatment targets. CELSR3 and WWC1 are only probable in the retained combined analysis, while other analyses differ. Sample reuse prevents counting every report as independent replication; network convergence in one database did not reproduce in another. [Gene-specific audit](../analyses/gene_specificity/2026-10-29/report.md).

The October 28 causal synthesis distinguishes enduring susceptibility, immediate tic initiation and a place where expression can be interrupted. It proposes input/control timing, heterogeneous routes to a shared state and event probability versus form as testable questions. Existing prior art and negative correlations prevent novelty or validated mechanism claims. Its explicitly synthetic counterexample demonstrates non-identification, not any patient's biology. Aligned lawful human evidence remains unavailable; a positive toy model cannot fill that gap. [Causal synthesis](../analyses/causal_synthesis/2026-10-28/report.md).

The adult sensory-attenuation paper, PMID 42947547, DOI 10.1002/mds.70590, is dated October 28 and compares 30 adults with TS with 30 controls. Its direct-condition finding and current-severity association are worth retaining alongside the indirect-condition null. Abstract-only access does not supply a verified formal interaction, precision or prospective prediction. An inaccessible methods contrast is not a negative result, and different sensory-gating experiments are not interchangeable replications. [Daily extraction](2026-10-29/report.md), [contrast audit](../analyses/sensory_contrast/2026-10-30/report.md).

Historical force-model work shows why a constant offset need not identify subtractive physiology and why an unlabeled multiplicative factor need not identify a biological cause. The following aggregate reliability audit found that changing the extraction window changes the direct-minus-slider contrast by 0.12 N. Split-half .94/.86 is not repeat-session or difference-score reliability; a pooled trial-order null is not a condition-specific learning test. The null remains counterevidence against a large common monotonic trend, not something to discard. [Model audit](../analyses/force_matching/2026-10-31/report.md), [reliability audit](../analyses/force_matching_reliability/2026-11-01/report.md).

**Decision:** close these fixed marker and measurement audits pending their exact lawful aggregate prerequisites. Do not keep producing synthetic demonstrations of the same missing clinical bridge. This weekly run independently reproduces the 0.12-N arithmetic without importing the earlier implementation, explicitly as verification rather than a new discovery. [Code](2026-11-01-weekly/verify_daily.py), [eight checks and output](2026-11-01-weekly/daily-verification.json).

## New weekly investigation: return to randomized adult function

The new [CANNA-TICS audit](../analyses/canna_function/2026-11-01/report.md) asks whether direct quality-of-life/function outcomes identify randomized benefit independently of the trial's tic-response result. Its dated local plan precedes extraction and computation; it is not a prospectively registered clinical study. The historical primary trial is PMID 36878177, DOI 10.1016/j.psychres.2023.115135; official results are EudraCT 2016-000564-42 / NCT03087201. No participant files were accessed.

The treated analysis includes 97 of 98 randomized people. The primary response counts were 14/64 versus 3/33; the prespecified stratified superiority test did not establish superiority. Our separately labelled unadjusted risk difference is +12.784 percentage points, with a Wilson/Newcombe 95% interval from −3.944 to +25.784 points. This is not a reconstruction of the published model.

Importantly, direct functional comparisons do exist, rather than all function claims being inferred from tic change. Yet all five focal intervals include zero: normalized GTS-QoL −4.13 [−8.65,0.39], life-satisfaction VAS +5.55 [−0.69,11.80], tic-attributed impairment −4.12 [−8.45,0.22], SF-12 physical +0.69 [−2.24,3.63] and mental +2.12 [−1.39,5.64]. They are exploratory and imputation-dependent, not proof of functional superiority, equivalence or no worthwhile benefit.

The VAS arm least-squares means do not subtract to the reported contrast; visual primary-table review confirms the discrepancy, with no correction invented. Four other rows reconcile. Adverse events occurred in 61/64 versus 26/33, while event totals are not people; ascertainment, exclusions and reporting limits remain explicit. Ten implementation tests and 29 independent numerical checks passed. No participant records, clinical threshold, pooled efficacy estimate or severe-adult subgroup effect was reconstructed.

## Retire unsupported inferences, not untested biology

Retire these uses of the reviewed evidence: high alpha means every kind of reliability or subgroup validity; correlation/discrimination makes scores interchangeable; trial repetition demonstrates learning causally; a gene passing a threshold is an exclusive or reversible treatment target; a significant direct condition plus a nonsignificant indirect condition proves their difference; current severity predicts future tics; a fitted force model uniquely identifies physiology; split-half reliability validates change between sessions; symptom response alone demonstrates functional benefit.

Retain the underlying positive observations, useful clinical scales, negative findings and uncertainty. No proposed timing mechanism is biologically falsified by missing methods. Neither symptomatic response nor a null-compatible functional estimate settles disease modification or cure. This weekly report does not rerank the full twenty-hypothesis portfolio or claim the separate monthly review occurred.

## Surveillance and evidence coverage

The week's verified daily scans distinguish older retrievals from new first publications. Older preclinical botanical/immune experiments do not establish human safety, mediation or efficacy. The small mixed-diagnosis postmortem HRH3 pilot has weak/corrected negative evidence, not a Tourette-specific target. GP-TiCS qualitative themes document unmet care and communication needs without providing prevalence or proven benefit of a future educational resource; no interview narratives are retained. Pediatric immune/vitamin correlations retain their multiple-testing nulls and do not justify supplementation. Repeated records and reviews are not independent studies.

No newly posted relevant clinical-trial result or qualifying new preprint was verified by the daily records through their stated cutoffs. New NCT07905898 is an adolescent feasibility protocol without results; enrollment metadata 95 versus narrative 85 and 60 randomized remain unreconciled. Other changing dates/availability are metadata, not efficacy or a causal safety signal. This bounded surveillance does not establish that nothing new exists worldwide.

One November 1 official HSA notice concerns tetrabenazine product/batch DNG1035A, recalled October 27 at retail level after black spots were observed. This is a specific quality recall, not a class-wide hazard or an individual medical conclusion. The separate EMA Deanxit combination review remains ongoing and excludes flupentixol monotherapy; communication and initiation dates are distinguished. [November 1 safety report](2026-11-01/safety/report.md), [October 31 safety report](2026-10-31/safety/report.md).

WHO query exports, CTIS parsing, some regulator attachments, non-English/global coverage and several full methods/supplements remain incomplete. Bot blocks are access limitations, not demonstrated broken links. The weekly run reuses daily surveillance rather than claiming a fresh search of every source or end-of-day coverage.

## Next informative safe experiment and dependencies

First inspect the trial's safely separated public aggregate supplementary functional sensitivity results and dated protocol/SAP documentation. Ask whether the direct functional contrasts remain compatible across declared missingness analyses, and whether endpoint timing, score coding and observed counts are explicit. Disconfirm concern with documented compatible between-arm sensitivity estimates and clarified scoring, not merely a similar p-value. A stable result across models does not validate their missingness assumptions. Stop at absent aggregate output rather than request patient rows or contact authors.

If that fixed documentation gap closes or remains inaccessible, the same-trial fitness-to-drive report (PMID 38265476, DOI 10.1089/can.2023.0114) is a distinct direct-function candidate. Verify its selected denominator, comparator and any prespecified margin before analysis. It is not independent replication, evidence that driving is safe for an individual, or a permission to conduct driving tests.

**Help needed from the owner: none for the next public-evidence step.** Do not supply medical histories, begin home monitoring, change treatment, buy tests or contact researchers for this task. Any future human experiment requires qualified clinical/institutional ownership, a suitable comparator and safety plan, lawful data governance, ethics/consent and separate authorization. Those dependencies cannot be solved with more simulations.

## Reproducibility, publication and public scope

The [source manifest](2026-11-01-weekly/source-manifest.json) pins required repository inputs. New analysis inputs, code, deterministic outputs, source-access limits and independent checks accompany the bounded report. Software/document checks are not clinical peer review. No individual/family records, identifiable community content, source full text, secrets, paid compute, outreach or intervention were used.

The repository has been public since the authorized October 13 release; stale private wording in the schedule does not change visibility or relax privacy. The already verified November 1 homepage feed, six approved optional activities and disabled collection are unchanged. No second homepage update, new rendered test or continuous execution is claimed. Exact remote commit/readback verification is recorded separately after publication.
