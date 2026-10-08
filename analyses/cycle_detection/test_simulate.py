"""Validation of SYNTHETIC benchmark implementation, not clinical validation."""
import unittest
import numpy as np
import simulate as sim


class Tests(unittest.TestCase):
    def test_zero_history_has_no_incremental_cycle_fit(self):
        result = sim.predict_from_history(np.zeros(96))
        self.assertEqual(result['fit_gain'], 0.0)
        self.assertFalse(result['fit_gain'] >= .25)

    def test_constant_history_has_no_incremental_cycle_fit(self):
        for level in (1.0, -2.0, 100.0):
            result = sim.predict_from_history(np.full(96, level))
            self.assertEqual(result['fit_gain'], 0.0)
            self.assertFalse(result['fit_gain'] >= .25)

    def test_linear_history_has_no_incremental_cycle_fit(self):
        for y in (np.arange(96)/100, 2+.012*np.arange(96)):
            result = sim.predict_from_history(y)
            self.assertEqual(result['fit_gain'], 0.0)
            self.assertFalse(result['fit_gain'] >= .25)

    def test_reproducibility(self):
        a = sim.generate('autocorrelated', 3)['observed']
        np.testing.assert_array_equal(a, sim.generate('autocorrelated', 3)['observed'])
        self.assertFalse(np.array_equal(a, sim.generate('autocorrelated', 4)['observed']))

    def test_reporting_nonidentifiability(self):
        a, b = (sim.generate(s, 2) for s in ('fixed_period', 'periodic_reporting_bias'))
        np.testing.assert_array_equal(a['observed'], b['observed'])
        self.assertGreater(np.std(a['latent']-b['latent']), 1)

    def test_exact_clean_period_recovery_and_forecast(self):
        t = np.arange(432)
        y = 2+.01*t+1.5*np.sin(2*np.pi*t/48+.8)
        pred, period, sse, _ = sim.fit_harmonic(y[:384])
        self.assertEqual(period, 48)
        self.assertLess(sse, 1e-20)
        np.testing.assert_allclose(pred, y[384:], atol=1e-10)

    def test_temporal_boundaries(self):
        for n, cuts in [(96, [48]), (192, [96, 144]), (384, [288, 336])]:
            self.assertEqual(sim.inner_origins(n), cuts)
            for cut in cuts:
                self.assertLessEqual(cut+sim.HORIZON, n)

    def test_future_independence(self):
        y = sim.generate('autocorrelated', 2)['observed']
        changed = y.copy()
        changed[192:] += 100000
        a, b = sim.predict_from_history(y[:192]), sim.predict_from_history(changed[:192])
        for key in ('harmonic', 'baseline', 'selected'):
            np.testing.assert_array_equal(a[key], b[key])
        self.assertEqual(a['inner_cv_mse'], b['inner_cv_mse'])

    def test_no_mutation_and_finite_predictions(self):
        for s in sim.SCENARIOS:
            y = sim.generate(s, 0)['observed'][:96]
            before = y.copy()
            pred = sim.predict_from_history(y)
            np.testing.assert_array_equal(y, before)
            for key in ('harmonic', 'baseline', 'selected'):
                self.assertEqual(pred[key].shape, (sim.HORIZON,))
                self.assertTrue(np.isfinite(pred[key]).all())

    def test_reject_missing_values(self):
        y = np.ones(96)
        y[2] = np.nan
        with self.assertRaises(ValueError):
            sim.predict_from_history(y)

    def test_stationary_ar_scale(self):
        y = sim.ar1(np.random.default_rng(10), 50000, .94)
        self.assertLess(abs(np.var(y)-1), .12)
        self.assertLess(abs(np.corrcoef(y[:-1], y[1:])[0, 1]-.94), .015)


if __name__ == '__main__':
    unittest.main()
