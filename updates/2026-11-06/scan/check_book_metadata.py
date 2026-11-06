"""Retrieve metadata only for a PubMed book record omitted by journal-only parser."""
import datetime as dt,hashlib,json,pathlib,urllib.request,xml.etree.ElementTree as E
p=pathlib.Path(__file__).resolve().parent
u='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=23556151&retmode=xml'
now=lambda:dt.datetime.now(dt.timezone.utc).isoformat()
rec={'url':u,'started_utc':now()}
with urllib.request.urlopen(u,timeout=60)as r:b=r.read();rec.update(status=r.status,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
root=E.fromstring(b);a=root.find('PubmedBookArticle');d=a.find('BookDocument')
txt=lambda x:''.join(x.itertext())if x is not None else ''
date=lambda x:{c.tag:c.text for c in x}if x is not None else None
x={'pmid':txt(d.find('PMID')),'title':txt(d.find('ArticleTitle')),'book_title':txt(d.find('Book/BookTitle')),'types':[txt(t)for t in d.findall('PublicationType')],'journal_pubdate':date(d.find('Book/PubDate')),'article_dates':[dict(type=t.attrib.get('DateType'),**date(t))for t in d.findall('ContributionDate')],'history':{t.attrib.get('PubStatus'):date(t)for t in a.findall('PubmedBookData/History/PubMedPubDate')},'identifiers':{t.attrib.get('IdType'):txt(t)for t in d.findall('ArticleIdList/ArticleId')},'source_url':'https://pubmed.ncbi.nlm.nih.gov/23556151/','record_type':'PubmedBookArticle','prior_scan_overlap':False,'abstract_retained':False,'screening_decision':'Secondary GeneReviews chapter about Coffin-Siris syndrome, not new primary Tourette evidence.','qualifying_primary_publication':False,'corrections':[]}
rec['completed_utc']=now();(p/'book-metadata.json').write_text(json.dumps({'request':rec,'record':x},indent=2)+'\n');print(json.dumps(x,indent=2))
