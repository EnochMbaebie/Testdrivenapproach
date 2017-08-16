import flask
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'the weather and football data files</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>the weather and football data files, %!</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)