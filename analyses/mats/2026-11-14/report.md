# Adult measurement lead audit: 14 November 2026

## Question and advance plan

Does a newly inspected adult MATS conference abstract provide the calibrated, invariant anchor or validated treatment prediction required by the latest measurement plan? Prediction: no. Direct calibration/invariance testing or prospectively held-out treatment prediction with uncertainty would challenge that prediction. This decision rule was recorded at 2026-11-14T02:42:42.019Z, before the numerical calculation. This is a published-aggregate audit, not a simulation or patient-data analysis.

## Source and classification

The [official ABCT abstract](https://abct2026.eventscribe.net/fsPopup.asp?PosterID=836632&mode=posterInfo), by Liu, Pine and McGuire, describes 51 adults with self-reported TS, recruited through an online support-group survey. MATS has 70 items; total alpha is .95, while the situational subscale alpha is .57. Reported total-score correlations are .40 with impairment and .12 with tic severity. This is preliminary conference evidence, not a peer-reviewed full article or treatment trial. The November 14 09:30 ET presentation was still scheduled in the future at this early-UTC check; publication of the abstract is verified, delivery of the presentation is not. No participant content was collected.

A [Johns Hopkins institutional listing](https://hour.jhu.edu/wp-content/uploads/2024/12/dreams-by-year.pdf), PDF page 48, already names a MATS construction project. It supplies no cohort identity or numerical results. It warns against claiming the scale was first created today; it is not independent validation. Targeted title searches found no separately verified full publication. GitHub MATS search returned no matches, with code-index limitations acknowledged.

## Reproducible calculation

For descriptive sensitivity only, apply Fisher's z transform to the two rounded correlations, assuming all 51 respondents supplied each complete pair. Approximate 95% interval: tanh(atanh(r) +/- 1.959963984540054/sqrt(n-3)). This complete-pair assumption is unverified; missingness and correlation type are not resolved by the abstract. The approximation assumes independent observations and an appropriate correlation sampling model. No random seed is needed.

- Impairment r=.40: 0.139830 to 0.608506.
- Tic severity r=.12: -0.160905 to 0.382920.

The arithmetic ran in hosted JavaScript. [Source](fisher.mjs), [inputs](inputs.json), and [actual output](output.json) are retained. Two sign/overlap assertions passed. A standalone Node command is provided for reproduction, but no Node execution is claimed in this run.

## Interpretation and counterevidence

The positive impairment association is retained. The severity interval spans zero and a positive association of meaningful size; a nonsignificant point estimate is not proof of no relationship. These two correlations share an outcome and respondents. Their difference cannot be tested as independent estimates, and interval overlap does not test that difference. The missing impairment/severity correlation and paired sample counts prevent a valid dependent-correlation contrast.

High internal consistency is neither retest stability nor invariance across context/treatment, and it does not calibrate a self-report scale to latent urge generation or control. The inspected abstract supplies no prospective prediction of CBIT benefit, randomized transfer test, or direct calibration. This is absence of those tests in the available abstract, not proof the instrument cannot eventually be useful.

## Decision and limits

The new lead does not reopen closed H18 identification work. Do not add these respondents to other cohorts or infer nonoverlap. Severe persistent adult burden and co-occurring conditions remain central; this selected survey cannot represent all adults or establish pediatric applicability. No tic-suppression activity or treatment recommendation follows.

Next informative safe step: inspect a lawful full instrument/methods publication with paired denominators, scoring, correlation type, missingness, external calibration or prospective prediction. Do not rerun this calculation without a changed input. New human-subject validation would need separate clinician/institutional/ethics review; no outreach, collection, intervention or paid resource was used.
