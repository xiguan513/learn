#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import logging

# def foo(s):
#     n=int(s)
#     #断言如果条不成立报错退出
#     assert n!=0,'n is zero'
#     return 10/n
#
# print foo(0)

s='0'
n=int(s)
logging.info('n=%d' %n)
print 10/n