#!/usr/bin/env python3
"""Reproduce the supplemental primary-source metadata reads used in this scan.

The live results are not frozen. Run: python scan_supplement.py --out PATH
No abstracts, full papers, individual case details or raw HTML/XML are persisted.
Web-search discovery queries and failed web-extractor attempts are in source-checks.json.
"""
import argparse, datetime as dt, hashlib, html, json, pathlib, re
import urllib.parse, urllib.request, xml.etree.ElementTree as ET

def utc(): return dt.datetime.now(dt.timezone.utc).isoformat()
def text(el): return ''.join(el.itertext()) if el is not None else ''

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out',default='.'); args=ap.parse_args()
    out=pathlib.Path(args.out); out.mkdir(parents=True,exist_ok=True)
    requests=[]
    def get(url,kind='json'):
        r={'url':url,'started_utc':utc()}
        try:
            req=urllib.request.Request(url,headers={'User-Agent':'PublicEvidenceScan/1.0'})
            with urllib.request.urlopen(req,timeout=30) as f: raw=f.read();r['status']=f.status
            r['sha256']=hashlib.sha256(raw).hexdigest()
            data=json.loads(raw) if kind=='json' else ET.fromstring(raw) if kind=='xml' else raw.decode('utf-8',errors='replace')
        except Exception as e:r['error']=str(e);data=None
        r['completed_utc']=utc();requests.append(r)
        return data,r
    registries=[]
    for nct in ['NCT05158439','NCT02119611','NCT07093541']:
        d,r=get('https://clinicaltrials.gov/api/v2/studies/'+nct)
        if d:
            p=d['protocolSection']
            registries.append(dict(id=nct,request=r,status=p.get('statusModule'),design=p.get('designModule'),hasResults=d.get('hasResults')))
    pub=[]
    url='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?'+urllib.parse.urlencode({'db':'pubmed','id':'42881067,42527169','retmode':'xml'})
    root,r=get(url,'xml')
    if root is not None:
        for a in root.findall('PubmedArticle'):
            pub.append({'pmid':text(a.find('MedlineCitation/PMID')),'title':text(a.find('MedlineCitation/Article/ArticleTitle')),
              'authors':[{'last_name':text(n.find('LastName')),'initials':text(n.find('Initials'))} for n in a.findall('MedlineCitation/Article/AuthorList/Author')],
              'identifiers':{n.get('IdType'):text(n) for n in a.findall('PubmedData/ArticleIdList/ArticleId')},
              'article_dates':[dict(n.attrib,**{c.tag:c.text for c in n}) for n in a.findall('MedlineCitation/Article/ArticleDate')],
              'history':{n.get('PubStatus'):{c.tag:c.text for c in n} for n in a.findall('PubmedData/History/PubMedPubDate')},
              'pubtypes':[text(n) for n in a.findall('MedlineCitation/Article/PublicationTypeList/PublicationType')],
              'corrections':[dict(n.attrib,pmid=text(n.find('PMID'))) for n in a.findall('MedlineCitation/CommentsCorrectionsList/CommentsCorrections')]})
    crossref=[]
    for doi in ['10.1016/j.therap.2026.08.002','10.1016/j.ijbiomac.2026.153656']:
        d,r=get('https://api.crossref.org/works/'+doi)
        if d:crossref.append({'request':r,'metadata':{k:d['message'].get(k) for k in ['DOI','title','published','published-online','published-print','created','deposited','indexed','type','relation','update-to','URL']}})
    publishers=[]
    for url in ['https://www.sciencedirect.com/science/article/pii/S0040595726000934','https://www.em-consulte.com/medecine/revue/THERAP/souspresse/therapies','https://www.sciencedirect.com/science/article/pii/S0141813026036019','https://www.em-consulte.com/article/1846440/behavioral-tics-following-sublingual-allergen-immu']:
        s,r=get(url,'text')
        z={'request':r}
        if s:
            z['title']=html.unescape((re.findall(r'<title[^>]*>(.*?)</title>',s,re.S|re.I) or [''])[0])
            z['citation_meta']=[html.unescape(n) for n in re.findall(r'<meta[^>]+>',s,re.I) if re.search(r'citation_(title|publication_date|online_date|doi|journal_title)',n)]
        publishers.append(z)
    (out/'supplement-reproduced-metadata.json').write_text(json.dumps({'requests':requests,'registry':registries,'pubmed':pub,'crossref':crossref,'publishers':publishers},indent=2)+'\n')

if __name__=='__main__': main()
