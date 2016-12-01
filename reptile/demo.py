#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import urllib2

# response=urllib2.urlopen("http://www.baidu.com")
#
# print response.read()

# request=urllib2.Request("http://www.baidu.com")
# response=urllib2.urlopen(request)
# print response.read()

import urllib
values={"username":"songbing513@163.com","password":"1234@qwer"}
data=urllib.urlencode(values)
print data
url="https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request=urllib2.Request(url,data)
response=urllib2.urlopen(request)
print response.read()
