# Daily public evidence scan: 27 October 2026

## Finding and decision

**No qualifying new-window primary publication, preprint or posted trial result was verified in this bounded scan.** An older September genetic-association paper was newly discovered through October publicity and added separately. Two official registry updates are metadata postings, not new clinical findings. This is not exhaustive worldwide surveillance or evidence that no new research exists.

## Scope, dates and method

Required project documents, current evidence and the prior scan were inspected at `10689d9b7194f8600dd2d9b01137975229cd036b`; [provenance](provenance.json) records hashes. Scope includes Tourette and chronic tic disorders across ages and severities, persistent severe adult symptoms, pain, function, co-occurring conditions, unmet needs and treatment response. No age, severity or human-only filter was applied.

- Previous core cutoff: **2026-10-26 02:59:34.225370 UTC**.
- Current core requests: **2026-10-27 03:14:32.867159–03:15:11.950351 UTC**.
- Inclusive overlap: **October 25–27**, with a narrower October 26–27 entry-date check. Today is only partly elapsed.
- Supplementary genetics metadata checked at **03:16:37–03:16:41 UTC**, outside core counts.

Publication, indexing, revision, registry posting and secondary-news dates are not interchangeable. PubMed history times have no verified timezone here. Metadata revision and search reappearance are not proof of new scientific findings.

## PubMed

Eight queries yielded **12 ID occurrences and 11 unique records**, all retrieved below the 1,000-ID cap. [Exact queries/translations](search-log.json), [requests](request-log.json) and [screening decisions](pubmed-screening.jsonl) are retained.

| Query family | Field | Interval | Count |
|---|---|---|---:|
| Tourette OR tic disorder(s) | edat | October 25–27 | 1 |
| Same core | edat | October 26–27 | 0 |
| Same core | pdat | October 25–27 | 0 |
| Same core | mdat | October 25–27 | 9 |
| Core plus correction/retraction | edat | October 25–27 | 0 |
| Tics and chronic motor/vocal/persistent tic synonyms | edat | October 25–27 | 1 |
| Same synonyms | pdat | October 25–27 | 0 |
| Core plus adult/severe/burden/comorbidity/treatment/adverse/negative terms | edat | October 25–27 | 1 |

Four records overlap yesterday; seven are absent from that day's bounded set, not necessarily new to all prior research. These include old functional-tic follow-up, developmental, rage, pediatric treatment-pattern and trial-representation reports, a care-pathway letter, and a previously screened case report. Their electronic dates precede this window; the case report's exact publication date remains unknown. No individual or family narratives were retained. Medication-use associations are not randomized treatment effects, and functional tic-like behaviors are not silently merged with primary Tourette outcomes.

