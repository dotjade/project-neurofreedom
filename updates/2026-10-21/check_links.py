import json,urllib.request,urllib.error,datetime,re,concurrent.futures
from pathlib import Path
root=Path('/workspace/shared/neuro-2026-10-21-repo')
f=json.loads((root/'public/research-feed.json').read_text())
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
items=[dict(kind='timeline',url=x['record'],title=x['title']) for x in f['timeline']]+[dict(kind='finding',url=x['url'],title=x['title']) for x in f['findings']]
def check(item):
 r=dict(item,checkedAt=now(),method='ordinary anonymous HTTP GET with redirects; no credentials, security override or bypass')
 try:
  with urllib.request.urlopen(item['url'],timeout=45) as x:
   b=x.read(2000000); r.update(httpStatus=x.status,finalUrl=x.url,contentType=x.headers.get('Content-Type'),bytesRead=len(b))
   text=b.decode('utf-8',errors='ignore'); t=re.search('<title[^>]*>(.*?)</title>',text,re.S|re.I)
   if t:r['documentTitle']=re.sub(r'\s+',' ',t.group(1)).strip()
   if item['kind']=='timeline':r['renderedArticlePresent']='react-app.embeddedData' in text or 'markdown-body' in text
   r['status']='retrievable';r['establishedBroken']=False
 except urllib.error.HTTPError as e:
  r.update(httpStatus=e.code,status='access limited, not established broken' if e.code in [401,403,429] else 'HTTP error; needs confirmation',establishedBroken=False)
 except Exception as e:r.update(status='retrieval limited',error=str(e),establishedBroken=False)
 return r
start=now()
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as p: out=list(p.map(check,items))
report=dict(checkedAt=start,completedAt=now(),checkDate='2026-10-21',scope='All 13 pre-existing timeline links and three finding sources in the repository feed. Response bodies were inspected transiently and not retained.',repositoryFeedUpdatedAt=f['updatedAt'],results=out)
Path('/workspace/shared/neuro-2026-10-21-public/link-checks.json').write_text(json.dumps(report,indent=2)+'\n')
for r in out:print(r['url'],r.get('httpStatus'),r['status'])
