# Reproduce the independent registry checks

This bundle preserves the 25 deterministic assertions executed during the 12 October 2026 independent review. It contains code, the actual rerun output and a minimal projection of public trial-level aggregate inputs. It contains no paper, supplement, participant-level information or full registry record.

## Files

- `registry_checks.py`: runnable 25-assertion audit, with an additional outcome-order guard.
- `registry_inputs.json`: selected aggregate fields from official NCT04578912 JSON already retrieved for the public-evidence scan.
- `registry_checks_output.json`: actual output of the saved script, including input and source hashes.
- `prepare_inputs.py`: reproduce the projection from an existing permitted registry JSON, or optionally read the latest official record into memory and save only the projection.
- [review.md](review.md): review conclusions, source checks, limitations and reviewed artifact hashes.

## Run the preserved audit

Use Python 3 with its standard library. Do not use `-O`, which disables assertions.

```sh
python registry_checks.py
```

The result should report `PASS` and `checks_passed: 25`. The breakdown is 18 outcome assertions, 2 serious-event count assertions, 3 non-serious event-count sums and 2 participant-flow assertions. The script writes the actual result to `registry_checks_output.json`.

This audits the captured aggregate values and their extraction. It does not compute clinical effects, participant treatment-related risk or sessions with adverse events. Event counts and participant denominators must not be interchanged. Other review checks, including outcome hierarchy and endpoint interpretation, were source-reading judgments rather than these 25 assertions.

## Reproduce the input projection

With the existing official aggregate capture:

```sh
python prepare_inputs.py --registry-json /path/to/permitted/NCT04578912.json --output registry_inputs.json
```

Its source SHA-256 is `24b49a5a5bec8d4d1a6899b387aa2235941448d7a96a7aac9276c9eb5723eae7`. The projection retains that source hash and the official API URL. Original group descriptions, contacts, documents and all unneeded fields are excluded.

To inspect a later official update separately, with network access:

```sh
python prepare_inputs.py --refresh --output registry_inputs_latest.json
python registry_checks.py --input registry_inputs_latest.json --output registry_checks_latest_output.json
```

The refresh reads https://clinicaltrials.gov/api/v2/studies/NCT04578912 into memory and saves only selected aggregate fields. It was not run when packaging this review. Later source changes can legitimately cause failures or a different source hash; inspect them rather than silently replacing the expected values. Preserve the original files for the dated audit.

## Correction status

The parent revised the TMS extraction's serious-adverse-event row to distinguish its zero recorded serious events from the separate non-serious-event assessment labels. The review records both its initially reviewed hash and its corrected hash. The correction does not alter any input or assertion in this bundle.
