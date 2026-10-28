# Controlled perturbations: control points are not necessarily root causes

Project NeuroFreedom | Executed targeted causal synthesis | October 28, 2026

## Bounded question and prediction

Does response to dopamine-related drugs or stimulation identify a universal transmitter leak, or only show that tic expression can be changed through particular control points?

**Prediction stated for this synthesis, after awareness of the literature:** if a strong pharmacological version of a universal excess model is adequate, interventions that reduce its proposed signaling should show consistent benefit in the tested populations, with verified engagement, and improvement should track that engagement. A heterogeneous-network model instead permits differing responses across targets, ages, timescales and burdens. Both models can accommodate average symptom improvement. Without specifying transmitter, compartment, concentration or dynamics, and a quantitative response prediction, a “leak” cannot be falsified by these trials.

The current data do **not** identify a unique upstream defect. They support modifiable symptom expression and constrain some overly broad predictions. Heterogeneous network control remains a useful research framework, not a mechanism proven merely by mixed trial results.

## Methods and novelty boundary

Ten purposively selected peer-reviewed controlled trials span D1 modulation, D2-active pharmacology, VMAT2 inhibition, severe-adult pallidal DBS, peripheral stimulation and cortical stimulation. Eight official registry records were checked directly on October 28. This is a causal contrast set, not a systematic review, class-wide efficacy synthesis or treatment ranking. The structured [trial records](trial-records.json) carry populations, denominators, comparators, timeframes, endpoints, selected estimates, harms and source links. [Registry metadata](registry-checks.json) is not independent replication.

The repository already covered ecopipam maintenance, both MNS trials, DBS observational outcomes and the general distinction between treatment and cure. The earlier [MNS attrition calculation](../../../mns_attrition/report.md) is not rerun or presented as new. Today's added value is the typed perturbation comparison, preserved negative and conflicting trials, quantitative limits on a strong prediction, and explicit prerequisites for causal discrimination. No claim that these papers or ideas were previously overlooked is made.

Primary public pages and ordinary anonymous HTTP retrieval were used. Web-reader challenges and successful direct retrieval sometimes differed. No access bypass, full-text archive, participant-level reconstruction, patient narratives or proprietary dataset was used. No dedicated exhaustive correction/retraction search, registry-version audit, complete supplement extraction or formal bias grading was performed. The exact search strings and access limits are in [methods](methods.json).

## What the contrasts actually discriminate

### 1. Dopamine-related efficacy is not a dopamine assay

