# Three publications, two randomizations: weekly evidence-structure verification

Project NeuroFreedom | 18 October 2026 | Bounded historical literature reanalysis

## Decision

The three selected result publications resolve to **two independently recruited randomized trial clusters**. McGuire's functioning report adds outcomes from the Wilhelm trial; it does not add a new randomized replication. The analysis preserves acute tic benefit while rejecting automatic promotion of exploratory or selected follow-up findings to independently replicated, randomized functional benefit after verified cessation of structured treatment exposure.

This is an executed evidence-structure computation, not a clinical pooled effect, meta-analysis or new treatment result. It addresses a new synthesis-level bookkeeping question without rerunning the daily p-value corrections or missing-outcome bounds.

## Prediction and fixed coding rules

The [plan](prediction.md) was recorded before constructing the new input table and executing the code, after the existing daily conclusions were known. It is not a preregistered clinical hypothesis or a blind rediscovery. The fixed inclusion set was Haas/ONLINE-TICS 2022, Wilhelm 2012 and McGuire 2019-online/2020-issue. Protocol and registry records identify trials; they are not extra result reports.

Publication identity uses normalized DOI, then trial registration and explicit recruitment methods establish clusters. Titles, manuscript versions, online/issue years, repeated source URLs and multiple repository reports do not create new trials. Shared treatment names alone do not merge trials. Conflicting identifiers cause an error rather than a silent decision.

Eleven analyst-defined inference blocks organize the three publications. They are **not eleven author-prespecified endpoints, independent tests, studies, efficacy votes or a denominator for the field**. A block may contain several correlated tests. Test hierarchy, outcome, timing, comparison, selection and exposure are coded separately; nominal significance never supplies missing design requirements.

## Actual source mapping and counterevidence

- [ONLINE-TICS 2022](https://juser.fz-juelich.de/record/905141/files/jcm-11-00250-v4.pdf), DOI 10.3390/jcm11010250, is NCT02605902: 161 allocations, five German centers, 2016–2020 recruitment, ages 18–62. Its acute primary tic contrast missed superiority. Later favorable tic, impairment and disease-specific quality-of-life findings remain exploratory and visit-specific. Platform access continued through follow-up.
- [Wilhelm 2012](https://jamanetwork.com/journals/jamapsychiatry/fullarticle/1307556), DOI 10.1001/archgenpsychiatry.2011.1528, is NCT00231985: 122 allocations, three US centers, 2005–2009 recruitment, ages 16–69. Its acute primary tic-severity advantage remains supported: 3.3 points, 95% CI 1.4–5.2, p<.001. Acute impairment is a distinct nominal secondary finding. Maintenance concerns returning acute responders after a booster-inclusive program.
- [McGuire 2019/2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7190082/), DOI 10.1017/S0033291719002150, explicitly reuses NCT00231985 and its recruitment. Its 12 acute randomized functional contrasts did not establish superiority; two responder associations and selected follow-up findings answer different questions. These null contrasts do not establish equivalence or exclude important benefit.

The [ONLINE-TICS protocol](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2016.00119/pdf) requires primary superiority before confirmatory non-inferiority. Satisfying the displayed numerical margin alone does not reopen that gate. This preserves a second concrete counterexample to automatic promotion of a favorable result.

## Computed output

The [deterministic program](verify_structure.py) reads the [small original input table](aggregate_inputs.json), validates identifiers/provenance and returns the [actual output](aggregate_checks.json):

- Three distinct result publications; two randomized trial clusters.
- Two audited primary contrasts: one demonstrated superiority and one did not. This is not a pooled success rate; interventions, populations and comparators differ.
- Eleven inference blocks: one supported primary; one missed primary; three exploratory randomized blocks with positive findings at some visits; one closed confirmatory gate; one nominal secondary randomized positive; one selected-responder maintenance block; one randomized functional block without demonstrated difference; one responder-association block; one selected within-group follow-up block.
- Counting each publication's parent enrollment would repeat 122 allocations: 405 report-level slots versus 283 trial-level slots. These are accounting quantities, not an analysis sample, an adult-only sample, a pooled denominator or a verified unique-person census across trials.
- Neither cluster documents all requirements for a favorable randomized functional follow-up comparison after verified cessation of platform/booster exposure. This remains true even without requiring confirmatory multiplicity control or adult-only inclusion.

The last finding is a documentation predicate for a **stronger claim**, not proof that benefit disappears when treatment ends. It does not downgrade useful benefit under continuing access, require a person to stop practicing learned skills, or recommend stopping treatment. Function, clinician-rated impairment and disease-specific quality of life remain distinct measurements.

## Verification and falsification controls

Twenty-four implementation checks passed. A duplicate publication with a different year/DOI URL form adds neither a publication nor a trial. A clearly labelled hypothetical distinct trial adds a cluster, demonstrating that the code does not merge everything sharing a treatment. A conflicting same-DOI trial assignment is rejected. Unknown requirements cannot be silently promoted to true, while a hypothetical fully verified record can pass the claim predicate.

The positive control retains Wilhelm's acute efficacy result. The empirical cross-domain counterexample is that the same trial's functional contrasts do not automatically inherit that result. This is a counterexample to **inferential substitution**, not evidence of individual-level discordance, a zero causal effect, or proof that tic improvement cannot improve function.

These tests verify mechanical consistency of the specified coding rules. They cannot validate subjective source interpretation, detect every reporting error or provide clinical peer review. Primary recruitment/methods, hierarchy, exposure and selected endpoint facts were separately checked against readable original sources, with access limits in [provenance](provenance.json). The parent reviewer reran the program and reported byte-identical output plus five separate count/status assertions, with code and coding reviewed against the prior primary audits. This is parent reproduction and source/interpretation review, not independent clinical validation; see [verification record](parent_reproduction.json).

## Limits and stopping condition

This bounded set is deliberately selected from three completed daily audits, not a systematic search or complete behavioral-treatment literature. Other trials, outcomes, harms and patient-important thresholds are outside the table. Uncertainty intervals and joint participant outcomes were not reconstructed. Missingness and selection remain clinical interpretation limits even where a randomized contrast is retained. Mixed-age CBIT results cannot become severe-adult estimates by deduplication.

The computation is complete. Reopen only for a corrected identifier, material source correction, newly verified exposure/endpoint information, or an explicitly expanded evidence set with a revised coding plan. No participant records, single-participant cells, paper copies, simulation, medical intervention, outreach, paid resources or GitHub writes were used.
