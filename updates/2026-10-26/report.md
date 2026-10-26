# Daily public evidence scan: 26 October 2026

## Finding and decision

**One earlier preclinical paper was newly encountered, not verified as a new publication since the prior cutoff.** The October 24 rat-model study reports treatment-associated behavioral and molecular changes; its abstract explicitly leaves C1qa causality unresolved. Neither human efficacy nor human safety follows. No qualifying new-window primary publication, preprint, posted trial result or retraction was verified within this bounded scan. This is not absence of new evidence worldwide.

## Scope and provenance

Required repository documents and prior evidence were read at baseline `1dafa0fdb06d4f08ba13f281bc866c3b5f58b170`; [provenance hashes](provenance.json) identify the inputs. Tourette and chronic tic disorders across ages/severities, persistent severe adult symptoms, function, pain, co-occurring conditions and treatment needs remain in scope. No age, severity or human-only search filter was imposed. Animal findings are not clinical evidence, and pediatric data are not silently extrapolated to adults.

- Prior core cutoff: **2026-10-25 02:46:02.904884 UTC**.
- Current core requests: **2026-10-26 02:58:52.222699–02:59:34.225370 UTC**.
- Inclusive overlap: **October 24–26**; narrower entry-date check October 25–26. October 26 is only partly elapsed.
- Official registry supplements: **02:58:58–02:59:20 UTC**.

Publication, Entrez entry, PubMed processing, revision and registry posting are distinct. History fields lack a verified timezone in this review. Search omission cannot prove a later indexing event.

## PubMed

Eight ESearch queries produced **14 ID occurrences and 10 unique records**, all fetched below the 1,000-ID cap. [Queries/translations](search-log.json), [request timestamps and hashes](request-log.json) and [individual decisions](pubmed-screening.jsonl) are saved.

| Query family | Field | Date interval | Count |
|---|---|---|---:|
| Tourette OR tic disorder(s) | edat | October 24–26 | 1 |
| Same core | edat | October 25–26 | 1 |
| Same core | pdat | October 24–26 | 1 |
| Same core | mdat | October 24–26 | 9 |
| Core plus correction/retraction | edat | October 24–26 | 0 |
| Tics and chronic motor/vocal/persistent tic synonyms | edat | October 24–26 | 1 |
| Same synonyms | pdat | October 24–26 | 0 |
| Core plus adult/severe/burden/comorbidity/treatment/adverse/negative terms | edat | October 24–26 | 1 |

### Newly encountered preclinical evidence

