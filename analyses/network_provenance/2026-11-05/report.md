# H15 atlas provenance gate and synthetic domain audit

5 November 2026. Historical source/code audit plus **SYNTHETIC mathematical experiment**, not patient evidence or a spatial reanalysis of the clinical maps.

## Question and prior prediction

Can the exact atlas/table and SCAN/CON masks used in the archived overlap analysis be identified, licensed and mapped to a compatible space? The [prospective plan](plan.md) was saved before numerical execution. It also predicted that padding a synthetic comparison with true-negative background would increase balanced accuracy when false positives are nonzero, while coverage remains fixed. The disconfirming conditions and boundary controls were specified there.

## What was verified

[Baldermann et al.](https://doi.org/10.1038/s41467-024-55242-6), peer-reviewed, published December 16, 2024, PMID 39681552, reports network overlap and balanced accuracy. Its favorable network associations remain evidence, but not randomized targeting validation. The inspected September 2024 archive precedes the version of record. Its four-file group archive and missing individual inputs were already audited on November 4 and are not new discoveries today.

The exact code ZIP SHA256 again matches d3ca8280d97404beea905a13d6f8bbec1689ba74a909870deab106c57ac64d4e. Read-only inspection of `quantify_networkoverlaps.m` identifies `CAREN_GTSMAP.nii`, `CAREN_GTSMAP.txt`, and appended `Somato-Cognitive Action.nii` and `Cingulo-Opercular.nii` as external dependencies. The script does not establish their versions, transforms or checksums. No external code was executed.

The primary [CAREN study](https://pmc.ncbi.nlm.nih.gov/articles/PMC6771873/), Doucet et al., DOI 10.1002/hbm.24722, first online July 19, 2019, describes five networks: salience, central executive, sensorimotor, default mode and visual. The TS paper's comparator list instead includes language. The missing local table and label mapping therefore matter; a standard CAREN download cannot silently be treated as the exact study derivative. This discrepancy does not prove a paper error. The CAREN paper's CC BY-NC-ND notice is not proof of unrestricted derivative-mask rights. Its supplementary atlas and author's linked resource exist, but the exact custom derivative and its terms were not established.

The [Lead-DBS atlas catalog](https://www.lead-dbs.org/helpsupport/knowledge-base/atlasesresources/cortical-atlas-parcellations-mni-space/) independently documents standard five-network CAREN in an MNI-space collection. That is useful provenance, not a checksum/space-transform match to CAREN_GTSMAP.

The [2023 SCAN primary study](https://doi.org/10.1038/s41586-023-05964-2), published April 19, points to [GitLab](https://gitlab.com/DosenbachGreene/SCAN). That project's README redirects to [MidnightScanClub/SCAN](https://github.com/MidnightScanClub/SCAN), verified at commit 65345af77cfb99edbf1623ccccf6c96cf99d5800. Its README and MIT software license were read, and a complete repository path listing was inspected without downloading imaging files. Code dependencies include a submodule and hard-coded paths. Surface-resource names refer to Conte69/32k fs_LR, whereas the prior TS group maps have a 2 mm volumetric grid. No exact mapping to the two TS masks was established. The software license does not automatically establish rights or group-only eligibility for every bundled third-party imaging resource. No individual files, new masks or participant data were acquired.

## Executed SYNTHETIC experiment

The original [Python script](synthetic_domain.py) uses synthetic confusion counts only, with no randomness or seed. Execute `python synthetic_domain.py`; [results](synthetic-results.json) are deterministic. True positives 40, false negatives 60 and false positives 20 are held fixed. True negatives increase from 80 to 180, 1,080 and 10,080 as empty background is added.

| Added true-negative background | Coverage | Cover ratio | Balanced accuracy |
|---:|---:|---:|---:|
| 0 | 0.4 | 0.666667 | 0.600000 |
| 100 | 0.4 | 0.666667 | 0.650000 |
| 1,000 | 0.4 | 0.666667 | 0.690909 |
| 10,000 | 0.4 | 0.666667 | 0.699010 |

The prediction was supported for these constructed counts. For background addition d, the exact increase is FP*d/[2*(TN+FP)*(TN+FP+d)]. It is zero if FP=0 and positive otherwise when denominators are nonzero. Coverage c and cover ratio are linked by c/(1-c) for c<1; their rankings cannot be counted as independent corroboration. At complete coverage with a nonempty ROI, the ratio tends to positive infinity (zero denominator); the script records null as a nonfinite-result marker rather than a finite estimate. Empty-ROI coverage and balanced accuracy are undefined. Fifteen implementation assertions passed, including the no-effect FP=0 control and both boundaries. An independent exact-rational check verifies all four balanced accuracies (3/5, 13/20, 38/55 and 353/505) and invariant coverage/ratio, with 12 value checks recorded in [independent-arithmetic.json](independent-arithmetic.json). No sampling confidence interval is applicable to exact constructed counts.

The archived MATLAB script counts negatives across the loaded array and has no explicit brain-domain intersection at that step. This makes the synthetic test relevant to future mask specification. It does **not** show that the published values used inappropriate background, establish their actual bias, or reproduce their network ranking. Exact study masks, prior preprocessing and final-version mapping remain missing. Arbitrary voxel exchangeability is not justified by having many voxels; a clinical or spatial-null p-value was not computed.

## Decision and next step

**Close this bounded provenance search without a spatial specificity claim.** Reopen only when exact group-only atlas/table and SCAN/CON masks, reuse terms, final-version mapping, spatial transforms and a defensible common brain domain are publicly verifiable. Do not contact authors, acquire individual records or substitute a convenient atlas. A future authorized group comparison would prespecify alternative masks and spatially constrained nulls before inspecting its contrast; failure against those nulls would disconfirm specificity.

Next audit H13's targeted-tic learning augmentation evidence ([McGuire et al., 2020, DOI 10.1038/s41386-020-0762-4](https://doi.org/10.1038/s41386-020-0762-4)): map targeted, global and untrained-tic outcomes, follow-up and harms to test whether published aggregates support generalization or durability. Retain the separate negative D-serine/riluzole trial as counterevidence without pooling unlike mechanisms. Check aggregate access and pediatric-to-adult applicability before numerical comparison; stop if required quantities are unavailable. This is a planned literature audit, not a treatment recommendation or completed efficacy calculation. Persistent severe adult symptoms, pain, participation and co-occurring conditions remain central; these map and synthetic results say nothing about a particular patient's biology, treatment response or cure. Pediatric and chronic-tic applicability require separate evidence. The historical severe-adult SMA trial ([PMID 25912296](https://pubmed.ncbi.nlm.nih.gov/25912296/), electronic publication December 3, 2014; 2015 journal issue) randomized 20 adults and did not demonstrate active-versus-sham superiority at three weeks. Its later seven-person open-label improvement is retained but cannot supply the missing controlled comparison. This weakens simple cortical-target escalation without disproving network biology or equivalence, as preserved in H15. Any new human experiment would require clinical/institutional ethics, consent and safety oversight, none initiated here.

## Access and coverage limits

Bounded search and metadata inspection on November 5, 2026 covered exact dependency-name searches, the three primary publications, Lead-DBS catalog, GitLab project/tree, and GitHub README/license/tree. Direct Nature open redirected to an inaccessible identity endpoint; indexed primary text remained available. Earlier PMC access was intermittent. These are access limitations, not broken publications or proof that no mask exists elsewhere. No full-text paper, imaging file or external source code is republished. [Inventory](provenance.json) records URLs and unresolved gates.
