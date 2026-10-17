#!/usr/bin/env python3
"""Independent arithmetic audit of published aggregates; no participant-level data."""
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
x = json.loads((HERE / "independent_inputs.json").read_text())
s, p, h, z = x["sample"], x["table3"], x["section9"], x["secondary_arithmetic_checks"]

def pct(a, b):
    return a / b * 100

def rounded_interval(value, decimals=1):
    half = 0.5 * 10 ** (-decimals)
    return [value - half, value + half]

def pooled_sd(groups):
    n = sum(g[0] for g in groups)
    m = sum(g[0] * g[1] for g in groups) / n
    ss = sum((a - 1) * sd**2 + a * (mu - m)**2 for a, mu, sd in groups)
    return {"mean": m, "sample_sd": math.sqrt(ss / (n - 1))}

seek_n = h["reported_seek_men_n"] + h["reported_seek_women_n"]
relief_n = h["reported_relief_men_n"] + h["reported_relief_women_n"]
weighted = {
    kind: (s["pain_men_n"] * p[kind]["men_mean"] + s["pain_women_n"] * p[kind]["women_mean"]) / s["pain_past_or_present_n"]
    for kind in ["present", "worst"]
}
stratum_checks = []
for kind in ["present", "worst"]:
    for sex in ["men", "women"]:
        n1, n2 = s[f"pain_gts_{sex}_n"], s[f"pain_cmtd_{sex}_n"]
        m1 = p["diagnosis_means"][f"{kind}_{sex}_gts"]
        m2 = p["diagnosis_means"][f"{kind}_{sex}_cmtd"]
        wm = (n1 * m1 + n2 * m2) / (n1 + n2)
        weighted_interval = rounded_interval(wm)
        total_interval = rounded_interval(p[kind][f"{sex}_mean"])
        overlap = max(weighted_interval[0], total_interval[0]) < min(weighted_interval[1], total_interval[1])
        stratum_checks.append({"outcome": kind, "sex": sex, "diagnosis_weighted_mean": wm, "diagnosis_weighted_rounding_interval": weighted_interval, "printed_total_rounding_interval": total_interval, "rounding_can_reconcile": overlap})

n56 = s["pain_past_or_present_n"]
hypothetical_seek_counts = [n for n in range(n56 + 1) if round(pct(n, n56)) == h["reported_seek_percent"]]
provider_compatibility = {}
for name, percent in h["provider_percentages"].items():
    provider_compatibility[name] = {
        "reported_percent": percent,
        "integer_counts_if_denominator_56_and_standard_one_decimal_rounding": [n for n in range(n56 + 1) if round(pct(n, n56), 1) == percent],
        "nearest_integer_count_if_denominator_56": round(percent * n56 / 100),
        "warning": "Hypothetical arithmetic check only. Do not promote inferred counts or denominator into observed data. Provider categories are not established as exclusive."
    }
a = z["ygtss_full_sample"]
result = {
    "pain_fraction": {"numerator": 56, "denominator": 76, "percent": pct(56, 76), "within_men_percent": pct(26, 38), "within_women_percent": pct(30, 38), "time_frame": "Past OR present; not current prevalence and not a defined chronic-pain case count."},
    "sex_weighted_displayed_means": {**weighted, "worst_minus_present": weighted["worst"] - weighted["present"], "warning": "Arithmetic summaries of rounded displayed aggregates, not observed raw-data means; female worst-pain stratum inconsistency remains. Gap is neither longitudinal change nor a treatment effect, and has no paired inference."},
    "table3_rounding_checks": stratum_checks,
    "help_seeking": {
        "printed_count_sum": seek_n,
        "printed_counts_as_percent_pain_group": pct(seek_n, n56),
        "printed_percent": h["reported_seek_percent"],
        "female_seek_count_exceeds_female_pain_count": h["reported_seek_women_n"] > s["pain_women_n"],
        "hypothetical_counts_that_round_to_86_percent_of_56": hypothetical_seek_counts,
        "warning": "Do not choose a corrected help-seeking numerator. The 48 alternative is a diagnostic scenario, not a recovered count."
    },
    "relief": {
        "printed_count_sum": relief_n,
        "percent_of_pain_group_56": pct(relief_n, n56),
        "percent_of_printed_seeker_sum_50": pct(relief_n, seek_n),
        "percent_of_hypothetical_48_seekers": pct(relief_n, 48),
        "printed_percent_of_seekers": h["reported_relief_percent_of_seekers"],
        "warning": "Unresolved denominator; subjective recalled usefulness, neither a trial response rate nor a causal effectiveness estimate."
    },
    "provider_denominator_checks": provider_compatibility,
    "secondary_checks": {
        "adhd_percent_if_denominator_76": pct(z["adhd"]["n"], 76),
        "sleep_disorders_percent_if_denominator_76": pct(z["sleep_disorders"]["n"], 76),
        "ygtss_pooled_from_displayed_sex_summaries": pooled_sd([(a["men_n"], a["men_mean"], a["men_sd"]), (a["women_n"], a["women_mean"], a["women_sd"])]),
        "ygtss_printed_total_sd": a["printed_total_sd"],
        "table5_women_continuous_component_sum": sum(z["table5_women_continuous"]["component_score_totals"]),
        "table5_women_continuous_printed_total": z["table5_women_continuous"]["printed_total"]
    },
    "not_reproduced": ["Paired participant-level current/worst analysis", "Mann–Whitney or Spearman tests from raw data", "Clinical diagnosis of neuropathic pain", "Scoring validation of the exact Polish instrument versions"]
}
assert sum([s["pain_men_n"], s["pain_women_n"]]) == 56
assert sum([s["gts_n"], s["cmtd_n"]]) == 76
assert math.isclose(weighted["present"], 2.925)
assert math.isclose(weighted["worst"], 4.3)
assert math.isclose(weighted["worst"] - weighted["present"], 1.375)
assert [a["rounding_can_reconcile"] for a in stratum_checks] == [True, True, True, False]
assert hypothetical_seek_counts == [48]
assert provider_compatibility["psychiatry"]["integer_counts_if_denominator_56_and_standard_one_decimal_rounding"] == []
assert result["secondary_checks"]["table5_women_continuous_component_sum"] == 100
(HERE / "independent_audit_output.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print("PASS: independent aggregate checks; reported contradictions retained, not repaired.")
print(json.dumps({"present_displayed_weighted_mean": weighted["present"], "worst_displayed_weighted_mean": weighted["worst"], "help_seeking_count_sum": seek_n, "hypothetical_86_percent_count": hypothetical_seek_counts}, indent=2))