[Li et al., PMID 42925937](https://pubmed.ncbi.nlm.nih.gov/42925937/), [DOI 10.1016/j.jep.2026.122551](https://doi.org/10.1016/j.jep.2026.122551), studied an IDPN-induced TS-like model in male rats. The abstract describes seven randomized groups, ten rats allocated per group, and four weeks of botanical-formulation administration. It reports a 51% reduction in stereotypy versus the model group (p<.001), alongside molecular changes. Outcome-specific denominators and confidence intervals were not verified.

The title makes stronger mechanistic claims than the abstract's conclusion, which leaves C1qa causality unresolved. Treatment-associated markers do not prove mediation. A toxicant model's stereotypy is not human tic disability, quality of life, or durable disease modification. Human safety is untested here; full-methods blinding, attrition, multiplicity and harms require verification. No dose translation or self-treatment recommendation is made. [Original extraction](primary-evidence.jsonl), [independent abstract check](preclinical-independent-review.json).

Electronic publication and Entrez history are dated October 24, before the prior cutoff. PubMed history is October 25 at 03:36, but its timezone is unverified; new indexing after the previous scan is therefore not asserted. This paper was absent from the prior repository snapshot. Novel retrieval is not the same as novel science.

### Remaining metadata and integrity

Four records overlap the prior scan: adult persistence, CHD/Tourette, cortical morphology and a secondary review. The CHD table/prose discrepancy and adult-risk limitations remain unchanged. Six IDs were absent from that day's bounded result set, not necessarily absent from all earlier research. The 2025 chronic-pain study was already cited in the project's pain-audit provenance; an October 24 revision is not a new publication. Other old records include a pediatric tic/functional-tic comparison, a cervical-dystonia trial and Parkinson hospital-care review. They were not added as new tic-treatment evidence.

The October 23 PANDAS case series [PMID 42921162](https://pubmed.ncbi.nlm.nih.gov/42921162/) is retained as citation metadata only, without clinical narratives or individual/family details. It is not controlled Tourette-treatment evidence. Secondary publicity dated October 25 does not change its primary publication date.

Known retracted preclinical paper [PMID 39947542](https://pubmed.ncbi.nlm.nih.gov/39947542/) and [notice 42527169](https://pubmed.ncbi.nlm.nih.gov/42527169/) retain unchanged reciprocal linkage and selected metadata. They remain excluded from positive evidence. [Integrity comparison](integrity-recheck.json).

## Preprints

Official bioRxiv API pages were fully paginated with stable observed totals. Title/abstract lexical screening with `\btourett\w*|\btics?\b` found **zero matches among 321 DOI/version records**.

| Server | Records | Pages | Prior overlap | Not in prior bounded feed |
|---|---:|---:|---:|---:|
| bioRxiv | 246 | 9 | 159 | 87 |
| medRxiv | 75 | 3 | 69 | 6 |

Other servers, alternate terminology, indexing lag and dynamic pagination remain limitations. No preprint was promoted to peer-reviewed evidence. Indexes contain DOI/version/date only; abstracts were not retained.

## Registries

Four ClinicalTrials.gov update-window queries returned zero records, without next-page tokens. Four direct controls were retrieved with server projection excluding results measurements, contacts and locations. Selected status/design/result flags are unchanged versus October 25. [Registry records](registry-evidence.jsonl).

- [NCT05158439](https://clinicaltrials.gov/study/NCT05158439): withdrawn for inability to recruit, actual enrollment zero, no results. Negative feasibility, not negative efficacy.
- [NCT07093541](https://clinicaltrials.gov/study/NCT07093541): expanded access remains temporarily unavailable; no new reason inferred.
- [NCT06194305](https://clinicaltrials.gov/study/NCT06194305): pediatric CBIT study remains recruiting with no results in selected fields.
- [NCT07137442](https://clinicaltrials.gov/study/NCT07137442): observational protocol, planned 75 participants ages 18–80, estimated October 28 start, no results. Eligibility is not observed population, and planned dates are not proof of actual recruitment.

ISRCTN's October 24–26 edited-date window returned zero. Its positive control returned total 22, with only one requested record, not all 22 reviewed. WHO's homepage remained readable, listing October 19 among import dates, but no Tourette query export was obtained. CTIS returned an application shell, not parsed trial data. Worldwide registration coverage is incomplete. [Supplement metadata](supplement-selected-metadata.json).

## Access, reproducibility and boundaries

All **29 core requests** succeeded. Web-reader PubMed/DOI routes for the new preclinical source failed, while official PubMed API abstract retrieval succeeded. These are access limitations, not proven broken links. Full text/supplements were not reviewed. No participant rows, source full text, case narratives, private data, outreach, paid compute or intervention were retained or performed.

```sh
python updates/2026-10-26/prepare_baseline.py --repo . --out /tmp/day26-baseline.json
python updates/2026-10-26/scan_sources.py --baseline /tmp/day26-baseline.json --out /tmp/day26-live-scan
python updates/2026-10-26/build_results.py --raw /tmp/day26-live-scan/search-log.json --repo . --out /tmp/day26-reviewed
python updates/2026-10-26/validate_artifacts.py --repo .
python updates/2026-10-26/verify_reproduction.py --repo .
```

The normalization script rejects unreviewed IDs/registry changes; future live results may differ. Supplement/integrity scripts write beside themselves: copy them to a temporary directory before a live rerun. Thirty offline metadata/date/privacy checks passed, and seven normalized outputs reproduced byte-for-byte. These checks verify documentation/software, not clinical findings. The new title-based case-report/series guard avoids relying solely on incomplete publication-type indexing.

The separate bounded YGTSS investigation, safety/link review and homepage integration are owned by the integrating researcher. Publication is only established by the later GitHub and live-feed receipt, not by this scan.


## Bounded investigation and public journal

The [YGTSS validation audit](../../analyses/ygtss_validation/2026-10-26/report.md) advances the latest plan using the original 2018 multicenter study, not a newly published paper. Pooled internal consistency does not establish ASD/communication-group equivalence; interrater and test-retest reliability across sites were not tested, and proposed revised anchors were not prospectively validated here. Neither measurement bias nor its absence is established. Adult sample representation, impairment and negative age comparisons remain distinct from persistent-severe-adult validity or equivalence. Seven implementation tests and 20 independent checks passed; these are software/source checks, not clinical peer review.

The [safety/link report](safety/report.md) records no qualifying new notice within its official-source coverage and retains access limits. All six approved activities and disabled collection are unchanged; notice-one-thing is the dated optional selection. The public note distinguishes the older preclinical source from new-window evidence. Final publication is established only by the later exact GitHub and production readback receipt.
