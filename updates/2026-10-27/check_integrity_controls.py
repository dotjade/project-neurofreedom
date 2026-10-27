#!/usr/bin/env python3
"""Recheck known retraction metadata. No abstracts or case narratives retained."""
import datetime as dt,hashlib,json,pathlib,urllib.request,xml.etree.ElementTree as E
OUT=pathlib.Path(__file__).resolve().parent
def utc():return dt.datetime.now(dt.timezone.utc).isoformat()
def txt(x):return ''.join(x.itertext()) if x is not None else ''
def main():
 url='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=39947542,42527169&retmode=xml';log={'url':url,'started_utc':utc(),'records':[]}
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'PublicEvidenceScan/1.0'}),timeout=60)as f:b=f.read();log.update(status=f.status,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
  for art in E.fromstring(b).findall('PubmedArticle'):
   m=art.find('MedlineCitation');p=art.find('PubmedData');a=m.find('Article')
   log['records'].append({'pmid':txt(m.find('PMID')),'title':txt(a.find('ArticleTitle')),'types':[txt(x)for x in a.findall('PublicationTypeList/PublicationType')],'DateRevised':{c.tag:c.text for c in m.find('DateRevised')},'corrections':[dict(type=x.attrib.get('RefType'),source=txt(x.find('RefSource')),pmid=txt(x.find('PMID')))for x in m.findall('CommentsCorrectionsList/CommentsCorrections')]})
 except Exception as e:log['error']=str(e)
 log['completed_utc']=utc();(OUT/'integrity-control-source.json').write_text(json.dumps(log,indent=2)+'\n');print(json.dumps(log,indent=2))
if __name__=='__main__':main()
