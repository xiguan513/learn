#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re
memlist=[]
file=open("mem.txt")
def mem_monitor(memlist):
    for i in file.readlines():
        i=i.strip("\n")
        memlist.append(i)

    for e in memlist:
        reip = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
        remem= re.compile(r'\d{3,5}')
        if reip.findall(e):
            memip=reip.findall(e)
        elif remem.findall(e):
            memsize=int(e)
            if memsize<600:
                return memsize

mem=mem_monitor(memlist)
print mem


