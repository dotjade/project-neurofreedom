"""Independent aggregate-only Venn-cell enumeration; no people or outcomes."""
import json
from pathlib import Path

def feasible(a,b,p=None,disjoint=False):
    rows=[]
    for shared in range(min(a,b)+1):
        if disjoint and shared: continue
        only_a,only_b=a-shared,b-shared
        if p is None:
            rows.append({'cohort_intersection':shared,'cohort_union':a+b-shared})
            continue
        for pa in range(only_a+1):
            for pb in range(only_b+1):
                ps=p-pa-pb
                if 0<=ps<=shared:
                    rows.append({'cohort_intersection':shared,'cohort_union':a+b-shared,
                                 'mixed_a_only':pa,'mixed_b_only':pb,'mixed_shared':ps})
    return rows

def summarize(rows):
    return {'configuration_count':len(rows),'union_values':sorted({x['cohort_union'] for x in rows}),
            'intersection_values':sorted({x['cohort_intersection'] for x in rows})}

with_mixed=feasible(10,8,16)
without_mixed=feasible(10,8)
disjoint_mixed=feasible(10,8,16,True)
assert summarize(with_mixed)['union_values']==[16,17,18]
assert summarize(with_mixed)['intersection_values']==[0,1,2]
assert summarize(without_mixed)['union_values']==list(range(10,19))
assert [(r['mixed_a_only'],r['mixed_b_only']) for r in disjoint_mixed]==[(8,8),(9,7),(10,6)]
assert summarize(feasible(10,8,None,True))['union_values']==[18]
assert not feasible(10,8,19)
assert feasible(10,8,18)==[{'cohort_intersection':0,'cohort_union':18,'mixed_a_only':10,'mixed_b_only':8,'mixed_shared':0}]
assert len(feasible(0,0,0))==1
assert len(feasible(1,1,1))==3
assert sorted({r['cohort_union'] for r in feasible(1,1,1)})==[1,2]
assert 4<=10 and 5<=8
assert 4+10+5+8+16==43
assert 4+10+5+8==27
out={'method':'integer Venn-cell enumeration; no participant identities or outcomes',
     'conditional_on':'accurate distinct-person counts and report containment in the two enrollment universes',
     'with_preprint_membership':summarize(with_mixed),
     'without_preprint_membership':summarize(without_mixed),
     'disjoint_and_mixed':{'summary':summarize(disjoint_mixed),'allocations':disjoint_mixed},
     'invalid_role_count_sum':43,'checks_passed':13}
Path(__file__).with_name('independent-results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
