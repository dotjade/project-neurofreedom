#!/usr/bin/env python3
"""Independent aggregate arithmetic check; Python standard library only.

Manual source extraction: Wilhelm et al. (2012), DOI
10.1001/archgenpsychiatry.2011.1528, Table 4 and Results.
https://jamanetwork.com/journals/jamapsychiatry/fullarticle/1307556
Read 2026-10-15. No participant-level data or inferred trajectories.
"""
from fractions import Fraction
from pathlib import Path
import json

OUT = Path(__file__).resolve().parent

def proportion(n, d):
    f = Fraction(n, d)
    return {"numerator": n, "denominator": d,
            "fraction": str(f), "percent": float(100*f)}

# Each row is a separate timepoint. No across-time participant matching assumed.
inputs = [
    dict(arm="CBIT", month=3, randomized=63, acute_responders=24, assessed=15, positive=13),
    dict(arm="CBIT", month=6, randomized=63, acute_responders=24, assessed=15, positive=12),
    dict(arm="PST", month=3, randomized=59, acute_responders=4, assessed=2, positive=1),
    dict(arm="PST", month=6, randomized=59, acute_responders=4, assessed=2, positive=1),
]
rows=[]
for r in inputs:
    a, n, y = r["acute_responders"], r["assessed"], r["positive"]
    missing = a-n
    assert 0 <= y <= n <= a <= r["randomized"]
    lower, upper = Fraction(y,a), Fraction(y+missing,a)
    # The unknown binary outcomes can take every integer success total 0..missing.
    scenarios = [dict(positive_among_missing=k,
                      maintenance_among_acute_responders=proportion(y+k,a))
                 for k in range(missing+1)]
    assert min(Fraction(s["maintenance_among_acute_responders"]["numerator"], a) for s in scenarios)==lower
    assert max(Fraction(s["maintenance_among_acute_responders"]["numerator"], a) for s in scenarios)==upper
    rows.append({**r,
        "assessed_without_positive_response": n-y,
        "unknown_followup_status": missing,
        "ascertainment_among_acute_responders": proportion(n,a),
        "missing_among_acute_responders": proportion(missing,a),
        "available_case_positive": proportion(y,n),
        "confirmed_positive_among_all_acute_responders": proportion(y,a),
        "missing_outcome_bound_lower": proportion(y,a),
        "missing_outcome_bound_upper": proportion(y+missing,a),
        "confirmed_positive_fraction_of_original_randomized_arm_descriptive_only": proportion(y,r["randomized"]),
        "unknown_outcome_scenarios": scenarios})

assert Fraction(12,15)==Fraction(4,5)
assert Fraction(15,24)==Fraction(5,8)
assert Fraction(9,24)==Fraction(3,8)
assert Fraction(12,24)==Fraction(1,2)
assert Fraction(12+9,24)==Fraction(7,8)
assert Fraction(13+9,24)==Fraction(11,12)
assert 63+59==122
assert 60+53==113
assert 56+49==105
assert (63-60)+(59-53)==9
assert (63-56)+(59-49)==17
assert round(100*4/59,1)==6.8
assert round(100*4/63,1)==6.3  # The abstract's printed 6.4 also differs from usual rounding.

result={
 "source":"https://jamanetwork.com/journals/jamapsychiatry/fullarticle/1307556",
 "source_locators":["Table 1","Table 4 and footnote","Methods / Study design", "Results / Outcomes", "Results / Treatment durability"],
 "interpretation":"Bounds concern the original acute responders' pointwise binary follow-up status. They are deterministic missing-outcome bounds, not confidence intervals. The available-case percentage does not identify maintenance in all acute responders unless an additional missingness assumption is imposed. None of these quantities is an all-randomized causal treatment effect, off-treatment durability, uninterrupted response, remission, cure, or an adult-only estimate.",
 "acute_response_denominator_check": {
   "randomized": {"CBIT":63,"PST":59,"total":122},
   "body_PST":proportion(4,59),
   "abstract_PST":proportion(4,63),
   "abstract_printed_percent":6.4,
   "assessment":"Use the body numerator/denominator (4/59) and disclose the abstract discrepancy. Four divided by 63 is 6.349206 percent, conventionally 6.3 percent to one decimal; 4/59 is 6.779661 percent, conventionally 6.8 percent. Do not silently repair the source."
 },
 "rows":rows,
 "assertions":"passed"
}
(OUT/"independent_output.json").write_text(json.dumps(result,indent=2)+"\n")
lines=["arm\tmonth\tacute_responders\tassessed\tpositive\tunknown\tascertainment_pct\tavailable_case_pct\tconfirmed_pct_of_acute_responders\tmissing_outcome_lower_pct\tmissing_outcome_upper_pct"]
for r in rows:
    vals=[r['arm'],r['month'],r['acute_responders'],r['assessed'],r['positive'],r['unknown_followup_status'],
          r['ascertainment_among_acute_responders']['percent'],r['available_case_positive']['percent'],
          r['confirmed_positive_among_all_acute_responders']['percent'],r['missing_outcome_bound_lower']['percent'],r['missing_outcome_bound_upper']['percent']]
    lines.append('\t'.join(str(v) for v in vals))
(OUT/"independent_output.tsv").write_text('\n'.join(lines)+'\n')
print('\n'.join(lines))
print('All independent arithmetic assertions passed.')
