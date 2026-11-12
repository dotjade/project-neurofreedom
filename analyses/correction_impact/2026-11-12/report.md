# Historical correction: dependency known, scientific impact unresolved

12 November 2026. Bounded metadata/dependency audit, not a clinical reanalysis or new biological result.

## Question, prediction and methods

Does the September corrigendum to the 2025 sensorimotor-integration report change a scientific claim already used by this repository? The earlier November 12 run recorded the prediction before its source attempts: metadata alone cannot establish what changed or justify revising a scientific conclusion. A readable notice identifying a changed method/result and a dependent claim would disconfirm a no-revision decision.

The original uncommitted audit files were lost during an interruption. This package rebuilds the dependency computation and refreshes official metadata with current timestamps. The earlier prediction and access outcomes are recovered from the retained execution record, not represented as a surviving original preregistration or byte-exact archive. No new biological computation is substituted for unavailable inputs.

The reproducible [script](audit.py) reads official PubMed metadata, searches all tracked text at baseline commit 4894c40b9da2714730fb50d5730bea6e3fc92608 for the original/notice PMID, DOI, title and distinctive authors, then searches broader construct terms in Markdown and core evidence/feed files. Only top-level PubMed article identifiers are extracted, excluding reference-list identifiers. Full paper text and participant records are not saved.

## Actual result

The [original](https://pubmed.ncbi.nlm.nih.gov/40680639/) is electronically dated July 13, 2025, DOI 10.1016/j.nicl.2025.103844, PMID 40680639, PMC12296559. The [notice](https://pubmed.ncbi.nlm.nih.gov/42767894/) is a Published Erratum electronically dated September 21, 2026, DOI 10.1016/j.nicl.2026.104054. Current [metadata](metadata.json) verifies reciprocal links. Neither is a new November publication.

**The notice's substantive content remains unavailable in this bounded pass, so its scientific impact is unknown.** Earlier November 12 publisher opens returned 403, the DOI open was inaccessible, and PubMed supplied no notice abstract. Indexed passages of the original were readable, but cannot reveal the later correction. Those unsuccessful routes were not repeated during recovery. Differing affiliation text is not enough to infer an affiliation-only correction. The notice is not assumed harmless, and the original is not declared invalid.

The fresh [dependency computation](dependencies.json) searched all 1,699 tracked UTF-8 baseline files. Six exact-hit paths are confined to November 11 screening/notice metadata. No exact dependency appears in evidence.jsonl, hypotheses, foundation, roadmap, the current public feed or a scientific analysis. One broader paragraph in the October 28 [causal critique](../../causal_synthesis/2026-10-28/critique/critical-synthesis.md) cites Kleimaker 2020 (PMID 32464659) and Wehmeyer 2023 (PMID 37019631), not this corrected paper.

No existing scientific claim is revised and no empirical evidence record is added. This is a repository-dependency finding, not a biological finding. An uncredited paraphrase or indirect citation chain could escape this text search. Eleven fresh consistency checks pass; they do not validate the inaccessible notice or constitute clinical peer review. A [fresh separate AI consistency review](review.md) reproduced the rebuilt dependency result and 11 checks. The lost earlier review artifact is not treated as current verification.

## Uncertainty and next decision

The operational prediction was not disconfirmed by the available metadata. Missing correction text is not evidence that nothing important changed. The original concerns task-related EEG and stimulus-response integration; its contextual associations do not themselves establish the cause of tics, treatment selection, clinical benefit or an invariant measure of urge generation. That is not a verified corrected extraction.

Close this fixed audit until a lawful readable publisher or licensed repository copy identifies the notice's exact changed item and its mapping to the original, or a new repository claim begins relying on the paper. Then revise only supported dependent claims. Do not repeat blocked routes, contact authors or acquire participant data to manufacture an answer.

The notice supplies no verified H18 calibration/transfer input, H15 exact map provenance or adult driving analysis-set table. Their separate [existing stop rules](../../../updates/2026-11-11/analysis-feasibility.md) remain. A useful clinical-benefit study need not satisfy all three mechanism-specific gates. Persistent severe adult pain, effort, function, participation and co-occurring burden remain central alongside all ages and severities.

No treatment change, intervention, recruitment, outreach, author contact, personal data, paid resource or cure claim is involved. No owner action is needed for continued bounded surveillance.

## Reproduce

From the repository root, run `python analyses/correction_impact/2026-11-12/audit.py`. The fixed baseline must be in Git history. Metadata is a live source and may change; the saved JSON preserves this run's result and time. [Access record](access-record.json) distinguishes fresh verification from earlier recovered outcomes.
