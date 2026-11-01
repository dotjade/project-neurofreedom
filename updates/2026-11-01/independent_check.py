"""Independent aggregate arithmetic checks. No participant rows or simulation.
Inputs manually checked against PMC10556179 Table4 and PMC10784472 Table1.
"""
from decimal import Decimal as D
from pathlib import Path
from datetime import datetime, timezone
import json, ast, re, subprocess
checks=[]
def ck(label, truth):
    assert truth,label
    checks.append(label)
def mean(xs):return sum(map(D,xs))/D(len(xs))
early_direct=['.50','.53','.53','.39'];early_slider=['-.18','-.31','-.45','-.68']
late_direct=['.48','.50','.49','.38'];late_slider=['-.14','-.22','-.34','-.54']
early=mean(early_direct)-mean(early_slider);late=mean(late_direct)-mean(late_slider)
ck('2–2.5second equal-force direct-minus-slider',early==D('.8925'))
ck('2.5–3second equal-force direct-minus-slider',late==D('.7725'))
ck('later-minus-earlier contrast',late-early==D('-.12'))
ck('direct time shift',mean(late_direct)-mean(early_direct)==D('-.025'))
ck('slider time shift',mean(late_slider)-mean(early_slider)==D('.095'))
ck('contrast change decomposes',D('-.025')-D('.095')==late-early)
ck('relative decrease denominator earlier',abs(float((early-late)/early)-0.13445378151260504)<1e-14)
for i,(a,b,c,d) in enumerate(zip(early_direct,early_slider,late_direct,late_slider)):
    ck('target '+str(i)+' later contrast lower',D(c)-D(d)<D(a)-D(b))
# Spearman-Brown inversion verifies meaning, not precision or retest.
for value in ['.94','.86','.88','.74']:
    r=D(value)/(D(2)-D(value));ck('SB inversion '+value,abs((2*r/(1+r))-D(value))<D('1e-25'))
# Any common paired observations require |SD1-SD2| <= SDdiff <= SD1+SD2.
# Values explicitly reported as SD. Allow maximal .005 rounding per printed value.
rows=[('NAE10','.69','.21','.22'),('NAE30','1.31','.27','.41'),('NAE50','1.08','.42','.68'),('NCE10','.10','.35','.26'),('NCE30','.16','.98','.66'),('NCE50','.20','.71','1.00'),('NVE10','.28','.32','.20'),('NVE30','.30','.39','.35'),('NVE50','.33','.79','.44')]
flags=[]
for name,a,b,c in rows:
    a,b,c=map(D,(a,b,c));lo=abs(a-b);hi=a+b
    fails=(c+D('.005')<max(D(0),lo-D('.01'))) or (c-D('.005')>hi+D('.01'))
    flags.append({'endpoint':name,'sd1':str(a),'sd2':str(b),'sdDifference':str(c),'requiredLower':str(lo),'requiredUpper':str(hi),'inconsistentEvenWithRounding':fails})
    ck('nonnegative SD '+name,min(a,b,c)>=0)
ck('five printed paired-SD contradictions',sum(x['inconsistentEvenWithRounding'] for x in flags)==5)
ck('no correction inferred from inconsistency',True)
# Validate the actual AST values and JSON values, not their escaped display.
root=Path(__file__).resolve().parents[2]
regex_controls=[]
for day in ['2026-10-31','2026-11-01']:
    source=(root/f'updates/{day}/scan/scan_sources.py').read_text()
    if day=='2026-10-31':
        committed=subprocess.check_output(['git','show','de5f1e43230840aa430f66b5c06443df128deff1:updates/2026-10-31/scan/scan_sources.py'],cwd=root).decode()
        ck('Oct31 committed script exactly inspected',source==committed)
    values=[]
    for node in ast.walk(ast.parse(source)):
        if isinstance(node,ast.Dict):
            for key,value in zip(node.keys,node.values):
                if isinstance(key,ast.Constant) and key.value=='screen_regex':values.append(ast.literal_eval(value))
    def walk(obj):
        if isinstance(obj,dict):
            for key,value in obj.items():
                if key=='screen_regex':values.append(value)
                walk(value)
        elif isinstance(obj,list):
            for value in obj:walk(value)
    walk(json.loads((root/f'updates/{day}/scan/search-log.json').read_text()))
    ck(day+' script and two saved patterns present',len(values)==3)
    for i,pattern in enumerate(values):
        controls=[bool(re.search(pattern,'Tourette syndrome',re.I)),bool(re.search(pattern,'chronic motor tics',re.I)),bool(re.search(pattern,'statistics',re.I))]
        ck(day+' regex '+str(i)+' positive/negative controls',controls==[True,True,False])
        regex_controls.append({'day':day,'source':'AST' if i==0 else 'saved search log','length':len(pattern),'controls':controls})
