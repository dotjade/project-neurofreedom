"""Published aggregate arithmetic only; not simulation or patient reconstruction."""
from pathlib import Path
from decimal import Decimal as D
import json
P=Path(__file__).resolve().parent

def analyze(x):
 c=x['counts'];pct=lambda a,b:str((D(a)*100/D(b)).quantize(D('.000001')))
 tp=c['both_moderate_severe'];tn=c['both_mild'];fn=c['clinician_moderate_severe']-tp;fp=c['clinician_mild']-tn;n=c['paired_assessments']
 d={k:D(v) for k,v in x['mean_difference_points'].items()}
 return {'kind':'Deterministic published-aggregate audit, not simulation','seed':None,
 'assessment_table':{'reference':'Clinician category, not independent biological truth','parent_moderate_clinician_moderate':tp,'parent_mild_clinician_moderate':fn,'parent_moderate_clinician_mild':fp,'parent_mild_clinician_mild':tn},
 'checks':{'table_sums_to_pairs':tp+tn+fn+fp==n,'reference_categories_sum_to_pairs':c['clinician_mild']+c['clinician_moderate_severe']==n},
 'patient_paired_analysis_fraction_percent':pct(c['patients_paired_analysis'],c['patients_enrolled']),
 'parent_assessment_pairing_percent':pct(n,c['parent_assessments']),
 'fellow_assessment_pairing_percent':pct(n,c['fellow_assessments']),
 'unpaired_fellow_assessments':c['fellow_assessments']-n,
 'unpaired_parent_assessments':c['parent_assessments']-n,
 'patients_not_in_paired_analysis':c['patients_enrolled']-c['patients_paired_analysis'],
 'sensitivity_percent':pct(tp,tp+fn),'specificity_percent':pct(tn,tn+fp),
 'category_agreement_percent':pct(tp+tn,n),'category_disagreement_percent':pct(fn+fp,n),
 'discordant_assessments':fn+fp,
 'difference_additivity_audit':{'component_sum':str(d['combined_tic']+d['impairment']),
 'entire_minus_component_sum':str(d['entire']-d['combined_tic']-d['impairment']),
 'mean_absolute_sum_lower_bound':str(abs(d['combined_tic']-d['impairment'])),
 'mean_absolute_sum_upper_bound':str(d['combined_tic']+d['impairment']),
 'entire_within_conditional_absolute_bounds':abs(d['combined_tic']-d['impairment'])<=d['entire']<=d['combined_tic']+d['impairment'],
 'conditions':'If components and total refer to same paired observations and absolute differences of an additive score; if signed means, sum identity instead applies. No mechanism chosen or source value repaired.'},
 'limits':'Visit-level descriptive fractions, not population accuracy or person-level discordance; no newly computed confidence interval or equivalence test. GEE not refitted.'}
if __name__=='__main__':(P/'results.json').write_text(json.dumps(analyze(json.loads((P/'inputs.json').read_text())),indent=2)+'\n')
