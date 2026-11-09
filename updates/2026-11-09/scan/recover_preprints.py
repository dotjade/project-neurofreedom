#!/usr/bin/env python3
"""Resume only the failed medRxiv pagination, without redoing completed requests."""
import datetime as dt, hashlib,json,pathlib,re,urllib.request
p=pathlib.Path(__file__).resolve().parent
def now():return dt.datetime.now(dt.timezone.utc).isoformat()
j=json.loads((p/'search-log.json').read_text());s=next(x for x in j['preprints'] if x['server']=='medrxiv');cursor=s['total_returned'];regex=re.compile(s['screen_regex'],re.I)
out={'started_utc':now(),'server':'medrxiv','recovery_of_failed_cursor':cursor,'requests':[],'version_index':[],'matches':[],'pages':[],'complete':False}
while True:
 u=f'https://api.biorxiv.org/details/medrxiv/2026-11-06/2026-11-09/{cursor}';rec={'url':u,'started_utc':now()}
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'PublicEvidenceScan/1.0'}),timeout=60) as r:raw=r.read();rec.update(status=r.status,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
  d=json.loads(raw);coll=d.get('collection',[]);m=d.get('messages',[{}])[0];out['pages'].append({'cursor':cursor,'returned':len(coll),'message':m})
  for x in coll:
   out['version_index'].append({k:x.get(k) for k in ('doi','version','date')})
   if regex.search(x.get('title','')+' '+x.get('abstract','')):out['matches'].append({k:x.get(k) for k in ('doi','version','date','title','category','published')})
  total=int(m.get('total',0));rec['completed_utc']=now();out['requests'].append(rec)
  if cursor+len(coll)>=total:out['complete']=True;break
  if not coll:break
  cursor+=len(coll)
 except Exception as e:
  rec['error']=str(e);rec['completed_utc']=now();out['requests'].append(rec);break
out['completed_utc']=now();(p/'preprint-recovery.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['version_index','pages']},indent=2))
