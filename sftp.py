# -*- coding: utf-8 -*-
__author__ = 'blfeng'
import  sys,os
sys.path.append(os.getcwd()+'/lib')

import  paramiko,Sftp,string
import Ssh
import  FileMerge
import  shutil

def vip_authorized_keys(outfile,port):
    f=open("conf/hostname.txt")
    while True:
        host = f.readline()
        if host:
            ini_line = host.split(':',3)
            c = map(string.strip, ini_line)
            hostname=c[0]
            username=c[1]
            password=c[2]
            # sftp file to remote
            tp = paramiko.Transport((hostname,port))
            tp.connect(username=username,password=password)
            sftp = paramiko.SFTPClient.from_transport(tp)
            user = '~'+username
            targetfilename = os.path.expanduser(user)+"/.ssh/authorized_keys"
            sftp.put(outfile,targetfilename)
        else:
            break
    f.close()


def merge_authorized_keys(target_path,outfile):
    filemerge = FileMerge.FileMerge()
    filemerge.filemerge(fdir=target_path,outfile=outfile)


def authorized_keys_generate(port,remotepath,localpath,target_path):
    f=open("conf/hostname.txt")
    if os.path.exists(target_path):
        shutil.rmtree(target_path)
        os.mkdir(target_path)
    else:
        os.mkdir(target_path)
    while True:
        line = f.readline()
        if line:
            ini_line = line.split(':',3)
            c = map(string.strip, ini_line)
            hostname=c[0]
            username=c[1]
            password=c[2]
            # sftp file to remote
            s = Sftp.Sftp(hostname=hostname,username=username,password= password,port=port,localpath=localpath,remotepath=remotepath)
            s.sftpput()
            #remote gernerakey
            path = remotepath+"/"+localpath
            cmd1 = "/usr/bin/python /tmp/gernerRSAkey/gernerakey.py"
            ssh_file_path=os.path.expanduser('~')+"/"+".ssh"
            #ssh=Ssh.Ssh(hostname,username,password,cmd1,cmd2)
            ssh=Ssh.Ssh(hostname,username,password,cmd1)
            ssh.sshconnect()
            #copy remote authorized_keys
            user = '~'+username
            s = Sftp.Sftp(hostname=hostname,username=username,password= password,port=port,localpath=localpath,remotepath=remotepath)
            src = os.path.expanduser(user)+"/.ssh/authorized_keys"
            target =target_path+'/%s' % (hostname)
            s.sftpget(src,target)
        else:
            break
    f.close()




def main():


    outfile = '/tmp/sshkey/authorized_keys'
    port = 22
    remotepath = '/tmp'
    localpath = 'gernerRSAkey'
    target_path = '/tmp/sshkey/'
    outfile = '/tmp/sshkey/authorized_keys'

    #sftp get local path
    authorized_keys_generate(port=port,remotepath=remotepath,localpath=localpath,target_path=target_path)

    #generate total authorized_keys
    merge_authorized_keys(target_path=target_path,outfile=outfile)
    
    #vip authorized_keys to all hosts
    vip_authorized_keys(outfile=outfile,port=port)

if __name__=='__main__':
    main()

