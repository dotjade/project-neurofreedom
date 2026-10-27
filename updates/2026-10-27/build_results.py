#!/usr/bin/env python3
"""Normalize reviewed Oct27 public metadata. Refuse new unreviewed identifiers."""
import argparse,csv,json,pathlib,re,subprocess
from prepare_baseline import build

def write(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def flat(x,p=''):
 o={}
 if isinstance(x,dict):
  for k,v in x.items():o.update(flat(v,p+'.'+k if p else k))
 else:o[p]=x
 return o

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--raw',required=True);ap.add_argument('--repo',required=True);ap.add_argument('--out',required=True);a=ap.parse_args();repo=pathlib.Path(a.repo);out=pathlib.Path(a.out);out.mkdir(exist_ok=True,parents=True);raw=json.loads(pathlib.Path(a.raw).read_text());base=build(repo)
 known={'41059647','41392858','42189206','42391199','42412229','42467078','42525239','42910671','42919181','42921162','42925937'}
 pub=raw['pubmed'].pop('date_type_correction_screen');assert {x['pmid'] for x in pub}==known,'Identifiers need review'
 decisions={
 '41059647':('historical_primary_metadata_revision','October 2025 functional tic-like behavior follow-up, not a new primary Tourette publication. No identifying narratives retained.'),
 '41392858':('historical_secondary_metadata_revision','December 2025 trial-representation meta-analysis, not new independent trial results.'),
 '42189206':('historical_primary_metadata_revision','May 2026 pediatric tic/functional-tic comparison; revision is not new research. No family-level descriptions extracted.'),
 '42391199':('historical_primary_metadata_revision','July 2026 rage-attacks study; October revision is not a new publication. Burden remains relevant without equating rage and tics.'),
 '42412229':('historical_primary_metadata_revision','July 2026 developmental cohort study, not new-window evidence or adult-specific prediction.'),
 '42467078':('historical_primary_metadata_revision','July 2026 pediatric EMTICS treatment-pattern report; medication-use associations are not randomized treatment effects.'),
 '42525239':('historical_letter_metadata_revision','July 2026 care-pathway letter, not new controlled treatment evidence.'),
 '42910671':('prior_case_report_metadata_only','Prior case report; exact publication date unknown. Citation metadata only, no narrative retained.'),
 '42919181':('prior_primary_overlap','Previously extracted CHD/Tourette study. Null overall estimate and table/prose contradiction retained; revision is not new research.'),
 '42921162':('case_series_citation_metadata_only','October 23 case series already screened. Citation metadata only; not controlled Tourette treatment evidence.'),
 '42925937':('prior_preclinical_primary_overlap','October 24 rat-model paper already extracted. Preserve unresolved causality, abstract-only access and absent human efficacy/safety evidence.')}
 for x in pub:
  pm=x['pmid'];doi=x['identifiers'].get('doi');matches=set()
  for term in [pm,doi]:
   if term:
    r=subprocess.run(['git','grep','-l','-F',term,'10689d9b7194f8600dd2d9b01137975229cd036b','--','*.md','*.json','*.jsonl','*.tsv'],cwd=repo,text=True,capture_output=True)
    matches.update(t.split(':',1)[1] for t in r.stdout.splitlines())
  typ,decision=decisions[pm]
  x.update(historical_repository_reference_paths=sorted(matches),abstract_retained=False,new_to_repository_primary_record=False,new_publication_since_prior_cutoff=None if pm=='42910671' else False,evidence_class=typ,screening_decision=decision)
 (out/'pubmed-screening.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n'for x in pub))
 prior={x['id']:{k:x[k]for k in ['status','design','hasResults']}for x in base['registry']};reg=[]
 interpretations={'NCT01019343':'October 26 metadata posting for a historical mixed-movement-disorder basic-science study completed in 2020, actual enrollment 1273 across diagnoses, no results. This is not a new completed trial or 1273 Tourette participants.','NCT07137442':'Estimated start changed October 28 to October 29, with October 26 posting; planned 75 and no results unchanged. Planned dates do not establish actual recruitment or efficacy.','NCT05158439':'Unchanged withdrawal for inability to recruit, actual enrollment zero, no results. Negative feasibility, not negative efficacy.','NCT07093541':'Expanded access remains temporarily unavailable without results; no new cause inferred.','NCT06194305':'Pediatric CBIT study remains recruiting without results; selected metadata unchanged.'}
 for x in raw.pop('registry_records'):
  n=x['nctId'];assert n in interpretations,'New registry needs review';b=flat({k:x[k]for k in ['status','design','hasResults']});p=flat(prior.get(n,{}));changes=[{'field':k,'previous':p.get(k),'current':b.get(k)}for k in sorted(set(p)|set(b))if p.get(k)!=b.get(k)];assert (n in ['NCT07137442','NCT01019343']) or not changes,'Changes need review';x.update(id=n,evidence_class='registry_status_control',previous_day_comparison_available=n in prior,selected_field_changes=changes if n in prior else [],comparison_scope='Selected status/design/hasResults versus previous day only; new-to-day record lacks a previous-day snapshot. Not full amendment history.',interpretation=interpretations[n]);reg.append(x)
 (out/'registry-evidence.jsonl').write_text(''.join(json.dumps(x,separators=(',',':'))+'\n'for x in reg))
 for p in raw['preprints']:
  idx=p.pop('version_index');p['index_path']=p['server']+'-preprint-index.tsv'
  with(out/p['index_path']).open('w')as f:w=csv.DictWriter(f,fieldnames=['doi','version','date'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(idx)
  assert not p['matches'],'New lexical hit needs review'
 requests=raw.pop('retrieval_requests');write(out/'request-log.json',requests);raw.update(request_log_path='request-log.json',scope='Selected public metadata and original summaries only. No source abstracts/full papers, participant rows, contacts or private narratives retained.');write(out/'search-log.json',raw)
 s={'date':'2026-10-27','strict_prior_cutoff_utc':base['cutoff_utc'],'core_started_utc':raw['started_utc'],'core_completed_utc':raw['completed_utc'],'pubmed_unique_records':len(pub),'pubmed_id_occurrences':raw['pubmed']['id_occurrences'],'pubmed_previous_day_overlap':raw['pubmed']['previous_overlap_count'],'new_to_previous_scan_records':7,'new_to_repository_primary_records':1,'verified_new_primary_publications_since_prior_cutoff':0,'verified_newly_entered_pubmed_since_prior_cutoff':0,'unknown_exact_publication_date_records':1,'preprint_doi_versions':sum(x['unique_doi_versions']for x in raw['preprints']),'preprint_lexical_matches':0,'qualifying_preprints':0,'registry_update_window_unique_ids':sorted(set(i for q in raw['registry']for i in q.get('response',{}).get('nct_ids',[]))),'new_posted_trial_results':0,'new_retractions':0,'api_request_errors':sum('error'in x for x in requests),'decision':'One September genetics paper newly found by supplementary discovery is added, not a new-window publication. No qualifying preprint or new posted trial result verified. Two registry postings are metadata updates, not clinical results.'};write(out/'summary.json',s);print(json.dumps(s,indent=2))
if __name__=='__main__':main()
