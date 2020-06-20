'''
Created on 2011-9-16

@author: slieer
'''
import configparser

CONFIG_FILE = './xcapclient.ini'

def f() :
    cf = configparser.ConfigParser();
    cf.read(CONFIG_FILE)
    
    s = cf.sections()
    print('sections:', s)
    
    o = cf.options("Account")
    print("Account Options:",o)
    
    v = cf.items("Account")
    print("Account Items:",v)
    
    sip_addr = cf.get("Account", "sip_address")
    threads = cf.getint("concurrent", "thread")
    processors = cf.getint("concurrent", "processor")
    
    print("get section.item:", sip_addr, threads, processors)
    
    
    print('ini file modify test start:')
    cf.set("db", "db_pass", "zhaowei")
    cf.write(open(CONFIG_FILE, "w"))

if __name__ == '__main__':
    f()
    