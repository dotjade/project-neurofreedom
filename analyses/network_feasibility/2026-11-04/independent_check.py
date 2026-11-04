"""Independent standard-library NIfTI byte/count verification, no imported audit code.
Usage: python independent_check.py /directory/with/three/maps
"""
import struct, math, hashlib, json, pathlib, sys, datetime, zipfile
ROOT=pathlib.Path(__file__).resolve().parent
folder=pathlib.Path(sys.argv[1]); inputs=json.loads((ROOT/'inputs.json').read_text()); results=json.loads((ROOT/'results.json').read_text()); checks=[]; details={}
def check(label,condition):
 if not condition: raise AssertionError(label)
 checks.append(label)
for item in inputs['files']:
 if not item['name'].endswith('.nii'):continue
 name=item['name'];b=(folder/name).read_bytes();reported=results['maps'][name]
 check(name+' SHA-256',hashlib.sha256(b).hexdigest()==item['sha256'])
 check(name+' bytes',len(b)==item['bytes'])
 check(name+' NIfTI-1 magic',b[344:348]==b'n+1\0' and struct.unpack('<i',b[:4])[0]==348)
 dims=struct.unpack('<8h',b[40:56]);check(name+' 3D positive shape',dims[0]==3 and all(d>0 for d in dims[1:4]));n=math.prod(dims[1:4]);code,bits=struct.unpack('<2h',b[70:74]);check(name+' float32 encoding',code==16 and bits==32)
 off=int(struct.unpack('<f',b[108:112])[0]);slope,inter=struct.unpack('<2f',b[112:120]);check(name+' payload exactly sized',len(b)-off==4*n)
 values=[x[0]*slope+inter for x in struct.iter_unpack('<f',b[off:])]
 counts={'finite':sum(math.isfinite(x) for x in values),'nan':sum(math.isnan(x) for x in values),'infinite':sum(math.isinf(x) for x in values),'positive':sum(x>0 for x in values),'negative':sum(x<0 for x in values),'zero':sum(x==0 for x in values),'voxel_count':len(values)}
 for key,v in counts.items():check(name+' '+key,reported[key]==v)
 finite=[x for x in values if math.isfinite(x)]
 check(name+' finite extrema',reported['finite_min']==min(finite) and reported['finite_max']==max(finite))
 check(name+' dimensions',reported['shape']==list(dims[1:4]))
 check(name+' millimeter spatial units',b[123]&7==2)
 pix=struct.unpack('<8f',b[76:108]);q=struct.unpack('<6f',b[256:280]);sr=struct.unpack('<12f',b[280:328]);qc,sc=struct.unpack('<2h',b[252:256])
 check(name+' qform/sform consistent for this quaternion',q==(0.,1.,0.,90.,-126.,-72.) and pix[:4]==(-1.,2.,2.,2.) and sr==(-2.,0.,0.,90.,0.,2.,0.,-126.,0.,0.,2.,-72.) and qc==sc==2)
 details[name]={'scaling_slope':slope,'scaling_intercept':inter,'spatial_units':'mm','qform_sform_agree':True,'independent_counts':counts}
check('prospective plan hash',hashlib.sha256((ROOT/'plan.md').read_bytes()).hexdigest()==inputs['plan_sha256'])
check('no specificity analysis claimed',results['spatial_specificity_test_executed'] is False)
check('no clinical validation claimed',results['clinical_target_validation'] is False)
check('full pipeline gate closed',results['full_published_pipeline_gate_passed'] is False)
report={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'passed':len(checks),'checks':checks,'method':'Independent stdlib struct.iter_unpack and Python math; does not import audit.py or execute external MATLAB code','details':details,'limitations':['Integrity and grid consistency do not prove registration or biological validity.','Group classification relies on paper provenance plus filenames; 3D shape alone is not a privacy test.','Code archive predates final publication and lacks an explicit final-version file-generation mapping.','No participant-level inputs or spatial specificity inference reviewed.']}
(ROOT/'independent-review.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':len(checks),'details':details},indent=2))
