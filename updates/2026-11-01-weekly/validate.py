import json,hashlib,re,subprocess
from pathlib import Path
R=Path(__file__).resolve().parents[2]
A=R/'analyses/canna_function/2026-11-01'
count=0
def check(x):
 global count
 assert x
 count+=1
for p in [*A.rglob('*.json'),*Path(__file__).parent.glob('*.json')]:
 if p.name=='validation.json': continue
 json.loads(p.read_text());check(True)
a=json.loads((A/'inputs.json').read_text());o=json.loads((A/'results.json').read_text())
check(hashlib.sha256((A/'plan.md').read_bytes()).hexdigest()==a['plan_hash'])
check(o['functional_intervals_including_zero']==5)
check(o['functional_rounding_compatible_rows']==4)
check(a['study']['doi']=='10.1016/j.psychres.2023.115135')
check(a['primary']['paper_ci95']==[-.28,.01]);check(a['primary']['registry_ci95']==[-.2688,.0131])
check('visually verified' in (A/'report.md').read_text())
check('SOURCE_TO_INSERT' not in (A/'report.md').read_text())
s=(R/'updates/2026-11-01-weekly-synthesis.md').read_text()
check('RESULTS_TO_INSERT' not in s);check('NEXT_TO_INSERT' not in s)
check('Help needed from the owner: none' in s)
for p in [A/'report.md',R/'updates/2026-11-01-weekly-synthesis.md']:
 for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if not re.match(r'https?://',link): check((p.parent/link).exists())
base=subprocess.check_output(['git','show','HEAD:public/research-feed.json'],cwd=R)
check(base==(R/'public/research-feed.json').read_bytes())
check(not list(A.rglob('*.pdf')));check(not list(A.rglob('*.png')))
rs=[json.loads(l) for l in (R/'evidence.jsonl').read_text().splitlines() if l]
check(sum(x.get('pmid')=='36878177' for x in rs)==1)
print(json.dumps({'checks_passed':count,'scope':'Documentation, links, input identity, no paper images and unchanged feed; not clinical validation'},indent=2))
