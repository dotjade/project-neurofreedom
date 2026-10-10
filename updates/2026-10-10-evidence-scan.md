# Project NeuroFreedom: daily public-evidence scan

10 October 2026 | Checked approximately 02:43–02:48 UTC

## Result

No new qualifying primary Tourette/tic study or posted trial result was verified in this bounded update. Four newly indexed PubMed candidates were screened: one new review with a companion visual summary, a historical biography, and an unrelated case report. A newly updated adult rTMS registry record preserves important negative evidence, but its trial ended in 2012; it is **not a newly failed 2026 trial**. No material new tic-therapy safety notice was identified in the official FDA/EMA/MHRA checks.

This scan covers all ages and severities. Persistent, severe adult tics, treatment resistance, burden and durable functional benefit remain central to selection. Childhood improvement, cyclic fluctuations and remission are components of that broader mission, not assumptions about every person's course. No age, severity, language, human-only or study-design restriction was applied to the core database searches.

## Baseline and dates

Read current private repository files before searching: README.md, RESEARCH_PROTOCOL.md, STATUS.md, evidence.jsonl and updates/2026-10-09-evidence-scan.md. The evidence file contained 18 primary-study records. Baseline blobs were respectively `45d2e639090a8516781c807ff747352f501ebef1`, `6b7bbe11ded85da1786485e9b816dac7a639f6fd`, `3d59e8ed9136f1928be97314ec4b1530292be3bc`, `47ccdf03793760bfd6abd3bb71113ad17d917797`, and `7b0f4d643200086d9ec6ea21ba64faabbec10887`.

The previous verified scan ended about 03:17 UTC on 9 October. Current discovery uses an inclusive 8–10 October overlap, plus a nested 9–10 October entry-date query. Publication, database entry, metadata revision, registry posting and trial-event dates are treated separately. The current early-day check cannot cover later 10 October postings. Most sources provide only a calendar date, so an item dated 9 October is not automatically known to have appeared after 03:17 UTC.

## New-to-scan literature: no new primary tic experiment

