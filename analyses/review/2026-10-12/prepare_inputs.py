"""Project the permitted official aggregate registry into the audit's minimal inputs.

No paper, supplement, participant record, or full registry file is downloaded or saved.
When --refresh is requested, the public registry JSON is read into memory only.
"""
import argparse
import hashlib
import json
from pathlib import Path
from urllib.request import urlopen

URL = "https://clinicaltrials.gov/api/v2/studies/NCT04578912"


def project(source_bytes):
    record = json.loads(source_bytes)
    if record["protocolSection"]["identificationModule"]["nctId"] != "NCT04578912":
        raise ValueError("Unexpected trial identifier")
    results = record["resultsSection"]
    outcomes = []
    for outcome in results["outcomeMeasuresModule"]["outcomeMeasures"]:
        outcomes.append({
            key: outcome[key]
            for key in (
                "type", "title", "paramType", "dispersionType", "unitOfMeasure",
                "denoms", "classes", "analyses"
            )
            if key in outcome
        })
    events = results["adverseEventsModule"]
    event_groups = [
        {key: group[key] for key in ("id", "title", "seriousNumAffected", "seriousNumAtRisk")}
        for group in events["eventGroups"]
    ]
    other_events = [
        {
            "term": event["term"],
            "stats": [
                {key: stat[key] for key in ("groupId", "numEvents")}
                for stat in event["stats"]
            ],
        }
        for event in events["otherEvents"]
    ]
    return {
        "provenance": {
            "source": URL,
            "nct_id": "NCT04578912",
            "source_json_sha256": hashlib.sha256(source_bytes).hexdigest(),
            "selection": "Only aggregate fields consumed by the 25-check audit, plus row labels and reported units.",
            "arm_order": ["CBIT + 1 Hz rTMS", "CBIT + cTBS", "CBIT + sham"],
            "scope": "Public trial-level aggregates. No participant information or source papers.",
        },
        "resultsSection": {
            "participantFlowModule": {"periods": results["participantFlowModule"]["periods"]},
            "outcomeMeasuresModule": {"outcomeMeasures": outcomes},
            "adverseEventsModule": {"eventGroups": event_groups, "otherEvents": other_events},
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    choice = parser.add_mutually_exclusive_group(required=True)
    choice.add_argument("--registry-json", type=Path, help="Existing permitted official aggregate JSON")
    choice.add_argument("--refresh", action="store_true", help="Read latest public official JSON into memory")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.refresh:
        with urlopen(URL, timeout=60) as response:
            source_bytes = response.read()
    else:
        source_bytes = args.registry_json.read_bytes()
    args.output.write_text(json.dumps(project(source_bytes), indent=2) + "\n")
    print(f"Saved aggregate projection: {args.output}")


if __name__ == "__main__":
    main()
