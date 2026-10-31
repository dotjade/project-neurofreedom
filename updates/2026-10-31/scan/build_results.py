#!/usr/bin/env python3
"""Normalize reviewed October 31 public citation metadata; reject unreviewed identifiers."""
import argparse,csv,json,pathlib,subprocess,hashlib,datetime
BASE='8b9fd54ff445e8f5e74ffffa48f49a80ad36990b'
def write(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def flat(x,p=''):
 o={}
 if isinstance(x,dict):
  for k,v in x.items():o.update(flat(v,p+'.'+k if p else k))
 else:o[p]=x
 return o
DECISIONS={
'32560953':'Historical 2020 pediatric trichotillomania study, not new tic evidence.',
'33944988':'Historical 2021 EMTICS presentation study. Cross-sectional age differences are not individual trajectories.',
'33959852':'Historical 2021 oral-orthotic pilot. Initial tic difference was not reproduced at follow-up; no recommendation.',
'33966152':'Historical 2021 pediatric prevalence/comorbidity study, not new publication.',
'34817664':'Historical 2021 clinician consensus definition, not treatment-effect evidence. Linked 2025 erratum 40111559 is historical, not new notice.',
'34854986':'Historical 2021 pediatric stress/emotion-regulation association. No causality or adult extrapolation.',
'35567613':'Historical 2022 dystonic-tic characterization. No videos or individual narratives inspected.',
'35859051':'Historical 2022 cannabis systematic review, not new independent treatment results.',
'36723683':'Historical 2023 oromandibular-tic clinical series; abstract only, no patient videos or narratives inspected.',
'37442132':'Historical 2023 mouse pain/analgesia study, not primary human tic evidence.',
'37517703':'Historical 2023 lifespan TMS review, not new trial evidence.',
'37776102':'Historical 2023 Slitrk1 mouse perturbation study. Animal stereotypies do not establish human treatment benefit.',
'41263644':'Historical 2025 tardive-dystonia letter. Citation metadata only; no patient descriptions retained.',
'41618542':'Historical biographical tribute, not primary clinical evidence.',
'41927332':'MRI time-intensity curves acronym collision, not tic disorders.',
'42412229':'Prior July 2026 developmental cohort paper; metadata revision is not new publication.',
'42467078':'Prior July 2026 EMTICS medication-use report, not randomized effects.',
'42525239':'Historical July 2026 care-pathway letter, not independent efficacy evidence.',
'42856611':'October 1 TMS/CBIT preprint already extracted. Preserve preprint status and do not duplicate.',
'42934522':'Prior July 30 GP-TiCS qualitative paper; not new primary evidence. No interview narratives retained.',
'42952789':'Prior October 14 pediatric immune/vitamin paper already extracted; preserve vitamin multiplicity nulls.',
'42956657':'Newly retrieved October 20 postmortem mixed-diagnosis histamine transcriptomic pilot. Small HRH3 group association with weak Bayesian support, other corrected genes null. Not TS-specific causality or treatment target.',
'42956658':'Newly retrieved October 23 pediatric EF/comorbidity systematic review. Secondary narrative synthesis, not independent participant data or adult validation.',
'42957926':'Telephone cognitive-status TICS acronym collision in older-adult fracture study, not tic disorders.'}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--raw',required=True);ap.add_argument('--repo',required=True);ap.add_argument('--out',required=True);a=ap.parse_args();repo=pathlib.Path(a.repo);out=pathlib.Path(a.out);out.mkdir(parents=True,exist_ok=True);raw=json.loads(pathlib.Path(a.raw).read_text());priorpath=repo/'updates/2026-10-30/scan';priorreg={x['id']:x for x in map(json.loads,(priorpath/'registry-evidence.jsonl').read_text().splitlines())}
 pub=raw['pubmed'].pop('date_type_correction_screen');assert set(DECISIONS)=={x['pmid'] for x in pub},'Unreviewed source set'
 for x in pub:
  pm=x['pmid'];matches=set()
  for term in [pm,x['identifiers'].get('doi')]:
   if term:
    rr=subprocess.run(['git','grep','-l','-F',term,BASE,'--','*.md','*.json','*.jsonl','*.tsv'],cwd=repo,text=True,capture_output=True);matches.update(t.split(':',1)[1] for t in rr.stdout.splitlines())
  x.update(historical_repository_reference_paths=sorted(matches),abstract_retained=False,new_to_repository_primary_record=pm=='42956657',new_publication_since_prior_cutoff=False,screening_decision=DECISIONS[pm])
 (out/'pubmed-screening.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in pub))
 reg=[]
 for x in raw.pop('registry_records'):
  n=x['nctId'];assert n in {'NCT05158439','NCT06194305','NCT07093541','NCT07137442','NCT07905898'};p=flat({k:priorreg.get(n,{}).get(k) for k in ['status','design','hasResults']});b=flat({k:x[k] for k in ['status','design','hasResults']});changes=[{'field':k,'previous':p.get(k),'current':b.get(k)} for k in sorted(set(p)|set(b)) if p.get(k)!=b.get(k)]
  if n in priorreg and n!='NCT07137442':assert not changes,'Unreviewed change'
  x.update(id=n,evidence_type='official registry metadata, not results',new_protocol=n=='NCT07905898',previous_day_comparison_available=n in priorreg,selected_field_changes=changes if n in priorreg else [],comparison_scope='Selected status/design/hasResults only; not full amendment history.')
  x['interpretation']={'NCT05158439':'Unchanged withdrawn for inability to recruit, actual enrollment zero. Negative feasibility, not negative efficacy.','NCT06194305':'Unchanged pediatric CBIT protocol, recruiting, no results.','NCT07093541':'Unchanged expanded access no longer available; no reason or safety cause inferred.','NCT07137442':'October 30 posting moves estimated start from November 3 to November 4. Planned date, not observed recruitment or efficacy.','NCT07905898':'First posted October 30, not yet recruiting. Adolescent resilience/supportive-care adaptation and feasibility protocol, no results. Top-line 95 enrollment versus detailed 85 adolescent participants remains an unresolved denominator distinction; do not call all 95 randomized.'}[n];reg.append(x)
 (out/'registry-evidence.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n'for x in reg))
 for p in raw['preprints']:
  idx=p.pop('version_index');p['index_path']=p['server']+'-preprint-index.tsv';assert not p['matches'],'Unreviewed preprint'
  with(out/p['index_path']).open('w')as f:w=csv.DictWriter(f,fieldnames=['doi','version','date'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(idx)
 requests=raw.pop('retrieval_requests');write(out/'request-log.json',requests);raw.update(request_log_path='request-log.json',scope='Public citation/protocol metadata and original summaries only; no participant rows, source abstracts, private narratives or unlicensed papers retained.');write(out/'search-log.json',raw)
 write(out/'summary.json',{'date':'2026-10-31','strict_prior_cutoff_utc':raw['prior_core_end_utc'],'core_started_utc':raw['started_utc'],'core_completed_utc':raw['completed_utc'],'pubmed_unique_records':len(pub),'pubmed_id_occurrences':raw['pubmed']['id_occurrences'],'pubmed_previous_day_overlap':raw['pubmed']['previous_overlap_count'],'new_to_previous_scan_records':len(raw['pubmed']['new_to_prior_scan_ids']),'new_to_repository_primary_records':1,'verified_new_primary_publications_since_prior_cutoff':0,'preprint_doi_versions':sum(x['unique_doi_versions']for x in raw['preprints']),'preprint_lexical_matches':0,'qualifying_preprints':0,'registry_update_window_unique_ids':sorted(set(i for q in raw['registry'] for i in q.get('response',{}).get('nct_ids',[]))),'new_registry_protocols':['NCT07905898'],'new_posted_trial_results':0,'new_retractions':0,'api_request_errors':sum('error'in x for x in requests),'decision':'Older October 20 mixed-diagnosis histamine pilot newly retrieved; no new-window first publication or clinical result. New adolescent resilience feasibility protocol is not efficacy evidence. One estimated registry start shifted one day.'})
if __name__=='__main__':main()
