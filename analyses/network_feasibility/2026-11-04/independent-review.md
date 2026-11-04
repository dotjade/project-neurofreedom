# Independent audit review, 4 November 2026

## Result

The independent standard-library reader passes **55 checks** against the recorded outputs without importing `audit.py` or running the supplied MATLAB code. All three file hashes and lengths agree with the inventory. Every finite/NaN/infinite/sign/zero count, finite extremum and dimension agrees. The nontrivial NIfTI slope (0.003921568859368563) and zero intercept were applied correctly. Both transform encodings agree for these files, with millimeter units and a shared 91 by 109 by 91 grid. No numerical correction is requested.

The code ZIP contains 14 MATLAB source files and no bundled atlas or outcome spreadsheet. Read-only inspection of its master, R-map and overlap routines supports the listed external requirements: individual outcome/spatial inputs for original associations, and separate atlas resources for overlap work. The supplied external code was not executed. The archive hash agrees with the recorded OSF hash. A public archive and CC0 license do not authorize collection of individual health information.

## Interpretation and next decision

The group-artifact integrity gate can pass while the full-pipeline gate remains closed. A three-dimensional shape alone does not establish group provenance or privacy; the paper's group-output statement and identified project manifest supply that distinction. Matching transforms do not prove correct registration, map semantics, or final-paper reproducibility. Pre-publication archive dates and the code's row-selection details justify a provenance question, not an allegation of error.

A bounded, public aggregate atlas/mask provenance gate is worthwhile before any further spatial calculation. It should establish source/version/license, exact network labels, matching anatomical space, how the analysis mask is chosen, and whether the proposed null preserves the relevant spatial structure. Stop if those cannot be established without individual data, payment, or contact. Choosing an available but incompatible atlas would not reproduce the original result. Neither a successful grid audit nor a later spatial association would demonstrate that network-guided treatment is superior or appropriate for an individual.

## Reproduce

Run `python independent_check.py /directory/with/the/three/verified/maps` using Python standard library. No random seed or external software install is required. The JSON records the actual check time, all checks and exact independent counts. This review adds computational verification, not clinical validation.
