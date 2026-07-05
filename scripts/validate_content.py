#!/usr/bin/env python3
from pathlib import Path
import json, re, sys
root = Path(__file__).resolve().parents[1]
errors=[]
for md in (root/'docs').rglob('*.md'):
    text=md.read_text(encoding='utf-8')
    if text.startswith('---'):
        fm=text.split('---',2)[1]
        for field in ['title']:
            if f'{field}:' not in fm: errors.append(f'{md}: missing {field}')
    else:
        if md.name!='index.md': errors.append(f'{md}: missing frontmatter')
try:
    pages=json.loads((root/'data/pages.json').read_text(encoding='utf-8'))
    for p in pages:
        if not (root/'docs'/p['path']).exists(): errors.append(f"Missing page path: {p['path']}")
except Exception as e:
    errors.append(f'pages.json invalid: {e}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('Content validation passed.')
