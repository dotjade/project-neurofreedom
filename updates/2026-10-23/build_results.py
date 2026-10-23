#!/usr/bin/env python3
"""Normalize saved live metadata with reviewed, date-aware decisions. New IDs require review."""
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
 new={'42902960','42903303'};historic={'11527335','15970726','17453897','18058387','18280023','19395047','19698938','24236274','24795782','24840790','25161066','39985332','40265762','40304057','40353708'};known=new|historic|{'39947542','42527169'}
 pub=raw['pubmed'].pop('date_type_correction_screen');assert {x['pmid'] for x in pub}<=known,'New IDs need original review'
 files=[p for p in repo.rglob('*') if p.is_file() and '.git' not in p.parts and p.suffix in ('.md','.json','.jsonl','.tsv')];texts={str(p.relative_to(repo)):p.read_text(errors='replace') for p in files}
 for x in pub:
  pm=x['pmid'];doi=x['identifiers'].get('doi');matches=sorted(p for p,t in texts.items() if re.search(r'(?<!\d)'+pm+r'(?!\d)',t) or (doi and doi in t));x.update(historical_repository_reference_paths=matches,abstract_retained=False,new_to_repository_primary_record=pm in new,new_publication_since_prior_cutoff=False)
  if pm in new:
   decision='Newly indexed after prior cutoff; earlier electronic publication. Include original primary-study extraction, not a new trial result.';typ='newly_indexed_cross_sectional_primary'
  elif pm=='39947542':decision='Known February 2025 retracted preclinical paper remains excluded from positive mechanism/efficacy evidence. October 21 metadata revision is not reinstatement.';typ='historical_retracted_preclinical'
  elif pm=='42527169':decision='Known July 29, 2026 electronic retraction notice with October issue date. No new notice; linked RetractionOf unchanged.';typ='historical_retraction_notice'
  elif pm=='40304057':decision='Historical 2025 case report; metadata revision only. Individual case narrative was not extracted or retained.';typ='historical_case_report_metadata'
  elif pm=='40353708':decision='May 2025 pediatric ecopipam extension, not a new-window result. PubMed trial-type labels do not establish this report is a new independent randomization.';typ='historical_trial_report_metadata'
  elif pm in {'24795782','40265762'}:decision='Historical conceptual/review article; not a new independent primary tic outcome.';typ='historical_secondary_metadata'
  else:decision='Historical 2001–2025 publication resurfacing through metadata revision. Not a new-window result; no full-method efficacy claim added.';typ='historical_publication_metadata'
  x.update(evidence_class=typ,screening_decision=decision)
 (out/'pubmed-screening.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in pub))
 prior={x['pmid']:x for x in base['pubmed']};write(out/'integrity-recheck.json',[{'id':x['pmid'],'source_url':x['source_url'],'compared_to':'updates/2026-10-22/pubmed-screening.jsonl','selected_metadata_changes':{k:{'previous':prior[x['pmid']].get(k),'current':x.get(k)} for k in ['types','corrections','DateRevised'] if prior[x['pmid']].get(k)!=x.get(k)},'new_notice':False,'interpretation':'Known retraction and reciprocal notice remain; selected metadata unchanged from prior scan.'} for x in pub if x['pmid'] in {'39947542','42527169'}])
 prior={x['id']:{k:x[k] for k in ['status','design','hasResults']} for x in base['registry']};reg=[]
 interpretations={'NCT07137442':'Estimated start October 26 to October 27; posting October 21 to October 22; submission October 20 to October 21. Recruiting, observational, planned enrollment 75 and no-results flag unchanged. Not evidence of actual recruitment or efficacy.','NCT05158439':'Withdrawn for inability to recruit, actual enrollment zero, no results. Negative feasibility, not negative efficacy or evidence of cell administration.','NCT07093541':'Expanded access remains temporarily unavailable without results; no new suspension or cause inferred.','NCT06194305':'Pediatric CBIT study remains recruiting without results; selected metadata unchanged.'}
 for x in raw.pop('registry_records'):
  n=x['nctId'];assert n in prior and n in interpretations,'New registry needs review';b=flat({k:x[k] for k in ['status','design','hasResults']});p=flat(prior[n]);changes=[{'field':k,'previous':p.get(k),'current':b.get(k)} for k in sorted(set(p)|set(b)) if p.get(k)!=b.get(k)];x.update(id=n,evidence_class='registry_protocol_update_without_results' if changes else 'registry_status_control',selected_field_changes=changes,comparison_scope='Selected status/design/hasResults only, not full amendment history.',interpretation=interpretations[n]);reg.append(x)
 (out/'registry-evidence.jsonl').write_text(''.join(json.dumps(x,separators=(',',':'))+'\n' for x in reg))
 for p in raw['preprints']:
  idx=p.pop('version_index');p['index_path']=p['server']+'-preprint-index.tsv'
  with (out/p['index_path']).open('w') as f:w=csv.DictWriter(f,fieldnames=['doi','version','date'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(idx)
  for m in p['matches']:
   d={'10.64898/2026.06.25.734531':'TICs means thermodynamically infeasible cycles in prostate-cancer modeling.','10.64898/2026.10.17.759814':'TIC means Taxonomy-Informed Clustering in 16S amplicon methods.'};assert m['doi'] in d,'New lexical hit needs review';m.update(screening_decision='Excluded lexical false positive: '+d[m['doi']],qualifying_tic_result=False)
 requests=raw.pop('retrieval_requests');write(out/'request-log.json',requests);raw.update(request_log_path='request-log.json',scope='Selected public metadata. No full abstracts/papers, participant measurements, contacts, private narratives, or raw physiological signals retained.');write(out/'search-log.json',raw)
 summary={'date':'2026-10-23','strict_prior_cutoff_utc':base['cutoff_utc'],'core_started_utc':raw['started_utc'],'core_completed_utc':raw['completed_utc'],'pubmed_unique_records':len(pub),'pubmed_id_occurrences':raw['pubmed']['id_occurrences'],'pubmed_previous_day_overlap':raw['pubmed']['previous_overlap_count'],'newly_indexed_primary_records':2,'new_to_repository_primary_records':2,'new_primary_publications_since_prior_cutoff':0,'historical_metadata_records':17,'preprint_doi_versions':sum(x['unique_doi_versions'] for x in raw['preprints']),'preprint_lexical_matches':sum(len(x['matches']) for x in raw['preprints']),'qualifying_preprints':0,'registry_update_window_unique_ids':sorted(set(i for q in raw['registry'] for i in q['response']['nct_ids'])),'new_posted_trial_results':0,'new_retractions':0,'api_request_errors':sum('error' in x for x in requests),'decision':'Two newly indexed cross-sectional primary studies extend adult-burden/comorbidity evidence; neither establishes a treatment effect, prospective prediction or population remission. Registry update remains a planned-date change without results.'};write(out/'summary.json',summary);print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
