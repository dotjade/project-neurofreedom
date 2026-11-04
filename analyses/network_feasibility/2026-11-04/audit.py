"""Deterministic audit of explicitly licensed group maps, not patient biology.
Usage: python audit.py /path/to/three/maps
No automatic download, no third-party code execution, no random seed.
"""
import sys,json,pathlib,struct,hashlib
import numpy as np
HERE=pathlib.Path(__file__).resolve().parent

def read_nifti(path):
 b=path.read_bytes(); endian='<' if struct.unpack('<i',b[:4])[0]==348 else '>'
 assert struct.unpack(endian+'i',b[:4])[0]==348,'NIfTI-1 only'
 dims=struct.unpack(endian+'8h',b[40:56]);assert dims[0]==3,'Group-only 3D audit requires manual review of other dimensionalities'
 shape=dims[1:4];code,bitpix=struct.unpack(endian+'2h',b[70:74]); assert code in (16,64),'Float32/64 only'
 offset=int(struct.unpack(endian+'f',b[108:112])[0]);slope,inter=struct.unpack(endian+'2f',b[112:120]);
 arr=np.frombuffer(b,dtype=endian+('f4' if code==16 else 'f8'),offset=offset,count=int(np.prod(shape))).astype(float)
 if np.isfinite(slope) and slope!=0:arr=arr*slope+inter
 pix=struct.unpack(endian+'8f',b[76:108]);qcode,scode=struct.unpack(endian+'2h',b[252:256]);srow=np.array(struct.unpack(endian+'12f',b[280:328])).reshape(3,4)
 meta={'shape':list(shape),'voxel_sizes':list(pix[1:4]),'datatype_code':code,'bitpix':bitpix,'vox_offset':offset,'qform_code':qcode,'sform_code':scode,'srow':srow.tolist(),'file_bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'voxel_count':arr.size,'finite':int(np.isfinite(arr).sum()),'nan':int(np.isnan(arr).sum()),'infinite':int(np.isinf(arr).sum()),'positive':int((arr>0).sum()),'negative':int((arr<0).sum()),'zero':int((arr==0).sum()),'finite_min':float(np.nanmin(arr)),'finite_max':float(np.nanmax(arr))}
 return meta,arr

def audit(folder):
 inputs=json.loads((HERE/'inputs.json').read_text());out={};arrays={}
 for item in inputs['files']:
  if not item['name'].endswith('.nii'):continue
  m,a=read_nifti(folder/item['name']);assert m['sha256']==item['sha256'];assert m['file_bytes']==item['bytes'];out[item['name']]=m;arrays[item['name']]=a
 vals=list(out.values());same=all(m['shape']==vals[0]['shape'] and m['srow']==vals[0]['srow'] and m['voxel_sizes']==vals[0]['voxel_sizes'] for m in vals)
 return {'analysis_type':'Group-artifact integrity and structural feasibility audit; not clinical replication','seed':None,'maps':out,'same_header_grid':same,'group_files_integrity_gate_passed':True,'full_published_pipeline_gate_passed':False,'spatial_specificity_test_executed':False,'clinical_target_validation':False,'reason_for_pipeline_stop':'Master/R-map code requires participant-level outcomes and connectivity; atlas and provenance dependencies absent from inspected archive.'}
if __name__=='__main__':
 r=audit(pathlib.Path(sys.argv[1]));(HERE/'results.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
