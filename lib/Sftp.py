# -*- coding: utf-8 -*-
__author__ = 'blfeng'

import  paramiko,os

class Sftp():
    def __init__(self,hostname,port,username,password,localpath,remotepath):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.localpath = localpath
        self.remotepath = remotepath
    def sftpput(self):
        tp = paramiko.Transport((self.hostname,self.port))
        tp.connect(username=self.username,password=self.password)
        sftp = paramiko.SFTPClient.from_transport(tp)
        if os.path.exists(self.localpath):
            if os.path.isdir(self.localpath):
                remote_full_path = []
                dict={}
                for parent,dirnames,filenames in os.walk(self.localpath):
                    for filename in filenames:
                        remote_full_path.append(self.remotepath +"/"+parent)
                        dict[os.path.abspath('.')+"/"+os.path.join(parent,filename)]="%s" %(self.remotepath +"/"+parent+"/"+filename)   
                #mkdir remote dir
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(hostname=self.hostname,port=self.port,username=self.username,password=self.password,timeout=5)
                for p in remote_full_path:
                    cmd = 'mkdir -p %s' % (p)
                    client.exec_command(cmd)
                client.close()
                #sftp file to remote
                for file in  dict:
                    sftp.put(file,dict[file])      
            else:
                sftp.put(self.localpath,self.remotepath)
        else:
            print("localpath is not exist")
        tp.close()

    def sftpget(self,src,target):
        tp = paramiko.Transport((self.hostname,self.port))
        tp.connect(username=self.username,password=self.password)
        sftp = paramiko.SFTPClient.from_transport(tp)
        sftp.get(src,target)
        tp.close()




