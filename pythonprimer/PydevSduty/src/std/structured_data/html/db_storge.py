'''
Created on Apr 13, 2015

@author: dev
'''

import sqlite3

db_home = '/home/dev/Documents/db'
db_name = 'area_cn'
create = """
    create table area_cn (code integer primary key, name varchar(50)）
    """
insert = '''insert into area_cn values(?, ?)'''
  
class DbOp:
    def __init__(self, name):
        self.cx = sqlite3.connect(db_home + "/" + db_name + ".db")
    
    def createDb(self):
        self.cx.execute(create)
    
    def inert(self,code, name):
        self.cx.execute(insert, (code, name))
        self.cx.commit()
    
     