The pediatric [ecopipam initiation trial](https://publications.aap.org/pediatrics/article/151/2/e2022059574/190459/Ecopipam-for-Tourette-Syndrome-A-Randomized-Trial) and [aripiprazole trial](https://pmc.ncbi.nlm.nih.gov/articles/PMC5689110/) support placebo-controlled average symptomatic effects. They do not measure an endogenous excess or prove that the therapeutic target is the initiating lesion. Aripiprazole's multiple receptor actions also prevent treating it as a selective D2 experiment. Drug effects could alter downstream gain, selection or compensation even if the initiating vulnerability differs. Those alternatives are hypotheses, not demonstrated mediation.

The [2026 ecopipam withdrawal trial](https://jamanetwork.com/journals/jamaneurology/fullarticle/2849573) asks whether selected responders maintain benefit, not whether everyone initially benefits. Its adult subgroup is small and uncertain. Selection for response and tolerability means neither pediatric efficacy nor maintenance safety automatically generalizes to persistent severe adults, comorbidity-excluded groups or people who discontinued before randomization. Continued-treatment benefit is not treatment-free disease modification.

### 2. VMAT2 failures put a numerical boundary on a simplistic prediction

[ARTISTS 1](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2784765) and [ARTISTS 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC8524312/) are separate negative pediatric trials, not failed case anecdotes to remove from the map. Their printed confidence intervals both include no difference, but neither includes an average placebo-adjusted benefit of five TTS points or greater under the tested conditions.

The executed [interval audit](interval-results.json) compares four **illustrative, nonclinical** thresholds with each reported interval. A three-point benefit remains compatible with both; a four-point benefit remains compatible with ARTISTS 1 but not ARTISTS 2; five and 6.5 points are outside both intervals. These are marginal reported intervals, not simultaneous familywise confidence statements, posterior probabilities, a meta-analysis or individual-response predictions. The thresholds were selected after seeing the estimates and are not preregistered minimum important differences.

Thus the operational claim “every tested dopamine-lowering regimen yields at least five average TTS points beyond placebo in these pediatric settings” conflicts with both reported intervals. This does **not** refute all dopamine involvement or every possible leak model. No individual CNS engagement/mediation assay here proves that the hypothesized excess was corrected. Exposure, anatomical specificity, receptor adaptation, outcome timing and population heterogeneity remain alternative explanations. Calling the negative trials “only placebo response” without testing those alternatives would protect the hypothesis from falsification.

### 3. Adult surgical results must not be averaged into pediatric pharmacology

The [2015 GPi crossover](https://pubmed.ncbi.nlm.nih.gov/25882029/) found a small-sample on/off advantage; the [2017 anterior-GPi parallel sham trial](https://pubmed.ncbi.nlm.nih.gov/28645853/) did not show its primary superiority result. Both address persistent, severe refractory adults. Their differing designs, programming, selection, carryover possibilities and duration preclude declaring either universal DBS success or universal failure. A delayed-effect explanation is a future prediction to test, not a license to replace a null blinded comparison with a favorable open phase.

Crucially, these DBS outcomes use a global YGTSS total, not the drug trials' 0-50 tic-only score. Surgical and stimulation harms also change the benefit-burden interpretation. A surgically accessible control point does not uniquely locate the developmental cause. Registry enrollment counts and publication analysis counts are retained separately rather than silently equated.

### 4. Symptom improvement can survive a challenge to its proposed mechanism

The [home MNS trial](https://pmc.ncbi.nlm.nih.gov/articles/PMC10947020/) supports a short-term active-versus-sham difference, subject to exclusions and other design limitations. It does not isolate rhythmic entrainment as mediator. The [rhythmic-versus-arrhythmic crossover](https://pmc.ncbi.nlm.nih.gov/articles/PMC10095326/) is more directly discriminating: both patterns helped during stimulation without a demonstrated differential advantage. This challenges the necessity of rhythm-specific entrainment, but is not formal equivalence and did not establish same-person EEG mediation. An active comparator can share sensory, expectancy or alternative physiological effects. Absence of demonstrated persistence is not proof that persistence is impossible.

The [severe-adult SMA rTMS trial](https://pmc.ncbi.nlm.nih.gov/articles/PMC4454615/) preserves a negative sham-controlled result despite favorable uncontrolled extensions elsewhere. The abstract and completer figure report different null-test p values; this pass retains both without conflating analyses. Anatomical plausibility plus a positive open-label trajectory does not establish that a tested cortical implementation works. Conversely, a small negative implementation does not falsify all network modulation.

## Symptoms, function and mechanism are different outcomes

Tic-score improvement can coexist with sedation, effort, persistent urges, pain, participation barriers or co-occurring symptoms. Some trials report impairment or daily-function measures, but these cannot be substituted for direct work/school, injury, comfort or quality-of-life outcomes. ARTISTS 1's ADL contrast remained imprecise and null; ecopipam initiation did not demonstrate broad improvement across the measured co-occurring-condition scales. A global YGTSS score mixes tic severity and impairment and is not identical to a dedicated quality-of-life instrument. No causal mediation from fewer tics to better function is established by this set.

This distinction is especially consequential for severe adult persistence: a person can remain highly burdened despite a population-average response, and an average null trial can conceal responders and nonresponders. Neither observation alone identifies biological subtypes. Reliable response heterogeneity requires prespecified interaction estimates and replication, not a significant result in one subgroup and a nonsignificant result in another.

## Next discriminating decisions and exact prerequisites

1. **Specify the biochemical claim before testing it.** Name transmitter, compartment and dynamics, a validated engagement assay, target population, minimum predicted effect and time course. Missing prerequisite: compatible longitudinal human engagement and outcome data, not merely a drug label or regional bulk metabolite concentration. Do not collect patient data under this task.
2. **Separate target engagement from symptom mediation.** A prespecified causal analysis would need temporal mediator measurement, randomized perturbation, credible controls for expectancy/sensation and exposure, and assumptions about mediator-outcome confounding. Engagement without benefit would constrain that target implementation; benefit without the proposed engagement would challenge mediator necessity. No such new experiment is performed or authorized here.
3. **Test durability distinctly from on-treatment control.** Responder-withdrawal maintenance, uncontrolled continuation and independent treatment-free follow-up are different estimands. Safe withdrawal can only be designed under clinical governance; no treatment changes are proposed.
4. **Retain the function endpoint.** Require separately interpretable symptom and burden estimates with uncertainty, harms and attrition, stratifying persistent adults and co-occurring conditions rather than assuming childhood-to-adult transportability.

The immediate research decision is to reject transmitter-target response as a diagnostic proof of a universal leak, while retaining dopamine and network hypotheses for sharper, engagement-linked tests. No treatment recommendation, cure claim, simulation or new clinical discovery follows from this analysis.
