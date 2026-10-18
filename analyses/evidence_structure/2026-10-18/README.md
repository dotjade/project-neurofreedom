# Reproduce the weekly evidence-structure audit

18 October 2026. Standard-library Python; no dependencies, randomness, network calls or participant data.

Run from this directory:

    python verify_structure.py

The program reads aggregate_inputs.json and writes aggregate_checks.json. execution_log.txt contains the actual initial run. build_inputs.py constructs the same small original input table; it need not be rerun for verification. prediction.md defines the prior coding plan; report.md explains interpretation and limitations; provenance.json records source checks.

Expected output: three result publications, two trial clusters, eleven analyst-defined inference blocks, 24 passing implementation checks. Counts are bookkeeping, never independent clinical endpoints, evidence weights or a pooled treatment estimate. Source interpretation needs separate review from program consistency.

Parent reproduction: python parent_check.py. parent_check.log records byte-identical reproduction and five separate count/status assertions.
