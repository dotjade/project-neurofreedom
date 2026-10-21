#!/usr/bin/env python3
"""Record publisher date contexts without persisting source HTML/full text."""
import pathlib,urllib.request,hashlib,json,re,html
from html.parser import HTMLParser
from scan_supplement import utc
OUT=pathlib.Path(__file__).resolve().parent
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.text=[];self.skip=0
 def handle_starttag(self,tag,attrs):
  if tag in ['script','style']:self.skip+=1
 def handle_endtag(self,tag):
  if tag in ['script','style']:self.skip=max(0,self.skip-1)
 def handle_data(self,data):
  if not self.skip:self.text.append(data)
def main():
 url='https://doi.org/10.3174/ajnr.A9681';r={'url':url,'started_utc':utc(),'body_retained':False}
 try:
  with urllib.request.urlopen(url,timeout=60) as f:raw=f.read();r.update(status=f.status,final_url=f.url,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
  p=Parser();p.feed(raw.decode(errors='replace'));text=re.sub(r'\s+',' ',' '.join(p.text))
  r['visible_date_contexts']=[text[max(0,m.start()-35):m.end()+45] for m in re.finditer(r'(?:October|Oct)\.?\s+(?:15|19),?\s+2026|(?:15|19)\s+October\s+2026',text)][:10]
 except Exception as e:r['error']=str(e)
 r['completed_utc']=utc();(OUT/'publisher-date-check.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
if __name__=='__main__':main()
