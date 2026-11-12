#!/usr/bin/env python3
"""Small public-metadata scan with 18-second total HTTP deadlines and checkpoints.
Run: python scan.py --baseline prior/search-log.json --out .
Does not save abstracts, participant rows, contacts or source full texts.
"""
import argparse, concurrent.futures, datetime, hashlib, json, pathlib, re, subprocess, threading, time, urllib.parse, xml.etree.ElementTree as ET
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
ap=argparse.ArgumentParser();ap.add_argument('--baseline',required=True);ap.add_argument('--out',default='.');a=ap.parse_args()
out=pathlib.Path(a.out);out.mkdir(parents=True,exist_ok=True);rawbase=pathlib.Path(a.baseline).read_bytes();base=json.loads(rawbase)
log={'date':'2026-11-12','started_utc':utc(),'baseline_sha256':hashlib.sha256(rawbase).hexdigest(),'prior_cutoff_utc':base['completed_utc'],'status':'Running','requests':[],'pubmed':{},'registry':{},'preprints':{},'limits':['This fresh smaller rebuild replaces lost local scan archives; earlier findings survive only in conversation, not retained artifacts.','18-second total HTTP deadline; no automatic retries.','Metadata dates and administrative changes are not new clinical outcomes.']}
lock=threading.RLock()
def save():
 with lock:
  p=out/'scan.json';tmp=out/'scan.json.tmp';tmp.write_text(json.dumps(log,separators=(',',':'))+'\n');tmp.replace(p)
def get(url,kind='json'):
 r={'url':url,'started_utc':utc()}
 proc=subprocess.run(['curl','--fail','--silent','--show-error','--location','--max-time','18','--user-agent','PublicEvidenceScan/1.0',url],capture_output=True,timeout=22)
 r['completed_utc']=utc();r['exit_code']=proc.returncode
 if proc.returncode:r['error']=proc.stderr.decode(errors='replace')[:300];data=None
 else:
  r.update(bytes=len(proc.stdout),sha256=hashlib.sha256(proc.stdout).hexdigest())
  try:data=json.loads(proc.stdout) if kind=='json' else ET.fromstring(proc.stdout)
  except Exception as e:r['parse_error']=str(e);data=None
 with lock:log['requests'].append(r);save()
 return data
def url(base,params):return base+'?'+urllib.parse.urlencode(params)
def tx(x):return ''.join(x.itertext()) if x is not None else ''
def dates(x):return {c.tag:c.text for c in x} if x is not None else None
def pm():
 terms='Tourette OR "tic disorder" OR "tic disorders" OR "chronic motor tic" OR "chronic vocal tic" OR "persistent tic" OR tics'
 window=' OR '.join('("2026/11/10"['+f+']:"2026/11/12"['+f+'])' for f in ['EDAT','PDAT','MDAT'])
 queries=[('all_dates',f'({terms}) AND ({window})'),('notices',f'({terms}) AND (retraction OR retracted OR correction OR corrigendum OR erratum) AND ({window})'),('adult_burden',f'({terms}) AND (adult OR severe OR pain OR burden OR function OR participation OR comorbid* OR adverse OR treatment) AND ("2026/11/10"[EDAT]:"2026/11/12"[EDAT])')]
 qlog=[];ids=set()
 for label,term in queries:
  params={'db':'pubmed','term':term,'retmode':'json','retmax':200}
  x=get(url('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi',params));r={'label':label,'term':term}
  if x and 'esearchresult' in x:
   z=x['esearchresult'];r.update(count=int(z['count']),ids=z['idlist'],querytranslation=z.get('querytranslation'),warnings=z.get('warninglist'));ids.update(z['idlist'])
  qlog.append(r)
  with lock:log['pubmed']['queries']=qlog;save()
  time.sleep(.4)
 records=[];prior={x['pmid'] for x in base['pubmed']['date_type_correction_screen']}
 if ids:
  x=get(url('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi',{'db':'pubmed','id':','.join(sorted(ids)),'retmode':'xml'}),'xml')
  if x is not None:
   for ar in x.findall('PubmedArticle'):
    m=ar.find('MedlineCitation');art=m.find('Article');pd=ar.find('PubmedData');pid=tx(m.find('PMID'))
    row={'pmid':pid,'title':tx(art.find('ArticleTitle')),'article_dates':[dict(type=d.attrib.get('DateType'),**dates(d)) for d in art.findall('ArticleDate')],'journal_date':dates(art.find('Journal/JournalIssue/PubDate')),'types':[tx(t) for t in art.findall('PublicationTypeList/PublicationType')],'ids':{i.attrib.get('IdType'):tx(i) for i in pd.findall('ArticleIdList/ArticleId')},'corrections':[{'type':c.attrib.get('RefType'),'pmid':tx(c.find('PMID'))} for c in m.findall('CommentsCorrectionsList/CommentsCorrections')],'prior_scan_overlap':pid in prior,'source':'https://pubmed.ncbi.nlm.nih.gov/'+pid+'/','decision':'Pending metadata review'}
    records.append(row)
 with lock:log['pubmed'].update(unique_ids=sorted(ids),records=records,record_count=len(records),previous_overlap=len(ids&prior));save()
