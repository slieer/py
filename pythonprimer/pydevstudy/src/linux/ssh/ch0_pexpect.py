#!/usr/bin/env python

#ssh_cmd_ver2.py
#coding:utf-8
import pexpect
def ssh_cmd(ip, user, passwd, cmd):
    ssh = pexpect.spawn('ssh %s@%s "%s"' % (user, ip, cmd))
    try:
        i = ssh.expect(['password: ', 'continue connecting (yes/no)?'])
        if i == 0 :
            ssh.sendline(passwd)
            r = ssh.read()
        elif i == 1:
            ssh.sendline('yes\n')
            ssh.expect('password: ')
            ssh.sendline(passwd)
            r = ssh.read()
            return r
    except pexpect.EOF:
        ssh.close()
 
hosts = '''
192.168.1.125:root:slieer:df -h,uptime
192.168.1.126:root:slieer:df -h,uptime
'''
 
for host in hosts.split("\n"):
    if host:
        ip, user, passwd, cmds = host.split(":")
        for cmd in cmds.split(","):
            print "-- %s run:%s --" % (ip, cmd)
            print ssh_cmd(ip, user, passwd, cmd)
