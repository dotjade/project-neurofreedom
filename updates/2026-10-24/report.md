# Daily public evidence scan: 24 October 2026

## Finding and decision

**One newly indexed primary methods paper illustrates a boundary, not a validated tic detector.** Cif et al. was electronically published October 7 and entered PubMed October 23. Its small external pediatric cohort contained no consensus-positive tics. Better overall movement-phenotype classification therefore cannot establish sensitivity for detecting actual tics, adult Tourette performance or clinical benefit. This adjacent methods finding does not displace the separate adult-risk audit or the planned age/measurement question.

The screen also found one newly indexed case report, retained as citation metadata only, and 17 historical/previous-scan records. No new qualifying preprint, posted relevant trial result or new retraction was verified. These are bounded findings, not proof of absence.

## Scope and provenance

README, RESEARCH_PROTOCOL, STATUS, relevant evidence and public/journal-source/README were inspected at read-only repository commit `275d4cbb7386f41dc275395a11acad3a479c5a95`; [source hashes](provenance.json) identify the snapshot. No age, severity, language or human-only filter was imposed. Persistent severe adult symptoms, pain, function, co-occurring conditions and negative evidence remain within scope.

- Previous core cutoff: **2026-10-23 02:57:07.490048 UTC**.
- Current core requests: **2026-10-24 02:44:06.135112–02:45:24.341792 UTC**.
- Inclusive overlap: **October 22–24**; narrower entry-date check October 23–24. October 24 was only partly elapsed.
- Official registry supplements: **02:44:13.754846–02:44:18.512950 UTC**.
- Primary XML metadata confirmation: **02:46:02.984795–02:46:07.776625 UTC**.
- Known-retraction control: **02:46:27.677951–02:46:30.914566 UTC**.

Publication, PubMed entry/revision, preprint version, registry submission/posting and search crawl dates are distinct events. PubMed history date/time fields are retained as supplied; no unreported timezone was assigned to them.

## PubMed

Eight ESearch queries returned **28 ID occurrences and 19 unique records**, all fetched and below the 1,000-ID cap. [Exact queries/translations](search-log.json), [request timestamps and hashes](request-log.json) and [screening decisions](pubmed-screening.jsonl) are retained.

| Query family | Date field | Interval | Count |
|---|---|---|---:|
| Tourette OR “tic disorder” OR “tic disorders” | edat | October 22–24 | 3 |
| Same core | edat | October 23–24 | 1 |
| Same core | pdat | October 22–24 | 0 |
| Same core | mdat | October 22–24 | 18 |
| Core plus correction/retraction terms | edat | October 22–24 | 0 |
| tics OR chronic motor/vocal tic OR persistent tic | edat | October 22–24 | 4 |
| Same synonyms | pdat | October 22–24 | 0 |
| Core plus adult/severe/burden/comorbidity/treatment/adverse/negative terms | edat | October 22–24 | 2 |

### Adjacent primary methods evidence

