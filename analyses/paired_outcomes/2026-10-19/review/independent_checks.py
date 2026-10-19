#!/usr/bin/env python3
"""Independent regeneration from frozen specification; does not import analysis code.
Run from any working directory. Reads main artifacts, writes nothing outside review.
"""
import csv, hashlib, json, math, random, statistics, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
TOL=2e-12
checks=0
maxdiff=0.0

def check(ok,label):
    global checks
    checks+=1
    assert ok,label

def close(a,b,label):
    global maxdiff
    d=abs(a-b);maxdiff=max(maxdiff,d)
    check(d<=TOL,label+f': {a} vs {b}')

def avg(v):return sum(v)/len(v)
def metrics(t,p):
    mt,mp=avg(t),avg(p)
    return {'tic_mean':mt,'pain_mean':mp,'cross_moment':avg([a*b for a,b in zip(t,p)]),
            'covariance':avg([(a-mt)*(b-mp) for a,b in zip(t,p)])}

def main():
    cfg=json.loads((ROOT/'config.json').read_text())
    for line in (ROOT/'preexecution.sha256').read_text().splitlines():
        digest,name=line.split(maxsplit=1)
        check(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,'frozen hash '+name)
    # Separate generator; enforce frozen constants rather than copying analysis functions.
    check(cfg['population_size']==400 and cfg['replicates']==200,'frozen sample sizes')
    check(cfg['population_seed']==20261019 and cfg['replicate_seed_start']==20262019,'frozen seeds')
    check(cfg['measurement_error_half_width']==.25 and cfg['baseline']==5,'frozen measurement constants')
    check(cfg['designs']=={'complete':{'-1':1,'1':1},'mcar':{'-1':.6,'1':.6},'mar':{'-1':.8,'1':.3},'support_loss':{'-1':1,'1':0}},'frozen observation designs')
    gen=random.Random(20261019); pop=[]
    for x in [-1,1]:
        uv=[]
        for j in range(100):uv.append((gen.uniform(-1,1),gen.uniform(-1,1)))
        for sign in [1,-1]:
            for u,v in uv:
                u,v=sign*u,sign*v
                a=1+.4*x+.2*v
                pop.append({'unit':len(pop),'x':x,'u':u,'v':v,'t':2+.4*x+.2*u,
                            'A':a,'B':.4*x+.2*v,'C':a-(2 if x==1 else 0)})
    stored=list(csv.DictReader((ROOT/'synthetic_inputs.csv').open()))
    check(len(stored)==len(pop)==400,'population rows')
    for got,want in zip(stored,pop):
        for key in want:close(float(got[key]),want[key],'population '+key)
    truths={w:metrics([z['t'] for z in pop],[z[w] for z in pop]) for w in 'ABC'}
    close(truths['A']['pain_mean'],1,'A mean');close(truths['B']['pain_mean'],0,'B mean');close(truths['C']['pain_mean'],0,'C mean')
    close(truths['C']['covariance']-truths['B']['covariance'],-.4,'C-B covariance')
    close(truths['A']['covariance']-truths['B']['covariance'],0,'A-B covariance')
    for x in [-1,1]:
        for v in ['u','v']:close(sum(z[v] for z in pop if z['x']==x),0,'antithetic zero mean')
    # Both baseline and follow-up visit scores, including all realized errors.
    actual_low=math.inf;actual_high=-math.inf
    derived={};count_ranges={d:[] for d in cfg['designs']}
    for r in range(200):
        gen=random.Random(20262019+r); observed=[]
        for z in pop:
            tb,tf,pb,pf=[gen.uniform(-.25,.25) for _ in range(4)]
            q=gen.random()
            t=(5+tb)-(5-z['t']+tf)
            p={w:(5+pb)-(5-z[w]+pf) for w in 'ABC'}
            scores=[5+tb,5-z['t']+tf,5+pb]+[5-z[w]+pf for w in 'ABC']
            actual_low=min(actual_low,*scores);actual_high=max(actual_high,*scores)
            check(all(0<=s<=10 for s in scores),'realized visit bounds')
            observed.append((t,p,q))
        for d,probs in cfg['designs'].items():
            ids=[i for i,z in enumerate(pop) if observed[i][2]<probs[str(z['x'])]]
            count_ranges[d].append(len(ids));check(bool(ids),'nonempty observed sample')
            for w in 'ABC':
                t=[observed[i][0] for i in ids];p=[observed[i][1][w] for i in ids]
                vals={'cc_'+k:v for k,v in metrics(t,p).items()}
                if min(probs.values())==0:
                    vals.update({k:None for k in ['ht_tic_mean','ht_pain_mean','ht_cross_moment','ht_covariance']})
                    check(all(pop[i]['x']==-1 for i in ids) and len(ids)==200,'support-loss membership')
                else:
                    tt=sum(observed[i][0]/probs[str(pop[i]['x'])] for i in ids)/400
                    pp=sum(observed[i][1][w]/probs[str(pop[i]['x'])] for i in ids)/400
                    tp=sum(observed[i][0]*observed[i][1][w]/probs[str(pop[i]['x'])] for i in ids)/400
                    vals.update(ht_tic_mean=tt,ht_pain_mean=pp,ht_cross_moment=tp,ht_covariance=tp-tt*pp)
                vals.update(seed=20262019+r,n_observed=len(ids),n_minus=sum(pop[i]['x']==-1 for i in ids),n_plus=sum(pop[i]['x']==1 for i in ids))
                derived[r,d,w]=vals
            if d=='support_loss':
                for i in ids:close(observed[i][1]['A'],observed[i][1]['C'],'full observed A/C identity')
            for w in 'BC':close(derived[r,d,'A']['cc_tic_mean'],derived[r,d,w]['cc_tic_mean'],'identical tic records')
    rows=list(csv.DictReader((ROOT/'replicate_results.csv').open()))
    check(len(rows)==len(derived)==2400,'replicate rows')
    seen=set()
    for row in rows:
        key=(int(row['replicate']),row['design'],row['world'])
        check(key not in seen,'unique replicate row');seen.add(key)
        for k,v in derived[key].items():
            if v is None:check(row[k]=='','unsupported HT is unavailable')
            else:close(float(row[k]),v,'replicate '+str(key)+' '+k)
    result=json.loads((ROOT/'results.json').read_text())
    for w in 'ABC':
        for k,v in truths[w].items():close(result['truth'][w][k],v,'truth '+w+' '+k)
    check(len(result['summaries'])==84,'summary count')
    flags=[]
    for row in result['summaries']:
        d,w,e,m=[row[k] for k in ['design','world','estimator','metric']]
        values=[derived[r,d,w][e+'_'+m] for r in range(200)]
        target=truths[w][m]
        errors=[v-target for v in values]
        bias=avg(errors)
        mcse=math.sqrt(sum((v-bias)**2 for v in errors)/(199*200))
        close(row['target'],target,'summary target');close(row['mean'],avg(values),'summary mean')
        close(row['bias'],bias,'summary bias');close(row['monte_carlo_se'],mcse,'summary MCSE')
        eligible=m!='covariance' and ((e=='ht' and d!='support_loss') or (e=='cc' and d in ['complete','mcar']))
        flag=eligible and abs(bias)>4*mcse+1e-10
        check(row['unbiased_raw_moment_expected']==eligible,'diagnostic eligible')
        check(row['diagnostic_flag']==flag,'diagnostic flag')
        if flag:flags.append(row)
    check(result['diagnostic_flags']==flags,'complete diagnostic retention')
    # Analytic expectation of HT plug-in covariance; never require unbiasedness here.
    analytic={}
    for d,probs in cfg['designs'].items():
        if min(probs.values())<=0:continue
        analytic[d]={w:-sum((1-probs[str(z['x'])])/probs[str(z['x'])]*z['t']*z[w] for z in pop)/400**2 for w in 'ABC'}
    summary={'checks_passed':checks,'numeric_tolerance':TOL,'maximum_numeric_difference':maxdiff,
             'rows_independently_recomputed':len(derived),'diagnostic_flags':len(flags),
             'realized_score_bounds':[actual_low,actual_high],
             'observed_sample_ranges':{d:[min(v),max(v)] for d,v in count_ranges.items()},
             'analytic_HT_covariance_bias':analytic,
             'input_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['preregistration.md','config.json','run_analysis.py','synthetic_inputs.csv','replicate_results.csv','results.json']}}
    print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
