#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import paramiko

"""
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
        
        
