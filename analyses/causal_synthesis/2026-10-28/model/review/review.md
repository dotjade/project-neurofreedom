# Independent review of the synthetic identifiability construction

Reviewed 28 October 2026. This is a mathematical/software review, not clinical peer review.

## What was independently checked

`independent_checks.py` uses 60-digit Decimal closed forms, separately from the author's floating-point Boolean enumeration. All 113 checks pass: drive calibration, every event/control row, and marginal/mass constraints for the separate Fréchet construction. Comparison tolerance for rounded authored outputs is 1e-12. The author's ten tests also pass.

No random draws, patient data, fitted clinical parameters or empirical confidence intervals enter this example. The probabilities were chosen to demonstrate a logical ambiguity. This is not a new biological result, an estimate of treatment response or evidence favoring any of the candidate mechanisms.

## Inference boundaries required for integration

- Equivalence is restricted to the selected observable event probabilities and downstream-control contrasts. Latent input marginals differ, and observing those inputs could distinguish these artificial worlds. No equivalence of full trajectories, neural signals or all observable distributions is demonstrated.
- The gate is independent of the drives. Intervention effects assume perfect target selectivity, no compensation and no unmodeled causal pathways. Common operational definitions of X and Z would be necessary to compare a real perturbation across candidate models.
- A single-drive model still has a necessary gate. Abolition by blocking X therefore does not identify a literally unique cause, nor distinguish one upstream drive from necessary conjunction of two drives.
- Shared-gate suppression of ordinary actions follows from the specified control model. It does not show that every real treatment is nonspecific or that preserving ordinary actions identifies a particular origin.
- The fixed .25-marginal Fréchet scenario is separate from the .20-drive calibration. Its joint probability is not a neuronal synchrony estimate, temporal mechanism or patient-specific quantity.

## Integration recommendation

Use this as a small methods illustration explaining which inference rule fails. The substantive mechanistic synthesis must instead rest on independently checked primary evidence, counterevidence, population coverage and feasible discriminating measurements. Do not count engineered agreement as a biological discovery or a novelty claim. Any future real-world target test has separate assay, selectivity, ethics and clinical-governance prerequisites; none is authorized or executed here.

The final model report incorporates the required observational-equivalence, operational-target, independence, control and separate-scenario limits. No blocking mathematical or ethical-language issue remains in the model deliverable. Integration should retain these limits and keep this demonstration subordinate to the primary-evidence synthesis. The broader biological synthesis was not independently source-reviewed by this methods reviewer.
