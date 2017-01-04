#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import paramiko

"""
下载文件到本地
"""
def ssh2_download(ip, port, username, passwd):
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
def ssh2_upload(ip, port, username, passwd):
    t = paramiko.Transport((ip, port))
    t.connect(username = username, password = passwd)
    sftp = paramiko.SFTPClient.from_transport(t)
    remotepath = '/var/log/system.log'
    localpath = '/tmp/system.log'
    sftp.put(localpath,remotepath)
    t.close()
