#!/usr/bin/env python3
"""Second implementation using Decimal; does not import analyze.py.

Checks arithmetic, not independent source accuracy or statistical assumptions.
Written by the same analyst; not an independent peer review.
"""
import json
from decimal import Decimal as D, getcontext
from pathlib import Path

getcontext().prec=50
root=Path(__file__).resolve().parent
i=json.loads((root/"inputs.json").read_text())
r=json.loads((root/"results.json").read_text())
N=D(i["cohort"]["n"])
B=D(i["cohort"]["baseline_mean"])
p=i["baseline_partition_check"]
B_alt=(D(p["retained_n"])*D(p["retained_baseline_mean"])+D(p["dropped_n"])*D(p["dropped_baseline_mean"]))/N
checks=[]


def check(label, actual, stored):
    num,sep,den=stored["exact_fraction"].partition("/")
    expected=D(num)/(D(den) if sep else D(1))
    assert abs(actual-expected)<D("1e-45"),label
    checks.append(label)


for b,baseline in zip(r["branches"],[B,B_alt]):
    for t,out in zip(i["timepoints"],b["timepoints"]):
        n=D(t["n_observed"]); m=N-n
        y=D(t["observed_mean"]); br=D(t["returnee_baseline_mean"])
        prefix=b["name"]+"/"+t["id"]+"/"
        check(prefix+"paired change",y-br,out["returnee_paired_change"])
        check(prefix+"lower",(n*y)/N-baseline,out["full_change_lower"])
        check(prefix+"upper",(n*y+m*D(25))/N-baseline,out["full_change_upper"])
        check(prefix+"tip outcome",(N*baseline-n*y)/m,out["tipping_missing_followup"])
        check(prefix+"tip change",(n*br-n*y)/m,out["tipping_missing_change"])
        for s in out["scenarios"]:
            a,sep,c=s["missing_mean"]["exact_fraction"].partition("/")
            missing=D(a)/(D(c) if sep else D(1))
            check(prefix+s["name"],(n*y+m*missing)/N-baseline,s["full_change"])
print(f"PASS: {len(checks)} aggregate checks using independent Decimal formulas; no analysis-module import")
print("Month-3 paired printed means: 15.33 - 18.73 = -3.40; 15 * 3.40 = 51.00 score-points")
print("26 * 2 - 51 = 1; one score-point / 41 = +0.024390243902439 full-cohort mean change")
print("These are aggregate identities, not recovered individual outcomes or response counts.")
