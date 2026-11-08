"""Read public metadata only to resolve date/source-type leads; no participant data."""
import urllib.request,urllib.parse,json,datetime,hashlib,pathlib,xml.etree.ElementTree as E
P=pathlib.Path(__file__).parent
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def txt(e):return ''.join(e.itertext()) if e is not None else ''
url='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?'+urllib.parse.urlencode(dict(db='pubmed',id='42991793,42995077',retmode='xml'))
r={'url':url,'started_utc':now()}
try:
 with urllib.request.urlopen(url,timeout=45) as f:raw=f.read();r.update(status=f.status,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
 root=E.fromstring(raw);r['records']=[]
 for a in root.findall('PubmedArticle'):
  m=a.find('MedlineCitation');art=m.find('Article');pd=a.find('PubmedData')
  r['records'].append({'pmid':txt(m.find('PMID')),'title':txt(art.find('ArticleTitle')),'journal':txt(art.find('Journal/Title')),'types':[txt(x) for x in art.findall('PublicationTypeList/PublicationType')],'ids':{x.attrib.get('IdType'):txt(x) for x in pd.findall('ArticleIdList/ArticleId')},'article_dates':[dict(x.attrib,**{c.tag:c.text for c in x}) for x in art.findall('ArticleDate')],'corrections':[dict(x.attrib,source=txt(x.find('RefSource')),pmid=txt(x.find('PMID'))) for x in m.findall('CommentsCorrectionsList/CommentsCorrections')],'abstract_available':art.find('Abstract') is not None})
except Exception as e:r['error']=str(e)
r['completed_utc']=now();(P/'supplement-pubmed.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
