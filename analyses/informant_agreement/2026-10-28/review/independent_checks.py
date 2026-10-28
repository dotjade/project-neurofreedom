"""Independent aggregate checks of Ho 2020 counts; no participant reconstruction."""
from decimal import Decimal as D
from pathlib import Path
import json
checks=[]
def check(name,actual,expected):
 assert actual==expected,(name,actual,expected)
 checks.append({'name':name,'actual':str(actual),'expected':str(expected),'passed':True})
check('reports_not_paired',3356-1455,1901)
check('enrollees_without_analyzed_pair',594-527,67)
check('reference_positive_partition',507+129,636)
check('reference_negative_partition',752+67,819)
check('all_classifications',507+129+752+67,1455)
check('discordant_classifications',129+67,196)
check('concordant_classifications',507+752,1259)
check('parent_positive_classifications',507+67,574)
check('parent_negative_classifications',752+129,881)
check('sensitivity_1dp',(D(507)/636*100).quantize(D('.1')),D('79.7'))
check('specificity_1dp',(D(752)/819*100).quantize(D('.1')),D('91.8'))
check('discordance_2dp',(D(196)/1455*100).quantize(D('.01')),D('13.47'))
check('paired_report_coverage_2dp',(D(1455)/3356*100).quantize(D('.01')),D('43.36'))
check('paired_patient_coverage_2dp',(D(527)/594*100).quantize(D('.01')),D('88.72'))
check('component_difference_sum',D('2.40')+D('2.41'),D('4.81'))
check('absolute_total_possible_cancellation',D('4.15')<=D('4.81'),True)
check('fellow_evaluations_unpaired',1522-1455,67)
check('absolute_lower_bound',abs(D('2.40')-D('2.41')),D('.01'))
r=json.loads(Path(__file__).resolve().parents[1].joinpath('results.json').read_text())
for key,n,d in [('sensitivity_percent',507,636),('specificity_percent',752,819),('category_agreement_percent',1259,1455),('category_disagreement_percent',196,1455),('patient_paired_analysis_fraction_percent',527,594),('parent_assessment_pairing_percent',1455,3356)]:
 check('author_'+key,D(r[key]),(D(n)*100/d).quantize(D('.000001')))
check('author_absolute_lower_bound',D(r['difference_additivity_audit']['mean_absolute_sum_lower_bound']),D('.01'))
check('author_absolute_upper_bound',D(r['difference_additivity_audit']['mean_absolute_sum_upper_bound']),D('4.81'))
check('author_absolute_compatible',r['difference_additivity_audit']['entire_within_conditional_absolute_bounds'],True)
check('author_fellow_pairing_percent',D(r['fellow_assessment_pairing_percent']),(D(1455)*100/1522).quantize(D('.000001')))
check('author_unpaired_fellow_assessments',r['unpaired_fellow_assessments'],67)
out={'method':'Published classification aggregates and arithmetic only. Repeated assessments are not independent people. No ICC, interval, causal learning effect or individual score estimated. No random seed.','passed':len(checks),'checks':checks}
Path(__file__).with_name('checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(f'{len(checks)} independent checks passed')
