"""Published-count arithmetic only; no participant records or statistical model."""
from fractions import Fraction
import json
from pathlib import Path

def overlap_bounds(n, a, b):
    assert 0 <= a <= n and 0 <= b <= n
    return max(0, a + b - n), min(a, b)

def main():
    n, n6, n12 = 95, 63, 55
    lower, upper = overlap_bounds(n, n6, n12)
    checks = 0
    for x in range(lower, upper + 1):
        cells = (x, n6-x, n12-x, n-n6-n12+x)
        assert min(cells) >= 0 and sum(cells) == n
        assert cells[0]+cells[1] == n6 and cells[0]+cells[2] == n12
        checks += 1
    for args, expected in [((0,0,0),(0,0)),((10,10,10),(10,10)),((10,0,10),(0,0)),((10,2,3),(0,2))]:
        assert overlap_bounds(*args) == expected
        checks += 1
    for values, total in [([81,13,1],95),([210,16,1],227),([82,145],227),([78,140],218),([108,119],227)]:
        assert sum(values) == total
        checks += 1
    assert Fraction(n6,n) == Fraction(63,95)
    assert Fraction(n12,n) == Fraction(11,19)
    assert lower == 23 and upper == 55
    assert 227-218 == (82-78)+(145-140) == 9
    assert 33+66-95 == 4
    checks += 5
    out = {
      "analysis_type":"deterministic aggregate-count audit; no inference about unobserved outcomes",
      "calgary_enrolled":n,
      "six_month_completed_at_analysis":{"n":n6,"fraction_of_enrollment":str(Fraction(n6,n)),"percent":100*n6/n},
      "twelve_month_completed_at_analysis":{"n":n12,"fraction_of_enrollment":str(Fraction(n12,n)),"percent":100*n12/n},
      "both_followups_completed_set_bounds":{"lower":lower,"upper":upper,"assumption":"Both completion groups are subsets of the reported 95 enrollees; endpoint item completeness is not implied."},
      "expanded_comorbidity_denominator_gap":227-218,
      "expanded_antipsychotic_count_discrepancy":{"printed_total":95,"printed_female":33,"printed_male":66,"subgroup_sum":99,"excess_over_total":4,"correct_value":"unresolved"},
      "checks_passed":checks,
      "limits":["Due-for-follow-up denominators are unavailable; these are not verified retention estimates.","Set bounds are not severe-persistence or complete-endpoint bounds.","No standard errors, covariance, causal effects or pooled estimates were calculated."]
    }
    Path(__file__).with_name("aggregate_checks.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))

if __name__ == "__main__":
    main()
