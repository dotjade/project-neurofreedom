# Independent review: Taylor, Anderson and Davies 2022

18 October 2026 | Historical primary-source and aggregate-reporting audit

## Decision

The paper supports direct measurement of pain interference in a pain-selected, adult-dominant mixed-age sample. It cannot supply representative pain prevalence, an age-18-plus interference estimate, a persistently severe-adult estimate, a causal pain-management effect, or an established tic-pain feedback mechanism. Retain the descriptive burden evidence while closing this source pass at the missing quantities below.

## Scope and source verification

Read the current NeuroFreedom protocol, STATUS through its 17 October entry, the 17 October pain report, and relevant evidence records before review. GitHub STATUS was retrieved read-only during this review. No GitHub writes were made.

Primary source: [Taylor et al., Frontiers in Psychiatry 13:914044](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2022.914044/full), DOI 10.3389/fpsyt.2022.914044, [PMID 35990066](https://pubmed.ncbi.nlm.nih.gov/35990066/), PMCID PMC9388784. Published 5 August 2022; survey conducted 10 June–13 July 2021. This is not a new 2026 result.

Publisher HTML and original [15-page PDF](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2022.914044/pdf) were checked independently. PDF pages 3–7 were visually inspected, including methods, demographic table, all interference cells, and help-seeking table/prose. PDF SHA-256: 4c7b5f9c6d116b6616407a6494a62306b4b7b0ca1812ba4f23ec1ab55440a6b2. Publisher PDF states CC BY. No paper copies, participant quotations, individual-level values or records are included in these deliverables.

Web PDF screenshots failed; ordinary publisher download and local rendering succeeded without a security bypass. Direct PubMed/PMC web openings showed browser challenges; indexed PubMed metadata corroborated identifiers. Exact-DOI corrigendum and retraction searches returned no results, and no correction notice was identified on the publisher page. This limited check is not comprehensive clearance. No linked supplement was identified in the publisher HTML. The data-availability statement promises author provision; it is not a public aggregate release, granted access or authorization to request participant data.

## Findings verified from methods and tables

- **Pain-based entry:** eligible participants were aged at least 16, had suspected or confirmed tic disorder, and were experiencing both tics and tic-related pain at participation. Recruitment used patient organizations, social media and an online support community; English literacy and internet participation were required. There is no pain-free sampling denominator or probability-sampling frame. The authors explicitly state prevalence was not the aim.
- **Sample and adulthood:** 181 completers, range 16–71; 41 in the 16–18 bin and 140 aged 19 or older. The number aged exactly 18 is unavailable. Calling everyone an adult because the authors used a 16-year threshold would misstate an age-18-plus estimand. Neither the age-bin totals nor the overall mean age identify adult-only interference means. No severe-state definition, persistence duration or severe-adult subgroup is supplied.
- **Interference:** the BPI-SF interference section was adapted to rate tics across 13 domains, with six domains added, a 1–5 response scale, and a not-applicable option. A corresponding adapted set rated tic-related pain. Both concern the previous week; separate domain means and SDs are printed. These are not reported as the standard unchanged BPI-SF, a validated total score, or a validated adult meaningful-change endpoint. No validation of this adapted instrument is demonstrated here.
- **Denominators:** the paper states no missing outcome data, but gives no per-domain valid-response counts or method of handling not-applicable responses. Completion and applicable numeric responses are distinct. Do not assume n=181 for every item, compute standard errors from that assumption, pool the 13 domains into an invented score, or derive paired tic-versus-pain tests without matching and covariance.
- **Descriptive values:** pain interference is highest for mood 3.31 (SD 1.24), sleep 3.24 (1.40), and enjoyment of life 3.04 (1.32). Table 3 gives the largest tic-interference mean for social situations, 3.86 (1.07), although the prose's list of highest domains omits it. Tic-related sleep SD is 1.31 in Table 3 versus 1.21 in prose. Neither conflict changes the pain-column means but both must remain visible.
- **Other measures/windows:** ATQ separately assesses current self-reported tic severity; BRS separately assesses resilience. The methods give no bounded recall interval for the help-seeking and previously used pain-management items. Previous use, current medication, perceived help, treatment receipt and past-week pain interference are not interchangeable estimands.
- **Mechanism:** the four themes and the tic-pain-cycle diagram arise from inductive analysis of open-ended responses. The diagram is explicitly theorized, with temporal ordering/timing uncertain. It is not a time-series or intervention demonstration. Self-attributed causes in Table 4 do not establish pathology, neuropathic pain or causal feedback; prior literature cited in the introduction is not a measured mechanism in this sample.
- **Effectiveness:** no randomization, comparator, assigned standardized therapy, prospective change or duration-of-benefit estimate establishes treatment efficacy. Table 4's treatment-specific perceived impact is separate from general professional-help receipt; the limitations say professional-help satisfaction/appraisal was not assessed. Counts of methods used are not success rates.

## Reporting conflicts and independent arithmetic

Table 5's categories sum to 181: 71 received help, 46 sought without receiving, 61 did not seek, and 3 uncertain. The first two imply **117 seekers**, also the table's provider denominator; prose/abstract report **118**. The reported 64.6% matches 117/181, not 118/181. Conditional receipt fractions are 71/117 = 60.68% and 71/118 = 60.17%; neither rounds conventionally to the prose's 60.1%. These are checks of incompatible printed statements, not recovered true counts.

Provider counts differ too: Table 5 lists GP 60 and physiotherapy 42; prose gives 61 and 43. The table's 51.3% and 35.9% match its 117 denominator. No corrected denominator or treatment-success estimate is adopted.

Ancillary discrepancies retained without extending the clinical question: Table 1 diagnosis-status categories total 180; prescribed-pain-medication categories total 178; no explanation is supplied. Table 2's low-resilience ATQ total is 72.26 versus 75.26 in prose, while its component means sum to 75.26. These prevent uncritical numeric reuse but do not erase reported pain burden.

`independent_checks.py` uses independently transcribed published aggregates and Python Decimal arithmetic. Its output records 18 checks, conditional denominator arithmetic and printed mean differences. All checks passed. Mean differences are descriptive arithmetic only; unknown matched denominators prevent promoting them to paired effect estimates. These checks are not independent clinical peer review or a participant-data reanalysis.

## Exact prerequisite and stopping point

To estimate age-18-plus pain interference, need a public age-eligible aggregate table with outcome-specific valid Ns, means and SDs, together with not-applicable/scoring rules. For matched contrasts need paired denominators/covariance; for clinically interpretable change need relevant validation, longitudinal outcomes and an appropriate anchor. Neither this report nor the earlier adult-pain study supplies these prerequisites. Do not pool unlike samples, infer missing data, collect participants or initiate custodian contact. Close the unchanged source audit pending a public correction or relevant aggregate release.

## Analysis-package cross-check

The main package's `aggregate_inputs.json`, code, outputs, 25 tests and report were reviewed independently. Its 13 domain means and SDs match the original table, with the table/prose sleep-SD conflict disclosed. Age counts, help-seeking counts and unknown item/adult denominators were preserved correctly. No numerical amendment was required.

Reran the main analysis and all 25 unit tests successfully; regenerated output was byte-for-byte identical. Separate Fraction calculations matched all 13 mean differences and all 26 conservative rounding-envelope endpoints, plus four denominator guardrails: 43 cross-implementation comparisons passed. See `compare_outputs.py`, `comparison_result.json` and `analysis_tests_rerun.txt`. The smallest gap remains positive even allowing for printed rounding; this is not an inferential or clinically important result.

The main report correctly distinguishes descriptive interference, qualitative themes, treatment-use/receipt and efficacy, and preserves the exact missing adult-specific prerequisites. The next-trial proposal is prospective work and has not been analytically reviewed here. No participant quotes, case-level records or individualized medical instructions were found in the reviewed deliverables. The final structured extraction and provenance also passed source-claim/privacy and internal-consistency review. Readability-only spacing amendments were applied. The documented PDF hash matches the independently retrieved source. No material source or numerical amendment was required. Ancillary retrieval details verified by the other source review were not represented as a new independent download in this audit.
