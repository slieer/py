import sqlite3
from flask import g
from flask import Flask, escape
app = Flask(__name__)

DATABASE = '/home/zhaixiaobin/.superset/superset.db.bak~'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.route('/')
def index():
    cur = get_db().cursor()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
