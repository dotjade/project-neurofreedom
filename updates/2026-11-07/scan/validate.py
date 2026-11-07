"""Deterministic artifact consistency checks, not independent clinical review."""
import json,pathlib,re,hashlib,datetime
P=pathlib.Path(__file__).parent
J=lambda f:json.loads((P/f).read_text())
L=lambda f:[json.loads(x) for x in (P/f).read_text().splitlines() if x.strip()]
s=J('search-log.json');sm=J('summary.json');a=J('reported-arithmetic.json');p=L('pubmed-screening.jsonl');r=L('registry-evidence.jsonl');e=L('new-evidence.jsonl');checks=[]
def c(label,value):checks.append({'check':label,'passed':bool(value)})
ids=set().union(*(set(x.get('ids',[])) for x in s['pubmed']['queries']))
c('All PubMed query IDs accounted',ids=={x['pmid'] for x in p})
c('22 unique records',len(ids)==len(p)==sm['pubmed_unique_ids']==22)
c('33 query occurrences',sum(x['count'] for x in s['pubmed']['queries'])==sm['pubmed_id_occurrences']==33)
c('Eight query families',len(s['pubmed']['queries'])==8)
for q in s['pubmed']['queries']:
 c(q['label']+' full return',q['count']==len(q['ids']) and q['count']<q['params']['retmax'])
c('Book included in prior complete scan',[x for x in p if x['pmid']=='23556151'][0]['prior_complete_scan_overlap'])
c('Four nonoverlap IDs after book correction',len(sm['pubmed_ids_not_in_prior_complete_scan'])==4)
c('One qualifying journal paper',[x['pmid'] for x in p if x.get('qualifying_new_journal_publication')]==['42993949'])
c('Not first public disclosure',not e[0]['first_public_disclosure_in_window'])
c('New PMID metadata date',next(x for x in p if x['pmid']=='42993949')['article_dates'][0]['Day']=='06')
for x in s['preprints']:
 name=x['server'];pairs={(v['doi'],v['version']) for v in x['version_index']}
 c(name+' complete pagination',x['pagination_complete_for_observed_response'])
 c(name+' totals stable and accounted',x['reported_totals']==[len(pairs)] and len(pairs)==len(x['version_index']))
 c(name+' zero matches',x['matches']==[])
 c(name+' cursor continuity',[v['cursor'] for v in x['pages']]==list(range(0,len(pairs),30)))
 c(name+' date range',all('2026-11-04'<=v['date']<='2026-11-07' for v in x['version_index']))
 c(name+' saved TSV rows',len((P/(name+'-preprint-index.tsv')).read_text().splitlines())-1==len(pairs))
c('1084 unique preprint versions',sm['preprint_versions']==1084)
c('409 absent from prior index',sum(x['not_in_previous_scan_doi_versions'] for x in s['preprints'])==409)
regex=re.compile(r'\btourett\w*|\btics?\b',re.I)
c('Positive lexical controls',all(regex.search(x) for x in ['Tourette syndrome','chronic motor tics','persistent tic disorder']))
c('Negative lexical controls',all(not regex.search(x) for x in ['statistics','genetics','politics']))
failed=[x for x in s['retrieval_requests'] if 'error' in x];success=[x for x in s['retrieval_requests'] if x.get('status')==200]
c('Two transient failures, 55 successes, 57 requests',len(failed)==2 and len(success)==55 and len(s['retrieval_requests'])==57)
for f in failed:c('Recovered '+f['url'],any(x['url']==f['url'] and x['started_utc']>f['completed_utc'] for x in success))
c('No worker errors',not s.get('worker_errors'))
c('Six registry IDs',len(r)==len({x['nctId'] for x in r})==6)
c('Five direct watches',len(s['registry_direct_controls'])==5)
c('No unconsumed registry page',all(not q['response']['nextPageToken'] for q in s['registry']))
c('No posted results',all(x['hasResults'] is False for x in r))
c('One changed watch',[x['nctId'] for x in r if x['selected_field_changes']]==['NCT07137442'])
ch=next(x for x in r if x['nctId']=='NCT07137442')['selected_field_changes']
c('Only three date changes',{x['field'] for x in ch}=={'status.startDateStruct.date','status.lastUpdateSubmitDate','status.lastUpdatePostDateStruct.date'})
c('Clinical registry privacy projection',all(not any(k in json.dumps(x) for k in ['contactsLocationsModule','resultsSection','responsibleParty']) for x in r))
c('13 official safety sources',len(J('safety-review.json')['official_pages'])==13)
c('90 EMA index headlines',J('ema-index-check.json')['date_stamped_rows']==90)
c('EMA match only historical asenapine',J('ema-index-check.json')['matched_headings']==['03/11/2026 Medicine : Sycrest asenapine Updated'])
c('Six safety search queries',len(J('safety-query-log.json')['queries'])==6)
c('Primary new record DOI',e[0]['doi']=='10.2196/98782')
c('Clip distinction preserved','not 55 independent' in (P/'report.md').read_text() or 'not 55 independently' in (P/'report.md').read_text())
c('Qwen integer arithmetic',a['rows']['Qwen3-VL']['compatible_correct_counts_n55']==[49])
for name,k in [('DNN',40),('Embed-freeze',41),('Embed-partial',43)]:c(name+' discrepancy not repaired',a['rows'][name]['compatible_correct_counts_n55']==[] and a['rows'][name]['compatible_correct_counts_n54']==[k])
c('No transient abstract file retained',not (P/'transient-screen-output.txt').exists())
c('No full text or images retained',not any(x.suffix.lower() in ['.pdf','.png','.jpg','.jpeg','.mp4','.xml','.html'] for x in P.glob('*')))
c('Baseline required file hashes',all(x['matches'] for x in J('baseline-verification.json')['files']))
out={'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'passed':all(x['passed'] for x in checks),'check_count':len(checks),'checks':checks,'limits':'Artifact accounting and arithmetic only; not independent clinical peer review or model replication.'}
(P/'validation.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='checks'}));print('Failures',[x for x in checks if not x['passed']]);assert out['passed']
