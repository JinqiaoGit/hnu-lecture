from flask import Flask, render_template


app = Flask(__name__)


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/index/<string:name>')
def index2(name: str):
    return render_template('name.html', name=name)


if __name__ == '__main__':
    app.run()
