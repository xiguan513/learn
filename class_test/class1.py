#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class statud(object):#新式类

    name='test'#公共属性外部可以修改，调用
    __age=18#私有属性外部不能修改，调用

    def __init__(self,sorce):#初始化函数，定义初始化属性
        self.__sorce_num=sorce

    def __sorce(self):#私有方法，不能被外部调用
        print("%s socre is %s" % (self.name,self.__sorce_num))

    def who(self):#共有方法，可以直接被外部调用
        print("I'm %s and my age is %d year old" % (self.name,self.__age))
        self.__sorce()

    @staticmethod#静态方法更改类方法变成一个普通函数
    def static():
        print("This is test static!")

    @classmethod#指定的方法都是类方法，类方法的第一个参数是类本身。在 Python 中，这个参数常被写作 cls
    def foo(cls):
        print("Call class methode foo")
        print("cls.__name__is",cls.__name__)


test=statud("60")
test.who()

test.name="ceshi"#修改内部属性
test.who()

lisa=statud("90")
lisa.name="lisa"#修改内部属性
lisa.who()
lisa.static()
lisa.foo()

print('======================================')

class Duck:
    def __init__(self,input_name):
        self.__name=input_name

    @property#把方法转为静态属性
    def name(self):
        print("inside the getter")
        return self.__name

    @name.setter
    def name(self,input_name):
        print('inside the setter')
        self.__name=input_name

fowl=Duck("howard")
#print(fowl.name)
fowl.name='Donald'
print(fowl.name)