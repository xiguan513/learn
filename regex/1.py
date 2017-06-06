#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

"""
group(num=0)	匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
groups()	返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
"""



m=re.match(r'.* (\w+)! (.*) .*','hello world! this test') #分组匹配
print m.group(1,2)


print "################"

print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配 #span 返回一个开始位置和结束位置组成的元组
print(re.match('.*b\.(.*)', 'www.runoob.com').group(1)) # 不在起始位置匹配


text = "This is a very beautiful girl, I like her very much."
print re.match("\w+\sis\sa\s(?P<status>.*)\sgirl,(.*)",text).group('status')

print "*******************"

print re.search('(\d{1,3}\.){3}\d{1,3}','1.2.1.100 test').group() #匹配ip地址

print "++++++++++++++++++++"

#(?P<groupname>) 为子模式命名
m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
print m.group(1)
print m.group(2)
print m.group()
print m.group('first_name')
print m.group('last_name')
print m.groupdict() #以字典模式返回
print m.groups()

print "================================"

exampleString = '''There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
never  is test .
Although never is often better than right now.'''

pattern=re.compile(r'(?<=\w\s)never(?=\s\w)')
matchResult=pattern.search(exampleString)
print matchResult.span()

pattern1=re.compile(r'(?<=\w\s)never')
matchResult1=pattern1.search(exampleString)
print matchResult1.span()

p=re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
print p.search('Paris in the the spring').group()




text='kitty kitty'
w=re.match(r'\b(?P<word>\w+)\b\s+(?P=word)',text)
print w.groupdict()
print w.group()
print w.group(1)


t='reading a book'
t1=re.search(r'(?<=\bre)\w+',t)
print t1.group()

t2='song test this'
t3=re.findall(r'(?<=\s)\w+',t2)
print t3

t3=re.search(r'(?<=\s)\w+',t2)
print t3.group()