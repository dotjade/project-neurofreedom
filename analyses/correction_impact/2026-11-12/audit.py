#!/usr/bin/env python3
"""Current metadata and fixed-baseline dependency audit. No paper text or clinical data saved."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,subprocess,urllib.request,xml.etree.ElementTree as E
p=Path(__file__).resolve().parent;r=p.parents[2];BASE='4894c40b9da2714730fb50d5730bea6e3fc92608'
def git(*args):return subprocess.check_output(['git',*args],cwd=r)
def write(n,x):(p/n).write_text(json.dumps(x,indent=2)+'\n')
url='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=40680639,42767894&retmode=xml'
raw=urllib.request.urlopen(url,timeout=20).read();meta=[]
for a in E.fromstring(raw).findall('PubmedArticle'):
 meta.append({'pmid':a.findtext('./MedlineCitation/PMID'),'title':''.join(a.find('./MedlineCitation/Article/ArticleTitle').itertext()),'ids':{x.get('IdType'):x.text for x in a.findall('./PubmedData/ArticleIdList/ArticleId')},'dates':[{**{'type':x.get('DateType')},**{z.tag:z.text for z in x}} for x in a.findall('./MedlineCitation/Article/ArticleDate')],'types':[x.text for x in a.findall('./MedlineCitation/Article/PublicationTypeList/PublicationType')],'corrections':[{'type':x.get('RefType'),'pmid':x.findtext('PMID')} for x in a.findall('./MedlineCitation/CommentsCorrectionsList/CommentsCorrections')],'has_abstract':a.find('./MedlineCitation/Article/Abstract') is not None})
write('metadata.json',{'retrieved_utc':datetime.now(timezone.utc).isoformat(),'url':url,'response_sha256':hashlib.sha256(raw).hexdigest(),'records':meta,'scope':'Only top-level article identifiers; reference-list IDs and full abstracts excluded.'})
pattern=re.compile(r'40680639|42767894|10\.1016/j\.nicl\.2025\.103844|10\.1016/j\.nicl\.2026\.104054|temporal disintegration|\bWendiggensen\b|\bYifan Hao\b',re.I)
broad=re.compile(r'sensorimotor integration|event.file|\bHao\b',re.I)
paths=git('ls-tree','-r','--name-only',BASE).decode().splitlines();hits=[];bh=[];text_count=0;skip=[]
for path in paths:
 try:s=git('show',f'{BASE}:{path}').decode('utf-8')
 except UnicodeDecodeError:skip.append(path);continue
 text_count+=1
 lines=[i for i,line in enumerate(s.splitlines(),1) if pattern.search(line)]
 if lines:hits.append({'path':path,'lines':lines})
 if path.endswith('.md') or path in ['evidence.jsonl','public/research-feed.json']:
  lines=[i for i,line in enumerate(s.splitlines(),1) if broad.search(line)]
  if lines:bh.append({'path':path,'lines':lines})
write('dependencies.json',{'baseline_commit':BASE,'checked_at_utc':datetime.now(timezone.utc).isoformat(),'tracked_files':len(paths),'utf8_files_searched':text_count,'non_utf8_skipped':skip,'exact_pattern':pattern.pattern,'exact_hits':hits,'broader_pattern':broad.pattern,'broader_hits':bh,'interpretation':'Manual review is required; this is not an automatic classifier of scientific claims.'})
by={a['pmid']:a for a in meta};checks={
'original_ids':by['40680639']['ids']['pubmed']=='40680639' and by['40680639']['ids']['doi']=='10.1016/j.nicl.2025.103844' and by['40680639']['ids']['pmc']=='PMC12296559',
'notice_ids':by['42767894']['ids']['pubmed']=='42767894' and by['42767894']['ids']['doi']=='10.1016/j.nicl.2026.104054',
'original_date':{'type':'Electronic','Year':'2025','Month':'07','Day':'13'} in by['40680639']['dates'],
'notice_date':{'type':'Electronic','Year':'2026','Month':'09','Day':'21'} in by['42767894']['dates'],
'original_link':{'type':'ErratumIn','pmid':'42767894'} in by['40680639']['corrections'],
'notice_link':{'type':'ErratumFor','pmid':'40680639'} in by['42767894']['corrections'],
'notice_type':'Published Erratum' in by['42767894']['types'],
'no_notice_abstract':not by['42767894']['has_abstract'],
'all_baseline_files':len(paths)==text_count==1699 and not skip,
'six_scan_only_hits':len(hits)==6 and all(x['path'].startswith('updates/2026-11-11/scan/') for x in hits),
'one_broader_paragraph':len(bh)==1 and bh[0]['path']=='analyses/causal_synthesis/2026-10-28/critique/critical-synthesis.md'}
assert all(checks.values()),checks
write('validation.json',{'checked_at_utc':datetime.now(timezone.utc).isoformat(),'checks':checks,'all_pass':True,'scope':'Metadata identifiers/dates and dependency accounting only, not inaccessible notice-content verification.'})
print(json.dumps({'metadata':meta,'tracked_files':text_count,'hits':hits,'broader_hits':bh,'checks_passed':len(checks)},indent=2))
