#!/usr/bin/env python3
"""Read primary publisher HTML transiently; retain selected metadata/aggregate rows only."""
import datetime as dt,hashlib,html,json,pathlib,re,urllib.request
from html.parser import HTMLParser
OUT=pathlib.Path(__file__).resolve().parent
class Rows(HTMLParser):
 def __init__(self):super().__init__();self.row=None;self.rows=[];self.inscript=False
 def handle_starttag(self,t,a):
  if t=='tr':self.row=[]
 def handle_endtag(self,t):
  if t=='tr'and self.row is not None:self.rows.append(' '.join(self.row));self.row=None
 def handle_data(self,d):
  if self.row is not None and d.strip():self.row.append(d.strip())
def utc():return dt.datetime.now(dt.timezone.utc).isoformat()
def main():
 checks=[];base='https://link.springer.com/article/10.1186/s12888-026-08454-7'
 for suffix in ['', '/tables/2','/tables/3']:
  u=base+suffix;r={'url':u,'started_utc':utc()}
  try:
   with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'PublicEvidenceScan/1.0'}),timeout=60)as f:b=f.read();r.update(status=f.status,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
   s=b.decode();p=Rows();p.feed(s)
   if suffix:
    ix=next(i for i,x in enumerate(p.rows)if'Tourette syndrome'in x);r['selected_tourette_rows']=p.rows[ix:ix+(3 if suffix.endswith('3')else 1)]
   else:
    r['selected_metadata']={'doi':'10.1186/s12888-026-08454-7','published_date':'2026-07-25','version_of_record_date':'2026-10-23','license':'CC-BY-NC-ND-4.0','competing_interests':'Authors declare none','funding':'Shanghai Children’s Medical Center GuiZhou Hospital talent fund and Guizhou provincial innovation-talent support'}
  except Exception as e:r['error']=str(e)
  r['completed_utc']=utc();checks.append(r)
 (OUT/'primary-source-checks.json').write_text(json.dumps(checks,indent=2,ensure_ascii=False)+'\n');print(json.dumps(checks,indent=2,ensure_ascii=False))
if __name__=='__main__':main()
