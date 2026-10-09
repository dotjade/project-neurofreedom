"""Deterministic reporting audit, not a participant-data reanalysis.

Source: Buse et al. 2016, doi:10.3389/fpsyt.2016.00084,
publisher PDF page 4, 'Number of Tics'.
Published interaction: F(2,54)=3.1, p<0.044.
Published situation main effect: F(2,54)=3.1, p=0.053.
"""
import json
import math
import platform
import scipy
from scipy.stats import f


def df2_survival(x, denominator_df):
    # Exact F survival function when the numerator degrees of freedom equal 2.
    return (denominator_df / (denominator_df + 2 * x)) ** (denominator_df / 2)


observed = float(f.sf(3.1, 2, 54))
independent = df2_survival(3.1, 54)
assert math.isclose(observed, independent, rel_tol=1e-12, abs_tol=1e-12)
rounding_lower = float(f.sf(3.15, 2, 54))
rounding_upper = float(f.sf(3.05, 2, 54))
assert rounding_lower > 0.044
assert rounding_lower < observed < rounding_upper

print(json.dumps({
    "run_date_utc": "2026-10-09",
    "source": "https://www.frontiersin.org/articles/10.3389/fpsyt.2016.00084/pdf",
    "source_locator": "PDF page 4, Number of Tics",
    "input": {"F": 3.1, "numerator_df": 2, "denominator_df": 54,
              "F_is_published_and_potentially_rounded": True,
              "underlying_unrounded_F_available": False,
              "reported_interaction_p": "<0.044"},
    "calculated_upper_tail_p_scipy": observed,
    "calculated_upper_tail_p_closed_form": independent,
    "p_range_for_F_rounding_to_3_1_nearest_tenth": [rounding_lower, rounding_upper],
    "result": "Printed F/df and interaction p do not agree under the ordinary F distribution, including nearest-tenth rounding.",
    "limit": "Cannot identify the correct interaction statistic without original output or corrected reporting. This does not reproduce the ANOVA or show that the underlying interaction is absent.",
    "assumptions": "Ordinary upper-tail F test with the printed degrees of freedom; rounding check assumes nearest-tenth rounding of the printed F value.",
    "versions": {"python": platform.python_version(), "scipy": scipy.__version__},
    "randomness": "none"
}, indent=2))
