#!/bin/bash

service ntpd stop
if [ $? -eq 0 ];then
	/usr/sbin/ntpdate  pool.ntp.org
	/bin/systemctl start ntpd.service
fi

