"""Deterministic report dependence and inference-boundary audit; stdlib only."""
import collections
import copy
import hashlib
import json
from pathlib import Path
P=Path(__file__).resolve().parent

def doi_key(value):
    value=value.strip().lower()
    for prefix in ('https://doi.org/','http://doi.org/','doi:'):
        if value.startswith(prefix): value=value[len(prefix):].strip()
    if not value.startswith('10.') or '/' not in value: raise ValueError('Invalid DOI')
    return value

def normalized_reports(data):
    reports={}
    trials={t['trial_id']:t for t in data['trials']}
    for r in data['reports']:
        if r['trial_id'] not in trials: raise ValueError('Unknown trial')
        key=doi_key(r['doi'])
        if key in reports and reports[key]['trial_id']!=r['trial_id']:
            raise ValueError('Conflicting same-report trial assignment')
        reports[key]=r
    return list(reports.values())

def status(block):
    c,r,pos=block['comparison'],block['role'],block['nominal_positive']
    if r=='gated_noninferiority':
        return 'confirmatory_gate_closed' if not block['hierarchy_gate_passed'] else 'gate_open_needs_result'
    if c=='selected_responders': return 'selected_responder_maintenance'
    if c=='postrandomization_response': return 'postrandomization_association'
    if c=='selected_within_group': return 'selected_within_group_followup'
    if c!='randomized': raise ValueError('Unknown comparison')
    if r=='primary': return 'primary_superiority_supported' if pos else 'primary_superiority_not_demonstrated'
    if not pos: return 'randomized_difference_not_demonstrated'
    if r=='exploratory': return 'exploratory_randomized_positive_some_visits'
    if r=='secondary': return 'secondary_randomized_nominal_positive'
    raise ValueError('Unknown role')

def passes_followup_claim(row, require_confirmatory=False, require_adult_only=False):
    # Every element must be verified true. Unknown exposure cannot be promoted.
    fields=['functional_favorable_reported','randomized_contrast_retained','cessation_of_platform_or_boosters_verified']
    if require_confirmatory: fields.append('confirmatory_support')
    if require_adult_only: fields.append('adult_only')
    return all(row[field] is True for field in fields)

def summarize(data):
    reports=normalized_reports(data)
    trials={t['trial_id']:t for t in data['trials']}
    clusters=sorted({r['trial_id'] for r in reports})
    by_report={r['report_id']:r for r in data['reports']}
    if len({b['id'] for b in data['inference_blocks']})!=len(data['inference_blocks']): raise ValueError('Duplicate block ID')
    blocks=[]
    for b in data['inference_blocks']:
        if b['report_id'] not in by_report: raise ValueError('Unknown report')
        if any(s not in data['sources'] for s in b['source_ids']): raise ValueError('Missing provenance')
        blocks.append({'id':b['id'],'trial_id':by_report[b['report_id']]['trial_id'],'status':status(b)})
    primaries=[b for b in blocks if b['status'].startswith('primary_')]
    primary_clusters=[b['trial_id'] for b in primaries]
    if len(set(primary_clusters))!=len(primary_clusters): raise ValueError('Primary contrast double counting')
    qualified=[r['trial_id'] for r in data['followup_claims'] if passes_followup_claim(r)]
    return {
      'result_publications':len(reports),'independent_randomized_trial_clusters':len(clusters),
      'trial_to_reports':{t:sorted(r['report_id'] for r in reports if r['trial_id']==t) for t in clusters},
      'report_level_repeated_enrollment_slots':sum(trials[r['trial_id']]['randomized_allocations'] for r in reports),
      'deduplicated_trial_allocation_slots':sum(trials[t]['randomized_allocations'] for t in clusters),
      'enrollment_warning':'Allocation accounting only; not an analysis sample, adult-only N, meta-analysis or verified unique-person census across trials',
      'inference_block_count':len(blocks),'status_counts':dict(sorted(collections.Counter(b['status'] for b in blocks).items())),
      'blocks':blocks,'primary_status_counts':dict(sorted(collections.Counter(b['status'] for b in primaries).items())),
      'randomized_functional_followup_after_verified_cessation_clusters':qualified,
      'replicated_randomized_functional_followup_after_verified_cessation_supported':len(set(qualified))>=2,
      'strict_confirmatory_adult_only_cessation_clusters':[r['trial_id'] for r in data['followup_claims'] if passes_followup_claim(r,True,True)],
      'scope_warning':'Counts describe this fixed coding table only. Blocks are correlated and unequally sized, not evidence weights or a probability of efficacy.'}

