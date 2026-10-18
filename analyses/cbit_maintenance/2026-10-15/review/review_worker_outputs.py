#!/usr/bin/env python3
"""Read-only review and independent rerun of the main audit artifacts."""
from pathlib import Path
from fractions import Fraction
from math import ceil
import hashlib, json, subprocess, sys

HERE = Path(__file__).resolve().parent
WORKER = HERE.parent if (HERE.parent/'aggregate_checks.py').exists() else HERE.parent/'day15_cbit'
files=['aggregate_checks.py','aggregate_inputs.json','aggregate_checks.json','computation_plan.md']
def hashes():
    return {f:hashlib.sha256((WORKER/f).read_bytes()).hexdigest() for f in files}
before=hashes()
p=subprocess.run([sys.executable,str(WORKER/'aggregate_checks.py'),'--input',str(WORKER/'aggregate_inputs.json'),'--output',str(HERE/'worker_rerun.json')],capture_output=True,text=True,check=True)
(HERE/'worker_rerun.log').write_text(p.stdout+p.stderr)
assert hashes()==before, 'Worker artifacts changed during review.'
original=json.loads((WORKER/'aggregate_checks.json').read_text())
rerun=json.loads((HERE/'worker_rerun.json').read_text())
assert rerun==original, 'Rerun output differs from saved worker output.'
assert (HERE/'worker_rerun.json').read_bytes()==(WORKER/'aggregate_checks.json').read_bytes(), 'Rerun bytes differ.'
ours=json.loads((HERE/'independent_output.json').read_text())
checks=['worker_files_unchanged','saved_output_matches_rerun']
for w in rerun['rows']:
    r=next(r for r in ours['rows'] if r['arm']==w['arm'] and r['month']==w['months_after_acute'])
    stem=f"{w['arm']}_{w['months_after_acute']}m"
    for theirs,own in [('eligible_acute_responders','acute_responders'),('assessed','assessed'),('positive','positive'),('unknown','unknown_followup_status')]:
        assert w[theirs]==r[own]
        checks.append(stem+'_'+theirs)
    for theirs,own in [('ascertainment','ascertainment_among_acute_responders'),('available_case_positive','available_case_positive'),('documented_positive_among_acute_responders','confirmed_positive_among_all_acute_responders'),('documented_acute_and_later_positive_among_randomized','confirmed_positive_fraction_of_original_randomized_arm_descriptive_only')]:
        assert Fraction(w[theirs]['fraction'])==Fraction(r[own]['fraction'])
        checks.append(stem+'_'+theirs)
    for endpoint in ['lower','upper']:
        assert Fraction(w['acute_responder_identification_bounds'][endpoint]['fraction'])==Fraction(r['missing_outcome_bound_'+endpoint]['fraction'])
        checks.append(stem+'_bound_'+endpoint)
    assert [Fraction(s['fraction']) for s in w['missing_outcome_scenarios']]==[Fraction(s['maintenance_among_acute_responders']['fraction']) for s in r['unknown_outcome_scenarios']]
    checks.append(stem+'_all_scenarios')
assert 12+7 < Fraction(4,5)*24 <= 12+8
assert rerun['CBIT_6m_80pct_benchmark']['minimum_missing_positive']==8
checks.append('80_percent_benchmark_independent')
rd=Fraction(24,63)-Fraction(4,59)
assert Fraction(rerun['acute_source_arithmetic']['unadjusted_risk_difference']['fraction'])==rd
assert rerun['acute_source_arithmetic']['reciprocal_risk_difference']==float(1/rd)
assert rerun['acute_source_arithmetic']['ceil_reciprocal']==ceil(1/rd)==4
assert rerun['acute_source_arithmetic']['reported_NNT']==5
checks.append('acute_NNT_discrepancy_independent')
assert rerun['tests']['passed']==37
checks.append('worker_checks_passed')
report={'verdict':'PASS: no substantive arithmetic or estimand-label defect found in reviewed computation files.',
 'worker_self_checks_passed':37,'independent_comparison_checks_passed':len(checks),
 'independent_comparison_check_names':checks,'worker_files_sha256':before,
 'worker_saved_json_identical_to_rerun':True,'worker_saved_json_byte_identical_to_rerun':True,'worker_files_unchanged':True,
 'scope':'Computation plan, aggregate input, code and saved JSON; final narrative review documented separately.'}
(HERE/'worker_review_result.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
