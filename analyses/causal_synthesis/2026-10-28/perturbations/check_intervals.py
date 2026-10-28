"""Descriptive constraints from published marginal CIs, not simulation or meta-analysis."""
import json,pathlib
p=pathlib.Path(__file__).resolve().parent
r={x['id']:x for x in json.loads((p/'trial-records.json').read_text())['records']}
thresholds=[3,4,5,6.5] # Illustrative score differences, not clinical importance thresholds.
out=[]
for id in ['artists1','artists2']:
 x=r[id]['selectedAggregateResult'];lo,hi=x['CI95'];assert lo<x['activeMinusPlacebo']<hi
 out.append({'id':id,'CI95':[lo,hi],'includesZero':lo<=0<=hi,'illustrativeBeneficialDifferences':[{'benefitPoints':b,'anyEffectAtLeastThisBeneficialCompatibleWithReportedCI':lo<=-b} for b in thresholds]})
assert out[0]['illustrativeBeneficialDifferences'][1]['anyEffectAtLeastThisBeneficialCompatibleWithReportedCI']
assert not out[1]['illustrativeBeneficialDifferences'][1]['anyEffectAtLeastThisBeneficialCompatibleWithReportedCI']
assert all(not x['illustrativeBeneficialDifferences'][2]['anyEffectAtLeastThisBeneficialCompatibleWithReportedCI'] for x in out)
result={'method':'Intersect each printed 95% CI with (-infinity, -threshold]. No pooling, fitted model, seed, participant reconstruction or probabilities assigned to parameters. Printed CI rounding preserved.','thresholdsAreIllustrativeNotClinical':True,'results':out,'assertionsPassed':5}
(p/'interval-results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
