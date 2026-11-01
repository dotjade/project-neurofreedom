# Daily evidence scan: 1 November 2026

## Result

**No qualifying new-window first publication, preprint or posted trial result was verified.** Historical November issue assignments brought older papers into the date query. Those are not new November discoveries. Selected registry metadata and known retraction controls were unchanged.

The previous verified core cutoff was **2026-10-31T03:27:38.991962+00:00**. Today's final core ran **2026-11-01T03:09:40.997253+00:00 to 2026-11-01T03:12:29.801672+00:00**. PubMed and ClinicalTrials.gov use October 30-November 1 inclusive overlap; the final preprint pass uses October 29-November 1. November 1 is only partly elapsed, and date-only source fields do not establish exact within-day ordering. All **48 final core API requests** succeeded. [Requests](request-log.json), [exact queries](search-log.json), [summary](summary.json).

Scope covers all ages and severities, including persistent severe adult symptoms, chronic motor/vocal tics, functional burden, pain, co-occurring conditions, unmet needs and treatment response. No age/severity/human-only filter was imposed. This bounded check is not an exhaustive systematic review or proof that no relevant evidence exists.

## Primary publications and secondary context

Eight PubMed query families returned **19 ID occurrences and 17 unique records**, all fetched below the query cap. Twelve overlap yesterday's scan; five are absent from yesterday, not necessarily new to the repository or newly published. [Record-level decisions](pubmed-screening.jsonl).

| Query | Date field | Count |
|---|---|---:|
| core_edat | edat | 0 |
| near_edat | edat | 0 |
| core_pdat | pdat | 6 |
| core_mdat | mdat | 9 |
| notice_edat | edat | 0 |
| syn_edat | edat | 1 |
| syn_pdat | pdat | 3 |
| burden_treatment_edat | edat | 0 |

The older [pediatric protective-care medication study](https://pubmed.ncbi.nlm.nih.gov/42664664/) was electronically published August 28, DOI 10.1016/j.chiabu.2026.108287. Its 231 children aged 5-12 were not a TS-selected sample. A Tourette diagnosis was among reported correlates of polypharmacy, but the abstract lacks a TS subgroup denominator, coefficient and interval. Confounding by indication and ascertainment prevent efficacy or causal safety conclusions. It does not validate persistent-severe-adult care. This is a newly retrieved historical context record, not new-window evidence.

The [August 11 cannabinoid synthesis](https://pubmed.ncbi.nlm.nih.gov/42617303/), DOI 10.1016/j.psychres.2026.117380, is secondary, not an independent primary cohort. Its abstract describes trivial-to-no randomized TS benefit and predominantly very-low-certainty evidence overall. Its pooled adverse-withdrawal finding is not a TS-specific estimate. No treatment recommendation follows. [Original limited extractions](older-evidence.json).

The already screened [cross-sectional imaging cohort](https://pubmed.ncbi.nlm.nih.gov/42640249/) was published August 25, not November 1. Its tic-severity null remains relevant counterevidence; neither a causal stable trait nor treatment target is established. The historical possible PANDAS case series is metadata-only here, with no individual narratives inspected. Cognitive-test TICS acronym collisions are excluded. The [known retracted paper](https://pubmed.ncbi.nlm.nih.gov/39947542/) and [notice](https://pubmed.ncbi.nlm.nih.gov/42527169/) retain unchanged selected metadata and remain excluded from positive evidence. [Integrity control](integrity-recheck.json).

## Preprints

The case-insensitive title-plus-abstract screen `\btourett\w*|\btics?\b` found no lexical matches in the final pass. Positive controls match “Tourette syndrome” and “persistent motor tics”; “statistics” is a negative control. AST/runtime inspection confirms the prior committed pattern also passes these controls.

| Server | DOI/version records | Pages | Yesterday's overlap | Absent from yesterday |
|---|---:|---:|---:|---:|
| bioRxiv | 707 | 24 | 521 | 186 |
| medRxiv | 191 | 7 | 163 | 28 |

Both observed page sequences completed with stable totals. [bioRxiv index](biorxiv-preprint-index.tsv), [medRxiv index](medrxiv-preprint-index.tsv). DOI/version counts are not counts of new papers. Other servers, alternate vocabulary and delayed indexing remain outside coverage. A repeated verification run broadened the preprint overlap by one day; it does not imply new evidence or continuous execution. The first completed pass is separately recorded in [initial-pass-summary.json](initial-pass-summary.json).

## Official trial registries

ClinicalTrials.gov's four update-window queries returned 1, 2, 2 and 0 records, yielding two unique IDs. Four direct controls brought the selected comparison set to five. All selected status/design/results fields were unchanged from October 31, with no posted results. [Comparisons](registry-evidence.jsonl).

- [NCT07905898](https://clinicaltrials.gov/study/NCT07905898): adolescent PRISM-TS feasibility protocol, not yet recruiting. The previously documented top-line 95 versus narrative 85 adolescent denominator difference remains unresolved; this is not 95 randomized adolescents. No efficacy or safety estimate exists.
- [NCT07137442](https://clinicaltrials.gov/study/NCT07137442): the estimated November 4 start is unchanged, not an observed event.
- [NCT05158439](https://clinicaltrials.gov/study/NCT05158439): withdrawn, actual enrollment zero; recruitment feasibility failure is not negative efficacy.
- [NCT07093541](https://clinicaltrials.gov/study/NCT07093541): expanded access remains unavailable; no reason or safety cause inferred.
- [NCT06194305](https://clinicaltrials.gov/study/NCT06194305): pediatric CBIT protocol, recruiting without results.

ISRCTN returned zero for October 30 inclusive to November 1 exclusive; the positive control returned 22 total with one requested record. The window excludes November 1 changes. WHO ICTRP yielded no current query export; CTIS returned an application shell, not an audited trial record. HTTP success does not establish comprehensive registry coverage. [Supplement](supplement-selected-metadata.json). Ranked web discovery returned older and indirect sources; mirror crawl dates were not used as official amendment dates.

## Reproduction, limitations and decision

From repository root:

```sh
python updates/2026-11-01/scan/prepare_baseline.py --repo . --out /tmp/nf-baseline.json
python updates/2026-11-01/scan/scan_sources.py --baseline /tmp/nf-baseline.json --out /tmp/nf-live
python updates/2026-11-01/scan/build_results.py --raw /tmp/nf-live/search-log.json --repo . --out /tmp/nf-normalized
python updates/2026-11-01/scan/validate_artifacts.py
```

Live APIs may change; the normalizer rejects unreviewed IDs, registry changes and preprint matches. Supplement/control scripts write beside themselves, so run a temporary copy to preserve this dated record. Validation checks metadata consistency and privacy minimization, not clinical validity or comprehensive capture. No participant rows, full-text papers, private content or source abstracts are retained.

Do not turn historical issue assignments into new discoveries. Before quantitative use of the older polypharmacy association, obtain lawful participant-free TS subgroup counts and adjusted coefficients with uncertainty. Secondary cannabinoid estimates require primary-cohort deduplication before synthesis. Today's separate bounded analysis, safety audit and publication verification are owned by the parent daily report.
