#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
http://httpbin.org/ #http协议测试网站
kamidox@gmail.com
Python Spider Basic

'''


import requests

def get_querysting():
    url='http://httpbin.org/get'
    params={'qs1':'value1','qs2':'value2'}
    headers={'x-headr1':'value1'}
    r=requests.get(url,params=params)
    #r=requests.get(url,headers=headers)
    print r.status_code
    print "=============="
    print r.headers
    print "=============="
    print r.content


if __name__=="__main__":
    get_querysting()