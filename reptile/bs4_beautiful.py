#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import urllib2
from  bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

"""
它查找的是在所有内容中的第一个符合要求的标签
"""

soup=BeautifulSoup(html,"html.parser")

#soup=BeautifulSoup(open('index.html'))

#print soup.prettify()

# print soup.title
# print soup.head
# print soup.a
# print soup.p
# print soup.p.string

# for child in soup.body.children:
#     print child
#     print '==========='

#print soup.body.contents

for string in soup.strings:
    print repr(string)