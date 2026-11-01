#!/usr/bin/env python3
"""Normalize reviewed November 1 citation metadata; reject unreviewed identifiers."""
import argparse,csv,json,pathlib,subprocess,copy
BASE='de5f1e43230840aa430f66b5c06443df128deff1'
def write(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def flat(x,p=''):
 o={}
 if isinstance(x,dict):
  for k,v in x.items():o.update(flat(v,p+'.'+k if p else k))
 else:o[p]=x
 return o
NEW={
'42566820':'Historical August 7 cognitive-aging study; TICS instrument acronym collision, not tic disorders.',
'42617303':'Historical August 11 cannabis systematic review/meta-analysis, November issue assignment. Secondary evidence, no independent participants. Preserve very-low-certainty and trivial-to-no TS benefit; no treatment recommendation.',
'42640249':'Historical August 25 cross-sectional TS imaging cohort already screened October 24. November issue assignment is not new publication. Tic-severity null preserved; no causal stable-trait or treatment-target inference.',
'42664664':'Historical August 28 cross-sectional pediatric protective-care medication study, November issue assignment. TS diagnosis associated with polypharmacy, not efficacy or causal safety. Not persistent-severe-adult validation.',
'42921162':'Historical October 23 possible PANDAS case series already screened October 26. Not new publication, controlled evidence or general TS mechanism. Citation metadata only; no individual narratives inspected.'}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--raw',required=True);ap.add_argument('--repo',required=True);ap.add_argument('--out',required=True);a=ap.parse_args();repo=pathlib.Path(a.repo);out=pathlib.Path(a.out);out.mkdir(parents=True,exist_ok=True);raw=json.loads(pathlib.Path(a.raw).read_text());priorpath=repo/'updates/2026-10-31/scan';priorreg={x['id']:x for x in map(json.loads,(priorpath/'registry-evidence.jsonl').read_text().splitlines())};priorpub={x['pmid']:x for x in map(json.loads,(priorpath/'pubmed-screening.jsonl').read_text().splitlines())}
 pub=raw['pubmed'].pop('date_type_correction_screen');assert {x['pmid'] for x in pub}<=set(priorpub)|set(NEW),'Unreviewed source set'
 for x in pub:
  pm=x['pmid'];matches=set()
  for term in [pm,x['identifiers'].get('doi')]:
   if term:
    rr=subprocess.run(['git','grep','-l','-F',term,BASE,'--','*.md','*.json','*.jsonl','*.tsv'],cwd=repo,text=True,capture_output=True);matches.update(t.split(':',1)[1] for t in rr.stdout.splitlines())
  decision=NEW.get(pm,priorpub.get(pm,{}).get('screening_decision'))
  x.update(historical_repository_reference_paths=sorted(matches),abstract_retained=False,new_to_repository_primary_record=pm=='42664664',new_publication_since_prior_cutoff=False,screening_decision=decision)
 (out/'pubmed-screening.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in pub))
 reg=[]
 for x in raw.pop('registry_records'):
  n=x['nctId'];assert n in priorreg,'Unreviewed registry ID';p=flat({k:priorreg[n].get(k) for k in ['status','design','hasResults']});b=flat({k:x[k] for k in ['status','design','hasResults']});changes=[{'field':k,'previous':p.get(k),'current':b.get(k)} for k in sorted(set(p)|set(b)) if p.get(k)!=b.get(k)]
  x.update(id=n,evidence_type='official registry metadata, not results',new_protocol=False,previous_day_comparison_available=True,selected_field_changes=changes,comparison_scope='Selected status/design/hasResults only; not full amendment history.')
  assert not changes,'Unreviewed registry change'
  x['interpretation']='Unchanged selected metadata from October 31; no posted results. Preserve prior protocol limitations and do not infer efficacy or safety from status.';reg.append(x)
 (out/'registry-evidence.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n'for x in reg))
 for p in raw['preprints']:
  idx=p.pop('version_index');p['index_path']=p['server']+'-preprint-index.tsv';assert not p['matches'],'Unreviewed preprint'
  with(out/p['index_path']).open('w')as f:w=csv.DictWriter(f,fieldnames=['doi','version','date'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(idx)
 requests=raw.pop('retrieval_requests');write(out/'request-log.json',requests);raw.update(request_log_path='request-log.json',scope='Public citation/protocol metadata and original summaries only; no participant rows, source abstracts, private narratives or unlicensed papers retained.');write(out/'search-log.json',raw)
 write(out/'summary.json',{'date':'2026-11-01','strict_prior_cutoff_utc':raw['prior_core_end_utc'],'core_started_utc':raw['started_utc'],'core_completed_utc':raw['completed_utc'],'pubmed_unique_records':len(pub),'pubmed_id_occurrences':raw['pubmed']['id_occurrences'],'pubmed_previous_day_overlap':raw['pubmed']['previous_overlap_count'],'new_to_previous_scan_records':len(raw['pubmed']['new_to_prior_scan_ids']),'new_to_repository_primary_records':1,'verified_new_primary_publications_since_prior_cutoff':0,'preprint_doi_versions':sum(x['unique_doi_versions']for x in raw['preprints']),'preprint_lexical_matches':0,'qualifying_preprints':0,'registry_update_window_unique_ids':sorted(set(i for q in raw['registry'] for i in q.get('response',{}).get('nct_ids',[]))),'new_registry_protocols':[],'new_posted_trial_results':0,'new_retractions':0,'api_request_errors':sum('error'in x for x in requests),'decision':'No verified new-window first publication, qualifying preprint or posted trial result. November issue assignments return older papers; selected registry fields unchanged.'})
if __name__=='__main__':main()
