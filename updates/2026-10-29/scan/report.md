# Daily evidence scan: 29 October 2026

## Meaningful findings

A newly retrieved **October 28 adult force-matching study** reports reduced sensory attenuation associated with tic severity. This differs from the older paired-air-puff sensory-gating study, whose null gating finding remains. It does not establish causation, a universal tic trigger or a validated predictive biomarker.

The ecopipam expanded-access registry changed to **no longer available** in an October 28 posting. No reason, safety cause or efficacy implication is inferred. No newly posted trial result or qualifying preprint was verified within this bounded coverage.

## Scope and baseline

Required documents, evidence and the October 28 daily scan were inspected at `4dcd1aeaa9c31ec4912a1f19b6e6d51946a08951`. The later October 28 causal synthesis is not substituted for the last daily scan. [Provenance](provenance.json).

- Prior core cutoff: **2026-10-28 02:55:55.467615 UTC**.
- Current core interval: **2026-10-29 03:13:25.510089–03:16:14.716688 UTC**.
- Inclusive dates: **October 27–29**; narrower entry-date check October 28–29. Today is partly elapsed.
- A five-request medRxiv recovery ran during that interval after a first-attempt HTTP 503. The failed attempt is preserved.

Scope includes all ages/severities, persistent severe adults, functional burden, co-occurring conditions, unmet needs and treatment response. No age, severity or human-only filters were imposed. Publication, indexing, revision and publicity dates differ. PubMed history times have no verified timezone here.

## Primary paper

