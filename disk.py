#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import sys

disk_status=""
#file_name="1221.log"
file_name=sys.argv[1]
file=open(file_name)


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = "songbing513@163.com"
password = "%!#+513-1990bing"
to_addr = "songbing513@163.com"
smtp_server = "smtp.163.com"


for i in file.readlines():
    reip = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
    if reip.findall(i):
        disk_ip=reip.findall(i)[0]
        #print reip.findall(i)[0]
    else:
        disk_num=i.split()[-2]
        disk_fenqu=i.split()[-1]
        if disk_num.strip("%").isdigit():
            if int(disk_num.strip("%")) >= 70:
                disk_status+=disk_num + " " + disk_fenqu + " " + disk_ip+"\n"
            else:
                disk_status="磁盘使用正常"
else:
    msg = MIMEText(disk_status, 'plain', 'utf-8')
    msg['From'] = _format_addr(u'磁盘报警 <%s>' % from_addr)
    msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
    msg['Subject'] = Header(u'阿里服务器', 'utf-8').encode()
    server = smtplib.SMTP(smtp_server, 25)
    #server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()







