# Daily public evidence scan: 28 October 2026

## Finding and decision

**Two older primary papers were newly retrieved: a qualitative primary-care study and a rat/cell experiment.** Neither is a newly first-published paper in this window. The care study's current publisher page identifies an October 27 version of record after July publication. A newly posted supportive-care protocol has no results. No qualifying new-window first publication, preprint or posted clinical result was verified within this bounded scan.

## Scope and dates

Required project documents, current evidence and the prior scan were inspected at `7ef323818a2a808a19e367e78ba01533fc9dce58`. [Provenance](provenance.json) records hashes. Tourette and chronic tic disorders across ages/severities, persistent severe adult symptoms, functional burden, co-occurring conditions, unmet needs and treatment response remain in scope. No age, severity or human-only filter was imposed.

- Prior core cutoff: **2026-10-27 03:15:11.950351 UTC**.
- Current core requests: **2026-10-28 02:54:37.863420–02:55:55.467615 UTC**.
- Inclusive overlap: **October 26–28**, with an October 27–28 entry-date query. Today is only partly elapsed.
- Publisher/supplementary checks occurred afterward, with their own saved timestamps.

Publication, version-of-record, entry, processing, revision and news dates differ. PubMed history times lack a verified timezone here. No precise after-cutoff indexing claim follows merely from prior search omission or a date-only field.

## PubMed

Eight queries produced **31 ID occurrences and 20 unique records**, all retrieved below the 1,000-ID cap. [Queries/translations](search-log.json), [requests](request-log.json), and [decisions](pubmed-screening.jsonl) are retained.

| Query family | Field | Interval | Count |
|---|---|---|---:|
| Tourette OR tic disorder(s) | edat | October 26–28 | 3 |
| Same core | edat | October 27–28 | 3 |
| Same core | pdat | October 26–28 | 0 |
| Same core | mdat | October 26–28 | 18 |
| Core plus correction/retraction | edat | October 26–28 | 0 |
| Tics and chronic motor/vocal/persistent tic synonyms | edat | October 26–28 | 3 |
| Same synonyms | pdat | October 26–28 | 1 |
| Core plus adult/severe/burden/comorbidity/treatment/adverse/negative terms | edat | October 26–28 | 3 |

### Newly retrieved care-experience study

