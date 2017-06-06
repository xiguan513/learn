#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
import os

bak_list=['E:\\ftp','E:\\11']
back_dir="E:\\backtest\\"
tar='C:\\Program Files\\2345Soft\\HaoZip\\'



def bakcup(file_com,file_list,back_dir):
    for dic in file_list:
        back_name=dic.split("\\")[1]
        time.sleep(2)
        #print(""""%sHaoZipC.exe" a -tzip %s%s%s.zip %s""" % (file_com,back_dir,back_name,time.strftime('%Y%m%d%H%M%S'),dic))
        os.system(""""%sHaoZipC.exe" a -tzip %s%s%s.zip %s""" % (file_com,back_dir,back_name,time.strftime('%Y%m%d%H%M%S'),dic))


bakcup(tar,bak_list,back_dir)