"""Build original screening and selected-field comparison from saved public metadata."""
import csv,hashlib,json,pathlib,re
p=pathlib.Path(__file__).resolve().parent
s=json.loads((p/'search-log.json').read_text());b=json.loads((p/'baseline.json').read_text())
pub=s['pubmed']['date_type_correction_screen']
for x in pub:
 x['abstract_retained']=False;x['new_publication_since_prior_cutoff']=False
 x['screening_decision']='Historical first publication or prior-screened overlap; metadata revision/issue assignment is not a new study.'
 if x['pmid']=='42964513':x['screening_decision']='New retrieval of historical July 30, 2026 video-method study; not new-window publication; abstract-only method lead, not validated clinical or functional outcome.'
 if x['pmid']=='42856611':x['screening_decision']='October 1 preprint previously audited October 12; revised PubMed metadata not evidence of a new preprint version or independent trial.'
 if x['corrections']:x['screening_decision']+=' Linked PMID38767700 correction verified as historical 2024/2025, not new-window notice.'
(p/'pubmed-screening.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n'for x in pub))
reg=s['registry_records'];prev={x['id']:x for x in b['registry']}
for x in reg:
 x['id']=x['nctId'];x['evidence_type']='Official registry metadata, not trial results';x['selected_field_changes']=[k for k in ['status','design','hasResults','conditions','eligibility']if x.get(k)!=prev.get(x['id'],{}).get(k)];x['comparison_scope']='Selected fields versus November1 snapshot, not complete amendment history';x['interpretation']='No posted results; no selected-field change.' if not x['selected_field_changes'] else 'Inspect changed metadata; not efficacy evidence.'
(p/'registry-evidence.jsonl').write_text(''.join(json.dumps(x)+'\n'for x in reg))
for x in s['preprints']:
 with (p/(x['server']+'-preprint-index.tsv')).open('w')as f:
  w=csv.DictWriter(f,fieldnames=['doi','version','date'],delimiter='\t');w.writeheader();w.writerows(x['version_index'])
summary={'date':s['date'],'strict_prior_cutoff_utc':s['prior_core_end_utc'],'core_started_utc':s['started_utc'],'core_completed_utc':s['completed_utc'],'pubmed_unique_records':len(pub),'pubmed_id_occurrences':s['pubmed']['id_occurrences'],'pubmed_previous_day_overlap':s['pubmed']['previous_overlap_count'],'new_to_previous_scan_records':len(s['pubmed']['new_to_prior_scan_ids']),'verified_new_primary_publications_since_prior_cutoff':0,'preprint_doi_versions':sum(x['unique_doi_versions']for x in s['preprints']),'preprint_lexical_matches':sum(len(x['matches'])for x in s['preprints']),'qualifying_preprints':0,'registry_update_window_unique_ids':sorted({n for x in s['registry']for n in x.get('response',{}).get('nct_ids',[])}),'registry_direct_comparisons':len(reg),'registry_selected_changes':sum(bool(x['selected_field_changes'])for x in reg),'new_posted_trial_results':0,'new_retractions':0,'api_request_errors':sum('error'in x for x in s['retrieval_requests']),'decision':'No verified new-window first publication, qualifying preprint or posted trial result within bounded coverage.'}
(p/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
(p/'request-log.json').write_text(json.dumps(s['retrieval_requests'],indent=2)+'\n')
print(json.dumps(summary,indent=2));print('Registry diffs',[(x['id'],x['selected_field_changes'])for x in reg])
