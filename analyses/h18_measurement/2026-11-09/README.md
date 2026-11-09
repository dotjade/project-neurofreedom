# H18 measurement audit package

The [report](report.md) states the decision and transfer estimands. [measurement-adequacy.json](measurement-adequacy.json) is the canonical six-source extraction. [search-ledger.json](search-ledger.json) records the exact targeted searches, access limits and stopping rule. [evidence-additions.jsonl](evidence-additions.jsonl) contains lightweight append candidates linked to the canonical extraction; deduplicate against the current repository before publication.

No primary papers, participant-level files or videos are included. The suggested repository destination is `analyses/h18_measurement/2026-11-09/`. The author did not edit the repository.

Run the consistency checks from this directory:

```sh
python validate.py
```

The output is [validation.json](validation.json). These checks verify authored accounting and inference constraints, not source truth or clinical validity. Source access was partial for several records and is explicitly disclosed. This historical measurement audit does not replace the separate daily publication/registry/safety scan.
