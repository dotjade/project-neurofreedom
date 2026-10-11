#!/usr/bin/env python3
"""Deterministic published-aggregate sensitivity analysis, standard library only.

No participant data or random simulation. Negative change is improvement.
Fractions retain exact arithmetic on printed (rounded) decimal inputs; decimal
display precision is computational precision, not scientific precision.
"""
from __future__ import annotations
import csv
import hashlib
import json
import platform
from datetime import datetime, timezone
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def validate(N, n, lo, hi, B, BR, Y):
    if not isinstance(N, int) or not isinstance(n, int) or not 0 < n <= N:
        raise ValueError("Require integer 0 < observed n <= cohort N")
    if lo >= hi or not all(lo <= x <= hi for x in (B, BR, Y)):
        raise ValueError("Invalid scale or out-of-scale observed aggregate")


def full_mean(N, n, observed_mean, missing_mean):
    return (n * observed_mean + (N - n) * missing_mean) / N


def analyze_timepoint(N, n, lo, hi, B, BR, Y):
    validate(N, n, lo, hi, B, BR, Y)
    m = N - n
    observed_change = Y - BR
    out = dict(N=N, n_observed=n, n_missing=m,
               observed_fraction=F(n, N), missing_fraction=F(m, N),
               assumed_full_baseline=B, returnee_baseline=BR,
               observed_followup=Y, returnee_paired_change=observed_change,
               unpaired_observed_minus_full_baseline=Y-B,
               full_followup_lower=full_mean(N, n, Y, lo),
               full_followup_upper=full_mean(N, n, Y, hi))
    out["full_change_lower"] = out["full_followup_lower"] - B
    out["full_change_upper"] = out["full_followup_upper"] - B
    out["direction_robust_to_scale_bounded_missingness"] = out["full_change_upper"] < 0
    if m == 0:
        out.update(implied_missing_baseline=None, tipping_missing_followup=None,
                   tipping_missing_change=None, tipping_feasible=None, scenarios=[])
        return out
    BM = (N * B - n * BR) / m
    if not lo <= BM <= hi:
        raise ValueError("Baseline partition requires an out-of-scale missing mean")
    tip = (N * B - n * Y) / m
    out.update(implied_missing_baseline=BM, tipping_missing_followup=tip,
               tipping_missing_change=-n * observed_change / m,
               tipping_feasible=lo <= tip <= hi)
    candidates = [("scale_minimum", lo), ("same_followup_as_observed", Y),
                  ("same_change_as_observed", BM+observed_change),
                  ("missing_no_mean_change", BM),
                  ("missing_mean_worsening_1", BM+1),
                  ("missing_mean_worsening_2", BM+2),
                  ("missing_mean_worsening_3", BM+3),
                  ("null_tipping_point", tip), ("scale_maximum", hi)]
    out["scenarios"] = [dict(name=name, missing_mean=ym, missing_mean_change=ym-BM,
                            feasible=lo <= ym <= hi,
                            full_followup=full_mean(N,n,Y,ym),
                            full_change=full_mean(N,n,Y,ym)-B)
                        for name,ym in candidates]
    return out


def rounding_envelope(N, n, lo, hi, B_interval, BR, Y):
    """Conservative deterministic envelope for rounding, not a statistical CI."""
    eps = F("0.005")
    bl, bh = B_interval
    yl, yh = Y-eps, Y+eps
    m = N-n
    ans = dict(full_change_lower=full_mean(N,n,yl,lo)-bh,
               full_change_upper=full_mean(N,n,yh,hi)-bl)
    if m:
        ans.update(tipping_missing_followup_lower=(N*bl-n*yh)/m,
                   tipping_missing_followup_upper=(N*bh-n*yl)/m,
                   tipping_missing_change_lower=n*((BR-eps)-(Y+eps))/m,
                   tipping_missing_change_upper=n*((BR+eps)-(Y-eps))/m)
    return ans


def pack(value):
    if isinstance(value, F):
        return {"exact_fraction": str(value), "decimal": float(value)}
    if isinstance(value, dict):
        return {k: pack(v) for k,v in value.items()}
    if isinstance(value, list):
        return [pack(v) for v in value]
    return value


