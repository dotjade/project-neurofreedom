# Daily public evidence scan: 25 October 2026

## Finding and decision

**One older primary paper was newly encountered, not newly published in this interval.** The July 25 CHD/Tourette population study was absent from yesterday's saved search but has an October 23 PubMed entry and publisher version-of-record date. Its overall Tourette estimate is null-compatible. Its severity prose and printed table disagree; neither establishes a directional severity conclusion. No qualifying new-window primary publication, preprint, posted trial result or retraction was verified. New-to-repository evidence is distinct from new evidence since the prior cutoff.

## Scope and provenance

Required repository documents, prior reports and evidence were inspected at `ab9d4320f0e51198866a176467a9a131cc7c44cd`. [Hashes](provenance.json) identify this baseline. No age, severity, language or human-only filters were imposed. Adult persistence, severe burden, comorbidities, unmet needs and negative findings remain within scope; pediatric observational results are not extrapolated to adults.

- Prior core cutoff: **2026-10-24 02:45:24.341792 UTC**.
- Current core requests: **2026-10-25 02:45:01.257480–02:46:02.904884 UTC**.
- Inclusive overlap: **October 23–25**, with narrower entry-date check October 24–25. October 25 was only partly elapsed.
- Official registry supplements: **02:45:16–02:45:24 UTC**.
- Primary source/table and independent checks occurred after the core scan, with exact timestamps in their records.

Publication, entry, revision, preprint version and registry posting dates are not interchangeable. PubMed supplies history date/time fields without a verified timezone here; preserve the raw fields rather than assigning a timezone.

## PubMed

Eight ESearch queries yielded **12 ID occurrences and 8 unique records**, all fetched below the 1,000-ID cap. [Queries and translations](search-log.json), [request timestamps/hashes](request-log.json) and [decisions](pubmed-screening.jsonl) are saved.

| Query family | Field | Interval | Count |
|---|---|---|---:|
| Tourette OR tic disorder(s) | edat | October 23–25 | 2 |
| Same core | edat | October 24–25 | 0 |
| Same core | pdat | October 23–25 | 0 |
| Same core | mdat | October 23–25 | 7 |
| Core plus correction/retraction terms | edat | October 23–25 | 0 |
| tics OR chronic motor/vocal tic OR persistent tic | edat | October 23–25 | 2 |
| Same synonyms | pdat | October 23–25 | 0 |
| Core plus adult/severe/burden/comorbidity/treatment/adverse/negative terms | edat | October 23–25 | 1 |

### Older primary study newly captured

