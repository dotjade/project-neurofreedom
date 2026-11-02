# CANNA-TICS: documentation, missingness and the endpoint hierarchy

2 November 2026. **Historical primary-source reconciliation, not a new trial, simulation, patient-data reanalysis or treatment recommendation.**

## Question and prediction

The [prospective local plan](plan.md), SHA-256 `afc402787a2949fc03451205cb0b5bd210d4c92d00827511d2c8e14586ab1d5e`, asked whether public supplementary aggregates and dated scoring/endpoint documentation resolve the functional uncertainty identified [on November 1](../../canna_function/2026-11-01/report.md). It preceded supplement extraction, but was not externally preregistered.

Prediction: tic response alone cannot settle function, and missingness assumptions may matter. Disconfirming documentation would provide observed functional denominators, explicit scoring, reconciled VAS output, sensitivity estimates with uncertainty and dated pre-unblinding plans. This is a documentation/access test, not a biological falsification test.

## Method and actual results

We compared the peer-reviewed [2020 protocol](https://doi.org/10.3389/fpsyt.2020.575826), [2023 primary randomized report](https://doi.org/10.1016/j.psychres.2023.115135), official [EU protocol record](https://www.clinicaltrialsregister.eu/ctr-search/trial/2016-000564-42/DE), prior verified aggregate extraction and a newly located [institutional attachment record](https://freidok.uni-freiburg.de/data/234831). DOI, PMID 36878177, NCT03087201 and EudraCT 2016-000564-42 identify the same trial, not independent replications. [Original extraction](extraction.json) records source-level answers and limitations.

### What the documents resolve

The protocol names GTS-QoL and SF-12, so direct function was not simply inferred from tic scores after the fact. It specifies ANCOVA **and** an additional longitudinal AR(1) mixed model. Its no-imputation statement applies to that mixed model; it does not prohibit imputation for every analysis. Secondary analyses are exploratory. Driving noninferiority is hierarchically gated on primary superiority, with a minus 32 percentage-point margin. This matters when auditing the later driving paper: an exploratory result must not be promoted to confirmatory evidence when the preceding test did not establish superiority.

The registry lists GTS-QoL/SF-12 assessments after four and nine stable-treatment weeks and one month afterward. These are planned timepoints, not proof of complete observations or treatment-free durability. Protocol publication on November 26, 2020 follows the registered trial end on November 20. Publication date alone therefore cannot prove original pre-enrollment specification. A current registry text's early first-entry date likewise does not timestamp each later field.

### What remains unresolved

The primary report describes baseline-mean imputation and LOCF, with sensitivity analyses. It asserts compatible findings for impairment and QoL-VAS, among other endpoints. We preserve that assertion as counterevidence to a blanket claim of instability, but cannot independently evaluate its numerical robustness without the actual aggregate sensitivity table. The report describes a November 2017 driving amendment before enrollment and blinded-review changes to response threshold, center adjustment and per-protocol definition. This is not evidence of outcome-driven misconduct. Exact dated SAP/amendment files and scoring details remain unverified.

No endpoint-specific observed function denominators, corrected VAS contrast or trial-specific coding reconciliation were verified. Overall trial completion is not questionnaire completeness. We did not substitute unknown denominators or infer unavailable covariance, missing outcomes or sensitivity intervals.

### A readable attachment is not necessarily the right document

The institutional record labels a PDF as the article's supplement. Its bytes match the listed SHA-256 `52acf06222b9ad150e2f7c8a821f30b38893f61a6eb728407c06e65e9082e50b`, but the actual 18-page content concerns phosphorus removal by photogranules, not this trial. Two independent downloads and first-page visual inspections confirmed the content-identity mismatch. The PDF and temporary renders were not retained or published. This is a specific repository-attachment mismatch, not an HTTP broken link, a claim about the authors' intended supplement, or evidence of misconduct. A matching checksum proves byte identity, not scientific relevance.

The publisher article route returned HTTP 403; indexed excerpts were available. We did not bypass the restriction. A lawful National Library primary PDF was read transiently. No participant rows or individual narratives were used.

## Decision, uncertainty and next step

The documentation concern is **partly resolved**: function measures, exploratory status and the driving hierarchy are documented. The numerical missingness/scoring concern is **unresolved**, not disproved. The November 1 null-compatible functional estimates remain unchanged; neither established superiority nor no benefit is warranted. Adult inclusion does not establish applicability to older adults, chronic vocal-only disorders, or separately analyzed persistent-severe symptoms and excluded comorbidities. Pain, participation, harms and co-occurring conditions remain distinct priorities.

The planned quantitative sensitivity comparison was **not feasible**. Exact prerequisites are a genuine lawful aggregate Supplementary Table 4 (methods and arm contrasts/intervals), endpoint-specific observed counts, VAS coding/correction and dated analysis-plan history. No simulation was substituted. No numerical effect computation or RNG/seed was used today. Independent source checks are verification, not a new clinical result.

Close this bounded supplement search until a corrected or independently lawful aggregate source becomes available. Next audit the already identified same-trial [driving report](https://doi.org/10.1089/can.2023.0114), explicitly checking the hierarchy, noninferiority margin, analyzed population, missingness and direct functional harms. It is not independent replication or individual driving clearance. Public aggregate literature work needs no owner action; participant research, clinical advice and custodian contact remain outside authorization.
