"""Independent public-aggregate arithmetic; no people-level data or randomness."""
from decimal import Decimal as D
from pathlib import Path
import json
checks = []
def check(name, value, expected):
    assert value == expected, (name, value, expected)
    checks.append({'name':name,'actual':str(value),'expected':str(expected),'passed':True})
check('age_partition',516+101,617)
check('diagnosis_partition',552+46+5+14,617)
check('sites_partition',181+207+66+47+41+40+35,617)
check('structured_interview_partition',157+122+106+25,410)
check('diagnostic_procedure_partition',410+207,617)
check('adult_percent_2dp',(D(101)/617*100).quantize(D('.01')),D('16.37'))
check('structured_interview_percent_2dp',(D(410)/617*100).quantize(D('.01')),D('66.45'))
check('ts_percent_2dp',(D(552)/617*100).quantize(D('.01')),D('89.47'))
check('adult_minus_youth_tic_mean',D('22.86')-D('23.88'),D('-1.02'))
check('adult_minus_youth_impairment_mean',D('24.38')-D('22.61'),D('1.77'))
check('adult_minus_youth_motor_mean',D('15.16')-D('14.21'),D('.95'))
check('adult_minus_youth_phonic_mean',D('7.70')-D('9.67'),D('-1.97'))
results=json.loads(Path(__file__).resolve().parents[1].joinpath('results.json').read_text())
check('author_adult_percent',D(results['adult_percent']), (D(101)*100/617).quantize(D('.000001')))
check('author_structured_percent',D(results['structured_interview_percent']), (D(410)*100/617).quantize(D('.000001')))
check('author_chronic_motor_vocal_percent',D(results['chronic_motor_or_vocal_percent']), (D(51)*100/617).quantize(D('.000001')))
for key, expected in [('motor','.95'),('phonic','-1.97'),('total_tic','-1.02'),('impairment','1.77')]:
    check('author_'+key+'_difference',D(results['adult_minus_youth_printed_mean_points'][key]),D(expected))
check('author_partitions_pass',all(results['partition_checks'].values()),True)
output={'method':'Independent Decimal arithmetic from publicly reported aggregate counts and rounded means. Not a simulation, statistical reanalysis or validation. No seed applies.','checks':checks,'passed':len(checks)}
Path(__file__).with_name('checks.json').write_text(json.dumps(output,indent=2)+'\n')
print(f'{len(checks)} independent arithmetic checks passed')
