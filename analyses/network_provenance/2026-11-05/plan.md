# Prospective bounded plan

Written 2026-11-05T02:41:00Z before executing the numerical experiment; after inspecting prior metadata and the overlap script.

Question: are the exact CAREN_GTSMAP atlas/table and appended SCAN/CON masks identifiable with public group-only provenance, version, reuse terms and compatible space? Inspect the cited primary studies and their public code/metadata only. Stop this fixed search if exact mapping is absent. Do not obtain individual data or substitute a newer atlas silently.

Synthetic methods question: with fixed true positives, false negatives and false positives, does adding true-negative background change balanced accuracy while leaving sensitivity and coverage unchanged? Prediction: balanced accuracy increases if false positives are nonzero; cover ratio is a monotone transformation of proportion covered, not independent support. Disconfirm by an unchanged/decreasing balanced accuracy under positive background addition with fixed positive false positives, or a changed coverage under those conditions. Include zero-false-positive and complete-coverage boundaries. Synthetic counts only, no anatomical or patient inference; deterministic, no seed. Derive formulas independently and check implemented outputs. This tests metric properties, not whether the published study's results are wrong.
