# Bounded evidence and safety scan: 11 November 2026

## Result

No qualifying new-window primary tic publication, relevant preprint or posted trial result was verified. One watched registry has a November 10 metadata update: NCT07137442 moved its estimated start from November 12 to November 15. No new watched-treatment official safety warning was verified. This is bounded surveillance, not proof of absence, efficacy or safety. No empirical evidence addition or hypothesis upgrade is proposed.

Read the repository README, research protocol, opening status, journal-source README, November 10 scan report/log, and 71 current evidence records. The baseline was retrieved from main at commit f6391480c4ac6249e8a9efc03ceb792e604f6299. The previous core scan ended November 10 at 03:27:55.287498 UTC. Current core API checks ran November 11 at **03:15:02.412552–03:17:28.667600 UTC**. Supplemental checks are individually timed in their files; the historical correction check completed at 03:17:32 UTC. Web checks occurred in the same run, but individual web-query times were not captured.

## Primary publications and notices

Eight PubMed query labels covered entry, publication and modification dates for November 9–11, including tic synonyms, notices, and adult/severe/pain/function/comorbidity/treatment-burden terms without age or language filters. The near-entry query duplicates the core entry query and adds no independent coverage. Exact parameters, translated queries and IDs are preserved in search-log.json.

There were **25 ID occurrences and 25 unique records**, all from the modification-date query. Entry-date, publication-date and correction/retraction entry-date queries returned zero. Twenty records overlap the previous scan and five were absent from that scan's returned set; this is not five new publications. All 25 publications precede the surveillance window. Two are 2026 secondary reviews; the other 23 first appeared before 2026. PMID 40238019 has a December 2026 issue date but an April 16, 2025 electronic date. Screening decisions and identifiers are in pubmed-screening.jsonl.

The returned historical primary paper PMID 40680639 has a linked corrigendum, [PMID 42767894](https://pubmed.ncbi.nlm.nih.gov/42767894/), DOI 10.1016/j.nicl.2026.104054, electronically published September 21, 2026. The reciprocal original/notice link and date were verified. Neither is a new-window publication. The correction's substantive content was not fully reviewed, and absence of a link on other records is not comprehensive correction clearance.

Web discovery also verified a [pediatric neuroimmune narrative review](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2026.2006073/full), DOI 10.3389/fimmu.2026.2006073, published November 9. It is newly found in this run but predates the previous cutoff. It does not add a primary experiment or establish immune-directed treatment. Search-labelled fresh copies of a [GWAS](https://pubmed.ncbi.nlm.nih.gov/36738982/) and [Finnish comorbidity cohort](https://pubmed.ncbi.nlm.nih.gov/42425918/) were confirmed as older publications. Web timestamp and issue-date changes were not counted as discoveries.

## Preprints

The bioRxiv/medRxiv APIs returned **721 distinct DOI/version records** for November 7–11: 521 bioRxiv and 200 medRxiv. Title/abstract lexical screening for Tourette or tic/tics returned zero matches; positive/negative lexical controls passed. Only DOI/version/date indexes are retained, not abstracts or papers.

Both paginations reached their observed totals, with stable reported totals across pages. Compared with the full November 10 saved indexes, 293 bioRxiv and 107 medRxiv versions overlap; 228 and 93, respectively, were not in those indexes. The combined 321 unmatched versions are not 321 relevant new studies. These are live mutable indexes, not fixed snapshots. Other servers, indexing delays, missing keywords and non-English terminology remain limits.

## Trial registries

Four ClinicalTrials.gov date-window queries returned two distinct study IDs, NCT01019343 and NCT07137442. Seven watched official snapshots were compared on selected title, status, design, condition, age and results fields. None had posted results.

- [NCT07137442](https://clinicaltrials.gov/study/NCT07137442): estimated start changed November 12 to November 15; last submission changed November 6 to November 9 and last posting November 9 to November 10. Other selected fields are unchanged. An estimated date is not actual enrollment or a study finding.
- NCT01019343, NCT05158439, NCT06194305, NCT06678737, NCT07093541 and NCT07905898: no selected-field change.

Six supplemental official ClinicalTrials.gov snapshots bring the distinct total to **13**. NCT07839377 and NCT06825520 remain last posted September 24, 2026 and May 28, 2025. Newly rediscovered NCT05942716, NCT05558566, NCT06909656 and NCT07854665 were last posted December 4, 2024; June 9, 2026; April 3, 2025; and October 28, 2026, respectively. None has results. Third-party November 9–10 synchronization dates were not official updates. Recruitment labels and past estimated dates do not verify present availability.

A separate [UMIN000063483 official detail record](https://center6.umin.ac.jp/cgi-open-bin/ctr_e/ctr_view.cgi?recptno=R000071959) shows last modification November 2, disclosure October 31, a planned pediatric assessor-blinded waitlist trial and unpublished results. The current detail status field says Open public recruiting; a search-indexed list says Preinitiation. The full history and actual enrollment remain unverified. This is not a new-window result. WHO, ISRCTN and ChiCTR checks were supplemental web discovery rather than exhaustive direct database searches.

## Official safety

Inspected nine official source pages: FDA drug and device communications; MHRA drug updates and device/medicine alerts; EMA latest updates and PRAC signal recommendations; TGA safety updates, alerts and its monthly Product Information table. Targeted searches covered aripiprazole, guanfacine, clonidine, topiramate, ecopipam and pimozide.

No new watched-treatment warning was verified. FDA's latest drug index item was the November 9 GLP-1 eye-risk communication, outside this scope; its visible device index began with June 3. MHRA visible drug/medicine notices remained dated November 5 or earlier. EMA's first-page updates included November 10 entries without a watched treatment; PRAC recommendations remained first published October 26. TGA's visible safety-update and safety-alert lists began with October 14 and November 5, respectively. Its apparent fresh aripiprazole search hit actually records a September 24 PI approval, covering fall-related injuries and overdose-management wording. No November class-wide warning is inferred.

These checks do not constitute worldwide pharmacovigilance, a full label review or individualized safety advice. Exact official URLs and 14 web searches are in web-query-provenance.json.

## Reproduction and decision

The core script was adapted from November 10 by advancing the run/date-window dates by one day. It made 45 successful API requests. Six supplemental registry reads and one linked-notice read also succeeded. Summary, selected registry fields, PubMed screening metadata and preprint indexes are archived. Scripts rerun live sources and can produce different results later; no participant data or random seed was involved.

This scan identified no new primary result or accessible analysis input that reopens the previously closed H18 measurement/transfer, H15 group-mask provenance or adult CANNA-TICS missingness gates. That is a surveillance decision, not a fresh exhaustive re-audit. Continue only on materially changed prerequisites. No outreach, recruitment, intervention, controlled-data access or personal health information was involved.

The first offline checker omitted the scanner's case-insensitive flag and failed its uppercase lexical control. The checker was corrected to match the executed scan; all 14 checks now pass. No query or classification changed. The supplemental script's fixed temporary output path was made configurable after execution for portability; source requests were not rerun for this edit. See validation-history.json.
