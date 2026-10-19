#!/usr/bin/env python3
"""Bounded positive-control check for the documented ISRCTN public API.
Saves counts, selected bibliographic/status/date metadata, and provenance only.
"""
import datetime as dt,hashlib,json,pathlib,sys,urllib.parse,urllib.request,xml.etree.ElementTree as ET
out=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else '.')
entries=[]
for label,url in [('undated_positive_control','https://www.isrctn.com/api/query/format/default?'+urllib.parse.urlencode({'q':'Tourette','limit':1})),('saturn_direct','https://www.isrctn.com/api/trial/ISRCTN14910154/format/default')]:
    e={'label':label,'url':url,'started_utc':dt.datetime.now(dt.timezone.utc).isoformat()}
    try:
        with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'PublicEvidenceScan/1.0'}),timeout=30) as r:raw=r.read();e.update(status=r.status,bytes=len(raw),final_url=r.url,sha256=hashlib.sha256(raw).hexdigest())
        root=ET.fromstring(raw);e.update(root_tag=root.tag,root_attributes=root.attrib)
        allowed={'isrctn','title','scientificTitle','publicTitle','lastEdited','dateApplied','recruitmentStatus','trialStatus','registrationDate','dateAssigned','dateUpdated'}
        e['selected_nodes']=[{'tag':n.tag,'text':n.text,'attributes':n.attrib} for n in root.iter() if n.tag.rsplit('}',1)[-1] in allowed and (n.text or '').strip() not in ['Dr','Prof','Mrs','Mr','Ms']]
        e['tag_names']=sorted(set(n.tag for n in root.iter()))
    except Exception as x:e['error']=str(x)
    e['completed_utc']=dt.datetime.now(dt.timezone.utc).isoformat();entries.append(e)
(out/'isrctn-control.json').write_text(json.dumps(entries,indent=2)+'\n');print(json.dumps(entries))

