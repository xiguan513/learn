#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class SchoolMember(object):
    def __init__(self,schoolname,age):
        self.schoolname=schoolname
        self.age=age

    def tell(self):
        print "school name: %s" % (self.schoolname)

class Teacher(SchoolMember):
    #子类继承父类并重写新构造函数的时候，需要把父类的函数继承下来
    def __init__(self,schoolname,name,age,salary):
        #继承父类的属性
        SchoolMember.__init__(self,schoolname,age)
        #设置子类的构造属性
        self.name=name
        self.salary=salary
    #继承父类的方法并重写原来的方法
    def tell(self):
        #继承父类的方法
        SchoolMember.tell(self)
        print "My name is %s,age is %s salary is %s " % (self.name,self.age,self.salary)

class Student(SchoolMember):
    def __init__(self,schoolname,name,age,marks):
        SchoolMember.__init__(self,schoolname,age)
        self.name=name
        self.marks=marks

    def tell(self):
        SchoolMember.tell(self)
        print "My name is %s,age is %s marks is %s " % (self.name,self.age,self.marks)

t1=Teacher("北大","李老师",50,4000)
t1.tell()

print "---------------------"

s1=Student("北大","小明",24,1000)
s1.tell()
