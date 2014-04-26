'''
Created on 2011-9-16

@author: slieer
'''
from application.configuration import ConfigFile, ConfigSection, ConfigSetting

CONFIG_FILE = './xcapclient.ini'


class Account(ConfigSection):
    sip_address = ''
    password = ConfigSetting(type=str, value=None)
    auth = ConfigSetting(type=str, value=None)
    xcap_root = ''

def f() :
    client_config = ConfigFile(CONFIG_FILE)
    acc = client_config.get_section("Account") 
    if acc is None:
        return None
    else:
        print acc
        return dict(Account)

if __name__ == '__main__':
    print f();
    