"""Check one reported F,p pair. No participant-level inference or source correction."""
from pathlib import Path
import json
import scipy
from scipy.stats import f
out={'scope':'Internal consistency check of printed aggregate statistic; no participant-level reanalysis.','source':'https://doi.org/10.1016/j.brat.2015.05.006','reported_F':5.59,'reported_df':[1,1167],'reported_p':'<.015','computed_upper_tail_p':float(f.sf(5.59,1,1167)),'scipy_version':scipy.__version__,'formula':'scipy.stats.f.sf(5.59,1,1167)','decision':'Mismatch retained; do not silently replace the source p-value. Cluster-adjusted inference not reconstructed.'}
assert .01822<out['computed_upper_tail_p']<.01824
(Path(__file__).resolve().parent/'statistical-consistency.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['computed_upper_tail_p'])
