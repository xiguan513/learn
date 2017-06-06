#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import re


html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<a href="http://blog.csdn.net/watsy">watsy's blog</a>
"""

soup=BeautifulSoup(html,"html.parser")
#print soup.prettify()
# print soup.title
# print soup.body
#print soup.find_all("a")

# def blog_name():
#     for i in soup.find_all("a"):
#         i=str(i)
#         m=re.search(r'<a.*class=.*',i)
#         if m is None:
#             m1=re.search(r'.*">(.*)</a>.*',i,re.S)
#             return m1.group(1)

#print blog_name()


def blog_name():
    for i in soup.find_all("a"):
        i=str(i)
        m=re.compile(r'<a.*class=.*')
        if m.search(i) is None:
            m1=re.search(r'.*">(.*)</a>.*',i,re.S)
            return m1.group(1)

print blog_name()


# a='<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>'
# m=re.compile(r'<a.*class=.*')
# print m.search(a).group()

