# Proposed open Tourette research collaboration

8 October 2026 | Proposal version 0.1

## Purpose and current status

A worldwide community could contribute literature reviews, research questions, translations, software and reproducible analyses to Project NeuroFreedom. The practical starting point is a carefully reviewed public-science workstream. Any future collection of participants' experiences or health information would be a separate, institutionally governed research workstream.

**This is a proposal stored in the existing private project workspace. No public launch, repository visibility change, external sharing, outreach, recruitment, partnership or participant data collection is authorised by this document or has been performed for this proposal.** Roles below are proposed responsibilities, not appointments or commitments. The project does not claim a cure has been found or promise one on a timetable.

The proposal complements [RESEARCH_PROTOCOL.md](RESEARCH_PROTOCOL.md), [COMMUNITY_EVIDENCE.md](COMMUNITY_EVIDENCE.md) and [STATUS.md](STATUS.md). Existing clinical and privacy boundaries continue to apply.

## First bounded deliverable

Prepare one versioned evidence map of tic waxing and waning, candidate antecedents, developmental improvement and remission, using published research and aggregate results. Begin with what distinguishes a reproducible precursor from a concurrent correlate or a misleading apparent cycle. This follows the project's current scientific priority and needs no new participant data.

The proposed first release would contain:

1. A documented search scope and screening log, starting with the longitudinal studies already catalogued in the project.
2. A structured extraction of fluctuation timescale, candidate predictor timing, symptom and impairment measures, age, observation method, follow-up interval, treatment status, attrition, recurrence and functional outcomes.
3. A comparison of self-reported and observed outcomes, explicitly noting where definitions or populations make pooling inappropriate.
4. A short, source-linked explanation for non-specialist readers, including contradictions and remaining uncertainties.
5. A reproducible extraction template, any analysis code actually executed, and synthetic test fixtures. Proposed analyses must remain labelled as proposed.
6. A review log identifying material corrections, unresolved disagreements and the limits of source access.

Completion means that every included study has traceable provenance, every material numerical claim has been checked against its source, a second reviewer has checked key extractions, and remaining gaps are recorded. It does not mean that a systematic review, meta-analysis or clinical discovery has been completed. If no second reviewer has been appointed, the deliverable remains a draft awaiting that review.

The stopping point is a reviewed evidence-map release candidate. Public release needs the separate owner approval described below; it is not an automatic consequence of finishing the draft.

## Proposed stages

### Stage one  Prepare public science contributions

Keep preparation private until the project owner approves a specific public release. Establish a contribution guide, evidence template, code review rules, correction process and moderation policy. Volunteers could propose citations, check extractions, translate approved summaries, test code and challenge hypotheses. Use original summaries and permitted source links rather than unlicensed copies of full papers.

Every contribution should distinguish established findings, observational associations, preclinical results, hypotheses and unknowns. Contributor counts, anecdote counts and community votes must not be used as evidence that a treatment is effective. Repository issues must not become a patient intake form.

### Stage two  Establish community and research leadership

Seek, after approval of the specific outreach, a partnership with an appropriate university, hospital or established research organisation. Form a small advisory group including adults with Tourette syndrome and carers. Include young people's perspectives only through a suitable, supported and consent-aware process; adult or parent perspectives do not automatically represent them.

The group would help decide which question is important, what participation burden is acceptable, which outcomes matter and how results should be returned. Its involvement should not quietly become a dataset of personal medical experiences. If conversations will be recorded, systematically analysed or quoted as research data, obtain an institutional determination and the appropriate consent and review first.

Select one future study question and explore whether existing appropriately licensed or controlled-access data can answer it. No existing dataset is assumed to be available merely because a paper describes it.

### Stage three  Pilot governed participant research

Only after a research partner accepts responsibility and the required reviews are complete should the project invite people to contribute experience or health data for research. Begin in a defined jurisdiction or set of approved jurisdictions, with a narrow question, protocol, eligibility criteria and analysis plan. Global contribution to literature and code can begin independently of global health-data recruitment.

Prefer an existing institution-approved research system to building a custom registry first. Determine what information is actually necessary; minimise free text and avoid images, video, genetics and medical-record uploads unless they are essential to a specifically approved protocol.

The protocol should address selection bias, missing data, participant burden, safety reporting, withdrawal, analysis limitations and return of results. Recruitment through social-media groups alone cannot establish a representative global sample. Reports of improvement cannot on their own distinguish treatment effects from natural fluctuation, concurrent changes or regression to the mean.

