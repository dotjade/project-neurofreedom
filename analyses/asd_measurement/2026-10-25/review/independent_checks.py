#!/usr/bin/env python3
"""Independent aggregate/source audit; retains no article body or participant data."""
import pathlib,urllib.request,xml.etree.ElementTree as E,json,datetime as dt,hashlib,re,subprocess,tempfile,shutil
from decimal import Decimal
P=pathlib.Path(__file__).resolve().parent
A=P.parent if (P.parent/'inputs.json').exists() else P.parent/'day25_asd'
def txt(e): return ' '.join(''.join(e.itertext()).split()) if e is not None else ''
url='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=13683974&retmode=xml'
start=dt.datetime.now(dt.timezone.utc).isoformat()
with urllib.request.urlopen(url,timeout=60) as f:body=f.read();status=f.status
root=E.fromstring(body);article=root.find('.//article');meta=article.find('front/article-meta');ids={e.get('pub-id-type'):txt(e) for e in meta.findall('article-id')}
tables={txt(t.find('label')):t for t in article.findall('.//table-wrap')}
rows={k:[[txt(c) for c in tr if c.tag in ['td','th']] for tr in t.findall('.//tr')] for k,t in tables.items()}
x=json.loads((A/'inputs.json').read_text());r=json.loads((A/'results.json').read_text());checks=[]
def ck(n,c):checks.append({'check':n,'passed':bool(c)});assert c,n
ck('DOI identity',ids['doi']==x['study']['doi']);ck('PMID identity',ids['pmid']==x['study']['pmid']);ck('PMC identity',ids.get('pmc')==x['study']['pmc'] or ids.get('pmcid')==x['study']['pmc'])
for label,selected in x['selected_source_cells'].items():
 for row in selected: ck(label+' '+row[0]+' exact cell',row in rows[label])
for label,key in [('Total tic score','tic_severity'),('Impairment','impairment')]:
 row=next(z for z in rows['TABLE 2'] if z and z[0]==label)
 n=Decimal(re.match(r'[\d.]+',row[1])[0]);a=Decimal(re.match(r'[\d.]+',row[2])[0]);ck(key+' contrast independent',float(a-n)==r['comparisons'][key]['unadjusted_asd_minus_non_asd']);ck(key+' unadjusted p',float(row[3])==x['unadjusted'][key]['p'])
row=next(z for z in rows['TABLE 3'] if z and z[0]=='Autism spectrum disorder')
for k,index in [('impairment',1),('tic_severity',3)]:
 nums=[float(t) for t in re.findall(r'-?\d+\.\d+',row[index].replace('−','-'))];ck(k+' beta CI',nums==[x['adjusted'][k]['beta']]+x['adjusted'][k]['ci']);ck(k+' adjusted p',float(row[index+1].replace('*',''))==x['adjusted'][k]['p'])
foot=txt(tables['TABLE 3'])
ck('model counts in source',bool(re.search(r'Impairment: n\s*=\s*483',foot)) and bool(re.search(r'Tic severity: n\s*=\s*485',foot)))
for k,n in [('impairment',483),('tic_severity',485)]:
 ck(k+' missing count',r['model_coverage'][k]['not_in_model']==535-n);ck(k+' coverage',r['model_coverage'][k]['fraction_of_total']==n/535)
ck('overlap union bound',r['model_overlap_bounds']['minimum']==483+485-535)
ck('overlap subset bound',r['model_overlap_bounds']['maximum']==min(483,485))
ck('support3 proportion',r['support_level3_fraction_of_asd']==3/49)
ck('no simulated observations',r['seed'] is None)
supp=[txt(z) for z in article.findall('.//supplementary-material')];ck('only disclosure supplement',len(supp)==1 and 'Disclosure Statement' in supp[0])
# Tests in a disposable copy ensure parent outputs are untouched.
with tempfile.TemporaryDirectory() as d:
 q=pathlib.Path(d)
 for name in ['inputs.json','results.json','analyze.py','check_analysis.py','prediction.md','report.md','source-provenance.json']:shutil.copyfile(A/name,q/name)
 result=subprocess.run(['python',str(q/'check_analysis.py')],capture_output=True,text=True)
 ck('parent30 checks reproduced',result.returncode==0 and '30 checks passed' in result.stdout)
 ck('output bytes independently rerun',(q/'results.json').read_bytes()==(A/'results.json').read_bytes())
ck('overlap wording correction read back','At least two model-inclusion statuses differ because the counts differ' in (A/'report.md').read_text())
(P/'checks.json').write_text(json.dumps({'passed':len(checks),'checks':checks},indent=2)+'\n')
(P/'source-provenance.json').write_text(json.dumps({'source_url':url,'started_utc':start,'completed_utc':dt.datetime.now(dt.timezone.utc).isoformat(),'http_status':status,'response_sha256':hashlib.sha256(body).hexdigest(),'response_bytes':len(body),'article_body_retained':False,'participant_data_accessed':False,'identifiers':ids,'supplement_inventory':supp},indent=2)+'\n')
(P/'reviewed-file-hashes.json').write_text(json.dumps({f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in A.iterdir() if f.is_file()},indent=2)+'\n')
print(len(checks),'independent checks passed')
