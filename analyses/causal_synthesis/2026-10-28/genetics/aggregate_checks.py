#!/usr/bin/env python3
"""Deterministic arithmetic on published gene-set/sample counts, not patient data."""
import json,pathlib
P=pathlib.Path(__file__).resolve().parent
x=json.loads((P/'inputs.json').read_text())
r={'analysis':'published aggregate accounting; not simulation or clinical effect estimate','seed':None,'gene_sets':{'combined_high_confidence':x['combined_hc'],'union_high_confidence':x['union_hc'],'outside_combined_but_in_union':x['union_hc']-x['combined_hc'],'shared_bf_contribution_percent':100*x['shared_bf']/x['union_hc'],'contribution_partition_total':x['shared_bf']+x['ctd_only_bf']+x['ocd_only_bf']},'sequencing':{'total_probands':x['trio_probands']+x['singleton_probands'],'newly_sequenced_probands':x['new_trios']+x['new_singletons'],'previously_sequenced_probands':x['trio_probands']+x['singleton_probands']-x['new_trios']-x['new_singletons'],'previously_sequenced_percent':100*(x['trio_probands']+x['singleton_probands']-x['new_trios']-x['new_singletons'])/(x['trio_probands']+x['singleton_probands'])},'not_identified':['individual memberships','gene independence','independent replication','population penetrance','causal acute trigger','adult reversibility']}
assert r['gene_sets']['contribution_partition_total']==36
assert r['gene_sets']['outside_combined_but_in_union']==2
assert r['sequencing']['total_probands']==3964
assert r['sequencing']['newly_sequenced_probands']==1952
assert r['sequencing']['previously_sequenced_probands']==2012
assert r['sequencing']['newly_sequenced_probands']+r['sequencing']['previously_sequenced_probands']==3964
(P/'results.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
