import MySQLdb as mdb
import sys
"""
http://zetcode.com/databases/mysqlpythontutorial/
"""
def conn():
    return mdb.connect(host="www.omscn.com", user="devuser", passwd="123456", db="test")
    
def query(db):
    try:    
        querySql = "SELECT * FROM test.t_field_entity"
        cursor = db.cursor()
        cursor.execute(querySql)
        rows = cursor.fetchall()
        
        for row in rows:
            print row
        
        cursor.close()
    
    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)

def insert(db):
    cursor = db.cursor()
    cursor.executemany(
          """INSERT INTO test (name, email,phone)
          VALUES (%s, %s, %s )""",
          [
          ("jia","j@cn","1" ),
          ("mie","m@cn","2" ),
          ("yan","y@cn","3" )
          ])
    cursor.close()
 
    
db = conn()
query(db)
#insert(db)
db.commit()
db.close()




