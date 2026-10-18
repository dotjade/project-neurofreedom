# CBIT maintenance: response-selected follow-up, with incomplete ascertainment

Project NeuroFreedom | 15 October 2026 | Wilhelm et al. 2012 | Historical trial audit

## Decision

Retain evidence of acute tic improvement and a narrower **maintenance signal among returning acute responders in a booster-inclusive program**. Do not describe the six-month result as an 80% response rate among everyone randomized, an adult-only estimate, remission, off-treatment efficacy, disease modification, or cure.

The [prediction](prespecified_question.md) was recorded before extracting new trial sources. The evidence supports its principal restriction: the acute randomized comparison and the follow-up answer different questions. This bounded original-trial analysis is complete; the absent follow-up outcomes cannot be recovered by arithmetic.

## Source and denominator audit

[Wilhelm et al.](https://jamanetwork.com/journals/jamapsychiatry/fullarticle/1307556), Archives of General Psychiatry 2012;69(8):795–803, DOI 10.1001/archgenpsychiatry.2011.1528; [PMID 22868933](https://pubmed.ncbi.nlm.nih.gov/22868933/); [PMCID PMC3772729](https://pmc.ncbi.nlm.nih.gov/articles/PMC3772729/); NCT00231985. The journal issue is August 2012, dated August 1; PMC manuscript availability is September 13, 2013. These are not new 2026 results. The manuscript title uses “Tourette’s Disorder,” whereas the final publication uses “Tourette Syndrome.”

| Population/visit | CBIT | Psychoeducation/supportive therapy (PST) |
|---|---:|---:|
| Randomized | 63 | 59 |
| Acute efficacy analyzed, Figure 1 | 60 | 53 |
| Completed acute phase | 56 | 49 |
| Exited acute phase | 7 | 10 |
| Acute CGI-I positive, randomized denominator | 24/63 | 4/59 |
| Acute responders assessed at three months | 15/24 | 2/4 |
| Three-month CGI-I positive, assessed denominator | 13/15 | 1/2 |
| Acute responders assessed at six months | 15/24 | 2/4 |
| Six-month CGI-I positive, assessed denominator | 12/15 | 1/2 |

Sources: final paper Results and Table 4; [PMC Figure 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC3772729/figure/F1/), visually inspected. The continuous-outcome model includes participants with a postrandomization visit, assumes missing at random, and adjusts for site/baseline. Its 113 analyzed participants differ from both 122 randomized and 105 completers. CGI-I response means ratings 1 or 2, not tic absence.

Responders in both arms were offered three monthly boosters. Actual individual booster completion and continued practice are not established here. PST nonresponders could receive CBIT. Consequently, there is no preserved randomized between-arm comparison after week 10. The two-stage selection of acute responders and then returnees must stay visible.

## Executed missing-outcome analysis

The [plan](computation_plan.md), [aggregate inputs](aggregate_inputs.json), [Python code](aggregate_checks.py), [output](aggregate_checks.json) and [run log](execution_log.txt) preserve a deterministic enumeration of every possible number of positive outcomes among missing acute responders. No participant records, stochastic simulation, imputed observed outcomes, or model-based efficacy reanalysis were used.

Let A be acute responders, O assessed at a follow-up, R positive among those assessed, and M=A−O unknown. The available-case proportion is R/O. The documented-positive proportion among all acute responders is R/A. Without assumptions about missing status, the latter population's true visit-specific proportion lies between R/A and (R+M)/A.

| Follow-up | Available-case result | Ascertainment among acute responders | Documented positive among acute responders | Missing-outcome bounds among acute responders |
|---|---:|---:|---:|---:|
| CBIT, three months | 86.67% | 62.50% | 54.17% | 54.17–91.67% |
| CBIT, six months | 80.00% | 62.50% | 50.00% | 50.00–87.50% |
| PST, three months | 50.00% | 50.00% | 25.00% | 25.00–75.00% |
| PST, six months | 50.00% | 50.00% | 25.00% | 25.00–75.00% |

These are **finite-cohort identification bounds, not confidence intervals**. They express what nine unknown CBIT outcomes or two unknown PST outcomes could change. They do not include sampling uncertainty, measure error, or a causal correction for response selection. A binomial confidence interval for the 15 returning acute CBIT responders would not solve the missingness problem, so none is substituted here.

At six months, the difference between 80% and 50% is the denominator, not conflicting observed outcomes: both use the same 12 positives. Calling the other nine “failures” would assert something the evidence does not show. Equally, applying the returnees' 80% to all 24 acute responders assumes something about missingness that the data cannot establish.

To reach or exceed 80% among all 24 acute responders, at least eight of the nine missing participants would have to be positive: 20/24=83.33%; seven would give 19/24=79.17%. This is an explicitly hypothetical sensitivity calculation using the quoted available-case result as a benchmark, not a clinical response threshold or a prediction of missing outcomes.

Twelve of the original 63 assigned to CBIT were documented positive both acutely and at six months: 19.05%. That is a documented acute-and-later-positive fraction, **not** an estimate of the overall six-month response rate. Acute nonresponders' later response is outside the reported maintenance sample. Separate visit totals also do not identify uninterrupted benefit, recurrence between visits, or individual joint response at both follow-ups.

Thirty-seven implementation checks passed, including rational-arithmetic bounds, exhaustive missing-count endpoints, input constraints and manual expected values. Reproduction is: `python aggregate_checks.py`. The output is deterministic; no random seed applies. [Independent verification](review/independent_review.md) reproduced the output byte-for-byte and passed 49 additional count/rational-arithmetic/scenario checks; this is computational/source verification, not independent clinical validation.

## Acute benefit and burden remain distinct

The published adjusted week-10 tic-severity advantage is 3.3 YGTSS-TTS points, 95% CI 1.4–5.2, p<.001; effect size 0.57. Impairment is a separate 0–50 scale, with a reported adjusted advantage of 3.9 points, 95% CI 0.5–7.2, p=.03. These are reported adjusted contrasts; do not reconstruct them by subtracting rounded endpoint means. The [registration](https://clinicaltrials.gov/study/NCT00231985) lists week-10 tic severity as primary and impairment as secondary. The paper does not adjust secondary comparisons for multiplicity. [Final paper, Table 2 and Statistical analysis](https://jamanetwork.com/journals/jamapsychiatry/fullarticle/1307556).

The original maintenance table supplies CGI-I response, not direct six-month impairment or disease-specific quality-of-life effects. Improvement on the tic scale therefore cannot fill those gaps. This is a limitation of this report's outcomes, not proof that no functional measurements exist elsewhere in the trial program. The 2019/2020 secondary report below is a specific route to testing that separate question.

Applicability is restricted: ages 16–69 include minors; an age-18-and-over subgroup was not verified. Six screened people had TTS above 30, of whom only three were enrolled after panel review. That selection, plus stability requirements for medication/comorbidity and the English/IQ eligibility restrictions, limits extrapolation to adults with very severe tics or clinically unstable presentations. Mean age or a journal title cannot remove those restrictions.

## Discrepancies, negative findings and safety limits

- The final abstract and PubMed repeat PST 4/63 (6.4%); the body, allocation and tables support 4/59 (6.8%). Even 4/63 ordinarily rounds to 6.3%. This audit uses the internally supported body denominator and retains the conflict.
- Six-month prose juxtaposes CBIT 12/15 and PST 1/4, mixing an available-case denominator with all acute responders. Table 4 permits like-denominator descriptions, but still not a causal post-selection comparison.
- The reported acute NNT is 5. The simple reciprocal of 24/63−4/59 is 3.1933, whose ceiling is 4. This diagnostic arithmetic does not recover the authors' calculation or establish a corrected clinical estimate. The discrepancy is retained in the output rather than silently reproducing 5.
- The PMC manuscript gives impairment decreases of 36%/22% and different baseline medication percentages; the final journal gives 38.2%/23.3% and 17/63 versus 14/59 taking tic medication. Final-published values take priority where versions differ. No claim of a comprehensive version diff is made.
- Null moderator tests do not establish equal treatment effects across medication status or initial severity. Absence of a verified adult-only subgroup prevents an adult-only efficacy estimate.
- The paper reports 224 adverse events and three serious events judged unlikely related. Tic worsening occurred in four participants in each arm. Event totals and affected-person counts differ; a small, short trial cannot establish absence of rare harms or compare long-term safety. This audit contains no individual treatment recommendation.

## Next bounded scientific decision

Close this original-trial maintenance and aggregate-missingness pass unless corrected reporting or newly available follow-up outcomes change the inputs. Do not rerun unchanged bounds or launch participant collection.

Next inspect [McGuire et al., PMID 31451122](https://pubmed.ncbi.nlm.nih.gov/31451122/), DOI 10.1017/S0033291719002150, electronically published August 27, 2019 and issued September 2020. This is a **same-trial secondary report**, not independent replication or a new 2026 paper. Ask whether randomized acute CBIT–PST effects on disability/social/family functioning support broader benefit, separating those contrasts from responder-versus-nonresponder associations and selected follow-up. Extract instrument-specific direction, denominators, uncertainty, multiplicity and negative findings before computing anything. Do not substitute functional measures for GTS-QOL or claim a tic-to-function causal pathway. Stop if the relevant comparisons lack usable numerical detail. That is a prospective next task, not an analysis completed here.

## Provenance and limits

The repository README, protocol, status and October 14 ONLINE-TICS report were read first via GitHub; blob identifiers, exact searches, dates and access limitations are in [provenance.json](provenance.json). The final JAMA HTML, PubMed metadata, current registry API and PMC flow figure were inspected. PMC access varied by route; one ordinary HTTP fetch succeeded, while web retrieval and a later HTTP fetch returned a browser-check page. No security challenge was bypassed. The Europe PMC full-text XML request failed. No full paper is included in these deliverables.

The live registry remains completed, enrollment 122, last update posted February 9, 2012, without posted aggregate results. Current fields support identification but do not replace a historical protocol/version audit. Limited correction/retraction searches and the inspected PubMed record revealed none; this is not comprehensive clearance. Funding was principally NIMH with Tourette Syndrome Association support; relevant manual royalties and professional honoraria were disclosed. No patient data, private information, outreach, medical intervention, public upload or GitHub write occurred in this task.
