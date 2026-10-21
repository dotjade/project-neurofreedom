# NCT05371041: aggregate-only endpoint, timing and safety crosswalk

21 October 2026 | Historical trial results, not a newly posted treatment result

## Decision

**Stop without an efficacy calculation.** The public definitions do not establish a compatible baseline-to-endpoint clinical estimator. Baseline metadata describes a 0–100 YGTSS score including impairment; the primary endpoint describes the 0–50 total tic score. Both report eight participants, but a shared denominator does not make these constructs interchangeable. The protocol's postoperative calendar and the registry's “after initiation of DBS” calendar also remain unreconciled. These are limits on this project's computation, **not a finding of author error, an invalid study, or absence of treatment benefit**.

A useful additional distinction emerged: the protocol specifies early recording months relative to **pulse-generator implantation**, after lead implantation; the safety registry window instead explicitly refers to **lead surgery**. Do not silently collapse surgery, generator placement and stimulation activation into one date.

## Prediction, method and actual result

The working prediction was that the named protocol, statistical analysis plan (SAP) and posted-result definitions would either identify one consistent outcome/clock with a usable published aggregate estimator, or expose a precise missing prerequisite. This was a bounded documentation test, not a preregistered clinical analysis. A verified common score, time origin, eligible denominator and aggregate change/response summary would have weakened the stopping decision.

Read the current project README, research protocol, latest status, October 20 CM–aGPi report and its evidence/registry metadata, plus the relevant evidence-ledger entry. The public repository snapshot supplied for local review was `81feefe52fa1a401b01fd51ee8950a5e4de4a9ae`. Inspected the official 27-page protocol and two-page SAP in memory. Retrieved **server-projected** ClinicalTrials.gov fields, excluding every outcome/baseline result class and measurement row. Exact projection fields, retrieval time and response hash are retained in `registry-projected-metadata.json`; the retrieval script rejects unexpected measurement payloads before saving. No patient-level statistic, efficacy estimate, responder proportion, confidence interval or simulation was calculated.

The test resolved denominators and planned assessments, but not a compatible estimator or common time origin. Search coverage was confined to this trial and linked primary reports; it was not a systematic review. Exact queries, source access and the unexpected search-result exposure described below are logged separately.

## Source identities and dates

