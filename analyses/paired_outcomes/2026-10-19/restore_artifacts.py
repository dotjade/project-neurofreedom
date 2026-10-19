import hashlib,json
from pathlib import Path
r=Path(__file__).resolve().parent
m=json.loads((r/'artifact_parts/manifest.json').read_text())
for item in m['files']:
 data=b''.join((r/p).read_bytes() for p in item['parts'])
 assert len(data)==item['bytes'] and hashlib.sha256(data).hexdigest()==item['sha256'],item['path']
 (r/item['path']).write_bytes(data)
 print('Restored and hash-verified:',item['path'])
