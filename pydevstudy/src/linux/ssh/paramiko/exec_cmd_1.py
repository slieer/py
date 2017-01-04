'''
Created on Jan 4, 2017

@author: zhai
'''

from linux.ssh.paramiko import exec_cmd_multi_ip as cmd

ip = 'serv1'
port = 22
username = 'root'
password = 'slieer'

def exec_cmd(serv_ip):
    cmd.ssh2(ip, username, password,['systemctl status wildfly.service'])

if __name__ == '__main__':
    exec_cmd(ip)