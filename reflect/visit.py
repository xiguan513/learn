#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from reflect import commons

def run():
    inp=input("请输入您想访问页面的url: ").strip()
    if hasattr(commons,inp):
        func=getattr(commons,inp)
        func()
    else:
        print("404")

if __name__=="__main__":
    run()

#getattr函数的使用方法：它接收2个参数，前面的是一个对象或者模块，后面的是一个字符串，注意了！是个字符串！
#hasattr的内置函数，用于判断commons中是否具有某个成员
"""用户输入储存在inp中，这个inp就是个字符串，getattr函数让程序去commons这个模块里，寻找一个叫inp的成员（是叫，不是等于），
这个过程就相当于我们把一个字符串变成一个函数名的过程。然后，把获得的结果赋值给func这个变量，
实际上func就指向了commons里的某个函数。最后通过调用func函数，实现对commons里函数的调用。"""
