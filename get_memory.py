#!/usr/bin/env python

import json
import sys

with open('/Users/foltran/Desktop/repo/automation/memory.json','r') as f:
    mem_dict = json.load(f)

with open('/etc/systctl.conf'):
    print(find("kernel.shmmax"))
    

mem_sum = 0
for sid in mem_dict:
    mem_sum += int(sid['sga_target'])

print('TOTAL(Bytes): ' + str(mem_sum*1024*1024))