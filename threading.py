#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import threading
import time

def worker(num):
    time.sleep(1)
    print (num)
    return

for i in range(10):
    t=threading.Thread