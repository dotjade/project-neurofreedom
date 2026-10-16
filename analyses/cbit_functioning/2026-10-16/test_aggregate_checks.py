import unittest,json
from decimal import Decimal as D
from pathlib import Path
from aggregate_checks import adjust,compute
ROOT=Path(__file__).resolve().parent
class AggregateAuditTests(unittest.TestCase):
 def setUp(self):
  self.data=json.loads((ROOT/'aggregate_inputs.json').read_text());self.out=compute(self.data)
 def test_complete_functional_rows(self):
  for name in ['acute_randomized','acute_responder_association','selected_cbit_followup']:
   self.assertEqual(len(self.data[name]),12);self.assertEqual(len({r['id'] for r in self.data[name]}),12)
 def test_tested_counts(self):
  self.assertEqual([f['m'] for f in self.out['families'].values()],[12,12,11])
 def test_nominal_counts(self):
  self.assertEqual([len(f['nominal_ids']) for f in self.out['families'].values()],[0,2,2])
 def test_no_corrected_support(self):
  for f in self.out['families'].values():self.assertEqual(f['holm_below_05'],[]);self.assertEqual(f['bonferroni_below_05'],[])
 def test_tied_response_p(self):
  d={r['id']:r for r in self.out['families']['acute_responder_association']['details']}
  for k in ['sds_family','sas_parental_role']:self.assertEqual(D(d[k]['holm']),D('.24'));self.assertEqual(D(d[k]['bonferroni']),D('.24'))
 def test_followup_corrections(self):
  d={r['id']:r for r in self.out['families']['selected_cbit_followup']['details']}
  self.assertEqual(D(d['sds_total']['holm']),D('.33'));self.assertEqual(D(d['sds_work']['holm']),D('.40'));self.assertEqual(D(d['sds_work']['bonferroni']),D('.44'))
 def test_descriptive_acute_changes(self):
  d={r['id']:r for r in self.out['families']['acute_randomized']['details']}
  self.assertEqual(D(d['sds_total']['displayed_mean_arithmetic']['cbit_minus_pst_change']),D('-.83'))
  self.assertEqual(D(d['sds_social']['displayed_mean_arithmetic']['cbit_minus_pst_change']),D('.57'))
 def test_missing_parental_test_not_fabricated(self):
  f=self.out['families']['selected_cbit_followup'];self.assertEqual(f['untested_ids'],['sas_parental_role'])
  r=next(r for r in f['details'] if r['id']=='sas_parental_role');self.assertIsNone(r['printed_p']);self.assertNotIn('holm',r);self.assertNotIn('displayed_mean_arithmetic',r)
  source=next(r for r in self.data['selected_cbit_followup'] if r['id']=='sas_parental_role')
  for k in ['baseline','post','month6']:self.assertNotIn(k,source)
 def test_pairwise_marker_distinction(self):
  r=next(r for r in self.data['selected_cbit_followup'] if r['id']=='sds_total')
  self.assertTrue(r['baseline_post_significant_marker']);self.assertFalse(r['baseline_month6_significant_marker']);self.assertIsNone(self.data['pairwise_followup']['sds_total_baseline_month6_p'])
 def test_denominator_distinctions(self):
  d=self.out['denominator_audit'];self.assertEqual((d['randomized_total'],d['acute_analyzed_figure_total'],d['acute_completed_total']),(122,113,105));self.assertEqual(d['figure_flow_difference'],10);self.assertFalse(d['correction_inferred'])
 def test_holm_known_example(self):
  result=adjust({'a':D('.01'),'b':D('.02'),'c':D('.8')})
  self.assertEqual(result['holm'],{'a':D('.03'),'b':D('.04'),'c':D('.8')})
 def test_holm_monotonicity_and_bounds(self):
  ps={'a':D('0'),'b':D('.03'),'c':D('.03'),'d':D('1')};r=adjust(ps)
  vals=[r['holm'][k] for k in sorted(ps,key=lambda k:(ps[k],k))]
  self.assertEqual(vals,sorted(vals));self.assertTrue(all(0<=p<=1 for p in vals));self.assertTrue(all(r['holm'][k]>=p for k,p in ps.items()))
 def test_deterministic(self):self.assertEqual(self.out,compute(self.data))
if __name__=='__main__':unittest.main(verbosity=2)
