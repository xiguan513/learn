#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import re
import urllib,urllib2

url = 'http://v.qq.com/x/list/movie'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
request=urllib2.Request(url,headers=headers)
response=urllib2.urlopen(request)
connect=response.read().decode('utf-8')

page=BeautifulSoup(connect,"html.parser")
for p in page.find_all("a"):
    p=str(p)
    p1=re.compile(r'<a.*paging_page_\d.*href=.*\;(?P<page_url>.*)">(?P<page_num>\d).*')
    if p1.search(p) is not None:
        print p1.search(p).group('page_url')
        print p1.search(p).group('page_num')
