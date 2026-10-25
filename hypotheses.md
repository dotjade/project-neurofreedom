# Project NeuroFreedom: 20 falsifiable discovery hypotheses

Research planning document · evidence checked 8 October 2026

## Scope and bottom line

There is currently no established cure for Tourette syndrome (TS). Available treatments can reduce tics and impairment; improvement during treatment does not establish elimination of the underlying disorder. This document is a discovery portfolio, not a treatment recommendation, clinical protocol, or prediction that a cure will be found. No patient-level data were obtained or analyzed, and none of the proposed experiments has been conducted for this report. [CDC treatment overview, updated March 2026](https://www.cdc.gov/tourette-syndrome/treatment/index.html)

The most defensible strategy is to pursue several biologically defined subgroups while testing mechanisms that may converge on the same circuit. A universal single-target cure should not be assumed. The proposed portfolio combines genetically anchored mechanisms, cell-specific circuit repair, and durable learning or neuromodulation. Computational work is useful for prioritization and experimental design, but cannot establish therapeutic efficacy by itself.

### What would count as progress toward a cure?

Use three distinct milestones:

1. **Symptomatic benefit:** clinically meaningful improvement while treatment is active.
2. **Disease modification:** a randomized intervention changes the subsequent course beyond expected symptom fluctuation and development, with evidence surviving an appropriately supervised treatment-free observation period when safe.
3. **Sustained remission:** an explicitly proposed research endpoint of minimal or absent clinically impairing tics, corroborated by independent assessment, daily functioning and patient priorities for at least 12 months after a time-limited intervention. This is a proposed high bar, not a validated consensus definition of cure. Longer follow-up is necessary before claiming permanence.

Tic counts alone are insufficient. Motor and vocal tics, urges, pain/injury, everyday functioning, quality of life, cognitive performance, adverse effects and comorbid symptoms need separate reporting. Treatment should serve the person's goals, rather than make normality or suppression at any cost the objective. Clinically managed changes to treatment must never be improvised to test remission.

### Evidence and priority labels

- **Established anchor (E):** a well-supported clinical or biological observation. This never means that the proposed cure mechanism is established.
- **Preliminary anchor (P):** a small human study, model-system result, unreplicated association, or preprint. These sources establish a reason to test, not a reason to treat.
- **Speculative extension (S):** the new causal or therapeutic claim proposed here. Every numbered hypothesis contains an S component, explicitly separated from its supporting evidence.
- **P1 priority:** start with a relatively inexpensive, decision-relevant analysis or study-design task. Data-access dependencies remain real.
- **P2 priority:** promising mechanistic work requiring a specialist laboratory, controlled data access or prospective clinical collaboration.
- **P3 priority:** defer major investment until a more fundamental uncertainty is resolved; potentially costly, weakly supported, or difficult to translate safely.

These are research-investment priorities, not estimates of clinical efficacy. No numerical probability of cure is assigned.

### Shared falsification rules

Before each study, preregister population, target, direction of effect, primary endpoint, minimum worthwhile effect, target-engagement assay, analysis, adverse-event boundaries and a replication plan. An underpowered nonsignificant result is inconclusive. A useful negative result requires an informative confidence interval or equivalence test, adequate target engagement, and a validated assay. If target engagement fails, reject that intervention implementation rather than claiming the biological hypothesis is disproven. Separately distinguish failure in a specified subgroup from failure in all TS.

Animal stereotypies, startle gating and cellular firing are mechanistic proxies, not human tics or remission. Never label a rescued mouse phenotype a cure for people.

## The hypothesis portfolio: exactly 20 hypotheses

### H01. A subset of CELSR3-associated circuit abnormalities remains reversible after development

**Anchor classification:** P: human genetic and model-system mechanism; adult rescue is S.

**Proposed claim (S):** In TS-relevant CELSR3 variant models, correcting the abnormal downstream synaptic program after circuits have matured will normalize corticostriatal dynamics, not merely prevent an embryonic defect.

**Rationale and evidence:** CELSR3 was implicated by recurrent damaging de novo variants in a study of 802 trios. Human-variant mouse models subsequently demonstrated altered sensorimotor behavior and dopamine-related phenotypes. These are strong genetic discovery leads but preliminary therapeutic evidence. [Wang et al., Cell Reports, 2018](https://www.sciencedirect.com/science/article/pii/S221112471831386X); [Nasello et al., PNAS, 2024](https://pubmed.ncbi.nlm.nih.gov/38683996/)

**Counterevidence/confounding:** Variant effects differ. A separate R774H model showed dendritic and interneuron abnormalities without repetitive motor behavior at baseline. Genetic association does not tell us whether adult correction is possible. Homozygous or null models may poorly represent human heterozygous variants. [R774H model, 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12610430/)

**Test/data:** Compare several TS-associated variants, isogenic controls and independently derived neuronal models. Use staged rescue before versus after network maturation, with single-cell expression, connectivity and electrophysiology. Rank downstream intervention points using convergence across variants rather than an isolated differential gene.

**Falsification:** If verified late rescue normalizes the candidate molecular program but leaves the prespecified network defect unchanged across independent variants, reject adult reversibility through that program. Development-only rescue would narrow the hypothesis substantially.

**Feasibility:** **P2.** Variant-to-pathway analysis is tractable; valid mature circuit models and safe translation are major dependencies. This is not a proposal for patient gene editing.

### H02. Synaptic dosage defects define a treatable NRXN1/CNTN6 endotype

**Anchor classification:** P: rare-variant association as a therapeutic anchor; shared rescue endotype is S.

**Proposed claim (S):** A prespecified synaptic-adhesion phenotype in carriers of TS-associated NRXN1 deletions or CNTN6 duplications predicts a common, reversible network defect that is separable from general neurodevelopmental impairment.

**Rationale and evidence:** A large case-control copy-number study associated exonic NRXN1 deletions and CNTN6 duplications with TS. This supports studying synaptic assembly and dosage, not assuming both genes produce the same biological direction. [Huang et al., Neuron, 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5568251/)

**Counterevidence/confounding:** These variants are rare and pleiotropic. Autism, developmental and language phenotypes can accompany NRXN1 deletions. A shared culture phenotype could reflect generic developmental dysfunction rather than tic susceptibility. Duplication is not equivalent to deletion, and breakpoints or isoforms matter.

**Test/data:** Keep the two genetic classes separate initially. Compare gene/isoform-specific correction and matched neutral edits in isogenic corticostriatal cultures; include non-TS neurodevelopmental comparator variants. Identify a convergent downstream phenotype only if replicated across backgrounds, then test selective rescue without generalized activity suppression.

**Falsification:** Reject the proposed shared endotype if the variants do not converge reproducibly, if the same signature is equally present in unrelated neurodevelopmental controls, or if a molecularly engaged rescue cannot correct circuit dysfunction.

**Feasibility:** **P2.** Good construct validity and clear assays; rare recruitment and pleiotropy limit clinical scale. Treat as a precision-discovery arm, not a population-wide solution.

### H03. The 5q15 association acts through a specific developmental regulatory program

**Anchor classification:** P: associated locus and effector-gene nomination; therapeutic mechanism is S.

**Proposed claim (S):** The TS-associated 5q15 locus changes a particular regulatory program involving NR2F1 or nearby noncoding transcripts in a relevant neural cell state, and that program exposes a tractable downstream target.

**Rationale and evidence:** A GWAS meta-analysis of 6,133 cases and 13,565 controls identified a 5q15 locus; integrated annotations implicated NR2F1 and associated noncoding RNAs. The locus is evidence of association; the effector gene and therapeutic direction remain uncertain. [Tsetsos et al., Biological Psychiatry, online 2023/issue 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC10783199/)

**Counterevidence/confounding:** Some reported expression associations come from nonbrain tissues. Linkage disequilibrium can implicate a nearby gene incorrectly. An expression association is not proof that changing the gene is beneficial; broad developmental transcription factors may be unsafe intervention points.

**Test/data:** Fine-map with ancestry-appropriate linkage information, compare competing effector genes, and colocalize against neural developmental regulatory datasets. Functionally test the highest-supported enhancer-to-gene relationships in matched neural models, using orthogonal regulatory perturbations.

**Falsification:** Reject a particular NR2F1 mechanism if credible causal variants consistently regulate a different gene, or if validated enhancer perturbation does not change NR2F1 and the specified cellular phenotype. Failure to fine-map is unresolved uncertainty, not a negative biological finding.

**Feasibility:** **P1 for target nomination; P2 for validation.** The paper states that summary statistics are available on request, so full reanalysis is access-dependent. Do not report them as an already downloaded open dataset.

### H04. A downstream ASH1L program can be corrected without broad chromatin manipulation

**Anchor classification:** P: genetics and experimental models; selective downstream rescue is S.

**Proposed claim (S):** In ASH1L-related TS models, a limited downstream transcriptional module drives abnormal striatal activity and can be corrected without globally altering histone regulation.

**Rationale and evidence:** Human sequencing and functional experiments linked ASH1L variants to TS; mutant mice showed altered striatal activity and dopamine release. This is preliminary gene-to-mechanism evidence, not a validated disease-modifying target. [Liu et al., Molecular Psychiatry, 2019/2020](https://www.nature.com/articles/s41380-019-0560-8)

**Counterevidence/confounding:** ASH1L has broad developmental roles. Mouse motor phenotypes and their response to symptomatic drugs do not show specificity to TS or adult reversibility. A chromatin signature could be secondary to altered cell composition.

**Test/data:** Use independently engineered heterozygous variants, cell-type-resolved expression and chromatin profiling, and matched neuronal maturation. A causal mediation screen should separate direct ASH1L-regulated genes from generic stress responses, then test a small candidate module after maturation.

**Falsification:** If selective normalization of the module has no informative effect on the prespecified circuit abnormality despite molecular correction, reject that module. If only early global correction works, reject the claimed mature downstream rescue.

**Feasibility:** **P2/P3.** Mechanistic prioritization is plausible; a clinically safe intervention is remote. Broad epigenetic drugs should not be advanced on this association alone.

### H05. Histaminergic restoration benefits a defined low-histamine TS subgroup

**Anchor classification:** P: rare-family and animal mechanism; a broader biomarker-defined subgroup is S.

**Proposed claim (S):** A reproducibly identified histamine-signaling deficit, rather than TS diagnosis alone, predicts rescue of dopamine-related circuit abnormalities by selective restoration of that signaling.

**Rationale and evidence:** A rare HDC mutation segregated in a highly unusual family. Hdc-deficient mice and mutation carriers showed related sensorimotor findings, and histamine manipulation modified mouse abnormalities. This is a mechanistically valuable rare-family anchor, not proof that most TS reflects histamine deficiency. [Ercan-Sencicek et al., NEJM, 2010](https://pubmed.ncbi.nlm.nih.gov/20445167/); [Baldan et al., Neuron, 2014](https://pubmed.ncbi.nlm.nih.gov/24411733/)

**Counterevidence/confounding:** HDC variants are uncommon. Receptor location and presynaptic versus postsynaptic effects complicate the direction of treatment. Peripheral histamine is not a validated measure of brain histamine function; arousal or sedation can alter behavior independently.

**Test/data:** Define a neural histamine-pathway signature in variant and nonvariant experimental models, and test receptor-specific rescue with concurrent dopamine and motor-function readouts. Require independent confirmation of any candidate biomarker before considering stratified human research.

**Falsification:** Reject the endotype if its signature does not replicate, does not predict a target-specific response, or apparent rescue is explained entirely by nonspecific motor suppression. Reject broad generalization if the effect is confined to HDC models.

**Feasibility:** **P2.** Strong rare-mechanism logic, substantial biomarker gap. This does not support histamine supplements or unsupervised antihistamine experiments.

### H06. Cell-specific D3 receptor redistribution is a rescue target in CELSR3 dysfunction

**Anchor classification:** P: animal molecular and behavioral experiments; human translation is S.

**Proposed claim (S):** Excess postsynaptic D3 signaling in striosomal D1 neurons, rather than total striatal D3 abundance, mediates a reversible tic-like phenotype in a CELSR3-defined endotype.

**Rationale and evidence:** A 2025 Celsr3-deficient mouse study reported altered D3 receptor distribution and opposite behavioral effects from D3 activation and blockade. This suggests a specific molecular bridge between a developmental risk gene and a pharmacologically accessible pathway. [Celsr3–D3 study, Molecular Psychiatry, 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC13386578/)

**Counterevidence/confounding:** Findings come from a model rather than affected humans. Receptor distribution differs between presynaptic fibers and postsynaptic cells, so system-wide antagonism could combine opposing effects. Reduced grooming can reflect altered motivation or movement rather than selective tic control.

**Test/data:** Independently replicate across human-variant models; compare cell-restricted normalization with nonspecific receptor blockade. Measure spontaneous movement, reward learning and network activity alongside tic-like events. Seek human molecular convergence before clinical target claims.

**Falsification:** Reject the causal postsynaptic mechanism if verified cell-specific normalization fails while nonspecific blockade still changes behavior, or if benefit disappears after accounting for reduced normal movement. Absence in multiple human-relevant variants limits the endotype's scope.

**Feasibility:** **P2.** A relatively crisp preclinical experiment; clinical specificity and safety are unproven. Avoid treating druggability as validation.

### H07. D1 modulation can create a window for durable relearning

**Anchor classification:** E: randomized on-treatment symptom benefit in the studied populations; durable combination benefit is S.

**Proposed claim (S):** Combining a time-limited D1-targeted intervention with structured tic-focused behavioral learning yields benefit that persists after the drug effect ends, exceeding either intervention alone.

**Rationale and evidence:** D1 antagonism has randomized symptom-treatment evidence. The 2026 ecopipam phase 3 randomized-withdrawal trial found lower relapse risk among pediatric responders who continued treatment; adult evidence was exploratory and small. This establishes maintenance of suppression in selected responders, not disease modification. [Gilbert et al., JAMA Neurology, 2026](https://pubmed.ncbi.nlm.nih.gov/42189524/)

**Counterevidence/confounding:** Responder enrichment limits generalization. Continued-treatment benefit and relapse on withdrawal are compatible with purely symptomatic action. CNS adverse events, mood symptoms and learning effects require monitoring; pharmacological suppression could also interfere with useful learning.

**Test/data:** A specialist-led factorial trial would compare behavioral intervention plus active drug, behavioral intervention plus placebo, and matched control conditions. Model motor habit learning, then assess prespecified durability after clinically supervised treatment completion. Include blinded observations and patient-centered function.

**Falsification:** Reject durable synergy if the interaction effect is negligible with informative precision and no additional benefit remains after drug clearance and appropriate follow-up, even if on-treatment tic reduction is real.

**Feasibility:** **P2.** Clinically grounded hypothesis, but requires a regulated collaborative trial. Current phase 3 evidence is not a cure and does not establish this combination's efficacy.

### H08. Restoring striatal parvalbumin-interneuron timing reduces pathological action release

**Anchor classification:** P: small postmortem human studies; selective functional restoration is S.

**Proposed claim (S):** In an objectively defined inhibitory-control endotype, restoring the timing and recruitment of surviving striatal parvalbumin interneurons reduces inappropriate motor-program release without impairing intended movement.

**Rationale and evidence:** Small postmortem studies reported fewer striatal parvalbumin-positive interneurons in severe persistent TS. This motivates circuit-specific inhibition experiments; it does not demonstrate generalized GABA deficiency. [Kataoka et al., Journal of Comparative Neurology, 2010](https://pmc.ncbi.nlm.nih.gov/articles/PMC2846837/)

**Counterevidence/confounding:** Severe adult brain donors may not represent typical childhood TS. Protein-marker expression can change without actual cell death. Medication, agonal events and developmental history are difficult to disentangle. Fewer cells do not establish that stronger inhibition is always therapeutic.

**Test/data:** First distinguish cell abundance from cell state with independent anatomical and transcriptomic measurements. Then perturb timing versus tonic inhibition separately in model circuits and quantify selectivity for aberrant events over normal movement.

**Falsification:** Reject the proposed mechanism if appropriate interneuron recruitment is restored but pathological action release persists, or if apparent improvement requires indiscriminate suppression of normal actions. Failure to reproduce the putative endotype makes broad translation unjustified.

**Feasibility:** **P2.** High mechanistic value, limited human measurement tools. Cell transplantation is not justified by these findings alone and is not proposed here as a ready treatment.

### H09. Cholinergic signaling dynamics matter more than total cholinergic terminal abundance

**Anchor classification:** P: animal intervention and conflicting small human studies; timing-based rescue is S.

**Proposed claim (S):** A subgroup has abnormal striatal cholinergic response timing despite preserved terminal density, and correcting that timing normalizes action gating.

**Rationale and evidence:** Targeted striatal cholinergic-cell ablation produced TS-relevant mouse behavior, supporting causal plausibility of this cell class. [Xu et al., PNAS, 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4311862/)

**Counterevidence/confounding:** A PET study of 12 people with TS and 10 controls found no striatal vesicular acetylcholine transporter deficit. Thus, a universal loss-of-cholinergic-cells theory is not supported consistently. PET terminal density and signaling timing measure different things; that distinction cannot itself be used to dismiss a negative study. [Albin et al., eNeuro, 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5547197/)

**Test/data:** Measure phasic cholinergic dynamics in variant-defined models with intact versus reduced cell counts. Test timing-specific rescue against equal overall activity delivered at irrelevant times. Require convergence with a reproducible human physiological proxy before translation.

**Falsification:** Reject the timing-specific account if the presumed timing defect is absent or if restoring timing does no better than an activity-matched control, with adequate target engagement.

**Feasibility:** **P2.** Resolves a concrete conflict in the literature. No implication that increasing acetylcholine globally will be helpful or safe.

### H10. A microglial state drives circuit dysfunction in a restricted TS subgroup

**Anchor classification:** P: small postmortem molecular study; upstream immune causality and rescue are S.

**Proposed claim (S):** A reproducible microglial state is upstream of synaptic or interneuron dysfunction in a subset of TS, and selectively modifying that state rescues circuit function.

**Rationale and evidence:** Single-nucleus RNA and chromatin analysis of six TS and six matched control brains reported microglial immune-response changes. These are preliminary human molecular observations. [Wang et al., Biological Psychiatry, 2025](https://pubmed.ncbi.nlm.nih.gov/39892689/)

**Counterevidence/confounding:** Postmortem inflammation may follow chronic circuit activity, treatment, illness near death or other exposures. A blood immune signature does not establish brain microglial pathology. Differential gene expression does not demonstrate causation or justify immunosuppression.

**Test/data:** Replicate at the donor level with careful tissue covariates. In controlled neuron–microglia co-cultures, swap disease and control cell compartments and test temporally ordered perturbations. Compare the nominated state with generic inflammatory stress.

**Falsification:** Reject upstream causality if neuronal defects precede and persist independently of the microglial state, or if specific state correction has no network benefit despite adequate engagement. A signal fully explained by tissue quality or medication invalidates that biomarker.

**Feasibility:** **P2/P3.** Suitable for causal co-culture work; unsuitable for immediate clinical immune-treatment claims. Infection-triggered disorders and typical TS must not be merged without diagnostic justification.

### H11. Medium spiny neuron metabolic dysfunction amplifies a reversible circuit defect

**Anchor classification:** P: postmortem transcriptional signature; metabolic causality and rescue are S.

**Proposed claim (S):** Reduced oxidative metabolism in a molecularly defined medium spiny neuron subgroup is a causal amplifier of abnormal firing, and selective metabolic correction improves circuit function.

**Rationale and evidence:** The 2025 striatal single-nucleus study found reduced mitochondrial-function transcriptional signatures in medium spiny neurons. This is a candidate state, not evidence of a generalized systemic mitochondrial disease. [Wang et al., Biological Psychiatry, 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12255533/)

**Counterevidence/confounding:** RNA levels do not directly measure respiration or ATP. Chronic hyperactivity, treatment and postmortem handling may cause the signature. A compensatory downshift could be protective rather than pathological.

**Test/data:** Replicate expression results with functional metabolic measurements in living cellular models. Compare temporal trajectories before and after circuit dysfunction; test whether selective metabolic restoration changes abnormal firing independently of cell viability or global activity reduction.

**Falsification:** Reject the causal-amplifier claim if the signature is absent in well-controlled living models, or if verified metabolic correction leaves circuit abnormalities unchanged. Worsened network activity would contradict the proposed therapeutic direction.

**Feasibility:** **P2/P3.** Assays are feasible; disease specificity and causal direction are weakly established. This hypothesis does not support supplements, dietary restriction or other personal metabolic interventions.

### H12. Adaptive cortical GABA predicts who benefits from inhibition-focused intervention

**Anchor classification:** P: human MRS association; compensation-guided treatment selection is S.

**Proposed claim (S):** Higher supplementary motor area GABA reflects a useful compensatory state in some people, and baseline compensation predicts the direction and magnitude of response to a circuit intervention.

**Rationale and evidence:** An MRS study found increased supplementary motor area GABA and associations consistent with enhanced motor control. This argues against a simple whole-brain low-GABA explanation. [Draper et al., Current Biology, 2014](https://doi.org/10.1016/j.cub.2014.08.038)

**Counterevidence/confounding:** MRS measures a mixed tissue pool, not synaptic inhibition or receptor activity. Cross-sectional association cannot identify compensation. Age, medication, scanner effects, attention and tic suppression during scanning may confound results.

**Test/data:** Combine repeat MRS with physiology, behavior and longitudinal tic measurements. Preregister the prediction that a specified compensation profile moderates intervention response. Compare the biomarker model with a clinical-only baseline and test it at another site.

**Falsification:** Reject the predictive mechanism if the profile is unreliable, has no external incremental value, or the predicted treatment-by-biomarker interaction is excluded by precise estimates. Improvement correlated with GABA after treatment alone is insufficient.

**Feasibility:** **P1 for analysis/design; P2 for acquisition.** Useful for avoiding interventions that disrupt compensation; no recommendation for generalized GABA enhancement follows.

### H13. NMDA-dependent learning enhancement can increase durable behavioral benefit

**Anchor classification:** P: small augmentation trial; durable generalized learning enhancement is S.

**Proposed claim (S):** Enhancing a verified successful learning process during behavioral treatment produces durable reduction across clinically important tics, rather than a short-lived improvement only in practiced tics.

**Rationale and evidence:** A small randomized study of 20 young people found preliminary benefit from D-cycloserine augmentation of one habit-reversal session on targeted tics. [McGuire et al., Neuropsychopharmacology, 2020](https://www.nature.com/articles/s41386-020-0762-4)

**Counterevidence/confounding:** One session, a small sample, a targeted-tic outcome and brief follow-up cannot establish broad or lasting efficacy. A separate small trial of D-serine or riluzole did not demonstrate tic benefit over placebo, so generic glutamate modulation is not validated. [Lemmon et al., Pediatric Neurology, 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4454293/)

**Test/data:** A blinded, multisession trial should preregister a computational learning marker, global tic severity, untrained-tic generalization and post-treatment durability. Test whether intervention benefit depends on actual learning success rather than exposure alone.

**Falsification:** Reject the generalization hypothesis if precise estimates exclude worthwhile global or treatment-free benefit despite replicated improvement in practiced tics. Reject the learning mechanism if target engagement occurs without the predicted learning change.

**Feasibility:** **P2.** A testable augmentation question, not an off-label medication suggestion. Careful safety review and independent replication are required.

### H14. A prespecified endocannabinoid endotype explains heterogeneous trial response

**Anchor classification:** P: mixed clinical findings; a replicable biological treatment selector is S.

**Proposed claim (S):** A biological endocannabinoid-signaling profile, defined independently of treatment outcome, identifies a subgroup with reproducible tic benefit without unacceptable cognitive or psychiatric effects.

**Rationale and evidence:** A small THC/CBD crossover trial reported benefit, while the larger CANNA-TICS trial did not establish superiority on its primary endpoint. This mixed evidence supports examining heterogeneity only with strong protection against post hoc subgroup discovery. [Mosley et al., NEJM Evidence, 2023](https://evidence.nejm.org/doi/full/10.1056/EVIDoa2300012); [CANNA-TICS, Psychiatry Research, 2023](https://www.sciencedirect.com/science/article/pii/S0165178123000860)

**Counterevidence/confounding:** A randomized monoacylglycerol-lipase inhibitor study also failed its primary endpoint, with the reported difference favoring placebo. Psychoactive effects threaten blinding; nonspecific calming, expectations and cognitive impairment can alter measured tics. [Müller-Vahl et al., Movement Disorders, 2021](https://movementdisorders.onlinelibrary.wiley.com/doi/abs/10.1002/mds.28681)

**Test/data:** First preregister a biomarker and independently validate it. Then test a treatment-by-biomarker interaction, with active control of expectancy and blinded video ratings. Do not use exploratory sex or severity subgroups from a negative trial as validated selectors.

**Falsification:** Reject the endotype if it does not replicate or does not predict a beneficial interaction with informative precision and adequate engagement. Persistent benefit after treatment would need a separate test.

**Feasibility:** **P3.** Mixed and negative trial results raise the threshold for more investment. No self-experimentation or cannabis-use recommendation is implied.

### H15. Network-informed cortical targeting outperforms generic supplementary motor targeting

**Anchor classification:** P: lesion/connectivity and stimulation findings; superior individualized targeting is S.

**Proposed claim (S):** Selecting a cortical stimulation target by its connection to a tic-relevant action-control network improves outcomes compared with a fixed anatomical supplementary motor target.

**Rationale and evidence:** Lesion and DBS connectivity work implicated a distributed tic network; later work identified action-related functional networks relevant to tic modulation. This supports target discovery, not a demonstrated cortical stimulation treatment. [Ganos et al., Brain, 2022](https://academic.oup.com/brain/article/145/12/4385/6506575); [Action-related networks study, Nature Communications, 2024](https://www.nature.com/articles/s41467-024-55242-6)

**Counterevidence/confounding:** Lesion-induced tics differ from developmental TS. Normative connectomes may miss individual anatomy. Small randomized supplementary motor area stimulation studies have produced negative or mixed results. [Landeros-Weisenberger et al., Brain Stimulation, 2015](https://doi.org/10.1016/j.brs.2014.11.015)

**Test/data:** Reproduce published group maps with spatial-null controls, then compare preregistered network-based versus standard targeting and credible sham in a blinded clinical study. Use independent discovery and validation cohorts.

**Falsification:** Reject the targeting advantage if a well-powered comparison excludes meaningful superiority despite verified engagement of the predicted network. If a map performs no better than spatially matched random maps, reject the map's specificity before a trial.

**Feasibility:** **P1 for map replication; P2 for a clinical test.** Public group maps and code are reported available; individual scans remain access-controlled.

### H16. Tic-state responsive DBS provides more selective benefit than continuous DBS

**Anchor classification:** P: small feasibility cohorts; comparative advantage of responsive stimulation is S.

**Proposed claim (S):** A reproducible neural tic-state detector can trigger stimulation selectively enough to maintain or improve benefit while reducing stimulation exposure and adverse effects compared with optimized continuous DBS.

**Rationale and evidence:** A 2024 experimental cohort demonstrated responsive stimulation feasibility and meaningful response in some participants. This is proof of concept in a very small refractory group, not established superiority or a cure. [Okun et al., Scientific Reports, 2024](https://pubmed.ncbi.nlm.nih.gov/38499664/)

**Counterevidence/confounding:** Neural features can reflect movement artifact or consequences of tics. Different devices and programming strategies complicate comparison. An emerging circadian adaptive approach was reported in a single patient, illustrating feasibility but not generalizability. [Circadian adaptive DBS report, 2026](https://pubmed.ncbi.nlm.nih.gov/41950934/)

**Test/data:** Validate detectors prospectively on held-out days and voluntary movements; compare personalized responsive, optimized continuous and clinically appropriate control states under specialist oversight. Predefine noninferiority or superiority, energy exposure and quality-of-life endpoints.

**Falsification:** Reject the claimed advantage if decoding fails out of sample or responsive stimulation offers no worthwhile exposure-adjusted advantage. A classifier that merely detects a completed tic does not validate prediction or prevention.

**Feasibility:** **P2/P3.** Restricted to experienced clinical research centers and carefully selected already-eligible patients. Surgery is not justified to supply research signals alone.

### H17. Median nerve stimulation has a specific sensory-gating mechanism

**Anchor classification:** P: a positive short-duration controlled trial; the specific mechanism and durability are S.

**Proposed claim (S):** The tic benefit from patterned median nerve stimulation depends on a reproducible sensory-to-motor physiological mechanism rather than distraction or expectancy, and mechanism-matched stimulation yields greater durable benefit.

**Rationale and evidence:** A randomized active/sham/waitlist study reported short-term improvement with home-administered stimulation. It establishes a reason for independent mechanistic replication, not persistent remission. [Morera Maiquez et al., Journal of Neuropsychology, 2023](https://pubmed.ncbi.nlm.nih.gov/37133932/)

**Counterevidence/confounding:** Sensory differences can compromise masking, and attention can change tic expression. The investigators disclosed links to the device company. Short follow-up cannot distinguish lasting network change from temporary suppression. A 32-person rhythmic-versus-arrhythmic crossover found benefits with both patterns and no demonstrated post-stimulation persistence, challenging rhythm-specific entrainment. A September 2026 active-arm follow-up reported improvement at three months, but that uncontrolled follow-up cannot establish disease modification. These comparators and durability questions have already been studied; the next task is independent replication and stronger causal discrimination. [Crossover trial](https://pubmed.ncbi.nlm.nih.gov/37048598/); [2026 follow-up](https://pubmed.ncbi.nlm.nih.gov/42704310/)

**Test/data:** Compare sensation-matched control patterns while measuring EEG or other preregistered target engagement. Mask assessors, measure expectancy, and follow both treatment-on and treatment-free outcomes. Test physiological mediation while checking mediator–outcome confounding and direct intervention effects; statistical mediation alone does not prove causation. Require preserved normal movement.

**Falsification:** Reject the proposed specific mechanism if sensation-matched controls perform equivalently or clinical benefit is unrelated to verified engagement. Reject durability if benefit vanishes outside the active-treatment period, while retaining any supported symptomatic benefit.

**Feasibility:** **P1 for independent trial-analysis planning; P2 for execution.** A comparatively accessible clinical research path, but this is not a device-building or self-stimulation guide.

### H18. Personalized learning models improve the durability and reach of CBIT

**Anchor classification:** E: randomized CBIT symptom-treatment benefit; model-guided incremental benefit is S.

**Proposed claim (S):** A model distinguishing urge relief, contextual triggers and motor learning can select behavioral components that improve long-term patient-centered outcomes beyond standard CBIT.

**Rationale and evidence:** CBIT has randomized efficacy evidence in both children and adults. Those trials establish behavioral treatment benefit, but not one exclusive mechanism or a personalized matching algorithm. [Piacentini et al., JAMA, 2010](https://pmc.ncbi.nlm.nih.gov/articles/PMC2993317/); [Wilhelm et al., Archives of General Psychiatry, 2012](https://pmc.ncbi.nlm.nih.gov/articles/PMC3772729/)

**Counterevidence/confounding:** Learning parameters may be statistically unidentifiable, depend on self-report or reflect attention and adherence. Not every tic has a clearly recognized urge. A model may predict outcome without improving treatment decisions.

**Test/data:** Fit a small, interpretable preregistered model to ethically collected repeated measures; perform parameter-recovery tests before interpreting it. Randomize model-guided component allocation against equally intensive standard CBIT, measuring functioning, effort and durable generalization.

**Falsification:** Reject personalization if it yields no clinically worthwhile incremental benefit out of sample, or if recovered parameters cannot distinguish competing mechanisms. Better prediction alone is not evidence of a better intervention.

**Feasibility:** **P1 for simulations and design; P2 for prospective evaluation.** This does not imply that TS is a voluntary habit or that insufficient effort explains persistent symptoms.

### H19. Natural improvement reveals protective mechanisms that can be reproduced

**Anchor classification:** P: longitudinal imaging and observational cohorts; an actionable protective mechanism is S.

**Proposed claim (S):** A prospectively measured developmental circuit trajectory predicts later improvement independently of initial severity and treatment, and its specific functional feature can be reproduced by a safe intervention.

**Rationale and evidence:** Longitudinal imaging linked childhood caudate volume to later symptom severity. Prospective early-tic work also shows why remission requires careful observation rather than simply relying on subjective disappearance. [Bloch et al., Neurology, 2005](https://pubmed.ncbi.nlm.nih.gov/16247053/); [The New Tics study, 2020](https://pubmed.ncbi.nlm.nih.gov/32587895/)

**Counterevidence/confounding:** Predictors are not intervention targets. Natural maturation, regression to the mean, attrition, treatment access and context-dependent suppression can mimic protection. Small structural measures are not validated individual prognostic tests.

**Test/data:** Use multi-site repeated assessment to separate persistent, improving and minimally impairing trajectories. Compare prediction against simple clinical baselines, evaluate calibration and ancestry/sex generalization, and identify a functional mediator before selecting an intervention.

**Falsification:** Reject the nominated protective feature if it has no independent predictive value, fails another cohort, or manipulating its functional counterpart does not improve the predicted outcome. A volume correlation alone cannot establish a causal target.

**Feasibility:** **P1 for cohort-analysis design; P2 for access and follow-up.** Potentially high discovery value, but requires years of follow-up and consented data, not public video scraping.

### H20. SHH–GLI developmental mispatterning exposes a common downstream rescue point

**Anchor classification:** P: patient-derived organoid findings; broadly reproducible and therapeutically useful rescue is S.

**Proposed claim (S):** A defined SHH–GLI/ciliary response abnormality causes a reproducible interneuron-development deficit across a subset of TS backgrounds, and a downstream correction restores functional circuit balance.

**Rationale and evidence:** Patient-derived basal ganglia organoids showed altered ventral patterning and reduced interneuron differentiation, with SHH-pathway and ciliary findings. This is preliminary human cellular evidence of developmental vulnerability. [Brady et al., Molecular Psychiatry, 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9949887/)

**Counterevidence/confounding:** Few donors, line effects, organoid batch variation and differentiation protocols can create apparent fate shifts. Organoids incompletely model human development. Correcting embryonic cell specification does not establish a feasible intervention after TS onset.

**Test/data:** Replicate across independent laboratories and blinded differentiation batches, with donor as the statistical unit. Test direction-specific pathway correction, lineage allocation and mature circuit function. Compare early correction with correction after differentiation to determine the actual therapeutic window.

**Falsification:** Reject the shared mechanism if the lineage phenotype is not donor-replicable or if validated SHH–GLI correction fails to restore both cell fate and the functional phenotype. An early-only rescue rejects the late-treatment claim.

**Feasibility:** **P2 for mechanism; P3 for clinical translation.** Broad developmental signaling is not an acceptable ready-made drug target. The immediate aim is to discover safer downstream mechanisms, not prenatal intervention.

## Therapeutic target discovery map

The table is an index to the evidence and falsification requirements above. Arrows describe proposed causal paths, not confirmed therapeutic chains.

| Layer | Proposed path and candidate target class | Hypotheses | First decisive question | Priority |
|---|---|---|---|---|
| Genetic development | CELSR3 → synaptic/circuit patterning → downstream repair | H01 | Is a mature phenotype reversible? | P2 |
| Synaptic dosage | NRXN1/CNTN6 → adhesion/isoform imbalance | H02 | Is the phenotype TS-relevant and shared? | P2 |
| Regulatory genetics | 5q15 → effector transcript → neural program | H03 | Which gene and developmental state are causal? | P1/P2 |
| Chromatin regulation | ASH1L → restricted downstream module | H04 | Can selective rescue avoid global chromatin effects? | P2/P3 |
| Neuromodulators | HDC/histamine signaling → dopamine regulation | H05 | Is a measurable endotype present beyond rare variants? | P2 |
| Receptor localization | CELSR3 → striosomal D3 distribution | H06 | Does cell-specific correction outperform motor suppression? | P2 |
| Plasticity window | D1 modulation + behavioral learning | H07 | Does added benefit persist after treatment ends? | P2 |
| Fast inhibition | Parvalbumin recruitment → action gating | H08 | Is timing causally important and selectively rescuable? | P2 |
| Cholinergic control | Cholinergic response dynamics → striatal gating | H09 | Can a timing account survive density counterevidence? | P2 |
| Neuroimmune state | Microglial state → neuronal dysfunction | H10 | Cause, consequence or tissue confound? | P2/P3 |
| Cellular metabolism | MSN oxidative metabolism → firing instability | H11 | Does functional correction change circuit output? | P2/P3 |
| Compensatory inhibition | SMA GABA-related adaptation → response direction | H12 | Can the biomarker predict a treatment interaction? | P1/P2 |
| Learning pharmacology | NMDA-linked learning → durable generalization | H13 | Does benefit extend beyond trained tics? | P2 |
| Endocannabinoid regulation | Endotype → selective response | H14 | Can a prespecified selector replicate despite negative trials? | P3 |
| Network neuromodulation | Tic/action network → individualized cortical target | H15 | Does a map improve targeting beyond anatomy and sham? | P1/P2 |
| Responsive stimulation | Neural tic-state → selective DBS | H16 | Does prospective decoding yield a patient-relevant advantage? | P2/P3 |
| Peripheral sensory input | Median nerve → sensory–motor gating | H17 | Specific mechanism or nonspecific sensation/expectancy? | P1/P2 |
| Behavioral matching | Urge/context/learning profile → tailored CBIT | H18 | Does matching help beyond equal-intensity standard care? | P1/P2 |
| Developmental resilience | Natural improvement → protective circuit function | H19 | Prediction first; causal reproducibility second | P1/P2 |
| Lineage specification | SHH–GLI/cilia → interneuron development | H20 | Is the phenotype robust and is there a useful rescue window? | P2/P3 |

### Cross-cutting interpretive constraints

- **Do not collapse regional biology.** A 2026 DLPFC single-nucleus **preprint** reports preserved broad cell proportions with transcriptional remodeling. It is a useful caution against extending striatal cell-loss results to all cortex, and requires peer-reviewed independent confirmation. [Moos et al., bioRxiv, 2026](https://pubmed.ncbi.nlm.nih.gov/41648330/)
- **Drug response does not establish a primary cause.** Failed randomized VMAT2 inhibitor trials warn against concluding that generic dopamine reduction must work because some receptor-directed therapies do. [Flexible-dose deutetrabenazine RCT, 2021](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2784765); [Fixed-dose trial, 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8524312/)
- **Do not equate comorbidity benefit with tic remission.** ADHD, OCD, anxiety and depression must be measured and analyzed separately. A treatment can still be valuable because it improves life even when tics remain.
- **Do not select a target from differential expression alone.** Require converging genetics, perturbation, relevant cell state and functional rescue, or a comparably strong causal experimental case. Downregulated genes might reflect cell loss or useful compensation.
- **Do not use novelty as a priority score.** A new receptor, AI-ranked molecule or network map earns advancement only when it resolves a decision better than simpler alternatives.

## Computational research opportunities

These are proposed work packages, not claims of completed analysis. None requires identifying or contacting people with TS. Public aggregate evidence can be used first; participant-level information remains outside the present scope.

### C1. Build an auditable target–evidence graph

**Inputs:** The primary papers linked above, their published aggregate results, gene lists and trial endpoints. Record sample, species, study design, phenotype, direction, confidence interval, replication status, conflicts of interest and publication status.

**Method:** Keep separate edges for genetic association, expression association, causal perturbation, model rescue and clinical benefit. Store explicit negative edges and distinguish “not measured” from “no effect.” A language model can help extract candidate records, but a human check against the primary text remains necessary.

**Deliverable:** A queryable graph where every proposed target can be traced to a specific finding and limitation. Rank by independent evidence streams and experimentally testable uncertainty, not publication count.

**Success/stop:** Each high-priority claim has traceable support and a counterevidence field. Stop promotion of targets whose rank depends on treating correlational or duplicated evidence as independent causal support. **Start now; no patient data required.**

### C2. Reproduce public network maps with spatial specificity controls

**Inputs/access:** The action-network paper reports group imaging results and project code at [OSF UPJVB](https://doi.org/10.17605/OSF.IO/UPJVB), with normative functional connectivity data at [Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/25833). Its individual patient scans require data-use agreements. Availability is reported in the paper; this report has not downloaded or verified the full archive contents. [Source and access statement](https://www.nature.com/articles/s41467-024-55242-6)

**Method:** Recreate group figures; use spatially constrained null maps, robustness to atlas and smoothing choices, and held-out networks. Do not claim out-of-patient prediction from group maps alone.

**Deliverable:** Reproducibility report and a short list of candidate cortical regions with uncertainty, supporting H15. **Success/stop:** Retain regions robust to reasonable pipelines and spatial nulls; stop target claims if map specificity disappears. **Highest-priority public computation.**

### C3. Integrate rare-variant genes with developmental cell-state annotations

**Inputs/access:** Published aggregate variant/gene lists from H01–H04 and publicly documented reference brain-development annotations. Human individual genomes are unnecessary for an initial aggregate analysis.

**Method:** Gene-set enrichment with matched nulls for gene length, mutability, expression and constraint. Analyze deletion, duplication and missense evidence separately; test whether inferred convergence survives removal of the strongest single gene.

**Deliverable:** A ranked cell-state/pathway shortlist for H01, H02, H04 and H20, with an explicit developmental window and perturbation readout.

**Success/stop:** Advance only convergent signals surviving multiple-testing control and a separate reference dataset. Do not call enrichment therapeutic validation. **P1 computational entry point; preclinical follow-up P2.**

### C4. Fine-map regulatory loci only after access is established

**Inputs/access:** TS GWAS summary statistics plus suitable regulatory and linkage reference data. The H03 paper says statistics are available on request. No request or access approval has been made here. [Study and data-availability statement](https://research-portal.uu.nl/ws/portalfiles/portal/229152994/1-s2.0-S0006322323000513-main.pdf)

**Method:** Bayesian fine-mapping and colocalization that permit multiple causal signals; sensitivity to ancestry, tissue and prior choices. Treat transcriptome-wide associations and Mendelian-randomization outputs as prioritization, particularly when instruments are weak or pleiotropic.

**Deliverable:** Competing effector-gene models with credible sets and proposed enhancer tests. **Success/stop:** A resolved locus with a falsifiable mechanism is useful; an unresolved locus remains unresolved. **P1 after lawful access; otherwise prepare the reproducible pipeline using synthetic data.**

### C5. Reanalyze molecular signatures at donor level

**Inputs/access:** Aggregate tables can be inspected now. Full single-nucleus count matrices, donor covariates and sequencing metadata require a verified repository route or approved access; no accessible accession was confirmed during this research pass. Do not describe these as already acquired open data.

**Method:** Donor-level pseudobulk, compositional analysis, leave-one-donor-out sensitivity and cell-state versus cell-abundance separation. A nucleus is not an independent patient. Check postmortem interval, RNA quality, medication and batch whenever metadata permit.

**Deliverable:** Robust versus fragile signal lists for H08–H11 and H20. **Success/stop:** Prioritize only pathways that survive donor-level analyses and orthogonal biological validation; treat insufficient donor numbers as a limit that more cells cannot solve. **P2 because data and replication are limiting.**

### C6. Design trials that cannot mistake waxing and waning for remission

**Inputs:** Published aggregate trial effects, uncertainty ranges and synthetic longitudinal data. No individual clinical records are needed for design simulation.

**Method:** Simulate autocorrelated tic trajectories, baseline regression, natural development, dropout and treatment-response heterogeneity. Compare parallel, delayed-start and clinically appropriate randomized-withdrawal designs. Explicitly model how responder enrichment changes the target population.

**Deliverable:** A design decision memo with sensitivity curves for precision, follow-up duration, missingness and the difference between symptom suppression and a changed trajectory.

**Success/stop:** A design must separate the specified causal effect under realistic alternatives. Avoid a fabricated sample-size precision claim when variance and correlation estimates are weak. **P1 and directly relevant to H07, H13, H17–H19.**

### C7. Stress-test tic-state and behavioral-learning models before collecting new data

**Inputs:** Synthetic event sequences and any explicitly licensed aggregate or appropriately governed research data later made available. Do not scrape identifiable videos, infer diagnoses from social media, or assume posted recordings authorize biomedical reuse.

**Method:** Parameter recovery, temporal leakage checks, leave-person/site-out evaluation, voluntary-movement negatives and calibration. Distinguish a retrospective detector, a prospective predictor and a treatment-decision rule.

**Deliverable:** Benchmark requirements for H16–H18 and a model card stating failure modes. **Success/stop:** Prefer a simpler calibrated model if complex models cannot improve a prespecified decision. Clinical utility still requires a randomized test. **P1 design; P2 validation.**

### C8. Rank perturbations for laboratory validation, not medications for patients

**Inputs:** Only replicated cell-type-specific signatures and genetically supported pathways, linked to well-characterized perturbation data. Record cell type, concentration context, exposure duration and whether the candidate can plausibly engage the relevant brain target.

**Method:** Compare pathway correction with generic cytotoxicity, proliferation and stress signatures. Require agreement between genetic and pharmacological perturbation and avoid prioritizing a compound solely from docking, structural prediction or reversal of a transcriptional signature.

**Deliverable:** A small experimental candidate set with mechanism, expected direction, engagement assay, counter-screen and kill criterion. **Success/stop:** Advance only compounds with selective functional rescue in independent models; stop on nonspecific neuronal suppression or unacceptable safety signals. **P2; no automated clinical recommendations.**

## Recommended first decisions

1. **Start with evidence quality and public reproducibility:** C1, C2, C3 and C6. These can reject weak targets before expensive experiments and do not require personal patient data.
2. **Choose two complementary mechanistic programs:** one genetically anchored program, such as H01/H06 or H20, and one reversible circuit/learning program, such as H15/H17/H18. Keep their success criteria independent.
3. **Seek replication before immune, metabolic or endocannabinoid escalation:** H10, H11 and H14 have substantial causal or clinical uncertainty. They belong in a research portfolio with explicit stopping rules, not in a near-term treatment menu.
4. **Use patient and clinical input before translating endpoints:** determine which changes in daily life matter and how much burden a trial creates. No participant contact, recruitment, biospecimen work or intervention is authorized or undertaken by this document.
5. **Label progress honestly:** a validated target, a rescued culture, a better decoder, improved tics and treatment-free remission are different achievements. Report each at its actual evidentiary level.

## Research limitations

This is a focused primary-source discovery review rather than a registered systematic review or exhaustive trial census. Relevant evidence was checked on 8 October 2026. PubMed, publisher pages, institutional copies and official public-health sources were used; some full-text routes intermittently failed, so selected claims rely on indexed abstracts or accessible manuscript text. Commercial press releases were not used to establish treatment efficacy. Unverified data availability, preprints, small samples and negative trial results are explicitly marked. All study designs, prioritization judgments and falsification proposals are original research-planning inferences from the cited literature.

## Search scope and log

**Executed:** 8 October 2026, approximately 07:41–07:45 UTC. Forty-three web-search queries were run, followed by targeted opening and within-page checks of primary records. This was web-assisted primary-literature searching; it was not a complete native PubMed, Embase, PsycINFO or Cochrane database search. No paywalled subscription system, private clinical dataset or patient record was accessed.

**Primary-source platforms checked:** PubMed and PubMed Central; NEJM/NEJM Evidence; JAMA Network; Nature-family journals; ScienceDirect journal records; Wiley journal records; Oxford Academic; institutional manuscript repositories. CDC and NINDS provided the current no-cure framing. An EU Clinical Trials Register result appeared in the search for CANNA-TICS and corroborated its trial identity; no comprehensive registry search was performed. OSF and Harvard Dataverse links were verified from the publication's availability statement, not by a completed dataset download.

**Representative exact queries, grouped by the actual search sequence:**

- Genetics: “Tourette syndrome whole exome sequencing CELSR3 WWC1 FLT3 Nature primary research”; “Tourette disorder largest genome wide association study 2024 2025 FLT3 locus primary research”; “Tourette 2024 genome wide association 2025 2026 6133 cases risk loci”; “ASH1L mutations Tourette syndrome mice histone methyltransferase 2019”.
- Cellular mechanisms: “Tourette syndrome interneurons cholinergic parvalbumin striatum postmortem primary study”; “Tourette syndrome HDC histidine decarboxylase mutation mouse primary study NEJM”; “Interneuron loss and microglia” “GSE”; “Tourette organoids SHH interneuron development 2024 2025 Fasching”.
- Current pharmacology and negative trials: “Tourette randomized placebo controlled ecopipam 2023 2025 Pediatrics trial”; “Efficacy and Safety of Ecopipam” “Phase 3” 2026; “Tourette deutetrabenazine randomized clinical trial negative 2021 JAMA Network Open”; “Tourette monoacylglycerol lipase inhibition Lu AG06466 12 week randomized trial 2021 negative”.
- Neuromodulation: “Tourette median nerve stimulation randomized double blind sham 2023 trial”; “Tourette deep brain stimulation connectomic target network 2019 2021 primary study”; “Tourette chronic adaptive deep brain stimulation trial tic biomarkers thalamic 2021 2024”; “Tourette randomized sham controlled supplementary motor area transcranial magnetic stimulation negative 2015 trial”.
- Learning and development: “Tourette D cycloserine behavior therapy randomized pilot trial 2015 2020”; “Tourette glutamate riluzole D serine randomized trial 2015 placebo primary”; “Tourette remission longitudinal prospective study new tics persistent one year 2019 2021”; “Tourette remission caudate volume childhood predicts adulthood tic severity 2005 2006 study”.
- Availability/status checks: “A critical role of action-related functional networks” “Data availability”; “Genome-wide Association Study points to novel locus” “data” “Gilles”; “Tourette disorder features pervasive neuronal” publication preprint 2026.

**Inclusion judgment:** Prefer original human genetics, prospective human studies, controlled trials, causal model experiments and directly relevant molecular studies. Retain important negative evidence even when it weakens a candidate. Preprints are explicitly labeled. Reviews were useful for discovering vocabulary but were not the evidentiary foundation for a therapeutic claim.

**Known limits:** English-language search terms predominate; no exhaustive deduplication, risk-of-bias scoring or unpublished-data search was completed. Search-result publication timestamps were sometimes misleading and were resolved against article metadata when material. Intermittent PMC challenge pages and a PubMed rate-limit response limited some full-text checks; alternative indexed abstracts, publishers and institutional manuscripts were used. The remaining limitations are explicitly retained rather than presented as verified negatives.


## Evidence-status clarification - 18 October 2026

The [second weekly synthesis](updates/2026-10-18-weekly-synthesis.md) retires unsupported extrapolations, not the twenty biological hypotheses wholesale. H07/H13 durable combination learning, H17 mechanism-specific stimulation, H18 personalized matching and H19 developmental resilience remain speculative extensions not directly tested by this week's audits. Established symptomatic benefit does not establish their causal predictions, but inconclusive functional findings do not erase that benefit.

Do not promote tic improvement into generalized pain/QoL benefit, selected returnee maintenance into all-randomized treatment-free durability, same-trial secondary reports into independent replication, or registry updates/target engagement into efficacy. The [dated claim matrix](updates/2026-10-18-weekly/claim-matrix.json) records retained findings, rejected inferences and exact unknowns. The new report-structure computation is methodological verification, not a therapeutic discovery. A secondary pain-outcome lead in Marras 2001 weakens an endpoint-absence prediction; unavailable primary methods are not evidence that pain was unmeasured.


## Evidence-status clarification - 25 October 2026

The [third weekly synthesis](updates/2026-10-25-weekly-synthesis.md) retires unsupported bridges, not biological possibilities: phase-leading state association is not causal tic initiation; short-state tic assessment is not responsive-stimulation-specific functional benefit; retrospective/pooled association is not validated prospective/adult-subgroup prediction; report counts are not independent replications. H16 responsive-stimulation utility remains a testable extension, not promoted or falsified by missing compatible aggregate function estimates. H07/H13, H17–H19 remain at their prior evidentiary status. Registry amendments do not establish motive, and null tests do not establish equivalence. Direct burden and co-occurring-condition outcomes remain necessary across ages and severities.
