#!/usr/bin/env python3
"""Extract ONLY published numerical functioning rows from already retrieved PMC HTML.
No manuscript text/image is saved in the review deliverable directory.
Usage: python extract_independent.py /tmp/pmc.html
"""
import hashlib, json, re, sys
from html.parser import HTMLParser
from pathlib import Path

class Tables(HTMLParser):
    def __init__(self):
        super().__init__(); self.active=False; self.cells=[]; self.rows=[]; self.cell=None; self.tables=[]
    def handle_starttag(self,t,a):
        if t=='table': self.active=True; self.rows=[]
        if self.active and t=='tr': self.cells=[]
        if self.active and t in ('th','td'): self.cell=[]
    def handle_data(self,d):
        if self.cell is not None: self.cell.append(d)
    def handle_endtag(self,t):
        if t in ('td','th') and self.cell is not None:
            self.cells.append(' '.join(''.join(self.cell).split())); self.cell=None
        if t=='tr' and self.active: self.rows.append(self.cells)
        if t=='table': self.tables.append(self.rows); self.active=False

def cell(text):
    m=re.fullmatch(r'([0-9.]+)(?: \(([0-9.]+)\))?([abc]*)',text)
    assert m,text
    return {'mean':m[1], 'se':m[2], 'marker':m[3] or None}

def extract(html):
    p=Tables(); p.feed(html)
    assert len(p.tables)==3
    out={}
    groups=('acute_randomized','acute_responder_association','selected_cbit_followup')
    ids=('sds_total','sds_work','sds_social','sds_family','fam_iii','sas_overall','sas_occupation','sas_social_leisure','sas_extended_family','sas_relationship','sas_parental','sas_family_unit')
    columns=(('cbit_baseline','cbit_post','pst_baseline','pst_post'),('nonresponder_baseline','nonresponder_post','responder_baseline','responder_post'),('baseline','post','month6'))
    for index,(tab,group,cols) in enumerate(zip(p.tables,groups,columns)):
        start=next(i for i,r in enumerate(tab) if r==['Sheehan Disability Scale'])
        rows=[r for r in tab[start+1:] if len(r)==(8 if index<2 else 7)]
        assert len(rows)==12
        result=[]
        for key,row in zip(ids,rows):
            if index==2 and key=='sas_parental':
                result.append({'id':key,'source_label':'Parental Role','analysis_n':1,'f':None,'p':None,'partial_eta_squared':None,'scores_suppressed':True,'reason':'Single-participant row retained only as n=1, untested.'})
                continue
            result.append({'id':key,'source_label':row[0], **{k:cell(v) for k,v in zip(cols,row[1:])}, 'f':row[-3] or None,'p':row[-2] or None,'partial_eta_squared':row[-1] or None})
        out[group]=result
    return out

if __name__=='__main__':
    path=Path(sys.argv[1]); content=path.read_bytes(); out=extract(content.decode())
    out={'source':{'url':'https://pmc.ncbi.nlm.nih.gov/articles/PMC7190082/','access_route':'http://pmc.ncbi.nlm.nih.gov/articles/PMC7190082/','doi':'10.1017/S0033291719002150','pmid':'31451122','independent_retrieval_date':'2026-10-16','retrieved_html_sha256':hashlib.sha256(content).hexdigest()},**out}
    dest=Path(__file__).parent/'independent_inputs.json'; dest.write_text(json.dumps(out,indent=2)+'\n');print(dest)
