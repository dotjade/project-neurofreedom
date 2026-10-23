# Daily public evidence scan: 23 October 2026

## Finding and decision

**Two primary observational papers newly entered PubMed after the previous cutoff and were not found in the repository.** Their electronic publication dates precede that cutoff: October 20 and October 6. Both concern important comorbidity or adult-burden questions, but neither establishes treatment efficacy, a cure, prospective prediction or a universal remission trajectory. The 19-record PubMed screen otherwise found historical metadata revisions; no newly posted relevant trial result or qualifying preprint was verified.

The new adult paper supports a bounded next audit of model denominators, missingness and temporal alignment, not an unrestricted search or a new patient-data analysis. Today's separate historical-registration investigation remains separate from this scan.

## Scope, provenance and time

README, RESEARCH_PROTOCOL, STATUS, public journal source README, October 22 records and relevant evidence were inspected at repository commit `7d609957041a0a3be47fab331bf74dd838998927`. [Source hashes](provenance.json) identify the read-only snapshot.

- Prior core cutoff: **2026-10-22 03:00:44.969432 UTC**.
- Current core API scan: **2026-10-23 02:55:45.373465 to 02:57:07.490048 UTC**.
- Supplementary registry checks: **02:55:47.000305 to 02:55:52.885633 UTC**.
- Selected primary full-text confirmation requests: **02:59:31.537230 to 02:59:40.584478 UTC**.
- Inclusive overlap: **October 21–23**, with a narrower October 22–23 entry-date check. October 23 was only partly elapsed. Exact web-search brackets are in the [discovery log](discovery-log.json).

No age, severity, language or human-only filter was imposed. Adults with persistent severe symptoms, pain, function, co-occurring conditions, unmet needs and negative evidence remain in scope. Electronic publication, indexing, revision, registry posting and version dates are different events; none implies that a planned trial has actually started or reported results.

## PubMed screening

Eight ESearch queries returned **27 ID occurrences and 19 unique records**, all retrieved with EFetch and below `retmax=1000`.

| Query family | Date field | Inclusive interval | Count |
|---|---|---|---:|
| Tourette OR “tic disorder” OR “tic disorders” | edat | October 21–23 | 2 |
| Same core | edat | October 22–23 | 2 |
| Same core | pdat | October 21–23 | 0 |
| Same core | mdat | October 21–23 | 19 |
| Core plus retraction/retracted/erratum/corrigendum/correction | edat | October 21–23 | 0 |
| tics OR chronic motor/vocal tic OR persistent tic | edat | October 21–23 | 2 |
| Same synonyms | pdat | October 21–23 | 0 |
| Core plus adult/severe/pain/burden/comorbidity/treatment/adverse/negative/function terms | edat | October 21–23 | 2 |

[Exact queries and translations](search-log.json), [timestamped request metadata](request-log.json), [19 decisions and date fields](pubmed-screening.jsonl), and [two original primary extractions](primary-evidence.jsonl) are retained. PubMed entry dates for both new-to-repository studies are October 22, later than the prior cutoff; neither is a newly published-since-cutoff paper. DOI/PMID checks found no prior reference in the searched repository Markdown/JSON/JSONL/TSV files; this is not proof that the underlying cohorts never overlap other reports.

### ASD and tic measurement

