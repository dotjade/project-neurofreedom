"""Deterministic published-aggregate consistency audit; no participant data or RNG."""
import json
from decimal import Decimal
from pathlib import Path
P=Path(__file__).resolve().parent

def denominators(k, rounded_percent, maximum):
    # Printed percentages treated as nearest 0.1 percentage point, half-open envelope.
    lo=Decimal(str(rounded_percent))-Decimal('0.05')
    hi=Decimal(str(rounded_percent))+Decimal('0.05')
    return [n for n in range(k,maximum+1) if lo<=Decimal(100*k)/n<hi]

def calculate(x):
    arms=x['driving']['arms']; rows=[]
    for a in arms:
        ns=denominators(a['week13_fit'],a['week13_percent'],a['n'])
        transition=a['baseline_fit']-a['fit_to_unfit']+a['unfit_to_fit']
        rows.append({'arm':a['name'],'compatible_denominators':ns,'conditional_unrepresented_count':a['n']-ns[0] if len(ns)==1 else None,'transition_implied_fit_if_same_complete_population':transition,'reported_week13_fit':a['week13_fit'],'difference':transition-a['week13_fit']})
    n1,n0=(r['compatible_denominators'][0] for r in rows)
    crude=arms[0]['week13_fit']/n1-arms[1]['week13_fit']/n0
    lo,hi=x['driving']['reported_ci95']; margin=x['protocol']['margin']
    return {'kind':'Deterministic aggregate consistency checks, not simulation, statistical refit or clinical validation','arms':rows,'crude_difference_using_percentage_compatible_denominators':crude,'reported_difference':x['driving']['reported_rd'],'crude_minus_reported':crude-x['driving']['reported_rd'],'reported_interval_includes_zero':lo<=0<=hi,'reported_lower_above_margin':lo>margin,'distance_lower_to_margin':float(Decimal(str(lo))-Decimal(str(margin))),'primary_gate_passed':x['registry']['primary_superiority_p']<0.05,'confirmatory_noninferiority_established_under_published_hierarchy':False,'confirmatory_status_note':'Adjudicated from verified published hierarchy and failed primary gate; not a fitted statistical result','missingness_bounds_executed':False,'missingness_prerequisite':'Verified actual observed endpoint counts, analysis-set/transition definitions and imputation before interpreting percentage-compatible denominators as missing participants.'}

if __name__=='__main__':
    out=calculate(json.loads((P/'inputs.json').read_text()))
    (P/'results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
