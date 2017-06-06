#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#不用set集合方法，去除列表中的重复元素
List=['b','b','d','b','c','a','a','d','d','d','e']
# print "the list is:",List
# if List:
#     List.sort()#排序
#     print "排序以后输出： %s" % List
#     last=List[-1]#取最后一个值
#     print "输出list的长度",len(List)
#     for i in range(len(List)-2,-1,-1):#倒数的方法带入列表
#         print "输出i=",i
#         print "输出list对应的i的值：",List[i]
#         if last==List[i]:
#             del List[i]
#             print "删除以后的List",List
#         else:
#             last=List[i]
#             print "输出last的值", last
#
# print "after deleting the repreted element the list is :" ,List


# l2=[]
# [l2.append(i) for i in List if not i in l2]
# l2.sort()
# print l2

# import os
# dir="E:\s14\s14\python模块.md"
# print os.path.splitext(dir)
# print os.path.basename(dir)
# print os.path.dirname(dir)

# data = [(1,{'a':'A','b':'B','c':'C','d':'D'}),
#         (2,{'e':'E','f':'F','g':'G','h':'H',
#             'i':'I','j':'J','k':'K','l':'L'
#             }),
#         ]
#
# from pprint import pprint
# print "PRINT:"
# pprint(data)

# import uuid
#
# def get_mac_address():
#     mac=uuid.UUID(int=uuid.getnode()).hex[-12:]
#     return ":".join([mac[e:e+2] for e in range(0,11,2)])
# print get_mac_address()
#
# import socket
#
# myname=socket.getfqdn(socket.gethostname( ))
# myaddr=socket.gethostbyname(myname)
# print myname
# print myaddr


# def profile():
#     name="Dany"
#     age=30
#     return name,age
#
# profie_data=profile()
# print profie_data

# class MyClass(object):
#     __slots__=['name','identifier']
#     def __init__(self,name,identifier):
#         self.name=name
#         self.identifier=identifier


#from  collections import Counter
from collections import defaultdict
colours=(
    ('Yasoob','Yellow'),
    ('Ali','Blue'),
    ('Arham','Green'),
    ('Ali','Black'),
    ('Yasoob','Red'),
    ('Ahemd','Silver'),
)

# favs=Counter(name for name,colour in colours)
# print favs

# favourite_colours=defaultdict(list)#初始化字典valuse为空列表
# for name,colour in colours:
#
#     favourite_colours[name].append(colour)
#
# print favourite_colours
#
# for name,colour in colours:
#     print name,colour

# from collections import deque
# d=deque()
# d.append('1')
# d.append('2')
# d.append('3')
# print d


my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)