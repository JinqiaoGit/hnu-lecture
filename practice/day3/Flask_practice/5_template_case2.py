from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index/<string:name>')
def index(name=None):
    return render_template('name.html', name=name)
