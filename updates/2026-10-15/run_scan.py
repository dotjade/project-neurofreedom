"""Bounded public metadata scan. No full text, participant or contact data saved."""
import concurrent.futures, datetime, hashlib, json, pathlib, re, time, urllib.parse, urllib.request, xml.etree.ElementTree as ET
ROOT=pathlib.Path(__file__).parent
BASE=json.loads((ROOT/'baseline-metadata.json').read_text())
START='2026-10-13'; END='2026-10-15'
LEDGER={'date':END,'incremental_baseline':'2026-10-14 02:46:32–02:51:03 UTC; safety separately 02:44:53–02:49:22 UTC','inclusive_overlap':[START,END],'retrieval_requests':[],'baseline_blobs':BASE['blobs']}
def stamp(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def request(url,params=None,kind='json'):
 if params: url += '?'+urllib.parse.urlencode(params)
 log={'url':url,'started_utc':stamp()}
 try:
  r=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'NeuroFreedom-public-evidence-scan/0.1'}),timeout=60)
  b=r.read();log.update(status=r.status,completed_utc=stamp(),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
  return json.loads(b) if kind=='json' else b
 except Exception as e:
  log.update(completed_utc=stamp(),error=type(e).__name__+': '+str(e));raise
 finally: LEDGER['retrieval_requests'].append(log)
def t(e): return ''.join(e.itertext()) if e is not None else ''
def date(e): return {c.tag:c.text for c in e} if e is not None else None
def pubmed():
 core='Tourette OR "tic disorder" OR "tic disorders"'
 syn='tics OR "chronic motor tic" OR "chronic vocal tic" OR "persistent tic"'
 qs=[('core_edat',core,'edat',START),('near_edat',core,'edat','2026-10-14'),('core_pdat',core,'pdat',START),('core_mdat',core,'mdat',START),('notice_edat',f'({core}) AND (retraction OR retracted OR erratum OR corrigendum OR correction)','edat',START),('syn_edat',syn,'edat',START),('syn_pdat',syn,'pdat',START),('burden_treatment_edat',f'({core}) AND (adult OR severe OR pain OR burden OR comorbid* OR treatment OR adverse OR negative OR quality of life)','edat',START)]
 entries=[];ids=set()
 for label,term,typ,mindate in qs:
  p={'db':'pubmed','term':term,'datetype':typ,'mindate':mindate.replace('-','/'),'maxdate':END.replace('-','/'),'retmode':'json','retmax':1000}
  x=request('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi',p)['esearchresult']
  entries.append({'label':label,'params':p,'count':int(x['count']),'ids':x['idlist'],'querytranslation':x['querytranslation'],'warnings':x.get('warninglist'),'errors':x.get('errorlist')});ids.update(x['idlist']);time.sleep(.4)
 records=[];previous={r['pmid']:r for r in BASE['pubmed']['date_type_correction_screen']}
 if ids:
  xml=request('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi',{'db':'pubmed','id':','.join(sorted(ids)),'retmode':'xml'},'xml')
  for a in ET.fromstring(xml).findall('PubmedArticle'):
   pmid=t(a.find('MedlineCitation/PMID'));article=a.find('MedlineCitation/Article')
   rec={'pmid':pmid,'title':t(article.find('ArticleTitle')),'journal_pubdate':date(article.find('Journal/JournalIssue/PubDate')),'article_dates':[{'type':d.get('DateType'),**date(d)} for d in article.findall('ArticleDate')],'history':{d.get('PubStatus'):date(d) for d in a.findall('PubmedData/History/PubMedPubDate')},'types':[t(p) for p in article.findall('PublicationTypeList/PublicationType')],'identifiers':{d.get('IdType'):t(d) for d in a.findall('PubmedData/ArticleIdList/ArticleId')},'DateCompleted':date(a.find('MedlineCitation/DateCompleted')),'DateRevised':date(a.find('MedlineCitation/DateRevised')),'corrections':[{'type':c.get('RefType'),'source':t(c.find('RefSource')),'pmid':t(c.find('PMID'))} for c in a.findall('MedlineCitation/CommentsCorrectionsList/CommentsCorrections')],'prior_scan_overlap':pmid in previous,'source_url':'https://pubmed.ncbi.nlm.nih.gov/'+pmid+'/'}
   rec['linked_notice_changed']=pmid in previous and rec['corrections']!=previous[pmid].get('corrections',[])
   records.append(rec)
   if pmid not in previous:
    print('NEW_METADATA',json.dumps(rec),flush=True)
    print('ABSTRACT_FOR_SCREENING_ONLY',pmid,' '.join(t(x) for x in article.findall('Abstract/AbstractText')),flush=True)
 LEDGER['pubmed']={'queries':entries,'id_occurrences':sum(q['count'] for q in entries),'unique_records':len(records),'date_type_correction_screen':records,'new_to_prior_scan_ids':sorted(ids-set(previous)),'previous_overlap_count':len(ids&set(previous)),'screening_depth':'All retrieved date/type/identifier/linked-notice metadata; newly encountered abstracts inspected, not full-text review.'}
 print('PUBMED_SUMMARY',[(q['label'],q['count']) for q in entries],len(records),flush=True)
def preprints(server):
 prev={(r['doi'],r['version']) for p in BASE['preprints'] if p['server']==server for r in p['version_index']}
 result={'server':server,'interval':[START,END],'pages':[],'version_index':[],'matches':[],'screen_regex':r'\btourett\w*|\btics?\b','screen_fields':['title','abstract'],'scope_limit':'Titles/abstract lexical screen of this live official server interval only; DOI/version records are not necessarily new papers.'}
 cursor=0;seen=set();regex=re.compile(result['screen_regex'],re.I)
 while True:
  url=f'https://api.biorxiv.org/details/{server}/{START}/{END}/{cursor}'
  x=request(url);coll=x.get('collection',[]);msgs=x.get('messages',[])
  result['pages'].append({'cursor':cursor,'returned':len(coll),'messages':msgs})
  for r in coll:
   key=(r.get('doi'),r.get('version'));seen.add(key)
   result['version_index'].append({k:r.get(k) for k in ['doi','version','date']})
   if regex.search(r.get('title','')+' '+r.get('abstract','')):
    result['matches'].append({k:r.get(k) for k in ['doi','version','date','title','server','type','category','published','jatsxml']})
    print('PREPRINT_MATCH',server,json.dumps(result['matches'][-1]),r.get('abstract'),flush=True)
  total=int(msgs[0].get('total',0)) if msgs else 0
  if not coll or len(coll)<30 or cursor+len(coll)>=total: break
  cursor+=len(coll)
 result.update(total_returned=sum(p['returned'] for p in result['pages']),unique_doi_versions=len(seen),previous_scan_overlap_doi_versions=len(seen&prev),not_in_previous_scan_doi_versions=len(seen-prev),pagination_complete_for_observed_response=True,reported_totals=sorted(set(int(p['messages'][0].get('total',0)) for p in result['pages'] if p['messages'])))
 print('PREPRINT_SUMMARY',server,{k:v for k,v in result.items() if k not in ['version_index','pages']},flush=True)
 return result
def registry():
 queries=[];studies={}
 for label,key,val in [('ct_tourette','query.cond','Tourette'),('ct_tic_disorder','query.cond','tic disorder'),('ct_tics','query.cond','Tics'),('ct_ecopipam','query.term','ecopipam')]:
  p={key:val,'filter.advanced':f'AREA[LastUpdatePostDate]RANGE[{START},{END}]','pageSize':100,'format':'json','countTotal':'true'}
  x=request('https://clinicaltrials.gov/api/v2/studies',p);ids=[]
  for s in x.get('studies',[]):
   pro=s['protocolSection'];nct=pro['identificationModule']['nctId'];ids.append(nct)
   studies[nct]={'nctId':nct,'title':pro['identificationModule'].get('briefTitle'),'status':pro.get('statusModule'),'hasResults':s.get('hasResults'),'conditions':pro.get('conditionsModule'),'design':pro.get('designModule'),'outcomes':pro.get('outcomesModule'),'eligibility':{k:pro.get('eligibilityModule',{}).get(k) for k in ['minimumAge','maximumAge','sex','healthyVolunteers']},'source_url':'https://clinicaltrials.gov/study/'+nct}
  queries.append({'label':label,'params':p,'response':{'totalCount':x.get('totalCount'),'nct_ids':ids,'nextPageToken':x.get('nextPageToken')}})
  if x.get('nextPageToken'): raise RuntimeError('Registry pagination required')
 LEDGER['registry']=queries;LEDGER['registry_records']=list(studies.values());print('REGISTRY_SUMMARY',json.dumps(LEDGER['registry']),json.dumps(list(studies.values())),flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 futures={pool.submit(pubmed):'pubmed',pool.submit(registry):'registry',pool.submit(preprints,'biorxiv'):'biorxiv',pool.submit(preprints,'medrxiv'):'medrxiv'}
 LEDGER['preprints']=[]
 for f in concurrent.futures.as_completed(futures):
  task=futures[f]
  try:
   res=f.result()
   if task in ['biorxiv','medrxiv']: LEDGER['preprints'].append(res)
  except Exception as e: LEDGER.setdefault('errors',[]).append({'task':task,'error':str(e)});print('ERROR',task,str(e),flush=True)
  (ROOT/'search-log.json').write_text(json.dumps(LEDGER,indent=2)+'\n')
print('SAVED',str(ROOT/'search-log.json'),flush=True)
