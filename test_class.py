#!/usr/bin/env python
# -*- coding: UTF-8 -*-



class A(object):
    def save(self):
        print "save A"

class B(A):
    pass

class C(B):
    def save(self):
        print "save C"

class D(B,C):
    pass

test=D()
test.save()