"""Independent fixed-table accounting assertions, not clinical validation."""
import json, pathlib, subprocess, sys
p=pathlib.Path(__file__).resolve().parent
before=(p/'aggregate_checks.json').read_bytes()
subprocess.run([sys.executable,str(p/'verify_structure.py')],check=True,capture_output=True)
after=(p/'aggregate_checks.json').read_bytes()
assert before==after
x=json.loads(after)
assert x['result_publications']==3 and x['independent_randomized_trial_clusters']==2
assert x['deduplicated_trial_allocation_slots']==161+122
assert x['report_level_repeated_enrollment_slots']==161+122+122
assert x['primary_status_counts']=={'primary_superiority_not_demonstrated':1,'primary_superiority_supported':1}
assert x['randomized_functional_followup_after_verified_cessation_clusters']==[]
print('Byte-identical reproduction; five independent count/status assertions passed. No clinical effect was pooled.')
