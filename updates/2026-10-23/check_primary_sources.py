#!/usr/bin/env python3
"""Retrieve lawful primary XML transiently; retain identifiers, publication dates and license URLs only.
Never downloads participant data, figures, supplements, narratives, or full source bodies to disk.
"""
import datetime as dt,hashlib,json,pathlib,urllib.request,xml.etree.ElementTree as E
OUT=pathlib.Path(__file__).resolve().parent
def txt(x):return ' '.join(''.join(x.itertext()).split()) if x is not None else None
def utc():return dt.datetime.now(dt.timezone.utc).isoformat()
def main():
 records=[]
 for pmc,doi in [('13683974','10.1002/mdc3.70882'),('13680449','10.3389/fpsyt.2026.1948693')]:
  url=f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id={pmc}&retmode=xml';r={'url':url,'started_utc':utc()}
  try:
   with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'PublicEvidenceScan/1.0'}),timeout=60) as f:b=f.read();r.update(status=f.status,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
   root=E.fromstring(b);article=root.find('.//article') if root.tag!='article' else root;meta=article.find('front/article-meta');assert any(x.text==doi for x in meta.findall('article-id'))
   selected={'doi':doi,'pmc':'PMC'+pmc,'title':txt(meta.find('title-group/article-title')),'publication_dates':[{**x.attrib,**{c.tag:txt(c) for c in x}} for x in meta.findall('pub-date')],'license_url':next((x.text for x in meta.findall('.//{http://www.niso.org/schemas/ali/1.0/}license_ref')),None)}
   r['selected_metadata']=selected
  except Exception as e:r['error']=str(e)
  r['completed_utc']=utc();records.append(r)
 (OUT/'primary-source-checks.json').write_text(json.dumps(records,indent=2,ensure_ascii=False)+'\n');print(json.dumps(records,indent=2,ensure_ascii=False))
if __name__=='__main__':main()
