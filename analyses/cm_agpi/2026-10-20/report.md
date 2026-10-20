# CM–aGPi mechanism-evidence audit

20 October 2026 | Historical paper, not a new October publication

## Decision

**The paper adds a distinct simultaneous two-deep-target recording contrast to the earlier audited thalamocortical work, but it does not establish a causal tic generator, a validated predictor, or stimulation-free natural history.** The age and lawful full-methods gates are now resolved. Statistical units and exact visit contributions remain unresolved. Keep one physiology evidence record linked to its trial family; do not count the later registry results or mixed-cohort preprint as independent replication.

## Prediction and method

The bounded prediction was that full methods and trial links would either document an additional CM–aGPi state contrast in adults or show that the abstract only repeated an already audited measurement/cohort. A stronger inference would require explicit recording histories, independent analysis units, suitable controls and reproducible uncertainty. Failure of those stronger gates would limit the claim rather than erase an observed association.

Read the current repository README, protocol, status, October 19 lead, main evidence ledger and October 11 adult audit. Inspected the publisher's full article, source-linked primary reports, the named official registry, its protocol and statistical-analysis-plan PDFs. Searches were restricted to the exact paper, cited physiology papers and identified trial numbers. No generic cohort search, participant files, outreach, intervention or external write occurred. Full papers, source tables, individual outcome rows and participant narratives are not retained.

## Verified study facts

