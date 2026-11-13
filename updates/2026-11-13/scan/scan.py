import json, pathlib, urllib.request, urllib.parse, datetime, hashlib, concurrent.futures, re, time, xml.etree.ElementTree as ET
O=pathlib.Path(__file__).parent
def utc(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def text(e): return ''.join(e.itertext()) if e is not None else ''
L={'date':'2026-11-13','started_utc':utc(),'requests':[],'pubmed':{},'registry':{},'preprints':{}}
def get(url,params=None,xml=False):
 if params: url+='?'+urllib.parse.urlencode(params)
 r={'url':url,'started_utc':utc()}
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'PublicEvidenceReview/1.0'}),timeout=20) as f: b=f.read(); r.update(status=f.status,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
  data=ET.fromstring(b) if xml else json.loads(b)
 except Exception as e: r['error']=str(e);data=None
 r['completed_utc']=utc();L['requests'].append(r)
 (O/'scan.json').write_text(json.dumps(L,indent=2))
 return data
def pm():
 core='(Tourette OR "tic disorder" OR "tic disorders" OR "chronic motor tic" OR "chronic vocal tic" OR "persistent tic" OR tics)'
 dates=' OR '.join(f'("2026/11/11"[{x}]:"2026/11/13"[{x}])' for x in ['EDAT','PDAT','MDAT'])
 qs=[core+' AND ('+dates+')',core+' AND (correction OR retraction OR erratum OR corrigendum) AND ('+dates+')',core+' AND (adult OR severe OR refractory OR pain OR impairment OR participation OR ADHD OR adverse) AND ('+dates+')']
 ids=set();queries=[]
 for q in qs:
  d=get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi',{'db':'pubmed','term':q,'retmode':'json','retmax':500})
  queries.append({'query':q,'result':d});ids.update(d.get('esearchresult',{}).get('idlist',[]) if d else []);time.sleep(.4)
 records=[]
 if ids:
  d=get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi',{'db':'pubmed','id':','.join(sorted(ids)),'retmode':'xml'},True)
  if d is not None:
   for x in d.findall('PubmedArticle'):
    m=x.find('MedlineCitation');a=m.find('Article');p=x.find('PubmedData');pmid=text(m.find('PMID'))
    item={'pmid':pmid,'title':text(a.find('ArticleTitle')),'types':[text(t) for t in a.findall('PublicationTypeList/PublicationType')],'identifiers':{t.attrib.get('IdType'):text(t) for t in p.findall('ArticleIdList/ArticleId')},'article_dates':[{**t.attrib,**{c.tag:c.text for c in t}} for t in a.findall('ArticleDate')],'journal_date':text(a.find('Journal/JournalIssue/PubDate')),'corrections':[{**t.attrib,'pmid':text(t.find('PMID')),'source':text(t.find('RefSource'))} for t in m.findall('CommentsCorrectionsList/CommentsCorrections')],'source_url':'https://pubmed.ncbi.nlm.nih.gov/'+pmid+'/'}
    records.append(item)
    print('REVIEW',pmid,item['title'],text(a.find('Abstract')),flush=True)
 L['pubmed']={'queries':queries,'unique_returned_ids':sorted(ids),'records':records}
def ct():
 fields='NCTId,BriefTitle,StatusModule,DesignModule,Condition,MinimumAge,MaximumAge,StdAge,HasResults'
 d=get('https://clinicaltrials.gov/api/v2/studies',{'query.cond':'Tourette OR tic disorder OR tics','filter.advanced':'AREA[LastUpdatePostDate]RANGE[2026-11-11,2026-11-13]','fields':fields,'pageSize':100,'countTotal':'true','format':'json'})
 ids=['NCT01019343','NCT05158439','NCT07093541','NCT06194305','NCT07137442','NCT07905898','NCT06678737','NCT06271083','NCT06785532','NCT05615220']
 records={}
 if d:
  for x in d.get('studies',[]): records[x['protocolSection']['identificationModule']['nctId']]=x
 with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
  for i,x in zip(ids,pool.map(lambda i:get('https://clinicaltrials.gov/api/v2/studies/'+i,{'fields':fields}),ids)):
   if x: records[i]=x
 L['registry']={'query_result':d,'records':records}
def pre(server):
 rows={};matches=[];pages=[];cursor=0;start=time.monotonic();complete=False
 while time.monotonic()-start<160:
  d=get(f'https://api.biorxiv.org/details/{server}/2026-11-10/2026-11-13/{cursor}')
  if not d:break
  c=d.get('collection',[]);m=d.get('messages',[{}])[0];pages.append({'cursor':cursor,'message':m,'returned':len(c)})
  for x in c:
   key=(x.get('doi'),x.get('version'));rows[key]={k:x.get(k) for k in ['doi','version','date']}
   if re.search(r'\btourett\w*|\btics?\b',x.get('title','')+' '+x.get('abstract',''),re.I):
    matches.append({k:x.get(k) for k in ['doi','version','date','title','published']});print('PREPRINT_REVIEW',server,x.get('title'),x.get('abstract'),flush=True)
  if not c or cursor+len(c)>=int(m.get('total',0)):complete=True;break
  cursor+=len(c)
 L['preprints'][server]={'interval':['2026-11-10','2026-11-13'],'pages':pages,'unique_versions':list(rows.values()),'matches':matches,'pagination_complete_for_observed_responses':complete,'lexical_regex':r'\btourett\w*|\btics?\b','fields_screened':['title','abstract']}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as p:
 fs=[p.submit(pm),p.submit(ct),p.submit(pre,'medrxiv'),p.submit(pre,'biorxiv')]
 for f in fs:
  try:f.result()
  except Exception as e:print('ERROR',str(e),flush=True)
L['completed_utc']=utc();(O/'scan.json').write_text(json.dumps(L,indent=2));print('DONE',flush=True)
