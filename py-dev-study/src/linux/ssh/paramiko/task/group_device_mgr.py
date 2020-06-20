'''
Created on Jan 4, 2017

@author: zhai
'''

from linux.ssh.paramiko import remote_cmd as cmd
import threading

ip = 'serv1'
port = 22
username = 'root'
password = 'slieer'

def exec_cmd(serv_ip):
    cmd.ssh2(ip, username, password,['systemctl status wildfly.service'])
    cmd.ssh2(ip, username, password,['ip addr|grep inet'])


ips = ['serv1', 'serv2', 'serv3', 'serv4' ]
def updateSystem():
    for ip in ips :
        a = threading.Thread(target=cmd.ssh2, args=(ip, username, password, ["yum update -y"]))
        a.start()

if __name__ == '__main__':
    #exec_cmd(ip)
    updateSystem()