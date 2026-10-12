# Adult sensory gating precision audit

12 October 2026. Target: PMID 42810670, DOI 10.1016/j.biopsycho.2026.109408.

Read [report.md](report.md) for the finding and [preanalysis.md](preanalysis.md) for the prediction recorded before new retrieval. [extraction.json](extraction.json) distinguishes verified fields from missing prerequisites. [search_log.json](search_log.json) records bounded queries and access outcomes.

## What ran

The only supplied code is a **metadata retrieval and identity-check script**, not statistical effect-size estimation. It does not save abstracts, full text, or participant data. The actual run's selected metadata and console output are `source_metadata.json` and `source_check.log`.

To rerun from this directory with Python 3 and network access:

```sh
python -u check_source_metadata.py | tee source_check.log
```

The script uses only the Python standard library. A rerun replaces these two local outputs with a dated new metadata snapshot; source contents and hashes can change. Preserve the original snapshot separately before rerunning if historical provenance is needed. Each source records its URL, retrieval time, HTTP status, source-body hash and selected metadata. The source response bodies themselves are not retained.

## What did not run

No effect-size, confidence-interval, equivalence, power or participant-level calculation was performed. Missing numerical inputs and precise statistical definitions prevent a defensible study precision estimate. The report's variance expressions describe required information; they are not reconstructed paper results.

## Validation completed

- All three JSON files parsed successfully.
- Each baseline repository file has a recorded blob SHA.
- All four metadata endpoints returned a successful validated metadata extraction on the archived script run.
- The script hash in the output matches the delivered script.
- Every unobserved effect estimate and confidence interval remains null in the extraction.

These are bookkeeping and provenance checks, not statistical validation or independent scientific peer review. No repository files were committed by this worker; the parent review decides what to incorporate.
