#!/usr/bin/env python
#-*-coding:utf-8-*-
import json

data = []
timestamp =[]
with open('raw.json') as f:
    for line in f:
       data.append(json.loads(line))
    f.close()


dic={}
for item in data:
    key=item['name']
    value_and_time=[item['time'],item['value']]
    if dic.has_key(key):
        dic[key].extend(value_and_time)
    else:
        dic[key]=[]

for key,value in sorted(dic.items()):
    print key,value

