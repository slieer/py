'''
Created on Feb 19, 2017

@author: zhai
'''
import sys
import paramiko

__all__ = ['ssh2']

def ssh2(ip, username, passwd, cmds):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username, passwd, timeout=5)
        for m in cmds:
            stdin, stdout, stderr = ssh.exec_command(m)
#           stdin.write("Y")   #简单交互，输入 ‘Y’
            out = stdout.readlines()
            # 屏幕输出
            for o in out:
                print(o, end=' ')
        print('%s\tOK\n' % (ip))
        ssh.close()
    except :
        print('%s\tError\n' % (ip))
        print(sys.exc_info())
