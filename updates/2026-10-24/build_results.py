#!/usr/bin/env python3
"""Normalize reviewed Oct24 public metadata. Refuse unknown identifiers for manual review."""
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
 known={'11527335','15970726','17453897','18058387','18280023','19395047','19698938','24236274','24795782','24840790','25161066','40265962','40326633','42550254','42640249','42902960','42903303','42908833','42910671'}
 pub=raw['pubmed'].pop('date_type_correction_screen');assert {x['pmid'] for x in pub}<=known,'New IDs need original review'
 files=[p for p in repo.rglob('*')if p.is_file()and '.git' not in p.parts and p.suffix in('.md','.json','.jsonl','.tsv')];texts={str(p.relative_to(repo)):p.read_text(errors='replace')for p in files}
 for x in pub:
  pm=x['pmid'];doi=x['identifiers'].get('doi');matches=sorted(p for p,t in texts.items()if re.search(r'(?<!\d)'+pm+r'(?!\d)',t)or(doi and doi in t));x.update(historical_repository_reference_paths=matches,abstract_retained=False,new_to_repository_primary_record=pm=='42908833',new_publication_since_prior_cutoff=None if pm=='42910671' else False)
  if pm=='42908833':decision='Newly indexed October 23 after prior observed scan; published October 7. Include original adjacent primary-methods extraction. No consensus-positive tics in external cohort, so no tic-detection sensitivity validation.';typ='newly_indexed_primary_adjacent_methods'
  elif pm=='42910671':decision='Newly indexed October 23 case report; only title, identifiers, dates and publication types retained. No individual case narrative reviewed or extracted. Exact electronic publication date unavailable in PubMed metadata; indexing is not publication.';typ='newly_indexed_case_report_metadata_only'
  elif pm in {'42902960','42903303'}:decision='Already extracted October 23; historical overlap, not a newly added study. Retain original age/comorbidity, retrospective timing and model-denominator caveats.';typ='prior_day_primary_overlap'
  elif pm=='40265962':decision='April 2025 primary laryngeal-dystonia report, not a tic-disorder result; revised metadata only. No alcohol intervention recommendation or cross-disorder efficacy inference.';typ='historical_non_tic_primary_metadata'
  elif pm in {'40326633','42550254','24795782'}:decision='Historical secondary/conceptual report; not a new independent primary tic outcome.';typ='historical_secondary_metadata'
  elif pm=='42640249':decision='August 25 electronic publication with November issue assignment; October 23 metadata revision is not new publication. Cross-sectional MRI abstract does not establish a stable causal trait or therapeutic target. Prior repository discovery reference exists; no new extraction added.';typ='historical_primary_metadata_revision'
  else:decision='Historical 2001–2014 publication resurfacing through metadata revision. Not a new-window publication; no full-method efficacy claim added.';typ='historical_publication_metadata'
  x.update(evidence_class=typ,screening_decision=decision)
 (out/'pubmed-screening.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n'for x in pub))
 prior={x['id']:{k:x[k]for k in ['status','design','hasResults']}for x in base['registry']};reg=[]
 interpretations={'NCT07137442':'Estimated start October 27 to October 28; posting October 22 to October 23; submission October 21 to October 22. Recruiting, observational, planned enrollment 75 and no-results flag unchanged. Not evidence of actual recruitment or efficacy.','NCT05158439':'Withdrawn for inability to recruit, actual enrollment zero, no results. Negative feasibility, not negative efficacy or evidence of cell administration.','NCT07093541':'Expanded access remains temporarily unavailable without results; no new suspension or cause inferred.','NCT06194305':'Pediatric CBIT study remains recruiting without results; selected metadata unchanged.'}
 for x in raw.pop('registry_records'):
  n=x['nctId'];assert n in prior and n in interpretations,'New registry needs review';b=flat({k:x[k]for k in ['status','design','hasResults']});p=flat(prior[n]);changes=[{'field':k,'previous':p.get(k),'current':b.get(k)}for k in sorted(set(p)|set(b))if p.get(k)!=b.get(k)];x.update(id=n,evidence_class='registry_protocol_update_without_results'if changes else 'registry_status_control',selected_field_changes=changes,comparison_scope='Selected status/design/hasResults only, not full amendment history.',interpretation=interpretations[n]);reg.append(x)
 (out/'registry-evidence.jsonl').write_text(''.join(json.dumps(x,separators=(',',':'))+'\n'for x in reg))
 for p in raw['preprints']:
  idx=p.pop('version_index');p['index_path']=p['server']+'-preprint-index.tsv'
  with(out/p['index_path']).open('w')as f:w=csv.DictWriter(f,fieldnames=['doi','version','date'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(idx)
  for m in p['matches']:
   assert m['doi']=='10.64898/2026.10.17.759814','New lexical hit needs review';m.update(screening_decision='Excluded lexical false positive: TIC means Taxonomy-Informed Clustering in 16S amplicon methods.',qualifying_tic_result=False)
 requests=raw.pop('retrieval_requests');write(out/'request-log.json',requests);raw.update(request_log_path='request-log.json',scope='Selected public metadata and original summaries. No source abstracts/papers, participant measurement rows, contacts, private narratives, or raw physiological signals retained.');write(out/'search-log.json',raw)
 s={'date':'2026-10-24','strict_prior_cutoff_utc':base['cutoff_utc'],'core_started_utc':raw['started_utc'],'core_completed_utc':raw['completed_utc'],'pubmed_unique_records':len(pub),'pubmed_id_occurrences':raw['pubmed']['id_occurrences'],'pubmed_previous_day_overlap':raw['pubmed']['previous_overlap_count'],'newly_indexed_records':2,'newly_indexed_primary_records_added':1,'newly_indexed_case_reports_metadata_only':1,'new_to_repository_primary_records':1,'verified_new_primary_publications_since_prior_cutoff':0,'unknown_exact_publication_date_records':1,'historical_or_previous_scan_metadata_records':17,'preprint_doi_versions':sum(x['unique_doi_versions']for x in raw['preprints']),'preprint_lexical_matches':sum(len(x['matches'])for x in raw['preprints']),'qualifying_preprints':0,'registry_update_window_unique_ids':sorted(set(i for q in raw['registry']for i in q.get('response',{}).get('nct_ids',[]))),'new_posted_trial_results':0,'new_retractions':0,'api_request_errors':sum('error'in x for x in requests),'decision':'One newly indexed October 7 adjacent methods paper cannot validate tic-detection sensitivity because no external consensus-positive tics were present. A newly indexed case report is metadata-only. No new qualifying preprint or posted trial result verified.'};write(out/'summary.json',s);print(json.dumps(s,indent=2))
if __name__=='__main__':main()
