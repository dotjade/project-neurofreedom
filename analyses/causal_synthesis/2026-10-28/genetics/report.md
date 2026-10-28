# Genetic liability, development and an acute tic trigger are different claims

28 October 2026. Bounded primary-source synthesis and published-aggregate arithmetic, not a patient-data study or simulation.

## Prediction and actual result

**Prediction tested:** if the reported 36-gene discovery identifies a universal Tourette-specific causal route, its disorder-specific support should survive separating CTD, OCD and combined evidence, and independent functional observations should converge without requiring the same structural lesion in every model.

**Result:** that strong interpretation is not supported. A narrower model survives: heterogeneous inherited/de novo liabilities may alter developing and mature cortico-basal-ganglia function through several routes. A liability can exist long before a tic; changing a state or symptom does not establish correction of that liability. This synthesis does not prove that no final common circuit mechanism exists.

## Wang 2026: evidence labels that must not be collapsed

[Wang et al., September 1, 2026](https://www.nature.com/articles/s41593-026-02419-5), DOI 10.1038/s41593-026-02419-5, PMID 42680906:

- High-confidence gene counts are 10 in CTD analysis, 12 in OCD, 34 combined, 36 in their union (FDR < .1). These sets overlap.
- Thirty union genes receive some evidence from both disorders; one receives CTD-only contributions and five OCD-only/unknown-tic contributions. Contribution is neither separate significance nor biological exclusivity. CELSR3's CTD-only rare-variant support coexists with OCD common-variant evidence.
- CELSR3 and WWC1 lose high-confidence status in the combined omnibus analysis but retain it in trio-only analysis. Four combined genes have singleton-control directional counterevidence. Transmitted-variant and synonymous comparisons are null.
- All case singletons have OCD; singleton analyses use European ancestry. Unknown comorbidity and limited subgroup data constrain phenotype specificity.
- PCNet network convergence does not replicate in BioGRID. Expression/network enrichment is not a perturbational demonstration or treatment target.
- Prior cohorts are reused. Rare coding scope omits other variant classes. Gene-discovery and burden denominators also differ because previously validated events from 16 QC-excluded trios were retained only for discovery.

These qualifications go beyond the October 27 abstract-only extraction. Supplementary participant/variant tables were deliberately not accessed; this is not a complete 36-gene row-by-row reanalysis.

## Executed aggregate accounting

`python analyses/causal_synthesis/2026-10-28/genetics/aggregate_checks.py`

The archived inputs/code/output use published counts only. Six assertions pass. No random seed applies.

- Contributions partition as 30 + 1 + 5 = 36; 30/36 = 83.33%. This is a fraction of gene evidence categories, not of people or causal biology.
- Two union genes lie outside the combined high-confidence set.
- Published newly sequenced counts imply 1,952 newly sequenced and 2,012 previously sequenced probands among 3,964, or 50.76% previously sequenced. This arithmetic is not an independent replication estimate, proof of newly ascertained participants, or reconstruction of cohort membership.

No statistical significance was recalculated. Full allele-level or gene-level effect estimates were not reconstructed. Pooling risk-gene counts across studies would additionally require harmonized thresholds, callable regions, ancestry, ascertainment, overlapping cohorts and gene mappings.

## Mechanistic triangulation and counterevidence

### Histamine is a useful causal foothold, not a universal deficiency

The original [HDC study, PMID 20445167](https://pubmed.ncbi.nlm.nih.gov/20445167/) provided rare genetic evidence; no individual variant or pedigree details are retained here. [Baldan et al., 2014](https://pubmed.ncbi.nlm.nih.gov/24411733/) connects Hdc disruption to mouse stereotypy/gating and histamine-dopamine physiology. Experimental histamine repletion attenuated a mouse phenotype, supporting a manipulable mechanism in that model. It does not show that dietary histamine, supplementation, receptor-wide modulation or treatment of unselected people is effective or safe. Sensory gating and drug-provoked stereotypy are not synonymous with spontaneous human tics.

Critically, [independent stereological test, PMID 28681514](https://pubmed.ncbi.nlm.nih.gov/28681514/) reports preserved striatal interneuron numbers/distribution and cortical structure in Hdc-knockout mice despite altered exploration/habituation. Thus a mandatory chain from histamine loss to structural interneuron loss to all tic-related behavior is not supported by this model. It does not exclude functional interneuron disturbance, species effects or conditional circuit convergence. No H3 clinical efficacy claim is made: a review search found trial references, but this pass did not verify primary trial results.

### Developmental interneuron evidence does not identify tic-by-tic timing

[The 2022 organoid primary study, PMID 36447010](https://pubmed.ncbi.nlm.nih.gov/36447010/) reports altered ventral patterning and reduced interneuron differentiation, with GLI/SHH/ciliary biology implicated. Its model supports an early-developmental candidate mechanism, not a universal anatomical defect, demonstrated adult repair or acute trigger. Donor background, differentiation and model maturity remain alternatives; an organoid is not an intact sensorimotor system.

[Postmortem single-nucleus study, PMID 39892689](https://pubmed.ncbi.nlm.nih.gov/39892689/), online January 30, 2025, examined six adult TS and six control donors. It reports approximately 50% fewer interneurons, altered neuronal metabolism/synaptic programs and microglial activation. This gives human persistent-adult relevance, but cross-sectional tissue cannot establish whether inflammation initiated symptoms, followed altered activity, reflected treatment, or caused developmental loss. Neither donor count nor thousands of nuclei creates thousands of independent people. No donor metadata or cell-level data were retrieved.

### Same gene need not produce the same behavioral syndrome

[2024 CELSR3/WWC1 mouse work, PMID 38683996](https://pubmed.ncbi.nlm.nih.gov/38683996/) links genetic perturbation to sensorimotor/reward/dopamine phenotypes. A [different CELSR3 mouse study, PMID 41226347](https://pubmed.ncbi.nlm.nih.gov/41226347/), reports dendritic/interneuron-excitability and gating abnormalities but lacks hyperactivity and motor-learning deficits; some behavior varies by sex. The contrasts argue against inferring one uniform lesion or therapeutic direction from a gene label. A [2025 D3 study, PMID 40155412](https://pubmed.ncbi.nlm.nih.gov/40155412/) provides additional model-level receptor perturbation, not evidence of a universal human D3 target. No model allele identifiers are retained here.

## Ranked, falsifiable next hypotheses

These are proposed research tests, not performed experiments or clinical instructions. They refine existing repository H01/H05/H06/H09-type themes, not newly discovered ideas.

1. **Functional convergence without obligatory cell loss.** In authorized model work, diverse genetic perturbations may converge on a prespecified corticostriatal transfer/gating abnormality despite different cell counts. Require matched developmental stage, multiple backgrounds, orthogonal perturbations and preservation of ordinary movement. Counterexample: replicated molecular target engagement with no common circuit phenotype, or effects explained by generalized silencing. Existing public aggregate sources cannot yet execute that test.
2. **Developmental scar versus reversible state.** Separate early developmental correction from mature-stage intervention in the same model. Predict adult functional rescue only for a subset of routes, without requiring restored cell number. Falsifier: adequate late engagement corrects the proposed molecular state but not the defined circuit/behavioral phenotype, while early intervention works. This narrows adult reversibility rather than negating genetic liability.
3. **Transdiagnostic core plus phenotype-specific branch.** Preregister held-out gene-level CTD-versus-OCD enrichment with ancestry/ascertainment-matched controls, excluding discovery cohorts. A route that disappears after that separation is not yet a CTD-specific target. Test degree/mutability/expression-matched network nulls and require agreement across independent networks or direct interaction assays; BioGRID's negative result must remain visible.

No intervention is recommended. Severe persistent adults, burden/function and co-occurring conditions must be retained in any later human validation rather than substituted with available pediatric or cellular endpoints.

## Novelty, access and stopping decision

Targeted searches on October 28 identified pre-existing HDC rescue, developmental organoid, CELSR3/D3 and gene-convergence studies. The broad convergence and mature-rescue ideas are **not novel**; the useful advance is a stricter causal chain, denominator audit and explicit counterevidence. Search logs and selected-source metadata are archived. This was not an exhaustive prior-art review.

The Nature main article was readable. PMC routes intermittently returned browser challenges; official PubMed EFetch abstracts supplied the three developmental/HDC counterevidence records. Abstract-level claims are labelled. Full supplementary gene-specific q values and independently validated functional assays remain prerequisites for a complete 36-gene target ranking. A safely separated gene-only public table could enable a later audit; participant/variant/pedigree tables are neither needed nor authorized. No contact, private data, participant collection, paid compute, source full-text storage or medical action occurred.

**Decision:** reject promotion of the 36-gene union to a universal Tourette trigger or cure target. Retain heterogeneous liability with testable circuit convergence; prioritize independent, stage-specific and endpoint-specific perturbation evidence over another unqualified gene list.
