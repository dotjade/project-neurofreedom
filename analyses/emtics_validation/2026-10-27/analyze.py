"""Deterministic sensitivity of reported fit to published alternative cutoffs.
Not simulation, model estimation, participant reconstruction or clinical validation.
"""
from pathlib import Path
from decimal import Decimal as D
import json
P=Path(__file__).resolve().parent

def analyze(x):
 fit={k:D(v) for k,v in x['fit'].items()}
 decisions={}
 for label,cuts in x['cutoffs'].items():
  met={k:(v<=D(cuts[k]) if k=='RMSEA' else v>=D(cuts[k])) for k,v in fit.items()}
  decisions[label]={'individual_cutoffs_met':met,'count_met':sum(met.values()),'all_three_met':all(met.values())}
 h=D(x['rounding_half_unit'])
 return {'analysis_type':'Deterministic published-aggregate sensitivity; not simulation','random_seed':None,
 'alpha_minus_omega':{k:str(D(v['alpha'])-D(v['omega'])) for k,v in x['reliability'].items()},
 'cutoff_sensitivity':decisions,
 'rounding_sensitivity':{'assumption':'Hypothetical conventional rounding to two decimals; not source-supplied precision intervals',
 'TLI_upper_rounding_boundary':str(fit['TLI']+h),
 'TLI_below_even_lenient_cutoff_throughout_rounding_interval':fit['TLI']+h<D(x['cutoffs']['lenient']['TLI']),
 'RMSEA_lower_rounding_boundary':str(fit['RMSEA']-h),
 'RMSEA_above_stringent_cutoff_throughout_rounding_interval':fit['RMSEA']-h>D(x['cutoffs']['stringent']['RMSEA']),
 'CFI_lenient_boundary_is_rounding_sensitive':fit['CFI']-h<D(x['cutoffs']['lenient']['CFI'])<=fit['CFI']+h},
 'diagnosis_partition_matches':sum(x['sample'][k] for k in ['tourette','chronic_motor','chronic_vocal'])==x['sample']['total'],
 'limits':'Arithmetic differences are not estimates of alpha bias or reliability loss. Threshold conjunction is a transparent sensitivity convention, not a diagnostic decision. No significance tests or clinical effects computed.'}
if __name__=='__main__':(P/'results.json').write_text(json.dumps(analyze(json.loads((P/'inputs.json').read_text())),indent=2)+'\n')
