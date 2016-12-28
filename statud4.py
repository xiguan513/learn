#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Peoper(object):
    "这是创建一个类的父类"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def saying(self):
        print "My name is %s and age is %s" % (self.name,self.age)


class man(Peoper):
    "Peoper的子类"
    #旧式类：继承方法
    def __init__(self,name,age,job):
        Peoper.__init__(self,name,age)
        self.job=job

class woman(Peoper):
    'Peoper的子类'
    #新式类：继承方法
    def __init__(self,name,age,job):
        super(woman,self).__init__(name,age)