[Reduced Sensory Attenuation Scales with Tic Severity in Tourette Syndrome](https://pubmed.ncbi.nlm.nih.gov/42947547/), PMID 42947547, DOI [10.1002/mds.70590](https://doi.org/10.1002/mds.70590), is electronically dated October 28. Exact within-day publication time is unavailable, so ordering after the previous early-day UTC cutoff is not proven. It was absent from the baseline search and repository.

The abstract describes **30 adults with TS and 30 controls** reproducing forces directly or indirectly. Adults with TS overestimated less in the direct condition, interpreted as reduced attenuation. The indirect condition showed no group difference. Attenuation related to current YGTSS tic severity beyond medication load, obsessive-compulsive symptoms and urge severity.

Numeric effects, intervals, model completeness and a formal group-by-condition interaction are not available in the verified abstract. Significance in one condition and nonsignificance in another do not establish an interaction. Concurrent explained variance is not future prediction; residual confounding and reverse causation remain. The authors' first-direct-evidence wording is not independently verified novelty. No severe-persistent subgroup, clinical calibration or intervention effect is established. [Original extraction](primary-evidence.jsonl), [independent check](../primary-independent-review.json).

The [September 29 air-puff study, PMID 42810670](https://pubmed.ncbi.nlm.nih.gov/42810670/) concerns repeated externally delivered touch, not self-generated force. October 28 Vanderbilt publicity does not make it a new study or provide the previously missing numerical tables. Retain its gating null and distinguish smaller first-stimulus P50 from impaired gating. These endpoints cannot be pooled as interchangeable measures.

## PubMed search

Eight queries returned **40 ID occurrences, 22 unique records**. All IDs were fetched below the 1,000-ID cap. Fifteen overlap yesterday; seven are absent from that day's result set, not necessarily new to science. [Queries/translations](search-log.json), [requests](request-log.json), [decisions](pubmed-screening.jsonl).

| Query family | Field | Dates | Count |
|---|---|---|---:|
| Tourette OR tic disorder(s) | edat | October 27–29 | 5 |
| Same core | edat | October 28–29 | 2 |
| Same core | pdat | October 27–29 | 1 |
| Same core | mdat | October 27–29 | 20 |
| Core plus correction/retraction | edat | October 27–29 | 0 |
| Tics/chronic motor/vocal/persistent synonyms | edat | October 27–29 | 5 |
| Same synonyms | pdat | October 27–29 | 2 |
| Core plus burden/comorbidity/treatment/negative terms | edat | October 27–29 | 5 |

The other newly retrieved recent-indexed article is a July 8 DBS perspective, [PMID 42949677](https://pubmed.ncbi.nlm.nih.gov/42949677/), classified as a review, not a clinical trial or demonstrated target. The remaining new-to-day records are older population, adjacent-condition, outcome-measure or secondary reports. Prior GP-TiCS, preclinical, food-IgG and adult-burden limitations are retained. Acronym collisions and adjacent misophonia evidence are excluded from tic-treatment conclusions. No personal narratives were extracted.

Known retracted preclinical source [39947542](https://pubmed.ncbi.nlm.nih.gov/39947542/) and notice [42527169](https://pubmed.ncbi.nlm.nih.gov/42527169/) retain unchanged reciprocal linkage and remain excluded from positive evidence. [Integrity check](integrity-recheck.json).

## Preprints and recovery

Title/abstract lexical screening with `\btourett\w*|\btics?\b` found zero matches in **771 unique DOI/version records within each server**.

| Server | Final records | Pages | Prior overlap | Not in prior bounded feed |
|---|---:|---:|---:|---:|
| bioRxiv | 645 | 23 | 276 | 369 |
| medRxiv | 126 | 5 | 20 | 106 |

The initial medRxiv attempt stopped after 30 records because cursor 30 returned HTTP 503. A complete interval retry retrieved 126 unique records with stable observed total. [Recovery record](medrxiv-recovery.json). The first failure is not erased.

BioRxiv's reported total increased from **642 to 645** during pagination. All returned DOI/version pairs were unique, but completion against the last observed total is not a stable snapshot or proof that no item was skipped during changes. Other servers, wording and indexing delays remain limitations. No abstracts are retained.

## Registries

ClinicalTrials.gov query counts were **2, 4, 4 and 1**, deduplicating to four update-window IDs with no next-page tokens. Six selected records including direct controls were reviewed. Projection excludes results measurements, participant flow, contacts, officials and locations. [Records/diffs](registry-evidence.jsonl).

- [NCT07093541](https://clinicaltrials.gov/study/NCT07093541): expanded access changed from temporarily not available to **no longer available**, posted October 28. No reason is provided in selected metadata; do not infer withdrawal of a marketing approval, safety signal or treatment failure.
- [NCT07137442](https://clinicaltrials.gov/study/NCT07137442): estimated start moves November 1 to November 2; planned 75 and no results remain.
- [NCT07854665](https://clinicaltrials.gov/study/NCT07854665): October 28 update of an October 2 pediatric taVNS protocol, planned 124, ages 6–18, randomized parallel triple-masked design, not yet recruiting and no results. No previous-day snapshot means no verified historical design change. Planned eligibility is not observed adult-persistence evidence.
- [NCT07898592](https://clinicaltrials.gov/study/NCT07898592): broad parent supportive-care protocol remains unchanged, not yet recruiting/no results.
- [NCT05158439](https://clinicaltrials.gov/study/NCT05158439) remains withdrawn for inability to recruit, zero enrollment: negative feasibility, not negative efficacy. [NCT06194305](https://clinicaltrials.gov/study/NCT06194305) remains recruiting pediatric CBIT without results.

ISRCTN edited-date query returned zero; positive-control total 22, with only one requested record. WHO homepage retrieval is not a completed query export; CTIS returned a shell, not parsed records. [Supplement](supplement-selected-metadata.json). Worldwide coverage remains incomplete.

## Discovery and evidence types

A third-party AACAP listing resurfaced an ecopipam post-hoc analysis already presented at MDS. The [official MDS abstract](https://www.mdsabstracts.org/abstract/safety-and-effect-of-ecopipam-during-the-first-8-weeks-of-treatment-for-tourette-syndrome-a-post-hoc-analysis/) combines blinded phase 2b treatment with open-label phase 3 initiation. Its week-8 response proportion is 178/255 assessed, not 69.8% of all 292 treated; 37/292 discontinued because of adverse events. This is conference evidence from overlapping trials, not an independent new controlled effect or full peer-reviewed paper. No new first-publication date or new safety signal is claimed. No dosing or treatment advice is reproduced. [Discovery log](discovery-log.json).

## Reproducibility and boundaries

There were **42 core requests plus five recovery requests**, with 46 successes and one retained HTTP 503. Thirty-five offline metadata/count/date/privacy checks and seven exact normalized-output reproductions passed. These are documentation/software checks, not clinical validation.

```sh
python updates/2026-10-29/scan/prepare_baseline.py --repo . --out /tmp/day29-baseline.json
python updates/2026-10-29/scan/scan_sources.py --baseline /tmp/day29-baseline.json --out /tmp/day29-live
# Only if the medRxiv attempt is incomplete:
python updates/2026-10-29/scan/retry_medrxiv.py /tmp/day29-recovery.json
python updates/2026-10-29/scan/merge_recovery.py --raw /tmp/day29-live/search-log.json --recovery /tmp/day29-recovery.json --baseline /tmp/day29-baseline.json --out /tmp/day29-merged.json
python updates/2026-10-29/scan/build_results.py --raw /tmp/day29-merged.json --repo . --out /tmp/day29-reviewed
python updates/2026-10-29/scan/validate_artifacts.py --repo .
python updates/2026-10-29/scan/verify_reproduction.py --repo .
```

If no recovery is needed, normalize the original live search log. Future IDs/changes need fresh review. Copy supplement/integrity scripts to a temporary directory before rerunning because they write beside themselves. No participant data, full papers, source abstracts, private stories, outreach, intervention or paid compute occurred. The independent bounded analysis and publication are documented by the integrating researcher, not claimed by this scan.