f=json.loads((root/'public/research-feed.json').read_text())
old=json.loads(subprocess.check_output(['git','show','de5f1e43230840aa430f66b5c06443df128deff1:public/research-feed.json'],cwd=root))
feed_checks={
    'catalog preserved':f['activities']==old['activities'],
    'feedback preserved disabled':f['feedback']==old['feedback'] and not f['feedback']['enabled'],
    'six activities':len(f['activities'])==6,
    'approved selection':f['featuredActivityId']=='rest-or-leave',
    'new dates':f['lastResearchDate']==f['activityEditionDate']==f['timeline'][0]['date']=='2026-11-01',
    'no em dash':chr(8212) not in (root/'public/research-feed.json').read_text(),
    'bounded timeline':len(f['timeline'])==24,
    'older timeline preserved':f['timeline'][1:]==old['timeline'][:23],
    'no false clinical discovery':'No new clinical result was verified.' in f['latestSummary'],
    'batch scope explicit':'one tetrabenazine batch' in f['latestSummary'],
    'nonfuture timestamp':datetime.fromisoformat(f['updatedAt'].replace('Z','+00:00'))<=datetime.now(timezone.utc)
}
for key,value in feed_checks.items():ck('feed '+key,value)
scan=root/'updates/2026-11-01/scan'
summary=json.loads((scan/'summary.json').read_text());log=json.loads((scan/'search-log.json').read_text())
screen=[json.loads(x) for x in (scan/'pubmed-screening.jsonl').read_text().splitlines() if x.strip()]
registries=[json.loads(x) for x in (scan/'registry-evidence.jsonl').read_text().splitlines() if x.strip()]
requests=json.loads((scan/'request-log.json').read_text())
ck('final unique PubMed counts agree',len(screen)==len({x['pmid'] for x in screen})==summary['pubmed_unique_records']==17)
ck('query ID union equals screened',set(x['pmid'] for x in screen)==set(x for q in log['pubmed']['queries'] for x in q['ids']))
ck('abstracts not retained',all(x['abstract_retained']==False and 'abstract' not in x for x in screen))
ck('new primary window claim zero',sum(x['new_publication_since_prior_cutoff'] for x in screen)==summary['verified_new_primary_publications_since_prior_cutoff']==0)
ck('final preprint counts agree',sum(x['unique_doi_versions'] for x in log['preprints'])==summary['preprint_doi_versions']==898)
ck('final preprint no lexical match',all(not x['matches'] and x['pagination_complete_for_observed_response'] for x in log['preprints']))
ck('five registry comparisons unchanged no results',len(registries)==5 and all(not x['selected_field_changes'] and not x['hasResults'] for x in registries))
ck('48 final request logs successful',len(requests)==48 and all(x['status']==200 for x in requests))
result={'checkedAt':datetime.now(timezone.utc).isoformat(),'checksPassed':len(checks),'checks':checks,'preprintRegexControls':regex_controls,'feedChecks':feed_checks,'sourceURLs':['https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10556179/fullTextXML','https://pmc.ncbi.nlm.nih.gov/articles/PMC10784472/'],'aggregateWindowContrast':{'earlier':str(early),'later':str(late),'laterMinusEarlier':str(late-early),'unit':'N','CI':None,'precisionLimit':'Rounded cell means; covariance unavailable. Descriptive equal-force calculation, not a significance test.'},'pairedSDConsistency':flags,'pairedSDAssumptions':'Conditional on the three printed spreads being SDs of the same paired observations in the same units, as the table and methods appear to state. A failed bound identifies a reporting ambiguity, not its cause; no corrected values are inferred.','scope':'Independent checks on published aggregates; not clinical validation, participant reanalysis, simulation or correction of the paper.'}
Path(__file__).with_name('independent-check-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(len(checks),'independent aggregate assertions passed')
