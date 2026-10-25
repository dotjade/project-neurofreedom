#!/usr/bin/env python3
"""Normalize reviewed Oct25 public metadata. Refuse new unreviewed identifiers."""
import argparse,csv,json,pathlib,re
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
 known={'42550254','42640249','42790390','42902960','42903303','42908833','42910671','42919181'}
 pub=raw['pubmed'].pop('date_type_correction_screen');assert {x['pmid'] for x in pub}==known,'Identifiers need review'
 files=[p for p in repo.rglob('*')if p.is_file()and '.git'not in p.parts and p.suffix in('.md','.json','.jsonl','.tsv')];texts={str(p.relative_to(repo)):p.read_text(errors='replace')for p in files}
 for x in pub:
  pm=x['pmid'];doi=x['identifiers'].get('doi');matches=sorted(p for p,t in texts.items()if re.search(r'(?<!\d)'+pm+r'(?!\d)',t)or(doi and doi in t));x.update(historical_repository_reference_paths=matches,abstract_retained=False,new_to_repository_primary_record=pm=='42919181',new_publication_since_prior_cutoff=None if pm=='42910671'else False)
  if pm=='42919181':decision='New to this repository and overlap scan, but published July 25 and PubMed entry dated October 23 before prior cutoff. Absence yesterday does not establish indexing after cutoff. Original primary observational extraction retains null overall CHD-Tourette association and exploratory severity limits.';typ='older_primary_new_to_scan_not_new_window_publication'
  elif pm=='42910671':decision='Prior metadata-only case report; no case narrative reviewed or retained. Exact publication date remains unknown.';typ='prior_case_report_metadata_only'
  elif pm in {'42902960','42903303','42908833'}:decision='Already extracted primary evidence, not duplicate addition. Preserve mixed-age measurement, retrospective timing and absent external tic-positive validation limits.';typ='prior_primary_overlap'
  elif pm=='42790390':decision='July 28 electronic publication, September 25 entry; October 23 revision is not new research. Adult OCD quality-of-life cross-validation is not a tic-specific prospective model. Historical adjacent primary metadata; no new extraction.';typ='historical_adjacent_primary_metadata_revision'
  elif pm=='42550254':decision='Historical secondary review, not a new independent primary outcome.';typ='historical_secondary_metadata'
  else:decision='August 25 electronic publication, November issue assignment, October 23 revision. Prior scan overlap, not new publication or independent treatment evidence.';typ='historical_primary_metadata_revision'
  x.update(evidence_class=typ,screening_decision=decision)
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
 s={'date':'2026-10-25','strict_prior_cutoff_utc':base['cutoff_utc'],'core_started_utc':raw['started_utc'],'core_completed_utc':raw['completed_utc'],'pubmed_unique_records':len(pub),'pubmed_id_occurrences':raw['pubmed']['id_occurrences'],'pubmed_previous_day_overlap':raw['pubmed']['previous_overlap_count'],'new_to_previous_scan_records':2,'new_to_repository_primary_records':1,'verified_new_primary_publications_since_prior_cutoff':0,'verified_newly_entered_pubmed_since_prior_cutoff':0,'unknown_exact_publication_date_records':1,'preprint_doi_versions':sum(x['unique_doi_versions']for x in raw['preprints']),'preprint_lexical_matches':0,'qualifying_preprints':0,'registry_update_window_unique_ids':sorted(set(i for q in raw['registry']for i in q.get('response',{}).get('nct_ids',[]))),'new_posted_trial_results':0,'new_retractions':0,'api_request_errors':sum('error'in x for x in requests),'decision':'One older primary study newly encountered in overlap search is added, retaining null overall CHD-Tourette association. No qualifying new-window publication, preprint or trial result verified.'};write(out/'summary.json',s);print(json.dumps(s,indent=2))
if __name__=='__main__':main()
