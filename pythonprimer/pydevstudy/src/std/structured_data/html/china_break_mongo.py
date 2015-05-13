from pymongo import MongoClient
import json

__all__=['insert']

client = MongoClient('localhost', 27017)
#client = MongoClient('mongodb://localhost:27017/')
db = client.test
#db = client['test-database']

def insert(record):
    contentJson = json.loads(record)    
    db.data.insert_one(contentJson)

#import datetime
#print datetime.datetime.utcnow()
