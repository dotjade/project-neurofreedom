# Reproduce the bounded MNS attrition analysis

Read `report.md` for the original research brief and its prominently stated source inconsistency. This directory is an executed aggregate arithmetic analysis, not a clinical dataset or treatment recommendation.

Requirements: Python 3.10+ standard library; no packages, network, paid services or participant data.

From this directory:

```sh
python analyze.py
python -m unittest -v test_analysis.py
python check_arithmetic.py
```

`analyze.py` overwrites only the generated `results.json`, `scenarios.csv` and `run_metadata.json`. The results and scenario outputs are deterministic. Execution time in metadata changes on each run. Stored logs record the delivered run; redirect a new run to new log filenames if retaining the delivered history.

Inputs are printed aggregates from Jackson et al., DOI [10.1111/jnp.70080](https://bpspsychub.onlinelibrary.wiley.com/doi/10.1111/jnp.70080), with exact source locations and retrieval limits in `inputs.json`. Reported baseline means are inconsistent. Neither baseline branch in the output is a verified correction. All formulas distinguish the 0–25 motor scale, the full baseline cohort and each returnee subset. Missing-outcome scenarios are hypothetical.

The key three-month robustness result is baseline-independent conditional on the printed paired mean change and counts: 15 × 3.40 / 26 = 1.961538 points of mean worsening among missing participants offsets the observed improvement. It is not a responder count or a clinical cutoff.
