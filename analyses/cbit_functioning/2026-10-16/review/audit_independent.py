#!/usr/bin/env python3
"""Offline Decimal audit of independently extracted printed functional data.
Outputs restricted-family post-hoc sensitivity, not a new clinical analysis.
No covariance, outcome n, F-test degrees of freedom or CIs are reconstructed.
"""
import json
from decimal import Decimal as D
from pathlib import Path
HERE=Path(__file__).parent
GROUPS=('acute_randomized','acute_responder_association','selected_cbit_followup')

def adjust(rows):
    ps=[(row['id'],D(row['p'])) for row in rows if row['p'] is not None]
    m=len(ps); sorted_ps=sorted(ps,key=lambda x:x[1]); running=D(0); ans={}
    for rank,(key,p) in enumerate(sorted_ps):
        running=max(running,min(D(1),(m-rank)*p))
        ans[key]={'printed_p':str(p),'holm':str(running),'bonferroni':str(min(D(1),m*p))}
    return {'tested_rows':m,'nominal_significant':sum(p<D('.05') for _,p in ps),'holm_significant':sum(D(v['holm'])<D('.05') for v in ans.values()),'bonferroni_significant':sum(D(v['bonferroni'])<D('.05') for v in ans.values()),'p_min':str(min(p for _,p in ps)),'p_max':str(max(p for _,p in ps)),'adjusted':ans}

def change(row,a,b):return D(row[b]['mean'])-D(row[a]['mean'])

def main():
    data=json.loads((HERE/'independent_inputs.json').read_text()); result={k:adjust(data[k]) for k in GROUPS}
    assert [result[k]['tested_rows'] for k in GROUPS]==[12,12,11]
    assert [result[k]['nominal_significant'] for k in GROUPS]==[0,2,2]
    assert [result[k]['holm_significant'] for k in GROUPS]==[0,0,0]
    # synthetic independent routine checks, not biological simulation
    test=adjust([{'id':'A','p':'.01'},{'id':'B','p':'.04'},{'id':'C','p':'.03'}])
    assert test['adjusted']=={'A':{'printed_p':'0.01','holm':'0.03','bonferroni':'0.03'},'C':{'printed_p':'0.03','holm':'0.06','bonferroni':'0.09'},'B':{'printed_p':'0.04','holm':'0.06','bonferroni':'0.12'}}
    result['acute_displayed_mean_contrasts']={r['id']:str(change(r,'cbit_baseline','cbit_post')-change(r,'pst_baseline','pst_post')) for r in data['acute_randomized']}
    result['responder_displayed_mean_contrasts']={r['id']:str(change(r,'responder_baseline','responder_post')-change(r,'nonresponder_baseline','nonresponder_post')) for r in data['acute_responder_association']}
    result['followup_displayed_changes']={r['id']:{'baseline_to_post':str(change(r,'baseline','post')),'baseline_to_month6':str(change(r,'baseline','month6')),'post_to_month6':str(change(r,'post','month6'))} for r in data['selected_cbit_followup'] if not r.get('scores_suppressed')}
    # Printed hundredth rounding cannot move any smallest functional p under the restricted-family correction threshold.
    result['rounding_sensitivity']={k:{'assumption':'nearest-hundredth rounded p; sensitivity only','minimum_p_lower_bound':str(D(result[k]['p_min'])-D('.005')),'first_holm_bonferroni_lower_bound':str((D(result[k]['p_min'])-D('.005'))*result[k]['tested_rows'])} for k in GROUPS}
    # Only the already printed number of screened/excluded/randomized participants is checked here.
    result['flow_arithmetic']={'screened':172,'excluded':60,'screened_minus_excluded':112,'randomized':122,'discrepancy':10,'acute_allocated':63+59,'acute_analyzed':60+53,'acute_completed':56+49,'cbit_selected_followup':15,'cbit_followup_fraction_of_randomized':str(D(15)/D(63))}
    # Compare only numerical fields, never derive main values from the main extraction.
    mainpath=HERE.parent/'day16_functioning'/'aggregate_inputs.json'
    comparison={'main_path':str(mainpath),'mismatches':[],'matched_cells':0}
    if mainpath.exists():
        main_data=json.loads(mainpath.read_text())
        for g in GROUPS:
            for ours,theirs in zip(data[g],main_data[g]):
                if ours.get('scores_suppressed'):continue
                # IDs can differ in verbose naming, so compare source table order.
                for key,val in ours.items():
                    if key in ('id','source_label'):continue
                    if isinstance(val,dict):
                        for sub in ('mean','se'):
                            got=theirs[key][sub]
                            if got!=val[sub]:comparison['mismatches'].append([g,ours['id'],key,sub,val[sub],got])
                            else:comparison['matched_cells']+=1
                    elif theirs[key]!=val:comparison['mismatches'].append([g,ours['id'],key,val,theirs[key]])
                    else:comparison['matched_cells']+=1
        assert comparison['mismatches']==[],comparison['mismatches']
    result['main_extraction_crosscheck']=comparison
    outputpath=HERE.parent/'day16_functioning'/'aggregate_checks.json'
    outputcomparison={'main_path':str(outputpath),'mismatches':[],'matched_checks':0}
    if outputpath.exists():
        reported=json.loads(outputpath.read_text())
        def check(label,ours,theirs):
            if ours!=theirs:outputcomparison['mismatches'].append([label,str(ours),str(theirs)])
            else:outputcomparison['matched_checks']+=1
        for g in GROUPS:
            family=reported['families'][g]
            check(g+' tests',result[g]['tested_rows'],family['m'])
            check(g+' nominal',result[g]['nominal_significant'],len(family['nominal_ids']))
            for ours,theirs in zip(data[g],family['details']):
                key=ours['id']; label=g+' '+key
                if ours.get('scores_suppressed'):continue
                if ours['p'] is not None:
                    for method in ('holm','bonferroni'):
                        check(label+' '+method,D(result[g]['adjusted'][key][method]),D(theirs[method]))
                arithmetic=theirs['displayed_mean_arithmetic']
                if g=='acute_randomized':
                    check(label+' contrast',D(result['acute_displayed_mean_contrasts'][key]),D(arithmetic['cbit_minus_pst_change']))
                elif g=='acute_responder_association':
                    check(label+' contrast',D(result['responder_displayed_mean_contrasts'][key]),D(arithmetic['responder_minus_nonresponder_change']))
                else:
                    check(label+' post change',D(result['followup_displayed_changes'][key]['baseline_to_post']),D(arithmetic['post_minus_baseline']))
                    check(label+' month6 change',D(result['followup_displayed_changes'][key]['baseline_to_month6']),D(arithmetic['month6_minus_baseline']))
        for ours,theirs in zip(data['selected_cbit_followup'],main_data['selected_cbit_followup']):
            if ours.get('scores_suppressed'):continue
            check(ours['id']+' post marker',ours['post']['marker']=='a',theirs['baseline_post_significant_marker'])
            check(ours['id']+' month6 marker',ours['month6']['marker']=='a',theirs['baseline_month6_significant_marker'])
        assert outputcomparison['mismatches']==[],outputcomparison['mismatches']
    result['main_output_crosscheck']=outputcomparison
    (HERE/'independent_audit_output.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'families':{k:{f:v for f,v in result[k].items() if f!='adjusted'} for k in GROUPS},'main_extraction_crosscheck':comparison,'main_output_crosscheck':outputcomparison},indent=2))

if __name__=='__main__':main()
