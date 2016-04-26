# -*- coding: utf-8 -*-
__author__ = 'blfeng'

import  paramiko,os
class Ssh:
    def __init__(self,hostname,username,password,cmd1):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.cmd1 = cmd1
    def sshconnect(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(hostname=self.hostname,port=22,username=self.username,password=self.password,timeout=5)
            stdin,stdout,stderr = client.exec_command(self.cmd1)
            output_line = stdout.readlines()
            client.close()
        except:
            print("Connect %s failed") %(self.hostname)
            return 0
            client.close()
