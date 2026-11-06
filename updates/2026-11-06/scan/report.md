# Bounded evidence and safety scan: 6 November 2026

## Result

No qualifying new-window primary first publication, preprint, posted ClinicalTrials.gov result or watched-treatment official safety warning was verified. This is a bounded search, not evidence that no relevant work exists worldwide. Newly surfaced historical safety literature, secondary commentary, registry metadata and unresolved source leads are retained separately.

The authoritative baseline is main commit `cd78cc307253a3c38ee3b846849150721ea19264`, verified through the GitHub connector. README, RESEARCH_PROTOCOL, STATUS, the journal-source README and November 5 scan artifacts match the local baseline by Git blob hashes. The prior core cutoff was November 5 at 02:43:44.655875 UTC. Today's core ran 02:51:09.082496–02:55:38.829914 UTC; a book-record metadata supplement finished 02:55:43.665529 UTC.

## Publications

Eight PubMed query families returned 29 ID occurrences and **20 unique IDs**, including 19 journal records and one book chapter. Three overlap the prior scan and seventeen are absent from that returned set, not seventeen new studies. Exact queries, date types, IDs, response hashes and request timestamps are in [search-log.json](search-log.json). The calendar overlap was November 4–6, with a nearer entry-date check November 5–6. Relevant older evidence and negative/preclinical limitations remain in [pubmed-screening.jsonl](pubmed-screening.jsonl).

