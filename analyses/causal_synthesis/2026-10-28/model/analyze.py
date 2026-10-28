"""Deterministic synthetic causal-identifiability example; no patient inference."""
import itertools,json,math,pathlib
P=pathlib.Path(__file__).resolve().parent

def run(c):
 q=c['baseline_drive_probability']; ps={'single':q,'parallel':1-math.sqrt(1-q),'coincidence':math.sqrt(q)};rows=[]
 for model,p in ps.items():
  for context,g0 in c['gate_contexts'].items():
   for intervention in ['none','downstream','block_X','block_Z','block_both']:
    g=g0*(c['downstream_gate_multiplier'] if intervention=='downstream' else 1);rate=0.
    for x,z,k in itertools.product([0,1],repeat=3):
     weight=(p if x else 1-p)*(p if z else 1-p)*(g if k else 1-g)
     xx=0 if intervention in ['block_X','block_both'] else x;zz=0 if intervention in ['block_Z','block_both'] else z
     drive=xx if model=='single' else (xx or zz) if model=='parallel' else (xx and zz)
     rate+=weight*bool(drive and k)
    rows.append({'model':model,'context':context,'intervention':intervention,'event_probability':round(rate,12),'ordinary_action_probability':round(c['ordinary_action_demand_probability']*g,12)})
 m=c['coincidence_marginal_probability'];lo=max(0,2*m-1);hi=m
 joint=[{'joint_probability':j,'marginal_X':m,'marginal_Z':m,'p11':j,'p10':m-j,'p01':m-j,'p00':1-2*m+j,'AND_event_probability_at_gate_A':j*c['gate_contexts']['A']} for j in c['joint_grid']]
 assert all(lo<=r['joint_probability']<=hi for r in joint)
 return {'label':'SYNTHETIC MATHEMATICAL DEMONSTRATION, not biological discovery','method':'Finite Boolean-state enumeration, no random sampling or fitted patient data','seed':None,'input_probabilities':ps,'scenarios':rows,'coincidence_frechet_bounds':[lo,hi],'coincidence_sensitivity':joint,'limits':'Observational/response agreement is constructed, not empirical evidence. Ideal node specificity and gate sharing are assumptions. No patient mechanism, effect size or clinical recommendation follows.'}
if __name__=='__main__':
 result=run(json.loads((P/'inputs.json').read_text()));(P/'results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'scenarios':len(result['scenarios']),'coincidence_cases':len(result['coincidence_sensitivity']),'label':result['label']}))