[Aldurayhim et al., PMID 42902960](https://pubmed.ncbi.nlm.nih.gov/42902960/), DOI [10.1002/mdc3.70882](https://doi.org/10.1002/mdc3.70882), published October 20, analyzes first visits in Calgary child/adult registries: 535 participants aged 3–72, including 49 with ASD. It is not an adult-only sample. The adjusted ASD coefficient for tic-related impairment was −4.49 points (95% CI −8.46 to −0.51), while the severity coefficient was −0.31 (−2.91 to 2.29), not statistically significant. Outcome-model counts were 483 and 485, not 535. The authors discuss communication, classification and reporting challenges: lower measured impairment does not establish lower actual burden. Cross-sectional medication patterns are not treatment effects; referral selection and exploratory comparisons limit generalization. [Primary-source verification](primary-source-checks.json).

### Adult persistence: retrospective associations, not prospective prediction

[Kaylor et al., PMID 42903303](https://pubmed.ncbi.nlm.nih.gov/42903303/), DOI [10.3389/fpsyt.2026.1948693](https://doi.org/10.3389/fpsyt.2026.1948693), published October 6, surveys selected adults aged 26–78 from earlier genetics studies: 758 invited, 334 responding, 292 eligible for completeness, and 258 analyzed. Modified self-report YGTSS ratings concern six-month current symptoms and recalled childhood/adulthood worst periods. Fifty reused current ratings as adult-worst. Childhood-worst scores and OCD were associated with adult-worst severity; ADHD and life-event terms were nonsignificant in the multivariable severity model. The impairment-model OCD p value is printed as .050 despite significance wording. Retain that boundary rather than repairing it. Response/recall bias, diagnostic exclusions and uncertain temporal alignment prevent causal or population-persistence conclusions. Next audit outcome-specific model denominators, missingness, lifetime-versus-childhood OCD wording and whether current medication preceded the recalled outcome.

### Historical revisions and integrity

Seventeen other records have older publication dates. Two overlap yesterday's screen: the retracted preclinical paper [PMID 39947542](https://pubmed.ncbi.nlm.nih.gov/39947542/) and its [notice, PMID 42527169](https://pubmed.ncbi.nlm.nih.gov/42527169/). Selected type, linked-notice and revision fields are unchanged from October 22. The paper remains excluded from positive mechanism/efficacy evidence; this is neither a new retraction nor reinstatement. [Integrity comparison](integrity-recheck.json).

The remaining 15 are 2001–2025 publications resurfacing through revision dates, including adult neurocognitive/behavioral research, a pediatric ecopipam report, a diagnostic review and a case report. No new independent trial was inferred from indexing labels. Individual case narrative was not extracted. The full screening ledger preserves titles, IDs and exclusion reasons without republishing abstracts.

## Official preprint feeds

The bioRxiv API feeds were fully paginated for both servers within the observed interval, with stable reported totals and no core request errors:

| Server | DOI/version pairs | Pages | In previous bounded feed | Not in previous bounded feed |
|---|---:|---:|---:|---:|
| bioRxiv | 524 | 18 | 216 | 308 |
| medRxiv | 177 | 6 | 115 | 62 |

The title/abstract expression `\btourett\w*|\btics?\b` matched **two of 701** all-subject DOI/version records. Both were lexical false positives: prostate-cancer modeling uses TICs for thermodynamically infeasible cycles (DOI 10.64898/2026.06.25.734531, v2); a 16S methods paper uses TIC for Taxonomy-Informed Clustering (DOI 10.64898/2026.10.17.759814, v1). Neither is tic-disorder evidence. [bioRxiv index](biorxiv-preprint-index.tsv), [medRxiv index](medrxiv-preprint-index.tsv). Other servers, unrecognized terminology and indexing lag remain gaps.

## Registries and negative evidence

ClinicalTrials.gov used **server-side selected-field projection**, excluding result measurements, contacts, officials and locations. Tourette/tic disorder/Tics/ecopipam update queries returned **0/1/1/0**, deduplicating to NCT07137442, with no next-page token. Four direct controls were retrieved. [Selected metadata and differences](registry-evidence.jsonl).

- [NCT07137442](https://clinicaltrials.gov/study/NCT07137442): estimated start October 26→27, posting October 21→22 and submission October 20→21. Recruiting status, observational design, planned enrollment 75, eligibility ages 18–80 and no-results flag persist. Eligibility is not an observed age distribution. This is not a verified recruitment event, outcome or full amendment audit.
- [NCT05158439](https://clinicaltrials.gov/study/NCT05158439): still withdrawn for inability to recruit, actual enrollment zero and no results. Preserve negative feasibility, not negative efficacy or evidence of cell administration.
- [NCT07093541](https://clinicaltrials.gov/study/NCT07093541): expanded access remains temporarily unavailable without results. No new cause or suspension inferred.
- [NCT06194305](https://clinicaltrials.gov/study/NCT06194305): pediatric CBIT study remains recruiting without results on the selected fields.

The ISRCTN XML query used tic terms and `lastEdited GE 2026-10-21T00:00:00 AND lastEdited LT 2026-10-24T00:00:00`, returning HTTP200 and totalCount=0. An undated Tourette control returned totalCount=22, with only one control requested, not 22 reviewed. Only allowlisted metadata were retained. WHO ICTRP returned HTTP502, and a direct web retry timed out; no query export was obtained. CTIS returned its application shell, not an interpreted trial record. These are explicit worldwide-coverage gaps. [Supplementary log](supplement-selected-metadata.json).

## Limits and reproducibility

This is a bounded update, not a systematic review. Zero new trial results or preprints does not establish absence of evidence or risk. Regulator/safety checking is a separate pass. Public aggregate observations do not authorize treatment decisions. No patient rows, raw signals, private narratives, contacts, full papers or full abstracts are retained as artifacts; no outreach, recruitment, paid compute or medical action occurred.

Use the cited base checkout and run in a temporary directory; live APIs can change:

```sh
python prepare_baseline.py --repo /path/to/base-checkout --out /tmp/neurofreedom-baseline.json
python scan_sources.py --baseline /tmp/neurofreedom-baseline.json --out /tmp/neurofreedom-live-scan
python build_results.py --raw /tmp/neurofreedom-live-scan/search-log.json --repo /path/to/base-checkout --out /tmp/neurofreedom-reviewed-scan
```

`scan_supplement.py` and `check_primary_sources.py` write beside themselves: copy them to a temporary directory before live reruns. `build_results.py` requires review if new IDs appear; the two primary evidence records are original human-readable extractions, not automatically regenerated claims. `python validate_artifacts.py --repo /path/to/base-checkout` performs offline saved-metadata, deduplication, count and privacy-boundary checks. These are software/documentation checks, not clinical validation or independent peer review.