- [PMID 42982044](https://pubmed.ncbi.nlm.nih.gov/42982044/), DOI [10.1055/a-2984-7514](https://doi.org/10.1055/a-2984-7514), is titled *Aripiprazole-Induced Gambling Disorder as an Adverse Drug Reaction in Tourette Syndrome: A Case Report*. Both electronic publication and PubMed history date November 4, before the prior cutoff. It is newly surfaced in this scan, not proven newly indexed after the cutoff. Only bibliographic metadata was retained. No individual narrative, effect estimate, risk rate, causal certainty or treatment change is inferred. The [MHRA's existing December 18, 2023 warning](https://www.gov.uk/drug-safety-update/aripiprazole-abilify-and-generic-brands-risk-of-pathological-gambling) already covers pathological gambling and other impulse-control problems; it does not establish a frequency from spontaneous reports.
- [PMID 42984929](https://pubmed.ncbi.nlm.nih.gov/42984929/), DOI [10.3389/fneur.2026.1971225](https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2026.1971225/full), is an October 21 pediatric Perspective. Its three-domain assessment framework is explicitly an unvalidated clinical heuristic, not a new empirical result. Function, pain and co-occurring burden are relevant, but a pediatric proposal does not establish severe adult benefit.
- [PMID 42986906](https://pubmed.ncbi.nlm.nih.gov/42986906/), DOI 10.1371/journal.pone.0360750, is a November 5 chronic-stress inventory validation. “TICS-9” is an acronym collision, not tic-disorder evidence. The surgical-process and body-dysmorphic-disorder hits were also excluded.
- [PMID 23556151](https://pubmed.ncbi.nlm.nih.gov/23556151/), Bookshelf NBK131811, is a secondary *GeneReviews* chapter on Coffin-Siris syndrome. The original journal-only parser omitted this record, which was detected by ID accounting and separately retrieved as a PubmedBookArticle. All 20 returned IDs are now accounted for. November 5 database history is not a new primary Tourette finding.
- The previously verified September 1 date for PMID 42978485 is inherited from the November 5 publisher check, explicitly not freshly reverified today. Its year-only PubMed date does not justify counting it as a November trial.

No newly linked retraction was found among returned journal metadata. An official search card for the October 8 [Nature primer](https://www.nature.com/articles/s41572-026-00742-6) mentions a table correction without a correction date. Direct access failed at a publisher identity redirect and targeted searches did not resolve the date. It is an unresolved secondary-source lead, not a verified new-window notice or an absence claim.

## Preprints

bioRxiv and medRxiv APIs returned **1,171 unique DOI/version records**, respectively 966 and 205, over November 3–6. Complete pagination reached stable observed totals. Title/abstract screening with `\btourett\w*|\btics?\b` found no match. Of these, 239 version records are absent from yesterday's overlapping index, not necessarily new studies. Positive and negative lexical controls pass. Only DOI/version/date indexes are retained; abstracts were used transiently and not archived. Other servers, differently worded work and delayed indexing remain gaps.

## Trial registries

Four ClinicalTrials.gov update-window queries cover November 4–6. Five prespecified watch records were also fetched directly. Six unique records were screened using selected protocol fields, excluding contacts and result measurements. All six report `hasResults=false`.

- [NCT07137442](https://clinicaltrials.gov/study/NCT07137442): estimated start November 9→10, update submission November 3→4 and update posting November 4→5. It remains listed RECRUITING with estimated enrollment 75, ages 18–80. This is a selected-field snapshot change, not confirmation of actual recruitment, diagnostic validity or benefit. Calendar posting dates cannot resolve exact timing within yesterday's cutoff day.
- [NCT01019343](https://clinicaltrials.gov/study/NCT01019343): newly surfaced update posted November 5. This is a completed, nonrandomized, unmasked adult basic-science study across several movement disorders, with actual total enrollment 1,273 and completion October 9, 2020. Total enrollment is not a Tourette subgroup count. Without a prior snapshot, which fields changed is unknown. It has no posted results and is not a new efficacy trial.
- Selected fields for NCT05158439, NCT06194305, NCT07093541 and NCT07905898 are unchanged. Earlier PRISM-TS enrollment discrepancies are not resolved by unchanged metadata.

Supplementary discovery identified **UMIN000063483, Tic Manager RCT**, on the official UMIN index with an October 31 disclosure date. Opened index text says Open public recruiting while older cached official search snippets say Preinitiation. Detail/history links returned the index or were inaccessible. Exact protocol, current recruitment, result availability and amendment chronology remain unverified; no new-window result or verified recruitment claim is made. This is a bounded access limitation, not an exhaustive UMIN/WHO search.

## Official safety review

Six dated search queries and fifteen official index/referral/page checks are recorded in [safety-review.json](safety-review.json). No qualifying new watched-treatment warning or issued tic guideline was verified since the prior safety cutoff, November 5 at 02:40:55 UTC. New FDA index changes, EMA headings and MHRA givinostat/co-amoxiclav/tropicamide notices do not establish a warning for a watched tic treatment. The HSA tetrabenazine batch DNG1035A recall and open EMA Deanxit combination review remain historical; flupentixol alone is explicitly outside that referral. TicCare remains a registration, not issued guidance.

Two apparently recent search hits were resolved to older official dates: the TGA methylphenidate supply page says October 30, and its PI year table says September 29 with the located methylphenidate entry approved July 22. Crawl/search publication labels were not counted as new safety events. This is English-heavy surveillance, not all national agencies, labels or attachments and not proof of safety.

## Coverage, reproduction and decision

All **58 core API requests plus one recorded metadata supplement succeeded**. PubMed and DOI web-reader failures did not prevent official XML metadata retrieval; ClinicalTrials.gov's web shell did not replace API evidence. UMIN details and Nature correction chronology remain unresolved. Exact discovery queries and access outcomes are in [discovery-log.json](discovery-log.json).

Run `python scan_sources.py --out NEW_DIRECTORY --baseline baseline.json` for the live bounded queries, then separately run `check_book_metadata.py` for the book supplement and `build_results.py` for this captured classification. Live results can change. `validate.py` checks query/result accounting, pagination, date eligibility, exclusions, registry changes and privacy boundaries. These are consistency checks, not independent clinical validation. No simulation or random seed applies.

Continue the planned H13 historical outcome/generalization audit. Do not treat this null scan or historical case report as a clinical recommendation. Persistent severe adult burden, pain, function and co-occurring conditions remain central alongside all ages and chronic tic categories. No patient files, outreach, intervention, enrollment or paid compute are required. No repository files were edited during this scan preparation.
