# Daily evidence scan: 31 October 2026

## Result and decision

**No qualifying new-window first publication, preprint or posted clinical-trial result was verified in this bounded scan.** One older primary paper is newly retrieved: an October 20 postmortem, mixed-diagnosis histamine-expression pilot. A new adolescent resilience feasibility protocol was first posted October 30. Neither establishes an effective treatment, a Tourette-specific mechanism or a cure.

[PMID 42956657](https://pubmed.ncbi.nlm.nih.gov/42956657/), DOI [10.1016/j.psychres.2026.117545](https://doi.org/10.1016/j.psychres.2026.117545), reports higher HRH3 transcript expression in a pooled OCD/OCPD/tic-Tourette DLPFC group versus controls: η²=0.035, p=0.033, BF10=2.96. Other histamine-pathway genes did not survive multiplicity correction; HRH4's exploratory BF10=1.20 is weak evidence. This is a bulk-tissue association, not receptor-function measurement or a validated treatment target. No TS-specific estimate, sample size, age range, coefficient interval or Bayesian prior was available in the inspected abstract. [Original cautious extraction](primary-evidence.jsonl).

The primary paper was published October 20, not after yesterday's cutoff. Its October 29 indexing metadata was absent from yesterday's bounded retrieval. This discrepancy illustrates why search appearance, indexing and publication must remain separate; no exact indexing-delay explanation is established.

## Scope, dates and coverage

Required repository instructions, status and evidence were read at baseline `8b9fd54ff445e8f5e74ffffa48f49a80ad36990b`. [Versioned input hashes](provenance.json).

- Previous verified core cutoff: **2026-10-30 02:51:17.233943 UTC**.
- Current core: **2026-10-31 03:26:19.771888 to 03:27:38.991962 UTC**.
- Inclusive overlap: **October 29–31**, with a narrower October 30–31 entry-date query.
- All **41 core API requests** succeeded. Supplement/control and selected-source requests have separate actual timestamps.

Scope is all ages/severities, including chronic motor/vocal tics, persistent severe adult symptoms, functional burden, comorbidity, unmet needs and treatment response. No age, severity or human-only filter was imposed. October 31 is partly elapsed. PubMed history timezones were not independently verified, so date-only/indexing timestamps do not establish precise UTC sequence.

## PubMed and source classification

Eight queries produced **32 ID occurrences, 24 unique records**, with every returned ID fetched below the cap. Twelve overlap the previous daily scan; twelve are absent from that scan, not necessarily new research. [Exact translated queries](search-log.json), [request times/status/hashes](request-log.json), [record-level screening and baseline repository matches](pubmed-screening.jsonl).

| Query | Date field | Count |
|---|---|---:|
| Tourette / tic disorder core | Entry, October 29–31 | 3 |
| Same core | Entry, October 30–31 | 0 |
| Same core | Publication | 0 |
| Same core | Modification | 22 |
| Core plus correction/retraction words | Entry | 2 |
| Tics / persistent / chronic motor or vocal synonyms | Entry | 2 |
| Same synonyms | Publication | 1 |
| Core plus adult/burden/comorbidity/treatment/negative terms | Entry | 2 |

- The two correction-query hits, 42956657 and 42952789, concern statistical correction, **not correction notices**. Neither has a linked notice in fetched metadata.
- The historically revised consensus article [34817664](https://pubmed.ncbi.nlm.nih.gov/34817664/) links to [erratum 40111559](https://pubmed.ncbi.nlm.nih.gov/40111559/), electronically published March 20, 2025. It is not a new notice or a new treatment finding. Correction content was not independently audited beyond official linkage/date.
- Known retracted source [39947542](https://pubmed.ncbi.nlm.nih.gov/39947542/) and notice [42527169](https://pubmed.ncbi.nlm.nih.gov/42527169/) retain unchanged selected metadata and are excluded from positive evidence. [Control comparison](integrity-recheck.json).
- [42956658](https://pubmed.ncbi.nlm.nih.gov/42956658/), electronically October 23, is a pediatric executive-function/comorbidity **systematic review**, not independent primary participants. Its abstract describes 30 studies, narrative synthesis, and differing performance-based versus everyday-report findings. ADHD-related symptoms were consistent correlates of functional difficulties, but this does not establish causation or adult validity. [Secondary-only record](secondary-evidence.json).
- Historical mouse, clinical-characterization, consensus, prevalence and treatment papers retain their original evidence types. The October 1 TMS/CBIT paper 42856611 remains a **preprint**, already extracted, not a new peer-reviewed trial. MRI time-intensity curves (41927332) and telephone cognitive-status TICS (42957926) are acronym collisions. No individual narratives, videos or source abstracts are retained.

## Preprints

Screening of titles and abstracts with `\btourett\w*|\btics?\b` found **zero lexical matches among 684 DOI/version records**. Both servers reached their observed final page with stable totals during retrieval.

| Server | DOI/versions | Pages | Prior overlap | Absent from previous bounded feed |
|---|---:|---:|---:|---:|
| bioRxiv | 521 | 18 | 209 | 312 |
| medRxiv | 163 | 6 | 97 | 66 |

[Version indexes](biorxiv-preprint-index.tsv) and [medRxiv index](medrxiv-preprint-index.tsv) retain citation dates/identifiers only. This is not every preprint server or a permanent snapshot. Relevant papers with different vocabulary or delayed indexing may be missed. A DOI/version absent yesterday is not automatically a new first publication.

## Official registries

ClinicalTrials.gov counts were **1, 2, 2 and 0** across Tourette, tic disorder, Tics and ecopipam update-window queries, yielding **two unique IDs** without pagination. Four direct control requests bring the selected comparison set to five records, all without posted results. [Registry selected-field comparisons](registry-evidence.jsonl).

### New supportive-care protocol, not efficacy evidence

[NCT07905898](https://clinicaltrials.gov/study/NCT07905898), PRISM-TS, was first posted October 30 and remains **not yet recruiting**. It concerns ages 12–18, adaptation and feasibility of resilience support alongside usual care. The 60-person pilot phase is randomized 1:1, with matched check-ins in usual care and blinded outcome assessment. The primary endpoints are feasibility; tic severity, separate impairment and other functional/psychiatric outcomes are secondary. No benefit or clinical safety estimate exists yet.

The top-level enrollment field says **95**, whereas the detailed text says **85 adolescents**: 10 adaptation, 15 open trial and 60 randomized pilot. Caregivers are mentioned, but the source does not explicitly reconcile the 10-person difference. **Do not describe 95 randomized adolescents or silently repair the denominator.** [Protocol interpretation and request provenance](prism-protocol-summary.json). This is not persistent-severe-adult validation, a recruitment recommendation or permission for contact.

### Controls and metadata changes

- [NCT07137442](https://clinicaltrials.gov/study/NCT07137442): October 30 posting moves estimated start November 3 to November 4. Planned n=75 and no results persist. Estimates are not observed recruitment dates or scientific findings.
- [NCT07093541](https://clinicaltrials.gov/study/NCT07093541): expanded access still no longer available. No reason or safety cause inferred.
- [NCT05158439](https://clinicaltrials.gov/study/NCT05158439): withdrawn for recruitment inability, actual n=0, unchanged. Negative feasibility is not negative efficacy.
- [NCT06194305](https://clinicaltrials.gov/study/NCT06194305): recruiting pediatric CBIT protocol without results, unchanged.

ISRCTN returned zero in the October 29 inclusive to October 31 exclusive modification window; its positive control returned 22 total with one record requested. This excludes October 31 changes. WHO ICTRP homepage access did not yield a current query export, and CTIS returned a shell rather than a parsed trial. HTTP success is not comprehensive registry coverage. [Supplement limits](supplement-selected-metadata.json).

## Reproduction and next step

From repository root:

```sh
python updates/2026-10-31/scan/prepare_baseline.py --repo . --out /tmp/nf-baseline.json
python updates/2026-10-31/scan/scan_sources.py --baseline /tmp/nf-baseline.json --out /tmp/nf-live
python updates/2026-10-31/scan/build_results.py --raw /tmp/nf-live/search-log.json --repo . --out /tmp/nf-normalized
python updates/2026-10-31/scan/validate_artifacts.py --repo .
```

The baseline reconstruction matched the input exactly. **42 consistency/data-minimization checks passed.** Live APIs can change; the normalizer rejects unreviewed source sets and new preprint hits. Supplement/control scripts write alongside themselves and should be run in a temporary copy rather than overwriting this dated record. These are metadata checks, not clinical validation.

Keep the older HRH3 observation as a limited hypothesis lead. Before any TS-specific or target-level interpretation, obtain lawful participant-free methods/aggregate output specifying sample and diagnostic counts, age, dataset/cohort overlap, covariates, coefficient/interval and Bayesian prior. No underlying participant dataset or author contact was accessed. Parent integration advances the separately selected force-matching question and handles safety findings. This scan alone does not establish absence of all safety issues.