[GP-TiCS, PMID 42934522](https://pubmed.ncbi.nlm.nih.gov/42934522/), [DOI 10.1186/s12875-026-03496-y](https://link.springer.com/article/10.1186/s12875-026-03496-y), reports interviews with five adults with tics, five parents, six GPs and four secondary-care professionals in England. Themes concern education, service access/referrals, communication, stigma and recognition of wider burden. These 20 selected interviewees do not estimate population prevalence or establish that a planned educational resource improves care. Persistent-severe-adult and communication-group effects are not identified. No quotations or personal narratives were extracted.

PubMed and current publisher metadata give **July 30** online publication. Direct publisher HTML identifies **October 27 version of record**; an earlier web-reader snapshot still displayed an accepted-version disclaimer. Exact posting time and substantive version differences were not verified. This is a version/indexing update for an older study, not an entirely new first publication. [Selected publisher metadata](gptics-publisher-metadata.json), [independent source review](primary-independent-review.json).

### Newly retrieved preclinical study

[PMID 42943225](https://pubmed.ncbi.nlm.nih.gov/42943225/), [DOI 10.3390/ph19101529](https://doi.org/10.3390/ph19101529), was published **September 26**, with October 27 indexing. The abstract describes 72 allocated juvenile rats, a 28-day intervention and a separate BV2-cell TREM2 knockdown experiment. Reported behavioral and lipid/inflammatory changes remain preclinical. Cell perturbation adds more than correlation alone, but serum-associated reversal does not establish target necessity/sufficiency in people. Background claims of clinical effectiveness are not human results of this experiment. Outcome-specific denominators, precision, blinding, attrition and systematic safety were not verified. No human dose or treatment inference is made. [Original extractions](primary-evidence.jsonl).

### Other records and integrity

Nine records overlap yesterday; eleven are absent from that day's set, not necessarily new to the project. The food-IgG paper [PMID 42818614](https://pubmed.ncbi.nlm.nih.gov/42818614/) was explicitly deferred on October 9 and is not added again. Its retrospective association rules do not establish allergy diagnosis, dietary tic treatment or a reason to restrict food. The safety review separately checks authoritative guidance.

Other older reports cover pregnancy, adult psychiatric burden, pediatric developmental/treatment patterns, rage, functional tic-like behaviors and secondary reviews. Shared registry cohorts are not independent replications, and medication-use patterns are not randomized efficacy. One case report remains citation metadata only, with exact publication date unknown. Two new-search records are acronym collisions: toxic industrial chemicals and MRI time-intensity curves, not tics. The adjacent misophonia study is not a tic-treatment trial.

Known retracted paper [PMID 39947542](https://pubmed.ncbi.nlm.nih.gov/39947542/) and [notice 42527169](https://pubmed.ncbi.nlm.nih.gov/42527169/) retain unchanged selected metadata and reciprocal links. They remain excluded from positive evidence. [Integrity check](integrity-recheck.json).

## Preprints

Official bioRxiv API feeds were fully paginated with stable observed totals. Title/abstract screening using `\btourett\w*|\btics?\b` found **zero lexical matches among 581 DOI/version records**.

| Server | Records | Pages | Prior overlap | Not in prior bounded feed |
|---|---:|---:|---:|---:|
| bioRxiv | 443 | 15 | 140 | 303 |
| medRxiv | 138 | 5 | 118 | 20 |

Only DOI/version/date indexes are retained. Other servers, terminology, indexing delays and dynamic pagination remain limits; no preprint is promoted to peer-reviewed evidence.

## Official registries

ClinicalTrials.gov update queries returned **1, 3, 3 and 0**, deduplicating to three IDs with no next-page tokens. Server projection excluded participant measurements/results, contacts, officials and locations. [Selected records](registry-evidence.jsonl).

- [NCT07898592](https://clinicaltrials.gov/study/NCT07898592): first posted October 27, not yet recruiting, planned 50 adult parent participants, single-group supportive-care protocol across neurodevelopmental conditions including motor tic disorders. Planned dates and broad eligibility do not establish enrollment, tic-specific efficacy or a result.
- [NCT07137442](https://clinicaltrials.gov/study/NCT07137442): October 27 posting moves estimated start October 29 to November 1; planned 75 and no results remain. This is a date change, not observed recruitment or efficacy.
- [NCT01019343](https://clinicaltrials.gov/study/NCT01019343): selected fields unchanged; historical mixed-diagnosis physiology study, not a newly completed Tourette trial.
- Three other controls are unchanged: [NCT05158439](https://clinicaltrials.gov/study/NCT05158439) remains withdrawn for inability to recruit with zero enrollment, a feasibility negative rather than efficacy result; [NCT07093541](https://clinicaltrials.gov/study/NCT07093541) remains expanded access temporarily unavailable; [NCT06194305](https://clinicaltrials.gov/study/NCT06194305) remains recruiting pediatric CBIT without results in selected fields.

Discovery search's third-party October 27 synchronization for [NCT05558566](https://clinicaltrials.gov/study/NCT05558566) was checked against official metadata: last update June 9, no results. Synchronization is not a registry amendment. [Check](discovery-registry-check.json).

ISRCTN's October 26–28 edited-date query returned zero; positive control total was 22, with one requested record, not all 22 reviewed. WHO's homepage was readable but no Tourette query export obtained. CTIS returned an application shell, not parsed trial data. [Supplement metadata](supplement-selected-metadata.json). Worldwide registration coverage remains incomplete.

## Access, reproducibility and limits

All **37 core requests** succeeded. Publisher access for the rat/cell source returned HTTP 429 in the web reader, which is rate limiting rather than an established broken link; the official PubMed abstract was accessible. No full methods/supplements were extracted. No source papers, abstracts, individual/family narratives, participant rows or private data are deliverables. No outreach, recruitment, paid compute or medical action occurred.

Thirty-two offline metadata/date/privacy checks passed and seven normalized outputs reproduced byte-for-byte. These are software/documentation checks, not clinical validation. Future API responses may change and new IDs or registry fields require review.

```sh
python updates/2026-10-28/prepare_baseline.py --repo . --out /tmp/day28-baseline.json
python updates/2026-10-28/scan_sources.py --baseline /tmp/day28-baseline.json --out /tmp/day28-live
python updates/2026-10-28/build_results.py --raw /tmp/day28-live/search-log.json --repo . --out /tmp/day28-reviewed
python updates/2026-10-28/validate_artifacts.py --repo .
python updates/2026-10-28/verify_reproduction.py --repo .
```

Copy supplement/integrity scripts to temporary storage before live reruns because they write beside themselves. The bounded investigation, safety/link review and homepage integration are documented separately. Publication requires later exact GitHub/live-feed readback, not local preparation alone.


## Bounded investigation and public journal

The [Ho informant-agreement audit](../../analyses/informant_agreement/2026-10-28/report.md) advances the latest plan through source reconciliation and deterministic published-aggregate checks. It preserves positive discrimination, masking and clustered analysis while distinguishing category accuracy from continuous-score interchangeability, repeated assessments from patients, and practice associations from causal training benefit. There are 196 discordant assessments, not 196 established distinct people. Conditional triangle bounds show why the reported score differences are not automatically contradictory. Eleven implementation tests and 29 independent checks pass, not clinical peer review. No participant scores, new confidence intervals or biological mechanisms were reconstructed.

The [safety/link pass](safety/report.md) identifies a new MHRA communication of an older diagnostic interaction, corroborated in earlier FDA records. It is not a new tic-treatment safety discovery. Authoritative food-IgG interpretation safeguards are retained without diet or medication changes. All six approved activities remain unchanged, small-silly-mark is selected, and collection stays disabled. The feed separates older studies, registry metadata and historical analysis from new clinical results. Final publication requires the later exact source/live receipt.