def compact(r):
 p=r['protocolSection'];s=p.get('statusModule',{});e=p.get('eligibilityModule',{});d=p.get('designModule',{})
 return {'nctId':p['identificationModule']['nctId'],'title':p['identificationModule'].get('briefTitle'),'status':s,'conditions':p.get('conditionsModule',{}).get('conditions',[]),'ages':e,'studyType':d.get('studyType'),'enrollment':d.get('enrollmentInfo'),'hasResults':r.get('hasResults')}
def priorcompact(r):
 return {'nctId':r['nctId'],'title':r['title'],'status':r['status'],'conditions':r['conditions'],'ages':r['eligibility'],'studyType':r['design'].get('studyType'),'enrollment':r['design'].get('enrollmentInfo'),'hasResults':r['hasResults']}
def ct():
 fields='NCTId,BriefTitle,StatusModule,DesignModule,Condition,MinimumAge,MaximumAge,StdAge,HasResults'
 params={'query.cond':'Tourette OR tic disorder OR tics','filter.advanced':'AREA[LastUpdatePostDate]RANGE[2026-11-10,2026-11-12]','fields':fields,'pageSize':100,'countTotal':'true','format':'json'}
 x=get(url('https://clinicaltrials.gov/api/v2/studies',params));records={}
 if x:
  for r in x.get('studies',[]):records[r['protocolSection']['identificationModule']['nctId']]=compact(r)
 with lock:log['registry']['query']={'params':params,'count':x.get('totalCount') if x else None,'ids':list(records),'nextPageToken':x.get('nextPageToken') if x else None};save()
 watched=['NCT01019343','NCT05158439','NCT07093541','NCT06194305','NCT07137442','NCT07905898','NCT06678737'];additional=['NCT06785532','NCT06271083','NCT05615220'];prior={x['nctId']:priorcompact(x) for x in base['registry_records']}
 for n in watched+additional:
  x=get(url('https://clinicaltrials.gov/api/v2/studies/'+n,{'fields':fields}))
  if x:records[n]=compact(x)
  with lock:log['registry']['records']=list(records.values());save()
 diffs={}
 for n in watched:
  if n in records:diffs[n]={k:{'prior':prior[n].get(k),'current':v} for k,v in records[n].items() if v!=prior[n].get(k)}
 with lock:log['registry'].update(watched=watched,additional=additional,selected_field_diffs=diffs);save()
def pp():
 regex=re.compile(r'\btourett\w*|\btics?\b',re.I)
 for server,maxpages in [('medrxiv',4),('biorxiv',1)]:
  r={'interval':['2026-11-08','2026-11-12'],'pages':[],'index':[],'matches':[],'complete':False,'screen_regex':regex.pattern,'screen_fields':['title','abstract'],'max_pages':maxpages};cursor=0
  for i in range(maxpages):
   x=get(f'https://api.biorxiv.org/details/{server}/2026-11-08/2026-11-12/{cursor}')
   if not x:r['failure']='Request unavailable within bounded deadline; no complete negative conclusion.';break
   coll=x.get('collection',[]);msg=x.get('messages',[{}])[0];r['pages'].append({'cursor':cursor,'returned':len(coll),'total':msg.get('total')})
   for z in coll:
    r['index'].append([z.get('doi'),z.get('version'),z.get('date')])
    if regex.search(z.get('title','')+' '+z.get('abstract','')):r['matches'].append({k:z.get(k) for k in ['doi','version','date','title']})
   cursor+=len(coll)
   if not coll or cursor>=int(msg.get('total',0)):r['complete']=True;break
   with lock:log['preprints'][server]=r;save()
  r['unique_versions']=len({tuple(z[:2]) for z in r['index']})
  pri={tuple([z['doi'],z['version']]) for z in next(y for y in base['preprints'] if y['server']==server)['version_index']}
  r['previous_overlap']=len({tuple(z[:2]) for z in r['index']}&pri)
  if not r['complete']:r['limitation']='Partial/unavailable bounded scan; do not generalize match count to whole server.'
  with lock:log['preprints'][server]=r;save()
save()
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
 fs=[ex.submit(pm),ex.submit(ct),ex.submit(pp)]
 for f in fs:
  try:f.result()
  except Exception as e:
   with lock:log.setdefault('errors',[]).append(str(e));save()
log['completed_utc']=utc();log['status']='Completed bounded attempts';save()
print(json.dumps({'completed_utc':log['completed_utc'],'pubmed_records':log['pubmed'].get('record_count'),'registry_records':len(log['registry'].get('records',[])),'preprints':{k:{a:b for a,b in v.items() if a not in ['index','pages']} for k,v in log['preprints'].items()}},indent=2))

