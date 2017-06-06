#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import redis

try:
    r=redis.Redis(host='192.168.0.24',port=6379,db=0)##如果设置了密码，就加上password=密码
    r.ping()
except redis.ConnectionError as rediserror:
    print rediserror
r.set('guo','shuai')#设置key
r.set('ni','hao')
keys=r.keys()#查询所有key
print keys
print r.dbsize()#查询库里面多少数据
print r.get('guo')#获取key值
# print "111111111111111"
# r.delete(*keys)
# print r.keys()
