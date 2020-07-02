from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
#run:
# env FLASK_APP=hello_flask.py flask run