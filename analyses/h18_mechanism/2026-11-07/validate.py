"""Deterministic consistency checks for the authored evidence map, not clinical validation."""
import hashlib,json
from pathlib import Path
D=Path(__file__).resolve().parent
checks=[]
def check(name,value): checks.append({'check':name,'passed':bool(value)})
rows=[json.loads(x) for x in (D/'evidence.jsonl').read_text().splitlines() if x.strip()]
byid={r['id']:r for r in rows}
check('nine_evidence_records',len(rows)==9)
check('stable_ids_unique',len(byid)==len(rows))
for r in rows:
 check(r['id']+'_source',r['source_url'].startswith('https://'))
 check(r['id']+'_date',r['extraction_date']=='2026-11-07')
 check(r['id']+'_no_participant_data',r['participant_data_accessed'] is False)
for pmid in ['29029679','25988365','26763495']:
 check(pmid+'_shared_cohort_label',byid['pmid:'+pmid]['cohort_ids']==['NCT00218777','NCT00231985'])
h=byid['pmid:29029679']['results']
for k in ['bootstrap_95ci_youth','bootstrap_95ci_older']:
 check(k+'_contains_zero',h[k][0]<0<h[k][1])
m=byid['pmid:25988365']['sample']
check('mcguire_denominators_retained',m['original_randomized']==248 and m['usable_baseline']==240 and m['complete_treatment_data']==207)
r=byid['pmid:38881244']['results']
check('rotstein_endpoint_separation',r['Rush_p']<.05 and r['YGTSS_p']>.05 and r['PTQ_p']>.05)
check('rotstein_no_invented_ci',r['focal_contrast_CI'] is None)
reg=byid['nct:NCT06825520']
check('registry_no_result',reg['has_results'] is False)
check('registry_stale_date_visible',reg['last_update_posted']=='2025-05-28')
cm=json.loads((D/'contrast-map.json').read_text())
check('five_focal_reports',len(cm['contrasts'])==5)
check('no_verified_matching_strategy',not any(x['randomized_model_guided_strategy'] for x in cm['contrasts']))
check('no_verified_durable_function',not any(x['verified_incremental_durable_function'] for x in cm['contrasts']))
check('report_does_not_claim_equivalence','that is not equivalence' in (D/'report.md').read_text())
check('audit_label_honest','AI-assisted categorical audit, not clinical peer review.' in cm['scope'])
check('woods_date_precision',byid['pmid:8995831']['first_publication']=='1996' and 'Winter' in byid['pmid:8995831']['publication_date_precision'])
check('verdellen_dates_month_precision',byid['pmid:15033497']['first_publication']=='2004-05' and byid['pmid:18285507']['first_publication']=='2008-03')
check('mcguire_source_p_preserved',byid['pmid:25988365']['results']['p_reported']=='<.015')
check('mcguire_recomputed_p_flagged',.01822<byid['pmid:25988365']['results']['F_tail_p_computed']<.01824)
check('mcguire_cluster_limit_explicit',any('Sidak' in x and 'participant-cluster' in x for x in byid['pmid:25988365']['limitations']))
check('erp_visit_scope','Twelve weekly' in byid['pmid:38002700']['measurement'] and 'two training' in byid['pmid:38002700']['measurement'])
check('erp_absolute_fit_visible',byid['pmid:38002700']['results']['piecewise_model_RMSEA']==.26 and byid['pmid:38002700']['results']['piecewise_model_df']==21)
check('peterson_bothersome_window','ten weeks' in byid['pmid:26763495']['results']['new_bothersome_tic_occurrence'])
check('statistic_check_available',(D/'statistical-consistency.json').exists())
check('metadata_ten_records',len(json.loads((D/'metadata-verification.json').read_text())['records'])==10)
check('reward_provenance_exists',(D/'reward-component-sources.json').exists())
check('no_full_papers_or_participant_files',all(p.suffix in ['.md','.json','.jsonl','.py'] for p in D.iterdir() if p.is_file()))
result={'scope':'Artifact consistency and exact quoted aggregate fields, not independent source/clinical review. No computed clinical effects.','passed':all(x['passed'] for x in checks),'check_count':len(checks),'checks':checks}
(D/'validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'checks':len(checks)}))
assert result['passed']
