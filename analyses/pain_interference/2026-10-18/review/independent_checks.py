"""Independent deterministic audit of published aggregate reporting only.

Taylor, Anderson & Davies (2022), DOI 10.3389/fpsyt.2022.914044.
Values below were read independently from publisher PDF Tables 1, 2, 3 and 5.
No participant records, inferred missing outcomes, sampling inference or corrections.
"""
from decimal import Decimal as D
from fractions import Fraction as F
import json


def run():
    checks = []

    def check(name, condition):
        assert condition, name
        checks.append(name)

    age_counts = [41, 58, 38, 24, 12, 6, 2]
    check("Age groups sum to 181", sum(age_counts) == 181)
    check("Age 19+ groups sum to 140", sum(age_counts[1:]) == 140)
    help_categories = [71, 46, 61, 3]
    check("Help categories sum to 181", sum(help_categories) == 181)
    seekers_from_categories = help_categories[0] + help_categories[1]
    check("Table-derived seekers equal 117", seekers_from_categories == 117)
    check("Table-derived seekers disagree with prose 118", seekers_from_categories != 118)
    percentages = {
        "aged_19_plus_of_all": D(140) / D(181) * 100,
        "table_seekers_of_all": D(117) / D(181) * 100,
        "prose_seekers_of_all": D(118) / D(181) * 100,
        "received_help_over_table_seekers": D(71) / D(117) * 100,
        "received_help_over_prose_seekers": D(71) / D(118) * 100,
        "table_gp_over_table_seekers": D(60) / D(117) * 100,
        "table_physio_over_table_seekers": D(42) / D(117) * 100,
    }
    check("64.6% matches table seekers at one decimal", round(percentages["table_seekers_of_all"], 1) == D("64.6"))
    check("64.6% does not match prose seekers at one decimal", round(percentages["prose_seekers_of_all"], 1) != D("64.6"))
    check("Neither received-help denominator rounds to reported 60.1%", all(round(percentages[k], 1) != D("60.1") for k in ["received_help_over_table_seekers", "received_help_over_prose_seekers"]))
    check("Table GP percentage is arithmetically coherent", round(percentages["table_gp_over_table_seekers"], 1) == D("51.3"))
    check("Table physiotherapist percentage is arithmetically coherent", round(percentages["table_physio_over_table_seekers"], 1) == D("35.9"))
    rows = [
        ("General activity", "3.24", "2.9"),
        ("Mood", "3.57", "3.31"),
        ("Walking ability", "2.41", "2.28"),
        ("Typical daily work", "3.13", "2.73"),
        ("Self-esteem", "3.63", "2.77"),
        ("Family relationships", "2.52", "1.95"),
        ("Relationships with friends", "2.56", "2.09"),
        ("Relationship with partner", "2.24", "1.78"),
        ("Social situations", "3.86", "2.74"),
        ("School or education", "3.63", "2.78"),
        ("Work/employment", "3.23", "2.72"),
        ("Sleep", "3.46", "3.24"),
        ("General enjoyment of life", "3.09", "3.04"),
    ]
    check("Thirteen printed interference domains", len(rows) == 13)
    check("All printed means are within stated 1-5 scale", all(D(1) <= D(v) <= D(5) for row in rows for v in row[1:]))
    check("Social situations has highest printed tic mean", max(rows, key=lambda r: D(r[1]))[0] == "Social situations")
    check("Mood has highest printed pain mean", max(rows, key=lambda r: D(r[2]))[0] == "Mood")
    check("All printed tic means exceed printed pain means", all(D(r[1]) > D(r[2]) for r in rows))
    check("Diagnosis status rows total 180", sum([153, 10, 17]) == 180)
    check("Prescribed pain medication rows total 178", sum([13, 31, 134]) == 178)
    check("Low-resilience ATQ components conflict with total", D("47.21") + D("28.05") != D("72.26"))
    # Independent rational construction, preserving the source's printed precision.
    def half_unit(s):
        decimals = len(s.split(".")[1]) if "." in s else 0
        return F(1, 2 * 10 ** decimals)
    rational_envelopes = {}
    for domain, t, p in rows:
        gap = F(t) - F(p)
        radius = half_unit(t) + half_unit(p)
        rational_envelopes[domain] = [str(gap - radius), str(gap + radius)]
    return {
        "status": "passed",
        "checks_passed": len(checks),
        "checks": checks,
        "conditional_percentages": {k: str(v) for k, v in percentages.items()},
        "printed_mean_differences_tic_minus_pain": {r[0]: str(D(r[1]) - D(r[2])) for r in rows},
        "independent_rational_rounding_envelopes": rational_envelopes,
        "interpretation": "Reporting arithmetic only. Printed mean differences are not established paired contrasts because matched item denominators and covariance are unavailable. No corrected counts, adult-specific pain estimate or sampling intervals are inferred.",
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
