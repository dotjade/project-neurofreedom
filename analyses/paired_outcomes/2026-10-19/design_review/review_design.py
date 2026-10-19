"""Independent inferential audit: reads outputs, never imports analysis source."""
import argparse,csv,json,math,hashlib
from pathlib import Path
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--source',type=Path,default=Path(__file__).resolve().parent.parent,help='Analysis directory; defaults to parent of design_review directory')
args=parser.parse_args()
src=args.source.resolve()
out=Path(__file__).resolve().parent
c=json.loads((src/'config.json').read_text())
p=[{k:float(v) for k,v in r.items()} for r in csv.DictReader((src/'synthetic_inputs.csv').open())]
assert len(p)==400
assert hashlib.sha256((src/'preregistration.md').read_bytes()).hexdigest()==c['preregistration_sha256']
avg=lambda a: math.fsum(a)/len(p)
q=avg(z['u']*z['v'] for z in p)
truth={}
for w in 'ABC':
    mt=avg(z['t'] for z in p);mp=avg(z[w] for z in p)
    cov=avg((z['t']-mt)*(z[w]-mp) for z in p)
    truth[w]={'pain_mean':mp,'centered_covariance':cov,'cross_moment':avg(z['t']*z[w] for z in p)}
    expected=.16+.04*q if w!='C' else -.24+.04*q
    assert abs(cov-expected)<1e-14
assert all(abs(z['C']-(z['B']-z['x']))<1e-14 for z in p)
assert all(z['A']==z['C'] for z in p if z['x']==-1)
reported=json.loads((src/'results.json').read_text())
for w in 'ABC':
    assert abs(truth[w]['centered_covariance']-reported['truth'][w]['covariance'])<1e-14
bias={}
for design in ['complete','mcar','mar']:
    bias[design]={w:-math.fsum((1/c['designs'][design][str(int(z['x']))]-1)*z['t']*z[w] for z in p)/len(p)**2 for w in 'ABC'}
result={'status':'passed','plan_sha256':c['preregistration_sha256'],'finite_mean_uv':q,'independent_algebra_truth':truth,'analytic_expected_HT_plugin_covariance_bias':bias,'scope':'Inferential/plan-consistency review; full independent replication is a separate reviewer task.'}
(out/'design_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
