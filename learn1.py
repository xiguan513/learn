#!/usr/bin/env python
# -*- coding: UTF-8 -*-


#列表表达式
squares=[x**2 for x in [1,2,3,4,5]]
print(squares)

#代码语句
squares1=[]
for i in [1,2,3,4,5]:
    squares1.append(i**2)
print(squares1)

#map 和匿名函数 在Python3中map函数作为iterators展示
squares2=list(map(lambda x:x**2,[1,2,3,4,5]))
print(squares2)


#Python3中判断字典key只用get方法取消2中的has_key方法
#或者使用k in d 检查d中是否有键是k
dict={'name':'tom',
      'age':25,
      'job':'IT'
      }

print(dict)

if dict.get('name'):
    print("有")
else:
    print("没有")

print(dict.items())
print(dict.keys())

print(dict.get('ceshi'))

print('ceshi' in dict)

print("Name:%-10sAge:%-8dHeight:%-8.2f" % ("Aviad",25,1.8445) )