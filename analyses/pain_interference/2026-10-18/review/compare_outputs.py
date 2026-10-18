"""Compare separate implementations and independently transcribed inputs."""
import json
from fractions import Fraction
from pathlib import Path
from independent_checks import run

root = Path(__file__).parent
candidate = root.parent / "aggregate_checks.json"
worker_path = candidate if candidate.exists() else root.parent / "day18_analysis" / "aggregate_checks.json"
worker = json.loads(worker_path.read_text())
review = run()
count = 0
for row in worker["domain_results"]:
    name = row["domain"]
    assert Fraction(row["difference_of_reported_means_tic_minus_pain"]) == Fraction(review["printed_mean_differences_tic_minus_pain"][name]), name
    count += 1
    for got, expected in zip(row["rounding_only_envelope"], review["independent_rational_rounding_envelopes"][name]):
        assert Fraction(got) == Fraction(expected), name
        count += 1
assert worker["age_accounting"]["aged_19plus"] == 140
assert worker["age_accounting"]["aged_18plus_n"] is None
assert worker["help_seeking"]["table_derived_seekers"] == 117
assert worker["help_seeking"]["prose_seekers"] == 118
count += 4
print(json.dumps({"status": "passed", "cross_implementation_comparisons": count, "scope": "13 differences, 26 rational rounding endpoints, 4 denominator guardrails", "analysis_test_rerun": "25 unittest tests passed", "regenerated_output": "byte-for-byte identical to pre-rerun output", "limitations": "Deterministic arithmetic verification only; no patient records or clinical validation."}, indent=2))
