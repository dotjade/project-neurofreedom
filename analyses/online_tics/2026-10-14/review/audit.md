# Independent ONLINE-TICS audit

Checked 14 October 2026. Source inspection and arithmetic were independent of the main extraction. This is an original audit of published aggregates, not a replication of the trial model. No source full text or participant data are retained here.

## Decision

The primary superiority claim does not pass. The appropriate statement is that the prespecified primary test did not establish superiority. This does not establish zero benefit, equivalence, or the absence of a worthwhile effect.

## Primary-source verification

- Haas et al., [main report](https://doi.org/10.3390/jcm11010250), Tables 3–4 and §§2.1–2.4, 3.1–3.2: primary iCBIT-minus-psychoeducation YGTSS-TTS difference −1.28, 95% CI [−2.58, 0.01], p=.053. Randomized n=161 (67/70/24). Nominal ITT uses an MMRM with a missing-at-random assumption; LOCF appears in secondary/sensitivity analyses.
- Compliance is distinct from outcome availability: 108 compliant; 53 noncompliant comprises 42 missing-visit and 11 insufficient-session cases. Nine further follow-up dropouts are reported. Exact outcome-by-visit observed/model-contributor Ns were not supplied in the inspected main report.
- V3 is one week after treatment; V4/V5 are three/six months afterward. Nominal beneficial contrasts: TTS V4/V5; impairment V3/V5; GTS-QOL V4/V5. No uniform benefit across all outcomes and times.
- NI is explicitly exploratory in §3.2: estimate 0.98, CI [−1.01, 2.96], margin 3. Main-report V5 impairment table upper bound is −1.54; prose prints +1.54.

## Protocol cross-check

Jakubovski et al., [protocol](https://doi.org/10.3389/fpsyt.2016.00119), Primary/Secondary Analyses: confirmatory NI is permitted only after primary superiority succeeds; one-sided alpha=.025 and margin 3. The feasibility-driven face-to-face arm was not powered for NI. Other secondary comparisons have no reported comprehensive multiplicity procedure. Protocol treatment length is ten weeks; the main report says eight weeks. Preserve post-treatment visit timing rather than silently resolving that discrepancy. Protocol abstract registration is inconsistent with its body: use NCT02605902, as in the body and main report, not abstract NCT02413216.

## Interpretation and reproducibility checks

1. Run `python3 audit_checks.py`. Decimal arithmetic independently checks all nine selected estimate/CI pairs, the hierarchy, rounded compliance percentages, and a nine-comparison Holm/Bonferroni sensitivity. Both methods retain TTS V4/V5, impairment V5 and GTS-QOL V4 at .05. This family was selected after publication and is narrower than all trial tests. These are sensitivity calculations, not confirmatory findings. The p<.001 entry is kept as an upper bound, not silently treated as an exact p-value.
2. The primary CI includes zero and favorable differences; do not convert failure to reject into evidence of equivalence. The exploratory NI bound clears margin 3 by only 0.04 points, and the failed hierarchy precludes confirmatory NI regardless.
3. Larger later point estimates do not establish a statistically tested increase in treatment effect over time. Cross-time covariance is unavailable. The separate MMRMs described in Figure 1 should not be treated as independent time-point samples.
4. Group-average TTS, impairment and QoL contrasts cannot establish that the same individuals improved on all three. No joint responder computation is identified by these aggregates.
5. For scale direction, an independent [primary study's Methods](https://doi.org/10.3389/fnins.2016.00416) explicitly defines high GTS-QOL as worse and high GTS-QOL-VAS as better. Accordingly, ONLINE-TICS's negative VAS contrast at V3 points away from iCBIT under standard scoring. Preserve a coding caveat because trial-specific VAS coding was not independently supplied. Do not combine VAS with disease-specific GTS-QOL or claim uniform QoL improvement.

## Main-artifact review

The main worker's `aggregate_inputs.json`, `aggregate_checks.py`, `aggregate_checks.json`, and `computation_plan.md` were reviewed. All nine numerical input rows match the independently extracted source values. The worker's audit function was rerun without writing to its directory: all 33 checks passed. Every central/bounded Holm and Bonferroni value matches this audit's separate Decimal implementation. Reporting-precision envelopes preserve all four retained decisions. No numerical discrepancy found. Hashes and review results are in `main_artifact_review.json`. The final core-trial narrative and structured extraction were also reviewed. Suggested replacements of “null” with inconclusive/interval-includes-zero language and prose-spacing fixes were verified. No blocking discrepancy remains. This audit did not independently repeat the worker’s repository-context reads, full registry history, comprehensive correction search, or proposed next-study verification.
