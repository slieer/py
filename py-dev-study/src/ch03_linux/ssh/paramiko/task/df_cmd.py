'''
Created on 2016年12月23日

@author: Administrator
'''
import paramiko

import unittest

class Shell:
    def __init__(self):
        self.ip = "192.168.60.50"
        self.userName = "root"
        self.passwd = "dHie&tr#Ge"

    def command(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, 22, self.userName, self.passwd)
        stdin, stdout, stderr = ssh.exec_command("df -h")
        
        channel = stdout.channel
        status = channel.recv_exit_status()
        print(status)
        print(stdout.readlines())
        ssh.close()        

class Test(unittest.TestCase):
    def testCmd(self):
        s = Shell()
        s.command()
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()