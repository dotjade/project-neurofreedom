"""Original source-to-claim extraction, with aggregate metadata only."""
from pathlib import Path
import json
P=Path(__file__).parent
paper='https://movementdisorders.onlinelibrary.wiley.com/doi/10.1002/mds.70043'
registry='https://clinicaltrials.gov/api/v2/studies/NCT05371041'
protocol='https://cdn.clinicaltrials.gov/large-docs/41/NCT05371041/Prot_000.pdf'
sap='https://cdn.clinicaltrials.gov/large-docs/41/NCT05371041/SAP_001.pdf'
rows=[
 ('population','Adults aged 19–32; six implanted and five physiology contributors.',paper,'Methods: Participants; Data Analysis; Results: Electrophysiology and Structural Imaging','verified','Eligibility age range is not the observed sample age range; no table rows retained.'),
 ('trial','NCT05371041.',paper,'Methods: Participants; reference 19','verified','Do not merge this identifier with NCT02056873.'),
 ('state','Rest, cued hand movement and unrestricted tic conditions; synchronous bilateral CM/aGPi recording.',paper,'Electrophysiological Recordings; Postoperative Visits and Behavioral Tasks','verified','Selected comparison conditions are not a randomized causal intervention.'),
 ('window','Methods initial three months; abstract nine monthly visits; therapy begins month four.',paper,'Abstract Methods; Postoperative Visits and Behavioral Tasks; Figure 1','unresolved analysis-window discrepancy','No visit-by-visit analysis contribution inventory was verified.'),
 ('protocol_window','Physiology focus months 1–3; optimization months 4–9; physiology allowed at all protocol visits; intraoperative test stimulation possible.',protocol,'Research Plan; Surgical Procedure; Study Visits','verified planned design','A protocol does not establish which epochs the publication analyzed.'),
 ('epochs','Onset-centered two-second epochs with overlap; tic subtypes pooled.',paper,'Data Analysis','verified','Post-onset information prevents interpreting this analysis as an evaluated pre-onset predictor.'),
 ('power','Low-frequency tic-related increases; higher-frequency features not consistently preserved.',paper,'Results: Low-Frequency Power','reported','No participant-level effect reconstruction or general absence claim.'),
 ('coherence','Low-frequency intra/interhemispheric coherence differences; reported beta/low-gamma coherence nulls.',paper,'Results: Relationship between Thalamus and Pallidum; Figure 4','reported','Coherence magnitude, PSI and phase consistency must not be conflated.'),
 ('direction','Low-frequency phase lead attributed to CM.',paper,'Results: Phase Synchrony','reported association','Temporal phase lead does not identify a causal driver, direct connection, or beneficial intervention.'),
 ('counterevidence','Results report low-gamma interhemispheric phase features; Discussion makes broader low-gamma phase-null statement.',paper,'Final paragraph of Results: Phase Synchrony; Discussion paragraph beginning Because no significant','internal inconsistency retained','Reject a blanket no-high-frequency-effect summary.'),
 ('unit','Group feature averaging followed by rank tests per time-frequency pair; exact independent unit and epoch counts unresolved.',paper,'Final two paragraphs of Data Analysis','insufficient specification','Cannot infer participant-level precision or identify actual tested unit from the description.'),
 ('math','Exact two-sided signed-rank minimum at five independent nonzero distinct-rank pairs is 0.0625.','check_testing_unit.py','Post-reading exhaustive sign enumeration','executed original diagnostic','Not preregistered; not an audit of the authors actual calculation; not a clinical-effect result.'),
 ('registry_design','Eight actual enrollees; single-group, unmasked device feasibility; results first posted 2026-09-25.',registry,'protocolSection.designModule; statusModule; hasResults','verified historical linked result','Different denominator and estimand from five-person physiology analysis; not a new-window result.'),
 ('overlap_gate','Prior DBS/neurosurgery is excluded, including explanted DBS.',protocol,'Inclusion and Exclusion Criteria','verified planned eligibility','Supports distinctness from earlier implant cohort conditional on adherence, not identity-level proof.'),
 ('registry_safety','Serious affected 3/8; other affected 8/8; deaths 0/8; approximately two-year follow-up; non-systematic assessment.',registry,'resultsSection.adverseEventsModule.eventGroups, timeFrame, assessmentType','verified published aggregates','Occurrence not causality; does not contradict an earlier shorter-window report by itself.'),
 ('outcome_metadata','Clinical outcome construct and time origin require reconciliation before any effect calculation.',registry,'outcomesModule; baselineCharacteristicsModule measure descriptions; outcomeMeasuresModule group description','unresolved','No individual result rows retained or analyzed.'),
 ('sap','Dated 2021-12-20; manuscript-specific clinical paired endpoint analysis paragraph present.',sap,'Statistical Analysis Plan','verified document content','Does not establish preregistration of this physiology analysis.'),
 ('access','Paper offers reasonable-request access; registry IPD plan says NO.',paper+' ; '+registry,'Data Availability Statement; ipdSharingStatementModule','both verified','Different scopes may explain difference; neither grants data access.'),
 ('later_overlap','2026 Research Square preprint names NCT02056873 and NCT05371041 and 16 pooled participants.','https://pmc.ncbi.nlm.nih.gov/articles/PMC13596655/','Methods: Subjects; Ethical Disclosures','verified indexed primary manuscript','Not peer-reviewed; exact intersection not established; not independent replication.'),
]
mat=[dict(zip(['id','claim','source','location','status','limit'],r)) for r in rows]
(P/'source-claim-matrix.json').write_text(json.dumps(mat,indent=2,ensure_ascii=False)+'\n')
record={
 'date_checked':'2026-10-20','evidence_type':'primary_study','review_scope':'bounded full-methods, recording-state and cohort audit',
 'id':'pmid:40977255','title':'The CM-aGPi Network in the Generation of Tics in Tourette Syndrome',
 'authors_year':'Lowor et al., 2025','url':'https://pubmed.ncbi.nlm.nih.gov/40977255/','doi':'10.1002/mds.70043','pmcid':'PMC12710177','nct':'NCT05371041',
 'first_publication':'2025-09-22','design':'Observational intracranial physiology substudy within an implanted-device feasibility trial.',
 'population':'Selected medically refractory adults; implanted age range 19–32 years.',
 'n':{'implanted':6,'physiology_analyzed':5,'localization_exclusion':1},
 'baseline_severity':{'measure':'YGTSS total including impairment, out of 100','mean':91.5,'sd':3.8,'population':'six implanted participants; not the five-person analytic subset'},
 'followup':'Nine-visit protocol; main methods describe the initial three postoperative months without recording-time stimulation. Therapy starts in month four; actual visit contributions remain unresolved.',
 'attrition':'Six completed the initial three-month postoperative visits. One physiology localization exclusion leaves five analyzed; this is an analysis exclusion, not reported dropout. Later visit-level completeness is not established.',
 'adverse_events':{
  'paper':'The paper reports no severe or adverse events during the initial three-month postoperative window in six participants; do not extend that statement to all nine months.',
  'linked_registry':'Separate NCT05371041 results for eight participants report serious events affecting 3/8, other events 8/8 and deaths 0/8 from enrollment through approximately two years after lead implantation, using non-systematic assessment. Occurrence is not causal attribution.'
 },
 'applicability':'Selected severe, medically refractory implanted adults; limited generalization beyond this small surgical cohort. No pain/function mechanism or broad adult natural-history inference.',
 'reviewer':'AI-assisted primary-source extraction; separate independent source/methods review linked, not formal clinical peer review.',
 'review_artifacts':['review/independent_review.md','review/check_exact_rank_bound.py'],
 'claim_supported':'Tic-associated low-frequency activity and connectivity in simultaneously recorded CM/aGPi add a distinct state contrast relative to earlier audited thalamocortical work, with unresolved analysis-window and testing-unit details.',
 'comparators':['rest','cued voluntary hand movement','unrestricted tics'],
 'key_result':'Tic-associated low-frequency CM/aGPi power and synchrony; CM phase lead reported.',
 'uncertainty':'Recording-window and testing-unit ambiguity; small selected sample; no participant-level contrast CI reconstructed.',
 'negative_and_conflicting_evidence':'Beta/low-gamma coherence nulls coexist with low-gamma interhemispheric phase findings; broad Discussion phase-null wording conflicts.',
 'inference_not_supported':['causal generator','validated pre-tic predictor','stimulation-free natural history','efficacy','cure'],
 'related_cohort_ids':['NCT05371041','NCT02056873: prior measurement comparator, distinct trial','pmid:42780243: mixed-trial preprint overlap'],
 'data_access':'Author request statement; registry IPD sharing NO; no granted access.',
 'funding_conflicts':'NIH funding; investigational devices supplied by Medtronic; article reports no competing interests.',
 'retrieval_status':'Publisher full HTML inspected; linked official registry/protocol/SAP inspected; full supplement unavailable.',
 'correction_retraction_check':'No notice identified in inspected views and exact-DOI targeted search; bounded check only.',
 'next_verification_task':'Reconcile exact trial clinical outcome construct/time origin using aggregate public metadata; physiology unit/window remains unresolved.'
}
(P/'evidence-record.json').write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n')
(P/'evidence-record.jsonl').write_text(json.dumps(record,ensure_ascii=False,separators=(',',':'))+'\n')
structured={
 'question':'Does the historical paper add a nonduplicated mechanism test with verified adult coverage and recording state?',
 'prediction':'Full methods and trial links should distinguish an additional two-deep-target state comparison from duplicate thalamocortical observations; stronger causal/prediction inference requires additional gates.',
 'method':'Bounded primary-source full-methods, official trial/protocol, cohort-family and statistical-unit audit.',
 'actual_finding':'Adult age gate and full-main-methods gate pass. A distinct CM–aGPi contrast is documented, while exact visit inclusion and independent test units remain unresolved.',
 'counterevidence':['Metric-specific higher-frequency nulls coexist with low-gamma phase positives.','Voluntary movement is not matched to every tic subtype.','The windows contain post-onset information.','Trial therapies and possible surgical testing prevent a never-stimulated interpretation.'],
 'decision':'Retain one qualified historical physiology source; no causal, validated-prediction or natural-history promotion.',
 'next_step':'Bounded public aggregate outcome-definition/timepoint/protocol reconciliation for NCT05371041; stop at unresolved prerequisites.',
 'authorization_boundary':'No participant datasets, individual outcome extraction, contact, intervention, enrollment or external write.',
 'analysis_type':'Original evidence-structure audit plus a post-reading no-data combinatorial diagnostic; no patient effect reanalysis.'
}
(P/'structured-audit.json').write_text(json.dumps(structured,indent=2,ensure_ascii=False)+'\n')
log={
 'date_utc':'2026-10-20','approximate_work_window_utc':'02:47–03:00',
 'repository_reads':[
  {'path':'README.md','sha':'4c3bafbd09ca4073d183cef267c746afa09147bf'},
  {'path':'RESEARCH_PROTOCOL.md','sha':'d69c21b73447f7ad9df0a3949b7fcaf57dd5ddde'},
  {'path':'STATUS.md','sha':'17758ee520428e2de34ad93e9d9c7548ea999a20'},
  {'path':'updates/2026-10-19/report.md'}, {'path':'evidence.jsonl'},
  {'path':'analyses/data_feasibility/2026-10-11-adult-audit.md'}],
 'queries':[
  '"PMC12710177"', '"The CM-aGPi Network" age NCT methods', '"NCT05371041"', '"NCT05371041" "Tourette" "Gomez"',
  '"Differentiating tic electrophysiology" "NCT"', '"Deep Learning for Automated Tic Detection" "2026"',
  '"Thalamocortical network activity enables" "NCT"', 'site:pmc.ncbi.nlm.nih.gov/articles/PMC10948908 "NCT02056873"',
  'site:pmc.ncbi.nlm.nih.gov/articles/PMC9468946 "NCT02056873"', '"Differentiating tic electrophysiology" Tourette 2020 subjects',
  '"10.1002/mds.70043" correction erratum retraction', '"PMC9468946" "Clinical"', '"PMC10948908" "NCT"', '"PMC4936504" "NCT"'],
 'date_filters':'None; exact historical paper/trial/cited-report audit, not new-publication surveillance.',
 'source_access':[
  {'url':paper,'status':'Full HTML accessible through web reader; direct urllib returned HTTP 403.'},
  {'url':'https://pmc.ncbi.nlm.nih.gov/articles/PMC12710177/','status':'Direct challenge; indexed primary full-methods text accessible.'},
  {'url':'https://doi.org/10.1002/mds.70043','status':'Initial web resolver error; publisher direct URL worked.'},
  {'url':registry,'status':'Web parser error; direct official API HTTP 200, selected metadata saved.'},
  {'url':protocol,'status':'Official PDF HTTP 200, 734930 bytes parsed in memory; source PDF not retained.'},
  {'url':sap,'status':'Official PDF HTTP 200, 32736 bytes parsed in memory; source PDF not retained.'},
  {'source':'Article supplement mds70043-sup-0001-FigureS1-S4-TableS1.docx','status':'Publisher link error; not retrieved.'}
 ],
 'licensing':'Main article identifies CC BY-NC-ND 4.0. Original analysis/factual metadata only; no article, figures, source tables or full-text copies stored.',
 'coverage_limits':['Exact prior-report overlap beyond trial-family membership is not identity-verified.','Supplement plots/table not inspected.','Notice search is not exhaustive.','No global novel-first claim.','Registry results are historical and outside October 20 new-window evidence.']
}
(P/'retrieval-log.json').write_text(json.dumps(log,indent=2,ensure_ascii=False)+'\n')
print('Wrote source matrix, evidence record, structured audit and retrieval log.')
