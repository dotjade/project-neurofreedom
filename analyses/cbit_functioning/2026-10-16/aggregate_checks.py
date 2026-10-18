"""Deterministic, aggregate-only audit. Run: python aggregate_checks.py.
No packages, data downloads, random simulation or participant-level inference.
"""
import json
from decimal import Decimal as D
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def adjust(ps):
    """Holm and Bonferroni adjusted p-values; ps is a mapping of IDs to Decimal."""
    ordered=sorted(ps,key=lambda k:(ps[k],k)); m=len(ordered); maximum=D(0)
    holm={}
    for i,k in enumerate(ordered):
        maximum=max(maximum,min(D(1),D(m-i)*ps[k]));holm[k]=maximum
    return {'holm':holm,'bonferroni':{k:min(D(1),D(m)*p) for k,p in ps.items()}}

def mean(row,key):return D(row[key]['mean'])

def compute(data):
    result={'purpose':'Post hoc restricted-family sensitivity and reporting audit, not a clinical reanalysis or confirmatory test. Printed p-values are rounded.','random_seed':None,'families':{},'denominator_audit':{},'limits':['No outcome-specific denominators or F degrees of freedom reconstructed.','No within-person covariance, precision interval, equivalence margin, clinical threshold or missing outcomes invented.','Separate families do not adjust all tests in this report, and cannot repair postrandomization selection.']}
    for name in ('acute_randomized','acute_responder_association','selected_cbit_followup'):
        rows=data[name];ps={r['id']:D(r['p']) for r in rows if r['p'] is not None}; corrections=adjust(ps)
        details=[]
        for row in rows:
            k=row['id'];entry={'id':k,'printed_p':row['p']}
            if k in ps:
                entry.update({method:str(values[k]) for method,values in corrections.items()})
            if name=='acute_randomized':
                c=mean(row,'cbit_post')-mean(row,'cbit_baseline');p=mean(row,'pst_post')-mean(row,'pst_baseline')
                entry['displayed_mean_arithmetic']={'cbit_change':str(c),'pst_change':str(p),'cbit_minus_pst_change':str(c-p),'negative_contrast_favors':'CBIT, descriptively only; not a reconstructed model estimate'}
            elif name=='acute_responder_association':
                r=mean(row,'responder_post')-mean(row,'responder_baseline');n=mean(row,'nonresponder_post')-mean(row,'nonresponder_baseline')
                entry['displayed_mean_arithmetic']={'responder_change':str(r),'nonresponder_change':str(n),'responder_minus_nonresponder_change':str(r-n),'causal_interpretation':False}
            elif row.get('analysis_n') != 1:
                entry['displayed_mean_arithmetic']={'post_minus_baseline':str(mean(row,'post')-mean(row,'baseline')),'month6_minus_baseline':str(mean(row,'month6')-mean(row,'baseline')),'causal_interpretation':False}
            details.append(entry)
        result['families'][name]={'m':len(ps),'printed_p_range':[str(min(ps.values())),str(max(ps.values()))],'nominal_ids':[k for k,p in ps.items() if p<D('.05')],'holm_below_05':[k for k,p in corrections['holm'].items() if p<D('.05')],'bonferroni_below_05':[k for k,p in corrections['bonferroni'].items() if p<D('.05')],'untested_ids':[r['id'] for r in rows if r['p'] is None],'details':details}
    n=data['denominators']
    result['denominator_audit']={'randomized_total':n['randomized_cbit']+n['randomized_pst'],'acute_analyzed_figure_total':n['figure_acute_analyzed_cbit']+n['figure_acute_analyzed_pst'],'acute_completed_total':n['acute_completed_cbit']+n['acute_completed_pst'],'figure_screened_minus_excluded':n['figure_screened']-n['figure_excluded'],'figure_randomized_reported':n['figure_randomized'],'figure_flow_difference':n['figure_randomized']-(n['figure_screened']-n['figure_excluded']),'pst_followup_prose':n['pst_followup_prose'],'pst_followup_figure':n['pst_followup_figure'],'correction_inferred':False}
    return result

if __name__=='__main__':
    data=json.loads((ROOT/'aggregate_inputs.json').read_text());result=compute(data)
    (ROOT/'aggregate_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print('Deterministic aggregate audit completed.')
    for name,family in result['families'].items():print(name, 'tests=',family['m'],'nominal=',len(family['nominal_ids']),'Holm=',len(family['holm_below_05']),'Bonferroni=',len(family['bonferroni_below_05']))
    print('No clinical uncertainty interval or participant data analysis performed.')
