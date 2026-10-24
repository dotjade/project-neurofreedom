#!/usr/bin/env python3
"""Independent read-only verification; official XML is held in memory only.
Writes only aggregate tests/provenance to this review directory. Never infers model n.
"""
from fractions import Fraction
from pathlib import Path
import datetime as dt
import hashlib
import json
import re
import urllib.request
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent
SRC = HERE.parent / 'day24_adult'
inputs = json.loads((SRC / 'inputs.json').read_text())
results = json.loads((SRC / 'results.json').read_text())
temporal = json.loads((SRC / 'temporal-audit.json').read_text())
checks = []
def check(name, condition, evidence=None):
    checks.append({'name': name, 'passed': bool(condition), **({'evidence': evidence} if evidence is not None else {})})

def text(element):
    return ' '.join(''.join(element.itertext()).split()) if element is not None else ''

# No imports from the author's analysis: exact rational interval is independent
# of their Decimal.quantize implementation. Lower boundary included; upper excluded.
recomputed = []
for row in inputs['table1_percentages']:
    k = row['count']
    target = Fraction(row['percent'])
    candidates = [n for n in range(max(k, 1), 259)
                  if target - Fraction(1,20) <= Fraction(100*k,n) < target + Fraction(1,20)]
    stored = next(r for r in results['rounding_compatible_denominators'] if r['field'] == row['field'])
    missing = [258-n for n in candidates]
    check('exact rational denominators: '+row['field'], candidates == stored['candidates'], candidates)
    check('conditional complements: '+row['field'], missing == stored['conditional_missing_or_unknown_counts'], missing)
    check('conditional label: '+row['field'], 'NOT author-confirmed' in stored['status'])
    recomputed.append({'field':row['field'],'candidates':candidates,'conditional_complements':missing})
for label,k,n in [('response_of_invited',334,758),('complete_of_responded',292,334),('retained_of_complete',258,292),('retained_of_invited',258,758),('current_tics_in_retained',247,258),('current_reused_as_adult_worst',50,258)]:
    got = results['stage_proportions'][label]
    check('stage proportion: '+label, got == {'numerator':k,'denominator':n,'percent':round(float(Fraction(100*k,n)),6)})
check('stage differences', results['stage_differences']=={'did_not_respond':424,'responded_without_complete_tic_items':42,'excluded_after_tic_item_completeness':34})
check('flow partitions invited total', 424+42+34+258==758)
check('model n not inferred', all(x is None for x in results['model_counts'].values()) and all(temporal['model_documentation'][k]['n'] is None for k in ['tts','impairment']))
check('simulation absent',results['seed'] is None)

url='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=13680449&retmode=xml'
started=dt.datetime.now(dt.timezone.utc).isoformat()
with urllib.request.urlopen(url,timeout=60) as response:
    raw=response.read()
    status=response.status
root=ET.fromstring(raw)
article=root.find('.//article') if root.tag!='article' else root
ids={e.get('pub-id-type'):text(e) for e in article.findall('front/article-meta/article-id')}
check('official source identity',ids.get('doi')=='10.3389/fpsyt.2026.1948693' and ids.get('pmid')=='42903303' and ids.get('pmcid')=='PMC13680449')
source_hash=hashlib.sha256(raw).hexdigest()
check('same source version as audit',source_hash==json.loads((SRC/'source-provenance.json').read_text())['response_sha256'])
check('no XML supplementary-material element',len(article.findall('.//supplementary-material'))==0)
map1={'Sex':'male','Race':'white','Ethnicity':'non_hispanic','Current tic medication status':'current_medication','Tic disorder family history':'family_history','OCD status':'ocd','ADHD status':'adhd','Significant life event':'life_event'}
t1=article.find('.//table-wrap[@id="T1"]')
source_rows={}
for tr in t1.findall('.//tbody/tr'):
    cs=[text(x) for x in tr.findall('td')]
    if cs[0] in map1:
        m=re.search(r'(\d+) \(([\d.]+)%\)',cs[1])
        source_rows[map1[cs[0]]] = (int(m[1]),m[2])
for row in inputs['table1_percentages']:
    check('official Table 1 row: '+row['field'],source_rows[row['field']]==(row['count'],row['percent']))
check('Table 1 excludes missing or unknown', 'excluding missing/unknown values' in text(t1.find('caption')))

def section(sid):
    return article.find(f'.//sec[@id="{sid}"]')
def paragraphs(sid):
    return ' '.join(text(p) for p in section(sid).findall('p'))