Previously extracted CHD/Tourette and rat-model records remain qualified by their table/prose inconsistency and unresolved causal/human-translation limits, respectively. The known retracted preclinical source [PMID 39947542](https://pubmed.ncbi.nlm.nih.gov/39947542/) and [notice 42527169](https://pubmed.ncbi.nlm.nih.gov/42527169/) retain unchanged reciprocal links and selected metadata. They remain excluded from positive evidence. [Integrity check](integrity-recheck.json).

## Supplementary discovery: older genetics evidence

[Wang et al.](https://www.nature.com/articles/s41593-026-02419-5), [PMID 42680906](https://pubmed.ncbi.nlm.nih.gov/42680906/), was published **September 1**, not October 26. Its 3,964 affected probands include 2,418 trio probands and 1,546 singletons; 1,734 control trios are separate. The combined analysis identified 34 high-confidence genes, while 36 is the union across combined and diagnosis-specific analyses. These are associations, not 36 validated treatments or individual prognoses. Previously reported samples contribute, so independent replication is not established merely by this publication. No persistent-severe-adult clinical conclusion follows.

Only abstract and opening main-text passages were inspected. Gene-specific uncertainty, ancestry, full ascertainment and sample-overlap details remain unextracted. No genomic participant data were obtained. [Original extraction](primary-evidence.jsonl), [independent check](genetics-independent-review.json), [selected primary metadata](genetics-selected-metadata.json). The DOI/PMID were absent from the recorded baseline; October 26 publicity is discovery provenance, not scientific evidence or a new publication date.

## Preprints

Both official bioRxiv API feeds were fully paginated with stable observed totals. Title/abstract screening with `\btourett\w*|\btics?\b` found **zero matches among 343 DOI/version records**.

| Server | Records | Pages | Previous overlap | Not in prior bounded feed |
|---|---:|---:|---:|---:|
| bioRxiv | 219 | 8 | 55 | 164 |
| medRxiv | 124 | 5 | 6 | 118 |

Indexes retain DOI/version/date only. Other servers, different terminology, indexing delays and dynamic pagination remain limitations. No preprint was presented as peer-reviewed evidence.

## Official registries

ClinicalTrials.gov's four update queries returned **1, 2, 2 and 0** records, deduplicating to two IDs, without pagination tokens. The server projection excluded participant measurements/results, contacts, officials and locations. [Selected records and comparisons](registry-evidence.jsonl).

- [NCT07137442](https://clinicaltrials.gov/study/NCT07137442): October 26 posting; estimated start moved October 28 to October 29. Recruiting label, planned enrollment 75, adult eligibility and no-results flag remain. These dates do not establish actual recruitment or outcomes.
- [NCT01019343](https://clinicaltrials.gov/study/NCT01019343): October 26 posting for a basic-science movement-disorder study completed in 2020, with actual total enrollment 1,273 and no results. The mixed-diagnosis total is not a Tourette sample size. Without a previous-day snapshot, no historical status change is inferred.
- Three other direct controls are unchanged: [NCT05158439](https://clinicaltrials.gov/study/NCT05158439) remains withdrawn for inability to recruit, actual enrollment zero, which is negative feasibility rather than efficacy; [NCT07093541](https://clinicaltrials.gov/study/NCT07093541) remains expanded access temporarily unavailable; [NCT06194305](https://clinicaltrials.gov/study/NCT06194305) remains recruiting pediatric CBIT without results in selected fields.

ISRCTN's October 25–27 edited-date query returned zero; the positive control reported 22 total, with only one requested record, not all 22 reviewed. WHO's readable homepage is not a completed Tourette query export. CTIS returned an application shell, not parsed trial data. These are explicit worldwide coverage limits. [Supplement timestamps/metadata](supplement-selected-metadata.json).

## Reproducibility and limitations

All **30 core requests** succeeded. Thirty-two offline consistency/privacy checks passed, and seven normalized outputs reproduced byte-for-byte. These verify metadata/software, not clinical findings. Live APIs can change; the normalizer rejects unreviewed IDs, and new registry changes require manual assessment.

```sh
python updates/2026-10-27/prepare_baseline.py --repo . --out /tmp/day27-baseline.json
python updates/2026-10-27/scan_sources.py --baseline /tmp/day27-baseline.json --out /tmp/day27-live
python updates/2026-10-27/build_results.py --raw /tmp/day27-live/search-log.json --repo . --out /tmp/day27-reviewed
python updates/2026-10-27/validate_artifacts.py --repo .
python updates/2026-10-27/verify_reproduction.py --repo .
```

Copy supplement/integrity scripts to a temporary directory before live reruns because they write beside themselves. No full-text papers, abstracts, patient rows, case narratives, secrets or private data are deliverables. No outreach, recruitment, paid compute, medical action or patient-specific inference occurred. The separate bounded investigation, safety/link pass and public feed integration are reported by the integrating researcher; publication requires later exact source/live readback, not merely local preparation.


## Bounded investigation and public journal

The [EMTICS measurement audit](../../analyses/emtics_validation/2026-10-27/report.md) advances the latest plan by reconciling high reported alpha with lower reported omega, external correlations and marginal factor fit in the same pediatric sample. Published-cutoff comparisons and conditional rounding checks are reproducible deterministic arithmetic, not a model refit, clinical effect or participant reanalysis. The supplement's negative and inconclusive diagnostics remain visible. Exact omega implementation is unverified; no coefficient is declared the true reliability. Adult, severe-adult and ASD/communication-group validation are not supplied by this pediatric study. Ten implementation tests and 28 independent checks passed, not clinical peer review.

The [safety/link pass](safety/report.md) distinguishes new official documents and agenda items from adopted watched-treatment risk findings. No qualifying new risk was verified within its documented coverage. All six approved activities are unchanged, with rest-or-leave selected; collection stays disabled. The dated public note separates the no-new-publication/result scan from older genetics evidence and the historical methods audit. Publication is established only by the later exact GitHub and production receipt.
