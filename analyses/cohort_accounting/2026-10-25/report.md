# Five report-role counts are not five independent samples

25 October 2026 | Conditional published-aggregate set accounting, not patient data or simulation

## Question and decision

Can adding the five selected report-role counts in the linked DBS evidence chain establish a number of independent people or clinical replications? **No.** The reports name two trial families, and one preprint combines them. Nesting and different count roles invalidate addition. This new weekly calculation formalizes the overlap consequence; it does not repeat the daily exact-rank, endpoint, registration-history or outcome audits.

The [prediction and stopping rules](prediction.md) were written before constructing the input and running the code. This is a local pre-analysis specification, not externally registered research. A third independent recruitment universe or unlinked participants would disconfirm the fixed two-family model. Source identities, count roles, assumptions and access limits are in [inputs.json](inputs.json).

## Inputs and methods

| Report | Count used | Role and trial link |
|---|---:|---|
| [Cagle 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9468946/) | 4 | Embedded-device analysis within NCT02056873 |
| [Okun 2024](https://www.nature.com/articles/s41598-024-57071-5) | 10 | Enrolled NCT02056873 cohort, not functional paired n |
| [Lowor 2025](https://doi.org/10.1002/mds.70043) | 5 | Physiology contributors, from six implanted, NCT05371041 |
| [NCT05371041 results](https://clinicaltrials.gov/study/NCT05371041) | 8 | Actual enrollment, not every outcome denominator |
| [Lowor 2026 preprint](https://pmc.ncbi.nlm.nih.gov/articles/PMC13596655/) | 16 | Distinct subjects described as drawn from the two named studies |

The preprint is preliminary, DOI 10.21203/rs.3.rs-10832475/v1, dated September 20, not a new weekly publication. Its primary indexed Methods were checked again; the direct PMC route returned a challenge. The existing primary-source daily audits establish the other report roles; independent review also checked current server-projected registry enrollment and newer-trial eligibility. No individual result tables, identity matching or recording files were used. No full-text paper is retained.

Let the two enrollment universes have sizes a=10 and b=8. If the preprint's m=16 distinct subjects are a subset of their union, then max(a,b,m) <= union <= a+b. Integer enumeration retains overlaps k satisfying 0 <= k <= min(a,b) and a+b-k >= m. Under an additional disjointness assumption, enumerate preprint allocations x and m-x with 0 <= x <= a and 0 <= m-x <= b.

These are **conditional documentation bounds**. Trial identifiers and current enrollment totals do not themselves verify exact participant membership or completeness. The newer protocol's prior-DBS exclusion supports disjointness conditional on adherence, but is not identity verification. If containment fails, the union bounds do not apply. Counts were selected for this known overlap chain, not a systematic sample of all DBS research.

## Actual results and counterchecks

- Five report-role records resolve to two named trial families. Neither number measures independent efficacy replications.
- The deliberately invalid role sum is **43**. It mixes enrollment and analysis roles, so it is not a valid study sample or a denominator for a duplication percentage.
- With containment and the 16-person preprint, but without assuming disjointness, the union is bounded **16–18**, with possible cohort intersection **0–2**.
- With disjointness additionally assumed, the combined enrollment universe is **18**; the preprint could allocate **8/8, 9/7 or 10/6** to older/newer trials. These are feasible counts, not identified actual memberships.
- If the preliminary mixed report is omitted and disjointness is not assumed, the union bound widens to **10–18**. Thus the tighter lower bound depends on preliminary source coding.
- An impossible mixed count of 19 is rejected by the code, not silently repaired.

No outcome, response rate, safety rate, pooled effect, confidence interval, probability or power calculation follows. In particular, 18 is not a functional-outcome analysis n. The same participants can contribute complementary measurements without supplying independent replication; this does not erase the value of those measurements. Disjoint cohorts alone would not make different estimands comparable.

## Reproduce and limits

Python standard library; no random sampling and no seed. From this directory:

    python analyze.py
    python -m unittest test_analysis -v

[Results](results.json), [code](analyze.py), [13 implementation tests](tests.log), and [independent review](review/independent_review.md) are archived. The review uses separate arithmetic and checks source assumptions, not clinical peer review. All numerical outputs are deterministic set constraints, not simulated patient outcomes.

Close this fixed report-accounting exercise. Reopen only if corrected enrollment, explicit recruitment provenance or another public cohort link changes the graph. Do not seek identities or participant rows. For an efficacy or functional comparison, use a compatible aggregate estimand and uncertainty from its own analysis population; more report titles cannot repair missing endpoint information. The next scheduled primary-only task remains the YGTSS validation population/measurement audit, not another generic DBS cohort search.
