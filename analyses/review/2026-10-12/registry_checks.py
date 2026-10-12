"""Reproduce the 25 independent checks reported in day12_review.md.

These deterministic checks validate only extracted published aggregate facts.
They do not estimate clinical effects, affected-session counts or participant risk.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys


def audit(record):
    if sys.flags.optimize:
        raise RuntimeError("Run without -O; Python assertions must be enabled")
    results = record["resultsSection"]
    outcomes = results["outcomeMeasuresModule"]["outcomeMeasures"]
    checks = 0
    expected = [
        ([15, 13, 17], [.0312, .261, .158], [.05, .05, .03]),
        ([15, 13, 17], [.45, .01, .27], [1.25, 1.25, 1.3]),
        ([17, 16, 17], [46, 22, 18], None),
        ([17, 16, 17], [.58, -3.83, -8.24], [9.47, 23.92, 15.71]),
        ([17, 16, 17], [17, 15, 16], None),
    ]
    expected_titles = [
        "Change in Resting State fMRI Connectivity of SMA-mediated Brain Circuits",
        "Change in SMA Activation",
        "Safety: Measured as Rate of Adverse Events Related to Study Treatment",
        "Change in Tic Suppression Task",
        "Feasibility: Measured as Participant Treatment Completion",
    ]
    # Structural guard, not one of the 25 fact assertions. Prevent zip truncation
    # or a changed registry row order from silently changing what is tested.
    if [outcome["title"] for outcome in outcomes] != expected_titles:
        raise ValueError("Outcome count/order changed; inspect the registry before updating expected values")
    for outcome, (denominators, values, spreads) in zip(outcomes, expected):
        assert [int(x["value"]) for x in outcome["denoms"][0]["counts"]] == denominators
        checks += 1
        measurements = outcome["classes"][0]["categories"][0]["measurements"]
        assert [float(x["value"]) for x in measurements] == values
        checks += 1
        if spreads:
            assert [float(x["spread"]) for x in measurements] == spreads
            checks += 1
        assert not outcome.get("analyses")
        checks += 1
    events = results["adverseEventsModule"]
    groups = events["eventGroups"]
    assert [group["seriousNumAffected"] for group in groups] == [0, 0, 0]
    checks += 1
    assert [group["seriousNumAtRisk"] for group in groups] == [17, 15, 16]
    checks += 1
    for group_id, total in zip(["EG000", "EG001", "EG002"], [46, 22, 18]):
        assert sum(
            stat["numEvents"]
            for event in events["otherEvents"]
            for stat in event["stats"]
            if stat["groupId"] == group_id
        ) == total
        checks += 1
    flow = results["participantFlowModule"]["periods"][0]["milestones"]
    assert [int(x["numSubjects"]) for x in flow[0]["achievements"]] == [17, 16, 17]
    checks += 1
    assert [int(x["numSubjects"]) for x in flow[1]["achievements"]] == [17, 15, 16]
    checks += 1
    return checks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path(__file__).with_name("registry_inputs.json"))
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("registry_checks_output.json"))
    args = parser.parse_args()
    input_bytes = args.input.read_bytes()
    record = json.loads(input_bytes)
    checks = audit(record)
    output = {
        "status": "PASS",
        "checks_passed": checks,
        "check_breakdown": {
            "outcome_denominators_values_SDs_and_absent_analysis_rows": 18,
            "serious_AE_affected_and_at_risk_counts": 2,
            "nonserious_event_count_sums": 3,
            "participant_flow_started_and_completed": 2,
        },
        "input_sha256": hashlib.sha256(input_bytes).hexdigest(),
        "source_json_sha256": record["provenance"]["source_json_sha256"],
        "limits": [
            "Expected values are fixed to the 12 October 2026 reviewed capture.",
            "Event sums are not affected-session counts or participant treatment-related risks.",
            "Completion is not complete follow-up or complete endpoint availability.",
            "These checks do not validate efficacy, safety equivalence, or causal effects.",
        ],
    }
    rendered = json.dumps(output, indent=2) + "\n"
    args.output.write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
