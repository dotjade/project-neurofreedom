# NCT05371041 public-document compatibility audit

Start with `report.md`. The conclusion is **stop without an efficacy calculation**; this is not a negative treatment finding.

- `structured-extraction.json`: original claims with source paths/pages and compatibility gates.
- `registry-projected-metadata.json`: current official API fields returned at 02:51:59 UTC on 21 October 2026, with server projection excluding participant result classes.
- `retrieval-log.json`: exact queries, source dates/access, official PDF hashes and limitations.
- `evidence-record.json` / `.jsonl`: one original trial-family evidence record, not independent clinical replication.
- `artifact-manifest.json`: exact deliverable allowlist, sizes and SHA-256 hashes; excludes transient Python cache files.

Reproduce the local checks (18 metadata/boundary assertions, not statistical tests):

```sh
python build_extraction.py
python check_metadata.py
```

`collect_registry_metadata.py` fetches the **current**, mutable official record. Preserve the dated snapshot before refreshing; future changed metadata may correctly fail these snapshot-specific checks. It requests explicit safe metadata/aggregate fields and rejects result-class/measurement structures before writing. No efficacy calculation exists in these scripts. `finalize_artifacts.py` rebuilds the provenance record and manifest for this fixed run.

The official protocol/SAP were parsed in memory; PDF copies/full text are not deliverables. An initial web-search result unexpectedly displayed mirrored participant rows; no values are retained or used. See the report's privacy accounting rather than interpreting the safe artifacts as proof that no row was ever displayed.
