import hashlib,json,math,unittest
from pathlib import Path
from run_analysis import population,run,moments,summarize
ROOT=Path(__file__).resolve().parent
class Checks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c=json.loads((ROOT/'config.json').read_text());cls.p=population(cls.c);cls.r=run(cls.c,cls.p)
    def test_plan_hash(self):self.assertEqual(hashlib.sha256((ROOT/'preregistration.md').read_bytes()).hexdigest(),self.c['preregistration_sha256'])
    def test_population_count(self):self.assertEqual(len(self.p),400)
    def test_stratum_balance(self):self.assertEqual(sum(z['x']==1 for z in self.p),200)
    def test_zero_stratum_latents(self):
        for x in (-1,1):
            for var in ('u','v'):self.assertAlmostEqual(math.fsum(z[var] for z in self.p if z['x']==x),0)
    def test_truth_means(self):
        for w,expected in [('A',1),('B',0),('C',0)]:self.assertAlmostEqual(moments([z['t'] for z in self.p],[z[w] for z in self.p])['pain_mean'],expected)
        self.assertAlmostEqual(math.fsum(z['t'] for z in self.p)/400,2)
    def test_tic_only_identical(self):
        for r in range(200):
            for d in self.c['designs']:
                values=[z['cc_tic_mean'] for z in self.r if z['replicate']==r and z['design']==d]
                self.assertEqual(len(set(values)),1)
    def test_oracle_cross_moment(self):
        truths={w:moments([z['t'] for z in self.p],[z[w] for z in self.p]) for w in ('A','B','C')}
        self.assertAlmostEqual(truths['C']['covariance']-truths['B']['covariance'],-.4)
        self.assertAlmostEqual(truths['A']['covariance']-truths['B']['covariance'],0)
        self.assertAlmostEqual(truths['C']['cross_moment']-truths['B']['cross_moment'],-.4)
    def test_bounds_with_error_envelope(self):
        for z in self.p:
            for v in ('t','A','B','C'):
                self.assertGreaterEqual(5-z[v]-.25,0);self.assertLessEqual(5-z[v]+.25,10)
    def test_known_probabilities(self):
        for d,pr in self.c['designs'].items():
            for p in pr.values():self.assertTrue(0<=p<=1)
    def test_complete_counts(self):
        for z in self.r:
            if z['design']=='complete':self.assertEqual(z['n_observed'],400)
    def test_support_loss_counts(self):
        for z in self.r:
            if z['design']=='support_loss':self.assertEqual((z['n_minus'],z['n_plus']),(200,0));self.assertIsNone(z['ht_pain_mean'])
    def test_support_loss_observational_identity(self):
        for z in self.p:
            if z['x']==-1:self.assertEqual(z['A'],z['C'])
        for r in range(200):
            ac=[z for z in self.r if z['replicate']==r and z['design']=='support_loss' and z['world'] in ('A','C')]
            for k in ('cc_tic_mean','cc_pain_mean','cc_cross_moment','cc_covariance'):self.assertEqual(ac[0][k],ac[1][k])
    def test_complete_ht_equals_cc(self):
        for z in self.r:
            if z['design']=='complete':
                for k in ('tic_mean','pain_mean','cross_moment','covariance'):self.assertAlmostEqual(z['cc_'+k],z['ht_'+k])
    def test_population_reproducible(self):self.assertEqual(self.p,population(self.c))
    def test_replicates_reproducible(self):self.assertEqual(self.r,run(self.c,self.p))
    def test_row_count_and_seed(self):
        self.assertEqual(len(self.r),2400)
        for z in self.r:self.assertEqual(z['seed'],20262019+z['replicate'])
    def test_covariance_independent_centering(self):
        for w in ('A','B','C'):
            t=[z['t'] for z in self.p];p=[z[w] for z in self.p];mt=sum(t)/400;mp=sum(p)/400
            cov=sum((a-mt)*(b-mp) for a,b in zip(t,p))/400
            self.assertAlmostEqual(cov,moments(t,p)['covariance'])
    def test_no_diagnostic_omission(self):
        s=summarize(self.c,self.p,self.r)
        self.assertEqual(s['diagnostic_flags'],[z for z in s['summaries'] if z['diagnostic_flag']])
if __name__=='__main__':unittest.main(verbosity=2)
