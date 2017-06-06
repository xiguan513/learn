#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Student(object):
    "This is a Student class"

    count=0
    books=['1','2']
    def __init__(self,name,age):
        self.name=name
        self.age=age
    #@classmethod
    #@staticmethod
    def printClassAttr(self):
        print Student.count
        print Student.books
        print "Name: ",self.name

#Student.printClassAttr('1','2')
wilber=Student("Wilber",28)
wilber.printClassAttr()

