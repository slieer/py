'''
Created on Dec 14, 2015

@author: zhai
'''
import unittest

import mysql.connector
from mysql.connector import errorcode
"""
the use_pure connection argument determines whether 
to connect using a pure Python interface to MySQL, 
or a C Extension that uses the MySQL C client library
"""

def create_conn():
    config = {
        'user': 'devuser',
        'password': '123456',
        'host': 'cent1',
        #'database': 'employees',
        'raise_on_warnings': True,
    }
    try:
        return mysql.connector.connect(**config)
                
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong your username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exists")
        else:
            print(err)
    else:
        pass
        ##cnx.close()

class Test(unittest.TestCase):
    def test_conn_db(self):
        cnx = create_conn()
        print cnx.get_server_info()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()