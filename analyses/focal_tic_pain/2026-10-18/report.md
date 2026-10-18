# Marras focal-tic trial: access-limited pain-endpoint audit

Project NeuroFreedom | 18 October 2026 | Historical one-trial audit

## Decision

**Do not classify pain as unmeasured. Do not infer pain efficacy from tic improvement.** The planned full-methods gate could not be passed. The publisher's full HTML and PDF returned HTTP 403; official Europe PMC metadata lists subscription access without a PMC full text, and OpenAlex reports no open-access or repository copy. A lawful NIHR systematic review explicitly reports a pain score for the treated-tic area and presents a separate pain comparison. This corroborates pain measurement at the secondary-evidence level and weakens the prior absence prediction. It does not replace complete primary-source inspection or establish what the pain item measured.

The result is **pain measurement corroborated by a secondary review; primary endpoint definition and pain-benefit interpretation remain unresolved**, not an absent endpoint or verified evidence of analgesic benefit or harm. No clinical effect was calculated.

## What was tested

The [pre-extraction decision rule](prediction.md) asked whether the trial separately measured tic-related pain benefit or interference, distinguishable from tic frequency/severity, premonitory sensations and procedure discomfort. It predicted that a compatible pain endpoint would not be identifiable. A separately specified pain endpoint in complete primary methods/tables would disconfirm that prediction even if its treatment contrast were null.

The prediction was recorded before retrieving the Marras article. The later secondary-review finding weakens it; the prediction is not confirmed. Current README, research protocol, status, the October 18 pain-interference report and relevant evidence entries were read first. The protocol's public-release clarification was retained. This was a focused historical audit, not a new-publication scan or a systematic review.

## Verified primary-abstract layer

