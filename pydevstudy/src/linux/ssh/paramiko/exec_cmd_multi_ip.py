'''
Created on Jan 4, 2017

@author: zhai
'''
import paramiko
import threading

__all__ = ['ssh2']
"""
执行远远程命令
最好用root用户登录
"""
def ssh2(ip, username, passwd, cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username, passwd, timeout=5)
        for m in cmd:
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

"""
1.利用多线程，扫描局域局
"""
if __name__ == '__main__':
    cmd = ['cal', 'echo hello!']  # 你要执行的命令列表
    username = "root"  # 用户名
    passwd = "slieer"  # 密码
    threads = [2]  # 多线程
    print("Begin......")
    def scanIp() :
        for i in range(1, 254):
            ip = '192.168.1.' + str(i)
            a = threading.Thread(target=ssh2, args=(ip, username, passwd, cmd))
            a.start()
    def someIp():
        ips = [
               'serv1',
               'serv2',
               'serv3',
               'serv4'
               ]
        for ip in ips :
            a = threading.Thread(target=ssh2, args=(ip, username, passwd, cmd))
            a.start()
    someIp()