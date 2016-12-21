#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# def intersect(seq1,seq2):
#     res=[]
#     for x in seq1:
#         if x in seq2:
#             res.append(x)
#     return res
#
# # seq1="This"
# # seq2="That"
#
# seq1=[1,2,3]
# seq2=[3,4,5]
#
# print intersect(seq1,seq2)
#
#
# l=[x for x in seq1 if x in seq2]
# print l
def mysum(L):
    if not L:
        return 0
    else:
        print "====>",L[0]
        return L[0] + mysum(L[1:])

print mysum([1, 2, 3, 4, 5])

a=reduce(lambda x,y:x+y,[1,2,3,4,5])
print a

def fn(x,y):
    return x+y
print reduce(fn,[1,2,3,4,5])

num_list=range(10)
print filter(lambda x:x>=5,num_list)
