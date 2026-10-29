import urllib.request,json,datetime,hashlib,re
out={'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'server':'medrxiv','interval':['2026-10-27','2026-10-29'],'requests':[],'index':[],'matches':[],'pages':[]};cursor=0
while True:
 u=f'https://api.biorxiv.org/details/medrxiv/2026-10-27/2026-10-29/{cursor}';q={'url':u,'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  b=urllib.request.urlopen(u,timeout=30).read();d=json.loads(b);q.update(status=200,sha256=hashlib.sha256(b).hexdigest());c=d.get('collection',[]);m=d.get('messages',[{}])[0];out['pages'].append({'cursor':cursor,'returned':len(c),'message':m})
  for x in c:
   out['index'].append({k:x.get(k)for k in ['doi','version','date']})
   if re.search(r'\btourett\w*|\btics?\b',x.get('title','')+' '+x.get('abstract',''),re.I):out['matches'].append({k:x.get(k)for k in ['doi','version','date','title']})
  done=not c or cursor+len(c)>=int(m.get('total',0));cursor+=len(c)
 except Exception as e:q['error']=str(e);done=True
 q['completed_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();out['requests'].append(q)
 if done:break
out['completed_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();open(__import__('sys').argv[1],'w').write(json.dumps(out,indent=2));print(len(out['index']),out['matches'],out['requests'][-1])
