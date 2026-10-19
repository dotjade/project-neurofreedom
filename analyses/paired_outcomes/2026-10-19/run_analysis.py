#!/usr/bin/env python3
"""Fixed synthetic methods check. Standard library only; no participant data."""
import csv, hashlib, json, math, random, statistics
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def population(c):
    rng=random.Random(c['population_seed']); out=[]
    for x in (-1,1):
        pairs=[(rng.uniform(-1,1),rng.uniform(-1,1)) for _ in range(c['population_size']//4)]
        for u,v in pairs+ [(-u,-v) for u,v in pairs]:
            t=2+.4*x+.2*u
            out.append(dict(unit=len(out),x=x,u=u,v=v,t=t,A=1+.4*x+.2*v,B=.4*x+.2*v,C=1+.4*x+.2*v-2*(x==1)))
    return out

def moments(t,p):
    mt=statistics.fmean(t);mp=statistics.fmean(p);cross=statistics.fmean(a*b for a,b in zip(t,p))
    return dict(tic_mean=mt,pain_mean=mp,cross_moment=cross,covariance=cross-mt*mp)

def run(c,pop):
    n=len(pop); rows=[]
    for r in range(c['replicates']):
        rng=random.Random(c['replicate_seed_start']+r);h=c['measurement_error_half_width']
        obs=[]
        for z in pop:
            e=[rng.uniform(-h,h) for _ in range(4)]
            obs.append((z['t']+e[0]-e[1],e[2]-e[3],rng.random()))
        for design,probs in c['designs'].items():
            selected=[(z,o,probs[str(z['x'])]) for z,o in zip(pop,obs) if o[2]<probs[str(z['x'])]]
            for world in c['worlds']:
                ts=[o[0] for z,o,pr in selected];ps=[z[world]+o[1] for z,o,pr in selected]
                cc=moments(ts,ps)
                row=dict(replicate=r,seed=c['replicate_seed_start']+r,design=design,world=world,n_observed=len(selected),n_minus=sum(z['x']==-1 for z,o,pr in selected),n_plus=sum(z['x']==1 for z,o,pr in selected))
                row.update({'cc_'+k:v for k,v in cc.items()})
                if min(probs.values())>0:
                    mt=math.fsum(o[0]/pr for z,o,pr in selected)/n
                    mp=math.fsum((z[world]+o[1])/pr for z,o,pr in selected)/n
                    cp=math.fsum(o[0]*(z[world]+o[1])/pr for z,o,pr in selected)/n
                    row.update(ht_tic_mean=mt,ht_pain_mean=mp,ht_cross_moment=cp,ht_covariance=cp-mt*mp)
                else:
                    row.update({k:None for k in ('ht_tic_mean','ht_pain_mean','ht_cross_moment','ht_covariance')})
                rows.append(row)
    return rows

def summarize(c,pop,rows):
    truth={w:moments([z['t'] for z in pop],[z[w] for z in pop]) for w in c['worlds']}
    summaries=[];flags=[]
    for d in c['designs']:
        for w in c['worlds']:
            group=[r for r in rows if r['design']==d and r['world']==w]
            for estimator in ('cc','ht'):
                for metric in truth[w]:
                    key=estimator+'_'+metric
                    vals=[r[key] for r in group if r[key] is not None]
                    if not vals:continue
                    errors=[v-truth[w][metric] for v in vals]
                    bias=statistics.fmean(errors);mcse=statistics.stdev(errors)/math.sqrt(len(errors))
                    test_expected=(metric!='covariance' and ((estimator=='ht' and d!='support_loss') or (estimator=='cc' and d in ('complete','mcar'))))
                    flag=test_expected and abs(bias)>c['diagnostic_mcse_multiplier']*mcse+1e-10
                    entry=dict(design=d,world=w,estimator=estimator,metric=metric,target=truth[w][metric],mean=statistics.fmean(vals),bias=bias,monte_carlo_se=mcse,unbiased_raw_moment_expected=test_expected,diagnostic_flag=flag)
                    summaries.append(entry)
                    if flag:flags.append(entry)
    return dict(label='SYNTHETIC ONLY: arbitrary units, descriptive finite-population changes',truth=truth,diagnostic_flags=flags,summaries=summaries)

def write_csv(path,rows):
    with path.open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)

def main():
    c=json.loads((ROOT/'config.json').read_text())
    assert hashlib.sha256((ROOT/'preregistration.md').read_bytes()).hexdigest()==c['preregistration_sha256']
    p=population(c);r=run(c,p);s=summarize(c,p,r)
    write_csv(ROOT/'synthetic_inputs.csv',p);write_csv(ROOT/'replicate_results.csv',r)
    (ROOT/'results.json').write_text(json.dumps(s,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'finite_population':len(p),'replicate_rows':len(r),'diagnostic_flags':len(s['diagnostic_flags']),'truth':s['truth']},indent=2))
if __name__=='__main__':main()
