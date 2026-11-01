"""Independent deterministic weekly verification; no source code imported."""
import json
from decimal import Decimal as D
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'analyses/force_matching_reliability/2026-11-01/aggregate-inputs.json'
a=json.loads(p.read_text(),parse_float=D)
t=a['table4_mean_error_N']
means={k:[sum((row[j] for row in v),D(0))/D(4) for j in (2,3)] for k,v in t.items()}
c=[means['direct'][i]-means['slider'][i] for i in range(2)]
assert c==[D('.8925'),D('.7725')]
assert c[1]-c[0]==D('-.1200')
per=[(t['direct'][i][3]-t['slider'][i][3])-(t['direct'][i][2]-t['slider'][i][2]) for i in range(4)]
assert per==[D('-.06'),D('-.12'),D('-.15'),D('-.15')]
assert sum(per)/D(4)==c[1]-c[0]
assert D('.02')<abs(c[1]-c[0])
assert len(a['split_half_spearman_brown']['direct'])==4
assert a['split_half_spearman_brown']['direct'][-1]==D('.94')
assert a['split_half_spearman_brown']['slider'][-1]==D('.86')
out={'scope':'Independent verification, not a new result or clinical replication','source_input':str(p.relative_to(ROOT)),'mean_error_N':{k:list(map(str,v)) for k,v in means.items()},'contrasts_N':list(map(str,c)),'change_N':str(c[1]-c[0]),'per_force_change_N':list(map(str,per)),'assertions':8,'seed':None,'limitation':'No independent re-extraction of primary table in this script; published aggregate input and earlier source review reused. No patient data, sampling interval or hypothesis test.'}
print(json.dumps(out,indent=2))
