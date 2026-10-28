"""Independent closed-form oracle for a synthetic identifiability example.
No human parameters, data, simulation draws, interventions or clinical inference.
"""
from decimal import Decimal as D, localcontext
from pathlib import Path
import json
checks=[]
def near(name,a,b,tolerance=D("1e-40")):
 assert abs(a-b)<tolerance,(name,a,b)
 checks.append({'name':name,'actual':str(a),'expected':str(b),'passed':True})
with localcontext() as c:
 c.prec=60
 p=D('.2'); o=1-(1-p).sqrt(); a=p.sqrt()
 near('single_drive',p,D('.2'))
 near('OR_drive',2*o-o*o,p)
 near('AND_drive',a*a,p)
 predictions={}
 for g in [D('.5'),D('.8')]:
  key=str(g);predictions[key]={}
  for kind,drive,blockx,blockz in [('single',p,D(0),p),('OR',2*o-o*o,o,o),('AND',a*a,D(0),D(0))]:
   vals={'baseline':drive*g,'half_gate':drive*g/2,'block_X':blockx*g,'block_Z':blockz*g,'block_both':D(0)}
   predictions[key][kind]={k:str(v) for k,v in vals.items()}
   near(key+'_'+kind+'_baseline',vals['baseline'],p*g)
   near(key+'_'+kind+'_half_gate',vals['half_gate'],p*g/2)
  near(key+'_shared_gate_action_baseline',D('.4')*g,D('.2') if g==D('.5') else D('.32'))
  near(key+'_shared_gate_action_halved',D('.4')*g/2,D('.1') if g==D('.5') else D('.16'))
 # Separate fixed-marginal scenario; not the calibrated mechanisms above.
 m=D('.25'); qlo=max(D(0),2*m-1); qhi=m; qi=m*m
 near('Frechet_joint_lower',qlo,D(0));near('Frechet_joint_upper',qhi,D('.25'))
 near('Frechet_independent_joint',qi,D('.0625'))
 near('Frechet_OR_lower',2*m-qhi,D('.25'));near('Frechet_OR_upper',2*m-qlo,D('.5'))
 for q in [qlo,qi,qhi]:
  probs=[q,m-q,m-q,1-2*m+q]
  near('joint_mass_'+str(q),sum(probs),D(1))
  assert all(x>=0 for x in probs)
  near('X_marginal_'+str(q),probs[0]+probs[1],m)
  near('Z_marginal_'+str(q),probs[0]+probs[2],m)
 # Cross-check every authored finite-state row against a separate closed form.
 authored=json.loads(Path(__file__).resolve().parents[1].joinpath('results.json').read_text())
 names={'single':'single','parallel':'OR','coincidence':'AND'}
 interventions={'none':'baseline','downstream':'half_gate','block_X':'block_X','block_Z':'block_Z','block_both':'block_both'}
 for row in authored['scenarios']:
  g=D('.5') if row['context']=='A' else D('.8')
  expected=D(predictions[str(g)][names[row['model']]][interventions[row['intervention']]])
  name='_'.join([row['model'],row['context'],row['intervention']])
  near('author_event_'+name,D(str(row['event_probability'])),expected,D('1e-12'))
  expected_action=D('.4')*g*(D('.5') if row['intervention']=='downstream' else 1)
  near('author_action_'+name,D(str(row['ordinary_action_probability'])),expected_action,D('1e-12'))
 for row in authored['coincidence_sensitivity']:
  j=D(str(row['joint_probability'])); vals=[D(str(row[k])) for k in ['p11','p10','p01','p00']]
  near('author_joint_sum_'+str(j),sum(vals),D(1))
  near('author_X_marginal_'+str(j),vals[0]+vals[1],D('.25'))
  near('author_Z_marginal_'+str(j),vals[0]+vals[2],D('.25'))
  near('author_AND_gate_'+str(j),D(str(row['AND_event_probability_at_gate_A'])),j*D('.5'))
 out={'label':'SYNTHETIC MODEL ONLY. Analyst-chosen probabilities, no patients or treatment predictions.','method':'Independent high-precision closed forms, not authors finite-state enumeration. No random seed.','checks_passed':len(checks),'checks':checks,'predictions':predictions,'candidate_scope':'Equivalence only for specified observed marginal outputs/contrasts; not all measurements or biology.'}
Path(__file__).with_name('checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(len(checks),'independent checks passed')
