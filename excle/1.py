#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import xlrd
import dbconfig
import datetime

fname='4.xls'

#读取文件
bk=xlrd.open_workbook(fname,'rb')

#获取文件内表名称
name=bk.sheet_names()

#取第一个表
table=bk.sheet_by_name(name[0])

nrows=table.nrows


for i in range(nrows):
    dt=str(table.row_values(i)[2])
    dttime=datetime.datetime.strptime(dt, "%Y-%m-%d %H:%M")
    sql="insert into record (id,recordname,recordtime,recordnumber) VALUES (%s,'%s','%s','%s')" % ('null',table.row_values(i)[1], dttime,table.row_values(i)[0])
    dbinsert=dbconfig.mysql()
    dbinsert.insert(sql)









