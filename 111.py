#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def ceshi():
    return ""

test=ceshi()

if test=="":
    print 111
else:
    print 222

import pickle

f=open("disk1.pkl")
d=pickle.load(f)
print d