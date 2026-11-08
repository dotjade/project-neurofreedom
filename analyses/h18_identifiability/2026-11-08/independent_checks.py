#!/usr/bin/env python3
"""Independent closed-form checks; deliberately does not import the simulator."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.stats import nct, t

ROOT = Path(__file__).resolve().parent


def main():
    x = json.loads((ROOT/"results.json").read_text())
    freeze = json.loads((ROOT/"plan-freeze.json").read_text())
    checks = []
    expected = []

    def check(name, passed, detail=None):
        checks.append({"name": name, "passed": bool(passed), "detail": detail})

    check("frozen_plan_unchanged", hashlib.sha256((ROOT/"plan.md").read_bytes()).hexdigest()
          == freeze["plan_sha256"] == x["plan_sha256"])
    check("scenario_count_measurement", len(x["measurement"]) == 14)
    check("scenario_count_transfer", len(x["transfer"]) == 6)
    check("scenario_seeds_unique", len({tuple(v["spawn_key"]) for v in x["measurement"]+x["transfer"]}) == 20)
    check("rows_not_units", all(v["independent_units"] == 60 for v in x["measurement"]))
    check("reporting_shift_equivalence", x["structural"]["equivalent_observed_means_z_u"] == [[0.5, 0.0], [0.5, 0.0]])
    check("null_vector_annihilated", x["structural"]["null_product"] == [0.0, 0.0])
    check("unknown_loading_equivalence", x["structural"]["unknown_loading_observed_means"] == [[0.5, 0.1], [0.5, 0.1]])
    check("rank_tic_only", x["structural"]["measurement_ranks"]["tic_only"]["rank"] == 1)
    check("rank_known_weak_loading", x["structural"]["measurement_ranks"]["known_invariant_weak_loading"]["rank"] == 2)
    check("rank_known_unit_loading", x["structural"]["measurement_ranks"]["known_invariant_unit_loading"]["rank"] == 2)
    check("rank_unknown_shift", x["structural"]["measurement_ranks"]["unknown_reporting_shift"]["rank"] == 2)

    # With a known b=0, the covariance follows scalar linear-combination formulas.
    # An exact one-sample t distribution gives interval coverage. The noncentral
    # t gives the exact population-dominance label probabilities under this DGP.
    n, m = 60, 4000
    for row in x["measurement"]:
        lam, r, g, c, b = (row[k] for k in ["loading", "repeats", "g", "c", "b"])
        vz = vu = (0.45**2 + 0.80**2/r)/n
        czu = (0.30*0.45**2 + 0.20*0.80**2/r)/n
        varg = vu/lam**2
        varc = vz+vu/lam**2-2*czu/lam
        covgc = czu/lam-vu/lam**2
        vard = vz+4*vu/lam**2-4*czu/lam
        calc_cov = [[varg, covgc], [covgc, varc]]
        check(row["id"]+": covariance", np.allclose(calc_cov, row["theoretical_parameter_covariance"], atol=1e-14))
        check(row["id"]+": contrast_se", abs(np.sqrt(vard)-row["theoretical_dominance_se"]) < 1e-13)
        pseudo_g, pseudo_c = g+b/lam, c-b/lam
        bias_g, bias_c = b/lam, -b/lam
        crit = t.ppf(0.975, n-1)
        delta = (pseudo_g-pseudo_c)/np.sqrt(vard)
        pg = float(nct.sf(crit, n-1, delta))
        pc = float(nct.cdf(-crit, n-1, delta))
        pu = 1-pg-pc
        expected.append({"id": row["id"], "expected_estimate_g": pseudo_g,
                         "expected_estimate_c": pseudo_c,
                         "expected_dominance_labels": {"generation_dominant": pg,
                                                       "control_dominant": pc, "unresolved": pu}})
        for key, p in [("generation_dominant", pg), ("control_dominant", pc), ("unresolved", pu)]:
            empirical = row["labels"][key]["rate"]
            tolerance = 5*np.sqrt(p*(1-p)/m)+1/m
            check(row["id"]+": exact_t_"+key, abs(empirical-p) <= tolerance,
                  {"observed": empirical, "expected": p, "five_mc_se_tolerance": tolerance})
        check(row["id"]+": labels_partition", sum(z["count"] for z in row["labels"].values()) == m)
        for name, bias, variance in [("generation_parameter", bias_g, varg),
                                     ("control_parameter", bias_c, varc),
                                     ("dominance_parameter", 2*b/lam, vard)]:
            metric = row[name]
            check(row["id"]+": "+name+"_bias", abs(metric["bias"]-bias) < 5*np.sqrt(variance/m),
                  {"observed_bias": metric["bias"], "theoretical_bias": bias})
            check(row["id"]+": "+name+"_sd", abs(metric["empirical_estimator_sd"]/np.sqrt(variance)-1) < 0.06)
            noncentral = bias/np.sqrt(variance)
            expected_coverage = float(nct.cdf(crit, n-1, noncentral)-nct.cdf(-crit, n-1, noncentral))
            p = metric["coverage_95"]["rate"]
            check(row["id"]+": "+name+"_coverage", abs(p-expected_coverage) < 5*np.sqrt(expected_coverage*(1-expected_coverage)/m)+1/m,
                  {"observed": p, "expected": expected_coverage})
        if r == 1:
            check(row["id"]+": one_row_naive_equals_cluster", row["naive_row_independent_generation_coverage"] == row["generation_parameter"]["coverage_95"])

    for row in x["transfer"]:
        expected_se = np.sqrt(2*(0.45**2+0.8**2/8)/60)
        tg, tc = row["transfer_coefficients"]
        true_gap = (tg-1)*row["g"]+(tc-1)*row["c"]
        check(row["id"]+": transfer_mean", row["gap_summary"]["truth"] == true_gap)
        check(row["id"]+": independent_streams", row["training_spawn_key"] != row["heldout_spawn_key"])
        check(row["id"]+": transfer_se", abs(expected_se-row["theoretical_gap_se"]) < 1e-13)
        check(row["id"]+": transfer_bias", abs(row["gap_summary"]["bias"]) < 5*expected_se/np.sqrt(m))
        # Welch df varies across samples, so nominal .95 is an approximation,
        # not an exact nct identity. The bound is a Monte Carlo diagnostic.
        check(row["id"]+": transfer_coverage", abs(row["gap_summary"]["coverage_95"]["rate"]-.95) < 0.02)
    for row in x["structural"]["known_transfer_ranks"]:
        tg, tc = row["coefficients"]
        check(str(row["coefficients"])+": transfer_rank", row["rank"] == (1 if tg == tc else 2))

    result = {"kind": "Independent implementation and algebra checks, not clinical validation",
              "checks_passed": sum(c["passed"] for c in checks), "checks_total": len(checks),
              "all_passed": all(c["passed"] for c in checks),
              "exact_sampling_expectations": expected, "checks": checks}
    (ROOT/"independent-check-results.json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n")
    print(f"{result['checks_passed']}/{result['checks_total']} checks passed")
    if not result["all_passed"]:
        for item in checks:
            if not item["passed"]:
                print(item)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