def tests(data):
    checks=[]
    def check(label,condition):
        if not condition: raise AssertionError(label)
        checks.append(label)
    out=summarize(data)
    check('three_publications_two_trials',out['result_publications']==3 and out['independent_randomized_trial_clusters']==2)
    check('same_trial_secondary_publication',out['trial_to_reports']['NCT00231985']==['McGuire2020','Wilhelm2012'])
    check('date_and_doi_case_normalization',doi_key(' DOI: 10.1017/S0033291719002150 ')==doi_key('https://doi.org/10.1017/s0033291719002150'))
    duplicate=copy.deepcopy(data); duplicate['reports'].append(dict(data['reports'][2],report_id='online_2019_version',doi='https://doi.org/10.1017/S0033291719002150'))
    duplicate_out=summarize(duplicate)
    check('duplicate_date_version_does_not_add_trial',duplicate_out['independent_randomized_trial_clusters']==2 and duplicate_out['result_publications']==3)
    added=copy.deepcopy(data)
    added['trials'].append(dict(data['trials'][0],trial_id='HYPOTHETICAL_DISTINCT_TRIAL',recruitment='Distinct synthetic recruitment for software check'))
    added['reports'].append(dict(data['reports'][0],trial_id='HYPOTHETICAL_DISTINCT_TRIAL',report_id='HypotheticalReport',doi='10.9999/hypothetical'))
    added_out=summarize(added)
    check('distinct_synthetic_trial_adds_cluster',added_out['independent_randomized_trial_clusters']==3 and added_out['result_publications']==4)
    check('repeated_allocation_slots_removed',out['report_level_repeated_enrollment_slots']==405 and out['deduplicated_trial_allocation_slots']==283)
    check('genuine_acute_benefit_preserved',out['primary_status_counts']['primary_superiority_supported']==1)
    check('failed_online_primary_preserved',out['primary_status_counts']['primary_superiority_not_demonstrated']==1)
    check('eleven_preselected_blocks',out['inference_block_count']==11 and sum(out['status_counts'].values())==11)
    check('same_trial_function_does_not_inherit_primary_positive',next(b for b in out['blocks'] if b['id']=='M_randomized_function')['status']=='randomized_difference_not_demonstrated')
    check('noninferiority_gate_not_rescued',next(b for b in out['blocks'] if b['id']=='O_noninferiority')['status']=='confirmatory_gate_closed')
    check('selected_maintenance_not_randomized',next(b for b in out['blocks'] if b['id']=='W_maintenance')['status']=='selected_responder_maintenance')
    check('selected_function_not_randomized',next(b for b in out['blocks'] if b['id']=='M_followup_function')['status']=='selected_within_group_followup')
    check('responder_association_not_treatment_effect',next(b for b in out['blocks'] if b['id']=='M_response_function')['status']=='postrandomization_association')
    check('none_verified_treatment_cessation_functional_claim',out['randomized_functional_followup_after_verified_cessation_clusters']==[])
    check('no_replicated_claim',not out['replicated_randomized_functional_followup_after_verified_cessation_supported'])
    hypothetical={k:True for k in ('functional_favorable_reported','randomized_contrast_retained','cessation_of_platform_or_boosters_verified','confirmatory_support','adult_only')}
    check('claim_can_pass_when_all_requirements_verified',passes_followup_claim(hypothetical,True,True))
    for field in hypothetical:
        row=dict(hypothetical);row[field]=None
        check('unknown_'+field+'_does_not_pass_strict_claim',not passes_followup_claim(row,True,True))
    conflict=copy.deepcopy(data);conflict['reports'].append(dict(data['reports'][0],trial_id='NCT00231985'))
    try: normalized_reports(conflict)
    except ValueError: passed=True
    else: passed=False
    check('conflicting_same_doi_cluster_rejected',passed)
    check('not_equivalence_language',not any(b['status']=='equivalent' for b in out['blocks']))
    return checks

if __name__=='__main__':
    path=P/'aggregate_inputs.json'; data=json.loads(path.read_text())
    output=summarize(data); checked=tests(data)
    output['test_count']=len(checked);output['tests_passed']=checked
    output['input_sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
    output['code_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (P/'aggregate_checks.json').write_text(json.dumps(output,indent=2,sort_keys=True)+'\n')
    print(json.dumps(output,indent=2,sort_keys=True))
