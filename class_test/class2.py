#!/usr/bin/env python
# -*- coding: UTF-8 -*-


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