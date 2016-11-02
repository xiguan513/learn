#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import socket
import os

class FtpClient(object):
    def __init__(self,host,port):
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect(host,port)


    def interactive(self,msg):
        while True:
            user_input=input(">>").strip()
            if len(user_input)==0:continue
            user_input=user_input.split()

            if hasattr(user_input[0]):
                func=getattr(user_input[0])
                func(user_input)
