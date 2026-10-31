"""SYNTHETIC analytical identification checks, not participant data or model fitting.
Python standard library only. Run: python check_identification.py
No random sampling: seed is not applicable. All invented inputs live here.
"""
import json, math
from pathlib import Path

def moments(mu_i, sd_i, mu_k, sd_k):
    variance = mu_i**2 * sd_k**2 + (mu_k**2 + sd_k**2) * sd_i**2
    return dict(mean=mu_i*mu_k, variance=variance,
                skewness=6*mu_i*mu_k*sd_i**2*sd_k**2/variance**1.5 if variance else 0)

def main():
    checks=[]
    def check(name, condition):
        assert condition, name
        checks.append(name)
    rows=[]
    # Shared memory contraction turns a divisive mean relation into a target offset.
    k=1.5; a=0.5; b=2/3
    for target in [1,1.5,2,2.5,3,3.5]:
        indirect=a+b*target; direct=k*indirect
        row=dict(target=target, indirect=indirect, direct=direct,
                 direct_minus_target=direct-target, direct_over_indirect=direct/indirect,
                 direct_minus_indirect=direct-indirect)
        rows.append(row)
        check(f'constant target offset {target}', math.isclose(direct-target,.75))
        check(f'divisive condition ratio {target}', math.isclose(direct/indirect,1.5))
    check('condition difference not constant', rows[0]['direct_minus_indirect'] != rows[-1]['direct_minus_indirect'])
    distribution=[]
    for mu_i in [1,2,3]:
        m=moments(mu_i,.3,1.5,.2)
        # Independently expand normal raw moments through order three.
        raw2=(mu_i**2+.3**2)*(1.5**2+.2**2)
        raw3=(mu_i**3+3*mu_i*.3**2)*(1.5**3+3*1.5*.2**2)
        variance=raw2-m['mean']**2
        skew=(raw3-3*m['mean']*raw2+2*m['mean']**3)/variance**1.5
        check(f'product variance {mu_i}',math.isclose(variance,m['variance'],abs_tol=1e-12))
        check(f'product skewness {mu_i}',math.isclose(skew,m['skewness'],abs_tol=1e-11))
        check(f'positive product skewness {mu_i}',m['skewness']>0)
        # Relabel K as an independent random response-calibration gain G.
        calibration=moments(mu_i,.3,1.5,.2)
        check(f'calibration observational equivalence {mu_i}',m==calibration)
        distribution.append(dict(indirect_mean=mu_i,divisive=m,calibration_only=calibration,
            subtractive=dict(mean=mu_i+.75,variance=.3**2+.2**2,skewness=0)))
    no_gain_noise=moments(2,.3,1.5,0)
    check('no gain noise zero skewness',no_gain_noise['skewness']==0)
    check('fixed gain scales variance',math.isclose(no_gain_noise['variance'],1.5**2*.3**2))
    # General deterministic ratio: D/I = (k_D/k_I)*(c_D/c_I)*(m_D/m_I).
    check('attenuation versus calibration mean alias',1.5/1*1/1*1/1 == 1/1*1.5/1*1/1)
    check('attenuation versus memory mean alias',1.5/1*1/1*1/1 == 1/1*1/1*1.5/1)
    # At fixed k, an absolute mean difference depends on memory scale.
    check('absolute contrast not scale free', (1.5-1)*1 != (1.5-1)*2)
    result=dict(label='SYNTHETIC ANALYTICAL EXAMPLES, NOT HUMAN OR TOURETTE DATA',
        seed=None,random_sampling=False,inputs=dict(targets=[1,1.5,2,2.5,3,3.5],memory_intercept=.5,
        memory_slope=2/3,mean_gain=1.5,gain_sd=.2,indirect_sd=.3,subtractive_offset=.75),
        memory_rows=rows,distribution_rows=distribution,checks=checks,checks_passed=len(checks))
    Path(__file__).with_name('synthetic-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(f'{len(checks)} checks passed')
if __name__=='__main__': main()
