'''
Created on 2012-10-3

@author: me
'''
import mysql.connector
from mysql.connector import errorcode
        
DB_NAME = 'break_promise'
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print(("Failed creating database: {}".format(err)))
        exit(1)

def exec_sql(cnx):
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
    exec_sql()
