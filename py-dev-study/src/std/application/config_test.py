'''
Created on 2011-9-16

@author: slieer
'''
from distutils.command.config import config
import os
import configparser

CONFIG_FILE = os.getcwd() + '/py-dev-study/src/std/application/xcapclient.ini'


def f():
    iniConf = configparser.ConfigParser()
    file = open(CONFIG_FILE, mode='r')
    iniConf.read_file(file)

    sections = iniConf.sections()
    print('sections:', sections)

    options = iniConf.options("Account")
    print("Account Options:", options)
    items = iniConf.items("Account")
    print("Account Items:", items)

    sip_addr = iniConf.get("Account", "sip_address")
    iniConf['Account']['sip_address']
    threads = iniConf.getint("concurrent", "thread")
    processors = iniConf.getint("concurrent", "processor")

    print("get section.item:", sip_addr, threads, processors)

    print('ini file modify test start:')
    iniConf.set("db", "db_pass", "zhaowei")
    iniConf.write(open(CONFIG_FILE, "w"))


if __name__ == '__main__':
    f()
