import json
import unittest
from fractions import Fraction as F
from pathlib import Path
from analyze import analyze_timepoint, compute, full_mean, pack, rounding_envelope

ROOT=Path(__file__).resolve().parent


class AggregateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inputs=json.loads((ROOT/"inputs.json").read_text())
        cls.result=compute(cls.inputs)
        cls.w4,cls.m3=cls.result["branches"][0]["timepoints"]

    def test_counts(self):
        self.assertEqual((self.w4["n_missing"],self.m3["n_missing"]),(5,26))

    def test_retention(self):
        self.assertEqual(self.m3["observed_fraction"],F(15,41))

    def test_paired_and_unpaired_baselines_remain_distinct(self):
        self.assertEqual(self.m3["returnee_paired_change"],F("-3.4"))
        self.assertEqual(self.m3["unpaired_observed_minus_full_baseline"],F("-3.29"))
        self.assertNotEqual(self.m3["returnee_paired_change"],self.m3["unpaired_observed_minus_full_baseline"])

    def test_three_month_bounds_exact(self):
        self.assertEqual(self.m3["full_change_lower"],F(-53347,4100))
        self.assertEqual(self.m3["full_change_upper"],F(11653,4100))

    def test_tipping_point_gives_exact_zero(self):
        self.assertEqual(full_mean(41,15,F("15.33"),self.m3["tipping_missing_followup"])-F("18.62"),0)

    def test_missing_change_tipping_does_not_need_full_baseline(self):
        other=self.result["branches"][1]["timepoints"][1]
        self.assertEqual(self.m3["tipping_missing_change"],F(51,26))
        self.assertEqual(other["tipping_missing_change"],self.m3["tipping_missing_change"])

    def test_no_change_missing_weighted_paired_effect(self):
        s=next(x for x in self.m3["scenarios"] if x["name"]=="missing_no_mean_change")
        self.assertEqual(s["full_change"],F(-51,41))

    def test_two_point_worsening_erases_improvement(self):
        s=next(x for x in self.m3["scenarios"] if x["name"]=="missing_mean_worsening_2")
        self.assertTrue(s["feasible"])
        self.assertEqual(s["full_change"],F(1,41))

    def test_same_change_and_same_outcome_are_different(self):
        ss={x["name"]:x for x in self.m3["scenarios"]}
        self.assertEqual(ss["same_change_as_observed"]["full_change"],F("-3.4"))
        self.assertEqual(ss["same_followup_as_observed"]["full_change"],F("-3.29"))

    def test_four_week_tipping_is_outside_scale(self):
        self.assertGreater(self.w4["tipping_missing_followup"],25)
        self.assertFalse(self.w4["tipping_feasible"])

    def test_both_branches_same_sign_identification(self):
        for b in self.result["branches"]:
            self.assertTrue(b["timepoints"][0]["direction_robust_to_scale_bounded_missingness"])
            self.assertFalse(b["timepoints"][1]["direction_robust_to_scale_bounded_missingness"])

    def test_rounding_cannot_reconcile_baseline(self):
        self.assertFalse(self.result["baseline_consistency"]["rounding_intervals_overlap"])

    def test_rounding_does_not_change_qualitative_result(self):
        for b in self.result["branches"]:
            self.assertLess(b["timepoints"][0]["rounding_envelope_not_ci"]["full_change_upper"],0)
            self.assertGreater(b["timepoints"][1]["rounding_envelope_not_ci"]["full_change_upper"],0)
            self.assertLess(b["timepoints"][1]["rounding_envelope_not_ci"]["tipping_missing_change_upper"],2)

    def test_bounds_monotonic_in_missing_mean(self):
        vals=[full_mean(41,15,F("15.33"),F(x)) for x in range(26)]
        self.assertTrue(all(a<b for a,b in zip(vals,vals[1:])))

    def test_complete_followup_has_point_bound(self):
        t=analyze_timepoint(10,10,F(0),F(25),F(18),F(18),F(15))
        self.assertEqual(t["full_change_lower"],F(-3))
        self.assertEqual(t["full_change_upper"],F(-3))
        self.assertIsNone(t["tipping_missing_followup"])

    def test_invalid_count_rejected(self):
        with self.assertRaises(ValueError): analyze_timepoint(10,11,F(0),F(25),F(18),F(18),F(15))

    def test_out_of_scale_input_rejected(self):
        with self.assertRaises(ValueError): analyze_timepoint(10,5,F(0),F(25),F(18),F(18),F(26))

    def test_impossible_baseline_partition_rejected(self):
        with self.assertRaises(ValueError): analyze_timepoint(10,9,F(0),F(25),F(1),F(20),F(15))

    def test_saved_output_matches_recomputed(self):
        self.assertEqual(json.loads((ROOT/"results.json").read_text()),pack(self.result))


if __name__=="__main__": unittest.main(verbosity=2)
