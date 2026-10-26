#!/usr/bin/env python3
"""Normalize reviewed Oct26 public metadata. Refuse new unreviewed identifiers."""
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
 known={'40439027','40485368','40736219','42189206','42550254','42640249','42903303','42919181','42921162','42925937'}
 pub=raw['pubmed'].pop('date_type_correction_screen');assert {x['pmid'] for x in pub}==known,'Identifiers need review'
 decisions={
 '40439027':('historical_other_condition_primary_metadata_revision','May 2025 cervical-dystonia treatment paper, not new tic-treatment evidence.'),
 '40485368':('historical_primary_metadata_revision','June 2025 claims-based chronic-pain paper already cited in project pain audit provenance; October 24 revision is not a new publication.'),
 '40736219':('historical_other_condition_secondary_metadata_revision','July 2025 Parkinson hospital-care systematic review, not new primary tic evidence.'),
 '42189206':('historical_primary_metadata_revision','May 2026 pediatric tic/functional-tic comparison; October 24 revision is not new research. No family-level descriptions extracted.'),
 '42550254':('historical_secondary_metadata','August review, not independent primary outcome evidence.'),
 '42640249':('historical_primary_metadata_revision','August publication, November issue assignment; not new publication or treatment evidence.'),
 '42903303':('prior_primary_overlap','Previously extracted retrospective adult persistence paper; no duplicate addition.'),
 '42919181':('prior_primary_overlap','Previously extracted CHD/Tourette study; preserve null overall estimate and table/prose contradiction. Revision alone is not new research.'),
 '42921162':('case_series_citation_metadata_only','October 23 case series newly surfaced. Citation metadata only; no identifiable clinical narratives retained. Not controlled Tourette treatment evidence.'),
 '42925937':('older_preclinical_primary_new_to_scan','October 24 publication/Entrez entry precede prior cutoff. Newly encountered rat-model paper, not verified new-window publication. PubMed history October 25 03:36 has unverified timezone; indexing after prior cutoff is not asserted. Abstract-only preclinical extraction cannot establish human efficacy or C1qa causality.')}
 for x in pub:
  pm=x['pmid'];doi=x['identifiers'].get('doi');matches=set()
  for term in [pm,doi]:
   if term:
    r=subprocess.run(['git','grep','-l','-F',term,'1dafa0fdb06d4f08ba13f281bc866c3b5f58b170','--','*.md','*.json','*.jsonl','*.tsv'],cwd=repo,text=True,capture_output=True)
    matches.update(t.split(':',1)[1] for t in r.stdout.splitlines())
  typ,decision=decisions[pm]
  x.update(historical_repository_reference_paths=sorted(matches),abstract_retained=False,new_to_repository_primary_record=pm=='42925937',new_publication_since_prior_cutoff=False,evidence_class=typ,screening_decision=decision)
 (out/'pubmed-screening.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n'for x in pub))
 prior={x['id']:{k:x[k]for k in ['status','design','hasResults']}for x in base['registry']};reg=[]
 interpretations={'NCT07137442':'Selected fields unchanged: estimated start October 28, recruiting observational study, planned 75 and no results. Planned dates do not establish actual recruitment or efficacy.','NCT05158439':'Unchanged withdrawal for inability to recruit, actual enrollment zero, no results. Negative feasibility, not negative efficacy.','NCT07093541':'Expanded access remains temporarily unavailable without results; no new cause inferred.','NCT06194305':'Pediatric CBIT study remains recruiting without results; selected metadata unchanged.'}
 for x in raw.pop('registry_records'):
  n=x['nctId'];assert n in prior and n in interpretations,'New registry needs review';b=flat({k:x[k]for k in ['status','design','hasResults']});p=flat(prior[n]);changes=[{'field':k,'previous':p.get(k),'current':b.get(k)}for k in sorted(set(p)|set(b))if p.get(k)!=b.get(k)];assert not changes,'Changes need review';x.update(id=n,evidence_class='registry_status_control',selected_field_changes=changes,comparison_scope='Selected status/design/hasResults, not full amendment history.',interpretation=interpretations[n]);reg.append(x)
 (out/'registry-evidence.jsonl').write_text(''.join(json.dumps(x,separators=(',',':'))+'\n'for x in reg))
 for p in raw['preprints']:
  idx=p.pop('version_index');p['index_path']=p['server']+'-preprint-index.tsv'
  with(out/p['index_path']).open('w')as f:w=csv.DictWriter(f,fieldnames=['doi','version','date'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(idx)
  assert not p['matches'],'New lexical hit needs review'
 requests=raw.pop('retrieval_requests');write(out/'request-log.json',requests);raw.update(request_log_path='request-log.json',scope='Selected public metadata and original summaries only. No source abstracts/full papers, participant rows, contacts or private narratives retained.');write(out/'search-log.json',raw)
 s={'date':'2026-10-26','strict_prior_cutoff_utc':base['cutoff_utc'],'core_started_utc':raw['started_utc'],'core_completed_utc':raw['completed_utc'],'pubmed_unique_records':len(pub),'pubmed_id_occurrences':raw['pubmed']['id_occurrences'],'pubmed_previous_day_overlap':raw['pubmed']['previous_overlap_count'],'new_to_previous_scan_records':6,'new_to_repository_primary_records':1,'verified_new_primary_publications_since_prior_cutoff':0,'verified_newly_entered_pubmed_since_prior_cutoff':0,'unknown_exact_publication_date_records':0,'preprint_doi_versions':sum(x['unique_doi_versions']for x in raw['preprints']),'preprint_lexical_matches':0,'qualifying_preprints':0,'registry_update_window_unique_ids':sorted(set(i for q in raw['registry']for i in q.get('response',{}).get('nct_ids',[]))),'new_posted_trial_results':0,'new_retractions':0,'api_request_errors':sum('error'in x for x in requests),'decision':'One October 24 preclinical paper newly encountered is added, not a verified new-window publication. No qualifying preprint or new posted trial result verified; indexing timezone and retrieval lag remain uncertain.'};write(out/'summary.json',s);print(json.dumps(s,indent=2))
if __name__=='__main__':main()
