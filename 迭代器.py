#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# def generator_function():
#     for i in range(10):
#         yield i
#
# for item in generator_function():
#     print(item)

# def fibon(n):
#     a=b=1
#     for i in range(n):
#         yield a
#         a,b=b,a+b
#
# for x in fibon(5):
#     print(x)

def fenerator_function():
    for i in range(3):
        yield i
gen=fenerator_function()
print(next(gen))
print("Output: 0")
print(next(gen))
print("Output: 1")
print(next(gen))
print("Output: 2")
print(next(gen))