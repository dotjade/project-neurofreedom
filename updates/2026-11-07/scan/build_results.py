"""Classify captured public metadata; no network, participant data, or full-paper retention."""
import json,pathlib,csv,datetime
P=pathlib.Path(__file__).parent
s=json.loads((P/'search-log.json').read_text());b=json.loads((P/'baseline.json').read_text());book=json.loads((P/'baseline-book-metadata.json').read_text())
prior_ids={x['pmid'] for x in b['pubmed']}|{book['record']['pmid']}
exclude={'41152527':'Surgical process model; not tic-disorder evidence.','42976243':'Body dysmorphic disorder methods; not tic-specific primary evidence.','42986906':'TICS-9 chronic-stress questionnaire acronym collision.','42990710':'Modified TICS cognitive instrument acronym collision; not tic disorders.','23556151':'Secondary GeneReviews chapter, already accounted for in prior book supplement.'}
secondary={'40531361','41503301','41777158','42667351','42736497','42984929'}
preclinical={'41288886','41717446'}
rows=[]
for x in s['pubmed']['date_type_correction_screen']:
 x['prior_complete_scan_overlap']=x['pmid'] in prior_ids
 if x['pmid']=='42993949':
  x.update(screening_decision='Include new-window peer-reviewed primary measurement paper; publisher reports April 19 preprint, so not first public disclosure.',qualifying_new_journal_publication=True,qualifying_first_public_disclosure=False)
 elif x['pmid'] in exclude:x.update(screening_decision=exclude[x['pmid']],qualifying_new_journal_publication=False)
 elif x['pmid'] in secondary:x.update(screening_decision='Historical secondary/review/perspective evidence; database revision is not new primary publication.',qualifying_new_journal_publication=False)
 elif x['pmid'] in preclinical:x.update(screening_decision='Historical preclinical study; not new-window human therapeutic evidence.',qualifying_new_journal_publication=False)
 else:x.update(screening_decision='Historical primary study predating window; retain observational and subgroup limitations, do not count metadata revision as new publication.',qualifying_new_journal_publication=False)
 rows.append(x)
(P/'pubmed-screening.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows))
regs=[]; prev={x['id']:x for x in b['registry']}
def diff(a,b,path=''):
 if isinstance(a,dict) and isinstance(b,dict):
  out=[]
  for k in sorted(a.keys()|b.keys()):out+=diff(a.get(k),b.get(k),path+'.'+k if path else k)
  return out
 return [] if a==b else [{'field':path,'previous':a,'current':b}]
for x in s['registry_records']:
 old=prev.get(x['nctId']); x['selected_field_changes']=[] if old is None else sum((diff(old.get(k),x.get(k),k) for k in ['title','status','hasResults','conditions','design','eligibility']),[])
 x['classification']='Administrative date changes only; no posted results.' if x['selected_field_changes'] else 'No selected-field change; no posted results.'
 regs.append(x)
(P/'registry-evidence.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in regs))
for p in s['preprints']:
 with (P/(p['server']+'-preprint-index.tsv')).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=['doi','version','date'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(p['version_index'])
summary={'date':'2026-11-07','core_started_utc':s['started_utc'],'core_completed_utc':s['completed_utc'],'prior_core_cutoff_utc':b['cutoff_utc'],'prior_book_supplement_cutoff_utc':book['request']['completed_utc'],'pubmed_id_occurrences':s['pubmed']['id_occurrences'],'pubmed_unique_ids':s['pubmed']['unique_records'],'pubmed_records_accounted':len(rows),'pubmed_ids_not_in_prior_complete_scan':[x['pmid'] for x in rows if not x['prior_complete_scan_overlap']],'new_peer_reviewed_primary_publications':['42993949'],'new_first_public_disclosures_verified':0,'preprint_versions':sum(x['unique_doi_versions'] for x in s['preprints']),'preprints':[{k:x[k] for k in ['server','unique_doi_versions','not_in_previous_scan_doi_versions','pagination_complete_for_observed_response','reported_totals','matches']} for x in s['preprints']],'registry_unique':len(regs),'registry_ids_changed':[x['nctId'] for x in regs if x['selected_field_changes']],'registries_with_posted_results':[x['nctId'] for x in regs if x['hasResults']],'core_request_count':len(s['retrieval_requests']),'transient_failed_requests':[x for x in s['retrieval_requests'] if 'error' in x],'new_watched_treatment_official_warning_verified':False,'interpretation':'One new journal measurement study with an older preprint, no validated treatment/clinical-benefit claim; bounded safety null not proof of safety.'}
(P/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
(P/'request-log.json').write_text(json.dumps(s['retrieval_requests'],indent=2)+'\n')
print(json.dumps(summary,indent=2))
