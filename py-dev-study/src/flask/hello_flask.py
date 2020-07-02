from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Index Page!'

@app.route('/hello')
def hello():
    return 'Hello, World'
#run:
# env FLASK_APP=hello_flask.py flask run

#export FLASK_DEBUG=1
#export FLASK_APP=flask/hello_flask.py 
#flask run --host=0.0.0.0