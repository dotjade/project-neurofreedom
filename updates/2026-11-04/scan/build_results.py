"""Build selected metadata comparisons; fail rather than label a new-date paper historical."""
import csv,datetime as dt,json,pathlib
p=pathlib.Path(__file__).resolve().parent
s=json.loads((p/'search-log.json').read_text());b=json.loads((p/'baseline.json').read_text())
pub=s['pubmed']['date_type_correction_screen']
for x in pub:
 dates=x['article_dates'] or [x['history'].get('pubmed',x['journal_pubdate'])]
 assert all(int(d['Year'])<2026 or (int(d['Year'])==2026 and int(d['Month'])<11) for d in dates),x['pmid']
 x['abstract_retained']=False;x['new_publication_since_prior_cutoff']=False
 x['screening_basis']='Electronic publication date; if absent, historical PubMed history date. Metadata-only date eligibility decision, not full-text appraisal.'
 x['screening_decision']='Historical first publication; recent metadata revision or issue assignment is not a new study.'
 if 'Case Reports' in x['types']:x['screening_decision']+=' Case report, not comparative treatment evidence; individual narrative not extracted.'
 if 'Preprint' in x['types']:x['screening_decision']+=' Preprint, not peer-reviewed evidence; no new version inferred.'
 if any(y['type']=='ErratumIn' for y in x['corrections']):x['screening_decision']+=' Linked erratum citation predates 2026; correction content not reappraised.'
 if any(y['type']=='UpdateOf' for y in x['corrections']):x['screening_decision']+=' Earlier preprint link is not independent replication or a retraction.'
(p/'pubmed-screening.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n'for x in pub))
reg=s['registry_records'];prev={x['id']:x for x in b['registry']}
for x in reg:
 x['id']=x['nctId'];x['evidence_type']='Official registry metadata, not trial results';x['selected_field_changes']=[k for k in ['status','design','hasResults','conditions','eligibility']if x.get(k)!=prev.get(x['id'],{}).get(k)];x['comparison_scope']='Selected fields versus November3 snapshot, not complete amendment history'
 x['changed_values']={k:{'previous':prev[x['id']].get(k),'current':x.get(k)}for k in x['selected_field_changes']}
 x['interpretation']='No posted results; no selected-field change.' if not x['selected_field_changes'] else 'Estimated start shifts November5 to November8; last update submission October30 to November2; posting November2 to November3. Recruitment remains RECRUITING; no posted results, diagnostic validity or treatment benefit established.'
(p/'registry-evidence.jsonl').write_text(''.join(json.dumps(x)+'\n'for x in reg))
for x in s['preprints']:
 with (p/(x['server']+'-preprint-index.tsv')).open('w')as f:
  w=csv.DictWriter(f,fieldnames=['doi','version','date'],delimiter='\t');w.writeheader();w.writerows(x['version_index'])
summary={'date':s['date'],'strict_prior_cutoff_utc':s['prior_core_end_utc'],'core_started_utc':s['started_utc'],'core_completed_utc':s['completed_utc'],'pubmed_unique_records':len(pub),'pubmed_id_occurrences':s['pubmed']['id_occurrences'],'pubmed_previous_day_overlap':s['pubmed']['previous_overlap_count'],'new_to_previous_scan_records':len(s['pubmed']['new_to_prior_scan_ids']),'verified_new_primary_publications_since_prior_cutoff':0,'preprint_doi_versions':sum(x['unique_doi_versions']for x in s['preprints']),'preprint_lexical_matches':sum(len(x['matches'])for x in s['preprints']),'qualifying_preprints':0,'registry_update_window_unique_ids':sorted({n for x in s['registry']for n in x.get('response',{}).get('nct_ids',[])}),'registry_direct_comparisons':len(reg),'registry_selected_changes':sum(bool(x['selected_field_changes'])for x in reg),'new_posted_trial_results':0,'new_retractions':0,'preprint_pagination_complete':all(x['pagination_complete_for_observed_response'] for x in s['preprints']),'api_request_errors':sum('error'in x for x in s['retrieval_requests']),'decision':'No verified new-window first publication, qualifying preprint or posted trial result. One administrative registry date change, without efficacy evidence.'}
(p/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');(p/'request-log.json').write_text(json.dumps(s['retrieval_requests'],indent=2)+'\n');print(json.dumps(summary,indent=2))
