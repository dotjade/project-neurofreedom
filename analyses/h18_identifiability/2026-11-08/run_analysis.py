#!/usr/bin/env python3
"""Synthetic population-parameter exercise. No empirical or clinical data.

Run: python run_analysis.py --output results.json
Only NumPy/SciPy and Python standard library are required.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path

import numpy as np
import scipy
from scipy.stats import t


CONFIG = {
    "research_date": "2026-11-08",
    "master_seed": 20261108,
    "generator": "NumPy PCG64 via SeedSequence.spawn; ordered independent scenario streams",
    "monte_carlo_datasets": 4000,
    "independent_units": 60,
    "loadings": [0.25, 1.0],
    "repeats": [1, 8],
    "truths": [
        {"name": "generation", "g": 0.5, "c": 0.0},
        {"name": "control", "g": 0.0, "c": 0.5},
        {"name": "equal_mixture", "g": 0.25, "c": 0.25},
    ],
    "unit_sd": [0.45, 0.45],
    "unit_correlation": 0.30,
    "error_sd": [0.80, 0.80],
    "error_correlation": 0.20,
    "transfer_pairs": [[1.0, 1.0], [1.0, 0.25], [0.25, 1.0]],
    "units": "Arbitrary dimensionless changes; not PUTS/YGTSS or patient-derived values",
    "missingness": "None; complete rows in a deliberately idealized experiment",
}


def covariance(sd, correlation):
    a, b = sd
    return np.array([[a*a, correlation*a*b], [correlation*a*b, b*b]])


H = covariance(CONFIG["unit_sd"], CONFIG["unit_correlation"])
E = covariance(CONFIG["error_sd"], CONFIG["error_correlation"])


def probability(mask):
    """Empirical rate, MC SE, and Wilson interval over independent simulations."""
    n = len(mask)
    k = int(np.sum(mask))
    p = k/n
    z = 1.959963984540054
    denom = 1 + z*z/n
    center = (p + z*z/(2*n))/denom
    radius = z*np.sqrt(p*(1-p)/n + z*z/(4*n*n))/denom
    return {"count": k, "datasets": n, "rate": float(p),
            "monte_carlo_se": float(np.sqrt(p*(1-p)/n)),
            "wilson_95": [float(center-radius), float(center+radius)]}


def generate(rng, mean, repeats):
    """Return M x N x R x 2 paired-change observations with unit clustering."""
    m, n = CONFIG["monte_carlo_datasets"], CONFIG["independent_units"]
    h = rng.standard_normal((m, n, 2)) @ np.linalg.cholesky(H).T
    e = rng.standard_normal((m, n, repeats, 2)) @ np.linalg.cholesky(E).T
    return np.asarray(mean)[None, None, None, :] + h[:, :, None, :] + e


def summarize_parameter(est, se, truth, critical):
    err = est-truth
    return {
        "truth": float(truth),
        "mean_estimate": float(np.mean(est)),
        "bias": float(np.mean(err)),
        "monte_carlo_se_bias": float(np.std(err, ddof=1)/np.sqrt(len(err))),
        "rmse": float(np.sqrt(np.mean(err*err))),
        "empirical_estimator_sd": float(np.std(est, ddof=1)),
        "mean_estimated_se": float(np.mean(se)),
        "mean_95_interval_width": float(np.mean(2*critical*se)),
        "coverage_95": probability(np.abs(err) <= critical*se),
    }


def measurement_scenario(scenario, stream):
    rng = np.random.default_rng(stream)
    lam, r = scenario["loading"], scenario["repeats"]
    g, c, b = scenario["g"], scenario["c"], scenario["b"]
    n = CONFIG["independent_units"]
    x = generate(rng, [g+c, lam*g+b], r)
    unit_means = x.mean(axis=2)
    transform = np.array([[0, 1/lam], [1, -1/lam]])
    parameters = unit_means @ transform.T
    estimates = parameters.mean(axis=1)
    se = parameters.std(axis=1, ddof=1)/np.sqrt(n)
    critical = t.ppf(0.975, n-1)
    d = parameters[:, :, 0]-parameters[:, :, 1]
    dest, dse = d.mean(axis=1), d.std(axis=1, ddof=1)/np.sqrt(n)
    generation_label = dest-critical*dse > 0
    control_label = dest+critical*dse < 0
    unresolved = ~(generation_label | control_label)

    # Intentionally incorrect comparison: flatten repeated rows as if independent.
    naive_g = x[:, :, :, 1].reshape(len(x), n*r)/lam
    naive_se = naive_g.std(axis=1, ddof=1)/np.sqrt(n*r)
    naive_critical = t.ppf(0.975, n*r-1)

    theoretical_cov = transform @ ((H+E/r)/n) @ transform.T
    dvector = np.array([1, -1])
    return {
        **scenario,
        "spawn_key": list(stream.spawn_key),
        "independent_units": n,
        "observed_rows_per_dataset": n*r,
        "observed_mean": [g+c, lam*g+b],
        "fitted_assumptions": {"known_loading": lam, "reporting_shift": 0.0},
        "generation_parameter": summarize_parameter(estimates[:, 0], se[:, 0], g, critical),
        "control_parameter": summarize_parameter(estimates[:, 1], se[:, 1], c, critical),
        "dominance_parameter": summarize_parameter(dest, dse, g-c, critical),
        "labels": {"generation_dominant": probability(generation_label),
                   "control_dominant": probability(control_label),
                   "unresolved": probability(unresolved)},
        "naive_row_independent_generation_coverage": probability(
            np.abs(estimates[:, 0]-g) <= naive_critical*naive_se),
        "naive_to_cluster_mean_se_ratio": float(naive_se.mean()/se[:, 0].mean()),
        "theoretical_parameter_covariance": theoretical_cov.tolist(),
        "theoretical_dominance_se": float(np.sqrt(dvector @ theoretical_cov @ dvector)),
    }


def transfer_scenario(scenario, stream):
    # Independent units in each context: do not split rows from the same unit.
    train_stream, test_stream = stream.spawn(2)
    g, c = scenario["g"], scenario["c"]
    tg, tc = scenario["transfer_coefficients"]
    n, r = CONFIG["independent_units"], 8
    train = generate(np.random.default_rng(train_stream), [g+c, g], r).mean(axis=2)[:, :, 0]
    test = generate(np.random.default_rng(test_stream), [tg*g+tc*c, tg*g], r).mean(axis=2)[:, :, 0]
    train_mean, test_mean = train.mean(axis=1), test.mean(axis=1)
    gap = test_mean-train_mean
    va, vb = train.var(axis=1, ddof=1)/n, test.var(axis=1, ddof=1)/n
    se = np.sqrt(va+vb)
    df = (va+vb)**2/(va*va/(n-1)+vb*vb/(n-1))
    critical = t.ppf(0.975, df)
    true_gap = tg*g+tc*c-(g+c)
    return {
        **scenario,
        "spawn_key": list(stream.spawn_key),
        "training_spawn_key": list(train_stream.spawn_key),
        "heldout_spawn_key": list(test_stream.spawn_key),
        "independent_units_per_context": n,
        "repeats_per_unit": r,
        "training_expected_tic_change": g+c,
        "heldout_expected_tic_change": tg*g+tc*c,
        "training_full_transfer_prediction_mean": float(train_mean.mean()),
        "heldout_mean": float(test_mean.mean()),
        "gap_summary": summarize_parameter(gap, se, true_gap, critical),
        "mean_gap_interval_includes_zero": probability(np.abs(gap) <= critical*se),
        "theoretical_gap_se": float(np.sqrt(2*(H[0, 0]+E[0, 0]/r)/n)),
        "note": "Held-out data test a full-transfer population mean prediction, not individual predictions or a mechanism classifier.",
    }


def matrix_summary(a):
    a = np.asarray(a, dtype=float)
    singular = np.linalg.svd(a, compute_uv=False)
    return {"matrix": a.tolist(), "rank": int(np.linalg.matrix_rank(a)),
            "columns": a.shape[1], "singular_values": singular.tolist()}


def structural_results():
    ranks = {"tic_only": matrix_summary([[1, 1]]),
             "known_invariant_weak_loading": matrix_summary([[1, 1], [0.25, 0]]),
             "known_invariant_unit_loading": matrix_summary([[1, 1], [1, 0]]),
             "zero_loading": matrix_summary([[1, 1], [0, 0]]),
             "unknown_reporting_shift": matrix_summary([[1, 1, 0], [0.25, 0, 1]]),
             "unknown_loading_local_jacobian_at_g_0_4_lambda_0_25":
                 matrix_summary([[1, 1, 0], [0.25, 0, 0.4]])}
    transfer = [{"coefficients": [tg, tc],
                 **matrix_summary([[1, 1], [tg, tc]])}
                for tg, tc in CONFIG["transfer_pairs"]]
    # These worlds have equal full observed distributions because the covariance
    # model is fixed as well as the means. This is not merely similar fit.
    worlds = [[0.5, 0, -0.125], [0, 0.5, 0]]
    a = np.array([[1, 1, 0], [0.25, 0, 1]])
    means = np.asarray(worlds) @ a.T
    null = np.array([1, -1, -0.25])
    unknown_loading_worlds = [
        {"g": 0.4, "c": 0.1, "lambda": 0.25},
        {"g": 0.1, "c": 0.4, "lambda": 1.0},
    ]
    return {"measurement_ranks": ranks,
            "unknown_shift_null_direction": null.tolist(),
            "null_product": (a@null).tolist(),
            "equivalent_worlds_g_c_b": worlds,
            "equivalent_observed_means_z_u": means.tolist(),
            "equal_covariance_assumption": "The same H and E are specified in both worlds.",
            "unknown_loading_counterexample": unknown_loading_worlds,
            "unknown_loading_observed_means": [
                [v["g"]+v["c"], v["lambda"]*v["g"]] for v in unknown_loading_worlds],
            "known_transfer_ranks": transfer,
            "unknown_transfer_note": "Two observed tic means cannot generally identify g,c,t_g,t_c. Unequal known coefficients are an identifying assumption, not a discovered biological fact.",
            "repeated_measure_covariance_of_unit_mean": {
                str(r): (H+E/r).tolist() for r in CONFIG["repeats"]}}


def run():
    measurement = []
    for lam in CONFIG["loadings"]:
        for r in CONFIG["repeats"]:
            for truth in CONFIG["truths"]:
                measurement.append({"id": f"lambda_{lam}_r_{r}_{truth['name']}",
                                    "truth_label": truth["name"], "g": truth["g"],
                                    "c": truth["c"], "b": 0.0, "loading": lam,
                                    "repeats": r, "misspecified_shift": False})
    for lam in CONFIG["loadings"]:
        measurement.append({"id": f"lambda_{lam}_r_8_hidden_shift", "truth_label": "generation",
                            "g": 0.5, "c": 0.0, "b": -lam*0.5, "loading": lam,
                            "repeats": 8, "misspecified_shift": True})
    transfer = []
    for tg, tc in CONFIG["transfer_pairs"]:
        for truth in CONFIG["truths"][:2]:
            transfer.append({"id": f"transfer_{tg}_{tc}_{truth['name']}",
                             "truth_label": truth["name"], "g": truth["g"], "c": truth["c"],
                             "transfer_coefficients": [tg, tc]})
    streams = np.random.SeedSequence(CONFIG["master_seed"]).spawn(len(measurement)+len(transfer))
    plan = Path(__file__).with_name("plan.md")
    return {
        "kind": "Synthetic methods results, not clinical evidence",
        "config": CONFIG,
        "environment": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
        "plan_sha256": hashlib.sha256(plan.read_bytes()).hexdigest(),
        "structural": structural_results(),
        "measurement": [measurement_scenario(s, seed) for s, seed in zip(measurement, streams[:len(measurement)])],
        "transfer": [transfer_scenario(s, seed) for s, seed in zip(transfer, streams[len(measurement):])],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="results.json")
    args = parser.parse_args()
    output = Path(args.output)
    output.write_text(json.dumps(run(), indent=2, allow_nan=False)+"\n")
    print(f"Wrote {output}: 14 measurement and 6 transfer scenarios, 4,000 datasets each.")


if __name__ == "__main__":
    main()