[Cif et al., PMID 42908833](https://pubmed.ncbi.nlm.nih.gov/42908833/), DOI [10.3389/fneur.2026.1904458](https://doi.org/10.3389/fneur.2026.1904458), has no prior DOI/PMID reference in the searched repository text files. It is **one new evidence record**, not a new October 24 publication. [Original extraction](primary-evidence.jsonl); [official source metadata/license check](primary-source-checks.json).

The development cohort comprises **25 people: 21 affected adults and four controls**. Its 125 labeled video-derived files are repeated material from those people: 50 full-examination labels from two raters and 75 condition-specific files. External testing used 12 pediatric participants with monogenic combined movement disorders, five for clinician-selected calibration and seven held out. The 56 held-out person-by-phenotype decisions are not 56 independent participants.

Under majority reference labels, overall Hamming accuracy increased .804→.839 and Jaccard .548→.633 after calibration, with false positives increasing 2→5. But there were **zero consensus-positive tics in the external cohort**, including held-out cases. Tic sensitivity is consequently not estimable; it is neither 0% nor 100%. Negative calls do not test detection of positive tics. Under unanimous main-label rules, calibrated Jaccard was lower than baseline (.512 versus .655). Reference-label choice, selected calibration cases, small sample and domain shift matter. No patient-level uncertainty, code reanalysis, clinical outcome or treatment effect was calculated.

### Other screened records

- [PMID 42910671](https://pubmed.ncbi.nlm.nih.gov/42910671/) is an October 23 newly indexed case report about Tourettic OCD. Only title, identifiers, publication types and dates were retained; no case narrative was reviewed/extracted. PubMed gives publication year 2026 without an exact electronic date, so **new publication since cutoff remains unknown**, not established.
- The October 23 ASD and adult-persistence extractions are existing overlaps, not duplicate additions. Their measurement, adult-applicability and retrospective-timing caveats remain.
- Four records newly appearing in this overlap scan have earlier publication dates: laryngeal-dystonia research, two reviews and an August 25 MRI cohort paper assigned to a November issue. A future issue month is not future research, and an October metadata revision is not new publication. The MRI paper already had a repository discovery reference; no new extraction was added.
- Eleven other older records overlap yesterday. Historical clinical-trial labels do not establish new independent trials.

### Integrity

A separate direct PubMed control rechecked [PMID 39947542](https://pubmed.ncbi.nlm.nih.gov/39947542/) and [its retraction notice, PMID 42527169](https://pubmed.ncbi.nlm.nih.gov/42527169/). Types, reciprocal notice links and revision dates match October 23. The preclinical paper remains excluded from positive mechanism/efficacy evidence. This is not a new retraction or reinstatement. [Comparison](integrity-recheck.json).

## Preprints

Both official bioRxiv API feeds were fully paginated with stable observed totals:

| Server | DOI/version pairs | Pages | Previous bounded-feed overlap | Not in previous bounded feed |
|---|---:|---:|---:|---:|
| bioRxiv | 472 | 16 | 253 | 219 |
| medRxiv | 125 | 5 | 62 | 63 |

The title/abstract expression `\btourett\w*|\btics?\b` matched one of **597** all-subject DOI/version records. The October 22 TACTIC methods preprint uses TIC for Taxonomy-Informed Clustering, not tic disorders; it was excluded. No qualifying new preprint was verified. Other servers, unfamiliar terminology and indexing lag remain gaps. [bioRxiv index](biorxiv-preprint-index.tsv), [medRxiv index](medrxiv-preprint-index.tsv).

Web discovery also resurfaced the already-extracted September CBIT/TMS preprint; a new crawl date is not a new version. [Discovery log](discovery-log.json).

## Registries and feasibility negatives

ClinicalTrials.gov queries used server-side projection excluding outcome/result measurements, contacts, officials and locations. Tourette/tic disorder/Tics/ecopipam update queries returned **0/1/1/0**, deduplicating to NCT07137442, with no next-page token. Four direct controls were also retrieved. [Selected metadata/differences](registry-evidence.jsonl).

- [NCT07137442](https://clinicaltrials.gov/study/NCT07137442): estimated start October 27→28, posted update October 22→23, submission October 21→22. Recruiting, observational design, planned enrollment 75, eligibility ages 18–80 and no-results flag persist. Eligibility is not an observed age distribution, and planned dates do not verify actual recruitment or outcomes.
- [NCT05158439](https://clinicaltrials.gov/study/NCT05158439): unchanged withdrawal for inability to recruit, actual enrollment zero and no results. Negative feasibility is not negative efficacy or evidence of cell administration.
- [NCT07093541](https://clinicaltrials.gov/study/NCT07093541): expanded access remains temporarily unavailable without results; no new cause inferred.
- [NCT06194305](https://clinicaltrials.gov/study/NCT06194305): pediatric CBIT study remains recruiting without results on selected fields.

The ISRCTN query used tic terms with `lastEdited GE 2026-10-22T00:00:00 AND lastEdited LT 2026-10-25T00:00:00`: HTTP200, totalCount=0. An undated Tourette control returned totalCount=22, with only one control requested, not 22 reviewed. WHO ICTRP’s homepage was readable today and listed latest weekly-provider imports as October 19, but **no Tourette query export was obtained**. CTIS returned its application shell, not an interpreted trial record. These are explicit worldwide-coverage gaps, not evidence that no trials changed. [Supplementary metadata](supplement-selected-metadata.json), [WHO homepage check](who-homepage-check.json).

## Boundaries, blockers and reproducibility

No core API request failed or was denied. No operation remains pending. A local optional HTML-parser import failed before a network request; a standard-library parser completed that homepage check without installing packages. WHO query-export and CTIS-record coverage remain unverified; they were not bypassed or represented as completed. Safety/regulator checks are a separate pass.

This is a bounded update, not a systematic review or clinical advice. Source bodies/abstracts were inspected transiently where needed; only original summaries and selected metadata are retained. No patient images, videos, narratives, measurement rows, contact details or full papers are deliverables. No outreach, data request, paid compute or medical intervention occurred. The base repository was not modified or published.

```sh
python prepare_baseline.py --repo /path/to/base-checkout --out /tmp/neurofreedom-baseline.json
python scan_sources.py --baseline /tmp/neurofreedom-baseline.json --out /tmp/neurofreedom-live-scan
python build_results.py --raw /tmp/neurofreedom-live-scan/search-log.json --repo /path/to/base-checkout --out /tmp/neurofreedom-reviewed-scan
python validate_artifacts.py --repo /path/to/base-checkout
python verify_reproduction.py --repo /path/to/base-checkout
```

`scan_supplement.py`, `check_primary_sources.py` and `check_integrity_controls.py` write beside themselves; copy them to a temporary directory before live reruns. Live APIs can change; new identifiers require review. The primary extraction is an original source review, not an automatically generated clinical claim. Offline checks validate saved counts, metadata, dates, deduplication and retention boundaries, not clinical efficacy or independent peer review.

## Bounded investigation and public journal integration

The separate [adult-risk audit](../../analyses/adult_risk/2026-10-24/report.md) tests whether Kaylor's published aggregates support an outcome-specific, temporally ordered risk model. Recruitment stages and conditional rounding-compatible Table 1 denominators were computed reproducibly; the final outcome-model counts remain unknown. Retrospective/lifetime/current measurement timing prevents promotion to a prospective individual-risk or causal medication claim. The prediction, actual outputs, uncertainty, stopping rule and next decision are recorded. Thirty-five local documentation checks and 69 independent source/arithmetic checks passed; neither is clinical validation.

The [official safety and displayed-link pass](safety/report.md) found no additional qualifying watched safety notice or issued tic guideline within its documented coverage. EMA's new minutes release concerns an older meeting; a watched-drug renewal entry is not relabelled a new signal. The prior production feed was a preparation baseline. No bot challenge is called a broken link.

The dated public journal distinguishes the newly indexed older methods finding from the adult audit. Six approved activities and collection-disabled settings are preserved; hand-at-ease is the selected optional activity. Source and production verification will be recorded separately only after actual readback. No continuous execution, patient outcome, treatment change, recruitment or cure claim is implied.
