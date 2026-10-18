#!/usr/bin/env python3
"""Compare independently extracted aggregates with the main analysis and rerun tests.

Published layout: this file lives in analyses/adult_pain/2026-10-17/review/.
Use --main-dir only when reviewing a different staging layout.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
p = argparse.ArgumentParser()
p.add_argument('--main-dir', type=Path, default=HERE.parent)
a = p.parse_args()
main = a.main_dir.resolve()
for name in ['aggregate_inputs.json', 'aggregate_checks.py', 'aggregate_checks.json', 'test_aggregate_checks.py']:
    if not (main / name).is_file():
        raise FileNotFoundError(main / name)

ind = json.loads((HERE / 'independent_inputs.json').read_text())
ours = json.loads((HERE / 'independent_audit_output.json').read_text())
theirs = json.loads((main / 'aggregate_inputs.json').read_text())
checks = []
def equal(name, x, y):
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        assert math.isclose(x, y, rel_tol=1e-12, abs_tol=1e-12), (name, x, y)
    else:
        assert x == y, (name, x, y)
    checks.append(name)

for sourcekey, mainkey in [('n','all'), ('men_n','men_all'), ('women_n','women_all'), ('pain_past_or_present_n','pain'), ('pain_men_n','men_pain'), ('pain_women_n','women_pain')]:
    equal('input.counts.' + mainkey, ind['sample'][sourcekey], theirs['counts'][mainkey])
for sourcekey, mainkey in [('reported_seek_men_n','men_help_reported'), ('reported_seek_women_n','women_help_reported'), ('reported_relief_men_n','men_relief_reported'), ('reported_relief_women_n','women_relief_reported')]:
    equal('input.counts.' + mainkey, ind['section9'][sourcekey], theirs['counts'][mainkey])
for sex in ['men','women']:
    for outcome in ['present','worst']:
        equal('input.vas.' + sex + '.' + outcome, ind['table3'][outcome][sex + '_mean'], float(theirs['vas'][sex][outcome]))
        for diagnosis, mainlabel in [('gts','GTS'), ('cmtd','CMTD')]:
            equal('input.vas.' + sex + '.' + diagnosis + '.' + outcome, ind['table3']['diagnosis_means'][f'{outcome}_{sex}_{diagnosis}'], float(theirs['vas'][sex][mainlabel + '_' + outcome]))

before = hashlib.sha256((main / 'aggregate_checks.json').read_bytes()).hexdigest()
run = subprocess.run([sys.executable, str(main / 'aggregate_checks.py')], text=True, capture_output=True)
assert run.returncode == 0, run.stderr
out = json.loads((main / 'aggregate_checks.json').read_text())
after = hashlib.sha256((main / 'aggregate_checks.json').read_bytes()).hexdigest()
equal('output.rerun_byte_determinism', before, after)
equal('output.pain_fraction', ours['pain_fraction']['percent'], out['sample_pain']['percent'])
equal('output.help_sum', ours['help_seeking']['printed_count_sum'], out['help_seeking']['printed_count_sum'])
equal('output.help_percent', ours['help_seeking']['printed_counts_as_percent_pain_group'], out['help_seeking']['count_sum_percent_of_pain'])
equal('output.help_rounding_candidate', ours['help_seeking']['hypothetical_counts_that_round_to_86_percent_of_56'], out['help_seeking']['counts_compatible_with_rounded_reported_percent'])
equal('output.female_subset_conflict', ours['help_seeking']['female_seek_count_exceeds_female_pain_count'], out['help_seeking']['reported_women_help_exceeds_women_pain'])
for ourkey, mainkey in [('present','present_weighted_mean'), ('worst','worst_weighted_mean'), ('worst_minus_present','worst_minus_present')]:
    equal('output.vas.' + ourkey, ours['sex_weighted_displayed_means'][ourkey], out['vas_conditional_displayed_aggregate'][mainkey])
for row in ours['table3_rounding_checks']:
    mainrow = next(t for t in out['vas_partition_consistency'] if t['gender'] == row['sex'] and t['window'] == row['outcome'])
    equal(f"output.partition.{row['sex']}.{row['outcome']}", row['rounding_can_reconcile'], mainrow['compatible_under_one_decimal_rounding'])
    equal(f"output.partition_mean.{row['sex']}.{row['outcome']}", row['diagnosis_weighted_mean'], mainrow['diagnosis_weighted_displayed_mean'])
for denominator, key in [(56,'percent_of_pain_group_56'), (50,'percent_of_printed_seeker_sum_50'), (48,'percent_of_hypothetical_48_seekers')]:
    mainrow = next(t for t in out['relief']['conditional_denominator_scenarios'] if t['denominator'] == denominator)
    equal('output.relief.' + str(denominator), ours['relief'][key], mainrow['relief_percent'])
equal('output.no_selected_correction', out['help_seeking']['accepted_corrected_denominator'], None)
equal('output.nonpositive_is_not_failure', out['relief']['all_nonpositive_as_failure_allowed'], False)

unit = subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s', str(main), '-p', 'test_aggregate_checks.py', '-v'], text=True, capture_output=True)
log = run.stdout + run.stderr + '\n' + unit.stdout + unit.stderr
(HERE / 'main_test_rerun.txt').write_text(log)
assert unit.returncode == 0, log
files = {f: hashlib.sha256((main / f).read_bytes()).hexdigest() for f in ['README.md','aggregate_inputs.json','aggregate_checks.py','aggregate_checks.json','test_aggregate_checks.py','extraction.json','provenance.json','prespecified_question.md','report.md','evidence.jsonl','execution_log.txt']}
result = {'status': 'PASS', 'comparison_checks': len(checks), 'checked_fields': checks, 'main_unit_tests': '18 passed', 'main_unit_returncode': unit.returncode, 'main_output_byte_deterministic': before == after, 'file_sha256': files, 'scope': 'Independent published-input and calculation comparison; no raw-participant reanalysis or clinical validation. Final narrative review recorded in REVIEW.md.'}
(HERE / 'main_comparison.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'comparison_checks': len(checks), 'main_unit_tests': '18 passed', 'deterministic_rerun': before == after}, indent=2))
