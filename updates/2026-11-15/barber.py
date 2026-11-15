"""Reproduce deterministic sensitivity using published Tables 3-5 p-values."""
import json
tables=[
[.091,.097,.230,.048,.136,.216,.005,.575,.017,.121,.715,.653,.848,.701,.662,.759,.261,.801,.197,.769,.142,.121,.715,.653],
[.363,.568,.358,.327,.799,.382,.988,.614,.257,.924,.870,.885,.215,.670,.218,.434,.414,.899,.013,.814,.087,.029,.052,.008],
[.009,.032,.016,.024,.025,.273,.816,.557,.733,.550,.366,.356,.629,.521,.870,.682]]
def audit(x):
    x=sorted(x)
    n=len(x)
    bh=min(p*n/i for i,p in enumerate(x,1))
    return dict(tests=n,nominal=sum(p<.05 for p in x),min_p=x[0],
                min_holm=min(1,round(n*x[0],4)),min_bh=round(bh,4))
print(json.dumps({str(i):audit(x) for i,x in zip([3,4,5,'all'],tables+[sum(tables,[])])},indent=2))
