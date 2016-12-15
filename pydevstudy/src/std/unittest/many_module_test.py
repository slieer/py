'''
Created on 2012-11-4

@author: me
'''
import unittest

class Test(unittest.TestCase):
    def testTemplating(self):
        from string import Template
        t = Template('${village}folk send $$10 to $cause.')
        print t.substitute(village='Nottingham', cause='the ditch fund')
    
    def testLogging(self):
        import logging
        logging.debug('Debugging information')
        logging.info('Informational message')
        logging.warning('Warning:config file %s not found', 'server.conf')
        logging.error('Error occurred')
        logging.critical('Critical error -- shutting down')
 


if __name__ == "__main__":
    unittest.main()