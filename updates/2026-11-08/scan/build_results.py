"""Rebuild selected-field comparisons and counts from captured public metadata."""
import json,pathlib,csv
P=pathlib.Path(__file__).parent
s=json.loads((P/'search-log.json').read_text());b=json.loads((P/'baseline.json').read_text())
prior={x['pmid'] for x in b['pubmed']}
decisions={
 '41503301':'Historical narrative review marked Retracted Publication, linked to November 5 notice PMID 42991793. Status and link already present unchanged in November 7 baseline. Exclude as support for claims.',
 '41881176':'Historical March 2026 primary adult tract-imaging study, not new-window publication; retain prior observational/null-correlation limitations.',
 '42667351':'Historical August 2026 secondary DBS review; revision date is not new primary evidence.',
 '42984929':'Historical October 21 secondary clinical-assessment review, not new-window primary evidence.',
 '42990710':'Cognitive TICS instrument acronym collision, not tic-disorder evidence.',
 '42993949':'November 6 pediatric measurement study already included November 7. Same DOI/PMID and earlier April preprint; no independent new publication or validation today.',
 '42995077':'Trends in Cognitive Sciences editorial, not primary tic-disorder evidence; journal/DOI TICS collision.'
}
rows=[]
for x in s['pubmed']['date_type_correction_screen']:
 x.update(screening_decision=decisions.get(x['pmid'],'REQUIRES REVIEW'),prior_complete_scan_overlap=x['pmid'] in prior,qualifying_new_journal_publication=False,qualifying_first_public_disclosure=False)
 rows.append(x)
(P/'pubmed-screening.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows))
def diff(a,b,p=''):
 if isinstance(a,dict) and isinstance(b,dict):
  return sum((diff(a.get(k),b.get(k),p+'.'+k if p else k) for k in sorted(a.keys()|b.keys())),[])
 return [] if a==b else [{'field':p,'previous':a,'current':b}]
prev={x['id']:x for x in b['registry']};regs=[]
for x in s['registry_records']:
 old=prev.get(x['nctId']);x['selected_field_changes']=sum((diff(old.get(k),x.get(k),k) for k in ['title','status','hasResults','conditions','design','eligibility']),[]) if old else []
 x['classification']='No selected-field change; no posted results.' if not x['selected_field_changes'] else 'Changed selected fields; inspect before interpreting.'
 regs.append(x)
(P/'registry-evidence.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in regs))
for p in s['preprints']:
 with (P/(p['server']+'-preprint-index.tsv')).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=['doi','version','date'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(p['version_index'])
summary={'date':'2026-11-08','core_started_utc':s['started_utc'],'core_completed_utc':s['completed_utc'],'prior_core_cutoff_utc':b['cutoff_utc'],'pubmed_id_occurrences':s['pubmed']['id_occurrences'],'pubmed_unique_ids':s['pubmed']['unique_records'],'pubmed_records_accounted':len(rows),'pubmed_ids_not_in_prior_complete_scan':[x['pmid'] for x in rows if not x['prior_complete_scan_overlap']],'new_peer_reviewed_primary_publications':[],'new_first_public_disclosures_verified':0,'historical_retracted_review_id':'41503301','new_retraction_status_since_baseline':False,'preprint_versions':sum(x['unique_doi_versions'] for x in s['preprints']),'preprints':[{k:x[k] for k in ['server','unique_doi_versions','not_in_previous_scan_doi_versions','pagination_complete_for_observed_response','reported_totals','matches']} for x in s['preprints']],'registry_core_unique':len(regs),'registry_ids_changed':[x['nctId'] for x in regs if x['selected_field_changes']],'registry_supplement_unique':1,'registries_with_posted_results':[x['nctId'] for x in regs if x['hasResults']],'core_request_count':len(s['retrieval_requests']),'failed_requests':[x for x in s['retrieval_requests'] if 'error' in x],'new_watched_treatment_official_warning_verified':False,'interpretation':'No qualifying new-window primary publication, preprint, posted result or watched-treatment official warning verified in this bounded scan. Not proof of absence or safety.'}
(P/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');(P/'request-log.json').write_text(json.dumps(s['retrieval_requests'],indent=2)+'\n');print(json.dumps(summary,indent=2))
