"""Independent checks of reported public aggregates and conditional cutoff logic."""
from decimal import Decimal as D
from pathlib import Path
import json
checks=[]
def check(name, actual, expected):
    assert actual == expected, (name,actual,expected)
    checks.append({'name':name,'actual':str(actual),'expected':str(expected),'passed':True})
check('sex_partition',541+165,706)
check('diagnosis_partition',624+76+6,706)
check('older_group_complement',706-578,128)
check('no_recent_phonic_percent',(D(178)/706*100).quantize(D('.000001')),D('25.212465'))
check('no_recent_motor_percent',(D(21)/706*100).quantize(D('.000001')),D('2.974504'))
check('TTS_alpha_minus_omega',D('.87')-D('.58'),D('.29'))
check('GSS_alpha_minus_omega',D('.88')-D('.56'),D('.32'))
check('same_coefficient_crossstudy_alpha_difference',D('.87')-D('.82'),D('.05'))
for prefix,cutoffs,expected in [('lenient',('.10','.90','.90'),(True,True,False)),('stringent',('.06','.95','.95'),(False,False,False))]:
    vals=(D('.09')<=D(cutoffs[0]),D('.90')>=D(cutoffs[1]),D('.87')>=D(cutoffs[2]))
    for label,a,e in zip(['RMSEA','CFI','TLI'],vals,expected): check(prefix+'_'+label,a,e)
    check(prefix+'_all_pass',all(vals),False)
check('rounding_lower_CFI_fails_lenient',D('.895')>=D('.90'),False)
check('rounding_upper_CFI_passes_lenient',D('.904')>=D('.90'),True)
r=json.loads(Path(__file__).resolve().parents[1].joinpath('results.json').read_text())
for k,v in [('TTS','.29'),('GSS','.32')]: check('author_gap_'+k,D(r['alpha_minus_omega'][k]),D(v))
for label,expected in [('lenient',2),('stringent',0)]:
    check('author_cutoff_count_'+label,r['cutoff_sensitivity'][label]['count_met'],expected)
    check('author_conjunction_'+label,r['cutoff_sensitivity'][label]['all_three_met'],False)
check('author_TLI_upper_boundary',D(r['rounding_sensitivity']['TLI_upper_rounding_boundary']),D('.875'))
check('author_RMSEA_lower_boundary',D(r['rounding_sensitivity']['RMSEA_lower_rounding_boundary']),D('.085'))
check('author_CFI_rounding_sensitive',r['rounding_sensitivity']['CFI_lenient_boundary_is_rounding_sensitive'],True)
check('author_partition',r['diagnosis_partition_matches'],True)
out={'method':'Decimal arithmetic on printed aggregate values. Threshold outcomes are conditional on rounded reported point estimates, not new model fits. No simulation, clinical effect or random seed.','passed':len(checks),'checks':checks}
Path(__file__).with_name('checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(f'{len(checks)} independent checks passed')
