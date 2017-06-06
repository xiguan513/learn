#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sqlite3

create="""
CREATE TABLE "record" (
"id"  integer PRIMARY KEY AUTOINCREMENT,
"recordname"  varchar(500) NOT NULL,
"recordtime"  varchar(200) NOT NULL,
"recordnumber"  int(200) NOT NULL
);
"""

class mysql(object):

    def __init__(self):
        self.conn=sqlite3.connect('record.db')
        self.cursor=self.conn.cursor()

    def mysql_conf(self,sql):
        self.cursor.execute(sql)


    def insert(self,sql):
        self.mysql_conf(sql)
        self.conn.commit()

    def __del__(self):
        self.cursor.close()
        self.cursor.close()

if __name__=="__main__":
    b=mysql()
    b.mysql_conf(create)

