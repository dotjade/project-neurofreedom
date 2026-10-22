# Tic-state, longitudinal severity and function are different questions

Project NeuroFreedom | 22 October 2026 | Historical primary-methods audit, not a new clinical result

## Decision

**Do not calculate a responsive-versus-continuous functional effect from Okun et al. 2024.** Its blinded stimulation-state video assessment, longitudinal recalled tic severity and MOS-36 health/function report do not share a verified exposure window, comparator or aggregate analysis population. Function remains an important outcome in its own right, not something established by a tic response.

The MOS-36 narrative reports improvements exceeding ten points in several domains, but changes were not statistically significant after multiple-comparison adjustment. This preserves a potentially useful observation and a negative inferential result. It does **not** establish equivalence, absence of benefit, a clinically meaningful threshold, or a responsive-stimulation-specific effect. The missing aggregate estimator is a limit of this project's analysis, not a finding that the study is invalid. [Primary article, quality-of-life section and Table 6](https://www.nature.com/articles/s41598-024-57071-5).

## Prediction, method and actual finding

The working prediction, recorded after initial article orientation and before detailed extraction, was that these three assessments would not identify one interchangeable estimand. It was not preregistered. A documented common treatment regime, clock, recall window, denominator and paired uncertainty would have weakened this prediction. The [prediction record](prediction.md) defines the stopping rule.

Read README, protocol, status, journal-source instructions, the October 11 resource audit and October 21 crosswalk at commit `c9314ae695c3b5624f5049a3d819fef922ebe14b`. Inspected the named primary report, table headings/notes, official protocol/SAP and server-projected registry metadata. No result classes or participant measurements were requested from the registry. The bounded test found distinct questions, absent aggregate functional precision, and discrepancies requiring historical provenance rather than numerical repair. No patient-data reanalysis, simulation, new clinical-effect estimate or statistical hypothesis test was performed.

## Sources, cohort and scope

