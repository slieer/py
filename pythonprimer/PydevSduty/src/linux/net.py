#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 2012-11-30
@author: slieer
'''

import sys
import urllib

class parameters:
    def __init__(self):
        from optparse import OptionParser, OptionGroup
        op = OptionParser(
            usage="usage: %prog -u URL -d DAYS -U USERNAME -P PASSWORD",\
            version="%prog, " + "%s" #%__revision__
        )

        op.add_option("-u", action="store", type="string", \
            dest="url", \
            help="URL of site to open"
        )

        op.add_option("-d", action="store", type="int", \
            dest="days", default=1, \
            help="erase days before"
        )

        op.add_option("-U", action="store", type="string", \
            dest="username", \
            help="username"
        )

        op.add_option("-P", action="store", type="string", \
            dest="password", \
            help="password"
        )

        self.op = op
        (self.options, self.args) = self.op.parse_args()
params = parameters()

if not params.options.url or \
    not params.options.username or \
    not params.options.password :
    params.op.print_help()
    sys.exit(1)

url = "%s/Control_Panel/Database/manage_pack?days:float=%d" % \
     (params.options.url, params.options.days)

class MyOpener(urllib.FancyURLopener):
    def get_user_passwd(self, host, realm, clear_cache=0):
        return params.options.username, params.options.password

def main():
    try:
        f = MyOpener().open(url).read()
        print "Successfully packed ZODB on host %s" % params.options.url
    except:
        print "Cannot open URL %s, aborted" % url
        raise

if __name__ == '__main__':
    main()
