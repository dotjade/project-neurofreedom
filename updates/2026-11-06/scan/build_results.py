"""Build screened metadata without treating indexing or registry dates as clinical results."""
import csv,datetime as dt,json,pathlib
p=pathlib.Path(__file__).resolve().parent
s=json.loads((p/'search-log.json').read_text());b=json.loads((p/'baseline.json').read_text());book=json.loads((p/'book-metadata.json').read_text());cutoff=dt.datetime.fromisoformat(b['cutoff_utc']).date()
pub=s['pubmed']['date_type_correction_screen']+[book['record']]
for x in pub:
 x['abstract_retained']=False;x['qualifying_primary_publication']=False
 if x['pmid']=='23556151':continue
 if x['pmid']=='42986906':
  x['screening_decision']='Excluded: TICS-9 is a chronic stress inventory, not a tic-disorder study. November5 electronic publication does not make it relevant.';continue
 if x['pmid']=='42978485':
  x['publisher_citation_publication_date']='2026/09/01';x['screening_basis']='Date inherited from the November5 verified publisher metadata check, not re-fetched today.'
  x['screening_decision']='Historical September1 case report; not a new controlled result. Individual narrative excluded.';continue
 dates=x['article_dates']or[x['history'].get('pubmed',x['journal_pubdate'])]
 assert all(dt.date(int(d['Year']),int(d['Month']),int(d['Day']))<cutoff for d in dates),x['pmid']
 x['screening_basis']='Electronic first publication date; otherwise earlier PubMed publication history. Before the prior cutoff calendar day.'
 x['screening_decision']='Historical first publication; indexing or metadata revisions do not establish a new study.'
 if x['pmid']=='42982044':x['screening_decision']='Newly surfaced November4 bibliographic safety case report. Before prior cutoff; no individual narrative extracted, risk rate or causal certainty established. Existing aripiprazole impulse-control warning retained separately.'
 elif x['pmid']=='42984929':x['screening_decision']='October21 pediatric Perspective; three-domain clinical heuristic explicitly not validated. Newly surfaced secondary evidence, not new clinical outcome.'
 elif x['pmid']in['41152527','42976243']:x['screening_decision']='Excluded: surgical-process/BDD study, not primary Tourette/tic-disorder evidence.'
 elif 'Review'in x['types']or'Systematic Review'in x['types']:x['screening_decision']+=' Secondary evidence, not independent primary findings.'
 elif x['pmid']in['41288886','41717446']:x['screening_decision']+=' Rat model results cannot establish human efficacy, safety, disease modification or cure.'
(p/'pubmed-screening.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n'for x in pub))
reg=s['registry_records'];prev={x['id']:x for x in b['registry']}
for x in reg:
 x['id']=x['nctId'];x['evidence_type']='Official registry metadata, not results';x['comparison_scope']='Selected protocol fields versus November5 snapshot; not complete amendment histories.'
 if x['id']not in prev:
  x['selected_field_changes']=None;x['interpretation']='New to this scan: completed mixed movement-disorder adult basic-science study, November5 update, hasResults=false. No baseline to identify amended fields. Total enrollment is not a Tourette subgroup count.'
 else:
  x['selected_field_changes']=[k for k in ['status','design','hasResults','conditions','eligibility']if x.get(k)!=prev[x['id']].get(k)]
  x['changed_values']={k:{'previous':prev[x['id']].get(k),'current':x.get(k)}for k in x['selected_field_changes']}
  x['interpretation']='No selected-field change or posted results.'if not x['selected_field_changes']else'Estimated start November9 to November10; submission November3 to November4; posting November4 to November5. Remains RECRUITING, not verification of real-world recruitment; no results or diagnostic benefit established.'
(p/'registry-evidence.jsonl').write_text(''.join(json.dumps(x)+'\n'for x in reg))
for x in s['preprints']:
 with(p/(x['server']+'-preprint-index.tsv')).open('w')as f:
  w=csv.DictWriter(f,fieldnames=['doi','version','date'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(x['version_index'])
summary={'date':s['date'],'baseline_commit':'cd78cc307253a3c38ee3b846849150721ea19264','strict_prior_cutoff_utc':s['prior_core_end_utc'],'core_started_utc':s['started_utc'],'core_completed_utc':s['completed_utc'],'metadata_supplement_completed_utc':book['request']['completed_utc'],'pubmed_id_occurrences':s['pubmed']['id_occurrences'],'pubmed_unique_ids':s['pubmed']['unique_records'],'pubmed_journal_records':len(pub)-1,'pubmed_book_records':1,'pubmed_screened_records':len(pub),'pubmed_previous_day_overlap':s['pubmed']['previous_overlap_count'],'new_to_previous_scan_ids':len(s['pubmed']['new_to_prior_scan_ids']),'verified_new_primary_publications_since_prior_cutoff':0,'preprint_doi_versions':sum(x['unique_doi_versions']for x in s['preprints']),'preprint_new_to_previous_index_versions':sum(x['not_in_previous_scan_doi_versions']for x in s['preprints']),'preprint_lexical_matches':sum(len(x['matches'])for x in s['preprints']),'qualifying_preprints':0,'registry_update_window_ids':sorted({n for x in s['registry']for n in x.get('response',{}).get('nct_ids',[])}),'registry_direct_watched_comparisons':len(s['registry_direct_controls']),'registry_total_screened':len(reg),'registry_changed_watched_records':sum(bool(x['selected_field_changes'])for x in reg),'registry_new_to_scan_records':sum(x['selected_field_changes']is None for x in reg),'posted_trial_results':sum(x['hasResults']is True for x in reg),'new_linked_retractions':0,'preprint_pagination_complete':all(x['pagination_complete_for_observed_response']for x in s['preprints']),'core_api_requests':len(s['retrieval_requests']),'core_api_errors':sum('error'in x for x in s['retrieval_requests']),'supplement_api_requests':1,'decision':'No verified qualifying new-window primary first publication, preprint or posted registry result. Preserve newly surfaced older safety case report, secondary perspective, metadata updates and source-access limits separately.'}
(p/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');(p/'request-log.json').write_text(json.dumps(s['retrieval_requests']+[book['request']],indent=2)+'\n');print(json.dumps(summary,indent=2))
