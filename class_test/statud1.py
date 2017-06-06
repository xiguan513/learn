#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class MyObject(object):
    """This is test class"""
    def __init__(self):#初始化函数
        self.x=123

    def test(self):
        print "test method"

instance=MyObject()

# #判断MyObject类中是否有x，如果有为真，没有为假
# print hasattr(instance,'x')
#
# #如果没有x属性，设置此属性，如果类里面有此属性，覆盖重写
# setattr(instance,'x',19)
#
# print hasattr(instance,'x')
#
# #获取此属性的值
# print getattr(instance,'x')
#
# #判断test方法在类里面是否存在
# print hasattr(instance,'test')
# #获取test方法在里面的值
# getattr(instance,'test')()
#
# def ceshi():
#     print "This is ceshi"
# #类方法替换
# instance.test=ceshi
# instance.test()
#
# print hasattr(instance,"ceshi")

print MyObject.__class__
print MyObject.__doc__
print MyObject.__dict__
print MyObject.__module__
print MyObject.__name__


