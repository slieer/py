'''
Created on Jan 4, 2017

@author: zhai
'''
import sys
import paramiko
import threading
import select

from linux.ssh.paramiko import remote_cmd as cmd
"""
执行远远程命令
最好用root用户登录
"""

#http://www.cnblogs.com/leomo/p/5724909.html
def get_sql_log(host,port,user,password,key_words,out_put_filename):
    commond='cd crm-app/;./tailall.sh | grep %s' %key_words
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(host,port,user,password)
    transport=s.get_transport()
    channel = transport.open_session()
    channel.get_pty()
    channel.exec_command(commond)
    print('command %s', (commond))
    # print '%s' % (str(host))
    f=open(out_put_filename,'a+')
    # f.write(str(dir(s)))
    while 1:
        if channel.exit_status_ready():
            break
        try:
            rl,wl,xl= select.select([channel],[],[],1)
            #print rl
            if len(rl)>0:
                recv=channel.recv(65536)
                print(recv)
                #print recv
                #f.seek(2)
                f.write(str(recv))
                f.flush()

        except KeyboardInterrupt:
            print("Caught control-C")
            channel.send("\x03")#发送 ctrl+c
            channel.close()
            s.close()             
            exit(0)
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
            a = threading.Thread(target=cmd.ssh2, args=(ip, username, passwd, cmd))
            a.start()
    def someIp():
        ips = [
               'serv1',
               'serv2',
               'serv3',
               'serv4'
               ]
        for ip in ips :
            a = threading.Thread(target=cmd.ssh2, args=(ip, username, passwd, cmd))
            a.start()
    someIp()