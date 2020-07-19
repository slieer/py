from flask import Flask, escape
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page!'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

def hello_world():
    return 'hello world'
app.add_url_rule('/', 'other-hello', hello_world)

if __name__ == '__main__':
    app.run(debug = True)
#run:
# env FLASK_APP=hello_flask.py flask run

#export FLASK_DEBUG=1
#export FLASK_APP=hello_flask.py 
#flask run --host=0.0.0.0