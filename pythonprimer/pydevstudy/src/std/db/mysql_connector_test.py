'''
Created on 2012-10-3

@author: me
'''
import mysql.connector
from mysql.connector import errorcode
"""
the use_pure connection argument determines whether 
to connect using a pure Python interface to MySQL, 
or a C Extension that uses the MySQL C client library
"""

def connErrorTest():
    config = {
        'user': 'root',
        'password': 'slieer',
        'host': '127.0.0.1',
        #'database': 'employees',
        'raise_on_warnings': True,
    }
    try:
        cnx = mysql.connector.connect(**config)
        
        print cnx.get_server_info()
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong your username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exists")
        else:
            print(err)
    else:
        cnx.close()

DB_NAME = 'break_promise'
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)
        
def execSql(cnx):
    try:
        cursor = cnx.cursor()
        cnx.database = DB_NAME    
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor)
            cnx.database = DB_NAME
        else:
            print(err)
            exit(1)


if __name__ == '__main__':
    connErrorTest()
