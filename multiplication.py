#!/usr/bin/env python
# -*- coding: UTF-8 -*-


for i in range(1,10):
    print("i=",i)
    for j in range(1,i+1):
        #print(j)
        print("%sx%s=%s" % (j,i,j*i),end=" ")
    print("\n")



