# Pain interference in a pain-selected mixed-age survey

Project NeuroFreedom | 18 October 2026 | Historical primary-study audit

## Decision

Taylor, Anderson and Davies (2022) document pain-related interference in a **self-selected sample already experiencing tic-related pain**. Their 181 respondents aged 16–71 are not an adult-only sample or a denominator for pain prevalence. The report adds a clearly bounded **past-week interference** measure to the October 17 pain-intensity audit, but adult-specific interference estimates remain unavailable.

A reproducible audit finds that all 13 published tic-interference means exceed the corresponding pain-interference means, by 0.05–1.12 points on the adapted 1–5 scale. These are **differences between reported marginal means**, not established paired effects, clinically meaningful differences or evidence that pain matters less to every respondent. Unreported item denominators and N/A handling prevent stronger interpretation.

## Source and ascertainment

[Taylor et al., Frontiers in Psychiatry 13:914044](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2022.914044/full), DOI [10.3389/fpsyt.2022.914044](https://doi.org/10.3389/fpsyt.2022.914044), [PMID 35990066](https://pubmed.ncbi.nlm.nih.gov/35990066/), PMC9388784. Published **5 August 2022**; survey open **10 June–13 July 2021**. This is a historical audit, not a new October publication.

Eligibility required age at least 16, suspected or confirmed tic disorder, current tics and current tic-related pain, and ability to read and write English. Recruitment used patient-association websites/social media, an online support community and research-related social-media circulation. Four of eight contacted national charities agreed to advertise; advertisements were also circulated to 47 support associations. This is neither a population sampling frame nor recruitment independent of pain.

The survey took approximately 30 minutes. The article reports 181 completed responses from 18 countries and says outcome data were not missing, but does not report total advertisement exposure, survey starts, exclusions, dropouts or a response rate. Formal diagnoses were self-reported rather than independently established. The authors themselves state that prevalence was not the study's aim. Pain attribution was also self-reported; other pain conditions were allowed. No severe-persistent-adult eligibility threshold or longitudinal severity trajectory was established. [Source: methods, Table 1 and limitations.](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2022.914044/full)

## What the interference scores mean

The authors adapted seven Brief Pain Inventory interference domains, expanded them to 13, and separately asked about tics and tic-related pain. Both sets concern the **previous week**. Scores run from 1 (no interference) to 5 (severe interference), with an N/A option. These are study-specific ratings; validation of the expanded instrument, full question stems, middle response labels and a clinically important difference were not supplied in the checked public material. The exact awkwardly worded endpoint labels are preserved in the [source-method review](review/independent_review.md), rather than silently rewritten as a recovered questionnaire.

Table 3 reports means and SDs but no item-specific valid counts, N/A counts, exclusion/coding rules or matched tic/pain counts. The blanket statement of no missing outcome data does **not** establish that every mean uses all 181 people or that the same people contribute to each side of a contrast. General daily work, education and employment are separate domains. No total or composite interference score is reconstructed.

The highest reported pain means were mood **3.31 (SD 1.24)**, sleep **3.24 (1.40)** and enjoyment of life **3.04 (1.32)**. The highest tic mean in the table was social situations **3.86 (1.07)**. These domain summaries are distinct from pain intensity, tic severity measured by the Adult Tic Questionnaire, a validated quality-of-life endpoint, or treatment response. A past-week interference window does not establish duration-defined chronic pain. Help-seeking, techniques used and perceived treatment impact have no explicit bounded recall window in the described questions. [Source: survey methods and Table 3.](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2022.914044/full)

## Executed aggregate audit

The [pre-extraction decision rule](prediction.md) predicted that ascertainment and age mixing would prevent representative adult estimates. The public report supports that limitation, while providing a positive measurement finding: interference has an explicit one-week window.

[Inputs](aggregate_inputs.json), [code](aggregate_checks.py), [results](aggregate_checks.json), [25 passing implementation tests](test_aggregate_checks.py) and the [execution log](execution_log.txt) reproduce:

- **13/13 positive differences between printed tic and pain means.** The smallest is enjoyment of life, 3.09−3.04=0.05; the largest is social situations, 3.86−2.74=1.12. All remain positive under conservative envelopes for ordinary rounding at each printed precision. Rounding envelopes are not confidence intervals.
- **140 respondents aged 19 or older**, plus **41 in the combined 16–18 band**. The number aged at least 18 is unknown. Subtracting the whole youngest band would incorrectly discard 18-year-old adults; counting everyone as adult would include minors. No adult estimate is imputed.
- A **help-seeking reporting conflict**: Table 5's categories imply 71+46=117 seekers, and the provider header also says 117. Prose instead says 118. The printed 64.6% matches 117/181 after rounding, whereas 118/181 is 65.2%. For receipt of help, 71/117 is 60.7% and 71/118 is 60.2%; neither ordinarily rounds to the prose's 60.1%. Table counts for general doctors/physiotherapists are 60/42, versus 61/43 in prose. No corrected denominator is adopted.

The main gap result is descriptive counterevidence to any blanket claim that pain scores exceeded tic scores across domains. It does not contradict qualitative reports that pain was the more pressing problem for some people. Without matched observation sets and paired dispersion/covariance, no paired test or confidence interval is justified. Clinical materiality is also unknown. Receipt of help is not relief, satisfaction, or efficacy.

Two additional Table 3 inconsistencies remain visible: the prose's list of highest tic-interference domains omits the table's highest domain, social situations; tic-related sleep SD is 1.21 in prose versus 1.31 in the table. The table values were retained as extracted values, not declared corrections. [Source: results and Tables 3 and 5.](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2022.914044/full)

## Qualitative findings and negative evidence

Inductive thematic analysis described perceived links between tics and pain, physical and emotional burden, support/access problems and varying usefulness of pain-management approaches. One researcher led coding with another discussing/refining themes. These are interpretations of volunteered narratives, not coded population prevalence, verified diagnoses or tested causal pathways. The proposed tic–pain feedback cycle has unresolved timing; no time-series or intervention test establishes it.

Variation matters: accounts included more tolerable pain and differing experiences of care. Medication and behavioral therapy were not uniformly reported to relieve pain; unchanged pain and worsening were also reported. The authors did not quantitatively measure satisfaction/appraisal of professional help. Neither technique-use frequency nor qualitative favorable accounts establishes comparative effectiveness. No individual quotations, case details, small-cell treatment narratives or participant records are reproduced. [Source: qualitative analysis, discussion and limitations.](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2022.914044/full)

## Comparison with the October 17 Małek audit

[Małek 2025](https://doi.org/10.3389/fpsyg.2025.1537088) recruited 76 adults aged 18–51 attending Polish support groups; 56 reported past-or-present pain. Its present/worst pain ratings and unclear care denominators answer different questions. Taylor's mixed-age online sample required current pain and reports past-week interference. These differences prohibit pooling a pain prevalence, intensity score, treatment-success fraction or adult interference estimate. Both reports support treating pain and its consequences as distinct research outcomes, while neither establishes representative severe-adult burden or causal care effectiveness. [Prior audit](../../adult_pain/2026-10-17/report.md).

## Missing prerequisite and next decision

Close this source audit unless public methodological clarification or corrected reporting appears. Adult-only descriptive interference requires **age ≥18 item-level valid counts, N/A counts and handling, means and dispersion**, separated from ages 16–17. Paired adult tic-versus-pain inference additionally needs the matched contributing count and covariance or difference-score dispersion. An overall age split alone cannot recover these outcomes. Representative prevalence would require a different, pain-unselected sampling design. No public blank questionnaire, age-specific table or linked dataset was located; data-on-request wording is not public data access or authorization to contact the authors.

A distinct next bounded question is whether a controlled focal-tic intervention actually measures pain benefit separately from tic improvement and procedure discomfort. Begin with [Marras et al. 2001, PMID 11245710, DOI 10.1212/WNL.56.5.605](https://www.neurology.org/doi/abs/10.1212/wnl.56.5.605), a randomized double-blind crossover botulinum-toxin trial. Its primary abstract lists tic counts, severity, urge, premonitory sensation and global change; pain interference is not listed there. Verify the lawful full methods, tables and related reports before concluding whether any pain-specific endpoint exists. Distinguish local/injection discomfort from benefit for tic-related pain, check adult and severe-presentation applicability, and preserve crossover timing/carryover and uncertainty. Stop this one-trial endpoint audit if the full methods are inaccessible or no compatible pain outcome is reported; do not infer pain relief from tic reduction. Only trial identity and the abstract endpoint list were checked today; no trial-effect analysis was performed.

## Provenance and governance

Publisher HTML, the [CC BY publisher PDF](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2022.914044/pdf) and [official Europe PMC XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9388784/fullTextXML) were checked; PDF pages 5–7 were visually verified. [Provenance](provenance.json) records source hashes, retrieval limits and checks. No linked correction/retraction was found in the bounded checks; this is not comprehensive clearance. NIHR funding and the authors' no-commercial/financial-conflict declaration are recorded in [extraction](extraction.json).

The public deliverables contain original summaries and aggregates, without source-paper copies, personal/family data, clinical instructions, outreach or cure claims. Independent source-method and arithmetic reviews are supplied under [review](review/). Passing tests validate this reporting audit, not the clinical study.
