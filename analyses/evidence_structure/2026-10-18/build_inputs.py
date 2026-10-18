"""Construct original aggregate coding table, not a participant dataset."""
import json
from pathlib import Path
P=Path(__file__).resolve().parent
sources={
 'online_results':{'url':'https://juser.fz-juelich.de/record/905141/files/jcm-11-00250-v4.pdf','doi':'10.3390/jcm11010250','pmid':'35011989','locations':'Methods 2.1 and 2.5; Results 3.1-3.4; Tables 3-4; Discussion'},
 'online_protocol':{'url':'https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2016.00119/pdf','doi':'10.3389/fpsyt.2016.00119','locations':'Study Design; Booster Sessions; Statistical Analysis'},
 'wilhelm_results':{'url':'https://jamanetwork.com/journals/jamapsychiatry/fullarticle/1307556','doi':'10.1001/archgenpsychiatry.2011.1528','pmid':'22868933','locations':'Trial Registration; Table 2; Table 4; Treatment durability'},
 'mcguire_results':{'url':'https://pmc.ncbi.nlm.nih.gov/articles/PMC7190082/','doi':'10.1017/S0033291719002150','pmid':'31451122','locations':'Methods Design/Participants/Analytic Plan; Tables 1-3'}
}
trials=[
 {'trial_id':'NCT02605902','randomized_allocations':161,'recruitment':'Germany, five centers, September 2016-February 2020','age_range':'18-62','adult_only':True,'independence_basis':'Different randomization, sites and recruitment period from NCT00231985','registry_url':'https://clinicaltrials.gov/study/NCT02605902'},
 {'trial_id':'NCT00231985','randomized_allocations':122,'recruitment':'United States, three centers, December 2005-May 2009','age_range':'16-69','adult_only':False,'independence_basis':'Same identifier, enrollment and recruitment explicitly reused in McGuire methods','registry_url':'https://clinicaltrials.gov/study/NCT00231985'}
]
reports=[
 {'report_id':'Haas2022','doi':sources['online_results']['doi'],'trial_id':'NCT02605902','source_id':'online_results','publication_years':[2022]},
 {'report_id':'Wilhelm2012','doi':sources['wilhelm_results']['doi'],'trial_id':'NCT00231985','source_id':'wilhelm_results','publication_years':[2012]},
 {'report_id':'McGuire2020','doi':sources['mcguire_results']['doi'],'trial_id':'NCT00231985','source_id':'mcguire_results','publication_years':[2019,2020]}
]
# A block is an accounting group, not an independent endpoint or evidence weight.
blocks=[
 {'id':'O_primary','report_id':'Haas2022','domain':'tic_severity','phase':'acute','role':'primary','comparison':'randomized','nominal_positive':False,'numeric_anchor':'V3 TTS: -1.28, CI -2.58 to 0.01, p=.053','source_ids':['online_results','online_protocol']},
 {'id':'O_later_tics','report_id':'Haas2022','domain':'tic_severity','phase':'followup','role':'exploratory','comparison':'randomized','nominal_positive':True,'numeric_anchor':'V4 p=.003; V5 p<.001','source_ids':['online_results']},
 {'id':'O_impairment','report_id':'Haas2022','domain':'impairment','phase':'acute_and_followup','role':'exploratory','comparison':'randomized','nominal_positive':True,'numeric_anchor':'V3/V4/V5 p=.019/.097/.005','source_ids':['online_results']},
 {'id':'O_qol','report_id':'Haas2022','domain':'disease_specific_qol','phase':'acute_and_followup','role':'exploratory','comparison':'randomized','nominal_positive':True,'numeric_anchor':'V3/V4/V5 p=.272/.002/.013','source_ids':['online_results']},
 {'id':'O_noninferiority','report_id':'Haas2022','domain':'tic_severity','phase':'acute','role':'gated_noninferiority','comparison':'randomized','nominal_positive':None,'hierarchy_gate_passed':False,'numeric_anchor':'Upper CI 2.96 is below margin 3; failed primary superiority gate','source_ids':['online_results','online_protocol']},
 {'id':'W_primary','report_id':'Wilhelm2012','domain':'tic_severity','phase':'acute','role':'primary','comparison':'randomized','nominal_positive':True,'numeric_anchor':'Week10 adjusted advantage 3.3, CI 1.4-5.2, p<.001','source_ids':['wilhelm_results']},
 {'id':'W_impairment','report_id':'Wilhelm2012','domain':'impairment','phase':'acute','role':'secondary','comparison':'randomized','nominal_positive':True,'numeric_anchor':'Week10 adjusted advantage 3.9, CI 0.5-7.2, p=.03; multiplicity unadjusted','source_ids':['wilhelm_results']},
 {'id':'W_maintenance','report_id':'Wilhelm2012','domain':'clinician_improvement','phase':'followup','role':'maintenance','comparison':'selected_responders','nominal_positive':None,'numeric_anchor':'Six-month response 12/15 returnees from 24 acute CBIT responders','source_ids':['wilhelm_results']},
 {'id':'M_randomized_function','report_id':'McGuire2020','domain':'function','phase':'acute','role':'secondary','comparison':'randomized','nominal_positive':False,'numeric_anchor':'0/12 functional contrasts p<.05; reported p=.13-.70','source_ids':['mcguire_results']},
 {'id':'M_response_function','report_id':'McGuire2020','domain':'function','phase':'acute','role':'association','comparison':'postrandomization_response','nominal_positive':True,'numeric_anchor':'2/12 functional associations nominally positive; both p=.02','source_ids':['mcguire_results']},
 {'id':'M_followup_function','report_id':'McGuire2020','domain':'function','phase':'followup','role':'exploratory','comparison':'selected_within_group','nominal_positive':True,'numeric_anchor':'2/11 omnibus time tests nominally positive; not two demonstrated six-month pairwise effects','source_ids':['mcguire_results']}
]
# Explicit follow-up evidence predicates; None is unverified, not observed absence.
followup_claims=[
 {'trial_id':'NCT02605902','functional_favorable_reported':True,'randomized_contrast_retained':True,'confirmatory_support':False,'cessation_of_platform_or_boosters_verified':False,'adult_only':True,'scope_note':'Exploratory QoL/impairment contrasts during continued platform access; missing-at-random model assumptions remain'},
 {'trial_id':'NCT00231985','functional_favorable_reported':True,'randomized_contrast_retained':False,'confirmatory_support':False,'cessation_of_platform_or_boosters_verified':None,'adult_only':False,'scope_note':'Selected returning acute responders; booster-inclusive program; exact continued practice/exposure not verified'}
]
data={'schema_version':1,'scope':'Three fixed reports; evidence-structure audit only','sources':sources,'trials':trials,'reports':reports,'inference_blocks':blocks,'followup_claims':followup_claims,'input_limit':'No single-participant cells, outcomes or private records; no source paper copies'}
(P/'aggregate_inputs.json').write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
