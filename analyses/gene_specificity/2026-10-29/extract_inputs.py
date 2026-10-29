"""Optional re-extraction from the separately labelled Fig2 aggregate workbook, never the mixed supplement. Run with local workbook path. No network requests."""
import zipfile,xml.etree.ElementTree as E,json,hashlib,datetime,pathlib,sys
base=pathlib.Path(__file__).parent
f=pathlib.Path(sys.argv[1])
if hashlib.sha256(f.read_bytes()).hexdigest() != '265b43a939cdb3322e4282b23f788b7b17c1fc64e06593c58417cd585e956b63':
 raise ValueError('Not the verified standalone Fig2 workbook. Stop rather than inspect an unknown or mixed supplement.')
z=zipfile.ZipFile(f);ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
ss=[''.join(t.itertext()) for t in E.fromstring(z.read('xl/sharedStrings.xml'))]
def rows(sh):
 out=[]
 for r in E.fromstring(z.read(f'xl/worksheets/sheet{sh}.xml')).findall('.//m:row',ns):
  row={}
  for c in r:
   v=c.find('m:v',ns)
   if v is not None:row[''.join(x for x in c.get('r') if x.isalpha())]=ss[int(v.text)] if c.get('t')=='s' else v.text
  out.append(row)
 return out
sets={k:set() for k in ['hcOCD','hcCTD','hcOCDCTD']}
for r in rows(4)[1:]:
 for col,key in zip('ABC',sets):
  if r.get(col):sets[key].add(r[col])
union=set.union(*sets.values());bygene={r['A']:r for r in rows(3)[1:]}
records=[]
for g in sorted(union):
 r=bygene[g];records.append({'gene':g,**{k:g in v for k,v in sets.items()},'combined_q':r['B'],'combined_dnDam_count':int(r['F']),'published_combined_hc':int(r['G']),'published_combined_probable':int(r['H'])})
(base/'inputs.json').write_text(json.dumps({'source':'Wang2026 Source Data Fig.2','doi':'10.1038/s41593-026-02419-5','sheets':{'memberships':'Fig2d','combined_q_and_counts':'Fig2c'},'unit':'gene, never person or variant','records':records},indent=2)+'\n')
print(f'Extracted {len(records)} gene-level records')
(base/'source-checks.json').write_text(json.dumps({'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'main_url':'https://www.nature.com/articles/s41593-026-02419-5','source_data_fig2_url':'https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41593-026-02419-5/MediaObjects/41593_2026_2419_MOESM6_ESM.xlsx','source_data_fig2_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'source_data_fig2_bytes':len(f.read_bytes()),'source_scope':'Publisher labels standalone Fig2 statistical source data and gene sets. Read Fig2c and Fig2d only. Fig2c contains gene-level rows, q, counts, flags, chromosome; retained union36 and only relevant fields. No participant/variant IDs. Source workbook not copied into repository.','mixed_supplement_accessed':False,'source_data_fig3':'Standalone Fig3 inspected headers/first gene aggregate rows only. Not used in computation because plot decomposition is not unrestricted inferential Bayes factors.','limits':['Separate disorder q values and trio-only q not available in these selected standalone sheets.','No individual variant, pedigree or participant supplement was requested.','No independent-replication reanalysis.']},indent=2)+'\n')
