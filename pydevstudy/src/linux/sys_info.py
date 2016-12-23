# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Created on Apr 14, 2014
@author: root

内存信息的获取
获取 CPU 的信息
http://www.ibm.com/developerworks/cn/linux/1312_caojh_pythonlinux/
'''

from collections import OrderedDict


def CPUInfo():
    """Return the information if /proc/CPUinfo
    as a dictionary in the following format:
    CUP_info['pro0']={}
    
    """
    CPUinfo = OrderedDict()
    procinfo = OrderedDict()
    nprocs = 0
    with open('/proc/cpuinfo') as f:
        for line in f:
            tmp_str = line.strip()
            if not tmp_str:
                CPUinfo['proc%s' % nprocs] = procinfo
                nprocs = nprocs + 1
                
                procinfo = OrderedDict()
            else:
                line_arr = tmp_str.split(':')
                if len(line_arr) == 2 :
                    procinfo[line_arr[0].strip()] = line_arr[1].strip()
                else:
                    procinfo[line_arr[0].strip()] = ''
    return CPUinfo

def meminfo():
    '''
    Return the information in /proc/mominfo as a dictionary.
    '''
    meminfo = OrderedDict()
    with open('/proc/meminfo') as f:
        for line in f :
            arr = line.split(":")
            key = arr[0]
            value = arr[1].strip()
            meminfo[key] = value
    
     
    print('Total memory: {0}'.format(meminfo['MemTotal']))
    print('Free memory: {0}'.format(meminfo['MemFree']))
    return meminfo

if __name__ == '__main__' :
    CPUinfo = CPUInfo()
    for processor in list(CPUinfo.keys()):
        print(CPUinfo[processor]['model name'])

    meminfo()
