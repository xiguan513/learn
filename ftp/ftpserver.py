#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import socketserver
import os

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            instrunction=self.request.recv(1024).strip()
            if not instrunction:break
