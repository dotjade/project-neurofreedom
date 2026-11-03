"""Independent exact-rational verification; no import of production analysis."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,math
P=Path(__file__).resolve().parent
# Manually transcribed public abstract aggregates, checked 2026-11-03.
rows=[(43,24,28,F('71.8'),2,8),(21,14,10,F('52.6'),4,2)]
checks=[]
for total,start,end,percent,worse,better in rows:
    candidates=[n for n in range(1,total+1) if abs(F(100*end,n)-percent)<F(1,20)]
    checks.append({'compatible_denominators':candidates,'transition_conditional_final':start-worse+better,'conditional_difference':start-worse+better-end})
rd=F(28,39)-F(10,19)
out={'method':'Independent exact rational arithmetic; interior rounding bounds (no candidate at a tie)', 'arms':checks,'crude_exact':str(rd),'crude_float':float(rd),'crude_minus_reported':float(rd-F('0.17')),'lower_minus_margin':str(F('-.08')-F('-.32')),'ci_includes_zero':F('-.08')<0<F('.43'),'primary_p_25_gate_passed':F('.0755')<F('.05'),'primary_p_30_gate_passed':F('.0633')<F('.05')}
r=json.loads((P.parent/'results.json').read_text())
assert [a['compatible_denominators'] for a in checks]==[a['compatible_denominators'] for a in r['arms']]
assert [a['transition_conditional_final'] for a in checks]==[a['transition_implied_fit_if_same_complete_population'] for a in r['arms']]
assert math.isclose(float(rd),r['crude_difference_using_percentage_compatible_denominators'],abs_tol=1e-14)
assert math.isclose(float(rd-F('.17')),r['crude_minus_reported'],abs_tol=1e-14)
assert r['distance_lower_to_margin']==float(F('-.08')-F('-.32'))
assert r['reported_interval_includes_zero']==out['ci_includes_zero']
assert r['primary_gate_passed']==out['primary_p_25_gate_passed']
x=json.loads((P.parent/'inputs.json').read_text())
out['plan_hash_matches']=hashlib.sha256((P.parent/'plan.md').read_bytes()).hexdigest()==x['plan_sha256']
assert out['plan_hash_matches']
out['comparison_status']='All independent numeric comparisons passed'
(P/'verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
