#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def recv(maxsize,*,block):
    'Recevies a message'
    print(block)

#recv(1024,True)
recv(1024,block=True)