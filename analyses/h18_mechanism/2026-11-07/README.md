# H18 mechanism and generalization audit

Read [report.md](report.md) for the decision, evidence and limits. This historical source audit separates whole-treatment efficacy, mediation, treatment moderation, direct reward manipulation and transfer. H18 remains proposed; no personalized component rule is validated.

The five focal reports are not five independent randomized cohorts. Eight primary-study records and one no-results registry lead are preserved in evidence.jsonl. Three primary records reuse the original two CBIT trials. Abstract-only context, a partially accessible adult mechanistic lead and an open historical duration comparison are distinguished in the search ledger.

Run `python validate.py` for deterministic consistency checks. `build_artifacts.py` recreates the authored structured files from the local bibliographic metadata and original extractions; it performs no source requests or clinical reanalysis. Neither script establishes clinical validity. `python check_statistical_consistency.py` (SciPy) reproduces the F-tail consistency check; it preserves the printed p-value and does not reconstruct participant-cluster-adjusted inference. The substantive report and separate reward-component audit contain source links; no full text, participant data or videos are included.

The prediction was recorded after title/abstract discovery and before detailed primary-methods extraction; this was not preregistered research. No treatment, outreach, account creation or paid resource was used. Proposed synthetic work is a future analysis, not an executed result.
