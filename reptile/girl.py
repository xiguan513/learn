#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import os

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
all_url='http://www.mzitu.com/all'
start_html=requests.get(all_url,headers=headers)
#print(start_html.text)
Soup=BeautifulSoup(start_html.text,'lxml')
# li_list=Soup.find_all('li')
# for li in li_list:
#     print(li)
all_a=Soup.find('div',class_='all').find_all('a')
for a in all_a:
    title=a.get_text()
    href=a['href']
    print(title,href)
