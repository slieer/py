#!/usr/bin/env python
# -*- coding: utf-8 -*-

ignore_file = ['.gitignore', '.project', '.settings', 'pom.xml']
file_ext = [".war"]

import os
def parse_dir(_dir):
    war_files = []
    for i in os.listdir(_dir):
        if i in ignore_file :
            continue;
            
        sub_dir = os.path.join(_dir, i)        
        target_dir = sub_dir + "/target"
        
        for file in os.listdir(target_dir):
            dir3_file = os.path.join(target_dir, file)
            if not os.path.isdir(dir3_file) :
                ext = os.path.splitext(dir3_file)[1]
                #print() 
                if ext in file_ext :
                    war_files.append(dir3_file)
        
    return war_files
        #if (os.path.splitext(sub_dir)[1] == "war"):
files = parse_dir('D:/devTools/workspace/car_ocean_server/car_ocean_platform')
print(files)

import linux.ssh.paramiko.file_download_upload as upload
upload.ip = "192.168.60.50"
upload.port = 22
upload.username = "root"
upload.passwd = "dHie&tr#Ge"

for f in files :
    #print('update file:%d', os.stat(f).st_size)
    #print("upload file:" + os.path.split(f)[1])
    remoteFile = os.path.join("/tmp/", os.path.split(f)[1])
    #print(remoteFile)  
    #upload.ssh2_upload(f, remoteFile)
    
from linux.ssh.paramiko import exec_cmd_multi_ip as cmd
cmd.ssh2(upload.ip, upload.username, upload.passwd, ['mv -f /tmp/*war /opt/wildfly/latest/standalone/deployments/'])
    