[Marras, Andrews, Sime and Lang, Neurology 56:605–610](https://www.neurology.org/doi/abs/10.1212/wnl.56.5.605), DOI [10.1212/WNL.56.5.605](https://doi.org/10.1212/WNL.56.5.605), [PMID 11245710](https://pubmed.ncbi.nlm.nih.gov/11245710/), was published 13 March 2001. The publisher's indexed abstract and official Europe PMC record identify a randomized double-blind botulinum-toxin/placebo crossover trial, with week-two comparisons against baseline and 18 completers. The listed primary endpoint is video-counted treated-tic frequency. Listed secondary endpoints include untreated-tic frequency, a syndrome-severity scale, urge, premonitory sensation and global change.

The abstract reports lower treated-tic frequency and urge, but no significant differences on other listed secondary measures and no reported overall benefit. Those statements do not establish a pain-specific null result, pain equivalence, severe-adult efficacy, or durable benefit. The abstract does not provide an exhaustive full-study endpoint inventory. Its 18-completer count is not a verified pain-analysis denominator. [Primary abstract and bibliographic record.](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11245710%20AND%20SRC%3AMED&format=json&resultType=core)

## Lawful secondary corroboration, kept separate

The [NIHR full report by Hollis and colleagues (2016)](https://njl-admin.nihr.ac.uk/document/download/2003385), DOI [10.3310/hta20040](https://doi.org/10.3310/hta20040), was inspected through its official publisher PDF. Page 210 discusses a pain score for the treated-tic area; Figure 216 on page 211 presents the corresponding comparison and identifies Marras 2001. The review places the discussion under Safety and states that the scale was not reported. Its result is described as inconclusive.

This is reputable secondary evidence that a pain-related outcome was analyzed, stronger than an unofficial search snippet. It still does not verify the primary question/anchors, whether the item captures tic-related pain benefit or treatment-related discomfort, or a pain-interference endpoint. The review’s extraction and standardization were not independently reconciled to the inaccessible original tables. Its numerical effect was not adopted as a primary result, computational input or evidence of equivalence. The review is neither an additional trial nor independent treatment replication.

## Full-text access and source limits

- Publisher article, full-HTML and PDF routes could not be inspected; direct full-HTML/PDF requests returned HTTP 403. Search indexing exposed the abstract and the names of two publisher supplemental documents, marr3131.doc and marr3132.doc, but their contents and purpose were not verified. No supplement URL was guessed or document downloaded.
- Europe PMC returned the correct DOI/PMID record: subscription-required DOI route; isOpenAccess=N, inPMC=N, inEPMC=N, hasPDF=N, no author manuscript. Its hasSuppl=N flag does not prove no supplements exist, since the publisher lists two.
- [OpenAlex W2105290131](https://openalex.org/W2105290131) reports closed access, no best OA location and no repository full text. These are discovery-service observations, not proof that no lawful copy exists anywhere.
- Exact-title/DOI, author-institution and publisher/index searches did not locate a verified accessible institutional manuscript. A ResearchGate result offered a request route rather than a full text. No request, sign-in, payment or access application was made.
- Before the NIHR corroboration was found, a search result from an unverified third-party upload mentioned a pain-specific item and table row. It remains solely a verification lead. The file was not fetched, its numerical cells were not accepted as input, and no source text or paper copy is included here.

The bounded stop rule remains triggered by unavailable lawful primary full methods/tables; access to a lawful secondary review does not satisfy that gate. There was no attempt to bypass publisher restrictions. This is an access result, not proof that the original investigators failed to measure pain.

## What remains unverified

The exact prerequisite is a lawfully accessible, complete primary methods/results/table version, plus any outcome-relevant supplements. It must allow these questions to be answered without participant-level records:

1. **Measurement:** Is pain a separate treated-tic intensity outcome? What are its wording, anchors, scale, recall window and validation? Is any interference item specific to pain, or only to tics? How is benefit separated from injection pain, local discomfort, weakness and other adverse effects?
2. **Applicability:** What are the eligibility criteria, age distribution, adult-only count, baseline tic and pain burden, and severe/persistent-adult coverage? Mixed adolescent/adult indexing is not an adult-only or severe-adult effect estimate.
3. **Denominators:** How many were recruited, randomized, assigned to each sequence and included for each outcome? Are multiple treated tics represented per person? What happened to withdrawals and missing/zero-baseline observations? Eighteen completers alone cannot answer these questions.
4. **Timing and carryover:** What were the period length, assessment schedule, minimum washout or return-to-baseline rule, actual delays and crossover eligibility? How were sequence, period and carryover effects handled, and did any exclusion change the estimand? Week-two assessment alone does not establish those facts.
5. **Estimation and uncertainty:** What treatment contrast and direction does the pain table use? What is its outcome-specific paired sample, confidence interval or paired dispersion, analysis method and missing-data handling? Are multiplicity or outcome selection relevant? Were adverse effects likely to reveal assignment?
6. **Negative findings and governance:** What pain-specific negative or harmful findings, funding/conflicts, protocol/supplement details and correction notices exist? The abstract's general secondary-outcome statement cannot fill these gaps.

## Why no numerical pain check was executed

The necessary inputs did not pass source verification: a compatible pain endpoint, its valid denominator, paired crossover contrast, estimate/uncertainty and analysis definition. There is therefore no accepted pain input file, pain-effect program, fabricated standard error or inferred confidence interval. No participant data or synthetic clinical outcomes were used.

An arithmetic exercise on tic-frequency percentages would answer a different question. Nor is subtraction of marginal summaries a substitute for the trial's within-person crossover estimator. A nonsignificant pain claim from an unverified excerpt would not justify equivalence or the absence of clinically important benefit. The absence of a numerical analysis is the prespecified access-gate outcome, not an unreported failed computation.

## Next safe informative question

Keep this trial closed until a lawful primary full text is supplied or newly available. If that prerequisite is met, resume the same endpoint audit and reconcile the secondary review’s pain item with the original measurement and analysis; do not restart from an assumption of absence. No immediate clinical action, new participant collection or family data is needed.

A distinct candidate, **not audited here**, is whether the adult naturalistic registry report [Toxin for Tics, DOI 10.1002/mdc3.14296](https://doi.org/10.1002/mdc3.14296) measures pain intensity/interference independently of tic severity and continued treatment. First check prior project coverage to avoid repeating work. Its observational design would require a separate causal-limit assessment even if a pain endpoint exists. This suggestion does not authorize outreach or treatment.

## Provenance and completion

[Extraction status](extraction.json), [search/access log](search-log.json) and [source metadata](provenance.json) preserve the boundary between verified primary-abstract facts, inspected secondary evidence, discovery leads and unavailable primary methods. The official metadata had a linked editorial comment, not a correction/retraction classification; a focused DOI/title notice search found no correction or retraction. This is not comprehensive clearance.

Only original analysis and source identifiers are saved. No unlicensed paper copies, participant-level data/quotes, clinical instructions, GitHub writes, payments or external communications occurred. Independent review, if supplied, is a review of this access and inference boundary, not verification of inaccessible trial tables or clinical peer review.
