"""SYNTHETIC metric sensitivity, not patient or anatomical evidence. No randomness."""
import json
from pathlib import Path

def metrics(tp,fn,fp,tn):
    sensitivity=tp/(tp+fn) if tp+fn else None
    specificity=tn/(tn+fp) if tn+fp else None
    return {'coverage':sensitivity,'cover_ratio':tp/fn if fn else None,
            'specificity':specificity,'balanced_accuracy':(sensitivity+specificity)/2 if sensitivity is not None and specificity is not None else None}

def run():
    rows=[]
    for added in [0,100,1000,10000]:
        row={'label':'SYNTHETIC','tp':40,'fn':60,'fp':20,'tn':80+added,'added_background':added}
        row.update(metrics(row['tp'],row['fn'],row['fp'],row['tn']));rows.append(row)
    boundaries={'zero_false_positives':metrics(40,60,0,80), 'zero_false_positives_padded':metrics(40,60,0,1080), 'complete_coverage':metrics(100,0,20,80),'empty_roi':metrics(0,0,20,80)}
    tests=[]
    def check(name,result):
        assert result,name
        tests.append(name)
    check('coverage invariant',all(r['coverage']==0.4 for r in rows))
    check('cover ratio invariant',all(abs(r['cover_ratio']-2/3)<1e-12 for r in rows))
    check('BA increases',all(a['balanced_accuracy']<b['balanced_accuracy'] for a,b in zip(rows,rows[1:])))
    check('BA below asymptote',all(r['balanced_accuracy']<0.7 for r in rows))
    for r in rows:
        c=r['coverage'];check('coverage ratio identity '+str(r['added_background']),abs(c/(1-c)-r['cover_ratio'])<1e-12)
        delta=r['added_background'];expected=0.5*20*delta/(100*(100+delta))
        check('BA delta identity '+str(delta),abs(r['balanced_accuracy']-rows[0]['balanced_accuracy']-expected)<1e-12)
    check('zero FP no padding effect',boundaries['zero_false_positives']==boundaries['zero_false_positives_padded'])
    check('full coverage ratio undefined',boundaries['complete_coverage']['cover_ratio'] is None)
    check('empty ROI BA undefined',boundaries['empty_roi']['balanced_accuracy'] is None)
    return {'type':'SYNTHETIC, deterministic, not patient evidence','seed':None,'rows':rows,'boundaries':boundaries,'tests_passed':len(tests),'tests':tests}
if __name__=='__main__':
    out=run();Path(__file__).with_name('synthetic-results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
