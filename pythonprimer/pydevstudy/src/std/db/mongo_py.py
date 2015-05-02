'''
Created on May 7, 2015

@author: dev
'''
from pymongo import MongoClient
import datetime
from bson.objectid import ObjectId
from pymongo import ASCENDING, DESCENDING

client = MongoClient('localhost', 27017)
#client = MongoClient('mongodb://localhost:27017/')

db = client.test_database
#db = client['test-database']


collection = db.test_collection
#collection = db['test-collection']

print datetime.datetime.utcnow()

