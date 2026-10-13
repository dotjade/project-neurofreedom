# Independent audit: adult burden endpoint pass

Date: 2026-10-13. Verdict: **pass within the stated bounded scope; no material numerical or inferential error found.** The main report does not require expansion or correction from this audit.

## Reproducibility

- Re-executed the supplied analysis and its 26 checks without executing its file-writing main block. The output equals the saved output exactly.
- Independently rebuilt the binary classification from primary-source counts, calculated exact rational kappa, and calculated confidence limits by quadratic score-test inversion. All estimates match; interval differences are below 1e-12.
- Jeon: TP 63, FP 25, FN 9, TN 135; agreement 198/232 = 85.3448%; discordance 34/232 = 14.6552% (95% Wilson 10.6807–19.7810%); sensitivity 87.5%; specificity 84.375%; PPV 71.5909%; kappa 1035/1528 = 0.677356. These are pooled, in-sample response-agreement quantities.

The paper's Table 3 prints 0.87 sensitivity, whereas exact published overlaps yield 0.875. The report openly preserves that discrepancy. The script's one-percentage-point tolerance is a loose source-consistency check, not proof of a particular rounding convention; exact-count calculation remains the right result.

Run `python review/independent_checks.py`. Inputs: `reviewer_inputs.json`. Output: `independent_results.json`. The output includes hashes of the inspected worker artifacts and Python/SciPy versions. `verification.log` records the run. No worker analysis or report was edited.

## Source checks

1. [Jeon primary manuscript](https://escholarship.org/content/qt4rg7h4df/qt4rg7h4df.pdf): pp. 6–7 and Tables 3–4 confirm 248 randomized, 232 analyzed, 72/160 reference margins, 60/28 index positives and 48/15 overlaps. The younger trial enrolled ages 9–17 and the nominal adult trial 16–69. A 25% reduction was selected in this pooled sample. The worker correctly avoids calling this adult-only, QoL validation or a severe-state threshold.
2. [McGuire primary manuscript](https://escholarship.org/content/qt8f61z3r0/qt8f61z3r0.pdf): Methods, Results and Tables 1–3 confirm N=519, 101 adults, inclusion of motor/vocal chronic diagnoses, category margins, agreement counts and the printed overlap at TTS 43. No age- or diagnosis-specific accuracy was established. Shared CBIT parent-study citations support treating these analyses as dependent study families, with exact person overlap unknown.
3. [French validation primary report](https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0243912&type=printable): Methods and Tables 3, 6 confirm 109 participants aged 16–64, a six-domain solution, and retest 58 invited/48 returned/19 excluded/29 analyzed. All six extracted ICCs and their intervals match Table 6. The original English four-domain and French six-domain statements are correct. Only the cognitive domain retained the original item grouping. Retest excluded changed participants, so it cannot establish responsiveness.
4. [Cavanna original abstract](https://pubmed.ncbi.nlm.nih.gov/18955683/): confirms development counts 133/192/136 and the four-domain, 27-item instrument. The cited 0.5–0.7 values are interscale correlations. The worker appropriately marks unverified original age and retest details rather than borrowing them from later versions.
5. [Gerasch primary report](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2016.00416/full): Table 2 verifies the treated N=18 means and mean changes, Table 3 the baseline correlations, and Methods the exploratory unadjusted analysis. Tic significance versus QoL nonsignificance is not a test of effect differences. The report correctly makes no causal drug-effect, equivalence or change-correlation claim.
6. [Ivanova primary report](https://link.springer.com/content/pdf/10.1186/s44247-026-00284-7.pdf): Tables 2–3 verify N=31, 17 TS/14 motor-CTD, means and selected standardized-effect intervals. Methods confirm baseline-SD standardization and separate mixed models. The broad published intervals are retained. Multi-df later time tests and parallel mean declines do not identify a particular endpoint contrast or within-person cross-outcome correlation.

## Optional reviewer-only partial-identification result

McGuire's full severe-cell count is not point-identified, but the published margins already impose a useful ceiling. There are 25 CGI-S severe cases and only 3 TTS-model severe classifications, so sensitivity to that reference is at most 3/25 = 12%. The possible severe-overlap count is 0–3. Integer optimization using all category margins and the reported total exact matches confirms both endpoints remain feasible. Analogous bounds are 0–16% for impairment and 0–24% for global severity.

These are mathematical identification bounds, not confidence intervals, patient estimates, adult estimates or external-validation results. They condition on the published model classifications and do not resolve the printed score-43 overlap. No hypothetical contingency table is saved or presented as observed data. This optional result does not need to be added to the main report.

## Interpretation and limits

The report keeps cross-sectional association, stable-status ICC, responsiveness, meaningful change, treatment-effect surrogacy and severity-state classification separate. It does not pool dependent samples, infer paired covariance from marginal SDs, claim diagnosis-specific validity from inclusion, or transfer tic response to QoL response. Its absence conclusions are explicitly limited to this targeted source set.

This audit is not a systematic literature search, a clinical recommendation or independent validation of the instruments. Primary text retrieval succeeded, but the requested PDF screenshot attempts failed; visual-page verification is not claimed. Original Cavanna full methods remain unverified. Source-specific outcome denominators/covariance still limit longitudinal calculations. No full-text papers, individual records or unreported covariance were stored or manufactured; no outreach, paid access or GitHub changes occurred.

## Archived layout

Run the review script from the parent analysis directory with installed NumPy and SciPy (versions recorded in output). It resolves inputs relative to its own file and writes review/independent_results.json. Preserve dated outputs before rerunning with changed inputs. No randomness or seed is used. The directory reference was adjusted for the repository layout and the script rerun successfully before archival.
