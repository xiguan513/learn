#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#定义三个变量模拟三个属性，通过modlelearn3文件导入模块的方法调用这三个属性
a='dead'
b='parrot'
c='sketch'

#如果print在这里，其他文件导入此文件的同时，也执行了次文件的所有内容包括输出print内容
#print(a,b,c)
if __name__ == '__main__':
    print(a,b,c)