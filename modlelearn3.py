#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#导入modlelearn2模块，并输出里面a的变量

#import直接具有属性的模块，from会获得文件变量的复本

import modlelearn2
print(modlelearn2.a)

from modlelearn2 import a,b,c
print(a,b,c)


#通过dir函数获得模块内部的可用的变量名的类别
print(dir(modlelearn2))