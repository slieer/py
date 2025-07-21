#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import paramiko

"""
一个Python实现的SSHv2协议的库，可以用于在远程服务器上执行命令、上传和下载文件等操作。
它使用了加密算法，可以提供安全的远程访问。
由于其简单易用的API和丰富的功能，Paramiko被广泛用于自动化运维和云计算等领域。

下载文件到本地
"""
ip=None 
port=0
username=None
passwd=None

def validateParam(): 
    if not (ip and port and username and passwd) :
        raise Exception("请设置ssh参数!")

def ssh2_download():
    validateParam();
    
    t = paramiko.Transport((ip, port))
    t.connect(username=username, password=passwd)
      
    sftp = paramiko.SFTPClient.from_transport(t)
    remotepath = '/var/log/system.log'
    localpath = '/tmp/system.log'
     
    sftp.get(remotepath, localpath)
    t.close()

"""
上传文件
"""
import traceback

def ssh2_upload(file, remotepath):
    validateParam()
    try: 
        t = paramiko.Transport((ip, port))
        t.connect(username = username, password = passwd)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(file,remotepath)
        t.close()
    except Exception as e:
        traceback.print_exc()
        
        
