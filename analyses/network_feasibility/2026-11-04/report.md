# H15 group-network artifact feasibility audit

4 November 2026. Historical public-artifact analysis, not a new clinical result or a simulation. No individual biology or treatment target is inferred.

## Question and prediction

Can the reported public archive support a lawful, group-only, free-compute replication route? The [prospective plan](plan.md), written after metadata discovery but before map download/numerical inspection, predicted that file/grid checks would be feasible while complete outcome replication would require unavailable inputs. Failed hashes, unclear group provenance or participant-level dependencies would stop the relevant stage. A failed access gate does not falsify network biology.

## Provenance and scope

[Baldermann et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11649905/) is peer-reviewed: DOI 10.1038/s41467-024-55242-6, PMID 39681552, published December 16. It studies severe adult TS using two DBS cohorts and a lesion cohort, with a normative connectome. Its associations and cross-cohort convergence do not establish superiority of individualized cortical treatment. Its data statement identifies public group imaging results and separately restricted individual imaging. Negative/mixed SMA stimulation evidence remains counterevidence in [H15](../../../hypotheses.md), including [Landeros-Weisenberger et al.](https://doi.org/10.1016/j.brs.2014.11.015). No trial or patient reanalysis occurred here.

The [OSF node](https://api.osf.io/v2/nodes/upjvb/) resolves publicly, although the web page reader did not. It links the [CC0 license record](https://api.osf.io/v2/licenses/563c1cf88c5e4a3877f9e96c/). The [complete OSF storage listing](https://api.osf.io/v2/nodes/upjvb/files/osfstorage/) contains exactly four files with no next page; its children listing is empty. The node title still says preprint and all four files are version 1 from September 16, 2024, before journal publication. Final-version equivalence is not established by a shared DOI link alone. This is a provenance limitation, not evidence of a wrong archive.

Only the three explicitly group outputs and the small code-only ZIP were retrieved. No source-data spreadsheet, individual imaging, normative individual records or participant outcomes were obtained. No author contact, account, agreement or paid resource was needed. Original summaries, metadata and code are recorded here, not papers or raw maps.

## Executed methods and actual results

[inputs.json](inputs.json) records URLs, versions, byte sizes, SHA256 values, license and plan hash. [audit.py](audit.py) is original deterministic Python with NumPy; it reads NIfTI-1 dimensions, scaling and sform, verifies bytes/hashes, then counts finite/nonfinite, signed and zero values. No seed applies. Download the three named files from their recorded public URLs into a local directory, then run `python audit.py /path/to/maps`; it checks fixed hashes before accepting results. Do not substitute other archives or participant files.

All three 3,610,868-byte files matched the source hashes. All have shape 91×109×91, 902,629 voxels, 2×2×2 header voxel spacing and the same sform. Matching headers do not independently prove anatomical alignment or final-study provenance. Three-dimensionality alone is not privacy evidence: group-only eligibility comes from the paper’s data statement, archive identity and explicit file roles, not the header. The stored scaling slope is 0.003921568859368563 with zero intercept and was applied before value summaries.

| Artifact | Finite | NaN | Positive | Negative | Zero |
|---|---:|---:|---:|---:|---:|
| Rmap.nii | 120,524 | 782,105 | 63,228 | 57,285 | 11 |
| HeatMap.nii | 902,629 | 0 | 159,731 | 126,172 | 616,726 |
| Rmap_signFDR.nii | 902,629 | 0 | 36,617 | 31,981 | 834,031 |

There are no infinite values. These are descriptive file properties, not clinical effect estimates, independent observations or voxel-wise significance tests. Different NaN/zero support conventions must not silently become a common analysis mask. The heat-map range is not assumed to be a probability, percentile or correlation simply from its filename. Full outputs are in [results.json](results.json).

The [read-only code inspection](code-inspection.json) hashes all 14 MATLAB members. No external code was run. The master/R-map routines require an outcome spreadsheet and individual stimulation-connectivity maps; they are outside the permitted group-only scope. MATLAB/Lead-DBS/SPM functions, local prototype/model files and atlas/mask inputs are also dependencies. The group-overlap routine points to external network masks/table absent from the four-file archive. The master selects 41 rows whereas the final paper reports 37 main-cohort participants; without version/exclusion mapping this is an unresolved provenance question, not a demonstrated scientific error. Recreating excluded records is neither permitted nor attempted.

## Decision, uncertainty and next experiment

**Pass:** source-linked public group-artifact access, explicit node reuse terms, exact integrity and a small free-compute structural audit.

**Do not pass:** complete published-pipeline reproduction, independent spatial specificity, targeting superiority, or clinical validation. No corrected outcome model, target shortlist, spatial-null p-value or therapeutic recommendation was produced.

The next informative safe step is one bounded inventory of the exact cited group atlas/CON/SCAN masks, license, space and version mapping. Advance only if independent, compatible, participant-free masks and a defensible brain-domain/null specification are available. Then preregister a group-map specificity comparison with spatially constrained nulls and alternate reasonable masks. Disconfirm specificity if the observed contrast is not distinguishable from those nulls or is mask-sensitive. If exact safe inputs or version mapping remain unavailable, close this route pending that prerequisite rather than search indefinitely or use participant data.

Small selected DBS cohorts, normative connectivity, lesion-versus-developmental differences, shared pipelines and absence of randomized cortical targeting limit interpretation. Broader pediatric/chronic tic populations, persistent severe adult function, pain, ADHD/OCD and other burdens need separate outcomes. This gate does not establish durable benefit or a cure. A future human targeting comparison requires a qualified clinical institution, ethics/consent, independent statistics and safety monitoring; none is initiated. No owner action is required for the next public-metadata step.