participants=paragraphs('s2_1')
severity=paragraphs('s2_2_1')
comorbidity=paragraphs('s2_2_2')
clinical=paragraphs('s2_2_3')
events=paragraphs('s2_2_4')
statistics=paragraphs('s2_3')
sample=paragraphs('s3_1')
discussion=paragraphs('s4')
check('published recruitment stages',all(s in participants for s in ['758 adults','334 individuals','292 of 334','final sample of 258']))
check('current tic count',re.search(r'n\s*=\s*247',sample) is not None)
check('current score reused for 50', '50 participants' in severity and 'current YGTSS score was also used as their adult worst-ever score' in severity)
check('retrospective age periods', 'before age 18' in severity and 'childhood worst-ever' in severity and 'adulthood worst-ever' in severity)
check('lifetime OCD and ADHD designation','Lifetime diagnoses of OCD and ADHD' in comorbidity)
check('medication current at survey','currently taking medication for their tics' in clinical)
check('event contemporaneous not necessarily antecedent','at the time of their adulthood worst-ever tics' in events)
check('discussion childhood OCD wording exists','OCD, but not co-occurring ADHD, in childhood' in discussion)
check('authors acknowledge retrospective self report','retrospective reporting' in discussion and 'self-report data' in discussion)
check('ASD exclusion acknowledged','autism spectrum disorder (ASD)' in discussion)
check('selection rule p less than .1','p < 0.1' in statistics)
check('no explicit imputation or complete case rule in methods',re.search(r'\bimput\w*|complete[ -]case|listwise|na\.omit', text(section('s2')), re.I) is None)

# Table 4 rows have variable-width cells due to publisher rowspans.
# Read numeric tails and explicit outcome boundaries, without participant data.
model='tts'; parsed={'tts':{},'impairment':{}}
for tr in article.findall('.//table-wrap[@id="T4"]/table/tbody/tr'):
    cells=[text(c) for c in tr.findall('td')]
    if cells and cells[0]=='Adult worst-ever YGTSS-Impairment':model='impairment'
    label,estimate,se,t,p=cells[-5:]
    parsed[model][label]={'estimate':estimate,'p':p}
for model,label,p in [('tts','ADHD status','0.82'),('tts','Significant life event','0.098'),('impairment','OCD status','0.050'),('impairment','Current tic medication status','0.020'),('impairment','Significant life event','0.0078')]:
    check(f'official Table 4 p: {model} {label}',parsed[model][label]['p']==p,p)
check('medication coefficient',parsed['impairment']['Current tic medication status']['estimate']=='4.76')
map4={'OCD status':'ocd','ADHD status':'adhd','Significant life event':'life_event','Age':'age','Child worst-ever YGTSS-TTS':'childhood_worst_tts','Child worst-ever YGTSS-Impairment':'childhood_worst_impairment','Current tic medication status':'current_medication','Sex (male)':'sex'}
for model in parsed:
    actual=[map4[x] for x in parsed[model] if x!='Intercept']
    check('outcome predictor set: '+model,actual==temporal['model_documentation'][model]['predictors'],actual)
positive=[]
for tr in article.findall('.//table-wrap[@id="T5"]/table/tbody/tr'):
    cs=[text(c) for c in tr.findall('td')]
    if 'Event valence (Positive)' in cs:positive.append(cs[-1])
check('positive event nulls both outcomes',positive==['0.47','0.70'],positive)
check('boundary p preserved in temporal audit',temporal['model_documentation']['ocd_impairment_p_printed']=='0.050')
check('all source tables inspected',all(article.find(f'.//table-wrap[@id="T{i}"]') is not None for i in range(1,6)))

provenance={'url':url,'started_utc':started,'completed_utc':dt.datetime.now(dt.timezone.utc).isoformat(),'http_status':status,'response_bytes':len(raw),'response_sha256':source_hash,'identifiers':ids,'full_text_saved':False,'participant_data_or_figures_saved':False,'publisher_read':'Official Frontiers HTML via web tool; methods, Tables 1-5, discussion read','web_PMC_access_limit':'PMC HTML web.open failed with cache miss; official EFetch XML succeeded without bypass or escalation.'}
(HERE/'source-provenance.json').write_text(json.dumps(provenance,indent=2)+'\n')
summary={'passed':sum(c['passed'] for c in checks),'failed':sum(not c['passed'] for c in checks),'checks':checks,'independent_algorithm':'Exact Fraction interval [printed percent-0.05, printed percent+0.05), bounded integer denominator 1..258','conditional_denominators':recomputed,'model_n':{'tts':None,'impairment':None},'scope':'Published aggregate and documentation checks; not participant reconstruction, clinical validation, or a model-n derivation.'}
(HERE/'checks.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({'passed':summary['passed'],'failed':summary['failed'],'failures':[c for c in checks if not c['passed']]}))
assert not summary['failed']
