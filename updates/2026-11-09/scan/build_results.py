#!/usr/bin/env python3
"""Rebuild original screening decisions and summary from retained source metadata."""
import datetime as dt,hashlib,json,pathlib
p=pathlib.Path(__file__).resolve().parent
def save(name,obj): (p/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
def lines(name,rows):(p/name).write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows))
j=json.loads((p/'search-log.json').read_text());b=json.loads((p/'baseline.json').read_text());r=json.loads((p/'preprint-recovery.json').read_text())
priorreg=json.loads((p/'prior-supplement-registry.json').read_text())['snapshot'];pr=priorreg['protocolSection']
breg={x['id']:x for x in b['registry']};breg['NCT06678737']={'title':pr['identificationModule']['briefTitle'],'status':pr['statusModule'],'conditions':pr['conditionsModule']['conditions'],'design':pr['designModule'],'eligibility':pr['eligibilityModule'],'hasResults':priorreg['hasResults']}
decisions={
 '42995077':('editorial/acronym overlap','Trends in Cognitive Sciences editorial, not primary tic-disorder evidence; already present in November 8 scan.'),
 '42995839':('unrelated preprint','Prostate-cancer metabolic-flux preprint; not tic-disorder evidence. Electronic date October 21, not a new-window first disclosure.'),
 '42996864':('historical secondary review','Pediatric NLRP3 review; electronic publication October 23. Publisher explicitly labels Review and separates animal/non-tic models from unestablished disease-specific causality. Not new primary evidence.'),
 '42997457':('historical systematic review','Cross-disorder medical-cannabis systematic review/meta-analysis; electronic publication October 29. Abstract notes limited psychiatric evidence, uncontrolled Tourette signals and heterogeneous safety estimates. No new tic RCT or individual risk estimate inferred.'),
 '42997792':('unrelated acronym','Thyroid ultrasound time-intensity curves, not tics; electronic publication October 20.'),
 '42997938':('unrelated acronym','Rabbit liver-tumor ultrasound time-intensity curves, not tics; electronic publication September 29.')}
screen=[]
for x in j['pubmed']['date_type_correction_screen']:
 y=dict(x);typ,decision=decisions.get(x['pmid'],('historical metadata update','Historical 2002–2018 publication returned by modification-date query, not a new publication. No current result inferred.'))
 y.update(screening_class=typ,screening_decision=decision,new_primary_evidence=False)
 if x['pmid']=='17665284':y['screening_decision']+=' Linked erratum citation is December 2007; not a newly verified 2026 correction.'
 screen.append(y)
lines('pubmed-screening.jsonl',screen)
registries=[]
for x in j['registry_records']:
 y=dict(x);old=breg.get(x['nctId']);keys=['title','status','hasResults','conditions','design','eligibility'];changes=[k for k in keys if old is not None and old.get(k)!=x.get(k)]
 y.update(prior_scan_overlap=old is not None,selected_field_changes=changes,classification='No selected-field change and no posted results.' if old is not None and not changes else 'Requires review')
 if x['nctId']=='NCT06678737':y['baseline_source']='November 8 supplemental official registry snapshot'
 registries.append(y)
lines('registry-evidence.jsonl',registries)
pre=[]
for s in j['preprints']:
 v=s['version_index']+(r['version_index'] if s['server']=='medrxiv' else []);unique={(x['doi'],x['version']):x for x in v};old={(x['doi'],x['version']) for x in b['preprints'][s['server']]};pages=s['pages']+(r['pages'] if s['server']=='medrxiv' else [])
 (p/(s['server']+'-preprint-index.tsv')).write_text('doi\tversion\tdate\n'+''.join(f"{x['doi']}\t{x['version']}\t{x['date']}\n" for x in unique.values()))
 pre.append({'server':s['server'],'unique_doi_versions':len(unique),'previous_scan_overlap_doi_versions':len(set(unique)&old),'not_in_previous_scan_doi_versions':len(set(unique)-old),'pagination_complete_for_observed_response':r['complete'] if s['server']=='medrxiv' else s['pagination_complete_for_observed_response'],'reported_totals':sorted(set(int(x['message'].get('total',0)) for x in pages)),'matches':s['matches']+(r['matches'] if s['server']=='medrxiv' else [])})
summary={'date':'2026-11-09','core_started_utc':j['started_utc'],'core_completed_utc':j['completed_utc'],'preprint_recovery_completed_utc':r['completed_utc'],'prior_core_cutoff_utc':b['cutoff_utc'],'pubmed_id_occurrences':j['pubmed']['id_occurrences'],'pubmed_unique_query_ids':j['pubmed']['unique_records'],'pubmed_records_accounted':len(screen),'pubmed_overlap_with_prior_query_set':j['pubmed']['previous_overlap_count'],'pubmed_ids_absent_prior_query_set':j['pubmed']['new_to_prior_scan_ids'],'directed_historical_pubmed_ids':['42947547'],'distinct_pubmed_ids_including_directed':len(screen)+1,'new_peer_reviewed_primary_publications':[],'new_primary_evidence_records_proposed':0,'preprint_versions':sum(x['unique_doi_versions'] for x in pre),'preprints':pre,'registry_core_unique':len(registries),'registry_ids_changed':[x['nctId'] for x in registries if x['selected_field_changes']],'registry_supplement_unique':1,'registry_distinct_total':len(registries)+1,'registries_with_posted_results':[],'core_request_count':len(j['retrieval_requests']),'preprint_recovery_request_count':len(r['requests']),'initial_failed_requests':[x for x in j['retrieval_requests'] if 'error' in x],'unresolved_recovery_errors':[x for x in r['requests'] if 'error' in x],'new_watched_treatment_official_warning_verified':False,'interpretation':'No qualifying new-window primary publication, preprint, posted trial result or watched-treatment official warning verified. Bounded early-day surveillance, not absence or safety proof.'}
save('summary.json',summary);save('request-log.json',j['retrieval_requests']+r['requests'])
print(json.dumps(summary,indent=2))
