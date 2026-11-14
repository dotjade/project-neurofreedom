// Published-aggregate descriptive sensitivity; not patient data or simulation.
// Run with node fisher.mjs. Complete-pair n=51 is an assumption, not verified.
const n = 51;
const inputs = [{label:"MATS/impairment", r:0.40}, {label:"MATS/tic severity", r:0.12}];
const result = inputs.map(({label,r}) => {
 const z = Math.atanh(r), se = 1/Math.sqrt(n-3), h=1.959963984540054*se;
 return {label,r,n_assumed:n,low:Math.tanh(z-h),high:Math.tanh(z+h)};
});
if (!(result[0].low>0 && result[1].low<0 && result[1].high>0)) throw Error("Sign checks");
if (!(result[0].low<result[1].high)) throw Error("Intervals should overlap");
console.log(JSON.stringify({method:"Fisher z approximate 95% CI",result,assertions_passed:2},null,2));
