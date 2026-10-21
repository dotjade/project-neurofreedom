#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
root=Path(__file__).parent
m=json.loads((root/'registry-projected-metadata.json').read_text())
log={
 'date_utc':'2026-10-21','work_window_utc':'approximately 02:48–02:58',
 'scope':'Exact-trial aggregate metadata crosswalk, not new-publication surveillance or systematic review.',
 'repository_snapshot':'81feefe52fa1a401b01fd51ee8950a5e4de4a9ae',
 'repository_reads':['README.md','RESEARCH_PROTOCOL.md','STATUS.md: last completed daily update and next decision','evidence.jsonl: relevant NCT05371041/PMID40977255 entry','analyses/cm_agpi/2026-10-20/report.md','analyses/cm_agpi/2026-10-20/evidence-record.json','analyses/cm_agpi/2026-10-20/registry-selected-metadata.json','analyses/cm_agpi/2026-10-20/retrieval-log.json','RESEARCH_OVERVIEW.md','analyses/data_feasibility/2026-10-11-adult-audit.md','analyses/data_feasibility/2026-10-11-adult-matrix.json'],
 'date_filters':'None: fixed historical trial and linked reports.',
 'web_queries':[
 {'query':'"NCT05371041" "YGTSS"','domains':None},
 {'query':'"NCT05371041" "results" "2026"','domains':None},
 {'query':'"NCT05371041" stimulation "clinical outcomes" -site:clinicaltrials.gg -site:ichgcp.net -site:tundraspace.com -site:datalookout.com -site:trialx.com -site:centerwatch.com -site:plaintrial.com','domains':['pubmed.ncbi.nlm.nih.gov','pmc.ncbi.nlm.nih.gov','movementdisorders.onlinelibrary.wiley.com']},
 {'query':'"NCT05371041" "Month 9"','domains':['pubmed.ncbi.nlm.nih.gov','pmc.ncbi.nlm.nih.gov','movementdisorders.onlinelibrary.wiley.com','clinicaltrials.gov']},
 {'query':'"Defining targets for tic detection and suppression" "2025"','domains':['sciencedirect.com','brainstimjrnl.com','pubmed.ncbi.nlm.nih.gov']},
 {'query':'"NCT05371041" clinical outcome responder stimulation','domains':['pubmed.ncbi.nlm.nih.gov','pmc.ncbi.nlm.nih.gov','brainstimjrnl.com','medrxiv.org','biorxiv.org']},
 {'query':'"DEFINING TARGETS FOR TIC DETECTION" "Abstract"','domains':['brainstimjrnl.com','sciencedirect.com']},
 {'query':'"DEFINING TARGETS FOR TIC DETECTION" "10.1016"','domains':['brainstimjrnl.com','sciencedirect.com']},
 ],
 'source_units_fully_inspected_for_crosswalk':3,
 'included_sources':[
 {'url':m['source_url'],'request_url':m['request_url'],'http_status':200,'retrieved_utc':m['retrieved_utc'],'projected_response_sha256':m['projected_response_sha256'],'status':'Field-projected current official API; raw result classes not requested.'},
 {'url':'https://cdn.clinicaltrials.gov/large-docs/41/NCT05371041/Prot_000.pdf','http_status':200,'bytes':734930,'pages':27,'sha256':'52469442b6ec5c2f1e1e98ec0a1420d22d253d301eae14af81567a0fd0b9e7a9','status':'Direct official HTTP succeeded after web-reader failure; parsed in memory; source file and full text not saved.','locations_used':['pp.4–8: plan, response criterion, surgery/programming/calendar','p.13: YGTSS description','pp.19–22: assessment table and baseline footnote','pp.21,23: safety logging/monitoring']},
 {'url':'https://cdn.clinicaltrials.gov/large-docs/41/NCT05371041/SAP_001.pdf','http_status':200,'bytes':32736,'pages':2,'sha256':'dafd132f5aed539ae7de039e6d8506c320f11bc4ac31089350092c85618d8834','status':'Direct official HTTP succeeded after web-reader failure; parsed in memory; source file and full text not saved.','locations_used':['p.1: version date','p.2: general feasibility plan and manuscript-specific paragraph']},
 ],
 'discovery_only_not_effect_evidence':[
 {'id':'PMC12710177 / PMID40977255','reason':'Already audited physiology publication, not the current eight-person clinical endpoint aggregate.'},
 {'id':'PMC13051918 / 10.1016/j.prdoa.2026.100438','reason':'Mixed-trial video/EMG detection paper; search-hit methods did not provide the missing clinical aggregate estimator; no participant table inspected.'},
 {'id':'PMC13596655 / PMID42780243','reason':'Mixed-trial detection/prediction preprint, not independent clinical endpoint confirmation.'},
 {'id':'Brain Stimulation 18 (2025), pp.306–307, FS5E.6, title Defining Targets for Tic Detection and Suppression in Tourette Syndrome Deep Brain Stimulation','reason':'Search located title at page boundary in an adjacent abstract PDF; complete clinical abstract not verified and no efficacy claim extracted.'},
 {'id':'Third-party registry mirrors and secondary review search hits','reason':'Not used as primary evidence.'},
 ],
 'next_source_identity_verification':{'url':'https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?ids=PMC10948908&format=json','status':'ok','verified_on':'2026-10-21','pmcid':'PMC10948908','pmid':38499664,'doi':'10.1038/s41598-024-57071-5'},
 'privacy_incident_boundary':'Initial unrestricted exact-trial search unexpectedly displayed mirrored participant rows. No values copied into artifacts, analyzed, matched, pooled or reconstructed. Subsequent queries restricted to primary domains; official retrieval used server projection. No claim that no row was ever displayed.',
 'limitations':['Not a comprehensive linked-publication search or correction/retraction clearance.','No raw individual result classes inspected to infer aggregate absence; compatible estimator simply not established in inspected permitted metadata/documents.','No full conference abstract verified.','No actual individual follow-up times or stimulation histories obtained.','No inference of author error, invalidity, or no treatment benefit.'],
 'stopping_condition':'Compatible aggregate estimator and operational clock remain unestablished; fixed crosswalk closed without efficacy calculation.',
 'permissions':'No repository mutation, participant access request, outreach, purchase, or intervention.'
}
(root/'retrieval-log.json').write_text(json.dumps(log,indent=2,ensure_ascii=False)+'\n')
allowed=['report.md','structured-extraction.json','registry-projected-metadata.json','collect_registry_metadata.py','build_extraction.py','check_metadata.py','metadata-checks.json','evidence-record.json','evidence-record.jsonl','retrieval-log.json','README.md','finalize_artifacts.py']
manifest={'date':'2026-10-21','artifact_scope':'Original aggregate-only research extraction, safe projected metadata, acquisition/validation scripts and provenance.','allowlist':[],'excluded':'No source PDF, full text, individual results, event narratives or __pycache__ are part of the deliverable.'}
for name in allowed:
 p=root/name;b=p.read_bytes();manifest['allowlist'].append({'path':name,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
(root/'artifact-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Manifest includes',len(allowed),'allowlisted files; manifest itself additional.')
