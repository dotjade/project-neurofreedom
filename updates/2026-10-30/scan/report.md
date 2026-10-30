# Daily evidence scan: 30 October 2026

## Result and decision

**No qualifying new first-publication, posted trial result or preprint was verified after the previous cutoff within this bounded coverage.** An older October 14 pediatric immune/vitamin association was newly retrieved and is added as observational evidence, not a treatment discovery. A registry's estimated start moved by one day; no result or efficacy implication follows.

The newly retrieved [primary paper, PMID 42952789](https://pubmed.ncbi.nlm.nih.gov/42952789/), DOI [10.3389/fpsyt.2026.1903047](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2026.1903047/full), has important negative evidence: vitamin associations fail the primary multiplicity correction. Its outcome combines tic severity and impairment, and its short-duration pediatric sample cannot establish a persistent severe adult mechanism. [Selected aggregate extraction](primary-evidence.jsonl). Cross-sectional immune association does not justify supplementation, immune treatment, causal prediction or a patient-specific interpretation.

## Scope and provenance

Required README, protocol, status, evidence and journal-source README were inspected at baseline `e324b6d369652b9a280faf8b318d9321fd2d4dcb`. [Hashes and inputs](provenance.json).

- Previous daily core cutoff: **2026-10-29 03:16:14.716688 UTC**.
- Current core: **2026-10-30 02:49:31.632934–02:51:17.233943 UTC**.
- Inclusive overlapping dates: **October 28–30**, with a narrower entry-date query October 29–30. Today is only partly elapsed.
- All **43 core requests succeeded**. Supplementary registry retrieval ran 02:49:46–02:49:54 UTC. Discovery checks are separately dated.

No age, severity or human-only filters were imposed. Scope includes persistent severe adults, chronic motor/vocal tics, functional burden, co-occurring conditions, unmet needs and treatment response, without assuming remission. Indexing, revision, publication and publicity are different events. PubMed history timezone was not independently verified; date-only indexing is not a precise UTC ordering claim.

## PubMed and deduplication

Eight queries returned **37 ID occurrences and 22 unique records**. Every ID was fetched below the 1,000-record cap. Twelve overlap yesterday; ten are absent from that day's search, not necessarily new to the repository or science. [Exact queries/translations](search-log.json), [request dates/status/hashes](request-log.json), [record-level screening and baseline repository matches](pubmed-screening.jsonl).

| Query | Date field | Count |
|---|---|---:|
| Tourette / tic disorder core | Entry, October 28–30 | 4 |
| Same core | Entry, October 29–30 | 1 |
| Same core | Publication | 2 |
| Same core | Modification | 22 |
| Core plus correction/retraction terms | Entry | 1 |
| Tics / chronic motor or vocal / persistent synonyms | Entry | 2 |
| Same synonyms | Publication | 1 |
| Core plus adult / burden / comorbidity / treatment / negative terms | Entry | 4 |

The correction-query hit is the immune/vitamin paper's statistical-correction language, **not a correction notice**. No linked correction/retraction was present in its official metadata. Known retracted source [39947542](https://pubmed.ncbi.nlm.nih.gov/39947542/) and notice [42527169](https://pubmed.ncbi.nlm.nih.gov/42527169/) retain unchanged reciprocal linkage and remain excluded from positive evidence. [Control comparison](integrity-recheck.json).

The other recent-indexed article, [PMID 42951691](https://pubmed.ncbi.nlm.nih.gov/42951691/), DOI 10.1111/sjop.70154, is electronically dated October 28, before the prior cutoff. It studies ADHD presentations in an Icelandic clinical sample, with tic/Tourette comorbidity reported similarly prevalent between groups. It is adjacent evidence, not a tic-treatment study; a nonsignificant comparison does not establish equivalence. No detailed family or individual information was retained.

Older revised records include pediatric sex differences, prevalence/comorbidity, dystonic-tic characterization, a small oral-orthotic pilot, a cannabis systematic review, unrelated-condition studies and historical biography. The orthotic pilot's nonreplicated follow-up difference remains a limitation, not a recommendation. The October 1 TMS/CBIT trial, [42856611](https://pubmed.ncbi.nlm.nih.gov/42856611/), was already extracted on October 12 and is not duplicated. Prior adult sensory attenuation, GP-TiCS, preclinical and developmental studies retain their original limitations.

## Preprints

Title/abstract lexical screening used `\btourett\w*|\btics?\b`. No lexical hits were found among **764 DOI/version records**, deduplicated within each server. No source abstracts were saved.

| Server | Records | Pages | Prior overlap | Absent from prior bounded feed |
|---|---:|---:|---:|---:|
| bioRxiv | 561 | 19 | 335 | 226 |
| medRxiv | 203 | 7 | 106 | 97 |

Both returned stable totals during this observed retrieval and reached the reported end. This is not a permanent snapshot, proof against indexing delays or a search of every preprint server. Lexical screening may miss relevant work using other terminology. New-to-feed versions are not all new publications. [bioRxiv index](biorxiv-preprint-index.tsv), [medRxiv index](medrxiv-preprint-index.tsv).

## Official registries

ClinicalTrials.gov update-window query counts were **2, 3, 3 and 1**, yielding three unique update-window IDs and no next-page token. Direct controls bring the selected comparison set to **five records, all without posted results**. [Selected metadata and exact differences](registry-evidence.jsonl).

- [NCT07137442](https://clinicaltrials.gov/study/NCT07137442): October 29 posting moves estimated start November 2 to November 3. Planned enrollment 75, recruiting status and no results remain. Estimates are not observed recruitment dates or scientific findings.
- [NCT07093541](https://clinicaltrials.gov/study/NCT07093541): expanded access remains no longer available, unchanged. No reason or safety cause is inferred.
- [NCT07854665](https://clinicaltrials.gov/study/NCT07854665): pediatric taVNS protocol remains not yet recruiting, planned 124, no results. It is not adult efficacy evidence.
- [NCT05158439](https://clinicaltrials.gov/study/NCT05158439): withdrawal for inability to recruit, actual zero, remains negative feasibility rather than negative efficacy.
- [NCT06194305](https://clinicaltrials.gov/study/NCT06194305): pediatric CBIT control remains recruiting without results.

ISRCTN returned zero in the October 28 inclusive to October 30 exclusive modification window; its positive control reports 22 total with one record requested. This supplement does not cover October 30 changes. WHO ICTRP homepage was readable but no current query export was obtained. CTIS returned an application shell, not a parsed trial record. HTTP success is not full registry coverage. [Supplement log](supplement-selected-metadata.json).

## Reproduction, limits and next decision

Run from the repository root:

```sh
python updates/2026-10-30/scan/prepare_baseline.py --repo . --out /tmp/neurofreedom-baseline.json
python updates/2026-10-30/scan/scan_sources.py --baseline /tmp/neurofreedom-baseline.json --out /tmp/neurofreedom-live
python updates/2026-10-30/scan/build_results.py --raw /tmp/neurofreedom-live/search-log.json --repo . --out /tmp/neurofreedom-normalized
python updates/2026-10-30/scan/validate_artifacts.py --repo .
python updates/2026-10-30/scan/verify_reproduction.py --repo .
```

Live endpoints may change; normalization refuses unreviewed IDs. Re-run supplement/control scripts in a temporary copy to avoid overwriting the dated snapshot. **34 consistency/privacy-boundary checks passed; seven saved outputs reproduced byte-for-byte.** These are metadata checks, not clinical validation. No simulation, individual data or causal computation is represented by this scan.

This is a bounded evidence update, not exhaustive surveillance or reassurance that no safety issue exists. Parent integration handles the independent safety scan and the planned adult sensory-methods audit. Keep the older immune/vitamin finding separate from new-window discoveries; prioritize temporality, score identity and primary versus exploratory testing in any later synthesis. No treatment change, contact, recruitment or data collection is proposed.