[Yu et al., PMID 42919181](https://pubmed.ncbi.nlm.nih.gov/42919181/), [DOI 10.1186/s12888-026-08454-7](https://doi.org/10.1186/s12888-026-08454-7), analyzed caregiver-reported NSCH 2022–2023 data, ages 6–17 (unweighted n=52,846), with chronic-condition and missing-data exclusions. Tourette was exploratory. [Table 2](https://link.springer.com/article/10.1186/s12888-026-08454-7/tables/2) reports adjusted OR **1.48 (95% CI 0.54–4.07), p=.45** for CHD versus no CHD. This is not equivalence.

[Table 3](https://link.springer.com/article/10.1186/s12888-026-08454-7/tables/3) prints mild **1.32 (0.63–1.49), p=.08**, and moderate/severe **0.68 (0.22–3.26), p=.12**, at n=52,839. Prose instead describes a higher moderate/severe association. Preserve the inconsistency without repairing numbers or endorsing a directional severity claim. Weighted population totals are not participant counts. Cross-sectional reporting, diagnostic surveillance, exclusions, multiple outcomes and wide intervals preclude causal or adult-specific inference. No intervention is tested.

Publisher “Published” is July 25; “Version of record” is October 23. The latter and PubMed entry precede the prior cutoff, despite the earlier search omission. The reason for retrieval discordance is unknown. [Original extraction](primary-evidence.jsonl), [source checks](primary-source-checks.json), [independent check](chd-independent-review.json).

### Remaining records and integrity

Six records overlap yesterday: the ASD/tic, adult persistence and video-phenotyping studies; a historical MRI report; a review; and a metadata-only case report. No case narrative was read or retained. The case's exact publication date remains unknown. Newly encountered PMID 42790390 was electronically published July 28 and entered PubMed September 25; its October 23 revision is not new research. The OCD quality-of-life model was not added as a tic-specific prospective model.

The known retracted preclinical paper [PMID 39947542](https://pubmed.ncbi.nlm.nih.gov/39947542/) and [notice 42527169](https://pubmed.ncbi.nlm.nih.gov/42527169/) retain reciprocal links and the same selected metadata. They remain excluded from positive mechanism/efficacy evidence. No new retraction or reinstatement is claimed. [Comparison](integrity-recheck.json).

## Preprints

Both official bioRxiv API feeds were fully paginated, with stable observed totals:

| Server | DOI/version pairs | Pages | Prior-feed overlap | Not in prior bounded feed |
|---|---:|---:|---:|---:|
| bioRxiv | 403 | 14 | 178 | 225 |
| medRxiv | 132 | 5 | 63 | 69 |

Title/abstract screening with `\btourett\w*|\btics?\b` found **zero lexical matches in 535 records**. Other servers, terminology and indexing lag remain gaps. The old CBIT/TMS preprint resurfaced in web discovery, not as a verified new version. [Indexes](biorxiv-preprint-index.tsv), [discovery log](discovery-log.json).

## Registries

ClinicalTrials.gov's server projection excludes measurements/results, contacts, officials and locations. Tourette/tic disorder/Tics/ecopipam update queries returned **0/1/1/0**, deduplicating to NCT07137442 without a next-page token. Four direct controls were checked. All selected status/design/result flags were unchanged versus October 24. [Registry records](registry-evidence.jsonl).

- NCT07137442 remains an observational protocol, planned enrollment 75, eligibility ages 18–80, estimated start October 28 and no results. Eligibility is not observed age distribution; planned dates are not actual recruitment.
- NCT05158439 remains withdrawn for inability to recruit, actual enrollment zero and no results. This is negative feasibility, not negative efficacy.
- NCT07093541 remains expanded access temporarily unavailable, no new cause inferred.
- NCT06194305 remains recruiting pediatric CBIT without results in selected fields.

ISRCTN's October 23–25 edited-date query returned zero, with a positive-control total of 22 (one record requested, not all 22 reviewed). WHO's homepage was readable and listed October 19 among provider import dates, but no Tourette query export was obtained. CTIS returned an application shell, not parsed trial data. These remain worldwide coverage limitations. [Supplement](supplement-selected-metadata.json).

## Access and reproducibility

All 36 core requests succeeded. Web-reader PubMed/table/PDF routes produced errors; ordinary publisher HTML succeeded without changed permissions or security settings. Source bodies were read transiently, not saved. Supplements were not inspected. No participant data, source papers, case narratives, contacts or paid compute are deliverables. No account, outreach, recruitment or clinical action occurred.

```sh
python prepare_baseline.py --repo /path/to/base-checkout --out /tmp/day25-baseline.json
python scan_sources.py --baseline /tmp/day25-baseline.json --out /tmp/day25-live-scan
python build_results.py --raw /tmp/day25-live-scan/search-log.json --repo /path/to/base-checkout --out /tmp/day25-reviewed
python validate_artifacts.py --repo /path/to/base-checkout
python verify_reproduction.py --repo /path/to/base-checkout
```

Supplement, integrity and primary-source scripts write beside themselves; copy to a temporary directory before live reruns. Live APIs can change; new IDs require manual review. The reproduction check validates normalized saved metadata, not clinical findings. This bounded scan does not replace a systematic review. The parent's separate ASD/measurement audit and safety/link pass are integrated independently; no repository write or publication was performed by this scan worker.


## Bounded investigation and journal integration

The [ASD age/measurement audit](../../analyses/asd_measurement/2026-10-25/report.md) advances the latest plan through primary-methods reconciliation and deterministic published-aggregate checks. A pooled age-adjusted association is not an adult-specific estimate; communication/reporting differences remain a proposed explanation, not a tested mechanism. Counterevidence and uncertainty are retained. Independent review accompanies the calculations. The [safety/link pass](safety/report.md) records actual official-source and displayed-link checks. Six safe activities and disabled collection are preserved. GitHub/live publication is claimed only in the later verification receipt.
