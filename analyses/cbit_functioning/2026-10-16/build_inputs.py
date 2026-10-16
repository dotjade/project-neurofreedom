"""Transcribe published aggregate numeric facts into original structured inputs.
No full manuscript or participant records are saved. Source: PMC7190082 Tables 1-3.
"""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent
ids=['sds_total','sds_work','sds_social','sds_family','fam_iii','sas_overall','sas_occupation','sas_social_leisure','sas_extended_family','sas_primary_relationship','sas_parental_role','sas_family_unit']
names=['SDS total','SDS work','SDS social','SDS family','FAM-III short form','SAS-SR overall','SAS-SR primary occupation/role','SAS-SR social leisure','SAS-SR extended family','SAS-SR primary relationship','SAS-SR parental role','SAS-SR family unit']
def rows(data, cols):
 out=[]
 for i,line in enumerate(data.strip().splitlines()):
  vals=line.split('|');d={'id':ids[i],'measure':names[i],'direction':'lower is less disability or maladjustment'}
  for k,v in zip(cols,vals):
   v=v.strip()
   if k in ('f','p','partial_eta_squared'):d[k]=v
   else:
    m,se=v.split(',');d[k]={'mean':m,'se':se}
  out.append(d)
 return out
acute=rows('''8.36,0.90|5.00,0.79|8.32,0.97|5.79,0.85|0.56|.46|.01
2.78,0.35|1.56,0.30|2.32,0.37|1.76,0.32|2.04|.16|.02
3.07,0.38|2.11,0.31|3.58,0.40|2.05,0.33|1.69|.20|.02
2.51,0.36|1.33,0.28|2.42,0.38|1.98,0.30|2.29|.13|.02
25.51,0.97|24.73,0.97|26.83,1.02|25.54,1.02|0.20|.66|.002
1.83,0.06|1.71,0.06|1.87,0.06|1.83,0.06|1.71|.20|.02
1.83,0.13|1.68,0.12|1.75,0.14|1.65,0.12|0.15|.70|.002
2.01,0.08|1.95,0.08|2.14,0.09|1.96,0.08|1.22|.27|.01
1.63,0.06|1.49,0.06|1.68,0.06|1.67,0.06|2.10|.15|.02
1.76,0.11|1.65,0.11|1.92,0.10|1.97,0.10|1.47|.23|.04
1.15,0.22|1.35,0.26|1.78,0.17|1.67,0.19|0.82|.38|.06
1.84,0.14|1.58,0.13|1.78,0.16|1.69,0.14|1.07|.30|.01''',['cbit_baseline','cbit_post','pst_baseline','pst_post','f','p','partial_eta_squared'])
response=rows('''8.51,0.78|6.21,0.67|7.96,1.27|3.46,1.09|2.88|.09|.03
2.51,0.30|1.86,0.26|2.71,0.49|1.14,0.42|3.22|.08|.03
3.57,0.32|2.32,0.26|2.64,0.53|1.50,0.43|0.05|.83|<.001
2.43,0.31|1.95,0.24|2.61,0.50|0.82,0.39|5.67|.02|.05
26.49,0.82|25.92,0.81|24.92,1.38|22.76,1.36|1.54|.22|.02
1.89,0.05|1.81,0.05|1.76,0.08|1.67,0.08|0.06|.80|.001
1.88,0.11|1.71,0.10|1.57,0.18|1.55,0.16|0.93|.34|.01
2.12,0.07|1.97,0.06|1.94,0.11|1.90,0.10|0.65|.42|.01
1.69,0.05|1.62,0.05|1.55,0.08|1.48,0.08|0.01|.93|<.001
1.83,0.09|1.84,0.09|1.88,0.15|1.78,0.16|0.52|.48|.02
1.44,0.15|1.58,0.17|2.25,0.36|1.38,0.42|6.94|.02|.37
1.81,0.12|1.67,0.11|1.82,0.20|1.53,0.18|0.63|.43|.01''',['nonresponder_baseline','nonresponder_post','responder_baseline','responder_post','f','p','partial_eta_squared'])
followup=rows('''7.60,1.68|4.00,1.53|4.20,1.55|4.79|.03|.42
2.60,0.70|1.27,0.61|1.20,0.52|4.09|.04|.39
2.67,0.54|1.77,0.53|1.73,0.59|3.49|.06|.35
2.33,0.74|1.00,0.46|1.27,0.54|2.67|.11|.29
24.08,1.92|22.67,1.86|23.58,2.09|0.51|.61|.09
1.85,0.15|1.80,0.17|1.69,0.14|1.01|.40|.17
1.78,0.32|1.82,0.34|1.78,0.34|0.05|.95|.01
1.99,0.18|2.02,0.18|1.82,0.13|1.79|.21|.23
1.57,0.13|1.46,0.14|1.41,0.10|1.94|.19|.25
1.92,0.15|1.83,0.16|2.00,0.30|0.20|.83|.17
NA,NA|NA,NA|NA,NA|NA|NA|NA
1.52,0.24|1.39,0.17|1.48,0.25|0.21|.82|.04''',['baseline','post','month6','f','p','partial_eta_squared'])
for row in followup:
 if row['id']=='sas_parental_role':
  row.update(analysis_n=1,analysis_note='One participant with complete data; scores withheld from public aggregate artifact; no inferential test reported.')
  for k in ('f','p','partial_eta_squared'):row[k]=None
  for k in ('baseline','post','month6'):del row[k]
 else:row['analysis_n']=None
 for row_ in [row]:row_['baseline_post_significant_marker']=row['id'] in ['sds_total','sds_work'];row_['baseline_month6_significant_marker']=row['id']=='sds_work'
obj={'source':{'pmid':'31451122','pmcid':'PMC7190082','doi':'10.1017/S0033291719002150','url':'https://pmc.ncbi.nlm.nih.gov/articles/PMC7190082/','source_version':'NIH author manuscript','extraction_date':'2026-10-16'},'numeric_representation':'Numbers are strings to preserve printed precision. Means and SEs are labelled adjusted in the source. Null means not reported; no covariance or outcome-specific n is invented.','acute_randomized':acute,'acute_responder_association':response,'selected_cbit_followup':followup,'denominators':{'randomized_cbit':63,'randomized_pst':59,'figure_acute_analyzed_cbit':60,'figure_acute_analyzed_pst':53,'acute_completed_cbit':56,'acute_completed_pst':49,'response_groups_table_header':{'responders':28,'nonresponders':94},'cbit_followup_prose_and_figure':15,'pst_followup_prose':2,'pst_followup_figure':1,'figure_screened':172,'figure_excluded':60,'figure_randomized':122,'outcome_specific_n':'Not reported except Table 3 parental-role complete n=1.'},'pairwise_followup':{'sds_total_baseline_post_p':'.02','sds_total_baseline_month6_p':None,'sds_work_baseline_post_p':'.04','sds_work_baseline_month6_p':'.03','inattention_baseline_post_p':'>.99','inattention_baseline_month6_p':'.16','inattention_post_month6_p':'.03'},'multiplicity':'Exploratory outcome tests were uncorrected across outcomes. Paper reports Bonferroni correction for follow-up pairwise comparisons.'}
(ROOT/'aggregate_inputs.json').write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
print('Wrote 36 functional rows; 35 have reported inferential p-values.')
