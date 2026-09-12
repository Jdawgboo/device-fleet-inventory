"""Validate and summarize offline device inventory records."""
from __future__ import annotations
from collections import Counter
def summarize(records:list[dict])->dict:
 required={'id','model','firmware','health'};seen=set();errors=[]
 for index,row in enumerate(records):
  missing=required-set(row);errors.extend(f'row {index}: missing {key}' for key in sorted(missing));
  if row.get('id') in seen:errors.append(f'row {index}: duplicate id')
  seen.add(row.get('id'))
 return {'count':len(records),'models':dict(Counter(row.get('model','unknown') for row in records)),'health':dict(Counter(row.get('health','unknown') for row in records)),'errors':errors}
if __name__=='__main__':
 import json,sys;print(json.dumps(summarize(json.load(sys.stdin)),indent=2,sort_keys=True))
