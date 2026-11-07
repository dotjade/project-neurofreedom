"""Integer denominator check of published aggregate percentages; not a model replication."""
import json,pathlib
from fractions import Fraction
P=pathlib.Path(__file__).parent
rows={name:{'reported_percent':v,'compatible_correct_counts_n55':[k for k in range(56) if round(100*k/55,1)==v],'compatible_correct_counts_n54':[k for k in range(55) if round(100*k/54,1)==v]} for name,v in [('DNN',74.1),('Embed-freeze',75.9),('Embed-partial',79.6),('Qwen3-VL',89.1)]}
out={'source':'https://ai.jmir.org/2026/1/e98782','source_location':'Table 2 and its common-n=55 footnote','method':'Exhaustive integer numerator enumeration using published n; ordinary nearest-tenth rounding. Exact ratios also retained.','reported_49_of_55':str(Fraction(49,55)),'rows':rows,'interpretation':'The three baseline accuracies do not map to any integer numerator over the stated 55 test clips at one-decimal rounding. They are compatible with 40, 41, and 43 correct out of 54. This is a consistency flag, not proof that n=54 was actually used. No predictions, missing clip, or corrected significance estimate was invented.','clinical_validation':False}
(P/'reported-arithmetic.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
