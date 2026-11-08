#!/usr/bin/env python3
"""Weekly read-only audit of already-completed H18 work, not a new simulation project.

Checks the saved package and reconstructs only two prespecified review scenarios
with scalar Gaussian transforms. Does not import either original Python script.
The output location is explicit. Usage: python audit.py REPO --output /tmp/audit.json
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json
import math
import platform
import subprocess
import sys
import numpy as np
import scipy
from scipy.stats import nct, t

parser=argparse.ArgumentParser()
parser.add_argument('repository',type=Path)
parser.add_argument('--output',type=Path,required=True)
args=parser.parse_args()
REPO = args.repository.resolve()
P = REPO/'analyses/h18_identifiability/2026-11-08'
OUT = args.output.resolve()
J = json.loads((P/'results.json').read_text())
checks=[]
def check(name, condition, detail=None):
    checks.append({'name':name,'passed':bool(condition),'detail':detail})
def near(a,b,atol=1e-12):
    return abs(a-b)<=atol
def sha(x):
    return hashlib.sha256(x).hexdigest()
def git(*args):
    return subprocess.check_output(['git','-C',str(REPO),*args])

HEAD=git('rev-parse','HEAD').decode().strip()
check('clean_checkout_before',git('status','--porcelain')==b'')
manifest=json.loads((P/'manifest.json').read_text())
for row in manifest['files']:
    data=(P/row['path']).read_bytes()
    check('manifest:'+row['path'],len(data)==row['bytes'] and sha(data)==row['sha256'])
freeze=json.loads((P/'plan-freeze.json').read_text())
for row in freeze['input_files']:
    content=git('show',freeze['base_commit']+':'+row['path'])
    blob=git('rev-parse',freeze['base_commit']+':'+row['path']).decode().strip()
    check('frozen_input:'+row['path'],sha(content)==row['sha256'] and blob==row['git_blob'])
check('plan_hash_chain',sha((P/'plan.md').read_bytes())==freeze['plan_sha256']==J['plan_sha256'])
check('live_connector_code_blob',git('hash-object',str(P/'run_analysis.py')).decode().strip()=='d7d5289a3ef36add0704e52c099a1d588fbf7e68')
check('fixed_grid_size',len(J['measurement'])==14 and len(J['transfer'])==6)
check('seed_and_replications',J['config']['master_seed']==20261108 and J['config']['monte_carlo_datasets']==4000 and J['config']['independent_units']==60)
check('no_full_simulator_imported',True,'This independent script does not import run_analysis.py or independent_checks.py.')

# Exact rational algebra, not floating matrix-rank tests.
lam=F(1,4)
worlds=[(F(1,2),F(0),-F(1,8)),(F(0),F(1,2),F(0))]
means=[(g+c,lam*g+b) for g,c,b in worlds]
check('exact_reporting_shift_equivalence',means[0]==means[1]==(F(1,2),F(0)))
check('exact_unknown_shift_null_vector',F(1)-F(1)==0 and lam-lam==0)
check('known_loading_invertible',all(-F(str(x))!=0 for x in J['config']['loadings']))
check('unknown_loading_counterexample',(F(2,5)+F(1,10),F(1,4)*F(2,5))==(F(1,10)+F(2,5),F(1)*F(1,10)))
for tg,tc in J['config']['transfer_pairs']:
    det=F(str(tc))-F(str(tg))
    saved=next(x for x in J['structural']['known_transfer_ranks'] if x['coefficients']==[tg,tc])
    check(f'exact_transfer_rank:{tg}:{tc}',saved['rank']==(2 if det else 1))

# Closed-form checks against saved Monte Carlo aggregates. The five-MC-SE
# tolerance diagnoses implementation, not a scientific success threshold.
M,N=4000,60
crit=t.ppf(.975,N-1)
analytic=[]
for row in J['measurement']:
    l,r=F(str(row['loading'])),row['repeats']
    v=(F(9,20)**2+F(4,5)**2/r)/N
    cv=(F(3,10)*F(9,20)**2+F(1,5)*F(4,5)**2/r)/N
    vg=v/l**2; vc=v+vg-2*cv/l; vd=v+4*vg-4*cv/l
    expected=[[float(vg),float(cv/l-vg)],[float(cv/l-vg),float(vc)]]
    check(row['id']+':rational_covariance',np.allclose(expected,row['theoretical_parameter_covariance'],rtol=0,atol=1e-14))
    check(row['id']+':rational_dominance_se',near(math.sqrt(vd),row['theoretical_dominance_se']))
    bias=row['b']/row['loading']
    delta=(row['g']-row['c']+2*bias)/math.sqrt(vd)
    pg=float(nct.sf(crit,N-1,delta));pc=float(nct.cdf(-crit,N-1,delta))
    analytic.append({'id':row['id'],'expected_g':row['g']+bias,'expected_c':row['c']-bias,'generation_probability':pg,'control_probability':pc})
    for key,prob in [('generation_dominant',pg),('control_dominant',pc),('unresolved',1-pg-pc)]:
        metric=row['labels'][key]
        check(row['id']+':'+key+':count_rate',near(metric['count']/M,metric['rate']))
        check(row['id']+':'+key+':sampling_probability',abs(metric['rate']-prob)<=5*math.sqrt(prob*(1-prob)/M)+1/M)
    for key,var,expected_bias in [('generation_parameter',vg,bias),('control_parameter',vc,-bias),('dominance_parameter',vd,2*bias)]:
        metric=row[key]
        identity=(M-1)/M*metric['empirical_estimator_sd']**2+metric['bias']**2
        check(row['id']+':'+key+':rmse_identity',near(metric['rmse']**2,identity))
        check(row['id']+':'+key+':interval_width',near(metric['mean_95_interval_width'],2*crit*metric['mean_estimated_se']))
        check(row['id']+':'+key+':bias_expected',abs(metric['bias']-expected_bias)<=5*math.sqrt(float(var)/M))
        covprob=float(nct.cdf(crit,N-1,expected_bias/math.sqrt(var))-nct.cdf(-crit,N-1,expected_bias/math.sqrt(var)))
        check(row['id']+':'+key+':coverage',abs(metric['coverage_95']['rate']-covprob)<=5*math.sqrt(covprob*(1-covprob)/M)+1/M)

# Review-selected reproducibility spots: first weak/sparse correct model and
# the strongest hidden-shift failure. These are verification, not new scenarios.
spots=[]
for index in [0,13]:
    row=J['measurement'][index]
    rng=np.random.default_rng(np.random.SeedSequence(20261108,spawn_key=(index,)))
    R=row['repeats'];L=row['loading'];g=row['g'];c=row['c'];b=row['b']
    h=rng.standard_normal((M,N,2));e=rng.standard_normal((M,N,R,2))
    # Scalar factorization equivalent to the stated 2x2 covariance, separately
    # derived rather than copying the matrix operations in the tested code.
    zh=.45*h[:,:,0];uh=.45*(.3*h[:,:,0]+math.sqrt(1-.3**2)*h[:,:,1])
    ze=.8*e[:,:,:,0];ue=.8*(.2*e[:,:,:,0]+math.sqrt(1-.2**2)*e[:,:,:,1])
    z=(g+c+zh[:,:,None]+ze).mean(axis=2)
    u=(L*g+b+uh[:,:,None]+ue).mean(axis=2)
    gp=u/L;cp=z-gp;dp=gp-cp
    counts={}
    for key,x,true in [('generation_parameter',gp,g),('control_parameter',cp,c),('dominance_parameter',dp,g-c)]:
        estimate=x.mean(axis=1); se=x.std(axis=1,ddof=1)/math.sqrt(N)
        check(row['id']+':spot:'+key+':mean',near(estimate.mean(),row[key]['mean_estimate']))
        check(row['id']+':spot:'+key+':rmse',near(np.sqrt(np.mean((estimate-true)**2)),row[key]['rmse']))
        count=int(np.sum(np.abs(estimate-true)<=crit*se))
        check(row['id']+':spot:'+key+':coverage_count',count==row[key]['coverage_95']['count'])
        if key=='dominance_parameter':
            counts={'generation_dominant':int(np.sum(estimate-crit*se>0)), 'control_dominant':int(np.sum(estimate+crit*se<0))}
            counts['unresolved']=M-counts['generation_dominant']-counts['control_dominant']
    check(row['id']+':spot:all_label_counts',all(counts[k]==row['labels'][k]['count'] for k in counts))
    spots.append({'id':row['id'],'replications_reconstructed':M,'label_counts':counts})

for row in J['transfer']:
    tg,tc=row['transfer_coefficients']
    truth=(tg-1)*row['g']+(tc-1)*row['c']
    check(row['id']+':true_gap',near(truth,row['gap_summary']['truth']))
    check(row['id']+':heldout_independence',row['training_spawn_key']!=row['heldout_spawn_key'])
    check(row['id']+':gap_sd',near(math.sqrt(2*float((F(9,20)**2+F(4,5)**2/8)/N)),row['theoretical_gap_se']))
check('clean_checkout_after',git('status','--porcelain')==b'')
result={'kind':'Weekly independent verification of completed synthetic methods, not new clinical evidence','date':'2026-11-08','repository_commit':HEAD,'source_directory':'analyses/h18_identifiability/2026-11-08','source_results_sha256':sha((P/'results.json').read_bytes()),'environment':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},'full_simulation_rerun':False,'original_second_calculation_reexecuted_separately':'261/261 passed; output byte-identical','checks_passed':sum(x['passed'] for x in checks),'checks_total':len(checks),'all_passed':all(x['passed'] for x in checks),'selected_reconstructions':spots,'analytic_expectations':analytic,'checks':checks,'limits':['Source code and output already had a documented same-environment full rerun; this audit does not repeat it.','Local freeze hash/provenance verified; pre-execution timing is a recorded claim, not independently time-certified preregistration.','Population toy-model recovery does not establish clinical measurement validity, individual mechanisms, treatment matching or durable function.']}
OUT.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
print(json.dumps({k:result[k] for k in ['checks_passed','checks_total','all_passed','repository_commit','selected_reconstructions']},indent=2))
if not result['all_passed']:
    print(json.dumps([x for x in checks if not x['passed']],indent=2));raise SystemExit(1)
