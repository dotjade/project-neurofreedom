# Project NeuroFreedom

## Why this project exists

I am a parent supporting a child who lives with Tourette syndrome. This site grew from a simple, personal wish: to understand my child's experience better and find thoughtful ways to support their comfort, confidence and wellbeing. My child is so much more than their tics. I hope this project can offer understanding and reliable information for other individuals and families navigating similar questions, with compassion and respect for each person's experience.

It is also intended as a growing research resource for human researchers and AI agents, including more capable agents in the future. By bringing together source-linked evidence, research notes, open questions and the limits of what is known, this site can give them a useful starting point: a way to quickly understand what has been collected and examined so far, check the original sources, and build on the work. The hope is that each new researcher or agent can spend less time retracing the same ground and more time asking better questions and advancing our understanding.

## How this project works

This is a parent-initiated, AI-assisted research notebook. Behind the site, AI agents help search published research, examine the evidence, explore specific questions and record what they actually learn. The repository holds the detailed work; [tourette.fyi](https://tourette.fyi/) presents a more approachable public journal of it.

No research laboratory is affiliated with this project. If you are a researcher or part of a lab and this collection helps you find useful past research, evidence or connections, please consider quoting or citing the relevant project notes and sharing a link to help spread the word. Please also cite the original studies and their authors, whose work this collection brings together. The hope is to help valuable research reach more people and support further investigation.

The work follows a repeatable cycle:

1. **Find relevant evidence.** Search scientific publications, clinical-trial registries and official sources, including negative results and findings that challenge an idea.
2. **Check what each source really shows.** Record the study population, methods, results and limitations. Keep observations, hypotheses and demonstrated effects distinct, and make the original sources easy to find.
3. **Investigate one focused question.** Compare studies, test an interpretation or run a reproducible analysis when suitable data are available. Work using simulated data is labelled clearly; a successful simulation is not a finding about people.
4. **Leave a traceable record.** Save dated notes, evidence records, code and results, including uncertainties, failed ideas and missing information. This gives the next researcher or agent a place to continue without starting over.
5. **Share a readable summary.** The site's journal reads a public summary feed from this repository. The detailed notes and source links provide the context behind those summaries.

The [research protocol](RESEARCH_PROTOCOL.md) sets out daily evidence checks, weekly syntheses, monthly reviews and quarterly strategy reviews. These are separate research runs, not continuous activity: the dated records show what was actually completed. The [status record](STATUS.md) and [research updates](updates/) explain progress and unresolved questions; the [publication workflow](public/UPDATE_WORKFLOW.md) explains how summaries reach the site.

The aim is cumulative understanding that people and future agents can verify and build on. This work does not replace clinical care, and research notes or AI-generated hypotheses do not establish a treatment or a cure. No personal health records are needed for this evidence-review workflow.

## Where to start

- **For people:** start at [tourette.fyi](https://tourette.fyi/) for an approachable introduction and public research journal. For more detail, explore the [research portfolio and investigation reports](RESEARCH_OVERVIEW.md).
- **For AI agents and researchers:** use this repository directly. Read the [research protocol](RESEARCH_PROTOCOL.md), [status record](STATUS.md) and [latest dated updates](updates/) first, then follow the [evidence records](evidence.jsonl) and original sources. Clone the repository to examine the notes, run documented analyses and build on the work:

  ```sh
  git clone https://github.com/dotjade/project-neurofreedom.git
  ```

## Contribute evidence or a correction

People, researchers, laboratories and AI agents are welcome to suggest a missing study, correct an interpretation, share a reproducible analysis or improve an explanation.

[Submit a contribution using the GitHub issue template](https://github.com/dotjade/project-neurofreedom/issues/new?template=contribution.md). Include a source link or relevant file, explain what you found and why it matters, and note any uncertainty. For an analysis, include instructions that let someone reproduce it. Check [existing issues](https://github.com/dotjade/project-neurofreedom/issues) first to avoid duplicating a suggestion.

A maintainer checks the source, incorporates supported additions and acknowledges useful contributions. Discussion is only needed when clarification would help. **Pull requests are optional:** you can submit a suggestion without editing files or using Git. If you prefer to supply an exact edit or code change, a pull request is welcome. AI agents can use the same contribution format.

Please share public research sources and original summaries. Keep personal medical records, identifying health stories and unlicensed full-text papers out of issues and attachments.

## Working research record

- [Research protocol and planned update cycle](RESEARCH_PROTOCOL.md)
- [Structured primary-study evidence](evidence.jsonl)
- [Community perspectives and safeguards](COMMUNITY_EVIDENCE.md)
- [Version and execution status](STATUS.md)

## Privacy and reuse

This is a public research resource. No patient-specific medical records, family identifiers, personal images, diary entries or genetic data belong here. Store original evidence summaries and source identifiers. Do not upload unlicensed full-text papers or private community content. This repository is not a clinical-data system.

## How to continue

Read the protocol and latest status first. Verify the latest source and repository version before changing claims. Add evidence with provenance and retain contradictory and negative findings. Record what was actually done, what is only proposed, and what is blocked. Do not claim data access, an analysis, collaboration or scheduled research is active until verified.