| PMID / DOI | Verified dates and type | Decision |
|---|---|---|
| [42850293](https://pubmed.ncbi.nlm.nih.gov/42850293/), 10.1038/s41572-026-00742-6, Eapen et al., *Tourette syndrome* | Publisher publication/version of record 8 October; PubMed history date 9 October; review | Retain as a new secondary source and reference map. No new participant sample or independent efficacy result. |
| [42850245](https://pubmed.ncbi.nlm.nih.gov/42850245/), 10.1038/s41572-026-00748-0, *Tourette syndrome* | Published 8 October; PubMed history 9 October; publisher labels it PrimeView | Companion visual summary, not an independent study. Do not double-count with the review. |
| [42850218](https://pubmed.ncbi.nlm.nih.gov/42850218/), 10.1080/0964704X.2026.2734029, Seignot biography | Electronic publication 8 October; PubMed history 9 October | Historical biography/translation of a 1961 haloperidol observation; exclude from new efficacy evidence. |
| [42852027](https://pubmed.ncbi.nlm.nih.gov/42852027/), 10.3389/fpsyt.2026.1920653, somatic-cough case report | Electronic publication 24 September; PubMed history 9 October | Newly indexed older report; tic disorder was explicitly excluded. No support for a tic treatment or cure. |

The [Nature review's publisher page](https://www.nature.com/articles/s41572-026-00742-6) explicitly includes severe, incapacitating, treatment-refractory adult illness and quality-of-life/comorbidity outcomes. This is consistent with the broader research scope, but it is not primary confirmation of a mechanism. The accessible preview, abstract, dates, reference list and disclosures were inspected; the subscription full text was not obtained. The [PrimeView page](https://www.nature.com/articles/s41572-026-00748-0) confirms its companion format and publication date. The three 8 October items have Entrez-history dates on 8 October and PubMed-history dates on 9 October; their exact history timestamps do not supply an explicit timezone. They should be called newly indexed/discovered, not newly first-published on 9 October.

The modification-date sweep also returned an older pediatric OCD secondary analysis, PMID 42846224: electronic publication 11 July 2025, Entrez entry/PMC release 8 October 2026, but a backdated PubMed-history field in July 2025. It is outside the focused tic-treatment/trajectory evidence and was not promoted as a new 2026 study. This illustrates why a single entry-date field is insufficient.

## Official registry changes

### Adult posterior-parietal rTMS: negative historical evidence newly encountered

[NCT01043549](https://clinicaltrials.gov/study/NCT01043549), rTMSPPCGT, has a **last update posted 9 October 2026**, submitted 6 October. The [current official API record](https://clinicaltrials.gov/api/v2/studies/NCT01043549) reports:

- Terminated; stopping reason: lack of efficacy.
- Actual enrollment 5; eligibility ages 18–70 with TS, premonitory sensations and a registry-stated YGTSS range of 30–60. The score's exact subscale is not clarified.
- Crossover active/sham posterior-parietal rTMS; participant and outcome-assessor masking. Structured allocation is non-randomized although the narrative says randomized, an unresolved registration inconsistency.
- Primary/completion dates September 2012; status last verified February 2016; no results posted and no linked results publication in the retrieved record.

This is a useful negative-outcome lead for adult intervention research. It does not quantify the effect, uncertainty, attrition or harms, and cannot refute all rTMS targets or protocols. The recent posting does not establish that termination, enrollment or the reason first changed now. A cached official-page search extract already displayed the terminated status and the same enrollment under a 2016 update date; the current API takes precedence for current metadata. The official historical API returned HTTP 403, so no authoritative historical field diff was obtained. No access restriction was bypassed. Retain it as a **recent registry update containing historical negative evidence**, not a current efficacy result or recruitment opportunity.

### Existing adult physiology record: small scheduling change

[NCT07137442](https://clinicaltrials.gov/study/NCT07137442), distinguishing tics from functional tics, now has a 9 October update. Comparing the complete saved official API snapshot from the 9 October scan with today's snapshot found only:

- Estimated start date: 13 October → 14 October 2026.
- Update submitted/posted dates moved forward one day; derived version metadata also changed.

Recruiting status, estimated total enrollment 75, eligibility ages 18–80, endpoints and no-results status were unchanged. A recruiting label and estimated start are not proof that enrollment has begun or that a diagnostic biomarker is validated. Medication/comorbidity exclusions also limit applicability to many people with severe, treated adult illness. No participant suitability or clinical action is inferred.

The two remaining overlap records, NCT01019343 and NCT02119611, retained 8 October posting dates and their previous statuses/no-results state. Whole-record comparison found only the derived `versionHolder` date changed; these are not new efficacy or recruitment findings. The latter still lacks TS-specific eligibility despite search indexing and should not be presented as a TS recruitment option.

## Reproducible database ledger

### PubMed

Official NCBI ESearch endpoint: `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi`.

Core query exactly: `Tourette OR "tic disorder" OR "tic disorders"`.

All calls: `db=pubmed`, `retmode=json`, `retmax=1000`; start=0. Returned counts were below the limit and all IDs were fetched using EFetch XML. No silent count cap is involved.

| Retrieval start UTC | Date field / inclusive range | Count and IDs |
|---|---|---|
| 02:44:11 | edat, 2026/10/08–2026/10/10 | 5: 42852027, 42850293, 42850245, 42850218, 42845759 |
| 02:44:17 | edat, 2026/10/09–2026/10/10 | 4: the first four above |
| 02:44:22 | pdat, 2026/10/08–2026/10/10 | 3: 42850293, 42850245, 42850218 |
| 02:44:28 | mdat, 2026/10/08–2026/10/10 | 33, including all five entry-window IDs |
| 02:44:34 | edat, 2026/10/08–2026/10/10, notice query below | 0 |

[Reproducible entry-date search](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=Tourette%20OR%20%22tic%20disorder%22%20OR%20%22tic%20disorders%22&datetype=edat&mindate=2026%2F10%2F08&maxdate=2026%2F10%2F10&retmode=json&retmax=1000).

Notice query exactly: `(Tourette OR "tic disorder" OR "tic disorders") AND (retraction OR retracted OR erratum OR corrigendum OR correction)`.

Counts: 41 returns from the three overlapping broad searches (5+3+33), four additional returns from the nested check, **33 unique PMIDs**. All 33 titles, dates, publication types and linked correction metadata were screened; the four new entry candidates received full abstract/format/date screening. The additional 28 modification-only records were older publications, not new in-window studies. No retrieved record had a linked CommentsCorrections notice; the targeted notice search returned zero without unrecognized-phrase warnings. This is not an exhaustive publisher/Crossmark/retraction audit.

The 28 modification-only IDs, retained for reproducibility rather than presented again as new evidence: 42840857, 42810670, 42736497, 42713760, 42247083, 41961094, 41888346, 41724351, 41557034, 41288886, 41152527, 41079641, 40965605, 42846224, 40540000, 40457054, 40215249, 39679818, 39390224, 39175366, 38619754, 38468554, 38468546, 38291848, 38291846, 38291838, 38269641, 31980733. Metadata modification alone cannot establish new findings or the substance of a revision.

Identifier deduplication against all five baseline files found five previously mentioned IDs: 42845759, 42810670 and 42840857 already extracted in evidence.jsonl, plus 42247083 and 41724351 already screened in the prior update. The three prioritized studies were not repackaged as discoveries. No new primary-study JSONL record is warranted from this scan.

### ClinicalTrials.gov

API v2 queries used each `query.cond` value `Tourette`, `tic disorder`, and `Tics`, with `filter.advanced=AREA[LastUpdatePostDate]RANGE[2026-10-08,2026-10-10]`, `pageSize=100`, `format=json`, `countTotal=true`.

- Retrieval starts 02:44:46, 02:44:53, 02:44:58 UTC: counts 3, 4, 4, respectively; **11 returns, four unique NCTs**, no next-page tokens.
- Unique IDs: NCT01043549, NCT07137442, NCT02119611, NCT01019343. None has posted results. One ID is new to the baseline; one existing ID has a new posting date and the narrow changes above.
- Supplemental `query.term=ecopipam` with the same date expression and page/count parameters returned **0** updated records. This is not a claim that ecopipam has no studies/results outside the window.

[Reproducible registry query](https://clinicaltrials.gov/api/v2/studies?query.cond=Tourette&filter.advanced=AREA%5BLastUpdatePostDate%5DRANGE%5B2026-10-08%2C2026-10-10%5D&pageSize=100&format=json&countTotal=true).

Rendered PubMed search/article pages and ClinicalTrials.gov pages were unhelpful or failed; official API retrieval recovered the metadata. Two historical API attempts (`/api/int/studies/NCT01043549/history` and the same route for NCT07137442) returned 403. The latter comparison therefore uses two verified saved current-record snapshots, not a claimed complete registry history. The WHO trial-specific query did not return usable content. Targeted ISRCTN/EU-register discovery found older records only, but neither WHO/CTIS nor national-registry update coverage is complete.

## Regulatory safety

Through approximately 02:45 UTC, no new material warning concerning the specified tic therapies was identified. New 9 October official notices were outside scope: FDA Brevital injection recall and Philips Lumify ultrasound alert; EMA Ocrevus DHPC; MHRA StatStrip ketone-strip notices. These do not imply a tic-treatment safety change.

Checked the [FDA drug communication list](https://www.fda.gov/drugs/drug-safety-and-availability/drug-safety-communications), [device communications](https://www.fda.gov/medical-devices/medical-device-safety/safety-communications), [drug recalls](https://www.fda.gov/drugs/drug-safety-and-availability/drug-recalls), [device safety index](https://www.fda.gov/medical-devices/medical-device-safety), [EMA What's New](https://www.ema.europa.eu/en/news-events/whats-new), [PRAC highlights](https://www.ema.europa.eu/en/news/meeting-highlights-pharmacovigilance-risk-assessment-committee-prac-28-september-1-october), [MHRA alerts](https://www.gov.uk/drug-device-alerts) and [Drug Safety Update](https://www.gov.uk/drug-safety-update). EMA's 69 visible rows dated 8–9 October were screened. FDA drug/device communication lists still ended 15 September/3 June respectively; MHRA Drug Safety Update still ended 2 September.

This was a public-announcement and indexed-search check, not exhaustive label-version comparison, all recall enforcement records, FAERS/MAUDE analysis, every national regulator, or every manufacturer's notice. No clinical recommendation follows from the bounded negative finding.

## Supplementary search ledger and limits

Exact web queries (search-engine totals unavailable; not added to database counts):

1. `Tourette "October 9, 2026" OR "October 10, 2026"`
2. `Tourette tic disorder after:2026-10-07`, domains `pubmed.ncbi.nlm.nih.gov`
3. `Tourette after:2026-10-07`, domains `medrxiv.org`, `biorxiv.org`
4. `"Tourette" "October" "2026" adults`
5. `"42852027"`
6. `"42850293"`
7. `"42850245" OR "42850218"`
8. `"NCT01043549" "lack of efficacy"`
9. `ClinicalTrials.gov history API study changes` (technical route discovery only; findings rely on official retrievals)
10. `"Tourette" after:2026-10-07`, domains `clinicaltrials.gov`, `isrctn.com`, `clinicaltrialsregister.eu`
11. `"tic disorder" after:2026-10-07`, domains `medrxiv.org`, `biorxiv.org`
12. `"Tourette" "posterior parietal" "stimulation"`, domains `pubmed.ncbi.nlm.nih.gov`
13. `"NCT01043549"`
14. `"rTMSPPCGT"`

These searches returned many old or irrelevant items despite date operators. No new in-window preprint was verified; this was not a complete preprint feed/API scan. Public registry identifiers, not individual/family information, were used externally. No contact, enrolment, data application, treatment action or repository commit was performed during this research.

## Consequence for the research program

1. No promotion of a mechanistic or cure claim on today's evidence.
2. Preserve adult negative-treatment evidence, including underreported small studies, while requiring methods, numerical outcomes and historical context before interpreting efficacy.
3. Use the new review only as a secondary reference map for the all-age/severity program; verify its cited primary sources when advancing a hypothesis.
4. Keep registry-update dates separate from trial events. The newly observed adult rTMS record and one-day start-date change do not justify an urgent clinical update.


## Exact regulatory discovery queries

Web search was restricted through the following literal site qualifiers. Date operators sometimes returned older pages; dates were screened rather than trusted as strict database filters. Result counts below, when given, are returned hits rather than exhaustive database totals. The broad multi-site device search returned zero; other broad queries were noisy and no precise exhaustive count is claimed.

1. site:fda.gov "Safety Communications" medical devices 2026
2. site:fda.gov (ecopipam OR aripiprazole OR risperidone OR pimozide OR haloperidol OR clonidine OR guanfacine OR valbenazine OR deutetrabenazine OR tetrabenazine) (safety OR recall OR warning) after:2026-10-07 before:2026-10-11
3. site:ema.europa.eu (ecopipam OR aripiprazole OR risperidone OR pimozide OR haloperidol OR clonidine OR guanfacine OR valbenazine OR deutetrabenazine OR tetrabenazine) after:2026-10-07 before:2026-10-11
4. site:gov.uk (ecopipam OR aripiprazole OR risperidone OR pimozide OR haloperidol OR clonidine OR guanfacine OR valbenazine OR deutetrabenazine OR tetrabenazine) (safety OR recall OR warning) after:2026-10-07 before:2026-10-11
5. site:fda.gov (Tourette OR ecopipam OR "median nerve" OR neuromodulation OR "deep brain stimulation") (safety OR recall OR warning) after:2026-10-07 before:2026-10-11
6. site:gov.uk (Tourette OR ecopipam OR "median nerve" OR neuromodulation OR "deep brain stimulation") (safety OR recall OR warning) after:2026-10-07 before:2026-10-11
7. site:ema.europa.eu "Meeting highlights" "PRAC" "October 2026"
8. site:ema.europa.eu (ecopipam OR aripiprazole OR risperidone OR pimozide OR haloperidol OR clonidine OR guanfacine OR valbenazine OR deutetrabenazine OR tetrabenazine) "October 2026"
9. (site:fda.gov OR site:ema.europa.eu OR site:gov.uk) ecopipam "October 2026"
10. (site:fda.gov OR site:ema.europa.eu OR site:gov.uk) (aripiprazole OR risperidone OR pimozide OR haloperidol) "October 2026"
11. (site:fda.gov OR site:ema.europa.eu OR site:gov.uk) (clonidine OR guanfacine OR valbenazine OR deutetrabenazine OR tetrabenazine) "October 2026"
12. (site:fda.gov OR site:ema.europa.eu OR site:gov.uk) (Tourette OR "median nerve stimulation" OR Neupulse OR "deep brain stimulation" OR neuromodulation) (safety OR recall OR warning) after:2026-10-07 before:2026-10-11 — zero returned results.
13. site:fda.gov "ecopipam" safety — recency parameter 7 days; returned historical material.
14. site:gov.uk "ecopipam" safety — recency parameter 7 days; returned unrelated historical material.
15. site:fda.gov "Medical Device Recalls and Early Alerts"
16. site:fda.gov "Early Alert: Diagnostic Ultrasound System Issue from Philips Ultrasound"

