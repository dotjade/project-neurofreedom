# Newly indexed CBIT plus TMS preprint and linked registry audit

12 October 2026 | Original extraction of public aggregate evidence

## Bottom line

A newly indexed preprint reports a 50-person, three-arm experiment combining CBIT with 1 Hz rTMS, cTBS or sham in ages 12–21. Its abstract supports further investigation of neural target engagement. It does not establish that active stimulation adds clinical benefit over CBIT plus sham, durable disease modification, or efficacy for persistent severe adult illness. Keep the source in a separate preprint evidence file.

The associated registry supplies useful aggregate counts, but several units, time contrasts and analysis populations are insufficiently clear. Those ambiguities block a defensible clinical-effect reconstruction. This is a source/estimand audit, not a new participant-data analysis or an allegation of misconduct.

## Provenance and dates

- Preprint: Conelea and colleagues, “1Hz vs. cTBS Transcranial Magnetic Stimulation to Augment Behavior Therapy for Tics: A Randomized Clinical Trial.” DOI [10.64898/2026.09.29.26364036](https://doi.org/10.64898/2026.09.29.26364036); [PMID 42856611](https://pubmed.ncbi.nlm.nih.gov/42856611/); PMCID PMC13648794; trial [NCT04578912](https://clinicaltrials.gov/study/NCT04578912).
- The official [medRxiv DOI API](https://api.biorxiv.org/details/medrxiv/10.64898/2026.09.29.26364036) returned version 1, posting 1 October 2026, license `cc_by`, and `published: NA` on 12 October at 02:49:22 UTC. No peer-reviewed successor was verified. PubMed explicitly types it as a preprint.
- PubMed electronic publication: 1 October. Entrez history: 10 October 09:44. PubMed history: 11 October 05:07. PMC-release history: 8 October. The XML does not label the history timezone. The record was absent from yesterday's entry-query returns and present today; it is not newly first-published on 11 or 12 October.
- [ClinicalTrials.gov API](https://clinicaltrials.gov/api/v2/studies/NCT04578912) retrieved 12 October 02:49:09–02:49:15 UTC. Trial first posted 8 October 2020; actual start 1 November 2020; actual completion 31 December 2023. Results and last update were first posted 7 March 2025. These are previously posted results, not an October 2026 registry update or independent replication of the preprint.
- Published protocol: [Conelea et al., Trials, 3 July 2023, DOI 10.1186/s13063-023-07455-1](https://link.springer.com/article/10.1186/s13063-023-07455-1). Selected methods, outcome and sample-size sections were inspected. This is protocol version 6 dated 24 February 2022, not proof of the original 2020 registration or all subsequent amendments.

## Verified abstract findings

The authors describe ten stimulation sessions followed by CBIT, with 96% treatment completion. They report unchanged task-based SMA activation, cTBS-associated connectivity changes, improvement in tic frequency/controllability across all arms, and increased urges in the 1 Hz arm versus decreases in cTBS/sham. Treatment-related adverse events were described as mild-to-moderate and reported for 27%, 14.7% and 11.3% of sessions respectively. The abstract gives no exact session denominators or clinical between-arm effect estimates with confidence intervals. Session percentages are neither participant risks nor evidence of no rare/long-term harm.

## Aggregate registry extraction

All columns below use the order 1 Hz rTMS, cTBS, sham; all arms also received CBIT. Registry reporting categories are reproduced as data labels, not endorsed as analytically correct.

| Field | 1 Hz | cTBS | Sham | Interpretation |
|---|---:|---:|---:|---|
| Randomized / started | 17 | 16 | 17 | 50 total |
| Completed overall study | 17 | 15 | 16 | 48 total |
| Completed at least 80% of treatment sessions | 17 | 15 | 16 | Registry feasibility definition; 48/50 = 96% |
| Participants in both neural outcome rows | 15 | 13 | 17 | Different from completion and AE denominators; reason unverified |
| Treatment-related AE event count | 46 | 22 | 18 | Event counts, not affected-person counts; outcome table participant denominators 17/16/17 |
| AE-module risk denominators | 17 | 15 | 16 | Do not silently replace with randomized counts |
| Participants with serious AEs | 0 | 0 | 0 | As recorded over four months; small sample limits inference. Non-serious AE rows separately label assessment non-systematic |
| Headache, affected participants | 7 | 6 | 7 | Denominators 17/15/16 |
| Headache, event count | 21 | 10 | 9 | Repeat events can occur within one participant |
| Tic Suppression Task mean change, tics/minute | 0.58 | -3.83 | -8.24 | Registry lists only one unlabeled category despite describing five time contrasts |
| Corresponding standard deviation | 9.47 | 23.92 | 15.71 | Not confidence intervals |

The Tic Suppression Task row has participant denominators 17/16/17, a broad “baseline to 3 months” timeframe and no analysis rows providing a treatment contrast, confidence interval or p value. Its description names baseline-to-post, baseline-to-one-month, baseline-to-three-month, post-to-one-month and post-to-three-month changes, but its single values are not assigned to one of these intervals or a task condition. Do not calculate a purported treatment effect, pool it, or claim sham superiority from this ambiguous row.

The neural rows are also difficult to interpret. The resting-connectivity values are 0.0312, 0.261 and 0.158 (listed SDs 0.05, 0.05 and 0.03). SMA-activation values are 0.45, 0.01 and 0.27 (SDs 1.25, 1.25 and 1.30). Both rows use `MEAN`, `Standard Deviation` and unit `eta squared`, whereas their descriptions promise Cohen's d; the resting-connectivity description repeats the finger-tapping activation description. No clinical comparison is reconstructed from these inconsistent labels, and no within-arm neural effect is relabelled a between-arm clinical effect.

Exact session counts and number of sessions with at least one treatment-related event remain unverified. Multiplying randomized participants by ten would not resolve attrition, missed sessions or multiple events per session. Dividing registry event counts by hypothetical session counts would mix denominators and estimands.

## Population and baseline applicability

The current registry permits ages 12–21 with at least moderate chronic motor/vocal tics. It excludes antipsychotic use, left-handedness, inability to undergo MRI and several clinical contraindications; stable permitted medications require six weeks without change. These restrictions limit generalization to many adults with severe treated illness.

Registry age categories list 37 people at or below 18 and 13 in the “between 18 and 65” bin, constrained by the trial's maximum age 21. The category labels overlap at age 18; do not infer the exact count older than 18 or mature-adult representation. Sex counts are 8/8/7 female and 9/8/10 male. The registry baseline table does not supply tic severity, urges, suppressibility or medication distributions by arm. Therefore comparable clinical baselines cannot be verified from this record. No persistent-severe-adult subgroup result was identified.

## Protocol consistency and unresolved questions

The 2023 protocol planned phase 1 enrollment of 60, compared with actual 50. It foregrounds SMA activation, describes connectivity as a secondary neural measure, and specifies safety/feasibility go/no-go gates. The current registry labels both neural measures primary and safety/feasibility secondary; the preprint abstract calls safety, feasibility and neural engagement primary. These sources use different endpoint hierarchies. The protocol places clinical functioning and durability in further/exploratory analyses and phase 2. Its selection rules can favor cTBS without proving greater clinical efficacy. Historical versions and amendments were not checked, so the discrepancies alone do not establish undisclosed outcome switching. The protocol reports NIH/NIMH R61MH123754 support; final-preprint funding and conflicts remain unverified.

Next justified questions are: Why did enrollment stop at 50? Which endpoints and analysis populations were prespecified in the operative plan? Were baseline imbalances adjusted? What are exact session/event denominators, clinical between-arm estimates and intervals, multiplicity controls, masking success, missing-data treatment and follow-up retention? No author contact or access request was made.

## Access and reuse limits

Official PubMed abstract/date XML, medRxiv metadata, complete current ClinicalTrials.gov aggregate JSON and selected published protocol sections were read. Direct web opens of the preprint, PMC page and medRxiv JATS link were unsuccessful. A temporary full-text file retrieval was blocked before license verification and was not retried. Later DOI metadata verified CC BY, but the full preprint was not read in this extraction. No full paper, supplement, patient record or participant file is included in these deliverables.

No linked correction/retraction notice appeared in the retrieved PubMed record, and medRxiv metadata returned only version 1. This is not a complete publisher-history or retraction audit. Keep the preprint and registry as linked reports of one trial. Neither supports a treatment recommendation, home experiment, durable cure claim or replacement of the adult-persistence research priority.
