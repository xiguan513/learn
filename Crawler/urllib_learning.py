#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import urllib2
import urllib
import urlparse

'''
urlopen(url, data, timeout)
    第一个参数url即为URL，第二个参数data是访问URL时要传送的数据，第三个timeout是设置超时时间。

    第二三个参数是可以不传送的，data默认为空None，timeout默认为 socket._GLOBAL_DEFAULT_TIMEOUT

    第一个参数URL是必须要传送的，在这个例子里面我们传送了百度的URL，执行urlopen方法之后，返回一个response对象，返回信息便保存在这里面。


print response.read()
response对象有一个read方法，可以返回获取到的网页内容。


类文件方法
    read()#读取所有，可以指定字节数作为参数
    readline()#返回每行
    readlines()#返回列表
    getcode()#获取直接code码
    info()#返回httplib.HTTPMessage实例
        msg.headers获取response headers 信息
        msg.items()
        msg.getheader('Content-Type')#获取单个信息

    urlretrieve(url,filename)#远程数据下载到本地
        参数说明：
        url：外部或者本地url
        filename：指定了保存到本地的路径（如果未指定该参数，urllib会生成一个临时文件来保存数据）；
        reporthook：是一个回调函数，当连接上服务器、以及相应的数据块传输完毕的时候会触发该回调。我们可以利用这个回调函数来显示当前的下载进度。
        data：指post到服务器的数据。该方法返回一个包含两个元素的元组(filename, headers)，filename表示保存到本地的路径，header表示服务器的响应头。
        urlretrieve(url, filename=None, reporthook=None, data=None)
        该函数可指定回调函数reporthook(blocknum, bs, size)，
        reporthook(当前传输的块数，块大小，数据总大小)#监控下载进度（三个参数）
        默认下载1024*8字节回调一次，也就是bs大小，blocknum是块数量，其实就是回调的次数，size是下载文件总大小

    urlencode()#将字典数据参数转换为url编码，对url参数进行编码，对post上的form数据进行编码
urlparse

    urlparse()#解析url的请求参数
    parse_qs#把url编码转换为字典数据parse_qs(result.query)字典形式显示

'''


def print_list(list):
    for i in list:
        print i

def demo():
    s=urllib.urlopen('http://blog.kamidox.com')
    # print s.getcode()
    # lines=s.readlines()
    # print_list(lines)
    # print s.read()
    # print s.read(100)
    msg=s.info()
    #print_list(msg.headers)
    #print_list(msg.items())
    print msg.getheader('Content-Type')

def progress(blk,blk_siz,total_size):
    print '%d/%d - %0.2f%%' % (blk*blk_siz,total_size,(float)(blk*blk_siz)*100/total_size)

def retrieve():
    fname,msg=urllib.urlretrieve('http://blog.kamidox.com','index.html',reporthook=progress)
    print fname#返回文件名
    print msg#返回头部信息


def urlencode():
    params={'score':100,'name':'爬虫基础','comment':'ver good'}
    qs=urllib.urlencode(params)
    print qs
    print urlparse.parse_qs(qs)

def pars_qs():
    url='https://www.baidu.com/s?wd=python&rsv_spt=1&rsv_iqid=0xbf1e2e3000006ab4&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=7&rsv_sug1=5&rsv_sug7=100&rsv_t=0018q6%2F2blQH5JW%2B2RGHbLabBasundFAk%2FAMWlqBpKqF2iObqI90xZ65Rr4Jfrv6ggJA&rsv_sug2=0&inputT=6380&rsv_sug4=8087&rsv_sug=2'
    result=urlparse.urlparse(url)
    print result
    params=urlparse.parse_qs(result.query)
    print params

if __name__=="__main__":
    pars_qs()