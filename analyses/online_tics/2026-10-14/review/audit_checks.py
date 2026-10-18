#!/usr/bin/env python3
"""Independent aggregate-only arithmetic for Haas et al. ONLINE-TICS (2022).

Run: python3 audit_checks.py
Source: https://doi.org/10.3390/jcm11010250, Tables 3–4 and Results 3.1–3.2.
Protocol: https://doi.org/10.3389/fpsyt.2016.00119, Secondary Analyses.
No patient records, fitted trial model, reconstructed standard errors or covariances.
"""
from decimal import Decimal as D
import json
from pathlib import Path

ROWS = [
    ("TTS_V3", "-1.28", "-2.58", "0.01", ".053", False),
    ("TTS_V4", "-2.25", "-3.75", "-.75", ".003", False),
    ("TTS_V5", "-2.71", "-4.27", "-1.16", ".001", True),
    ("impairment_V3", "-3.43", "-6.29", "-.56", ".019", False),
    ("impairment_V4", "-2.80", "-6.10", ".51", ".097", False),
    ("impairment_V5", "-5.13", "-8.72", "-1.54", ".005", False),
    ("GTS_QOL_V3", "-1.67", "-4.67", "1.32", ".272", False),
    ("GTS_QOL_V4", "-5.28", "-8.69", "-1.88", ".002", False),
    ("GTS_QOL_V5", "-4.60", "-8.21", "-.99", ".013", False),
]

def adjusted_pvalues(rows):
    """Post hoc nine-test family; .001 is a conservative bound for <.001."""
    result = {}
    maximum = D(0)
    for rank, row in enumerate(sorted(rows, key=lambda r: D(r[4]))):
        key, estimate, lower, upper, p, strict = row
        raw = D(p)
        maximum = max(maximum, (len(rows) - rank) * raw)
        result[key] = {
            "p_used": str(raw), "p_is_strict_upper_bound": strict,
            "holm_value_or_bound": str(min(D(1), maximum)),
            "bonferroni_value_or_bound": str(min(D(1), len(rows) * raw)),
            "holm_below_05": maximum < D(".05"),
            "bonferroni_below_05": len(rows) * raw < D(".05"),
            "ci_excludes_zero_in_beneficial_direction": D(upper) < 0,
        }
        # Published rounded estimates and interval midpoints should agree to .01.
        assert abs(D(estimate) - (D(lower) + D(upper)) / 2) <= D(".01")
    return result

def main():
    adjusted = adjusted_pvalues(ROWS)
    expected_survivors = {"TTS_V4", "TTS_V5", "impairment_V5", "GTS_QOL_V4"}
    assert {k for k,v in adjusted.items() if v["holm_below_05"]} == expected_survivors
    assert {k for k,v in adjusted.items() if v["bonferroni_below_05"]} == expected_survivors
    randomized = {"iCBIT": 67, "placebo": 70, "f2f_CBIT": 24}
    noncompliant = {"iCBIT": 27, "placebo": 16, "f2f_CBIT": 10}
    percentages = {"iCBIT": D("40.3"), "placebo": D("22.9"), "f2f_CBIT": D("41.7")}
    for arm, n in randomized.items():
        assert (100 * D(noncompliant[arm]) / n).quantize(D(".1")) == percentages[arm]
    assert sum(randomized.values()) == 161
    assert sum(noncompliant.values()) == 53 == 42 + 11
    assert sum(randomized.values()) - sum(noncompliant.values()) == 108
    # Gate is independent of the exploratory noninferiority interval comparison.
    primary_superiority = D(".053") < D(".05") and D(".01") < 0
    exploratory_ni_interval_below_margin = D("2.96") < D("3")
    output = {
        "scope": "Independent published-aggregate checks; not a reanalysis of patient data",
        "primary_confirmatory_superiority": primary_superiority,
        "noninferiority_confirmatory_gate_open": primary_superiority,
        "exploratory_ni_upper_below_margin": exploratory_ni_interval_below_margin,
        "ni_upper_bound_clearance_points": str(D("3") - D("2.96")),
        "randomized_by_arm": randomized,
        "noncompliant_counts_inferred_from_rounded_percentages": noncompliant,
        "compliant_counts_inferred": {k:randomized[k]-noncompliant[k] for k in randomized},
        "denominator_caveat": "Compliance counts are not observed-outcome counts or MMRM-contributor counts. Exact outcome-by-visit Ns were not supplied in the inspected main report.",
        "adjustment_caveat": "Post hoc selected nine-test family, not the trial's full testing family. No adjusted inference restores the failed confirmatory gate. p<.001 is represented only by its conservative .001 boundary.",
        "nine_test_sensitivity": adjusted,
    }
    out = Path(__file__).with_name("audit_checks.json")
    out.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