- **Official registry:** NCT05371041, IRB202102161, University of Florida; single-group, unmasked, device-feasibility design; actual enrollment eight. Current status is active, not recruiting. Primary completion is recorded as 1 May 2026 (actual), overall completion as 31 August 2027 (estimated). Results and latest update were first posted 25 September 2026; fresh metadata were retrieved 21 October 2026 at 02:51:59 UTC. These are distinct dates, not evidence of eight completed two-year safety observations. [Official registry/API](https://clinicaltrials.gov/api/v2/studies/NCT05371041).
- **Protocol:** `Prot_000.pdf`, version approval/PI date 12 May 2025; header also identifies IRB version 7 September 2023. Uploaded 24 September 2026 at 11:52 (registry timestamp; timezone not stated). This is a later protocol version, not proof that every detail preceded enrollment. [Protocol](https://cdn.clinicaltrials.gov/large-docs/41/NCT05371041/Prot_000.pdf).
- **SAP:** `SAP_001.pdf`, cover version approval date 20 December 2021; uploaded 24 September 2026 at 11:52. The second page includes a manuscript-specific analysis paragraph. The cover date alone does not establish when that paragraph was added or prospectively specified. [SAP](https://cdn.clinicaltrials.gov/large-docs/41/NCT05371041/SAP_001.pdf).

## Endpoint and denominator crosswalk

| Item | Source definition | Resolution for this audit |
|---|---|---|
| Baseline construct | Registry `baselineCharacteristicsModule.measures`: YGTSS out of 100, comprising motor 0–25, vocal 0–25 and impairment 0–50 | Total including impairment; not the 0–50 tic-only endpoint |
| Primary endpoint construct | Registry protocol and results outcome metadata: YGTSS Total Tic Score; motor plus phonic scores 0–50; clinician rating of prior week | Clearly described as tic-only, but no permitted common-construct baseline aggregate is supplied |
| Baseline denominator | Registry baseline module: eight participants | Module-level count; no separate YGTSS-specific denominator is returned |
| Endpoint denominator | Registry outcome denominator eight; population description says eight enrolled/eight analyzed | Aggregate coverage is eight, not a reconstructed paired change dataset |
| Flow | Registry overall period: eight started, eight completed, zero not completed | Does not independently prove completion of every later safety visit |
| Protocol success criterion | Protocol pp.4, 8: individual improvement greater than 30%; p.8 gives a target of four of eight responders | A planned benchmark, not an observed responder result |
| Protocol scale specificity | Protocol p.13 describes motor/phonic dimensions; p.8 separately invokes a motor-scale criterion for a post-primary-treatment option | Do not infer that unspecified “YGTSS” always means the same composite or subscale |
| Posted representation | Outcome parameter type is `NUMBER`, unit scores on a scale; no aggregate analysis or dispersion object is returned by the explicit projection | Not an established mean/median change, paired uncertainty estimate or aggregate responder count |

Definitions and counts above come from the [official projected registry record](https://clinicaltrials.gov/api/v2/studies/NCT05371041); protocol criteria come from [pp.4, 8 and 13](https://cdn.clinicaltrials.gov/large-docs/41/NCT05371041/Prot_000.pdf). The baseline description itself says participant-specific scores are listed. Those rows are outside this project’s scope. We did not infer a correction from individual values, subtract impairment from anyone's score, reconstruct baseline/endpoint pairs, or average the rows.

The latest protocol's criterion also cannot be substituted for a published aggregate response count. The primary registry outcome is a score at one time point; the accompanying group narrative discusses responder classification, but narrative intent is not the missing aggregate estimator.

## Timing crosswalk

1. **Preoperative comparator:** protocol p.8 compares the on-responsive-stimulation assessment with a preoperative baseline. Its p.22 footnote says a separate baseline visit occurs only if screening assessments were more than 45 days before surgery. Thus “baseline” need not be an identically timed extra visit for everyone. The posted baseline metadata does not identify which rule supplied each observation, and no individual reconstruction is attempted.
2. **Two surgical stages:** p.6 allows lead placement in one or two surgeries, then generator placement approximately one month after all four leads. It expressly anchors the first three physiology months to **IPG implantation**. Pages 4–5 use the broader postoperative/implantation wording.
3. **Planned therapy and endpoint:** pp.5, 7–8 place programming/optimization in months 4–9, the primary assessment at day 270/month nine (±14 days), and require approximately 30 days of unchanged stimulation settings before assessment. Outcomes may be collected over two to three outpatient days. This is not nine months of therapeutic stimulation by default.
4. **Posted-result clock:** outcome/flow group descriptions say data were captured nine months after DBS initiation. They do not define whether “initiation” means surgery, generator placement or therapy activation. That wording therefore cannot be declared equivalent to the protocol clock or converted into an exact alternative postoperative month.
5. **Delivered intervention:** p.7 permits temporary open-loop settings if an appropriate control signal has not been identified. A responsive-stimulation plan is not documentation that every participant received an identical closed-loop exposure at the endpoint.

These distinctions are source-based, not proposed adjustments to the observations. The [protocol pp.4–8, 22](https://cdn.clinicaltrials.gov/large-docs/41/NCT05371041/Prot_000.pdf) and [registry group descriptions](https://clinicaltrials.gov/api/v2/studies/NCT05371041) do not provide the public aggregate clarification needed to reconcile them.

## What the SAP does and does not establish

The SAP p.2 describes an early feasibility study, chiefly assessing safe/tolerable delivery with initial efficacy testing rather than a pivotal comparison. Its general plan uses descriptive summaries across visits and primarily individual analyses. A separate manuscript paragraph names paired Wilcoxon signed-rank tests for baseline/month-nine group changes, median changes, Spearman associations with secondary outcomes and FDR adjustment for correlation p values. [SAP, p.2](https://cdn.clinicaltrials.gov/large-docs/41/NCT05371041/SAP_001.pdf).

Those test names supply neither the missing numerical aggregate estimator nor a clarified score/time origin. They do not provide a full missing-data rule, paired-change dispersion or an estimand distinguishing open-loop and closed-loop exposure. No manuscript is identified by that paragraph. We therefore cannot verify its temporal provenance or treat it as a complete prospectively specified analysis of the posted endpoint. This is an uncertainty judgment, not a claim of retrospective alteration.

## Safety: preserve the window and ascertainment

The registry gives an adverse-event interval from enrollment through follow-up, approximately two years after **lead implantation**, with non-systematic assessment and a zero-percent reporting threshold for other events. Published whole-cohort counts are **3/8 affected by serious events, 8/8 by other events, and 0/8 deaths**. These categories may overlap; they are not summed. No event narrative or participant-specific safety record was extracted. [Official adverse-event module](https://clinicaltrials.gov/api/v2/studies/NCT05371041).

The protocol p.21 schedules an adverse-event log throughout the study; p.23 describes investigator monitoring, seriousness/severity and relationship assessments, and DSMB review. This planned monitoring does not override the posted **non-systematic** ascertainment label. Nor does the group title “9 Month Primary Outcome” shorten the adverse-event module's separately stated window. [Protocol, pp.21, 23](https://cdn.clinicaltrials.gov/large-docs/41/NCT05371041/Prot_000.pdf).

These are reported affected-person totals, not device-attributable risks or incidence rates. Observation-time distribution and a common completed two-year risk period are not established. Do not merge this eight-person window with the earlier six-person physiology publication's shorter postoperative safety statement, or interpret differing counts as a contradiction without aligned populations and intervals. The October 20 audit already preserves that distinction; it was not reanalysed here.

## Missing prerequisites and stopping rule

Reopen this fixed crosswalk only if a public correction or new aggregate documentation supplies:

- an explicit common baseline/endpoint YGTSS construct and any needed corrected labels;
- an operational time zero distinguishing lead surgery, IPG placement and stimulation activation, with the actual aggregate assessment window;
- the analyzed population and missingness rules for that estimand, plus an already published aggregate paired change/uncertainty or responder numerator and denominator;
- intervention-state accounting if a closed-loop-specific interpretation is intended; and safety observation coverage if a fixed-period risk is intended.

These prerequisites can be satisfied by public aggregate clarification; they are **not a request for participant rows or investigator contact**. The bounded task is closed, with clinical effects left uncalculated. The result neither establishes nor rules out efficacy, functional benefit, disease modification or cure.

### Distinct next bounded question

Next audit the already named **Okun et al. 2024 report (PMID 38499664; PMC10948908; NCT02056873)**: do its blinded within-visit stimulation-state comparisons, longitudinal baseline comparisons and MOS-36 functional outcomes support the same estimand? Verify outcome versions, recall/assessment windows, eligible aggregate denominators, uncertainty and safety timing, without substituting tic improvement for functional benefit. The October 11 audit addressed resource/access feasibility, not this detailed clinical/function question; the research portfolio shows no completed audit of that exact contrast. Preserve overlap with Cagle 2022 rather than count a second independent cohort. Inspect lawful primary methods and aggregate tables only; if they do not establish a compatible functional contrast, record that prerequisite and stop without reconstructing individuals. [Named primary report](https://pmc.ncbi.nlm.nih.gov/articles/PMC10948908/).

## Access and privacy accounting

Both official PDFs were fetched and parsed in memory; only their identifiers, hashes and original factual summaries are retained, not PDF copies or full text. The web reader could not open those PDFs; direct official HTTP retrieval succeeded. All retained registry material was fetched using field projection, with result classes excluded at the server.

An initial broad exact-trial web search unexpectedly displayed participant rows from a third-party registry mirror. They were not copied into files, used to resolve discrepancies, reconstructed, pooled or analyzed. Subsequent searches were restricted to primary-source domains and official field-projected retrieval. This limitation is disclosed rather than claiming that no row was ever displayed. No participant data were requested from investigators; no outreach, clinical intervention or repository mutation occurred in this analysis.
