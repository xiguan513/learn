#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class SchoolMember(object):
    def __init__(self,schoolname):
        self.schoolname=schoolname

    def tell(self):
        print "school name is : %s " % (self.schoolname)


class Tearch(SchoolMember):
    def __init__(self,schoolname,name,age,salary):
        super(Tearch,self).__init__(schoolname)
        self.name=name
        self.age=age
        self.salary=salary

    def tell(self):
        super(Tearch,self).tell()
        print "My name is %s age is %s salary %s" % (self.name,self.age,self.salary)

class Stdent(SchoolMember):
    def __init__(self,schoolname,name,age,marks):
        super(Stdent,self).__init__(schoolname)
        self.name=name
        self.age=age
        self.marks=marks

    def tell(self):
        super(Stdent,self).tell()
        print "My name is %s age %s marks %s " % (self.name,self.age,self.marks)



t1=Tearch("清华",'李教授',55,1000)
t1.tell()

print "----------------"

s1=Stdent("清华",'小明',24,200)
s1.tell()