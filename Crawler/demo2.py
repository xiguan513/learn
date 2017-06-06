#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import requests
#
# r=requests.get("https://unsplash.com")
#
# print(r.text)

#get有参数请求
# payload={'key1':'value1','key2':'value2'}
# r=requests.get('http://httpbin.org/get',params=payload)
# print(r.text)


#post有参数请求
payload={'key1':'value1','key2':'value2'}
r=requests.post('http://httpbin.org/post',data=payload)
print(r.text)