- **Okun et al.**, *Responsive deep brain stimulation for the treatment of Tourette syndrome*, published **18 March 2024**, PMID **38499664**, PMCID **PMC10948908**, DOI **10.1038/s41598-024-57071-5**. Ten enrolled adults; mean age 30.1 (SD 8.2) years and disease duration 22.6 (SD 6.9) years. Eligibility included age at least 21, YGTSS tic score above 35/50 and medication-refractory disabling symptoms. This is a selected severe-adult surgical cohort, not a pediatric trajectory study or a sample of all adults with tics. [Publisher](https://www.nature.com/articles/s41598-024-57071-5), [PubMed](https://pubmed.ncbi.nlm.nih.gov/38499664/).
- **NCT02056873**, University of Florida, actual enrollment ten; current registry design is nonrandomized sequential assignment without overall masking. Results and latest update were posted **5 September 2024**, not today. Recorded completion is **24 August 2023**; the article gives **30 June 2023**. Neither date is silently substituted for the other. [Official record](https://clinicaltrials.gov/study/NCT02056873).
- **Official protocol with SAP**, dated **23 September 2019**, uploaded **10 October 2023**. This is later than first enrollment and cannot by itself prove all details were prespecified. It describes severe sustained burden and excludes untreated/unstable psychiatric conditions, limiting applicability to adults with those co-occurring difficulties. [Protocol, pp10-12](https://cdn.clinicaltrials.gov/large-docs/73/NCT02056873/Prot_SAP_000.pdf).
- **Cagle et al. 2022**, PMID **36094652**, DOI **10.1001/jamaneurol.2022.2741**, first online **12 September 2022**, is an earlier four-person embedded-device report from the same trial family, not independent replication. Six were screened/consented, with the first two lacking embedded firmware. The 2024 article cites this earlier report. Do not add its four to the later ten. [Earlier primary report](https://pmc.ncbi.nlm.nih.gov/articles/PMC9468946/).

## Estimand crosswalk

| Question | Measurement and comparison | What the public aggregate record supports |
|---|---|---|
| Current tic expression under a stimulation state | Modified Rush videotape scale, no stimulation versus conventional continuous versus responsive settings; randomized state order and masked participant/psychiatrist in the article | A state-specific video question, not a randomized long-term treatment allocation or a quality-of-life contrast. Actual state duration, carryover and eligible aggregate paired denominator must accompany any effect estimate. |
| Longitudinal tic severity | Preoperative YGTSS versus approximately six months after initial implants; clinical history covers prior weeks | The paper explicitly says this recalled scale could not compare continuous with responsive modes at the six-month primary assessment. It cannot inherit the video contrast's masking or time specificity. |
| Function, pain and broader health | MOS-36 baseline versus six months, with physical/social functioning, role limitation, pain and other domain labels | An uncontrolled longitudinal functional question. No published aggregate paired denominator, mean change with dispersion/CI, or responsive-versus-continuous functional estimator was established. |

[Article methods and outcomes](https://www.nature.com/articles/s41598-024-57071-5). These are operational distinctions, not a ranking that makes functional benefit secondary to visible tics.

### Measure identity, clock and assessment-window clarification

The protocol (p18) defines Modified Rush scoring as five 0-4 categories, total 0-20, and describes YGTSS motor/phonic dimensions separately. The article varies its Modified Rush abbreviation; no explicitly revised YGTSS-R version was verified. Do not treat the video score, 0-25 motor subscore, 0-50 tic total and impairment-inclusive severity as the same measure.

The article refers to a primary-outcome visit with three video conditions. The official protocol instead plans **three separate testing days**, one hour in the day's assigned mode before recording, around month six (pp31-32,38), and 30 days of stable parameters before the primary assessment (p38). Use **primary-outcome-period state contrast**; do not assert that all actual testing occurred within one day or that a one-hour interval proves complete washout. Planned procedures do not prove implementation in every participant. The protocol also separates lead placement from later neurostimulator implantation, while the article anchors six months to initial implants. [Protocol](https://cdn.clinicaltrials.gov/large-docs/73/NCT02056873/Prot_SAP_000.pdf).

The earlier Cagle methods describe YGTSS history over 14 days; the 2024 report uses prior-weeks/prior-settings wording. Neither makes a briefly changed device setting the exclusive exposure over that recall interval. The generic SF-36 description in protocol p19 does not specify version, standard versus acute recall form, scoring algorithm or a study-specific meaningful-change threshold. Do not silently assign a four-week recall window from a generic instrument name. Its schedule (pp23-24) allows assessment discretion; scheduled visits are not outcome-completeness counts. QOLAS is also planned, but this audit found no reported aggregate QOLAS contrast.

## Denominators and contrary documentation

1. The article reports **4/8** chronic-responsive-eligible participants meeting its response definition. Ten enrolled, eight device-capable, actual responsive exposure, and outcome-specific complete pairs are not interchangeable populations. The current registry separately reports eight starting its responsive period and five completing it. That is period flow, not the MOS-36 denominator. [Article](https://www.nature.com/articles/s41598-024-57071-5), [registry projection](registry-projected-metadata.json).
2. The abstract/Results mix **30 points** and **30 percent**, while the Discussion uses at least 30% motor reduction. The standard motor subscale is 0-25; a literal 30-point motor reduction is incompatible with that range. This flags unresolved wording, not authority to repair a criterion or reclassify anyone.
3. The current registry's primary endpoint is **40% reduction in total tic score (0-50) with continuous DBS**, baseline to six months. The 2019 protocol alternates total motor/phonic and motor-only wording across pp7,10,16,33,41-44. The article's 30% motor response is not silently equated to this registered endpoint. Current documents alone do not establish the timing or justification of amendments.
4. Table 3's cited **43.5%, 62.2%, 62.5% and 63.8%** summaries belong to the selected responder presentation, not an all-eight or all-ten effect. They are retained here only to prevent denominator drift, not used as a cohort efficacy estimate.
5. Table 6 is presented as participant-level scores, not an aggregate change/precision table. This project's boundaries prohibit reconstructing its missing denominator, means, covariance or confidence intervals from those rows. The prose and table notes preserve multiplicity-adjusted nonsignificance, but do not supply adjusted p values, test pairing details, correction method or a compatible uncertainty interval. Current registry outcome metadata contains no MOS-36 result endpoint that resolves this gap.

These points identify incompatible or undocumented quantities. No new response fraction, confidence interval, standardized effect, pooled effect or subgroup comparison was calculated.

## Co-occurring outcomes and safety remain visible

The article reports no statistically significant baseline-to-six-month changes on depression, mania, ADHD or obsessive-compulsive scales. These null tests are not equivalence findings, and psychiatric eligibility restrictions limit broader inference. A tic response cannot establish relief of pain, sleep problems, participation restrictions or co-occurring conditions. [Primary secondary-outcome sections](https://www.nature.com/articles/s41598-024-57071-5).

The article records infection-related explantation/reimplantation and a separate lead-repositioning procedure. Its supplement has aggregate adverse-event tables, but a common six-month safety window is not established by the main safety paragraph. The official registry specifies **three years**, systematic assessment and a 1% threshold for other events. Published affected-person totals are serious events **4/10**, other events **10/10**, deaths **0/10** for the continuous-DBS-labeled group; the responsive-labeled group reports **0/5** in each category. These sequential/selected groups can overlap and have different exposure coverage. Do not subtract risks, sum categories, assume all ten completed identical three-year observation, or call 0/5 proof of safety or superiority. [Official registry](https://clinicaltrials.gov/study/NCT02056873), [aggregate-only metadata](registry-projected-metadata.json).

## Uncertainty, access and reuse

This is one bounded source audit, not a systematic review, formal GRADE assessment or clinical peer review. Small selected cohorts, symptom-guided programming, changing hardware, nonrandomized chronic exposure, response selection, incomplete functional aggregates and uncertain carryover limit inference. No natural remission, quiet period or universal course is assumed. No durable disease modification or cure is inferred.

Publisher HTML, the official protocol and supplement were retrieved in memory; no paper/PDF/DOCX copy is retained. The article states CC BY 4.0; this report is a new paraphrased extraction and analysis, not unchanged article text. [License](https://creativecommons.org/licenses/by/4.0/). The publisher table pages were accessible by direct HTTP even though the web reader returned cache errors. The initial extraction route to PMC returned bot-check pages; indexed primary-text excerpts helped verify Cagle's methods and overlap. Independent review used indexed primary Cagle excerpts; direct JAMA PDF access remained unconfirmed. Exact access limits are documented in the linked review. A bounded exact-DOI correction/retraction search and inspected publisher view found no notice; indexed Crossmark labelled it current, but live Crossmark retrieval failed. This is not a guarantee of exhaustive correction surveillance.

A targeted search unexpectedly displayed participant rows, and an initial supplement parser displayed case narratives outside its tables. Neither was copied into artifacts, used for extraction, reconstructed, pooled or analyzed. Subsequent extraction was restricted to article narrative aggregate statements, headings/notes and projected official metadata. No participant file, raw signal, private story or unlicensed full text is published. No contact, access request, treatment change or participant collection occurred.

## Stopping rule and next bounded decision

Close this functional-effect calculation attempt unless public aggregate documentation supplies the MOS/SF-36 version and recall window, treatment exposure over that window, outcome-specific paired denominator/missingness rule, aggregate change with uncertainty, and a defined comparable treatment contrast. This is a request for documented prerequisites, not investigator outreach or individual data.

The distinct next task is a **bounded official historical-registration audit of NCT02056873**: locate dated outcome/design versions and public protocol amendments to determine when 40% total-tic, motor-only and responsive criteria and follow-up windows appeared. Keep paper wording discrepancies separate from actual registered changes. Inspect metadata/documents only, not result measurement rows. If historical official versions cannot be lawfully retrieved, record that exact provenance gap and stop; do not infer selective reporting, revise published responder counts, reopen generic cohort searches or repeat this fixed functional audit.

## Reproduction

`python check_extraction.py` validates the saved aggregate metadata and separation rules against `structured-extraction.json`. `python collect_registry_metadata.py` performs an optional new server-projected registry retrieval; later results may differ and must be dated separately. Checks are documentation/boundary checks, not scientific replication. Source URLs, retrieval hashes and limits are in `source-retrieval.json` and `provenance.json`.

### Independent verification

The [separate source/inference review](review/independent_review.md) checked the report and independently confirmed protocol timing and a fresh registry flow/safety projection. Its [narrow registry record](review/registry-independent-check.json) preserves only group-level metadata. The [draft review record](review/draft-review.json) identifies the reviewed bytes and any final access-wording check. The 25 offline checks in [checks.json](checks.json) passed. Neither independent source checking nor these software checks constitute clinical peer review or an efficacy replication.