### Stage four  Expand only after the pilot is reviewed

Add countries through suitable local partners and review arrangements, with accessible participant information and appropriately translated or validated measures. Resolve applicable research requirements, privacy obligations and international data transfers for each expansion. Review the pilot's feasibility, inclusion, data quality and burden before enlarging it. There is no universal cross-border approval implied by an initial ethics decision.

## Proposed contributor roles

- **Project owner and coordinating maintainer:** define scope, approve spending and external releases, maintain a decision log and ensure that commitments have named owners.
- **People with lived experience and carers:** help set priorities, identify burdens and accessibility needs, review participant-facing materials and interpret relevance. They should have a meaningful say in decisions and suitable recognition or compensation where possible.
- **Clinical research lead and institutional sponsor where applicable:** assess clinical relevance, accept scientific responsibility, arrange institutional determinations and required ethics review, and oversee participant research.
- **Evidence reviewers:** search, screen and extract published findings; independently check key results and preserve negative or contradictory evidence.
- **Methods specialist:** check study design, confounding, sample-size justification, missingness, measurement validity and statistical interpretation.
- **Developers and reproducibility reviewers:** maintain versioned code, tests, synthetic data and reproducible environments. Coding privileges do not grant access to participant records.
- **Data steward and institutional privacy/security team:** define the data controller and custodians, access rules, storage, retention, transfers, incident handling and disclosure review.
- **Moderators and accessibility/translation contributors:** enforce participation rules, remove unsafe disclosures through an agreed process, handle complaints and make approved material understandable across languages.

One person may cover compatible roles in an early literature-only phase. Responsibilities for research governance and participant privacy cannot be assumed to exist because volunteers are available.

## Moderation and scientific quality

Before opening participation, name moderators, an escalation contact and a response process. Publish a concise code of conduct with the following boundaries:

- No identifiable health histories, children's records, contact details, faces, genetic data, private messages or copied private-group posts in repository issues, discussions or pull requests.
- No instructions to change medication or conduct unsupervised experiments, and no personalised diagnosis or treatment advice.
- No cure claims, fabricated citations, unsupported efficacy claims, commercial recruitment or harassment. Require conflict-of-interest disclosure.
- Personal observations can suggest research questions, but detailed stories must not be solicited in public contribution channels. A public post is not blanket permission to reuse someone's health information.
- Use review before merging scientific claims. Clinically consequential statements need appropriate expert review. Preserve a visible correction history without preserving exposed personal information.
- If sensitive information is posted accidentally, restrict exposure promptly under the agreed policy, refer it to the responsible privacy team and address cached copies, notifications and repository history where relevant. Do not promise that public disclosure can be completely reversed.

Any future social-media recruitment needs both the relevant community administrator's permission and the research team's approved invitation and process. Group access or administrator approval does not substitute for each participant's consent. Private groups must not be scraped or exported for this project.

## Public and private information separation

**Eligible for a future approved public release:** original literature summaries, source identifiers and permitted links, evidence-review methods, hypotheses, protocols cleared for release, data dictionaries without records, code, synthetic examples and privacy-reviewed aggregate results.

**Restricted research system only if specifically approved:** consent records, participant contact details, study IDs and linkage keys, questionnaires, interview recordings, health histories and other individual-level research data. Keep contact information and re-identification keys separate from analysis datasets, with least-privilege access and an audit trail. This category belongs outside GitHub, including private GitHub repositories.

**Not collected by default:** private community archives, direct identifiers beyond necessary administration, child images or videos, detailed family histories, genomic information and medical records. Any later need requires an amended protocol and the corresponding approvals and permissions.

Removing names is not enough to guarantee anonymity. Distinctive narratives, small groups and linked attributes can enable re-identification. Controlled access may remain necessary for de-identified data. Do not promise public release of raw participant data as a condition of being an open-science project. NIH guidance specifically supports evaluating access controls even for de-identified data.[4]

Before consent, explain the intended uses, who can access data, any commercial involvement, secondary uses, retention, withdrawal options and the limits of removing information after lawful analysis or publication. Do not promise withdrawal mechanisms the eventual system cannot implement.

## Required human decisions and approvals

The following are decision gates, not evidence that approval already exists:

1. **Before public release:** the project owner approves the exact material, destination, visibility and licence. Review the selected files and relevant repository history for private information, permissions and copyright. Prefer a deliberately curated public release rather than assuming that the entire private repository is suitable for publication.
2. **Before contacting anyone:** the project owner approves the specific recipient or organisation, purpose and message. A reviewed invitation and any necessary group-administrator permission must precede recruitment. No invitation is drafted or sent as part of this proposal.
3. **Before collecting research data:** a named institutional research lead and sponsor where applicable accept their roles; the institution determines whether the activity is human-subject research and identifies required ethics, regulatory and site approvals. A written determination is needed if an exemption or non-research classification is relied on.
4. **Before participant enrolment:** the research team obtains approval for the protocol, recruitment materials and consent process, including parental permission and age-appropriate affirmative assent where applicable. Any exception or waiver must be determined by the appropriate authority. A parent's willingness to share does not remove a child's privacy interests.[3]
5. **Before configuring data collection or sharing:** the institutional data/privacy and security leads approve the storage platform, controller/custodian responsibilities, access permissions, legal basis, retention, transfer arrangements and applicable agreements. Research consent and data-protection requirements must both be addressed.
6. **Before intervention or clinical recommendations:** establish a separate clinician-led, appropriately reviewed protocol and necessary approvals. Experience gathering does not authorise medication changes, devices, supplements, stimulation or other experiments.
7. **Before expanding scope:** obtain the required approval for new countries, populations, data types, secondary uses, collaborators or publication of sensitive results. Confirm consent coverage and perform disclosure review before releasing aggregates or illustrative quotations.

## Public involvement and human subject research

Helping choose research priorities or improve a study design is different from being studied. The UK Health Research Authority states that public involvement in research planning or design does not itself need an application for HRA ethical approval.[1] This is useful guidance for a UK setting, not a worldwide exemption.

US OHRP guidance describes research in terms of systematic investigation designed to contribute to generalisable knowledge and explains the additional question of whether it involves human subjects.[2] A questionnaire or systematically analysed set of personal stories can meet relevant research criteria even when labelled citizen science, observational or anonymous. Definitions, legal coverage and review routes vary. The future partner institution must classify the actual activity in its jurisdiction rather than relying on the project's label.

## Existing routes worth evaluating

Tourettes Action describes a process for helping researchers recruit through its supporter network. Its current guidance asks for ethical approval or a support letter, a participant information sheet and a consent form, and asks researchers not to approach its local groups directly.[5] This is a possible partnership route to investigate, not a collaboration already arranged.

The Tourette Association of America lists research opportunities and provides a submission route for research teams.[6] These existing networks should be considered before creating a new recruitment infrastructure. A listing does not establish current eligibility or recruitment status; confirm those with the study team and registry when relevant.

## Costs and dependencies

The first evidence map can be scoped around volunteer effort and existing research tools, but it still requires time for coordination, source access, moderation and independent review. Do not assume those resources have been committed.

A participant-research phase needs a budget for institutional support, research staff, secure storage and collection, governance, methods support, community involvement, participant reimbursement where appropriate, translation/accessibility and ongoing stewardship. Scope and partner arrangements are needed before a credible total cost or launch date can be estimated. No funding, procurement, timetable or custom-platform build is committed here.

## Sources

Sources checked 8 October 2026. The staged design and governance choices above are recommendations informed by these sources; they are not claims of a universal legal rule.

1. Health Research Authority. [Public involvement guidance for researchers](https://www.hra.nhs.uk/planning-and-improving-research/best-practice/public-involvement/guidance-for-researchers/). UK guidance on involvement in planning/design and its distinction from research participation.
2. US Office for Human Research Protections. [Lesson 2 What is Human Subjects Research](https://www.hhs.gov/ohrp/education-and-outreach/online-education/human-research-protection-training/lesson-2-what-is-human-subjects-research/index.html). US regulatory concepts and institutional decision context.
3. US Office for Human Research Protections. [Research with Children FAQs](https://www.hhs.gov/ohrp/regulations-and-policy/guidance/faq/children-research/index.html). Parental permission, affirmative assent and review responsibilities under the applicable US framework.
4. National Institutes of Health. [Designating Scientific Data for Controlled Access](https://www.grants.nih.gov/policy-and-compliance/policy-topics/sharing-policies/dms/privacy/designating-scientific-data-controlled-access). Privacy assessment and controlled access, including for de-identified data.
5. Tourettes Action. [Support with your research](https://www.tourettes-action.org.uk/136-support-with-your-research.html). Recruitment support, required materials and contact process.
6. Tourette Association of America. [Research Studies](https://tourette.org/research-medical/research-studies/). Examples of institution-led participation and a route for study listings.

