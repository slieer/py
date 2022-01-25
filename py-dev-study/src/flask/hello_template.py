from flask import render_template

from flask import Flask, escape
app = Flask(__name__)

@app.route('/hello-tpl/')
@app.route('/hello-tpl/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)