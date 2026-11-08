"""Offline accounting and provenance validation, not clinical validation."""
import pathlib,json,re,hashlib,csv,datetime
P=pathlib.Path(__file__).parent
j=lambda n:json.loads((P/n).read_text())
rows=lambda n:[json.loads(l) for l in (P/n).read_text().splitlines() if l.strip()]
s=j('search-log.json');b=j('baseline.json');q=j('summary.json');p=rows('pubmed-screening.jsonl');r=rows('registry-evidence.jsonl');sp=j('supplement-pubmed.json');sr=j('supplement-registry.json');checks=[]
def check(name,ok):checks.append({'name':name,'pass':bool(ok)})
ids=set(sum([x['ids'] for x in s['pubmed']['queries']],[]))
check('Eight complete PubMed query families',len(s['pubmed']['queries'])==8 and all(x.get('count')==len(x.get('ids',[])) for x in s['pubmed']['queries']))
check('PubMed count and extraction agreement',len(ids)==len(p)==q['pubmed_unique_ids']==7)
check('PubMed occurrence accounting',sum(len(x['ids']) for x in s['pubmed']['queries'])==q['pubmed_id_occurrences']==13)
check('All returned PubMed IDs classified exactly once',ids=={x['pmid'] for x in p} and len(p)==len({x['pmid'] for x in p}) and all(x['screening_decision']!='REQUIRES REVIEW' for x in p))
check('No unknown PubMed worker errors',not s.get('worker_errors'))
check('Only one ID new to complete baseline',ids-{x['pmid'] for x in b['pubmed']}=={'42995077'})
check('No new qualifying journal primary',q['new_peer_reviewed_primary_publications']==[] and not any(x['qualifying_new_journal_publication'] for x in p))
check('Wu remains same-paper overlap',next(x for x in p if x['pmid']=='42993949')['prior_complete_scan_overlap'])
old=next(x for x in b['pubmed'] if x['pmid']=='41503301');cur=next(x for x in p if x['pmid']=='41503301')
check('Historical retraction status unchanged','Retracted Publication' in cur['types'] and cur['corrections']==old['corrections'] and not cur['linked_notice_changed'])
notices={x['pmid']:x for x in sp['records']}
check('Retraction notice reciprocal metadata','Retraction Notice' in notices['42991793']['types'] and any(x['pmid']=='41503301' and x['RefType']=='RetractionOf' for x in notices['42991793']['corrections']))
check('Editorial independently identified',notices['42995077']['types']==['Editorial'] and notices['42995077']['ids']['doi']=='10.1016/j.tics.2026.10.008')
check('Total distinct query and supplementary PubMed IDs',len(ids|set(notices))==8)
check('Core date overlap preserved',s['inclusive_overlap']==['2026-11-06','2026-11-08'] and s['prior_core_end_utc']==b['cutoff_utc'])
check('Core temporal order',s['started_utc']<s['completed_utc'] and s['started_utc'].startswith('2026-11-08'))
check('All core requests succeeded',len(s['retrieval_requests'])==44 and all(x.get('status')==200 and 'error' not in x for x in s['retrieval_requests']))
check('Each core response has timestamp and digest',all(len(x['sha256'])==64 and x['started_utc']<=x['completed_utc'] and x['bytes']>0 for x in s['retrieval_requests']))
check('Two preprint servers present',{x['server'] for x in s['preprints']}=={'biorxiv','medrxiv'})
regex=re.compile(r'\btourett\w*|\btics?\b',re.I)
check('Preprint lexical controls',bool(regex.search('Tourette syndrome')) and bool(regex.search('chronic motor tics')) and not regex.search('statistics'))
total=0;newtotal=0
for x in s['preprints']:
 name=x['server'];keys={(v['doi'],v['version']) for v in x['version_index']};prior={(v['doi'],v['version']) for v in b['preprints'][name]};total+=len(keys);newtotal+=len(keys-prior)
 check(name+' complete observed pagination',x['pagination_complete_for_observed_response'] and x['reported_totals']==[len(keys)] and sum(v['returned'] for v in x['pages'])==len(keys))
 check(name+' DOI/version index accounting',len(keys)==len(x['version_index'])==x['unique_doi_versions'] and len(keys-prior)==x['not_in_previous_scan_doi_versions'])
 with (P/(name+'-preprint-index.tsv')).open() as f:table=list(csv.DictReader(f,delimiter='\t'))
 check(name+' saved TSV matches captured index',table==x['version_index'])
 check(name+' no qualifying match',x['matches']==[])
check('Preprint totals reconciled',total==q['preprint_versions']==708 and newtotal==84)
check('Four registry query responses complete',len(s['registry'])==4 and all('response'in x and x['response']['nextPageToken'] is None and len(x['response']['nct_ids'])==x['response']['totalCount'] for x in s['registry']))
check('Six registry watches retained',len(r)==len(s['registry_direct_controls'])==6 and {x['nctId'] for x in r}==set(s['registry_direct_controls']))
check('No changed selected registry field',not any(x['selected_field_changes'] for x in r) and q['registry_ids_changed']==[])
check('No posted results among core registries',all(x['hasResults'] is False for x in r))
supp=sr['snapshot'];ps=supp['protocolSection']
check('Supplement is independent seventh registry',ps['identificationModule']['nctId']=='NCT06678737' and 'NCT06678737' not in {x['nctId'] for x in r})
check('Aggregator date resolved using official API',ps['statusModule']['lastUpdatePostDateStruct']['date']=='2026-05-20' and supp['hasResults'] is False)
check('Supplement requests successful',sp.get('status')==sr.get('status')==200 and len(sp['sha256'])==len(sr['sha256'])==64)
check('Baseline Git object verification passed',all(x['match'] and x['git_blob_sha']==x['git_blob_recomputed'] for x in j('baseline-verification.json')['sources']))
safe=j('safety-review.json')
check('Twelve official safety pages recorded',len(safe['official_pages'])==12)
check('Inaccessible safety lead retained',len(safe['unresolved_leads'])==1 and 'timed out' in safe['unresolved_leads'][0]['outcome'])
check('Web query limits and exact queries retained',len(j('safety-query-log.json')['queries'])==6 and len(j('discovery-log.json')['queries'])==8)
result={'date':'2026-11-08','checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':checks,'passed':sum(x['pass'] for x in checks),'total':len(checks),'all_pass':all(x['pass'] for x in checks),'scope':'Offline source-accounting and consistency checks only; no clinical validation.'}
(P/'validation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));raise SystemExit(0 if result['all_pass'] else 1)
