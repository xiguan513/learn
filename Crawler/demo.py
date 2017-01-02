#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import urllib2
import urllib

'''
urlopen(url, data, timeout)
第一个参数url即为URL，第二个参数data是访问URL时要传送的数据，第三个timeout是设置超时时间。

第二三个参数是可以不传送的，data默认为空None，timeout默认为 socket._GLOBAL_DEFAULT_TIMEOUT

第一个参数URL是必须要传送的，在这个例子里面我们传送了百度的URL，执行urlopen方法之后，返回一个response对象，返回信息便保存在这里面。


print response.read()
1
print response.read()
response对象有一个read方法，可以返回获取到的网页内容。


'''

# response=urllib2.urlopen("http://www.baidu.com")
# print response.read()

# request=urllib2.Request("http://www.baidu.com")
# response=urllib2.urlopen(request)
# print response.read()

values={"username":"songbing513@163.com","password":"1234@qwer"}
data=urllib.urlencode(values)
url="https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request=urllib2.Request(url,data)
response=urllib2.urlopen(request)
print response.read()