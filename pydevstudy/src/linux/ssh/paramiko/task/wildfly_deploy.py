#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import linux.ssh.paramiko.file_download_upload as upload
from linux.ssh.paramiko import remote_cmd as cmd

java_code_path = 'D:/devTools/workspace/car_ocean_server/car_ocean_platform'
ignore_file = ['.gitignore', '.project', '.settings', 'pom.xml']
file_ext = [".war"]

class AutoDeploy:
    war_files = []
    
    def gitPull(self):
        os.chdir(java_code_path)
        os.system('git pull')
            
    def mvnInstall(self):
        os.chdir(java_code_path)
        os.system('mvn clean install')
    def scanDeployFiles(self, _dir):
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
                        self.war_files.append(dir3_file)
        """        
            #if (os.path.splitext(sub_dir)[1] == "war"):
        """
    def uploadDeployFile(self):         
        files = self.war_files;
        print(files)

        upload.ip = "192.168.60.50"
        upload.port = 22
        upload.username = "root"
        upload.passwd = "dHie&tr#Ge"
        
        for f in files :
            #print('update file:%d', os.stat(f).st_size)
            #print("upload file:" + os.path.split(f)[1])
            remoteFile = os.path.join("/tmp/", os.path.split(f)[1])  
            upload.ssh2_upload(f, remoteFile)
    def execDeploy(self):
        cmd.ssh2(upload.ip, upload.username, upload.passwd, ['mv -f /tmp/*war /opt/wildfly/latest/standalone/deployments/'])
        
if __name__ == '__main__':
    auto = AutoDeploy()
    
    auto.gitPull()
    auto.mvnInstall()
    
    auto.scanDeployFiles(java_code_path)
    auto.uploadDeployFile()
    auto.execDeploy()
    
    
