'''
Created on 2012-10-3

@author: me
'''
import mysql.connector
from mysql.connector import errorcode

def connTest():
    cnx = mysql.connector.connect(user='devuser', password='123456',
                                  host='www.omscn.com',
                                  database='test')
    print cnx.get_server_info()
    cnx.close()


def connErrorTest():
    try:
        cnx = mysql.connector.connect(user='scott',
                                    database='testt')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong your username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exists")
        else:
            print(err)
    else:
        cnx.close()
        
def connTest2():
        config = {
                  'user': 'scott',
                  ' password': 'tiger',
                  'host': '127.0.0.1',
                  'database': 'employees',
                  'raise_on_warnings': True,
        }
        cnx = mysql.connector.connect(**config)
        cnx.close()               

if __name__ == '__main__':
    connTest()
