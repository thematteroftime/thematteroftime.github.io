#!/usr/bin/env python3
"""Build the English and Chinese GitHub Pages outputs from one template."""
from pathlib import Path
import html
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DATA_KEYS = ('research','projects','experience','education','recent','openTo','gallery','honors')
template = (ROOT/'src/page.html').read_text()
shell = (ROOT/'src/bundle.html').read_text()
# Both language links must enter the same release, even if an older page is cached.
version = hashlib.sha256((template + shell + (ROOT/'content/en.json').read_text() + (ROOT/'content/zh.json').read_text()).encode()).hexdigest()[:10]
for code, destination in (('en','index.html'), ('zh','zh.html')):
    content = json.loads((ROOT/'content'/f'{code}.json').read_text())
    ui = content['ui']
    values = {k:html.escape(str(v),quote=True) for k,v in ui.items()}
    values['heroName'] = ui['heroName']
    values['otherPage'] = ui['otherPage'] + '?v=' + version
    values['researchLabel'] = html.escape(ui['research'])
    values['recentLabel'] = html.escape(ui['recent'])
    values.update({k:json.dumps(content[k],ensure_ascii=False) for k in DATA_KEYS})
    values.update(experienceLabel=html.escape(ui['experience']),educationLabel=html.escape(ui['education']),openToLabel=html.escape(ui['openTo']),honorsLabel=html.escape(ui['honors']),workLabelJS=json.dumps(ui['selectedWork'],ensure_ascii=False),experienceLabelJS=json.dumps(ui['experience'],ensure_ascii=False))
    page=re.sub(r'@@(\w+)@@',lambda m:values[m[1]],template)
    output=shell.replace('@@PAGE_JSON@@',json.dumps(page,ensure_ascii=False).replace('</','<\\/'))
    output=output.replace('<html>','<html lang="'+ui['lang']+'">',1)
    output=re.sub(r'<title>.*?</title>','<title>'+html.escape(ui['title'])+'</title>',output,count=1)
    assert not re.search(r'@@\w+@@',output), 'Unresolved build token'
    (ROOT/destination).write_text(output)
    print(f'Built {destination}: {len(output.encode()):,} bytes')
