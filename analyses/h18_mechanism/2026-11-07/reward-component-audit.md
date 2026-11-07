# Reward-component audit: Rotstein et al. (2024)

The final published paper was inspected, not just the preprint. This is a public aggregate-evidence audit, not treatment advice. No participant files or patient-level rows were accessed.

## Published results and component

Source: [Wiley full text](https://movementdisorders.onlinelibrary.wiley.com/doi/full/10.1002/mds.29875), §§1.2, 2.2–2.6, 3.1.

ICR tied longer tic-free intervals to better dice, chests/cards and weaker opponents; DR randomized game outcomes. Both provided end-session feedback.

- In-game ITI endpoint: ICR **+1442±2250%**, DR **+242±493%**; Z=4.19, P=.0000285, d=.57. Learning-rate contrast: t(67)=3.15, P=.0025. Daily-change analyses were weaker.
- Clinical component contrasts: Rush favored ICR, t(47)=3.47, P=.002, FDR=.03; **YGTSS P=.98; PTQ P=.42**. Urge contrasts were nonsignificant.
- Combined-protocol YGTSS: **18.8±5.89→14.17±7.21**; individual reduction **25.69±23.39%**, d=.95. Three-month PTQ reduction: **42.99±31.69%**. These are SDs, not confidence intervals.
- Booster versus stopwatch ERP: no differential PTQ improvement, including pre-booster→three-month comparison, P=1.
- Sequence affected learning; AUC showed condition×order interaction. Authors acknowledge possible suppression during brief Rush observation rather than spontaneous-tic improvement.
- No systematic adverse-event accounting located in the main text. Supplement retrieval failed with HTTP 403; supplement-specific harms details remain unverified.
- Comparisons against group-CBIT/education used a different study, not concurrent randomized arms.

## Exact registration and assignment

Sources: [ClinicalTrials.gov record](https://clinicaltrials.gov/study/NCT06348511), verified using its [public API](https://clinicaltrials.gov/api/v2/studies/NCT06348511).

- Actual enrollment: **35**, ages **7–15**; crossover with randomly ordered ICR/DR weeks. Each condition involved three training days. Clinical assessments occurred at baseline, beginning of week 3, and beginning of week 5.
- Eligibility required YGTSS≥11 and screening frequency >1 tic/minute. Exclusions included potentially physically harmful tics, recent behavioral treatment, unstable medication and specified severe psychiatric/neurological histories. These restrict population transportability.
- Rush comprised two 2.5-minute resting recordings, with instructions **not** to suppress tics.
- Actual study dates: **July 1–December 31, 2022**. First submitted **March 21, 2024**, first posted **April 4, 2024**: ClinicalTrials.gov registration was retrospective.

## OSF protocol qualification

Sources: [AF74W](https://osf.io/af74w/), verified using [registration metadata](https://api.osf.io/v2/registrations/af74w/).

Registered **December 10, 2022**, after reported July–September recruitment. The registration describes registration before analysis, not before recruitment. It specifies randomized crossover sequence and **separate randomization** to two additional gamified booster sessions versus standard stopwatch-based ERP.

Its detailed blinding answer clarifies that clinical assessors and Rush video annotators were blinded, while **participants and real-time tic coders could not be blinded**, despite broader checkbox wording. The planned analysis included only participants completing all six sessions. Random-sequence generation and concealment details were not established from the retrieved registration text.

## Audit interpretation

This is a joint manipulation of contingency, timing and performance-linked gameplay, not a factorial isolation of any one of them, nor direct evidence about dopamine or negative-reinforcement mediation. A crossover involving a learned skill cannot assume learning washes out between periods. Combined pre/post and follow-up changes cannot identify the added ICR component, and nonsignificant clinical contrasts do not establish equivalence. Outcome-specific missingness and the absence of contrast confidence intervals further limit precision.

## Provenance note

Extraction completed in this research session on 2026-11-07 UTC. Exact timestamps of the original source checks were not retained. Artifact assembly time is recorded separately in `reward-component-sources.json`, without representing it as a source-check timestamp. Only this extraction and compact structured provenance are saved; no source full text, supplements or participant files are included.
