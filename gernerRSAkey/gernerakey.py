__author__ = 'blfeng'
import  sys
sys.path.append('/tmp/gernerRSAkey/lib')
import os,crypt,sys,paramiko,string
import Copyfile


def get_hostname_user():
    host = os.popen('hostname')
    hostname=host.read()
    user = os.popen('whoami')
    username = user.read()
    return  username.strip()+"@"+hostname.strip()


def gernerRSAkey(id_file,id_file_pub,):
    key = paramiko.RSAKey.generate(2048)
    key.write_private_key_file(id_file)
    file = open(id_file_pub,'w')
    file.write("ssh-rsa " +key.get_base64()+" "+get_hostname_user()+"\n")
    file.close()

def main():
    user_home_path = os.path.expanduser('~')
    id_path=user_home_path+"/.ssh"
    if not os.path.exists(id_path):
        os.mkdir(id_path)
    id_file = user_home_path+"/.ssh/id_rsa"
    id_file_pub =user_home_path+"/.ssh/id_rsa.pub"
    gernerRSAkey(id_file,id_file_pub)
    #copy id_rsa.pub to authorized_keys
    src = id_file_pub
    target = user_home_path+"/.ssh/authorized_keys"
    gernerRSAkey(id_file,id_file_pub)
    copyfile = Copyfile.Copyfile(src,target)
    copyfile.copyfile()


if __name__=='__main__':
    main()

