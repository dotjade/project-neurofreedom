"""Reproduce selected metadata classification without equating indexing with publication."""
import csv,datetime as dt,json,pathlib
p=pathlib.Path(__file__).resolve().parent
s=json.loads((p/'search-log.json').read_text());b=json.loads((p/'baseline.json').read_text());cutoff=dt.datetime.fromisoformat(b['cutoff_utc']).date()
pub=s['pubmed']['date_type_correction_screen']
for x in pub:
 x['abstract_retained']=False
 if x['pmid']=='42978485':
  x['new_publication_since_prior_cutoff']=False
  x['publisher_citation_publication_date']='2026/09/01'
  x['screening_basis']='Publisher HTML citation_publication_date=2026/09/01 directly retrieved November5; PubMed year-only date resolved against official metadata.'
  x['screening_decision']='Historical September1 case report newly indexed November4; not a new first publication or comparative efficacy evidence. Individual narrative not extracted or retained.'
  x['publisher_url']='https://www.tijdschriftvoorpsychiatrie.nl/en/artikelen/article/50-13711_Multilocus-rTMS-bij-Tourettic-obsessieve-compulsieve-stoornis'
 else:
  dates=x['article_dates'] or [x['history'].get('pubmed',x['journal_pubdate'])]
  assert all(dt.date(int(d['Year']),int(d['Month']),int(d['Day']))<cutoff for d in dates),x['pmid']
  x['new_publication_since_prior_cutoff']=False
  x['screening_basis']='Electronic first publication date; otherwise earlier PubMed history. All before prior cutoff calendar day.'
  x['screening_decision']='Previously published; indexing/metadata changes are not a new study.'
  if 'Case Reports'in x['types']:x['screening_decision']+=' Case report; individual narrative not extracted.'
  if 'Preprint'in x['types']:x['screening_decision']+=' Preprint, not peer-reviewed evidence; no new version inferred.'
  if x['pmid']=='42977160':x['screening_decision']+=' Adjacent pediatric HFMD cohort, electronic November3; abstract-only, not causal evidence for primary TS or a treatment finding.'
  if x['pmid']=='42469137':x['screening_decision']+=' July11 DBS mini-review, secondary evidence despite November issue.'
  if x['corrections']:x['screening_decision']+=' Historical linked notice/version retained; no new retraction established.'
(p/'pubmed-screening.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n'for x in pub))
reg=s['registry_records'];prev={x['id']:x for x in b['registry']}
for x in reg:
 x['id']=x['nctId'];x['evidence_type']='Official registry metadata, not trial results';x['selected_field_changes']=[k for k in ['status','design','hasResults','conditions','eligibility']if x.get(k)!=prev.get(x['id'],{}).get(k)];x['comparison_scope']='Selected fields versus November4 snapshot, not complete amendment history'
 x['changed_values']={k:{'previous':prev[x['id']].get(k),'current':x.get(k)}for k in x['selected_field_changes']}
 x['interpretation']='No posted results; no selected-field change.' if not x['selected_field_changes'] else 'Estimated start shifts November8 to November9; last update submission November2 to November3; posting November3 to November4. Recruitment remains RECRUITING; no posted results, diagnostic validity or benefit established.'
(p/'registry-evidence.jsonl').write_text(''.join(json.dumps(x)+'\n'for x in reg))
for x in s['preprints']:
 with (p/(x['server']+'-preprint-index.tsv')).open('w')as f:
  w=csv.DictWriter(f,fieldnames=['doi','version','date'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(x['version_index'])
summary={'date':s['date'],'strict_prior_cutoff_utc':s['prior_core_end_utc'],'core_started_utc':s['started_utc'],'core_completed_utc':s['completed_utc'],'pubmed_unique_records':len(pub),'pubmed_id_occurrences':s['pubmed']['id_occurrences'],'pubmed_previous_day_overlap':s['pubmed']['previous_overlap_count'],'new_to_previous_scan_records':len(s['pubmed']['new_to_prior_scan_ids']),'verified_new_primary_publications_since_prior_cutoff':0,'publication_date_unresolved_records':[],'preprint_doi_versions':sum(x['unique_doi_versions']for x in s['preprints']),'preprint_lexical_matches':sum(len(x['matches'])for x in s['preprints']),'qualifying_preprints':0,'registry_update_window_unique_ids':sorted({n for x in s['registry']for n in x.get('response',{}).get('nct_ids',[])}),'registry_direct_comparisons':len(reg),'registry_selected_changes':sum(bool(x['selected_field_changes'])for x in reg),'new_posted_trial_results':0,'new_retractions':0,'preprint_pagination_complete':all(x['pagination_complete_for_observed_response'] for x in s['preprints']),'api_request_errors':sum('error'in x for x in s['retrieval_requests']),'decision':'No verified qualifying new-window first publication, preprint or posted trial result. Newly indexed case report has verified September1 firstdate; one administrative registry date change.'}
(p/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');(p/'request-log.json').write_text(json.dumps(s['retrieval_requests'],indent=2)+'\n');print(json.dumps(summary,indent=2))