Lowor et al. (online 22 September 2025) enrolled six medically refractory adults aged 19–32; five contributed physiology after one localization exclusion. The reported six-person baseline total YGTSS was 91.5 (SD 3.8) out of 100; this must not be relabelled as the 0–50 total-tic scale. The trial is NCT05371041. Both CM and aGPi were recorded bilaterally at 250 Hz with synchronized video/EMG labeling. Conditions were rest (3 minutes), visually cued hand movement (3 minutes), and unrestricted tics (8 minutes). Tic categories were pooled. Two-second onset-centered epochs overlapped 50%; contaminated comparison segments were removed. Analysis covered power, coherence and phase-slope index (PSI), with group averaging and rank-based tests plus Bonferroni correction. [Primary article, Methods and Results](https://movementdisorders.onlinelibrary.wiley.com/doi/10.1002/mds.70043).

Reported findings include increased low-frequency power and CM–aGPi coherence during tics, with low-frequency CM phase leading pallidal phase. Beta/coherence nulls coexist with significant low-gamma interhemispheric PSI features. The latter conflicts with the Discussion's broader low-gamma phase-null wording. The three-month Methods window differs from the abstract's nine-visit wording; therapy starts in month four. [Primary article, recording timeline, Results and Discussion](https://movementdisorders.onlinelibrary.wiley.com/doi/10.1002/mds.70043).

### What the measurement actually contrasts

- Within a hemisphere, tic-associated spectral changes compare CM with aGPi, after subtraction of baseline power. Between-hemisphere comparisons are also reported. The reported low-frequency amplitude pattern is an observed state association.
- Coherence contrasts involve left/right CM, left/right aGPi, and ipsilateral CM–aGPi. Rest and cued voluntary movement are separate comparators. A state difference versus quiet rest does not alone discriminate a tic-specific cause from movement-related or common-input activity.
- PSI is a frequency-domain lag/direction summary. A leading phase is not proof that CM initiates a tic, that it acts through a direct CM-to-aGPi connection, or that intervening on that phase would improve symptoms. Shared input and recording/alignment effects remain competing explanations.
- Onset-centered windows contain post-onset signal. This analysis is not a prospectively evaluated pre-tic forecast. No unseen-participant clinical classifier is established by these tests.
- Cued hand actions differ from spontaneous motor/vocal tics in task structure, muscle recruitment and sensory consequences. They are a useful comparator, but not a fully matched counterfactual. Pooling tic types prevents subtype-specific conclusions.

These are analytic interpretations, not additional findings claimed by the investigators.

## Recording-state audit

The [official protocol](https://cdn.clinicaltrials.gov/large-docs/41/NCT05371041/Prot_000.pdf), approved 12 May 2025, separates physiological characterization in months 1–3 from programming/optimization in months 4–9. It also allows physiology at all protocol visits and possible intraoperative test stimulation. Its planned clinical endpoint is day 270, after approximately 30 days of stable settings. This corroborates a planned early recording phase; it does not identify the exact visits/epochs included in the published physiology estimates.

Do not replace the discrepancy with either “nine untreated months” or “only three months were analyzed.” The latter is plausible but not fully enumerated. A visit-level inclusion accounting and, if later visits contributed, prior stimulation/washout history are missing. “No current during the recording” answers a different question from “no earlier stimulation.” Even the early phase follows surgery, permits stable medication and represents a highly selected group. It cannot supply untreated population natural history.

## Statistical-unit diagnostic

The paper's descriptions do not unambiguously identify whether each rank-test observation is a participant summary, visit, epoch, frequency/time sample or another quantity. Epoch counts, inclusion by visit, weighting and the precise multiplicity family are not enumerated in the inspected main methods. Repeated visits, hemispheres and overlapping epochs cannot automatically be counted as independent people. Confidence intervals for the principal participant-level state contrasts are not provided in a form permitting effect reconstruction here.

A **post-reading diagnostic, not a preregistered study analysis**, tests one possible interpretation:

- Prediction under stated mathematical assumptions: an exact two-sided signed-rank test of five independent nonzero paired differences with distinct absolute ranks has a minimum doubled-tail p value of 2/32 = 0.0625.
- Method: enumerate all sign allocations; independently compare the enumerated minimum with 2^(1−n). Code and output are retained in `check_testing_unit.py` and `testing-unit-check.json`.
- Actual finding: n=5 yielded 32 allocations and minimum p=0.0625; the n=6 diagnostic control yielded 64 and p=0.03125. Assertions passed.
- Interpretation: very small published p values cannot be read as that exact five-pair calculation. This does not establish a reporting error, identify the authors' actual method, or choose among time/frequency/epoch units or asymptotic implementations. It makes the missing unit specification consequential.

No effect size, confidence interval, clinical sample-size recommendation or participant outcome was calculated.

## Counterevidence and internal consistency

The power/coherence and phase claims must remain metric-specific. Higher-frequency coherence nulls do not imply absent high-frequency information across all metrics. The reported low-gamma interhemispheric phase result is retained alongside the contradictory broad Discussion wording. Nonsignificance is not equivalence. The directional result also does not mean every synchrony metric is stronger for tics than for voluntary movement: phase consistency and coherence amplitude are different quantities.

The authors' steady-state focus leaves urge-to-tic and post-tic transitions untested. Limited nucleus coverage leaves possible common drivers unobserved. Localization exclusion narrows the physiological sample, while selection for severe refractory symptoms limits transport to less severe cases and the broader adult population. No persistent pain, function or quality-of-life mechanism is established by the state comparison.

## Trial and report overlap

| Primary source | Role in this audit | Deduplication decision |
|---|---|---|
| [Shute 2016, PMID 27419067](https://pubmed.ncbi.nlm.nih.gov/27419067/) | Earlier CM–motor-cortex recording/detection report | Prior measurement comparator; not simultaneous CM–aGPi confirmation |
| [Cagle 2020, PMID 32139653](https://pmc.ncbi.nlm.nih.gov/articles/PMC7296862/) | Four-person CM–M1 physiology report explicitly naming NCT02056873 | Older trial family; six monthly visits are repeated measures |
| [Cagle 2022, PMID 36094652](https://pmc.ncbi.nlm.nih.gov/articles/PMC9468946/) and [Okun 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC10948908/) | Embedded/responsive treatment reports in the older program already audited October 11 | Do not add their participants as independent new corroboration |
| [Lowor 2025, PMID 40977255](https://pubmed.ncbi.nlm.nih.gov/40977255/) | Current simultaneous deep-target paper, NCT05371041 | One source record in the newer trial family |
| [NCT05371041 results](https://clinicaltrials.gov/study/NCT05371041) | Eight-enrollee trial results posted 25 September 2026 | Same trial, different sample/timepoint/estimand; not an independent cohort |
| [Lowor et al. 2026 preprint, PMID 42780243](https://pubmed.ncbi.nlm.nih.gov/42780243/), [primary manuscript](https://pmc.ncbi.nlm.nih.gov/articles/PMC13596655/) | Sixteen-person EMG/video modeling report explicitly combining NCT02056873 and NCT05371041 | Overlap flag, not peer-reviewed independent replication; exact participant/recording intersection not resolved |

The current registry and its protocol exclude prior DBS/neurosurgical intervention, including explanted DBS. Together with the different implants and trial identifier, this supports a distinct enrolled implant cohort from earlier NCT02056873 work, conditional on adherence to eligibility. It is stronger evidence than different titles alone. It is not individual identity verification, and no private identity matching was attempted. A pooled preprint naming both trials does not create a third independent cohort.

## Separate linked registry finding

The official API verifies active-not-recruiting status, actual enrollment eight, a single-group unmasked feasibility design and results first posted 25 September 2026. Public aggregate flow is eight started/eight completed. The registry reports three of eight participants affected by serious adverse events and eight of eight by other events, with zero deaths. The AE interval runs from enrollment to end of follow-up, approximately two years after lead implantation; assessment is non-systematic. These are reported occurrences, not estimated device-caused risks. They must not be merged with the paper's earlier, smaller safety observation.

The current [registry](https://clinicaltrials.gov/api/v2/studies/NCT05371041) declares no IPD-sharing plan. The paper's reasonable-request statement does not establish public data availability, permission or that every modality can be supplied. No request was made.

Clinical endpoint metadata require a separate reconciliation: the protocol anchors month nine to implantation, whereas registry group wording anchors it to DBS initiation. The registry describes a total-tic outcome while its baseline description also invokes a total-plus-impairment scale. Do not calculate before/after effects or responder rates from mismatched constructs. Individual registry rows were neither retained nor analyzed. The [SAP](https://cdn.clinicaltrials.gov/large-docs/41/NCT05371041/SAP_001.pdf) is labelled 20 December 2021 but includes a manuscript-specific clinical baseline/month-nine analysis paragraph; it does not establish prospective specification of the current physiology comparisons.

## Next decision and stopping rule

The bounded methods/age/trial audit is complete with qualified additional mechanistic association evidence. It does not authorize a participant-data reanalysis or a clinical mechanism claim.

Next useful public-source task: reconcile this exact trial's clinical outcome construct, time origin, denominator and analysis plan using its protocol, registry metadata and any linked primary clinical report. Retain aggregate safety timing and non-systematic ascertainment. Stop without an efficacy calculation if the scale/timepoint or eligible aggregate outcomes cannot be verified. Do not reconstruct, download or publish participant rows, contact investigators, or reopen a generic cohort search.

A future causal or prospective-prediction test would additionally need the actual visit/epoch hierarchy, synchronization precision, comparator matching, pre-onset definitions, participant-held-out validation and governed data access. These are prerequisites, not a proposal to collect or perturb participants now.

## Access, licensing and notice checks

Publisher full HTML was accessible through the web reader; direct HTTP and the supplement link failed. PMC direct views sometimes returned a browser challenge, while indexed primary-source text was accessible. The main article's license is CC BY-NC-ND 4.0. This folder contains original criticism, factual metadata, identifiers and diagnostic code, not redistributed article/supplement text or figures. The unavailable supplement prevents independent confirmation of its full plots/Table S1 and may conceal clarifications; an absence judgment is limited to inspected material.

No correction/retraction notice was identified in the inspected PubMed/publisher views or an exact-DOI notice search. This is a bounded notice check, not comprehensive clearance. Source-claim locations and access limits are in `source-claim-matrix.json`; safe registry metadata and acquisition code are separate. No assertion about a newer paper or registry result is based on a mirror's crawl date.

## Independent review artifacts

The separately prepared [independent review](review/independent_review.md) checks source interpretation and boundaries. Its [independent exact-rank checker](review/check_exact_rank_bound.py) checks the conditional mathematical bound. Neither substitutes for clinical peer review or reproduces the original physiology calculation.
