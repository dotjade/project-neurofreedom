#!/usr/bin/env python3
"""Deterministic aggregate arithmetic, not simulation, clinical prediction or patient analysis."""
from decimal import Decimal, ROUND_HALF_UP
import hashlib,json,pathlib
P=pathlib.Path(__file__).resolve().parent
def pct(k,n):return round(100*k/n,6)
def calculate(d):
 s=d['stages']; out={'analysis_type':'published-aggregate documentation arithmetic; not simulation','seed':None,'stage_proportions':{}}
 for label,k,n in [('response_of_invited',s['responded'],s['invited']),('complete_of_responded',s['complete_tic_items'],s['responded']),('retained_of_complete',s['retained'],s['complete_tic_items']),('retained_of_invited',s['retained'],s['invited']),('current_tics_in_retained',s['current_tics'],s['retained']),('current_reused_as_adult_worst',s['current_as_adult_worst'],s['retained'])]:
  out['stage_proportions'][label]={'numerator':k,'denominator':n,'percent':pct(k,n)}
 out['stage_differences']={'did_not_respond':s['invited']-s['responded'],'responded_without_complete_tic_items':s['responded']-s['complete_tic_items'],'excluded_after_tic_item_completeness':s['complete_tic_items']-s['retained']}
 out['rounding_compatible_denominators']=[]
 for row in d['table1_percentages']:
  k=row['count']; target=Decimal(row['percent'])
  candidates=[n for n in range(k,s['retained']+1) if (Decimal(100)*k/n).quantize(Decimal('0.1'),rounding=ROUND_HALF_UP)==target]
  out['rounding_compatible_denominators'].append({**row,'candidates':candidates,'conditional_missing_or_unknown_counts':[s['retained']-n for n in candidates],'status':'conditional arithmetic, NOT author-confirmed denominator or regression sample'})
 out['model_counts']=d['model_counts'];out['no_model_n_inferred']=True
 out['interpretation_limits']=['Rounding assumption may be wrong; percentages may contain errors.','Single-variable denominators do not reveal joint overlap, outcome availability, imputation or regression n.','Retained sample is selected, not a population persistence denominator.','No inference of missing-at-random, exposure order, predictive performance or treatment harm.']
 return out
if __name__=='__main__':
 d=json.loads((P/'inputs.json').read_text());out=calculate(d)
 (P/'results.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