def compute(inputs):
    N = inputs["cohort"]["n"]
    B = F(inputs["cohort"]["baseline_mean"])
    lo,hi = F(inputs["scale"]["minimum"]), F(inputs["scale"]["maximum"])
    p = inputs["baseline_partition_check"]
    nr,nd = p["retained_n"],p["dropped_n"]
    assert nr+nd == N
    br,bd = F(p["retained_baseline_mean"]),F(p["dropped_baseline_mean"])
    pooled = (nr*br+nd*bd)/N
    ep,ed = F("0.005"),F("0.05")
    b_interval = (B-ep,B+ep)
    pool_interval = ((nr*(br-ep)+nd*(bd-ed))/N,(nr*(br+ep)+nd*(bd+ed))/N)
    result = {"analysis_id": inputs["analysis_id"],
              "interpretation": "Conditional deterministic bounds/scenarios, not treatment effects, empirical corrections, or confidence intervals.",
              "baseline_consistency": dict(printed_full_mean=B,pooled_subgroup_mean=pooled,
                  discrepancy=pooled-B,printed_full_rounding_interval=list(b_interval),
                  pooled_subgroup_rounding_interval=list(pool_interval),
                  rounding_intervals_overlap=max(b_interval[0],pool_interval[0]) <= min(b_interval[1],pool_interval[1]),
                  missing_baseline_implied_by_full_and_four_week_returnees=(N*B-nr*br)/nd,
                  printed_early_dropout_baseline=bd),
              "branches": []}
    for name,base,interval in [("conditional_printed_full_baseline",B,b_interval),
                               ("hypothetical_pooled_subgroup_baseline",pooled,pool_interval)]:
        branch = dict(name=name,baseline=base,timepoints=[])
        for t in inputs["timepoints"]:
            BR,Y = F(t["returnee_baseline_mean"]), F(t["observed_mean"])
            assert Y-BR == F(t["printed_returnee_change"])
            row = analyze_timepoint(N,t["n_observed"],lo,hi,base,BR,Y)
            row["id"] = t["id"]
            row["rounding_envelope_not_ci"] = rounding_envelope(N,t["n_observed"],lo,hi,interval,BR,Y)
            branch["timepoints"].append(row)
        result["branches"].append(branch)
    return result


def main():
    inputs = json.loads((ROOT/"inputs.json").read_text())
    results = compute(inputs)
    (ROOT/"results.json").write_text(json.dumps(pack(results),indent=2)+"\n")
    columns = ["branch","timepoint","scenario","feasible","missing_mean","missing_mean_change","full_followup","full_change"]
    with (ROOT/"scenarios.csv").open("w",newline="") as f:
        writer = csv.DictWriter(f,fieldnames=columns)
        writer.writeheader()
        for b in results["branches"]:
            for t in b["timepoints"]:
                for s in t["scenarios"]:
                    writer.writerow(dict(branch=b["name"],timepoint=t["id"],scenario=s["name"],
                        **{k:(float(s[k]) if isinstance(s[k],F) else s[k]) for k in columns[3:]}))
    print("Conditional aggregate motor-score analysis; lower severity = negative change")
    c=results["baseline_consistency"]
    print(f"Printed full baseline {float(c['printed_full_mean']):.6f}; subgroup pooled {float(c['pooled_subgroup_mean']):.6f}; rounding intervals overlap: {c['rounding_intervals_overlap']}")
    for b in results["branches"]:
        print("\n"+b["name"])
        for t in b["timepoints"]:
            print(f"{t['id']}: observed {t['n_observed']}/{t['N']}; paired change {float(t['returnee_paired_change']):.6f}; full change bounds [{float(t['full_change_lower']):.6f}, {float(t['full_change_upper']):.6f}]; tipping missing outcome {float(t['tipping_missing_followup']):.6f}; tipping missing change {float(t['tipping_missing_change']):.6f}; feasible={t['tipping_feasible']}")
    metadata = {"executed_utc":datetime.now(timezone.utc).isoformat(),"python":platform.python_version(),
                "random_seed":None,"reason_no_seed":"Deterministic exact rational arithmetic; no randomness.",
                "command":"python analyze.py","sha256":{p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                 for p in [ROOT/"ANALYSIS_SPEC.md",ROOT/"inputs.json",ROOT/"analyze.py",ROOT/"results.json",ROOT/"scenarios.csv"]}}
    (ROOT/"run_metadata.json").write_text(json.dumps(metadata,indent=2)+"\n")


if __name__ == "__main__":
    main()
