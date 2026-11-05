# Bounded new-evidence scan, 5 November 2026

## Result and methods

No qualifying new-window primary first publication, preprint, posted trial result or linked retraction was verified. A newly indexed case report was resolved to an older publisher date. One watched registry has an administrative date update. This bounded search is not evidence that no relevant work exists worldwide; regulatory safety is assessed separately.

The prior core cutoff was November 4 at 02:40:05.116250 UTC. Core queries ran November 5 from 02:39:34.609051 to 02:43:44.655875 UTC. Eight PubMed query families and four registry update-window queries overlap November 3–5; preprint queries cover November 2–5. Calendar-day filters cannot establish exact within-day posting order. Exact queries, response hashes, timestamps and source URLs are in [search-log.json](search-log.json). Five prespecified watched registries were also fetched directly with fields restricted to protocol metadata, excluding contacts and result measurements.

## Publications and preprints

PubMed yielded 28 ID occurrences and 25 unique records. Twenty-two overlap yesterday and three are absent from that comparison, not three new studies. All have first-publication evidence before the prior cutoff. Historical negative, mechanistic, pediatric and comorbidity evidence remains retained in the metadata screen.

- [PMID 42469137](https://pubmed.ncbi.nlm.nih.gov/42469137/), DOI 10.1016/j.parkreldis.2026.108419, is a secondary DBS mini-review electronically published July 11 despite its November issue assignment. It is not a new primary finding.
- [PMID 42977160](https://pubmed.ncbi.nlm.nih.gov/42977160/), DOI 10.1016/j.virs.2026.11.002, is a pediatric HFMD cohort electronically published November 3, before the cutoff. Its abstract includes tic disorders among several sequelae, but this adjacent observational evidence does not establish a cause of primary Tourette syndrome or treatment benefit. No tic-specific comparative effect estimate was extracted, and no full-text appraisal is claimed.
- [PMID 42978485](https://pubmed.ncbi.nlm.nih.gov/42978485/), publisher identifier TVPart_13711, was indexed November 4 after the prior cutoff. PubMed provides only the year for publication. Direct [publisher HTML metadata](https://www.tijdschriftvoorpsychiatrie.nl/en/artikelen/article/50-13711_Multilocus-rTMS-bij-Tourettic-obsessieve-compulsieve-stoornis) instead supplies citation_publication_date 2026/09/01. This is an older rTMS case report, not a new November controlled result. A favorable case-report title/claim cannot establish efficacy, safety, durability without ongoing treatment, or a cure. Individual clinical narrative was not extracted or retained. The publisher metadata check resolves date eligibility without importing the paper into the repository.

The bioRxiv and medRxiv APIs yielded 1,306 unique DOI/version records: 1,080 and 226 respectively. Title/abstract lexical screening found no Tourette/tic match. Five hundred twenty version records were absent from yesterday's overlapping indexes, not necessarily separate new studies. Both paginations completed with stable observed totals; positive/negative lexical controls passed. Other preprint servers, differently worded studies and indexing delays remain gaps.

## Registry comparison

All five watched registries still lack posted results. [NCT07137442](https://clinicaltrials.gov/study/NCT07137442), an observational tics/functional-tics protocol, changes estimated start November 8 to November 9, update submission November 2 to November 3, and update posting November 3 to November 4. It remains listed RECRUITING with estimated enrollment 75, ages 18–80. These are metadata, not confirmation of actual recruitment, diagnostic validity or benefit. Posting day alone cannot place the change precisely relative to yesterday's cutoff; snapshot differences are verified.

Selected fields for NCT05158439, NCT06194305, NCT07093541 and NCT07905898 are unchanged. The earlier PRISM-TS adolescent enrollment discrepancy is not resolved by unchanged fields. Full amendment histories and unselected fields were not compared.

## Access, coverage and next decision

All 62 core API requests succeeded. Supplementary web discovery returned older publications, registry mirrors and crawl/synchronization timestamps. Those timestamps were not treated as primary-source update dates. A Canadian official trial portal showed different last-update dates in search and opened cached views, both historical; neither establishes a new result. An official ClinicalTrials.gov web view returned a shell, while official API queries supplied the core comparisons. Two PubMed web pages were unavailable to the reader; their official XML metadata was successfully retrieved. A publisher index opened to a stale page, but direct article citation metadata resolved the relevant date. See [discovery-log.json](discovery-log.json).

No abstracts, unlicensed papers, individual case narratives, participant files or identifiable community content are archived. WHO and other national registries, non-English terminology, unindexed work and delayed notices are incompletely covered. A null daily scan does not diminish severe persistent adult burden, pain, functional limitations, co-occurring conditions or unmet needs across ages and chronic tic categories.

Continue the planned bounded group atlas/mask provenance gate. Do not reopen completed sensory/gene/CANNA-TICS audits due solely to metadata revisions. No outreach, treatment change or paid resource is required.

## Reproduction

Run `python scan_sources.py --out NEW_DIRECTORY --baseline baseline.json` for the live API search; responses may change. `python build_results.py` rebuilds metadata classifications, with the independently observed publisher date explicitly recorded. `python validate.py` performs 34 consistency and screening-control assertions. Baseline comes from the November 4 scan at commit d5450986a0df8b6c9d29344a6c576ae6bf922a05. No simulation or RNG applies. These checks are not independent clinical validation.
