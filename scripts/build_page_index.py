#!/usr/bin/env python3
from pathlib import Path
import json, re
root=Path(__file__).resolve().parents[1]
records=[]
for md in sorted((root/'docs').rglob('*.md')):
    rel=md.relative_to(root/'docs').as_posix()
    text=md.read_text(encoding='utf-8')
    title=md.stem
    if text.startswith('---'):
        fm=text.split('---',2)[1]
        m=re.search(r'^title:\s*"?([^"\n]+)"?',fm,re.M)
        if m: title=m.group(1)
    records.append({'title':title,'path':rel})
(root/'data/page_index.generated.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
print(f'Indexed {len(records)} docs pages.')
