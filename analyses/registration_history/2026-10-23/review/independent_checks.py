#!/usr/bin/env python3
"""Independent metadata review; no efficacy analysis or participant observations."""
import hashlib,json,re
from pathlib import Path
root=Path(__file__).parent
original=root.parent
live=json.loads((root/'live-metadata-check.json').read_text())
checks=[]
def test(name,value):
    checks.append({'name':name,'passed':bool(value)})
    assert value,name
test('review_versions_exact',[v['version'] for v in live]==[1,7,8,13,23,24,25])
for v in live:
    n=v['version']; prior=json.loads((original/f'version-{n}-metadata.json').read_text())
    test(f'v{n}_live_url_exact',v['url']==prior['url'])
    test(f'v{n}_live_sections_exact',v['sections']==prior['sections'])
    test(f'v{n}_four_allowed_metadata_sections',[s['heading'] for s in v['sections']]==['Study Status','Study Design','Outcome Measures','Document Section'])
history=live[0]['history']
prior_history=json.loads((original/'version-1-metadata.json').read_text())['history']
test('live_history_index_exact',history==prior_history)
test('history_is_25_contiguous_versions',[int(re.search(r'[?&]a=(\d+)',r['url'])[1]) for r in history]==list(range(1,26)))
test('exact_protocol_outcome_change_label_only_v25',[i+1 for i,r in enumerate(history) if 'Outcome Measures' in r['text'].splitlines()]==[25])
def section(n,name):
    return next(s['text'] for v in live if v['version']==n for s in v['sections'] if s['heading']==name)
early=section(1,'Outcome Measures'); current=section(25,'Outcome Measures')
test('selected_pre2024_outcomes_unchanged',all(section(n,'Outcome Measures')==early for n in [7,8,13,23,24]))
test('four_to_one_declared_primary_windows',early.count('[Time Frame:')==4 and current.count('[Time Frame:')==1 and 'Primary Outcome Measures' in early and 'Primary Outcome Measures' in current)
test('40_absent_early_present_current','40%' not in early and '40%' in current)
test('current_calendar_clock_is_postoperative','[Time Frame: Baseline to 6 months post-surgery]' in current and 'month 6 post-op compared to baseline' in current)
test('masking_labels_differ_v7_v8','Double (Participant, Outcomes Assessor)' in section(7,'Study Design') and 'None (Open Label)' in section(8,'Study Design'))
test('first_submitted_qc_posted_distinct','First Submitted\n2014-02-03\nFirst Submitted that Met QC Criteria\n2014-02-04\nFirst Posted\n2014-02-06 [Estimated]' in section(1,'Study Status'))
test('current_results_submission_qc_posting_distinct','Results First Submitted\n2023-10-18\nResults First Submitted That Met QC Criteria\n2024-08-30\nResults First Posted\n2024-09-05 [Actual]' in section(25,'Study Status'))
test('protocol_date_upload_distinct','Date\n2019-09-23\nUploaded\n2023-10-10 12:40' in section(25,'Document Section'))
test('original_checker_output_reproduces_exactly',(original/'checks.json').read_bytes()==(root/'checker_copy/checks.json').read_bytes())
test('reported_clock_corrected','at six months post-surgery during continuous DBS' in (original/'report.md').read_text())
test('protocol_hash_and_page_count_verified',json.loads((root/'protocol-hash-check.json').read_text())['hash_matches_original'] and json.loads((root/'protocol-hash-check.json').read_text())['page_count']==64)
out={'scope':'Independent live metadata comparison and original-checker replication; not clinical hypothesis tests','checks':checks,'passed':len(checks),'participant_data_analyzed':False,'simulation':False,'sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(original.glob('*')) if p.is_file()}}
(root/'independent-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(f'{len(checks)} independent checks passed')
